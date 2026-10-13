#!/usr/bin/env python3
"""
CLI Maestro de Consulta, Extracción y Descarga del Campus Virtual UNAD
Capacidades:
  - 'unad login': Inicio de sesión y captura autónoma de cookies.
  - 'unad cursos': Lista oficial de cursos matriculados y sus códigos.
  - 'unad tareas': Agenda de actividades pendientes, fechas de corte y puntos.
  - 'unad notas': Calificaciones y retroalimentaciones registradas.
  - 'unad momentos <curso>': Estructura pedagógica desglosada (Inicial, Intermedio, Final).
  - 'unad biblio <curso> [fase]': Referentes bibliográficos, libros, capítulos y enlaces.
  - 'unad descargar <curso> [fase]': Descarga automática de guías PDF y anexos DOCX.
  - 'unad leer-guia <pdf>': Lectura y resumen del contenido de una guía descargada.
  - 'unad aula <curso>': Acceso directo al aula Moodle.
"""

import sys
import os
import time
import json
import re
import argparse
import urllib.parse
import subprocess
import requests
from bs4 import BeautifulSoup

CHROME_BIN = "/opt/google/chrome/chrome"
SESSION_DIR = os.path.expanduser("~/.config/unad-session")
COOKIES_JSON = os.path.join(SESSION_DIR, "cookies.json")
COOKIE_TXT = os.path.join(SESSION_DIR, "cookie_header.txt")
UNAD_DOCS_DIR = os.path.expanduser("~/Documentos/UNAD")

CAMPUS_URL = "https://campus0b.unad.edu.co/campus/"
ACCESIT_URL = "https://campus0b.unad.edu.co/campus/accesit.php"
MISCURSOS_URL = "https://campus0b.unad.edu.co/campus/miscursos.php"
REDIRMD_URL = "https://campus0b.unad.edu.co/campus/redirmd.php"

DEFAULT_DOC = "1003882193"
DEFAULT_PASS = "Yeiny777@"

NOMBRES_MAP = {
    "100410": "Cálculo Diferencial",
    "40003": "Competencias Comunicativas",
    "213022": "Fundamentos de Programación",
    "900002": "Inglés A2",
    "204016": "Teoría de Sistemas en las Organizaciones"
}

HUMAN_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "es-419,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://campus0b.unad.edu.co/campus/accesit.php",
    "Connection": "keep-alive"
}


