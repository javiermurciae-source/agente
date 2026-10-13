#!/usr/bin/env python3
"""
Scraper de Habilidades y Prompts de Diapositivas (Slides / Presentaciones) en YouMind
Extrae:
- Landing de Diapositivas GPT Image 2 (Metodología, 8 plantillas maestras, comparación)
- Habilidades (Skills) de Generación de Diapositivas (HTML Presentations, Neo-Brutalism, Apple/Notion, Wang Hong Hand-drawn, etc.)
- Prompts, instrucciones, características visuales, resoluciones y estilos.
"""

import os
import json
import re
from curl_cffi import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUTPUT_DIR = "/home/rootkit/Proyectos/youmind-slides-prompts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SLIDE_SKILL_URLS = [
    "https://youmind.com/es-419/skills/html-presentation-generator-CviCTluY1BrF26",
    "https://youmind.com/es-419/skills/business-minimalist-presentation-ZLziNxhgJwjY6q",
    "https://youmind.com/es-419/skills/developer-neo-brutalism-slide-generator-aZDYUQJ8jcCmLp",
    "https://youmind.com/es-419/skills/article-to-slides-generator-Lg2w5F2OOG2rHd",
    "https://youmind.com/es-419/skills/academic-presentation-generator-EziTpTaTiSMMbF",
    "https://youmind.com/es-419/skills/corporate-presentation-generator-AOgJLzhK87eq6H",
    "https://youmind.com/es-419/skills/cinematic-sci-fi-presentation-7OkuIMoI4EBepB",
    "https://youmind.com/es-419/skills/chalkboard-chalk-slides-iz5gRRRPL1Ttbe",
    "https://youmind.com/es-419/skills/clay-minimal-slides-FHZEPlNk7I7YIj",
    "https://youmind.com/es-419/skills/diagonal-flow-deck-generator-XwoDY9hKrtaizL",
    "https://youmind.com/es-419/skills/editorial-minimalism-slides-ihQUJRAIfDvsZZ",
    "https://youmind.com/es-419/skills/hand-drawn-slides-generator-VQ6iIyAr0IcTvh",
    "https://youmind.com/es-419/skills/handwritten-academic-presentation-generator-XKGa6SBRNzDG18",
    "https://youmind.com/es-419/skills/audience-tailored-presentation-generator-VCDttmq2ASvUgh",
    "https://youmind.com/es-419/skills/editorial-product-deck-fht0CVmQs3zPFs",
    "https://youmind.com/es-419/skills/fashion-magazine-slides-Md9jtmlN5BIWmi",
    "https://youmind.com/es-419/skills/clean-minimal-slides-akIfSyQ0T2XHHg",
    "https://youmind.com/es-419/skills/contemporary-art-slides-9YJcrFYHvaVKBK",
    "https://youmind.com/es-419/skills/botanical-service-presentation-slides-ojTHmwIqWaSORa",
]

def parse_skill_page(url, session):
    try:
        res = session.get(url, timeout=15)
        if res.status_code != 200:
            return None
        soup = BeautifulSoup(res.text, "lxml")

        title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "Diapositivas"
        meta_desc = ""
        m = soup.find("meta", {"name": "description"})
        if m and m.get("content"):
            meta_desc = m["content"].strip()

        # Extraer párrafos descriptivos y de prompts
        paragraphs = []
        for p in soup.find_all(["p", "blockquote"]):
            txt = p.get_text(" ", strip=True)
            if len(txt) > 35 and not any(skip in txt.lower() for skip in ["cookies", "iniciar sesión", "youmind es el copiloto"]):
                if txt not in paragraphs:
                    paragraphs.append(txt)

        # Detectar tags/palabras clave
        tags = []
        for meta in soup.find_all("meta", {"name": "keywords"}):
            if meta.get("content"):
                tags.extend([t.strip() for t in meta["content"].split(",")])

        full_desc = "\n\n".join(paragraphs[:4])

        # Extraer instrucciones específicas si hay
        prompt_instruction = ""
        for p in paragraphs:
            if any(k in p.lower() for k in ["genera un", "convierte", "crea un", "plantilla", "html", "estilo", "palabras clave"]):
                prompt_instruction = p
                break

        return {
            "title": title,
            "url": url,
            "description": meta_desc,
            "full_content": full_desc,
            "prompt_instruction": prompt_instruction if prompt_instruction else full_desc,
            "tags": tags[:8]
        }
    except Exception as e:
        print(f"Error procesando {url}: {e}")
        return None

