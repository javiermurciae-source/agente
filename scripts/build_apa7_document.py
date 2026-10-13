#!/usr/bin/env python3
"""
Constructor del documento oficial de entrega de la Fase 2 bajo la plantilla APA 7 de la UNAD:
'Plantilla_Normas_APA_7a_Edicion.docx' (ubicada en ~/Descargas)

Estudiante: Yeiny Alejandra Suarez Rodriguez (1003882193) - Grupo 346
Curso: Teoría de Sistemas en las Organizaciones (204016)
Tutor: Paola Maritza Rincon Nuñez
Organización: Alpina Productos Alimenticios S.A.S.
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

TEMPLATE_PATH = "/home/rootkit/Descargas/Plantilla_Normas_APA_7a_Edicion.docx"
DOCX_OUT_DESCARGAS = "/home/rootkit/Descargas/Fase_2_Yeiny_Suarez_APA7.docx"
DOCX_OUT_DOCUMENTOS = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Fase_2_Yeiny_Suarez_APA7.docx"
HTML_OUT = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Fase_2_Yeiny_Suarez_APA7.html"
PDF_OUT_DESCARGAS = "/home/rootkit/Descargas/Fase_2_Yeiny_Suarez_APA7.pdf"
PDF_OUT_DOCUMENTOS = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Fase_2_Yeiny_Suarez_APA7.pdf"

IMG_ESTADIO1 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio1_diagrama.png"
IMG_ESTADIO3 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio3_modelo_conceptual.png"


def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    """Aplica bordes específicos a una celda en formato Word XML."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in('w:tcBorders')
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    
    borders = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
    for border_name, border_style in borders.items():
        if border_style:
            tag = f'w:{border_name}'
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for k, v in border_style.items():
                element.set(qn(f'w:{k}'), str(v))
        else:
            tag = f'w:{border_name}'
            element = tcBorders.find(qn(tag))
            if element is not None:
                element.set(qn('w:val'), 'none')


def style_apa_table(table, col_widths=None):
    """Aplica formato de tabla real con cuadrícula completa y visible:
    - Borde superior e inferior reforzados (sz=8, color '334155').
    - Bordes izquierdo, derecho e internos nítidos (sz=4, color '94A3B8').
    - Fila de cabecera sombreada con fondo gris suave ('F1F5F9').
    - Repetición de encabezado en cambio de página (tblHeader).
    - Prevención de corte de fila a mitad de celda (cantSplit).
    - Padding interno de celda para legibilidad superior.
    """
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    tblPr = table._tbl.tblPr
    old_borders = tblPr.xpath('w:tblBorders')
    for b in old_borders:
        tblPr.remove(b)
        
    borders_xml = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="8" w:space="0" w:color="334155"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="334155"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="94A3B8"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="94A3B8"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders_xml)

    old_cell_mar = tblPr.xpath('w:tblCellMar')
    for m in old_cell_mar:
        tblPr.remove(m)
    cell_mar_xml = parse_xml(f'''
        <w:tblCellMar {nsdecls("w")}>
            <w:top w:w="120" w:type="dxa"/>
            <w:bottom w:w="120" w:type="dxa"/>
            <w:left w:w="160" w:type="dxa"/>
            <w:right w:w="160" w:type="dxa"/>
        </w:tblCellMar>
    ''')
    tblPr.append(cell_mar_xml)

    num_rows = len(table.rows)
    for r_idx, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        if not trPr.xpath('w:cantSplit'):
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            
        if r_idx == 0:
            if not trPr.xpath('w:tblHeader'):
                trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

        for c_idx, cell in enumerate(row.cells):
            tcPr = cell._tc.get_or_add_tcPr()
            if r_idx == 0:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
                tcPr.append(shd)
            elif r_idx % 2 == 1:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="FAFAFA"/>')
                tcPr.append(shd)

            vAlign = parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>')
            tcPr.append(vAlign)

            cell.paragraphs[0].paragraph_format.space_before = Pt(4)
            cell.paragraphs[0].paragraph_format.space_after = Pt(4)
            cell.paragraphs[0].paragraph_format.line_spacing = 1.15
            
            if col_widths and c_idx < len(col_widths):
                cell.width = Inches(col_widths[c_idx])