def get_human_session():
    if not os.path.isfile(COOKIES_JSON):
        print("❌ No hay cookies guardadas. Primero ejecuta: unad login")
        return None

    try:
        with open(COOKIES_JSON, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        s = requests.Session()
        s.headers.update(HUMAN_HEADERS)

        for c in cookies:
            s.cookies.set(
                c["name"],
                c["value"],
                domain=c.get("domain", ""),
                path=c.get("path", "/")
            )
        return s
    except Exception as e:
        print(f"⚠️ Error cargando cookies: {e}")
        return None


def fetch_miscursos_soup(session):
    res = session.get(MISCURSOS_URL, timeout=15)
    if res.status_code != 200 or "txtdoc" in res.text:
        print("⚠️ Sesión expirada o no válida. Ejecuta: unad login")
        return None
    return BeautifulSoup(res.text, "lxml")


def get_moodle_session(session, query):
    """Realiza el salto SSO dinámico a Moodle para un curso y retorna la sesión con soup."""
    soup = fetch_miscursos_soup(session)
    if not soup:
        return None

    tables = soup.find_all("table")
    target = None

    for btn in tables[0].find_all("button"):
        oc = btn.get("onclick", "")
        m = re.search(r"redirmd\((\d+),\s*(\d+),\s*(\d+),\s*(\d+)\)", oc)
        if m:
            cod = m.group(3)
            nom = NOMBRES_MAP.get(cod, "").lower()
            if query == cod or query in cod or query.lower() in nom:
                target = {
                    "codigo": cod,
                    "nombre": NOMBRES_MAP.get(cod, f"Curso {cod}"),
                    "r1": m.group(1),
                    "r2": m.group(2),
                    "r3": m.group(3),
                    "r4": m.group(4)
                }
                break

    if not target:
        print(f"❌ No se encontró ningún curso con el término '{query}'.")
        return None

    session.headers["Referer"] = MISCURSOS_URL
    res_token = session.post(REDIRMD_URL, data=target)
    soup_redir = BeautifulSoup(res_token.text, "lxml")
    form = soup_redir.find("form")
    if not form:
        print("❌ Error en la respuesta de redirección del campus.")
        return None

    moodle_login_url = form.get("action")
    post_data = {inp.get("name"): inp.get("value") for inp in form.find_all("input") if inp.get("name")}

    session.headers["Referer"] = REDIRMD_URL
    res_moodle = session.post(moodle_login_url, data=post_data, allow_redirects=True)
    soup_moodle = BeautifulSoup(res_moodle.text, "lxml")

    return {
        "session": session,
        "moodle_url": res_moodle.url,
        "soup": soup_moodle,
        "target": target
    }


def cmd_login(args):
    from playwright.sync_api import sync_playwright

    doc = args.doc or DEFAULT_DOC
    pwd = args.pwd or DEFAULT_PASS

    print(f"🚀 Iniciando login automático para documento: {doc}...")
    os.makedirs(SESSION_DIR, exist_ok=True)
    playwright_args = [
        "--no-first-run",
        "--no-default-browser-check",
        "--ozone-platform=wayland",
        "--enable-features=UseOzonePlatform",
        "--deny-permission-prompts",
    ]

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            SESSION_DIR,
            executable_path=CHROME_BIN,
            headless=True,
            args=playwright_args,
            permissions=["geolocation"],
            geolocation={"latitude": 4.6097, "longitude": -74.0817},
        )
        page = context.pages[0] if context.pages else context.new_page()

        page.goto(CAMPUS_URL)
        page.wait_for_timeout(2000)

        if "accesit" in page.url or page.locator("#txtdoc").count() == 0:
            print("🎉 ¡Sesión activa detectada (ACCESIT)! No requiere reingreso.")
        else:
            try:
                page.wait_for_selector("#txtdoc", timeout=8000)
                page.fill("#txtdoc", doc)
                page.fill("#txtpass", pwd)
                page.click("#cmdIngresa")

                for _ in range(6):
                    time.sleep(1)
                    if "accesit" in page.url or page.locator("#txtdoc").count() == 0:
                        break
            except Exception as e:
                print(f"ℹ️ Estado de navegación: {e}")

        cookies = context.cookies()
        with open(COOKIES_JSON, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=2)

        cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in cookies)
        with open(COOKIE_TXT, "w", encoding="utf-8") as f:
            f.write(cookie_str)

        context.close()
        print(f"\n✅ ¡{len(cookies)} cookies capturadas exitosamente!")


def cmd_cursos(args):
    session = get_human_session()
    if not session:
        return

    print("👤 Consultando cursos matriculados en Mis Cursos...")
    soup = fetch_miscursos_soup(session)
    if not soup:
        return

    tables = soup.find_all("table")
    if not tables:
        print("❌ No se encontraron tablas de cursos.")
        return

    cursos = []
    for btn in tables[0].find_all("button"):
        oc = btn.get("onclick", "")
        m = re.search(r"redirmd\((\d+),\s*(\d+),\s*(\d+),\s*(\d+)\)", oc)
        if m:
            cod = m.group(3)
            nombre = NOMBRES_MAP.get(cod, f"Curso {cod}")
            cursos.append({"codigo": cod, "nombre": nombre})

    print(f"\n🎓 Cursos Matriculados ({len(cursos)}):")
    print("═" * 65)
    for i, c in enumerate(cursos, 1):
        print(f" {i}. [{c['codigo']}] {c['nombre']}")
        print(f"    👉 Momentos y contenidos: unad momentos {c['codigo']}")
        print(f"    👉 Descargar guías/anexos: unad descargar {c['codigo']}")
    print("═" * 65)


