#!/usr/bin/env python3
"""
Scraper avanzado de Prompts de Claude Opus 5.5 desde YouMind (https://youmind.com/es-419/opus-5-5-prompts)
- Utiliza curl_cffi para bypass de protecciones TLS/Cloudflare (impersonate='chrome120').
- Decodifica el stream RSC (React Server Components / Next.js Flight Stream) para extraer prompts completos sin cortes.
- Crawlea enlaces relacionados en profundidad para compilar una biblioteca completa.
- Exporta en JSON, Excel (.xlsx con openpyxl) y Markdown estructurado.
"""

import os
import sys
import json
import re
import time
from urllib.parse import urljoin
from curl_cffi import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_URL = "https://youmind.com"
OUTPUT_DIR = "/home/rootkit/Proyectos/youmind-opus-prompts"

SEEDS = [
    "https://youmind.com/es-419/opus-5-5-prompts",
    "https://youmind.com/es-419/opus-5-5-prompts/explore",
    "https://youmind.com/es-419/opus-5-5-prompts/explore?sortBy=views&sortOrder=desc",
    "https://youmind.com/es-419/opus-5-5-prompts/explore?sortBy=likes&sortOrder=desc",
    "https://youmind.com/es-419/opus-5-5-prompts/explore?sortBy=newest&sortOrder=desc",
]

def parse_flight_stream(html):
    """Extrae chunks y mapea referencias textuales T<hex_len> del stream Next.js Flight."""
    soup = BeautifulSoup(html, "lxml")
    chunks = []
    for s in soup.find_all("script"):
        content = s.string or ""
        for m in re.finditer(r"self\.__next_f\.push\(\[\d+,\s*\"((?:[^\"\\]|\\.)*)\"\]\)", content):
            try:
                val = json.loads("\"" + m.group(1) + "\"")
                chunks.append(val)
            except Exception:
                pass

    text_table = {}
    for i, c in enumerate(chunks):
        m = re.match(r"^([0-9a-fA-F]+):T([0-9a-fA-F]+),(.*)$", c, re.DOTALL)
        if m:
            cid = m.group(1)
            expected_len = int(m.group(2), 16)
            content = m.group(3)
            j = i + 1
            while len(content.encode("utf-8")) < expected_len and j < len(chunks):
                next_c = chunks[j]
                if re.match(r"^[0-9a-fA-F]+:", next_c):
                    break
                content += next_c
                j += 1
            text_table[cid] = content

    full_text = "".join(chunks)
    return text_table, full_text, soup

def extract_prompts(full_text, text_table):
    """Extrae objetos de prompt desde el texto plano reconstruido de Next.js."""
    prompts = {}
    for m in re.finditer(r"\{\"id\":(\d+),\"title\":\"([^\"]+)\"", full_text):
        start = m.start()
        depth = 0
        end = -1
        for idx in range(start, min(len(full_text), start + 16000)):
            if full_text[idx] == "{":
                depth += 1
            elif full_text[idx] == "}":
                depth -= 1
                if depth == 0:
                    end = idx + 1
                    break
        if end != -1:
            sub = full_text[start:end]
            try:
                obj = json.loads(sub)
                pid = obj.get("id")
                if pid:
                    for field in ["content", "translatedContent", "guidePrompt"]:
                        val = obj.get(field)
                        if isinstance(val, str) and val.startswith("$"):
                            ref_id = val[1:]
                            if ref_id in text_table:
                                obj[field] = text_table[ref_id]
                    prompts[pid] = obj
            except Exception:
                pid = int(m.group(1))
                title = m.group(2)
                slug_m = re.search(r"\"slug\":\"([^\"]+)\"", sub)
                desc_m = re.search(r"\"description\":\"([^\"]+)\"", sub)
                cont_m = re.search(r"\"content\":(?:\"([^\"]+)\"|\$(\w+))", sub)
                content_val = ""
                if cont_m:
                    if cont_m.group(1):
                        content_val = cont_m.group(1)
                    elif cont_m.group(2) and cont_m.group(2) in text_table:
                        content_val = text_table[cont_m.group(2)]
                prompts[pid] = {
                    "id": pid,
                    "title": title,
                    "slug": slug_m.group(1) if slug_m else "",
                    "description": desc_m.group(1) if desc_m else "",
                    "content": content_val
                }
    return prompts