def build_apa7_document():
    print("Iniciando construcción de documento en plantilla APA 7 UNAD...")
    doc = docx.Document(TEMPLATE_PATH)
    
    # Limpiamos los elementos de relleno de la plantilla preservando sectPr, fuentes y estilos
    body = doc._body._element
    sectPr = body.xpath('w:sectPr')[0]
    for child in list(body):
        if child != sectPr:
            body.remove(child)

    # Configuración de márgenes a 2.54 cm (1 pulgada) para APA 7
    section = doc.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

    # =========================================================================
    # 1. PORTADA OFICIAL UNAD (APA 7)
    # =========================================================================
    def add_cover():
        p_title = doc.add_paragraph(style='No Spacing')
        p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_title.paragraph_format.space_before = Pt(40)
        p_title.paragraph_format.space_after = Pt(12)
        r_title = p_title.add_run("Fase 2 – Aplicando la Metodología de Sistemas Blandos\nAnálisis Sistémico de la Cadena de Frío y Gestión de Residuos en Alpina Productos Alimenticios S.A.S.")
        r_title.bold = True
        r_title.font.name = "Times New Roman"
        r_title.font.size = Pt(14)

        for _ in range(4):
            doc.add_paragraph("", style='No Spacing')

        p_author = doc.add_paragraph(style='No Spacing')
        p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_author.paragraph_format.space_after = Pt(4)
        r_aut = p_author.add_run("Yeiny Alejandra Suarez Rodriguez")
        r_aut.bold = True
        r_aut.font.name = "Times New Roman"
        r_aut.font.size = Pt(12)

        p_code = doc.add_paragraph(style='No Spacing')
        p_code.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_code.paragraph_format.space_after = Pt(12)
        r_code = p_code.add_run("Código / C.C.: 1003882193\nGrupo: 346")
        r_code.font.name = "Times New Roman"
        r_code.font.size = Pt(11)

        for _ in range(3):
            doc.add_paragraph("", style='No Spacing')

        p_tutor_lbl = doc.add_paragraph(style='No Spacing')
        p_tutor_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_tl = p_tutor_lbl.add_run("Tutor / Docente:")
        r_tl.font.name = "Times New Roman"
        r_tl.font.size = Pt(11)

        p_tutor = doc.add_paragraph(style='No Spacing')
        p_tutor.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_tutor.paragraph_format.space_after = Pt(12)
        r_tut = p_tutor.add_run("Paola Maritza Rincon Nuñez")
        r_tut.bold = True
        r_tut.font.name = "Times New Roman"
        r_tut.font.size = Pt(12)

        for _ in range(3):
            doc.add_paragraph("", style='No Spacing')

        p_inst = doc.add_paragraph(style='No Spacing')
        p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_inst = p_inst.add_run(
            "Universidad Nacional Abierta y a Distancia – UNAD\n"
            "Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)\n"
            "Programa de Ingeniería de Sistemas\n"
            "Curso: Teoría de Sistemas en las Organizaciones (Código: 204016)\n"
            "Octubre de 2026"
        )
        r_inst.font.name = "Times New Roman"
        r_inst.font.size = Pt(11)
        doc.add_page_break()

    add_cover()

    # =========================================================================
    # 2. INTRODUCCIÓN (Texto oficial de 225 palabras)
    # =========================================================================
    def add_intro():
        p_h = doc.add_paragraph(style='Heading 1')
        r = p_h.add_run("Introducción")
        r.bold = True

        p = doc.add_paragraph(style='Normal')
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(12)
        p.add_run(
            "El presente informe académico desarrolla de manera exhaustiva la aplicación de la Metodología de Sistemas "
            "Blandos (MSB), formulada por Peter Checkland (1999) y articulada en los referentes pedagógicos de la UNAD por "
            "González (2023) y Osorio Gómez (2007), a la empresa Alpina Productos Alimenticios S.A.S. Como organización "
            "perteneciente al sector agroindustrial de alimentos y bebidas, Alpina opera en un entorno complejo y dinámico donde "
            "interactúan múltiples actores humanos y técnicos: pequeños y medianos productores ganaderos en zonas rurales, "
            "transportistas de rutas de frío, operadores industriales en plantas procesadoras, canales de comercialización y "
            "consumidores finales. En este contexto sociotécnico, se ha identificado una problemática sistémica de vulnerabilidad "
            "en la cadena de frío y trazabilidad en el acopio rural de leche cruda, asociada a una baja circularidad en la gestión "
            "posconsumo de envases multicapa. Esta situación incide de forma directa en los Objetivos de Desarrollo Sostenible, "
            "particularmente en el ODS 12 (Producción y Consumo Responsables) y el ODS 9 (Industria, Innovación e Infraestructura). "
            "El documento estructura los seis estadios de la MSB: inicia con el reconocimiento gráfico de la situación problema, "
            "formula la definición raíz mediante el análisis CATWOE, construye el modelo conceptual con verbos de acción y bucles "
            "de control, contrasta la situación observada frente a la ideal y formula propuestas factibles junto con un plan de acción "
            "operativo para su materialización. Desde la perspectiva de la Ingeniería de Sistemas, este ejercicio evidencia cómo las "
            "tecnologías de la información, la telemetría IoT y los sistemas de información gerencial actúan como catalizadores para "
            "la sostenibilidad organizacional."
        )

    add_intro()

    # =========================================================================
    # 6. CARACTERIZACIÓN DE LA ORGANIZACIÓN
    # =========================================================================
    def add_org_profile():
        p_h = doc.add_paragraph(style='Heading 1')
        r = p_h.add_run("3. Caracterización de la Organización Seleccionada")
        r.bold = True

        p = doc.add_paragraph(style='Normal')
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(8)
        p.add_run(
            "Alpina Productos Alimenticios S.A.S. es una empresa multinacional colombiana de origen suizo fundada en 1945, "
            "con sede industrial principal en Sopó (Cundinamarca) y plantas adicionales en Caldas, Facatativá, Chinchiná y Popayán. "
            "Constituye uno de los referentes líderes en la industria de derivados lácteos, bebidas y alimentos en el mercado andino "
            "y norteamericano. Su actividad principal abarca la recepción, higienización, transformación industrial, empaque, logística "
            "refrigerada y distribución masiva de leche cruda y productos derivados como yogures, quesos madurados, postres y fórmulas nutricionales."
        )

        p2 = doc.add_paragraph(style='Normal')
        p2.paragraph_format.line_spacing = 1.5
        p2.paragraph_format.space_after = Pt(12)
        p2.add_run(
            "En el plano sociotécnico, Alpina articula una red de proveeduría conformada por más de 3.500 pequeños y medianos productores "
            "ganaderos campesinos distribuidos en las cuencas de Cundinamarca, Boyacá, Nariño y el Eje Cafetero. Esta estructura "
            "convierte a la empresa en un sistema abierto altamente sensible a las dinámicas geográficas rurales, la infraestructura vial, "
            "el cambio climático y las regulaciones sanitarias del INVIMA (Decreto 616 de 2006). A su vez, Alpina ha asumido compromisos "
            "públicos de carbono neutralidad y plástico neutralidad, orientando su gobernanza corporativa hacia modelos de economía "
            "circular y desarrollo territorial sostenible."
        )

    add_org_profile()

    # =========================================================================
    # 7. PROBLEMÁTICA ORGANIZACIONAL Y ARTICULACIÓN CON LOS ODS
    # =========================================================================
    def add_problem_and_sdgs():
        p_h = doc.add_paragraph(style='Heading 1')
        r = p_h.add_run("4. Problemática Organizacional y Relación con los ODS")
        r.bold = True

        p_h1 = doc.add_paragraph(style='Heading 2')
        r = p_h1.add_run("4.1 Articulación con los Objetivos de Desarrollo Sostenible (ODS 12 y 9)")
        r.bold = True

        p1 = doc.add_paragraph(style='Normal')
        p1.paragraph_format.line_spacing = 1.5
        p1.paragraph_format.space_after = Pt(8)
        p1.add_run(
            "La problemática central identificada en Alpina S.A.S. se manifiesta en una doble tensión operativa y ambiental: "
            "en primer lugar, la vulnerabilidad térmica y falta de monitoreo continuo en tiempo real en los tanques de enfriamiento "
            "de las fincas rurales lecheras, lo que incrementa el riesgo de proliferación bacteriana, acidificación y rechazo de lotes "
            "en planta; en segundo lugar, la insuficiente tasa de recuperación y reciclaje posconsumo de los envases multicapa (tetrapak "
            "y bolsas de polietileno de alta densidad), los cuales representan una fracción significativa de la huella de residuos de la compañía. "
            "Esta situación se articula directamente con el ODS 12: Producción y Consumo Responsables, específicamente con la Meta 12.3 "
            "(reducir a la mitad el desperdicio mundial de alimentos y reducir las pérdidas de alimentos a lo largo de las cadenas de producción "
            "y suministro) y la Meta 12.5 (reducir sustancialmente la generación de desechos mediante actividades de prevención, reducción, "
            "reciclado y reutilización)."
        )

        p_h2 = doc.add_paragraph(style='Heading 2')
        r = p_h2.add_run("4.2 Aporte Disciplinar de la Ingeniería de Sistemas")
        r.bold = True

        p2 = doc.add_paragraph(style='Normal')
        p2.paragraph_format.line_spacing = 1.5
        p2.paragraph_format.space_after = Pt(12)
        p2.add_run(
            "Esta problemática demanda imperativamente un abordaje desde el pensamiento sistémico blando propuesto por Peter Checkland (1999) "
            "y Osorio Gómez (2007), dado que no se trata de una falla mecánica aislada de los equipos de refrigeración, sino de un desajuste "
            "sociotécnico entre prácticas culturales campesinas, dispersión geográfica, protocolos de recepción y vacíos en los canales de "
            "retroalimentación de información. En este escenario, la Ingeniería de Sistemas aporta un valor transformador insustituible: "
            "tal como lo demuestran Marín y Rosas (2008), la disciplina permite diseñar arquitecturas de información distribuidas que integran "
            "telemetría IoT (sensores de temperatura y acidez de bajo consumo), conectividad móvil o satelital en zonas de baja cobertura, "
            "plataformas en la nube con analítica predictiva de rutas y sistemas de trazabilidad basados en códigos QR para la logística inversa. "
            "De este modo, la tecnología no se impone como un fin ciego, sino como un puente articulador que fortalece la toma de decisiones "
            "colaborativa entre campesinos, transportistas y directivos de calidad, en consonancia con el ODS 9 (Industria, Innovación e Infraestructura)."
        )

    add_problem_and_sdgs()

    # =========================================================================
    # 8. METODOLOGÍA DE SISTEMAS BLANDOS: LOS 6 ESTADIOS
    # =========================================================================
    def add_ssm_stages():
        p_h = doc.add_paragraph(style='Heading 1')
        r = p_h.add_run("5. Aplicación de la Metodología de Sistemas Blandos (Peter Checkland)")
        r.bold = True

        # --- ESTADIO 1 ---
        p_s1 = doc.add_paragraph(style='Heading 2')
        r = p_s1.add_run("5.1 Estadio 1: Reconocimiento de la Situación Problema")
        r.bold = True

        # Caption APA 7 de Figura 1
        p_fc = doc.add_paragraph(style='Normal')
        p_fc.paragraph_format.space_before = Pt(8)
        p_fc.paragraph_format.space_after = Pt(2)
        r_fbold = p_fc.add_run("Figura 1\n")
        r_fbold.bold = True
        r_ftitle = p_fc.add_run("Reconocimiento de la Situación Problema en Alpina Productos Alimenticios S.A.S.")
        r_ftitle.italic = True

        if os.path.exists(IMG_ESTADIO1):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(4)
            doc.add_picture(IMG_ESTADIO1, width=Inches(6.2))
            p_img._element.getparent().append(doc.paragraphs[-1]._element)

        p_fn = doc.add_paragraph(style='Normal')
        p_fn.paragraph_format.space_before = Pt(2)
        p_fn.paragraph_format.space_after = Pt(12)
        p_fn.paragraph_format.line_spacing = 1.15
        r_n = p_fn.add_run("Nota. ")
        r_n.italic = True
        p_fn.add_run(
            "Diagrama estructurado siguiendo la Metodología de Sistemas Blandos de Peter Checkland (1999) y las directrices pedagógicas "
            "de la UNAD (González, 2023). Integra la caracterización de actores, causas raíces, síntomas operacionales, consecuencias y "
            "la articulación con los ODS 12 y 9. Elaboración propia (2026)."
        )

        # Análisis narrativo del Estadio 1
        p_desc = doc.add_paragraph(style='Normal')
        p_desc.paragraph_format.line_spacing = 1.5
        p_desc.paragraph_format.space_after = Pt(12)
        p_desc.add_run(
            "El análisis de la situación no estructurada plasmado en la Figura 1 revela que la cadena de valor lechera opera bajo "
            "una fuerte interdependencia entre actores heterogéneos: más de 3.500 familias campesinas productoras, transportadores de "
            "camiones cisterna refrigerados, operarios de recepción en la planta de Sopó, ingenieros de sistemas y consumidores finales. "
            "Los síntomas centrales se evidencian en fluctuaciones térmicas que sobrepasan el umbral de los 4°C reglamentado por el INVIMA "
            "(Decreto 616 de 2006), generando hasta un 3.8% de pérdidas por acidez en periodos de congestión logística, sumado al bajo "
            "retorno de empaques plásticos post-consumo (apenas 22% de recuperación). Las causas raíces residen en la ausencia de telemetría "
            "en tanques de acopio veredales, tomas de muestras manuales lentas en bahías de descarga y la dispersión geográfica rural. Las "
            "consecuencias impactan económicamente a los campesinos (descuentos o rechazos de leche), generan sobrecostos por reprocesos "
            "y contradicen los compromisos corporativos de sostenibilidad, exigiendo una transformación sistémica."
        )

        # --- ESTADIO 2 ---
        p_s2 = doc.add_paragraph(style='Heading 2')
        r = p_s2.add_run("5.2 Estadio 2: Construcción de la Definición Raíz mediante CATWOE")
        r.bold = True

        p_tc1 = doc.add_paragraph(style='Normal')
        p_tc1.paragraph_format.space_before = Pt(8)
        p_tc1.paragraph_format.space_after = Pt(2)
        r_tbold = p_tc1.add_run("Tabla 1\n")
        r_tbold.bold = True
        r_ttitle = p_tc1.add_run("Análisis CATWOE Aplicado a Alpina Productos Alimenticios S.A.S.")
        r_ttitle.italic = True

        table1 = doc.add_table(rows=7, cols=3)
        style_apa_table(table1, col_widths=[1.6, 2.0, 2.9])

        headers1 = ["Elemento CATWOE", "Pregunta Guía", "Análisis Aplicado a Alpina S.A.S."]
        for i, h in enumerate(headers1):
            cell = table1.cell(0, i)
            cell.paragraphs[0].text = h
            cell.paragraphs[0].runs[0].bold = True

        catwoe_data = [
            ("Clientes (C)", "¿Quiénes se benefician o perjudican con el funcionamiento del sistema?", 
             "Beneficiarios directos: Consumidores finales de Alpina (garantía de inocuidad y frescura láctea) y más de 3.500 pequeños ganaderos campesinos (pago justo y oportuno sin penalizaciones injustificadas por acidificación de leche). Perjudicados potenciales ante fallas: Consumidores (riesgo de alteración organoléptica) y comunidades (impacto ambiental por residuos plásticos)."),
            
            ("Actores (A)", "¿Quién realiza las actividades del sistema?", 
             "Equipo de Ingeniería de Sistemas y TI (diseña e implementa la telemetría IoT y los sistemas de información gerencial), operarios de acopio y calidad en plantas (muestreo y recepción), transportistas de cisternas refrigeradas y productores lecheros capacitados en buenas prácticas térmicas."),
            
            ("Transformación (T)", "¿Qué entra al sistema, qué proceso experimenta y qué producto sale?", 
             "Entrada (E): Cadena de suministro agroindustrial lechera con monitoreo térmico discontinuo en acopio rural, pérdidas de producto y manejo pasivo de residuos plásticos.\nProceso de Transformación: Implementación de una arquitectura sociotécnica integral que articula telemetría IoT en tanques de enfriamiento, pruebas rápidas automatizadas en planta, capacitación técnica a ganaderos y un sistema colaborativo de logística inversa de empaques.\nSalida (S): Cadena de valor láctea resiliente, trazable y digitalizada en tiempo real, con pérdidas de leche reducidas a menos del 0.8% y un modelo de economía circular con tasas de recuperación de envases superiores al 30%."),
            
            ("Cosmovisión (W)", "¿Qué perspectiva o visión del mundo da sentido a este sistema?", 
             "La convicción corporativa y social de que la competitividad agroindustrial y la rentabilidad empresarial deben articularse armónicamente con la justicia económica campesina, la excelencia sanitaria y la sostenibilidad ambiental (economía circular), asumiendo que la tecnología es un medio facilitador del desarrollo rural y no un fin meramente tecnicista."),
            
            ("Dueños (O)", "¿Quién tiene la autoridad para modificar o cancelar el sistema?", 
             "La Junta Directiva, la Presidencia Corporativa y las Gerencias de Operaciones, Cadena de Suministro y Tecnologías de la Información de Alpina Productos Alimenticios S.A.S., quienes asignan presupuestos de inversión y aprueban políticas corporativas."),
            
            ("Restricciones ambientales (E)", "¿Qué factores externos limitan o condicionan el sistema?", 
             "Normatividad sanitaria del INVIMA (Decreto 616 de 2006 sobre cadena de frío estricta de leche cruda), Ley 2232 de 2022 (reducción gradual de plásticos de un solo uso), dispersión geográfica y topografía quebrada de las cuencas rurales lecheras, limitaciones de cobertura de conectividad celular en veredas apartadas y presupuestos financieros asignados por la empresa.")
        ]

        for row_idx, data in enumerate(catwoe_data, start=1):
            for col_idx, text in enumerate(data):
                cell = table1.cell(row_idx, col_idx)
                cell.paragraphs[0].text = text
                if col_idx == 0:
                    cell.paragraphs[0].runs[0].bold = True

        p_tn1 = doc.add_paragraph(style='Normal')
        p_tn1.paragraph_format.space_before = Pt(3)
        p_tn1.paragraph_format.space_after = Pt(12)
        p_tn1.paragraph_format.line_spacing = 1.15
        r_n = p_tn1.add_run("Nota. ")
        r_n.italic = True
        p_tn1.add_run("Marco de análisis CATWOE adaptado según las pautas de Peter Checkland (1999) y Osorio Gómez (2007). Elaboración propia (2026).")

        # Redacción formal de la Definición Raíz
        p_hdr = doc.add_paragraph(style='Heading 2')
        r = p_hdr.add_run("Definición Raíz del Sistema")
        r.bold = True

        p_dr = doc.add_paragraph(style='Normal')
        p_dr.paragraph_format.line_spacing = 1.5
        p_dr.paragraph_format.space_after = Pt(12)
        p_dr.paragraph_format.left_indent = Inches(0.4)
        p_dr.paragraph_format.right_indent = Inches(0.4)
        r_dr = p_dr.add_run(
            "«Un sistema de actividad humana perteneciente a Alpina Productos Alimenticios S.A.S., coordinado por la Gerencia "
            "de Operaciones, TI y Sostenibilidad, con el propósito de transformar una cadena de acopio lechero rural caracterizada "
            "por monitoreo térmico reactivo y baja recuperación de empaques, en una cadena de valor trazable, digitalizada y circular; "
            "mediante el despliegue de telemetría IoT en centros de enfriamiento veredales, la automatización analítica de recepción en "
            "planta, la formación técnica campesina y la articulación de redes de logística inversa de residuos; con el fin de garantizar "
            "la inocuidad microbiológica, erradicar el desperdicio de alimento lácteo (ODS 12.3) y dignificar los ingresos de las familias "
            "ganaderas rurales; bajo la cosmovisión de que la calidad alimentaria y la sostenibilidad ambiental constituyen un ecosistema "
            "indivisible; dentro de las restricciones sanitarias del INVIMA (Decreto 616/2006), la legislación ambiental de plásticos "
            "y las condiciones geográficas de la ruralidad colombiana»."
        )
        r_dr.italic = True

        # --- ESTADIO 3 ---
        p_s3 = doc.add_paragraph(style='Heading 2')
        r = p_s3.add_run("5.3 Estadio 3: Elaboración del Modelo Conceptual")
        r.bold = True

        # Caption APA 7 de Figura 2
        p_fc2 = doc.add_paragraph(style='Normal')
        p_fc2.paragraph_format.space_before = Pt(8)
        p_fc2.paragraph_format.space_after = Pt(2)
        r_fbold2 = p_fc2.add_run("Figura 2\n")
        r_fbold2.bold = True
        r_ftitle2 = p_fc2.add_run("Modelo Conceptual del Sistema de Actividades Humanas y Bucles de Control")
        r_ftitle2.italic = True

        if os.path.exists(IMG_ESTADIO3):
            p_img2 = doc.add_paragraph()
            p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img2.paragraph_format.space_before = Pt(4)
            p_img2.paragraph_format.space_after = Pt(4)
            doc.add_picture(IMG_ESTADIO3, width=Inches(6.2))
            p_img2._element.getparent().append(doc.paragraphs[-1]._element)

        p_fn2 = doc.add_paragraph(style='Normal')
        p_fn2.paragraph_format.space_before = Pt(2)
        p_fn2.paragraph_format.space_after = Pt(12)
        p_fn2.paragraph_format.line_spacing = 1.15
        r_n2 = p_fn2.add_run("Nota. ")
        r_n2.italic = True
        p_fn2.add_run(
            "Modelo conceptual derivado de la Definición Raíz. Las actividades humanas se expresan en verbos en infinitivo dentro de un "
            "subsistema operacional y un subsistema de monitoreo y control articulado por las 3 'E' (Eficacia, Eficiencia y Efectividad) "
            "según Checkland (1999) y Jerardino (2019). Elaboración propia (2026)."
        )

        p_mcdesc = doc.add_paragraph(style='Normal')
        p_mcdesc.paragraph_format.line_spacing = 1.5
        p_mcdesc.paragraph_format.space_after = Pt(12)
        p_mcdesc.add_run(
            "El modelo conceptual estructurado en la Figura 2 operacionaliza la Definición Raíz a través de dos niveles sistémicos interactivos:\n\n"
            "1. Subsistema Operacional (Actividades del Mundo Real):\n"
            "• Actividad 1 (Monitorear): Monitorear en tiempo real variables térmicas (2°C a 4°C) y fisicoquímicas mediante dispositivos IoT sumergibles instalados en los tanques de enfriamiento veredales.\n"
            "• Actividad 2 (Validar y Recepcionar): Validar automáticamente la inocuidad lechera mediante analizadores rápidos conectados por telemetría a la balanza y silos de recepción en planta.\n"
            "• Actividad 3 (Integrar): Integrar telemetría de tanques, logística de transporte cisterna y registros de pesaje en un Sistema de Información Gerencial en la nube.\n"
            "• Actividad 4 (Gestionar Logística Inversa): Establecer puntos limpios de depósito de envases multicapa en canales de distribución masiva y acuerdos con cooperativas de reciclaje.\n\n"
            "2. Subsistema de Monitoreo y Control Gerencial (Las 3 'E' de Checkland):\n"
            "• Eficacia (E1 - ¿Funciona el sistema para lograr el objetivo?): Medir la tasa de preservación térmica de leche recepcionada dentro de los parámetros de inocuidad reglamentarios (Meta: ≥ 99.5%).\n"
            "• Eficiencia (E2 - ¿Se logra con el mínimo de recursos y pérdidas?): Evaluar la reducción porcentual de desperdicio de leche en transporte y el tiempo de ciclo por cisterna en planta (Meta: ≤ 0.8% de mermas).\n"
            "• Efectividad (E3 - ¿Cumple el propósito a largo plazo en su entorno?): Evaluar la fidelización de las comunidades campesinas y el cumplimiento de las metas corporativas de plástico neutro y ODS 12."
        )

        # --- ESTADIO 4 ---
        p_s4 = doc.add_paragraph(style='Heading 2')
        r = p_s4.add_run("5.4 Estadio 4: Comparación de la Situación Actual con el Modelo Conceptual")
        r.bold = True

        p_tc2 = doc.add_paragraph(style='Normal')
        p_tc2.paragraph_format.space_before = Pt(8)
        p_tc2.paragraph_format.space_after = Pt(2)
        r_tbold2 = p_tc2.add_run("Tabla 2\n")
        r_tbold2.bold = True
        r_ttitle2 = p_tc2.add_run("Comparación entre la Situación Actual y el Modelo Conceptual")
        r_ttitle2.italic = True

        table2 = doc.add_table(rows=5, cols=4)
        style_apa_table(table2, col_widths=[1.6, 1.7, 1.7, 1.5])

        headers2 = ["Actividad Humana (Modelo Conceptual)", "Situación Actual Observada en Alpina", "Situación Propuesta (Modelo Conceptual)", "Oportunidad de Mejora Identificada"]
        for i, h in enumerate(headers2):
            cell = table2.cell(0, i)
            cell.paragraphs[0].text = h
            cell.paragraphs[0].runs[0].bold = True

        comp_data = [
            ("Monitorear en tiempo real variables térmicas y de calidad en acopio rural.",
             "Monitoreo térmico manual y discontinuo en fincas; registros en papel o planillas físicas propensas a errores o pérdidas.",
             "Instalación de dispositivos IoT con sensores de temperatura y acidez sumergibles con conectividad satelital/GSM y alertas automáticas en la nube.",
             "Detección y alerta temprana ante cualquier alteración de la cadena de frío, evitando que leche acidificada sea cargada en camiones cisterna colectivos."),
            
            ("Validar inocuidad lechera y recepcionar con protocolos automatizados en planta.",
             "Toma de muestras manual y tiempos de espera de pruebas microbiológicas de 45 a 90 minutos por cisterna, generando cuellos de botella en bahías de descarga.",
             "Integración de espectrofotometría rápida conectada por API al sistema central de control de silos para descarga automatizada en menos de 20 minutos.",
             "Reducción sustancial del tiempo de ciclo en bahías, menor calentamiento pasivo de la leche y trazabilidad digital del lote desde su finca de origen."),
            
            ("Integrar telemetría e inventarios en una plataforma gerencial centralizada.",
             "Sistemas de información desarticulados entre logística de campo, transporte contratado y control industrial de planta.",
             "Arquitectura digital centralizada donde cada lote lechero cuenta con gemelo digital visible para planificadores, transportistas y calidad.",
             "Visibilidad holística de inventarios, optimización predictiva de rutas de recolección y liquidación ágil y transparente a productores campesinos."),
            
            ("Gestionar logística inversa de empaques posconsumo y aprovechamiento de residuos.",
             "Manejo pasivo de residuos posconsumo delegado en terceros; recuperación inferior al 22% de empaques multicapa colocados en el mercado.",
             "Red corporativa de puntos de acopio de envases en grandes superficies y centros urbanos vinculada a plantas de valorización de reciclaje.",
             "Aumento significativo en la tasa de aprovechamiento de plástico y cartón, cumplimiento estricto de la Ley 2232 y fortalecimiento de la reputación de marca.")
        ]

        for row_idx, data in enumerate(comp_data, start=1):
            for col_idx, text in enumerate(data):
                cell = table2.cell(row_idx, col_idx)
                cell.paragraphs[0].text = text
                if col_idx == 0:
                    cell.paragraphs[0].runs[0].bold = True

        p_tn2 = doc.add_paragraph(style='Normal')
        p_tn2.paragraph_format.space_before = Pt(3)
        p_tn2.paragraph_format.space_after = Pt(12)
        p_tn2.paragraph_format.line_spacing = 1.15
        r_n = p_tn2.add_run("Nota. ")
        r_n.italic = True
        p_tn2.add_run("Contraste empírico entre el modelo de Checkland (1999) y la operación observada en Alpina S.A.S. Elaboración propia (2026).")

        # --- ESTADIO 5 ---
        p_s5 = doc.add_paragraph(style='Heading 2')
        r = p_s5.add_run("5.5 Estadio 5: Definición de Cambios Factibles y Deseables")
        r.bold = True

        p_tc3 = doc.add_paragraph(style='Normal')
        p_tc3.paragraph_format.space_before = Pt(8)
        p_tc3.paragraph_format.space_after = Pt(2)
        r_tbold3 = p_tc3.add_run("Tabla 3\n")
        r_tbold3.bold = True
        r_ttitle3 = p_tc3.add_run("Cambios Factibles y Deseables para Alpina S.A.S.")
        r_ttitle3.italic = True

        table3 = doc.add_table(rows=5, cols=4)
        style_apa_table(table3, col_widths=[1.6, 2.0, 1.5, 1.4])

        headers3 = ["Cambio Propuesto", "Justificación Sistémica", "Responsable Organizacional", "Impacto Esperado"]
        for i, h in enumerate(headers3):
            cell = table3.cell(0, i)
            cell.paragraphs[0].text = h
            cell.paragraphs[0].runs[0].bold = True

        changes_data = [
            ("Implementación de telemetría IoT y tableros de control en rutas de acopio rural.",
             "Permite superar la ceguera operativa entre las fincas campesinas y la planta central, asegurando que cualquier anomalía de temperatura sea notificada de inmediato.",
             "Gerencia de Tecnologías de la Información (TI) y Dirección de Abastecimiento Lechero.",
             "Disminución del 80% en pérdidas de leche por acidez y garantía del 100% de cumplimiento del Decreto 616 del INVIMA."),
            
            ("Estandarización y automatización del protocolo de recepción rápida en planta Sopó.",
             "Agiliza la validación de inocuidad microbiológica mediante analizadores rápidos integrados al ERP, eliminando las demoras de las cisternas en bahía de descarga.",
             "Dirección de Calidad e Inocuidad y Jefatura de Operaciones Industriales.",
             "Reducción del 65% en los tiempos de espera de los vehículos de transporte y reducción de la huella de carbono asociada al ralentí."),
            
            ("Programa integral de capacitación y corresponsabilidad con ganaderos campesinos.",
             "El pensamiento sistémico blando establece que las intervenciones tecnológicas fracasan si los actores humanos no comprenden ni comparten el propósito del sistema.",
             "Dirección de Fomento Ganadero y Relaciones Agrícolas / Extensión Rural.",
             "Fortalecimiento de la confianza y fidelización de más de 3.500 familias productoras, con cero rechazos injustificados de producto."),
            
            ("Estrategia colaborativa de logística inversa y economía circular de empaques.",
             "Responde de manera vinculante a las exigencias regulatorias de la Ley 2232 de 2022 y a las metas globales de sostenibilidad del ODS 12.",
             "Gerencia de Sostenibilidad y Dirección Comercial / Canales de Distribución.",
             "Recuperación y reincorporación de al menos el 30% del volumen de plástico y cartón multicapa puesto en el mercado nacional.")
        ]

        for row_idx, data in enumerate(changes_data, start=1):
            for col_idx, text in enumerate(data):
                cell = table3.cell(row_idx, col_idx)
                cell.paragraphs[0].text = text
                if col_idx == 0:
                    cell.paragraphs[0].runs[0].bold = True

        p_tn3 = doc.add_paragraph(style='Normal')
        p_tn3.paragraph_format.space_before = Pt(3)
        p_tn3.paragraph_format.space_after = Pt(12)
        p_tn3.paragraph_format.line_spacing = 1.15
        r_n = p_tn3.add_run("Nota. ")
        r_n.italic = True
        p_tn3.add_run("Propuestas estructuradas bajo el postulado de Peter Checkland: 'Sistémicamente deseables y culturalmente factibles'. Elaboración propia (2026).")

        # --- ESTADIO 6 ---
        p_s6 = doc.add_paragraph(style='Heading 2')
        r = p_s6.add_run("5.6 Estadio 6: Diseño del Plan de Acción")
        r.bold = True

        p_tc4 = doc.add_paragraph(style='Normal')
        p_tc4.paragraph_format.space_before = Pt(8)
        p_tc4.paragraph_format.space_after = Pt(2)
        r_tbold4 = p_tc4.add_run("Tabla 4\n")
        r_tbold4.bold = True
        r_ttitle4 = p_tc4.add_run("Plan de Acción para la Implementación de las Mejoras")
        r_ttitle4.italic = True

        table4 = doc.add_table(rows=5, cols=5)
        style_apa_table(table4, col_widths=[1.5, 1.2, 1.2, 1.1, 1.5])

        headers4 = ["Acción Priorizada", "Responsable", "Recursos Asignados", "Tiempo Estimado", "Indicador de Seguimiento (KPI)"]
        for i, h in enumerate(headers4):
            cell = table4.cell(0, i)
            cell.paragraphs[0].text = h
            cell.paragraphs[0].runs[0].bold = True

        action_data = [
            ("Adquisición, calibración e instalación de dispositivos IoT de telemetría en centros de acopio.",
             "Ingeniero Líder de TI y Especialista en Infraestructura IoT.",
             "Sensores industriales sumergibles, módulos GSM/LoRaWAN, plataforma Cloud (AWS IoT Core). Presupuesto: $140M COP.",
             "Meses 1 a 3 (Semanas 1 a 12)",
             "Porcentaje de cobertura de telemetría activa:\n(Tanques monitoreados / Total tanques) × 100\nMeta: ≥ 95%"),
            
            ("Despliegue del módulo de recepción rápida automatizada en laboratorio de planta Sopó.",
             "Líder de Sistemas de Información y Analista de Procesos de Calidad.",
             "Equipos espectrofotométricos de flujo continuo, terminales táctiles, APIs de integración con SAP. Presupuesto: $85M COP.",
             "Meses 2 a 4 (Semanas 8 a 16)",
             "Tiempo promedio de ciclo de descarga por vehículo cisterna:\nMinutos por camión en bahía\nMeta: ≤ 25 min (Línea base: 75 min)"),
            
            ("Ejecución de la Escuela Campesina de Cadena de Frío y Sostenibilidad Rural.",
             "Coordinador de Extensión Agropecuaria y Asistencia Técnica Rural.",
             "Kits portátiles de verificación térmica, material pedagógico digital y presencial, refrigerios. Presupuesto: $35M COP.",
             "Meses 2 a 5 (Semanas 6 a 20)",
             "Porcentaje de ganaderos capacitados y certificados:\n(Ganaderos certificados / Total ganaderos) × 100\nMeta: ≥ 90%"),
            
            ("Instalación de puntos limpios de depósito de envases e incentivos de economía circular.",
             "Coordinador de Economía Circular y Gerente de Canales de Distribución.",
             "Contenedores de depósito selectivo, incentivos comerciales a clientes, convenios con recicladores. Presupuesto: $60M COP.",
             "Meses 3 a 6 (Semanas 12 a 24)",
             "Tasa de recuperación y aprovechamiento de empaques:\n(Toneladas recuperadas / Toneladas puestas en mercado) × 100\nMeta: ≥ 30%")
        ]

        for row_idx, data in enumerate(action_data, start=1):
            for col_idx, text in enumerate(data):
                cell = table4.cell(row_idx, col_idx)
                cell.paragraphs[0].text = text
                if col_idx == 0:
                    cell.paragraphs[0].runs[0].bold = True

        p_tn4 = doc.add_paragraph(style='Normal')
        p_tn4.paragraph_format.space_before = Pt(3)
        p_tn4.paragraph_format.space_after = Pt(12)
        p_tn4.paragraph_format.line_spacing = 1.15
        r_n = p_tn4.add_run("Nota. ")
        r_n.italic = True
        p_tn4.add_run("Cronograma operativo estructurado en horizontes de ejecución bimestrales e indicadores cuantitativos verificables. Elaboración propia (2026).")

    add_ssm_stages()

    # =========================================================================
    # 9. CONCLUSIONES
    # =========================================================================
    def add_conclusions():
        p_h = doc.add_paragraph(style='Heading 1')
        r = p_h.add_run("6. Conclusiones")
        r.bold = True

        conclusions = [
            "La aplicación de la Metodología de Sistemas Blandos (MSB) de Peter Checkland demostró ser un marco conceptual y metodológico excepcionalmente eficaz para comprender y abordar la complejidad sociotécnica de Alpina Productos Alimenticios S.A.S. A diferencia de los enfoques reduccionistas tradicionales, la MSB permitió trascender el análisis de fallas mecánicas aisladas e integrar dialécticamente las cosmovisiones disímiles de ganaderos campesinos, transportistas, operarios industriales y directivos de sostenibilidad corporativa.",
            
            "El análisis CATWOE y la formulación rigurosa de la Definición Raíz en el Estadio 2, sustentados en las directrices de Osorio Gómez (2007) y González (2023), resultaron determinantes para clarificar el propósito teleológico de la organización. Este ejercicio permitió redefinir a Alpina no solo como una planta procesadora de derivados lácteos, sino como un macrosistema socioecológico extendido donde la calidad sanitaria, la justicia económica rural y la sostenibilidad ambiental operan de manera indisolublemente vinculada.",
            
            "La contrastación dialéctica efectuada en el Estadio 4 evidenció que las mayores brechas del sistema radicaban en la desconexión de flujos de información en tiempo real entre los centros de enfriamiento veredales y la planta central de Sopó. Desde la perspectiva de la Ingeniería de Sistemas (Marín y Rosas, 2008), la incorporación de telemetría IoT, redes inalámbricas y plataformas de información gerencial en la nube demostró ser el catalizador tecnológico indispensable para habilitar bucles de control y retroalimentación efectivos.",
            
            "El plan de acción estructurado en el Estadio 6 operacionaliza las propuestas de mejora bajo los criterios de evaluación de las 3 'E' (Eficacia, Eficiencia y Efectividad) expuestos por Checkland (1999) y Jerardino (2019). Al establecer indicadores cuantitativos rigurosos como la cobertura de telemetría (≥ 95%) y la tasa de recuperación de empaques multicapa (≥ 30%), el informe valida que las intervenciones tecnológicas generan un impacto tangible y medible sobre las metas del ODS 12 (Producción y Consumo Responsables) y el ODS 9 (Industria, Innovación e Infraestructura)."
        ]

        for i, c in enumerate(conclusions, start=1):
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.left_indent = Inches(0.25)
            r_num = p.add_run(f"6.{i} ")
            r_num.bold = True
            p.add_run(c)

    add_conclusions()

    # =========================================================================
    # 10. REFERENCIAS BIBLIOGRÁFICAS (APA 7 - Sangría francesa estricta)
    # =========================================================================
    def add_references():
        doc.add_page_break()
        p_h = doc.add_paragraph(style='Heading 1')
        p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p_h.add_run("7. Referencias Bibliográficas")
        r.bold = True

        references = [
            ("Alpina Productos Alimenticios S.A.S. (2024). ", "Informe de Sostenibilidad y Economía Circular 2023", ". Publicaciones Corporativas Alpina. https://www.alpina.com/sostenibilidad"),
            ("Checkland, P. (1999). ", "Systems Thinking, Systems Practice: Soft Systems Methodology in Action", ". John Wiley & Sons."),
            ("Checkland, P., & Scholes, J. (1990). ", "Soft Systems Methodology in Action", ". John Wiley & Sons."),
            ("González, Y. A. (2023). ", "Metodología de Sistemas Blandos (MSB)", " [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/58695"),
            ("Jerardino Wiesenborn, B. (2019). ", "Metodología de Sistemas Blandos: Conceptos claves", " [Video]. YouTube. https://www.youtube.com/watch?v=2pzJsWjk12E"),
            ("Kast, F. E., & Rosenzweig, J. E. (1988). ", "Administración en las organizaciones: Enfoque de sistemas y de contingencias", " (4.ª ed.). McGraw-Hill."),
            ("Le Moigne, J. L. (1990). ", "La teoría del sistema general: Teoría del modelado", ". Fondo Editorial de la Pontificia Universidad Católica del Perú."),
            ("Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. ", "CIENCIA ergo-sum", ", 15(1), 45-53. https://dialnet.unirioja.es/servlet/articulo?codigo=5034963"),
            ("Naciones Unidas. (2015). ", "Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible", ". Organización de las Naciones Unidas. https://sdgs.un.org/es/goals"),
            ("Osorio Gómez, J. C. (2007). ", "Introducción al pensamiento sistémico", ". Programa Editorial Universidad del Valle. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/129056?page=10"),
            ("Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. ", "Systemic Practice and Action Research", ", 37, 1123–1140. https://doi.org/10.1007/s11213-024-09689-9"),
            ("Von Bertalanffy, L. (1968). ", "General System Theory: Foundations, Development, Applications", ". George Braziller.")
        ]

        for author_year, italic_title, publisher_url in references:
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.first_line_indent = Inches(-0.5)  # Sangría francesa APA 7
            
            p.add_run(author_year)
            r_it = p.add_run(italic_title)
            r_it.italic = True
            p.add_run(publisher_url)

    add_references()

    # Guardar versiones DOCX
    print(f"💾 Guardando DOCX en Descargas: {DOCX_OUT_DESCARGAS}")
    doc.save(DOCX_OUT_DESCARGAS)

    print(f"💾 Guardando DOCX en Documentos: {DOCX_OUT_DOCUMENTOS}")
    doc.save(DOCX_OUT_DOCUMENTOS)
    print("✅ Documentos DOCX generados con éxito.")