def cmd_tareas(args):
    session = get_human_session()
    if not session:
        return

    print("⏰ Consultando actividades pendientes y fechas de entrega...")
    soup = fetch_miscursos_soup(session)
    if not soup:
        return

    tables = soup.find_all("table")
    if len(tables) < 4:
        print("❌ No se encontró la agenda.")
        return

    tabla_tareas = tables[3]
    filas = tabla_tareas.find_all("tr")

    print("\n📅 AGENDA DE ACTIVIDADES Y VENCIMIENTOS:")
    print("═" * 70)

    for r in filas:
        tds = [td.get_text(strip=True) for td in r.find_all(["td", "th"])]
        if not tds:
            continue
        if len(tds) >= 2 and tds[1].isdigit():
            print(f"\n📘 [{tds[1]}] {tds[0]}")
        elif len(tds) >= 4:
            actividad = tds[1]
            fecha = tds[2]
            puntos = tds[3]
            tipo = tds[4] if len(tds) > 4 else ""
            alerta = "🚨" if "hoy" in fecha.lower() else "⏳"
            print(f"   {alerta} {actividad}")
            print(f"      • Vencimiento: {fecha} | Puntos: {puntos} | {tipo}")
    print("═" * 70)


def cmd_notas(args):
    session = get_human_session()
    if not session:
        return

    print("📊 Consultando calificaciones registradas...")
    soup = fetch_miscursos_soup(session)
    if not soup:
        return

    tables = soup.find_all("table")
    if len(tables) < 5:
        print("❌ No se encontró la tabla de notas.")
        return

    filas = tables[4].find_all("tr")
    print("\n📋 HISTORIAL DE CALIFICACIONES:")
    print("═" * 70)
    for r in filas:
        tds = [td.get_text(strip=True) for td in r.find_all(["td", "th"])]
        if not tds:
            continue
        if len(tds) >= 2 and tds[1].isdigit():
            print(f"\n📘 [{tds[1]}] {tds[0]}")
        elif len(tds) >= 4:
            print(f"   ✅ {tds[1]}: {tds[3]} (Fecha: {tds[2]})")
    print("═" * 70)


def cmd_momentos(args):
    session = get_human_session()
    if not session:
        return

    mdata = get_moodle_session(session, args.curso)
    if not mdata:
        return

    soup = mdata["soup"]
    target = mdata["target"]
    titulo_curso = soup.title.get_text(strip=True) if soup.title else target["nombre"]

    print("\n" + "═" * 75)
    print(f"🎓 CURSO: [{target['codigo']}] {target['nombre']}")
    print(f"📘 Moodle: {titulo_curso}")
    print(f"🔗 Enlace directo: {mdata['moodle_url']}")
    print("═" * 75)

    sections = soup.select("li.section, div.section, .course-section")
    for sec in sections:
        sec_id = sec.get("id", "")
        title_el = sec.select_one(".sectionname, .section-title, h3, h4")
        title = title_el.get_text(strip=True) if title_el else "Sección general"

        # Categorizar por momento
        momento_tag = "📌"
        tl = title.lower()
        if "fase 1" in tl or "reto 1" in tl or "task 1" in tl or "inicial" in tl:
            momento_tag = "🟢 [MOMENTO INICIAL]"
        elif any(f in tl for f in ["fase 2", "fase 3", "fase 4", "reto 2", "reto 3", "reto 4", "task 2", "task 3", "task 4", "intermedio"]):
            momento_tag = "🟡 [MOMENTO INTERMEDIO]"
        elif "fase 5" in tl or "reto 5" in tl or "final" in tl or "poa" in tl:
            momento_tag = "🔴 [MOMENTO FINAL]"
        elif any(k in tl for k in ["presentación", "primeros pasos", "acompañamiento", "noticias", "syllabus"]):
            momento_tag = "ℹ️ [INFORMACIÓN INICIAL]"

        print(f"\n{momento_tag} {title} (ID: {sec_id})")
        print("─" * 60)

        activities = sec.select(".activity, .activity-item")
        for act in activities:
            a_el = act.select_one(".instancename, .activityname, a")
            if not a_el:
                continue
            name = a_el.get_text(strip=True)
            link = act.select_one("a")
            href = link.get("href", "") if link else ""

            # Determinar tipo
            icono = "•"
            if "resource" in href or "guía" in name.lower():
                icono = "📄 [GUÍA / RECURSO]"
            elif "page" in href and "bibliogr" in name.lower():
                icono = "📖 [BIBLIOGRAFÍA]"
            elif "url" in href or "recurso educativo" in name.lower():
                icono = "🌐 [OVI / DIAPOSITIVAS]"
            elif "forum" in href:
                icono = "💬 [FORO]"
            elif "assign" in href:
                icono = "📥 [ENTREGA TAREA]"
            elif "quiz" in href:
                icono = "📝 [CUESTIONARIO]"

            print(f"  {icono} {name}")
            if href:
                print(f"     🔗 {href}")