def categorize_prompt(title, desc, content):
    """Infiere la categoría temática del prompt."""
    text = f"{title} {desc} {content}".lower()
    if any(k in text for k in ["three.js", "webgpu", "3d", "diorama", "blender", "rapier", "tsl"]):
        return "3D & WebGPU (Three.js)"
    elif any(k in text for k in ["ui motion", "sistema de movimiento", "slider", "toggle", "interface"]):
        return "UI & Motion Systems"
    elif any(k in text for k in ["hyperframes", "explainer", "noticias", "explicativo", "workflow", "flujo de trabajo"]):
        return "Workflows & Explicadores Animados"
    elif any(k in text for k in ["svg", "canvas", "código de animación", "tranvía", "generativo"]):
        return "SVG Animado & Canvas Generativo"
    elif any(k in text for k in ["música", "music video", "musical", "canción"]):
        return "Videos Musicales Interactivos"
    elif any(k in text for k in ["marca", "brand", "comercial", "producto", "showreel"]):
        return "Promocional & Brand Motion"
    else:
        return "Motion Graphics General"

def crawl_youmind(max_detail_pages=45):
    """Ejecuta el rastreo completo."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_prompts = {}
    visited = set()
    to_visit = list(SEEDS)

    session = requests.Session(impersonate="chrome120")
    print("🚀 Iniciando extracción de Prompts Claude Opus 5.5...")

    detail_count = 0
    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        is_detail = "/video-prompts/" in url
        if is_detail:
            detail_count += 1

        print(f"[{len(visited)}] GET {url} ...", end=" ", flush=True)
        try:
            res = session.get(url, timeout=15)
            if res.status_code != 200:
                print(f"Error {res.status_code}")
                continue

            text_table, full_text, soup = parse_flight_stream(res.text)
            extracted = extract_prompts(full_text, text_table)

            new_items = 0
            for pid, p in extracted.items():
                if pid not in all_prompts:
                    all_prompts[pid] = p
                    new_items += 1
                else:
                    # Si ya existía, enriquecer campos más largos o faltantes
                    existing = all_prompts[pid]
                    for k, v in p.items():
                        if v and (not existing.get(k) or len(str(v)) > len(str(existing.get(k)))):
                            existing[k] = v

            print(f"✓ ({len(extracted)} detectados, {new_items} nuevos). Total: {len(all_prompts)}")

            # Descubrir más enlaces si aún no alcanzamos el límite de detalle
            if detail_count < max_detail_pages:
                for a in soup.find_all("a", href=True):
                    href = a["href"]
                    if href.startswith("/es-419/video-prompts/") and href not in visited:
                        full_u = urljoin(BASE_URL, href)
                        if full_u not in visited and full_u not in to_visit:
                            to_visit.append(full_u)

        except Exception as e:
            print(f"✗ Falló: {e}")

    # Enriquecer y ordenar
    cleaned_prompts = []
    for pid, p in all_prompts.items():
        title = (p.get("title") or f"Prompt #{pid}").strip()
        slug = (p.get("slug") or "").strip()
        desc = (p.get("description") or "").strip()
        content = (p.get("content") or "").strip()
        translated = (p.get("translatedContent") or "").strip()

        # Si el prompt viene con $ref no resuelto o vacío, intentar usar el otro idioma
        if content.startswith("$"):
            content = ""
        if translated.startswith("$"):
            translated = ""

        prompt_principal = translated if translated else content
        prompt_secundario = content if translated and content != translated else ""

        author_data = p.get("author") or {}
        author_name = author_data.get("name", "Comunidad YouMind") if isinstance(author_data, dict) else str(author_data)
        author_link = author_data.get("link", "") if isinstance(author_data, dict) else ""

        videos = p.get("videos") or []
        video_url = ""
        thumb_url = ""
        if videos and isinstance(videos, list) and len(videos) > 0:
            first_v = videos[0]
            if isinstance(first_v, dict):
                video_url = first_v.get("sourceUrl", "")
                thumb_url = first_v.get("thumbnail", "")

        category = categorize_prompt(title, desc, f"{content} {translated}")
        url_prompt = f"https://youmind.com/es-419/video-prompts/{slug}-{pid}" if slug else f"https://youmind.com/es-419/video-prompts/{pid}"

        cleaned_prompts.append({
            "id": pid,
            "title": title,
            "category": category,
            "description": desc,
            "prompt_es": prompt_principal,
            "prompt_original": prompt_secundario,
            "author_name": author_name,
            "author_link": author_link,
            "source_link": p.get("sourceLink", ""),
            "video_url": video_url,
            "thumbnail_url": thumb_url,
            "url": url_prompt,
            "published_at": p.get("sourcePublishedAt", "")
        })

    cleaned_prompts.sort(key=lambda x: x["id"], reverse=True)
    return cleaned_prompts

def export_json(prompts):
    filepath = os.path.join(OUTPUT_DIR, "prompts_opus_5_5.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"📦 JSON guardado: {filepath} ({len(prompts)} registros)")
    return filepath

def export_excel(prompts):
    filepath = os.path.join(OUTPUT_DIR, "prompts_opus_5_5.xlsx")
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Opus 5.5 Prompts"
    ws.views.sheetView[0].showGridLines = True

    # Estilos
    header_fill = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    border_thin = Border(
        left=Side(style="thin", color="E2E8F0"),
        right=Side(style="thin", color="E2E8F0"),
        top=Side(style="thin", color="E2E8F0"),
        bottom=Side(style="thin", color="E2E8F0")
    )
    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="top", wrap_text=True)

    # Título principal
    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = "🎬 CATÁLOGO DE PROMPTS PARA CLAUDE OPUS 5.5 — MOTION GRAPHICS & 3D (YOUMIND)"
    title_cell.font = Font(name="Calibri", size=15, bold=True, color="FFFFFF")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    title_cell.fill = PatternFill(start_color="0D233A", end_color="0D233A", fill_type="solid")
    ws.row_dimensions[1].height = 40

    # Subtítulo
    ws.merge_cells("A2:H2")
    sub_cell = ws["A2"]
    sub_cell.value = f"Extracción automatizada • {len(prompts)} Prompts analizados con código, videos de muestra y parámetros técnicos"
    sub_cell.font = Font(name="Calibri", size=10, italic=True, color="B0BEC5")
    sub_cell.alignment = Alignment(horizontal="center", vertical="center")
    sub_cell.fill = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
    ws.row_dimensions[2].height = 22

    ws.row_dimensions[3].height = 10

    # Encabezados
    headers = [
        ("#", 6),
        ("ID", 10),
        ("Categoría", 24),
        ("Título del Prompt", 35),
        ("Descripción Resumida", 45),
        ("Prompt en Español / Principal", 70),
        ("Autor", 20),
        ("Video Demo / URL", 30)
    ]

    ws.row_dimensions[4].height = 28
    for col_idx, (h_text, width) in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=col_idx, value=h_text)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = align_center
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    # Filas
    for row_idx, p in enumerate(prompts, start=5):
        ws.row_dimensions[row_idx].height = 65
        is_even = (row_idx % 2 == 0)
        row_fill = zebra_fill if is_even else None

        values = [
            row_idx - 4,
            p["id"],
            p["category"],
            p["title"],
            p["description"],
            p["prompt_es"][:1200] + ("..." if len(p["prompt_es"]) > 1200 else ""),
            p["author_name"],
            p["video_url"] if p["video_url"] else p["url"]
        ]

        for col_idx, val in enumerate(values, start=1):
            c = ws.cell(row=row_idx, column=col_idx, value=val)
            c.font = Font(name="Calibri", size=10)
            c.border = border_thin
            if row_fill:
                c.fill = row_fill

            if col_idx in [1, 2]:
                c.alignment = align_center
            elif col_idx == 3:
                c.alignment = align_center
                c.font = Font(name="Calibri", size=10, bold=True, color="1E40AF")
            elif col_idx == 4:
                c.alignment = align_left
                c.font = Font(name="Calibri", size=10, bold=True, color="0F172A")
            elif col_idx in [5, 6]:
                c.alignment = align_left
            elif col_idx == 7:
                c.alignment = align_center
            elif col_idx == 8:
                c.alignment = align_center
                if val.startswith("http"):
                    c.hyperlink = val
                    c.font = Font(name="Calibri", size=10, color="2563EB", underline="single")

    wb.save(filepath)
    print(f"📊 Excel generado: {filepath} ({len(prompts)} filas)")
    return filepath

def export_markdown(prompts):
    filepath = os.path.join(OUTPUT_DIR, "prompts_opus_5_5.md")
    
    # Agrupar por categoría
    by_cat = {}
    for p in prompts:
        cat = p["category"]
        by_cat.setdefault(cat, []).append(p)

    lines = [
        "# 🎬 Catálogo Maestro de Prompts para Claude Opus 5.5",
        "",
        "> **Fuente**: [YouMind — Opus 5.5 Prompts](https://youmind.com/es-419/opus-5-5-prompts)  ",
        f"> **Total de prompts extraídos**: {len(prompts)}  ",
        f"> **Fecha de extracción**: 12 de Octubre de 2026",
        "",
        "---",
        "",
        "## 📑 Índice de Categorías",
        ""
    ]

    for cat, items in by_cat.items():
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("(", "").replace(")", "").replace(".", "")
        lines.append(f"- [**{cat}** ({len(items)} prompts)](#{anchor})")

    lines.append("\n---\n")

    for cat, items in by_cat.items():
        lines.append(f"## {cat}\n")
        for i, p in enumerate(items, 1):
            lines.append(f"### {i}. {p['title']}")
            lines.append(f"- **ID YouMind**: `{p['id']}`")
            if p["author_name"]:
                auth_str = f"[{p['author_name']}]({p['author_link']})" if p["author_link"] else p["author_name"]
                lines.append(f"- **Autor / Créditos**: {auth_str}")
            if p["url"]:
                lines.append(f"- **Ficha en YouMind**: [Ver en YouMind]({p['url']})")
            if p["source_link"]:
                lines.append(f"- **Post Original (X/Twitter)**: [Ver en X]({p['source_link']})")
            if p["video_url"]:
                lines.append(f"- **Video Demostrativo**: [Ver Video MP4]({p['video_url']})")
            
            lines.append(f"\n> **Descripción**: {p['description']}\n")

            if p["prompt_es"]:
                lines.append("#### 📝 Prompt en Español:")
                lines.append("```text")
                lines.append(p["prompt_es"])
                lines.append("```\n")

            if p["prompt_original"] and p["prompt_original"] != p["prompt_es"]:
                lines.append("#### 🌐 Prompt Original:")
                lines.append("```text")
                lines.append(p["prompt_original"])
                lines.append("```\n")

            lines.append("---\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"📄 Markdown generado: {filepath}")
    return filepath

def main():
    prompts = crawl_youmind(max_detail_pages=40)
    print(f"\n✨ Extracción completada con éxito: {len(prompts)} prompts procesados.")
    export_json(prompts)
    export_excel(prompts)
    export_markdown(prompts)

if __name__ == "__main__":
    main()