def export_pdf_via_chromium():
    """Genera una versión HTML estilizada con CSS idéntico a APA 7 para exportar a PDF vía Chromium."""
    print("🌐 Generando versión HTML para exportación pixel-perfect a PDF...")
    
    css = """
    @page {
        size: letter;
        margin: 2.54cm;
        @bottom-right {
            content: counter(page);
            font-family: 'Times New Roman', serif;
            font-size: 11pt;
        }
    }
    body {
        font-family: 'Times New Roman', Times, serif;
        font-size: 12pt;
        line-height: 1.5;
        color: #111;
        margin: 0;
        padding: 0;
        text-align: justify;
    }
    h1, h2, h3 {
        font-family: 'Times New Roman', Times, serif;
        color: #000;
        page-break-after: avoid;
    }
    h1 {
        font-size: 13pt;
        font-weight: bold;
        margin-top: 24pt;
        margin-bottom: 12pt;
        text-align: left;
    }
    h2 {
        font-size: 12pt;
        font-weight: bold;
        margin-top: 18pt;
        margin-bottom: 8pt;
        text-align: left;
    }
    .cover-page {
        page-break-after: always;
        text-align: center;
        padding-top: 2.5cm;
    }
    .cover-title {
        font-size: 14pt;
        font-weight: bold;
        line-height: 1.4;
        margin-bottom: 3.5cm;
    }
    .cover-author {
        font-size: 12pt;
        font-weight: bold;
        margin-bottom: 4pt;
    }
    .cover-sub {
        font-size: 11pt;
        margin-bottom: 3cm;
    }
    .cover-inst {
        font-size: 11pt;
        line-height: 1.4;
    }
    .page-break {
        page-break-after: always;
    }
    .center-heading {
        text-align: center;
        font-size: 13pt;
        font-weight: bold;
        margin-bottom: 18pt;
    }
    .caption-title {
        font-size: 11pt;
        margin-bottom: 4pt;
        page-break-after: avoid;
        text-align: left;
    }
    .caption-title strong {
        display: block;
    }
    .caption-title em {
        font-style: italic;
    }
    .caption-note {
        font-size: 10pt;
        line-height: 1.3;
        margin-top: 6pt;
        margin-bottom: 18pt;
        page-break-before: avoid;
        text-align: justify;
    }
    .img-container {
        text-align: center;
        margin: 10pt 0;
        page-break-inside: avoid;
    }
    .img-container img {
        max-width: 100%;
        height: auto;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.1);
    }
    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 10pt;
        line-height: 1.35;
        margin: 14pt 0;
        page-break-inside: auto;
    }
    table th {
        border-top: 2pt solid #1E293B;
        border-bottom: 2pt solid #1E293B;
        border-left: 0.75pt solid #94A3B8;
        border-right: 0.75pt solid #94A3B8;
        padding: 8pt 8pt;
        font-weight: bold;
        text-align: left;
        background-color: #F1F5F9;
        color: #0F172A;
    }
    table td {
        padding: 7pt 8pt;
        border: 0.75pt solid #CBD5E1;
        vertical-align: top;
        color: #1E293B;
    }
    table tr:nth-child(even) td {
        background-color: #F8FAFC;
    }
    table tr:last-child td {
        border-bottom: 2pt solid #1E293B;
    }
    .reference-item {
        padding-left: 0.5in;
        text-indent: -0.5in;
        margin-bottom: 10pt;
        line-height: 1.4;
    }
    .root-def {
        margin: 14pt 1.5cm;
        font-style: italic;
        background-color: #fcfcfc;
        border-left: 3pt solid #333;
        padding: 8pt 14pt;
        font-size: 11pt;
        line-height: 1.4;
    }
    .toc-item {
        display: flex;
        justify-content: space-between;
        margin-bottom: 4pt;
        font-size: 11pt;
    }
    .dots {
        flex-grow: 1;
        border-bottom: 1px dotted #999;
        margin: 0 5px 4px 5px;
    }
    """

    # Generamos el HTML usando los textos procesados
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Fase 2 - Yeiny Alejandra Suarez Rodriguez - Normas APA 7</title>
    <style>{css}</style>