def main():
    print("🚀 Extrayendo sección de Diapositivas y Presentaciones de YouMind...")
    session = requests.Session(impersonate="chrome120")

    # 1. Scraping Landing de GPT Image 2 Slides
    landing_url = "https://youmind.com/es-419/landing/gpt-image-2-slides"
    res_land = session.get(landing_url, timeout=20)
    soup_land = BeautifulSoup(res_land.text, "lxml")

    gpt2_features = []
    for h3 in soup_land.find_all("h3"):
        nxt = h3.find_next_sibling()
        desc = nxt.get_text(strip=True) if nxt else ""
        gpt2_features.append({"title": h3.get_text(strip=True), "description": desc})

    # Plantillas de la landing
    landing_templates = [
        {
            "name": "Informe de fin de año / Data Storytelling",
            "slug": "year-end-report",
            "style": "Infografía corporativa, métricas de alto impacto, storytelling cuantitativo.",
            "prompt_hint": "Genera una presentación de informe de fin de año con jerarquía visual estricta, gráficos y tarjetas de datos de alto contraste."
        },
        {
            "name": "Memphis Design Retro",
            "slug": "memphis-design",
            "style": "Geometrías abstractas ochenteras/noventeras, patrones de puntos, colores pastel saturados y dinamismo.",
            "prompt_hint": "Crea diapositivas en estilo Memphis Design con bloques flotantes, paleta retro-pop y tipografías sans-serif audaces."
        },
        {
            "name": "Folleto Visual Audaz (Bold Visual Brochure)",
            "slug": "bold-visual-brochure",
            "style": "Diseño editorial de revista, tipografía gigante de impacto, fondos limpios con enfoque en el producto.",
            "prompt_hint": "Diseña un deck estilo folleto editorial con titulares en display font grande, columnas asimétricas y fotografía protagónica."
        },
        {
            "name": "Diseño Kami (Papel Recortado Editorial)",
            "slug": "kami-design",
            "style": "Texturas de papel japonés, capas superpuestas, sombras suaves volumétricas y estética zen minimalista.",
            "prompt_hint": "Presentación con estética Kami / Paper Cutout: capas superpuestas de papel artesanal, sombras suaves y espacios en blanco."
        },
        {
            "name": "Dibujado a Mano Vibrante (Vibrant Handdrawn)",
            "slug": "vibrant-handdrawn",
            "style": "Garabatos ilustrados, notas al margen, diagramas orgánicos y sensación de pizarra creativa.",
            "prompt_hint": "Crea un mazo de diapositivas con estética hand-drawn: flechas dibujadas a mano, notas tipo sketch, cajas imperfectas y calidez humana."
        },
        {
            "name": "Digital Moderno (Modern Digital)",
            "slug": "modern-digital",
            "style": "SaaS / Tech contemporáneo, esquinas redondeadas, paleta oscura/modo noche y acentos violeta/cian controlados.",
            "prompt_hint": "Presentación digital moderna para producto de tecnología: tarjetas con bordes finos, gradientes de acento sutiles y métricas claras."
        },
        {
            "name": "Brutalismo & Neo-Brutalismo",
            "slug": "brutalism / neu-brutalism",
            "style": "Bordes negros gruesos (2-3px), sombras proyectadas rígidas sin desenfoque (hard shadows), paletas de alto contraste y fuentes monoespaciadas.",
            "prompt_hint": "Crea diapositivas en estilo Neo-Brutalism: bordes negros sólidos, cajas con sombras 4px 4px #000, colores planos vivos y estética de desarrollador."
        }
    ]

    # 2. Scraping de Skills individuales
    skills_data = []
    for idx, u in enumerate(SLIDE_SKILL_URLS, 1):
        print(f"[{idx}/{len(SLIDE_SKILL_URLS)}] Obteniendo skill: {u.split('/')[-1]} ...", end=" ", flush=True)
        sk = parse_skill_page(u, session)
        if sk:
            skills_data.append(sk)
            print("✓")
        else:
            print("✗")

    print(f"\nExtracción completada: {len(skills_data)} habilidades procesadas.")

    # 3. Guardar JSON
    json_path = os.path.join(OUTPUT_DIR, "diapositivas_ia_prompts.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "features_gpt_image_2": gpt2_features,
            "master_templates": landing_templates,
            "slide_skills": skills_data
        }, f, ensure_ascii=False, indent=2)
    print(f"📦 JSON guardado: {json_path}")

    # 4. Guardar Excel
    xlsx_path = os.path.join(OUTPUT_DIR, "diapositivas_ia_prompts.xlsx")
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Habilidades de Diapositivas"
    ws.views.sheetView[0].showGridLines = True

    header_fill = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    border_thin = Border(
        left=Side(style="thin", color="E2E8F0"),
        right=Side(style="thin", color="E2E8F0"),
        top=Side(style="thin", color="E2E8F0"),
        bottom=Side(style="thin", color="E2E8F0")
    )

    ws.merge_cells("A1:E1")
    t1 = ws["A1"]
    t1.value = "📊 CATÁLOGO MAESTRO DE DIAPOSITIVAS Y PRESENTACIONES CON IA (YOUMIND)"
    t1.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    t1.alignment = Alignment(horizontal="center", vertical="center")
    t1.fill = PatternFill(start_color="0D233A", end_color="0D233A", fill_type="solid")
    ws.row_dimensions[1].height = 36

    headers = [
        ("#", 6),
        ("Estilo / Habilidad", 32),
        ("Enfoque Visual & Caso de Uso", 40),
        ("Prompt / Instrucción Maestra", 75),
        ("Enlace en YouMind", 35)
    ]

    ws.row_dimensions[2].height = 26
    for col_idx, (h_text, width) in enumerate(headers, start=1):
        cell = ws.cell(row=2, column=col_idx, value=h_text)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center")
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    row_i = 3
    for s in skills_data:
        ws.row_dimensions[row_i].height = 70
        is_even = (row_i % 2 == 0)
        rf = zebra_fill if is_even else None

        vals = [
            row_i - 2,
            s["title"],
            s["description"],
            s["prompt_instruction"][:1200],
            s["url"]
        ]
        for col_idx, val in enumerate(vals, start=1):
            c = ws.cell(row=row_i, column=col_idx, value=val)
            c.font = Font(name="Calibri", size=10)
            c.border = border_thin
            if rf:
                c.fill = rf
            if col_idx == 1:
                c.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx == 2:
                c.font = Font(name="Calibri", size=10, bold=True, color="0F172A")
                c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            elif col_idx in [3, 4]:
                c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            elif col_idx == 5:
                c.alignment = Alignment(horizontal="center", vertical="center")
                if str(val).startswith("http"):
                    c.hyperlink = val
                    c.font = Font(name="Calibri", size=10, color="2563EB", underline="single")
        row_i += 1

    wb.save(xlsx_path)
    print(f"📊 Excel guardado: {xlsx_path}")

    # 5. Guardar Markdown Maestro
    md_path = os.path.join(OUTPUT_DIR, "diapositivas_ia_prompts.md")
    lines = [
        "# 📊 Guía Maestra y Catálogo de Diapositivas con IA (YouMind)",
        "",
        "> **Plataforma analizada**: [YouMind Diapositivas / Slides IA](https://youmind.com/es-419/landing/gpt-image-2-slides)  ",
        "> **Modelos soportados**: GPT Image 2 (OpenAI), Nano Banana Pro, Claude Opus 5.5 (HTML/Web Presentations)  ",
        "> **Formatos clave**: Diapositivas 16:9, Páginas Web HTML interactivas con animaciones, Exportación a Video con Voz Clonada.",
        "",
        "---",
        "",
        "## 💡 1. Arquitectura de las Diapositivas en YouMind",
        "",
        "YouMind aborda las diapositivas desde dos ángulos complementarios:",
        "",
        "### A. Generación Visual con GPT Image 2 (Diapositivas listas para entregar)",
        "- **99% Precisión Tipográfica**: Diseñado para resolver el talón de Aquiles de los modelos de imagen anteriores (texto borroso o incoherente).",
        "- **Renderizado Paralelo**: Con solo ingresar un artículo, enlace de YouTube o PDF, genera el deck completo de portada a cierre manteniendo la paleta, tipografía y coherencia de personajes.",
        "- **Smart Video Integrado**: Convierte el set de diapositivas en un video vertical u horizontal animado con transiciones, música de fondo (BGM) y narración por voz clonada.",
        "",
        "### B. Generación de Presentaciones en Código (HTML Presentations / Web Decks)",
        "- **Archivo Único `index.html`**: Presentaciones autocontenidas en HTML5, CSS3 y JS para navegación con teclado (`←` / `→` o barra espaciadora).",
        "- **Estética Apple / Notion**: Componentes limpios, tarjetas responsivas, barras de progreso de diapositiva y zona segura para cámara/talking head.",
        "",
        "---",
        "",
        "## 🎨 2. Las 8 Plantillas Maestras (Master Styles)",
        ""
    ]

    for t in landing_templates:
        lines.append(f"### 📌 {t['name']}")
        lines.append(f"- **Slug**: `{t['slug']}`")
        lines.append(f"- **Estilo Visual**: {t['style']}")
        lines.append("#### 📝 Prompt Base Sugerido:")
        lines.append("```text")
        lines.append(t["prompt_hint"])
        lines.append("```")
        lines.append("")

    lines.append("---\n")
    lines.append("## 🛠️ 3. Catálogo de Habilidades (Skills) Especializadas en Diapositivas\n")

    for idx, s in enumerate(skills_data, 1):
        lines.append(f"### {idx}. {s['title']}")
        lines.append(f"- **URL YouMind**: [Ver Ficha Técnica]({s['url']})")
        lines.append(f"- **Enfoque**: {s['description']}\n")
        lines.append("#### 📋 Instrucciones y Estructura:")
        lines.append("```text")
        lines.append(s["prompt_instruction"])
        lines.append("```")
        lines.append("")
        lines.append("---\n")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"📄 Markdown guardado: {md_path}")

if __name__ == "__main__":
    main()