def cmd_biblio(args):
    session = get_human_session()
    if not session:
        return

    mdata = get_moodle_session(session, args.curso)
    if not mdata:
        return

    soup = mdata["soup"]
    target = mdata["target"]
    fase_filtro = args.fase.lower() if args.fase else None

    print(f"\n📚 REFERENTES BIBLIOGRÁFICOS DE: [{target['codigo']}] {target['nombre']}")
    print("═" * 75)

    # Buscar páginas de contenidos y referentes bibliográficos
    paginas_biblio = []
    for a in soup.find_all("a"):
        href = a.get("href", "")
        txt = a.get_text(strip=True)
        if "mod/page" in href and ("bibliogr" in txt.lower() or "referentes" in txt.lower() or "contenidos" in txt.lower()):
            if fase_filtro:
                if fase_filtro in txt.lower():
                    paginas_biblio.append((txt, href))
            else:
                paginas_biblio.append((txt, href))

    if not paginas_biblio:
        print("❌ No se encontraron páginas bibliográficas que coincidan con la búsqueda.")
        return

    for nom, url in paginas_biblio:
        print(f"\n📖 {nom}:")
        print("─" * 65)
        try:
            r = session.get(url, timeout=12)
            bs = BeautifulSoup(r.text, "lxml")
            content = bs.select_one(".box.generalbox, #region-main, main, .page-content")
            if content:
                for p in content.find_all(["p", "li"]):
                    t = p.get_text(" ", strip=True)
                    if t and len(t) > 25 and not any(ign in t.lower() for ign in ["universidad nacional", "todos los derechos"]):
                        print(f"  • {t}")
                        link = p.find("a")
                        if link and link.get("href"):
                            print(f"    🔗 Enlace de lectura: {link['href']}")
        except Exception as e:
            print(f"  ⚠️ Error al consultar página bibliográfica: {e}")
    print("═" * 75)


def cmd_descargar(args):
    session = get_human_session()
    if not session:
        return

    mdata = get_moodle_session(session, args.curso)
    if not mdata:
        return

    soup = mdata["soup"]
    target = mdata["target"]
    fase_filtro = args.fase.lower() if args.fase else None

    # Carpeta base para descargas del curso
    slug_curso = f"{target['codigo']}_{target['nombre'].replace(' ', '_')}"
    base_dest = os.path.join(UNAD_DOCS_DIR, slug_curso)
    os.makedirs(base_dest, exist_ok=True)

    print(f"\n📥 INICIANDO DESCARGA AUTOMÁTICA DE GUÍAS Y ANEXOS:")
    print(f"🎓 Curso: [{target['codigo']}] {target['nombre']}")
    print(f"📂 Carpeta destino: {base_dest}")
    print("═" * 70)

    # Buscar todos los recursos descargables
    recursos = []
    for a in soup.find_all("a"):
        href = a.get("href", "")
        txt = a.get_text(strip=True)
        if "mod/resource" in href:
            if fase_filtro:
                if fase_filtro in txt.lower():
                    recursos.append((txt, href))
            else:
                recursos.append((txt, href))

    if not recursos:
        print("❌ No se encontraron recursos descargables para los criterios dados.")
        return

    total_bajados = 0
    for nom_rec, url_rec in recursos:
        # Determinar subcarpeta (ej: Fase_1, Fase_2, General)
        subcarpeta = "General"
        m_fase = re.search(r"(fase\s*\d+|reto\s*\d+|task\s*\d+)", nom_rec.lower())
        if m_fase:
            subcarpeta = m_fase.group(1).replace(" ", "_").capitalize()

        folder_fase = os.path.join(base_dest, subcarpeta)
        os.makedirs(folder_fase, exist_ok=True)

        print(f"\n🔍 Inspeccionando recurso: {nom_rec}")
        try:
            r = session.get(url_rec, timeout=12)
            bs = BeautifulSoup(r.text, "lxml")
            archivos_en_recurso = []
            for el in bs.find_all(["a", "object", "iframe", "embed"]):
                link = el.get("href") or el.get("src") or el.get("data") or ""
                if "pluginfile.php" in link and any(ext in link.lower() for ext in [".pdf", ".docx", ".zip", ".pptx", ".xlsx"]):
                    raw_filename = link.split("/")[-1].split("?")[0]
                    clean_filename = urllib.parse.unquote(raw_filename)
                    if clean_filename not in archivos_en_recurso:
                        archivos_en_recurso.append(clean_filename)
                        dest_file = os.path.join(folder_fase, clean_filename)
                        print(f"  ⬇️ Descargando: {clean_filename}...")
                        fdata = session.get(link, timeout=20).content
                        with open(dest_file, "wb") as f:
                            f.write(fdata)
                        kb = round(len(fdata) / 1024, 1)
                        print(f"     ✅ Guardado ({kb} KB) en: {dest_file}")
                        total_bajados += 1
        except Exception as e:
            print(f"  ⚠️ Error descargando {nom_rec}: {e}")

    print("\n" + "═" * 70)
    print(f"🎉 Descarga finalizada: {total_bajados} archivo(s) guardados en:")
    print(f"   📁 {base_dest}")