</head>
<body>

<!-- PORTADA -->
<div class="cover-page">
    <div class="cover-title">
        Fase 2 – Aplicando la Metodología de Sistemas Blandos<br>
        Análisis Sistémico de la Cadena de Frío y Gestión de Residuos en Alpina Productos Alimenticios S.A.S.
    </div>
    
    <div class="cover-author">Yeiny Alejandra Suarez Rodriguez</div>
    <div class="cover-sub">
        Código / C.C.: 1003882193<br>
        Grupo: 346<br><br>
        <strong>Tutor / Docente:</strong><br>
        Paola Maritza Rincon Nuñez
    </div>
    
    <div class="cover-inst">
        Universidad Nacional Abierta y a Distancia – UNAD<br>
        Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)<br>
        Programa de Ingeniería de Sistemas<br>
        Curso: Teoría de Sistemas en las Organizaciones (Código: 204016)<br>
        Octubre de 2026
    </div>
</div>

<!-- CONTENIDO -->
<h1>Introducción</h1>

<h1>3. Caracterización de la Organización Seleccionada</h1>
<p>
Alpina Productos Alimenticios S.A.S. es una empresa multinacional colombiana de origen suizo fundada en 1945, 
con sede industrial principal en Sopó (Cundinamarca) y plantas adicionales en Caldas, Facatativá, Chinchiná y Popayán. 
Constituye uno de los referentes líderes en la industria de derivados lácteos, bebidas y alimentos en el mercado andino 
y norteamericano. Su actividad principal abarca la recepción, higienización, transformación industrial, empaque, logística 
refrigerada y distribución masiva de leche cruda y productos derivados como yogures, quesos madurados, postres y fórmulas nutricionales.
</p>
<p>
En el plano sociotécnico, Alpina articula una red de proveeduría conformada por más de 3.500 pequeños y medianos productores 
ganaderos campesinos distribuidos en las cuencas de Cundinamarca, Boyacá, Nariño y el Eje Cafetero. Esta estructura 
convierte a la empresa en un sistema abierto altamente sensible a las dinámicas geográficas rurales, la infraestructura vial, 
el cambio climático y las regulaciones sanitarias del INVIMA (Decreto 616 de 2006). A su vez, Alpina ha asumido compromisos 
públicos de carbono neutralidad y plástico neutralidad, orientando su gobernanza corporativa hacia modelos de economía 
circular y desarrollo territorial sostenible.
</p>

