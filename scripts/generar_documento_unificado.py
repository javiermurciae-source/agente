#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Documento Unificado:
1. Sección I: Asignación de Roles del Proyecto SecureDesk (Tabla 11 roles + Descripciones)
2. Sección II: Actas Oficiales de Reunión (Actas 1 a 8 completas con firmas manuscritas)
Genera:
- SecureDesk_Roles_y_Actas_Reunion.docx (Documento Word)
- SecureDesk_Roles_y_Actas_Reunion.pdf (Documento PDF vía Typst)
"""

import io
import os
import subprocess
import zipfile

# Asegurar firmas
from generar_firmas import generate_kevin_mitnick_signature, generate_gerente_signature

sig_kevin_path = "scripts/firma_kevin_mitnick.png"
sig_gerente_path = "scripts/firma_gerente.png"

if not os.path.exists(sig_kevin_path):
    generate_kevin_mitnick_signature(sig_kevin_path)
if not os.path.exists(sig_gerente_path):
    generate_gerente_signature(sig_gerente_path)

# ==================== DATOS DE ROLES ====================
roles_info = [
    {
        "rol": "Programador",
        "actor": "Camilo Murcia",
        "desc": "Responsable directo de la construcción, desarrollo y codificación del software SecureDesk. Programa los módulos de registro, reporte, clasificación y atención de incidentes de ciberseguridad, así como la lógica de negocio y la integración con las APIs del sistema."
    },
    {
        "rol": "Cliente",
        "actor": "SigmaEntretenimiento",
        "desc": "Organización cliente y destinataria del sistema. Define las necesidades operativas de seguridad de la información, prioriza los requisitos funcionales del software, evalúa los avances entregados en cada iteración y otorga la aceptación formal del producto final."
    },
    {
        "rol": "Encargado de seguimiento (Tracker - Git)",
        "actor": "Pedronel GarciaForero Mateus",
        "desc": "Encargado de la trazabilidad y seguimiento del proyecto utilizando Git. Administra el repositorio central, flujo de trabajo en ramas (Git Flow), revisión de commits, pull requests, gestión del tablero de incidencias (issues), hitos (milestones) y métricas de avance del equipo."
    },
    {
        "rol": "Encargado de pruebas (Tester)",
        "actor": "Daniel Stiven mateus Marin",
        "desc": "Planifica, diseña y ejecuta los planes de prueba funcionales, unitarias y de integración. Evalúa los flujos de autenticación, la carga de reportes y la gestión del ciclo de vida de los incidentes para garantizar calidad, estabilidad y seguridad sin errores."
    },
    {
        "rol": "Líder de Proyecto (Project Manager)",
        "actor": "Juan Daniel Oviedo",
        "desc": "Lidera la coordinación general, asignación de responsabilidades, control de cronograma y mitigación de riesgos del proyecto. Actúa como canal principal de comunicación entre la gerencia de Dark Códex y el cliente SigmaEntretenimiento."
    },
    {
        "rol": "Líder de Análisis de Negocio y Requerimientos",
        "actor": "Juan Carlos Marin",
        "desc": "Responsable de la captura, especificación técnica y validación de los requerimientos del sistema. Define las reglas de negocio, los casos de uso, las matrices de clasificación por riesgo y los flujos de trabajo de los incidentes de ciberseguridad."
    },
    {
        "rol": "Entrenador (Coach Ágil)",
        "actor": "Jhon martin perez",
        "desc": "Facilita la adopción y cumplimiento de las prácticas metodológicas ágiles en el equipo de desarrollo. Asesora en las reuniones de sincronización, optimiza la productividad colectiva y ayuda a remover impedimentos y bloqueos técnicos u operativos."
    },
    {
        "rol": "Consultor de Ciberseguridad (Especialista SOC)",
        "actor": "kevin Mitnick",
        "desc": "Experto en seguridad que asesora en la clasificación de severidad de incidentes, taxonomía de amenazas, monitoreo de alertas, protocolos de contención y políticas defensivas de ciberseguridad para el entorno empresarial. Actúa como Autor de las actas de reunión."
    },
    {
        "rol": "Administrador de Infraestructura y Active Directory (DevOps)",
        "actor": "Daniel Stiven Forero Mateus",
        "desc": "Gestiona los servidores de aplicación y base de datos, la configuración del entorno web, la integración con Active Directory (LDAP) para la validación y gestión de usuarios y equipos, así como el despliegue continuo y la seguridad de la red."
    },
    {
        "rol": "Arquitecto de Software y Base de Datos",
        "actor": "Juan Carlos Marin",
        "desc": "Diseña la estructura técnica, componentes y patrones de diseño de la aplicación web SecureDesk. Modela el esquema relacional de la base de datos para usuarios, roles, activos tecnológicos, eventos, incidentes y pistas de auditoría."
    },
    {
        "rol": "Big Boss",
        "actor": "Eduard bernal",
        "desc": "Máxima autoridad ejecutiva y patrocinador principal del proyecto. Define los objetivos estratégicos de alto nivel, asigna el presupuesto y recursos institucionales, y supervisa el cumplimiento global de los acuerdos contractuales."
    }
]

# ==================== DATOS DE ACTAS ====================
from generar_8_actas_securedesk import actas_data, participantes_texto, build_acta_xml

def generar_docx_unificado(output_docx="SecureDesk_Roles_y_Actas_Reunion.docx"):
    # Construir sección de roles en XML
    tbl_rows_xml = ""
    for item in roles_info:
        r = item["rol"]
        a = item["actor"]
        tbl_rows_xml += f"""<w:tr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="4320"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>{r}</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="4320"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:r><w:t>{a}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>"""

    desc_paragraphs_xml = ""
    for i, item in enumerate(roles_info, 1):
        r = item["rol"]
        a = item["actor"]
        d = item["desc"]
        desc_paragraphs_xml += f"""
        <w:p>
            <w:pPr><w:spacing w:before="140" w:after="40"/></w:pPr>
            <w:r><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="23476A"/></w:rPr><w:t>{i}. {r}</w:t></w:r>
            <w:r><w:rPr><w:sz w:val="22"/><w:color w:val="555555"/></w:rPr><w:t> — Actor: </w:t></w:r>
            <w:r><w:rPr><w:b/><w:i/><w:sz w:val="22"/><w:color w:val="111111"/></w:rPr><w:t>{a}</w:t></w:r>
        </w:p>
        <w:p>
            <w:pPr><w:spacing w:before="20" w:after="140"/><w:ind w:left="360"/></w:pPr>
            <w:r><w:rPr><w:sz w:val="21"/></w:rPr><w:t>{d}</w:t></w:r>
        </w:p>"""

    roles_xml = f"""
    <w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="140"/></w:pPr>
        <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="23476A"/><w:sz w:val="34"/></w:rPr>
        <w:t>SECUREDESK — Documento Maestro del Proyecto</w:t></w:r>
    </w:p>
    <w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="280"/></w:pPr>
        <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:i/><w:color w:val="555555"/><w:sz w:val="22"/></w:rPr>
        <w:t>Dark Códex &amp; SigmaEntretenimiento — Roles de Ingeniería y Actas Oficiales de Reunión</w:t></w:r>
    </w:p>
    <w:p><w:pPr><w:spacing w:before="200" w:after="160"/></w:pPr>
        <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="23476A"/><w:sz w:val="28"/></w:rPr>
        <w:t>Sección I: Asignación de Roles del Proyecto</w:t></w:r>
    </w:p>
    <w:tbl>
        <w:tblPr>
            <w:tblStyle w:val="TableGrid"/><w:tblW w:type="auto" w:w="0"/><w:jc w:val="center"/>
            <w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/>
        </w:tblPr>
        <w:tblGrid><w:gridCol w:w="4320"/><w:gridCol w:w="4320"/></w:tblGrid>
        <w:tr>
            <w:tc><w:tcPr><w:tcW w:type="dxa" w:w="4320"/><w:shd w:fill="23476A"/></w:tcPr><w:p><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>Roles</w:t></w:r></w:p></w:tc>
            <w:tc><w:tcPr><w:tcW w:type="dxa" w:w="4320"/><w:shd w:fill="23476A"/></w:tcPr><w:p><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>Actores</w:t></w:r></w:p></w:tc>
        </w:tr>
        {tbl_rows_xml}
    </w:tbl>
    <w:p><w:pPr><w:spacing w:before="360" w:after="200"/></w:pPr>
        <w:r><w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="23476A"/></w:rPr><w:t>Descripción y Responsabilidades por Rol en SecureDesk</w:t></w:r>
    </w:p>
    {desc_paragraphs_xml}
    <w:p><w:r><w:br w:type="page"/></w:r></w:p>
    <w:p><w:pPr><w:spacing w:before="200" w:after="200"/></w:pPr>
        <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="23476A"/><w:sz w:val="28"/></w:rPr>
        <w:t>Sección II: Actas Oficiales de Reunión (Ciclo Completo)</w:t></w:r>
    </w:p>
    """

    actas_body_xml = ""
    for idx, acta in enumerate(actas_data):
        is_first = (idx == 0)
        is_last = (idx == len(actas_data) - 1)
        actas_body_xml += build_acta_xml(acta, is_first, is_last, idx)

    complete_doc_xml = f"""<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" 
            xmlns:mo="http://schemas.microsoft.com/office/mac/office/2008/main" 
            xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
            xmlns:mv="urn:schemas-microsoft-com:mac:vml" 
            xmlns:o="urn:schemas-microsoft-com:office:office" 
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" 
            xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" 
            xmlns:v="urn:schemas-microsoft-com:vml" 
            xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" 
            xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" 
            xmlns:w10="urn:schemas-microsoft-com:office:word" 
            xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" 
            xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" 
            xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" 
            xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" 
            xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" 
            xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" 
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" 
            xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" 
            mc:Ignorable="w14 wp14">
