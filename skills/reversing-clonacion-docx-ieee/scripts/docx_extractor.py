#!/usr/bin/env python3
"""
docx_extractor.py: Deconstructor y analizador de ingeniería inversa de archivos .docx
Extrae estructura OpenXML, metadatos, fuentes, estilos, tablas e imágenes.
"""
import os
import sys
import json
import zipfile
import argparse
from lxml import etree

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture'
}

def analyze_docx(docx_path, out_dir=None):
    if not os.path.exists(docx_path):
        print(f"❌ Error: Archivo no encontrado: {docx_path}")
        return None

    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        media_dir = os.path.join(out_dir, "media")
        os.makedirs(media_dir, exist_ok=True)

    result = {
        "file": os.path.basename(docx_path),
        "sections": [],
        "styles_used": set(),
        "tables": [],
        "paragraphs": [],
        "images": []
    }

    with zipfile.ZipFile(docx_path, 'r') as z:
        # 1. Extraer imágenes
        for name in z.namelist():
            if name.startswith('word/media/'):
                img_name = os.path.basename(name)
                img_size = z.getinfo(name).file_size
                result["images"].append({"name": img_name, "size_bytes": img_size})
                if out_dir:
                    with open(os.path.join(media_dir, img_name), 'wb') as f:
                        f.write(z.read(name))

        # 2. Parsear document.xml
        doc_xml = z.read('word/document.xml')
        root = etree.fromstring(doc_xml)

        # Secciones y configuración de columnas / márgenes
        for i, sect in enumerate(root.xpath('//w:sectPr', namespaces=NS)):
            cols = sect.find('w:cols', namespaces=NS)
            pg_mar = sect.find('w:pgMar', namespaces=NS)
            pg_sz = sect.find('w:pgSz', namespaces=NS)
            sec_info = {
                "index": i + 1,
                "columns": int(cols.get(f"{{{NS['w']}}}num", "1")) if cols is not None else 1,
                "column_space_dxa": int(cols.get(f"{{{NS['w']}}}space", "0")) if cols is not None and cols.get(f"{{{NS['w']}}}space") else 0,
                "margins": {k.split('}')[-1]: v for k, v in (pg_mar.attrib.items() if pg_mar is not None else {})},
                "page_size": {k.split('}')[-1]: v for k, v in (pg_sz.attrib.items() if pg_sz is not None else {})}
            }
            result["sections"].append(sec_info)

        # Párrafos y estilos
        for p in root.xpath('//w:p', namespaces=NS):
            p_style = p.find('.//w:pStyle', namespaces=NS)
            style_name = p_style.get(f"{{{NS['w']}}}val") if p_style is not None else "Normal"
            result["styles_used"].add(style_name)

            texts = [t.text for t in p.xpath('.//w:t', namespaces=NS) if t.text]
            text = ''.join(texts).strip()
            if text:
                result["paragraphs"].append({
                    "style": style_name,
                    "text": text
                })

        # Tablas
        for t_idx, tbl in enumerate(root.xpath('//w:tbl', namespaces=NS)):
            table_data = []
            for row in tbl.xpath('.//w:tr', namespaces=NS):
                row_cells = []
                for cell in row.xpath('.//w:tc', namespaces=NS):
                    c_texts = [t.text for t in cell.xpath('.//w:t', namespaces=NS) if t.text]
                    row_cells.append(''.join(c_texts).strip())
                if row_cells:
                    table_data.append(row_cells)
            result["tables"].append({
                "index": t_idx + 1,
                "rows": len(table_data),
                "cols": len(table_data[0]) if table_data else 0,
                "data": table_data
            })

    result["styles_used"] = sorted(list(result["styles_used"]))

    if out_dir:
        report_file = os.path.join(out_dir, "analysis_report.json")
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"✅ Análisis guardado en: {report_file}")
        if result["images"]:
            print(f"🖼️ {len(result['images'])} imágenes extraídas en: {media_dir}")

    return result

def main():
    parser = argparse.ArgumentParser(description="Deconstructor y analizador de documentos Word .docx")
    parser.add_argument("file", help="Ruta al archivo .docx")
    parser.add_argument("--out", "-o", help="Directorio para volcar el reporte y medios", default=None)
    args = parser.parse_args()

    res = analyze_docx(args.file, args.out)
    if res:
        print(f"\n📄 Archivo: {res['file']}")
        print(f"📐 Secciones: {len(res['sections'])} (Columnas detectadas: {[s['columns'] for s in res['sections']]})")
        print(f"📊 Tablas encontradas: {len(res['tables'])}")
        print(f"🖼️ Imágenes encontradas: {len(res['images'])}")
        print(f"🎨 Estilos empleados: {', '.join(res['styles_used'][:12])}...")

if __name__ == "__main__":
    main()