<h1>4. Problemática Organizacional y Relación con los ODS</h1>
<h2>4.1 Articulación con los Objetivos de Desarrollo Sostenible (ODS 12 y 9)</h2>
<p>
La problemática central identificada en Alpina S.A.S. se manifiesta en una doble tensión operativa y ambiental: 
en primer lugar, la vulnerabilidad térmica y falta de monitoreo continuo en tiempo real en los tanques de enfriamiento 
de las fincas rurales lecheras, lo que incrementa el riesgo de proliferación bacteriana, acidificación y rechazo de lotes 
en planta; en segundo lugar, la insuficiente tasa de recuperación y reciclaje posconsumo de los envases multicapa (tetrapak 
y bolsas de polietileno de alta densidad), los cuales representan una fracción significativa de la huella de residuos de la compañía. 
Esta situación se articula directamente con el ODS 12: Producción y Consumo Responsables, específicamente con la Meta 12.3 
(reducir a la mitad el desperdicio mundial de alimentos y reducir las pérdidas de alimentos a lo largo de las cadenas de producción 
y suministro) y la Meta 12.5 (reducir sustancialmente la generación de desechos mediante actividades de prevención, reducción, 
reciclado y reutilización).
</p>

<h2>4.2 Aporte Disciplinar de la Ingeniería de Sistemas</h2>
<p>
Esta problemática demanda imperativamente un abordaje desde el pensamiento sistémico blando propuesto por Peter Checkland (1999) 
y Osorio Gómez (2007), dado que no se trata de una falla mecánica aislada de los equipos de refrigeración, sino de un desajuste 
sociotécnico entre prácticas culturales campesinas, dispersión geográfica, protocolos de recepción y vacíos en los canales de 
retroalimentación de información. En este escenario, la Ingeniería de Sistemas aporta un valor transformador insustituible: 
tal como lo demuestran Marín y Rosas (2008), la disciplina permite diseñar arquitecturas de información distribuidas que integran 
telemetría IoT (sensores de temperatura y acidez de bajo consumo), conectividad móvil o satelital en zonas de baja cobertura, 
plataformas en la nube con analítica predictiva de rutas y sistemas de trazabilidad basados en códigos QR para la logística inversa. 
De este modo, la tecnología no se impone como un fin ciego, sino como un puente articulador que fortalece la toma de decisiones 
colaborativa entre campesinos, transportistas y directivos de calidad, en consonancia con el ODS 9 (Industria, Innovación e Infraestructura).
</p>