def cmd_leer_guia(args):
    ruta = args.ruta
    # Si pasaron código y fase (ej: unad leer-guia 204016 fase_2)
    if not os.path.isfile(ruta):
        # Buscar en UNAD_DOCS_DIR
        query = ruta.lower()
        candidatos = []
        for root, dirs, files in os.walk(UNAD_DOCS_DIR):
            for f in files:
                if f.lower().endswith(".pdf") and (query in f.lower() or query in root.lower()):
                    candidatos.append(os.path.join(root, f))
        if candidatos:
            ruta = candidatos[0]
            print(f"📄 Archivo detectado: {ruta}")
        else:
            print(f"❌ No se encontró el archivo PDF: {args.ruta}")
            return

    print(f"\n📖 LEYENDO CONTENIDO DE LA GUÍA:")
    print(f"📄 {os.path.basename(ruta)}")
    print("═" * 75)

    try:
        proc = subprocess.run(["pdftotext", ruta, "-"], capture_output=True, text=True, check=True)
        lineas = proc.stdout.splitlines()

        # Extraer bloques clave (Descripción, pasos, entregables, rúbrica)
        mostrando = False
        contador = 0
        for l in lineas:
            txt = l.strip()
            if any(h in txt.lower() for h in ["descripción detallada", "la actividad consiste en", "evidencias de aprendizaje", "rúbrica de evaluación", "criterios de evaluación"]):
                print(f"\n📌 {txt}")
                mostrando = True
                contador = 0
            elif mostrando:
                if txt:
                    print(f"   {txt}")
                    contador += 1
                    if contador > 40:
                        mostrando = False
    except Exception as e:
        print(f"❌ Error al procesar PDF con pdftotext: {e}")


def cmd_correo(args):
    session = get_human_session()
    if not session:
        return

    mdata = get_moodle_session(session, args.curso)
    if not mdata:
        return

    target = mdata["target"]
    moodle_url = mdata["moodle_url"]
    cid = re.search(r"id=(\d+)", moodle_url).group(1)
    base_moodle = moodle_url.split("/course/")[0]
    mail_url = f"{base_moodle}/local/mail/view.php?t=inbox&c={cid}"
    r_mail = session.get(mail_url, timeout=12)

    m_key = re.search(r'\"sesskey\":\s*\"([^\"]+)\"', r_mail.text)
    if not m_key:
        print("❌ No se pudo extraer la clave de sesión de correo.")
        return
    sesskey = m_key.group(1)
    ajax_url = f"{base_moodle}/lib/ajax/service.php?sesskey={sesskey}"

    # Leer mensaje individual
    if args.id:
        mid = int(args.id)
        print(f"\n📖 LEYENDO CORREO [ID: {mid}]...")
        session.headers["Content-Type"] = "application/json"
        res_body = session.post(
            f"{ajax_url}&info=local_mail_get_message",
            json=[{
                "index": 0,
                "methodname": "local_mail_get_message",
                "args": {"messageid": mid}
            }],
            timeout=12
        ).json()

        if not res_body[0].get("error"):
            msg = res_body[0].get("data", {})
            print("═" * 75)
            print(f"📩 ASUNTO: {msg.get('subject')}")
            print(f"👤 DE: {msg.get('sender', {}).get('fullname')}")
            print(f"📅 FECHA: {msg.get('fulltime')}")
            print("═" * 75)
            body_text = BeautifulSoup(msg.get("content", ""), "lxml").get_text("\n", strip=True)
            print(body_text)
            print("═" * 75)
        else:
            print("❌ Error al obtener el mensaje.")
        return

    # Listar últimos correos del buzón
    print(f"\n📬 BUZÓN DE CORREO DEL CURSO: [{target['codigo']}] {target['nombre']}")
    print("═" * 75)

    session.headers["Content-Type"] = "application/json"
    res_list = session.post(
        f"{ajax_url}&info=local_mail_search_messages",
        json=[{
            "index": 0,
            "methodname": "local_mail_search_messages",
            "args": {
                "query": {
                    "courseid": int(cid),
                    "roles": ["to", "cc", "bcc"],
                    "draft": False,
                    "deleted": False
                },
                "offset": 0,
                "limit": 20
            }
        }],
        timeout=12
    ).json()

    if res_list[0].get("error"):
        print("❌ Error consultando el buzón de correo.")
        return

    mensajes = res_list[0].get("data", [])
    print(f"Total mensajes encontrados: {len(mensajes)}\n")
    for m in mensajes:
        mid = m.get("id")
        remitente = m.get("sender", {}).get("fullname", "Docente")
        fecha = m.get("shorttime", "")
        asunto = m.get("subject", "")
        unread = "🔹 [NO LEÍDO]" if m.get("unread") else "   "
        print(f"{unread} [ID: {mid}] {remitente} ({fecha})")
        print(f"      Asunto: {asunto}")

    print("\n💡 Para leer un mensaje completo: unad correo <curso> <id>")
    print("═" * 75)