<w:body>
    {roles_xml}
    {actas_body_xml}
    <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
        <w:pgSz w:w="12240" w:h="15840"/>
        <w:pgMar w:top="605" w:right="749" w:bottom="605" w:left="749" w:header="288" w:footer="288" w:gutter="0"/>
        <w:cols w:space="720"/>
        <w:docGrid w:linePitch="360"/>
    </w:sectPr>
</w:body>
</w:document>"""

    base_docx = "Acta_de_reunion_recreada.docx"
    with open(sig_kevin_path, "rb") as f:
        img_kevin_bytes = f.read()
    with open(sig_gerente_path, "rb") as f:
        img_gerente_bytes = f.read()

    buffer = io.BytesIO()
    with zipfile.ZipFile(base_docx, "r") as zin:
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/document.xml":
                    zout.writestr(item, complete_doc_xml.encode("utf-8"))
                elif item.filename == "[Content_Types].xml":
                    ct_content = zin.read(item.filename).decode("utf-8")
                    if '<Default Extension="png"' not in ct_content:
                        ct_content = ct_content.replace('</Types>', '<Default Extension="png" ContentType="image/png"/></Types>')
                    zout.writestr(item, ct_content.encode("utf-8"))
                elif item.filename == "word/_rels/document.xml.rels":
                    rels_content = zin.read(item.filename).decode("utf-8")
                    if "rId_sig_kevin" not in rels_content:
                        rels_to_add = (
                            '<Relationship Id="rId_sig_kevin" '
                            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                            'Target="media/firma_kevin_mitnick.png"/>'
                            '<Relationship Id="rId_sig_gerente" '
                            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                            'Target="media/firma_gerente.png"/>'
                        )
                        rels_content = rels_content.replace('</Relationships>', rels_to_add + '</Relationships>')
                    zout.writestr(item, rels_content.encode("utf-8"))
                else:
                    zout.writestr(item, zin.read(item.filename))

            zout.writestr("word/media/firma_kevin_mitnick.png", img_kevin_bytes)
            zout.writestr("word/media/firma_gerente.png", img_gerente_bytes)

    with open(output_docx, "wb") as f:
        f.write(buffer.getvalue())

    print(f"DOCX Unificado generado: {output_docx}")

def generar_pdf_typst(output_typ="SecureDesk_Roles_y_Actas.typ", output_pdf="SecureDesk_Roles_y_Actas_Reunion.pdf"):
    # Generar archivo Typst
    lines = []
    lines.append('#set page(paper: "us-letter", margin: (x: 1.8cm, top: 1.8cm, bottom: 2.0cm),')
    lines.append('  header: align(right)[#text(size: 8pt, fill: rgb("#666666"))[SecureDesk — Dark Códex & SigmaEntretenimiento]],')
    lines.append('  footer: [')
    lines.append('    #grid(columns: (1fr, 1fr),')
    lines.append('      align(left)[#text(size: 8pt, fill: rgb("#777777"))[Proyecto de Ciberseguridad & Gestión SOC]],')
    lines.append('      align(right)[#text(size: 8pt, fill: rgb("#777777"))[Página #context counter(page).display("1")]])')
    lines.append('  ]')
    lines.append(')')
    lines.append('#set text(font: "DejaVu Sans", size: 9pt, lang: "es")')
    lines.append('#set par(justify: true, leading: 0.65em)')
    lines.append('')
    # Título Portada
    lines.append('#align(center)[')
    lines.append('  #text(size: 19pt, weight: "bold", fill: rgb("#23476A"))[PROYECTO SECUREDESK]')
    lines.append('  #v(2pt)')
    lines.append('  #text(size: 13pt, weight: "bold", fill: rgb("#333333"))[Asignación de Roles & Actas Oficiales de Reunión]')
    lines.append('  #v(2pt)')
    lines.append('  #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[Dark Códex (Desarrollador) & SigmaEntretenimiento (Cliente) | Ciclo Agosto – Noviembre 2026]')
    lines.append(']')
    lines.append('#v(12pt)')
    lines.append('')
    # Sección 1: Roles
    lines.append('== 1. Asignación Oficial de Roles del Proyecto')
    lines.append('#v(4pt)')
    lines.append('#table(')
    lines.append('  columns: (1fr, 1fr),')
    lines.append('  fill: (col, row) => if row == 0 { rgb("#23476A") } else if calc.even(row) { rgb("#f8fafc") } else { rgb("#ffffff") },')
    lines.append('  stroke: (x, y) => if y == 0 { (bottom: 1.5pt + rgb("#23476A")) } else { (bottom: 0.5pt + rgb("#e2e8f0")) },')
    lines.append('  align: (col, row) => if row == 0 { center } else { left },')
    lines.append('  table.header([#text(fill: white, weight: "bold")[Roles]], [#text(fill: white, weight: "bold")[Actores]]),')
    for item in roles_info:
        r = item["rol"].replace("#", "\\#")
        a = item["actor"].replace("#", "\\#")
        lines.append(f'  [*{r}*], [{a}],')
    lines.append(')')
    lines.append('#v(10pt)')
    lines.append('=== Descripción Técnica de Responsabilidades por Rol en SecureDesk')
    lines.append('#v(4pt)')
    for idx, item in enumerate(roles_info, 1):
        r = item["rol"].replace("#", "\\#")
        a = item["actor"].replace("#", "\\#")
        d = item["desc"].replace("#", "\\#")
        lines.append(f'*• {idx}. {r}* (#text(style: "italic", fill: rgb("#23476A"))[{a}]):')
        lines.append(f'#block(inset: (left: 12pt))[#text(size: 8.5pt)[{d}]]')
        lines.append('#v(2pt)')

    lines.append('#pagebreak()')
    lines.append('')
    # Sección 2: Actas de reunión
    lines.append('== 2. Actas Oficiales de Reunión de Seguimiento (Ciclo Completo)')
    lines.append('#v(6pt)')

    for idx, acta in enumerate(actas_data):
        num = acta["numero"]
        fecha = acta["fecha"]
        titulo = acta["titulo"].replace("#", "\\#")
        lugar = acta["lugar"].replace("#", "\\#")
        autor = acta["autor"].replace("#", "\\#")
        prox = acta["proxima_fecha"].replace("#", "\\#")
        temas = acta["temas"]
        secciones = acta["secciones"]
        acuerdos = acta["acuerdos"]

        lines.append(f'=== Acta de Reunión No. {num}')
        lines.append('#v(4pt)')
        # Tabla de encabezado institucional
        lines.append('#table(')
        lines.append('  columns: (2.8cm, 1fr, 2.5cm),')
        lines.append('  stroke: 0.5pt + rgb("#000000"),')
        lines.append('  align: (col, row) => left,')
        # Row 0: Header
        lines.append('  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],')
        # Row 1: Titulo
        lines.append(f'  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[{titulo}],')
        # Row 2: Fecha y Numero
        lines.append(f'  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [{fecha}], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. {num}]],')
        # Row 3: Lugar
        lines.append(f'  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[{lugar}],')
        # Row 4: Autor
        lines.append(f'  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*{autor}* (Consultor SOC)],')
        # Row 5: Participantes
        lines.append('  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],')
        parts_list = "\\\n".join([f"• {p}" for p in participantes_texto.splitlines()])
        lines.append(f'  table.cell(colspan: 3)[#text(size: 8pt)[{parts_list}]],')
        # Row 7: Temas tratados
        lines.append('  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],')
        temas_list = "\\\n".join([f"– {t}" for t in temas])
        lines.append(f'  table.cell(colspan: 3)[#text(size: 8pt)[{temas_list}]],')
        # Row 9: Header desarrollo
        lines.append('  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],')
        
        # Contenido de desarrollo
        dev_text = []
        for sec_title, sec_items in secciones:
            dev_text.append(f"*{sec_title}*")
            for itype, itext in sec_items:
                if itype == "p":
                    dev_text.append(f"#block(inset: (left: 8pt))[#text(size: 8pt)[{itext}]]")
                elif itype == "b":
                    dev_text.append(f"#block(inset: (left: 14pt))[• #text(size: 8pt)[{itext}]]")
        dev_full = "\n".join(dev_text)
        lines.append(f'  table.cell(colspan: 3)[{dev_full}],')
        
        # Resumen de acuerdos
        lines.append('  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],')
        acuerdos_list = "\\\n".join([f"*{p}*: {a}" for p, a in acuerdos])
        lines.append(f'  table.cell(colspan: 3)[#text(size: 8pt)[{acuerdos_list}]],')
        
        # Proxima reunion
        lines.append('  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],')
        lines.append(f'  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[{prox}]],')
        lines.append(')')
        lines.append('#v(8pt)')
        
        # Tabla de firmas con fondo blanco
        lines.append('#table(')
        lines.append('  columns: (1fr, 1fr),')
        lines.append('  stroke: none,')
        lines.append('  align: center,')
        lines.append(f'  [#image("{sig_kevin_path}", width: 4.8cm)], [#image("{sig_gerente_path}", width: 4.8cm)],')
        lines.append('  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) \n *kevin Mitnick* \n #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] \n #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],')
        lines.append('  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) \n *Ing. Roberto M. Gómez V.* \n #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] \n #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],')
        lines.append(')')
        if idx < len(actas_data) - 1:
            lines.append('#pagebreak()')
            lines.append('')

    with open(output_typ, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Compilar con Typst
    res = subprocess.run(["typst", "compile", output_typ, output_pdf], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"PDF Unificado generado exitosamente con Typst: {output_pdf}")
    else:
        print(f"Error compilando Typst: {res.stderr}")

if __name__ == "__main__":
    generar_docx_unificado()
    generar_pdf_typst()