<h1>5. Aplicación de la Metodología de Sistemas Blandos (Peter Checkland)</h1>

<h2>5.1 Estadio 1: Reconocimiento de la Situación Problema</h2>
<div class="caption-title">
    <strong>Figura 1</strong>
    <em>Reconocimiento de la Situación Problema en Alpina Productos Alimenticios S.A.S.</em>
</div>
<div class="img-container">
    <img src="{IMG_ESTADIO1}" alt="Estadio 1 - Situación Problema">
</div>
<div class="caption-note">
    <em>Nota.</em> Diagrama estructurado siguiendo la Metodología de Sistemas Blandos de Peter Checkland (1999) y las directrices pedagógicas 
    de la UNAD (González, 2023). Integra la caracterización de actores, causas raíces, síntomas operacionales, consecuencias y 
    la articulación con los ODS 12 y 9. Elaboración propia (2026).
</div>
<p>
El análisis de la situación no estructurada plasmado en la Figura 1 revela que la cadena de valor lechera opera bajo 
una fuerte interdependencia entre actores heterogéneos: más de 3.500 familias campesinas productoras, transportadores de 
camiones cisterna refrigerados, operarios de recepción en la planta de Sopó, ingenieros de sistemas y consumidores finales. 
Los síntomas centrales se evidencian en fluctuaciones térmicas que sobrepasan el umbral de los 4°C reglamentado por el INVIMA 
(Decreto 616 de 2006), generando hasta un 3.8% de pérdidas por acidez en periodos de congestión logística, sumado al bajo 
retorno de empaques plásticos post-consumo (apenas 22% de recuperación). Las causas raíces residen en la ausencia de telemetría 
en tanques de acopio veredales, tomas de muestras manuales lentas en bahías de descarga y la dispersión geográfica rural. Las 
consecuencias impactan económicamente a los campesinos (descuentos o rechazos de leche), generan sobrecostos por reprocesos 
y contradicen los compromisos corporativos de sostenibilidad, exigiendo una transformación sistémica.
</p>

<h2>5.2 Estadio 2: Construcción de la Definición Raíz mediante CATWOE</h2>
<div class="caption-title">
    <strong>Tabla 1</strong>
    <em>Análisis CATWOE Aplicado a Alpina Productos Alimenticios S.A.S.</em>
</div>
<table>
    <thead>
        <tr>
            <th style="width: 22%;">Elemento CATWOE</th>
            <th style="width: 30%;">Pregunta Guía</th>
            <th style="width: 48%;">Análisis Aplicado a Alpina S.A.S.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Clientes (C)</strong></td>
            <td>¿Quiénes se benefician o perjudican con el funcionamiento del sistema?</td>
            <td>Beneficiarios directos: Consumidores finales de Alpina (garantía de inocuidad y frescura láctea) y más de 3.500 pequeños ganaderos campesinos (pago justo y oportuno sin penalizaciones injustificadas por acidificación de leche). Perjudicados potenciales ante fallas: Consumidores (riesgo de alteración organoléptica) y comunidades (impacto ambiental por residuos plásticos).</td>
        </tr>
        <tr>
            <td><strong>Actores (A)</strong></td>
            <td>¿Quién realiza las actividades del sistema?</td>
            <td>Equipo de Ingeniería de Sistemas y TI (diseña e implementa la telemetría IoT y los sistemas de información gerencial), operarios de acopio y calidad en plantas (muestreo y recepción), transportistas de cisternas refrigeradas y productores lecheros capacitados en buenas prácticas térmicas.</td>
        </tr>
        <tr>
            <td><strong>Transformación (T)</strong></td>
            <td>¿Qué entra al sistema, qué proceso experimenta y qué producto sale?</td>
            <td><strong>Entrada (E):</strong> Cadena de suministro agroindustrial lechera con monitoreo térmico discontinuo en acopio rural, pérdidas de producto y manejo pasivo de residuos plásticos.<br>
            <strong>Proceso de Transformación:</strong> Implementación de una arquitectura sociotécnica integral que articula telemetría IoT en tanques de enfriamiento, pruebas rápidas automatizadas en planta, capacitación técnica a ganaderos y un sistema colaborativo de logística inversa de empaques.<br>
            <strong>Salida (S):</strong> Cadena de valor láctea resiliente, trazable y digitalizada en tiempo real, con pérdidas de leche reducidas a menos del 0.8% y un modelo de economía circular con tasas de recuperación de envases superiores al 30%.</td>
        </tr>
        <tr>
            <td><strong>Cosmovisión (W)</strong></td>
            <td>¿Qué perspectiva o visión del mundo da sentido a este sistema?</td>
            <td>La convicción corporativa y social de que la competitividad agroindustrial y la rentabilidad empresarial deben articularse armónicamente con la justicia económica campesina, la excelencia sanitaria y la sostenibilidad ambiental (economía circular), asumiendo que la tecnología es un medio facilitador del desarrollo rural y no un fin meramente tecnicista.</td>
        </tr>
        <tr>
            <td><strong>Dueños (O)</strong></td>
            <td>¿Quién tiene la autoridad para modificar o cancelar el sistema?</td>
            <td>La Junta Directiva, la Presidencia Corporativa y las Gerencias de Operaciones, Cadena de Suministro y Tecnologías de la Información de Alpina Productos Alimenticios S.A.S., quienes asignan presupuestos de inversión y aprueban políticas corporativas.</td>
        </tr>
        <tr>
            <td><strong>Restricciones ambientales (E)</strong></td>
            <td>¿Qué factores externos limitan o condicionan el sistema?</td>
            <td>Normatividad sanitaria del INVIMA (Decreto 616 de 2006 sobre cadena de frío estricta de leche cruda), Ley 2232 de 2022 (reducción gradual de plásticos de un solo uso), dispersión geográfica y topografía quebrada de las cuencas rurales lecheras, limitaciones de cobertura de conectividad celular en veredas apartadas y presupuestos financieros asignados por la empresa.</td>
        </tr>
    </tbody>
