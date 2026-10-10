#!/usr/bin/env python3
import zipfile
import io
import xml.etree.ElementTree as ET

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
        "desc": "Experto en seguridad que asesora en la clasificación de severidad de incidentes, taxonomía de amenazas, monitoreo de alertas, protocolos de contención y políticas defensivas de ciberseguridad para el entorno empresarial."
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

# Construir filas de la tabla
tbl_rows_xml = ""
for item in roles_info:
    r = item["rol"]
    a = item["actor"]
    tbl_rows_xml += f"""<w:tr>
        <w:tc>
            <w:tcPr>
                <w:tcW w:type="dxa" w:w="4320"/>
                <w:vAlign w:val="center"/>
            </w:tcPr>
            <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>{r}</w:t></w:r></w:p>
        </w:tc>
        <w:tc>
            <w:tcPr>
                <w:tcW w:type="dxa" w:w="4320"/>
                <w:vAlign w:val="center"/>
            </w:tcPr>
            <w:p><w:r><w:t>{a}</w:t></w:r></w:p>
        </w:tc>
    </w:tr>"""

# Construir párrafos descriptivos
desc_paragraphs_xml = ""
for i, item in enumerate(roles_info, 1):
    r = item["rol"]
    a = item["actor"]
    d = item["desc"]
    desc_paragraphs_xml += f"""
    <w:p>
        <w:pPr>
            <w:spacing w:before="140" w:after="40"/>
        </w:pPr>
        <w:r>
            <w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="23476A"/></w:rPr>
            <w:t>{i}. {r}</w:t>
        </w:r>
        <w:r>
            <w:rPr><w:sz w:val="22"/><w:color w:val="555555"/></w:rPr>
            <w:t> — Actor: </w:t>
        </w:r>
        <w:r>
            <w:rPr><w:b/><w:i/><w:sz w:val="22"/><w:color w:val="111111"/></w:rPr>
            <w:t>{a}</w:t>
        </w:r>
    </w:p>
    <w:p>
        <w:pPr>
            <w:spacing w:before="20" w:after="140"/>
            <w:ind w:left="360"/>
        </w:pPr>
        <w:r>
            <w:rPr><w:sz w:val="21"/></w:rPr>
            <w:t>{d}</w:t>
        </w:r>
    </w:p>"""

new_doc_xml = f"""<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
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
            mc:Ignorable="w14 wp14">
<w:body>
    <w:p>
        <w:pPr><w:jc w:val="center"/><w:spacing w:after="140"/></w:pPr>
        <w:r>
            <w:rPr><w:b/><w:sz w:val="34"/><w:color w:val="23476A"/></w:rPr>
            <w:t>Proyecto SecureDesk - Dark Códex</w:t>
        </w:r>
    </w:p>
    <w:p>
        <w:pPr><w:jc w:val="center"/><w:spacing w:after="260"/></w:pPr>
        <w:r>
            <w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="333333"/></w:rPr>
            <w:t>Asignación de Roles del Proyecto</w:t>
        </w:r>
    </w:p>
    <w:tbl>
        <w:tblPr>
            <w:tblStyle w:val="TableGrid"/>
            <w:tblW w:type="auto" w:w="0"/>
            <w:jc w:val="center"/>
            <w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/>
        </w:tblPr>
        <w:tblGrid>
            <w:gridCol w:w="4320"/>
            <w:gridCol w:w="4320"/>
        </w:tblGrid>
        <w:tr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="4320"/><w:shd w:fill="23476A"/></w:tcPr>
                <w:p><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>Roles</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="4320"/><w:shd w:fill="23476A"/></w:tcPr>
                <w:p><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>Actores</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        {tbl_rows_xml}
    </w:tbl>
    <w:p>
        <w:pPr><w:spacing w:before="360" w:after="200"/></w:pPr>
        <w:r>
            <w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="23476A"/></w:rPr>
            <w:t>Descripción y Responsabilidades por Rol en SecureDesk</w:t>
        </w:r>
    </w:p>
    {desc_paragraphs_xml}
    <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
        <w:pgSz w:w="12240" w:h="15840"/>
        <w:pgMar w:top="1296" w:right="1800" w:bottom="1440" w:left="1800" w:header="720" w:footer="720" w:gutter="0"/>
        <w:cols w:space="720"/>
        <w:docGrid w:linePitch="360"/>
    </w:sectPr>
</w:body>
</w:document>"""

target_file = "esto   es lo  que  tienes  que hacer en base   nuestro securedesk.docx"
buffer = io.BytesIO()
with zipfile.ZipFile(target_file, "r") as zin:
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == "word/document.xml":
                zout.writestr(item, new_doc_xml.encode("utf-8"))
            else:
                zout.writestr(item, zin.read(item.filename))

with open(target_file, "wb") as f:
    f.write(buffer.getvalue())

print("Actualización completada exitosamente.")
