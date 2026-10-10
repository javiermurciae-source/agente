#!/usr/bin/env python3
"""
ieee_doc_builder.py: Generador y clonador de alta precisión de informes IEEE (UNISANGIL)
Crea documentos Word (.docx) perfectamente formateados en 2 columnas, con estilos oficiales IEEE.
"""
import os
import sys
import json
import shutil
import zipfile
import argparse
from lxml import etree

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "ieee_template_unisangil.docx")

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
V_NS = "urn:schemas-microsoft-com:vml"
O_NS = "urn:schemas-microsoft-com:office:office"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
PIC_NS = "http://schemas.openxmlformats.org/drawingml/2006/picture"

NSMAP = {
    'w': W_NS,
    'r': R_NS,
    'v': V_NS,
    'o': O_NS,
    'wp': WP_NS,
    'a': A_NS,
    'pic': PIC_NS
}

def qn(tag):
    prefix, name = tag.split(":")
    return f"{{{NSMAP[prefix]}}}{name}"

class IEEEDocumentBuilder:
    def __init__(self, template_path=None):
        self.template_path = template_path or TEMPLATE_PATH
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Plantilla base no encontrada: {self.template_path}")

    def build(self, spec_data, output_path):
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        temp_dir = os.path.join("/tmp", f"ieee_build_{os.getpid()}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        try:
            # 1. Descomprimir plantilla
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(temp_dir)

            doc_xml_path = os.path.join(temp_dir, "word", "document.xml")
            rels_path = os.path.join(temp_dir, "word", "_rels", "document.xml.rels")
            media_dir = os.path.join(temp_dir, "word", "media")
            os.makedirs(media_dir, exist_ok=True)

            with open(doc_xml_path, 'rb') as f:
                root = etree.fromstring(f.read())

            with open(rels_path, 'rb') as f:
                rels_root = etree.fromstring(f.read())

            # Encontrar el ID de relación más alto
            existing_rids = []
            for rel in rels_root.findall(qn("r:Relationship")):
                rid = rel.get("Id", "")
                if rid.startswith("rId") and rid[3:].isdigit():
                    existing_rids.append(int(rid[3:]))
            max_rid = max(existing_rids) if existing_rids else 50

            # Guardar propiedades de sección (márgenes y columnas)
            sect_prs = root.xpath("//w:sectPr", namespaces=NSMAP)
            sect1_pr = sect_prs[0] if len(sect_prs) > 0 else None
            sect2_pr = sect_prs[-1] if len(sect_prs) > 1 else None

            # Limpiar cuerpo
            body = root.find(qn("w:body"))
            for child in list(body):
                body.remove(child)

            # ================= SECCIÓN 1: ENCABEZADO 1 COLUMNA =================
            # Título ES
            body.append(self._create_p(spec_data.get("title_es", "Título del Laboratorio"), style="Ttulo", bold=True, size_pt=24, align="center"))
            
            # Título EN
            if spec_data.get("title_en"):
                body.append(self._create_p(spec_data["title_en"], style="EnglishTitle", italic=True, size_pt=12, align="center"))

            # Autores
            authors = spec_data.get("authors", "Bernal, Dana., Reyes, Andrey y Murcia, Camilo")
            body.append(self._create_p(authors, style="Authors", align="center", size_pt=11))

            # Filiación
            inst = spec_data.get("institution", "Fundación Universitaria de San Gil (UNISANGIL)")
            course = spec_data.get("course", "Asignatura Comunicación de Datos")
            city = spec_data.get("city", "San Gil, Colombia")
            for line in [inst, course, city]:
                body.append(self._create_p(line, align="center", size_pt=10))

            # Correos
            emails = spec_data.get("emails", ["danabernal222@unisangil.edu.co", "andreyreyes@unisangil.edu.co", "camilomurcia@unisangil.edu.co"])
            for em in emails:
                body.append(self._create_p(em, align="center", size_pt=9))

            # Fechas
            dates = spec_data.get("dates", {})
            f_rec = dates.get("reception", "Fecha de Recepción:")
            f_ace = dates.get("acceptance", "Fecha de Aceptación:")
            body.append(self._create_p(f"{f_rec}\n{f_ace}", align="left", size_pt=8, italic=True))

            # Resumen ES
            if spec_data.get("abstract_es"):
                p_abs = self._create_mixed_p([
                    ("Resumen — ", True, True),
                    (spec_data["abstract_es"], False, False)
                ], style="Abstract", align="both", size_pt=9)
                body.append(p_abs)

            # Palabras clave ES
            if spec_data.get("keywords_es"):
                p_kw = self._create_mixed_p([
                    ("Palabras clave— ", True, True),
                    (spec_data["keywords_es"], False, False)
                ], style="IndexTerms", align="both", size_pt=9)
                body.append(p_kw)

            # Abstract EN
            if spec_data.get("abstract_en"):
                p_abs_en = self._create_mixed_p([
                    ("Abstract— ", True, True),
                    (spec_data["abstract_en"], False, False)
                ], style="Abstract", align="both", size_pt=9)
                body.append(p_abs_en)

            # Keywords EN
            if spec_data.get("keywords_en"):
                p_kw_en = self._create_mixed_p([
                    ("Keywords— ", True, True),
                    (spec_data["keywords_en"], False, False)
                ], style="IndexTerms", align="both", size_pt=9)
                body.append(p_kw_en)

            # Cierre de Sección 1 (Salto continuo a 2 columnas)
            if sect1_pr is not None:
                p_break = etree.SubElement(body, qn("w:p"))
                p_pr = etree.SubElement(p_break, qn("w:pPr"))
                p_pr.append(etree.fromstring(etree.tostring(sect1_pr)))

            # ================= SECCIÓN 2: CUERPO 2 COLUMNAS =================
            sections = spec_data.get("sections", [])
            for sec in sections:
                s_title = sec.get("title", "")
                if s_title:
                    body.append(self._create_p(s_title, style="Ttulo1", bold=True, size_pt=10, align="center"))

                for p_text in sec.get("paragraphs", []):
                    body.append(self._create_p(p_text, style="Text", align="both", size_pt=10))

                # Tablas
                for tbl_info in sec.get("tables", []):
                    t_title = tbl_info.get("title")
                    if t_title:
                        body.append(self._create_p(t_title, style="TableTitle", bold=True, align="center", size_pt=8))
                    tbl_el = self._create_table(tbl_info.get("headers", []), tbl_info.get("rows", []))
                    body.append(tbl_el)

                # Figuras / Imágenes
                for fig in sec.get("figures", []):
                    img_path = fig.get("image")
                    caption = fig.get("caption", "Fig.")
                    if img_path and os.path.exists(img_path):
                        max_rid += 1
                        new_rid = f"rId{max_rid}"
                        img_ext = os.path.splitext(img_path)[-1]
                        dest_img_name = f"image_cust_{max_rid}{img_ext}"
                        shutil.copy(img_path, os.path.join(media_dir, dest_img_name))

                        # Agregar Relationship
                        new_rel = etree.SubElement(rels_root, qn("r:Relationship"))
                        new_rel.set("Id", new_rid)
                        new_rel.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
                        new_rel.set("Target", f"media/{dest_img_name}")

                        # Insertar Drawing
                        p_img = self._create_drawing_p(new_rid, width_pt=fig.get("width_pt", 220), height_pt=fig.get("height_pt", 150))
                        body.append(p_img)

                    if caption:
                        body.append(self._create_p(caption, style="FigureCaption", size_pt=8, align="center"))

            # Referencias
            refs = spec_data.get("references", [])
            if refs:
                body.append(self._create_p("REFERENCIAS", style="ReferenceHead", bold=True, align="center", size_pt=10))
                for idx, r_text in enumerate(refs):
                    prefix = f"[{idx+1}] "
                    body.append(self._create_mixed_p([
                        (prefix, False, False),
                        (r_text, False, False)
                    ], style="References", size_pt=8, align="both"))

            # Propiedades finales de sección 2
            if sect2_pr is not None:
                body.append(etree.fromstring(etree.tostring(sect2_pr)))

            # Guardar XMLs
            with open(doc_xml_path, 'wb') as f:
                f.write(etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True))

            with open(rels_path, 'wb') as f:
                f.write(etree.tostring(rels_root, xml_declaration=True, encoding="UTF-8", standalone=True))

            # Empaquetar .docx resultante
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zout:
                for foldername, subfolders, filenames in os.walk(temp_dir):
                    for filename in filenames:
                        filepath = os.path.join(foldername, filename)
                        arcname = os.path.relpath(filepath, temp_dir)
                        zout.write(filepath, arcname)

            print(f"⚡ Informe IEEE generado con éxito en: {output_path}")
            return output_path

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def _create_p(self, text, style=None, bold=False, italic=False, size_pt=10, align=None):
        p = etree.Element(qn("w:p"))
        pPr = etree.SubElement(p, qn("w:pPr"))
        if style:
            pStyle = etree.SubElement(pPr, qn("w:pStyle"))
            pStyle.set(qn("w:val"), style)
        if align:
            jc = etree.SubElement(pPr, qn("w:jc"))
            jc.set(qn("w:val"), align)

        r = etree.SubElement(p, qn("w:r"))
        rPr = etree.SubElement(r, qn("w:rPr"))
        
        # Tipografía Times New Roman estricta IEEE
        rFonts = etree.SubElement(rPr, qn("w:rFonts"))
        rFonts.set(qn("w:ascii"), "Times New Roman")
        rFonts.set(qn("w:hAnsi"), "Times New Roman")

        if bold:
            etree.SubElement(rPr, qn("w:b"))
        if italic:
            etree.SubElement(rPr, qn("w:i"))
        if size_pt:
            sz = etree.SubElement(rPr, qn("w:sz"))
            sz.set(qn("w:val"), str(int(size_pt * 2)))

        t = etree.SubElement(r, qn("w:t"))
        t.text = text
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        return p

    def _create_mixed_p(self, segments, style=None, align=None, size_pt=9):
        p = etree.Element(qn("w:p"))
        pPr = etree.SubElement(p, qn("w:pPr"))
        if style:
            pStyle = etree.SubElement(pPr, qn("w:pStyle"))
            pStyle.set(qn("w:val"), style)
        if align:
            jc = etree.SubElement(pPr, qn("w:jc"))
            jc.set(qn("w:val"), align)

        for text, bold, italic in segments:
            r = etree.SubElement(p, qn("w:r"))
            rPr = etree.SubElement(r, qn("w:rPr"))
            rFonts = etree.SubElement(rPr, qn("w:rFonts"))
            rFonts.set(qn("w:ascii"), "Times New Roman")
            rFonts.set(qn("w:hAnsi"), "Times New Roman")
            if bold:
                etree.SubElement(rPr, qn("w:b"))
            if italic:
                etree.SubElement(rPr, qn("w:i"))
            if size_pt:
                sz = etree.SubElement(rPr, qn("w:sz"))
                sz.set(qn("w:val"), str(int(size_pt * 2)))
            t = etree.SubElement(r, qn("w:t"))
            t.text = text
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        return p

    def _create_table(self, headers, rows):
        tbl = etree.Element(qn("w:tbl"))
        tblPr = etree.SubElement(tbl, qn("w:tblPr"))
        tblW = etree.SubElement(tblPr, qn("w:tblW"))
        tblW.set(qn("w:w"), "4500")
        tblW.set(qn("w:type"), "dxa")
        jc = etree.SubElement(tblPr, qn("w:jc"))
        jc.set(qn("w:val"), "center")

        # Bordes IEEE: Superior e inferior sólidos, sin bordes verticales
        tblBorders = etree.SubElement(tblPr, qn("w:tblBorders"))
        for b_name in ["top", "bottom"]:
            b = etree.SubElement(tblBorders, qn(f"w:{b_name}"))
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "8")
            b.set(qn("w:space"), "0")
            b.set(qn("w:color"), "auto")
        for b_name in ["left", "right", "insideV"]:
            b = etree.SubElement(tblBorders, qn(f"w:{b_name}"))
            b.set(qn("w:val"), "none")

        # Header Row
        if headers:
            tr = etree.SubElement(tbl, qn("w:tr"))
            for h in headers:
                tc = etree.SubElement(tr, qn("w:tc"))
                tcPr = etree.SubElement(tc, qn("w:tcPr"))
                tcBorders = etree.SubElement(tcPr, qn("w:tcBorders"))
                b_bot = etree.SubElement(tcBorders, qn("w:bottom"))
                b_bot.set(qn("w:val"), "single")
                b_bot.set(qn("w:sz"), "6")
                b_bot.set(qn("w:space"), "0")
                b_bot.set(qn("w:color"), "auto")

                p = self._create_p(str(h), style="Encabezadodelatabla", bold=True, size_pt=8, align="center")
                tc.append(p)

        # Data Rows
        for row in rows:
            tr = etree.SubElement(tbl, qn("w:tr"))
            for cell_val in row:
                tc = etree.SubElement(tr, qn("w:tc"))
                p = self._create_p(str(cell_val), style="Contenidodelatabla", size_pt=8, align="center")
                tc.append(p)

        return tbl

    def _create_drawing_p(self, r_id, width_pt=220, height_pt=150):
        # 1 pt = 12700 EMUs
        cx = int(width_pt * 12700)
        cy = int(height_pt * 12700)

        drawing_xml = f"""
        <w:p xmlns:w="{W_NS}" xmlns:wp="{WP_NS}" xmlns:a="{A_NS}" xmlns:pic="{PIC_NS}" xmlns:r="{R_NS}">
          <w:pPr>
            <w:jc w:val="center"/>
          </w:pPr>
          <w:r>
            <w:drawing>
              <wp:inline distT="0" distB="0" distL="0" distR="0">
                <wp:extent cx="{cx}" cy="{cy}"/>
                <wp:docPr id="1" name="Figura IEEE"/>
                <wp:cNvGraphicFramePr>
                  <a:graphicFrameLocks noChangeAspect="1"/>
                </wp:cNvGraphicFramePr>
                <a:graphic>
                  <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
                    <pic:pic>
                      <pic:nvPicPr>
                        <pic:cNvPr id="1" name="Image"/>
                        <pic:cNvPicPr/>
                      </pic:nvPicPr>
                      <pic:blipFill>
                        <a:blip r:embed="{r_id}"/>
                        <a:stretch>
                          <a:fillRect/>
                        </a:stretch>
                      </pic:blipFill>
                      <pic:spPr>
                        <a:xfrm>
                          <a:off x="0" y="0"/>
                          <a:ext cx="{cx}" cy="{cy}"/>
                        </a:xfrm>
                        <a:prstGeom prst="rect">
                          <a:avLst/>
                        </a:prstGeom>
                      </pic:spPr>
                    </pic:pic>
                  </a:graphicData>
                </a:graphic>
              </wp:inline>
            </w:drawing>
          </w:r>
        </w:p>
        """
        return etree.fromstring(drawing_xml)

def main():
    parser = argparse.ArgumentParser(description="Constructor de informes IEEE para UNISANGIL")
    parser.add_argument("spec", help="Archivo JSON con la especificación del laboratorio")
    parser.add_argument("--out", "-o", required=True, help="Ruta del archivo .docx de salida")
    parser.add_argument("--view", action="store_true", help="Abrir de inmediato en WPS Office")
    args = parser.parse_args()

    with open(args.spec, 'r', encoding='utf-8') as f:
        spec = json.load(f)

    builder = IEEEDocumentBuilder()
    out = builder.build(spec, args.out)

    if args.view:
        import subprocess
        subprocess.run(["viewxls", out] if out.endswith(".xlsx") else ["wps", out], check=False)

if __name__ == "__main__":
    main()