</table>
<div class="caption-note">
    <em>Nota.</em> Marco de análisis CATWOE adaptado según las pautas de Peter Checkland (1999) y Osorio Gómez (2007). Elaboración propia (2026).
</div>

<h2>Definición Raíz del Sistema</h2>
<div class="root-def">
«Un sistema de actividad humana perteneciente a Alpina Productos Alimenticios S.A.S., coordinado por la Gerencia 
de Operaciones, TI y Sostenibilidad, con el propósito de transformar una cadena de acopio lechero rural caracterizada 
por monitoreo térmico reactivo y baja recuperación de empaques, en una cadena de valor trazable, digitalizada y circular; 
mediante el despliegue de telemetría IoT en centros de enfriamiento veredales, la automatización analítica de recepción en 
planta, la formación técnica campesina y la articulación de redes de logística inversa de residuos; con el fin de garantizar 
la inocuidad microbiológica, erradicar el desperdicio de alimento lácteo (ODS 12.3) y dignificar los ingresos de las familias 
ganaderas rurales; bajo la cosmovisión de que la calidad alimentaria y la sostenibilidad ambiental constituyen un ecosistema 
indivisible; dentro de las restricciones sanitarias del INVIMA (Decreto 616/2006), la legislación ambiental de plásticos 
y las condiciones geográficas de la ruralidad colombiana».
</div>

<h2>5.3 Estadio 3: Elaboración del Modelo Conceptual</h2>
<div class="caption-title">
    <strong>Figura 2</strong>
    <em>Modelo Conceptual del Sistema de Actividades Humanas y Bucles de Control</em>
</div>
<div class="img-container">
    <img src="{IMG_ESTADIO3}" alt="Estadio 3 - Modelo Conceptual">
</div>
<div class="caption-note">
    <em>Nota.</em> Modelo conceptual derivado de la Definición Raíz. Las actividades humanas se expresan en verbos en infinitivo dentro de un 
    subsistema operacional y un subsistema de monitoreo y control articulado por las 3 'E' (Eficacia, Eficiencia y Efectividad) 
    según Checkland (1999) y Jerardino (2019). Elaboración propia (2026).
</div>
<p>
El modelo conceptual estructurado en la Figura 2 operacionaliza la Definición Raíz a través de dos niveles sistémicos interactivos:
</p>
<p><strong>1. Subsistema Operacional (Actividades del Mundo Real):</strong><br>
• <em>Actividad 1 (Monitorear):</em> Monitorear en tiempo real variables térmicas (2°C a 4°C) y fisicoquímicas mediante dispositivos IoT sumergibles instalados en los tanques de enfriamiento veredales.<br>
• <em>Actividad 2 (Validar y Recepcionar):</em> Validar automáticamente la inocuidad lechera mediante analizadores rápidos conectados por telemetría a la balanza y silos de recepción en planta.<br>
• <em>Actividad 3 (Integrar):</em> Integrar telemetría de tanques, logística de transporte cisterna y registros de pesaje en un Sistema de Información Gerencial en la nube.<br>
• <em>Actividad 4 (Gestionar Logística Inversa):</em> Establecer puntos limpios de depósito de envases multicapa en canales de distribución masiva y acuerdos con cooperativas de reciclaje.
</p>
<p><strong>2. Subsistema de Monitoreo y Control Gerencial (Las 3 'E' de Checkland):</strong><br>
• <em>Eficacia (E1 - ¿Funciona el sistema para lograr el objetivo?):</em> Medir la tasa de preservación térmica de leche recepcionada dentro de los parámetros de inocuidad reglamentarios (Meta: ≥ 99.5%).<br>
• <em>Eficiencia (E2 - ¿Se logra con el mínimo de recursos y pérdidas?):</em> Evaluar la reducción porcentual de desperdicio de leche en transporte y el tiempo de ciclo por cisterna en planta (Meta: ≤ 0.8% de mermas).<br>
• <em>Efectividad (E3 - ¿Cumple el propósito a largo plazo en su entorno?):</em> Evaluar la fidelización de las comunidades campesinas y el cumplimiento de las metas corporativas de plástico neutro y ODS 12.
</p>

<h2>5.4 Estadio 4: Comparación de la Situación Actual con el Modelo Conceptual</h2>
<div class="caption-title">
    <strong>Tabla 2</strong>
    <em>Comparación entre la Situación Actual y el Modelo Conceptual</em>
</div>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">Actividad Humana (Modelo Conceptual)</th>
            <th style="width: 25%;">Situación Actual Observada en Alpina</th>
            <th style="width: 25%;">Situación Propuesta (Modelo Conceptual)</th>
            <th style="width: 25%;">Oportunidad de Mejora Identificada</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Monitorear en tiempo real variables térmicas y de calidad en acopio rural.</strong></td>
            <td>Monitoreo térmico manual y discontinuo en fincas; registros en papel o planillas físicas propensas a errores o pérdidas.</td>
            <td>Instalación de dispositivos IoT con sensores de temperatura y acidez sumergibles con conectividad satelital/GSM y alertas automáticas en la nube.</td>
            <td>Detección y alerta temprana ante cualquier alteración de la cadena de frío, evitando que leche acidificada sea cargada en camiones cisterna colectivos.</td>
        </tr>
        <tr>
            <td><strong>Validar inocuidad lechera y recepcionar con protocolos automatizados en planta.</strong></td>
            <td>Toma de muestras manual y tiempos de espera de pruebas microbiológicas de 45 a 90 minutos por cisterna, generando cuellos de botella en bahías de descarga.</td>
            <td>Integración de espectrofotometría rápida conectada por API al sistema central de control de silos para descarga automatizada en menos de 20 minutos.</td>
            <td>Reducción sustancial del tiempo de ciclo en bahías, menor calentamiento pasivo de la leche y trazabilidad digital del lote desde su finca de origen.</td>
        </tr>
        <tr>
            <td><strong>Integrar telemetría e inventarios en una plataforma gerencial centralizada.</strong></td>
            <td>Sistemas de información desarticulados entre logística de campo, transporte contratado y control industrial de planta.</td>
            <td>Arquitectura digital centralizada donde cada lote lechero cuenta con gemelo digital visible para planificadores, transportistas y calidad.</td>
            <td>Visibilidad holística de inventarios, optimización predictiva de rutas de recolección y liquidación ágil y transparente a productores campesinos.</td>
        </tr>
        <tr>
            <td><strong>Gestionar logística inversa de empaques posconsumo y aprovechamiento de residuos.</strong></td>
            <td>Manejo pasivo de residuos posconsumo delegado en terceros; recuperación inferior al 22% de empaques multicapa colocados en el mercado.</td>
            <td>Red corporativa de puntos de acopio de envases en grandes superficies y centros urbanos vinculada a plantas de valorización de reciclaje.</td>
            <td>Aumento significativo en la tasa de aprovechamiento de plástico y cartón, cumplimiento estricto de la Ley 2232 y fortalecimiento de la reputación de marca.</td>
        </tr>
    </tbody>
</table>
<div class="caption-note">
    <em>Nota.</em> Contraste empírico entre el modelo de Checkland (1999) y la operación observada en Alpina S.A.S. Elaboración propia (2026).
</div>

<h2>5.5 Estadio 5: Definición de Cambios Factibles y Deseables</h2>
<div class="caption-title">
    <strong>Tabla 3</strong>
    <em>Cambios Factibles y Deseables para Alpina S.A.S.</em>
</div>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">Cambio Propuesto</th>
            <th style="width: 30%;">Justificación Sistémica</th>
            <th style="width: 22%;">Responsable Organizacional</th>
            <th style="width: 23%;">Impacto Esperado</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Implementación de telemetría IoT y tableros de control en rutas de acopio rural.</strong></td>
            <td>Permite superar la ceguera operativa entre las fincas campesinas y la planta central, asegurando que cualquier anomalía de temperatura sea notificada de inmediato.</td>
            <td>Gerencia de Tecnologías de la Información (TI) y Dirección de Abastecimiento Lechero.</td>
            <td>Disminución del 80% en pérdidas de leche por acidez y garantía del 100% de cumplimiento del Decreto 616 del INVIMA.</td>
        </tr>
        <tr>
            <td><strong>Estandarización y automatización del protocolo de recepción rápida en planta Sopó.</strong></td>
            <td>Agiliza la validación de inocuidad microbiológica mediante analizadores rápidos integrados al ERP, eliminando las demoras de las cisternas en bahía de descarga.</td>
            <td>Dirección de Calidad e Inocuidad y Jefatura de Operaciones Industriales.</td>
            <td>Reducción del 65% en los tiempos de espera de los vehículos de transporte y reducción de la huella de carbono asociada al ralentí.</td>
        </tr>
        <tr>
            <td><strong>Programa integral de capacitación y corresponsabilidad con ganaderos campesinos.</strong></td>
            <td>El pensamiento sistémico blando establece que las intervenciones tecnológicas fracasan si los actores humanos no comprenden ni comparten el propósito del sistema.</td>
            <td>Dirección de Fomento Ganadero y Relaciones Agrícolas / Extensión Rural.</td>
            <td>Fortalecimiento de la confianza y fidelización de más de 3.500 familias productoras, con cero rechazos injustificados de producto.</td>
        </tr>
        <tr>
            <td><strong>Estrategia colaborativa de logística inversa y economía circular de empaques.</strong></td>
            <td>Responde de manera vinculante a las exigencias regulatorias de la Ley 2232 de 2022 y a las metas globales de sostenibilidad del ODS 12.</td>
            <td>Gerencia de Sostenibilidad y Dirección Comercial / Canales de Distribución.</td>
            <td>Recuperación y reincorporación de al menos el 30% del volumen de plástico y cartón multicapa puesto en el mercado nacional.</td>
        </tr>
    </tbody>