def main():
    parser = argparse.ArgumentParser(description="CLI Maestro de Campus Virtual UNAD (Extracción y Descarga)")
    subparsers = parser.add_subparsers(dest="command")

    # Login
    p_login = subparsers.add_parser("login", help="Login directo y captura de cookies")
    p_login.add_argument("--doc", help="Número de documento")
    p_login.add_argument("--pwd", help="Contraseña")

    # Resumen general
    subparsers.add_parser("cursos", help="Ver cursos matriculados")
    subparsers.add_parser("tareas", help="Agenda de tareas y fechas de entrega")
    subparsers.add_parser("notas", help="Historial de calificaciones")

    # Estructura pedagógica detallada (Momentos, Bibliografía, Descargas)
    p_momentos = subparsers.add_parser("momentos", help="Estructura por momentos pedagógicos (Inicial, Intermedio, Final)")
    p_momentos.add_argument("curso", help="Código o nombre del curso")

    p_biblio = subparsers.add_parser("biblio", help="Extraer bibliografía, libros y lecturas recomendadas")
    p_biblio.add_argument("curso", help="Código o nombre del curso")
    p_biblio.add_argument("fase", nargs="?", help="Filtro opcional de fase (ej: fase 2, reto 1)")

    p_descargar = subparsers.add_parser("descargar", help="Descargar automáticamente guías PDF y anexos DOCX/ZIP")
    p_descargar.add_argument("curso", help="Código o nombre del curso")
    p_descargar.add_argument("fase", nargs="?", help="Fase específica (opcional, ej: fase 2)")

    p_leer_guia = subparsers.add_parser("leer-guia", help="Leer y resumir los requerimientos de una guía PDF")
    p_leer_guia.add_argument("ruta", help="Ruta al PDF o término de búsqueda (ej: 204016, fase 2)")

    # Correo interno de los profesores
    p_correo = subparsers.add_parser("correo", help="Buzón de correo interno de los profesores en el curso")
    p_correo.add_argument("curso", help="Código o nombre del curso")
    p_correo.add_argument("id", nargs="?", help="ID opcional del mensaje para leerlo completo")

    args = parser.parse_args()

    if args.command == "login":
        cmd_login(args)
    elif args.command == "cursos":
        cmd_cursos(args)
    elif args.command == "tareas":
        cmd_tareas(args)
    elif args.command == "notas":
        cmd_notas(args)
    elif args.command == "momentos":
        cmd_momentos(args)
    elif args.command == "biblio":
        cmd_biblio(args)
    elif args.command == "descargar":
        cmd_descargar(args)
    elif args.command == "leer-guia":
        cmd_leer_guia(args)
    elif args.command == "correo":
        cmd_correo(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