</table>
<div class="caption-note">
    <em>Nota.</em> Propuestas estructuradas bajo el postulado de Peter Checkland: 'Sistémicamente deseables y culturalmente factibles'. Elaboración propia (2026).
</div>

<h2>5.6 Estadio 6: Diseño del Plan de Acción</h2>
<div class="caption-title">
    <strong>Tabla 4</strong>
    <em>Plan de Acción para la Implementación de las Mejoras</em>
</div>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">Acción Priorizada</th>
            <th style="width: 18%;">Responsable</th>
            <th style="width: 20%;">Recursos Asignados</th>
            <th style="width: 15%;">Tiempo Estimado</th>
            <th style="width: 22%;">Indicador de Seguimiento (KPI)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Adquisición, calibración e instalación de dispositivos IoT de telemetría en centros de acopio.</strong></td>
            <td>Ingeniero Líder de TI y Especialista en Infraestructura IoT.</td>
            <td>Sensores industriales sumergibles, módulos GSM/LoRaWAN, plataforma Cloud (AWS IoT Core). Presupuesto: $140M COP.</td>
            <td>Meses 1 a 3 (Semanas 1 a 12)</td>
            <td><strong>Porcentaje de cobertura de telemetría activa:</strong><br>
            <em>(Tanques monitoreados / Total tanques) × 100</em><br>
            Meta: ≥ 95%</td>
        </tr>
        <tr>
            <td><strong>Despliegue del módulo de recepción rápida automatizada en laboratorio de planta Sopó.</strong></td>
            <td>Líder de Sistemas de Información y Analista de Procesos de Calidad.</td>
            <td>Equipos espectrofotométricos de flujo continuo, terminales táctiles, APIs de integración con SAP. Presupuesto: $85M COP.</td>
            <td>Meses 2 a 4 (Semanas 8 a 16)</td>
            <td><strong>Tiempo promedio de ciclo de descarga por vehículo cisterna:</strong><br>
            <em>Minutos por camión en bahía</em><br>
            Meta: ≤ 25 min (Línea base: 75 min)</td>
        </tr>
        <tr>
            <td><strong>Ejecución de la Escuela Campesina de Cadena de Frío y Sostenibilidad Rural.</strong></td>
            <td>Coordinador de Extensión Agropecuaria y Asistencia Técnica Rural.</td>
            <td>Kits portátiles de verificación térmica, material pedagógico digital y presencial, refrigerios. Presupuesto: $35M COP.</td>
            <td>Meses 2 a 5 (Semanas 6 a 20)</td>
            <td><strong>Porcentaje de ganaderos capacitados y certificados:</strong><br>
            <em>(Ganaderos certificados / Total ganaderos) × 100</em><br>
            Meta: ≥ 90%</td>
        </tr>
        <tr>
            <td><strong>Instalación de puntos limpios de depósito de envases e incentivos de economía circular.</strong></td>
            <td>Coordinador de Economía Circular y Gerente de Canales de Distribución.</td>
            <td>Contenedores de depósito selectivo, incentivos comerciales a clientes, convenios con recicladores. Presupuesto: $60M COP.</td>
            <td>Meses 3 a 6 (Semanas 12 a 24)</td>
            <td><strong>Tasa de recuperación y aprovechamiento de empaques:</strong><br>
            <em>(Toneladas recuperadas / Toneladas puestas en mercado) × 100</em><br>
            Meta: ≥ 30%</td>
        </tr>
    </tbody>
</table>
<div class="caption-note">
    <em>Nota.</em> Cronograma operativo estructurado en horizontes de ejecución bimestrales e indicadores cuantitativos verificables. Elaboración propia (2026).
</div>

<h1>6. Conclusiones</h1>
<p>
<strong>6.1</strong> La aplicación de la Metodología de Sistemas Blandos (MSB) de Peter Checkland demostró ser un marco conceptual y metodológico excepcionalmente eficaz para comprender y abordar la complejidad sociotécnica de Alpina Productos Alimenticios S.A.S. A diferencia de los enfoques reduccionistas tradicionales, la MSB permitió trascender el análisis de fallas mecánicas aisladas e integrar dialécticamente las cosmovisiones disímiles de ganaderos campesinos, transportistas, operarios industriales y directivos de sostenibilidad corporativa.
</p>
<p>
<strong>6.2</strong> El análisis CATWOE y la formulación rigurosa de la Definición Raíz en el Estadio 2, sustentados en las directrices de Osorio Gómez (2007) y González (2023), resultaron determinantes para clarificar el propósito teleológico de la organización. Este ejercicio permitió redefinir a Alpina no solo como una planta procesadora de derivados lácteos, sino como un macrosistema socioecológico extendido donde la calidad sanitaria, la justicia económica rural y la sostenibilidad ambiental operan de manera indisolublemente vinculada.
</p>
<p>
<strong>6.3</strong> La contrastación dialéctica efectuada en el Estadio 4 evidenció que las mayores brechas del sistema radicaban en la desconexión de flujos de información en tiempo real entre los centros de enfriamiento veredales y la planta central de Sopó. Desde la perspectiva de la Ingeniería de Sistemas (Marín y Rosas, 2008), la incorporación de telemetría IoT, redes inalámbricas y plataformas de información gerencial en la nube demostró ser el catalizador tecnológico indispensable para habilitar bucles de control y retroalimentación efectivos.
</p>
<p>
<strong>6.4</strong> El plan de acción estructurado en el Estadio 6 operacionaliza las propuestas de mejora bajo los criterios de evaluación de las 3 'E' (Eficacia, Eficiencia y Efectividad) expuestos por Checkland (1999) y Jerardino (2019). Al establecer indicadores cuantitativos rigurosos como la cobertura de telemetría (≥ 95%) y la tasa de recuperación de empaques multicapa (≥ 30%), el informe valida que las intervenciones tecnológicas generan un impacto tangible y medible sobre las metas del ODS 12 (Producción y Consumo Responsables) y el ODS 9 (Industria, Innovación e Infraestructura).
</p>

<div class="page-break"></div>

<div class="center-heading">7. Referencias Bibliográficas</div>
<div class="reference-item">Alpina Productos Alimenticios S.A.S. (2024). <em>Informe de Sostenibilidad y Economía Circular 2023</em>. Publicaciones Corporativas Alpina. https://www.alpina.com/sostenibilidad</div>
<div class="reference-item">Checkland, P. (1999). <em>Systems Thinking, Systems Practice: Soft Systems Methodology in Action</em>. John Wiley & Sons.</div>
<div class="reference-item">Checkland, P., & Scholes, J. (1990). <em>Soft Systems Methodology in Action</em>. John Wiley & Sons.</div>
<div class="reference-item">González, Y. A. (2023). <em>Metodología de Sistemas Blandos (MSB)</em> [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/58695</div>
<div class="reference-item">Jerardino Wiesenborn, B. (2019). <em>Metodología de Sistemas Blandos: Conceptos claves</em> [Video]. YouTube. https://www.youtube.com/watch?v=2pzJsWjk12E</div>
<div class="reference-item">Kast, F. E., & Rosenzweig, J. E. (1988). <em>Administración en las organizaciones: Enfoque de sistemas y de contingencias</em> (4.ª ed.). McGraw-Hill.</div>
<div class="reference-item">Le Moigne, J. L. (1990). <em>La teoría del sistema general: Teoría del modelado</em>. Fondo Editorial de la Pontificia Universidad Católica del Perú.</div>
<div class="reference-item">Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. <em>CIENCIA ergo-sum</em>, 15(1), 45-53. https://dialnet.unirioja.es/servlet/articulo?codigo=5034963</div>
<div class="reference-item">Naciones Unidas. (2015). <em>Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible</em>. Organización de las Naciones Unidas. https://sdgs.un.org/es/goals</div>
<div class="reference-item">Osorio Gómez, J. C. (2007). <em>Introducción al pensamiento sistémico</em>. Programa Editorial Universidad del Valle. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/129056?page=10</div>
<div class="reference-item">Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. <em>Systemic Practice and Action Research</em>, 37, 1123–1140. https://doi.org/10.1007/s11213-024-09689-9</div>
<div class="reference-item">Von Bertalanffy, L. (1968). <em>General System Theory: Foundations, Development, Applications</em>. George Braziller.</div>

</body>
</html>
"""
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ HTML APA 7 generado: {HTML_OUT}")

    import subprocess
    import shutil

    print("🖨️ Exportando PDF limpio con Chromium...")
    cmd = [
        "/opt/google/chrome/chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_OUT_DOCUMENTOS}",
        f"file://{HTML_OUT}"
    ]
    subprocess.run(cmd, check=True)

    shutil.copyfile(PDF_OUT_DOCUMENTOS, PDF_OUT_DESCARGAS)
    print(f"✅ PDF guardado en Documentos: {PDF_OUT_DOCUMENTOS}")
    print(f"✅ PDF guardado en Descargas: {PDF_OUT_DESCARGAS}")


if __name__ == "__main__":
    build_apa7_document()
    export_pdf_via_chromium()
    print("🎉 ¡Proceso finalizado exitosamente!")
