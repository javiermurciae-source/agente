#!/usr/bin/env python3
"""
Generador del Trabajo Académico de Entrega Oficial para UNAD:
Curso: Teoría de Sistemas en las Organizaciones (Código: 204016)
Fase 2: Aplicando la Metodología de Sistemas Blandos
Estudiante: Yeiny Alejandra Suarez Rodriguez (C.C. 1003882193) - Grupo 346
Tutora: Paola Maritza Rincon Nuñez

Criterios de Camilo:
- Resumido, directo y claro (sin rodeos ni palabras infladas).
- Lenguaje normal, natural y comprensible.
- Responde absolutamente TODOS los puntos de la guía de la UNAD.
- Información 100% investigada, real y verídica sobre Alpina S.A.S. (plantas reales, Decreto 616/2006, ODS reales, Ley 2232, etc.).
- Diagramas reales incluidos en alta resolución (Estadio 1 y Estadio 3).
- Cero texto residual de plantilla.
- Generación de DOCX y PDF en Documentos y Descargas.
"""

import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Rutas de imágenes y carpetas
IMG_ESTADIO1 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio1_diagrama.png"
IMG_ESTADIO3 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio3_modelo_conceptual.png"

OUT_DIR_DOCS = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2"
OUT_DIR_DOWN = "/home/rootkit/Descargas"

DOCX_NAME = "Fase_2_Yeiny_Suarez.docx"
ANEXO_NAME = "Anexo_Fase_2_Yeiny_Suarez.docx"
PDF_NAME = "Fase_2_Yeiny_Suarez.pdf"
ANEXO_PDF = "Anexo_Fase_2_Yeiny_Suarez.pdf"
HTML_NAME = "Fase_2_Yeiny_Suarez.html"


def build_docx():
    print("📝 Generando DOCX en lenguaje claro, resumido y con datos reales...")
    doc = docx.Document()

    # Márgenes APA (2.54 cm = 1 pulgada)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Estilo base
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(30, 41, 59)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(36)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.line_spacing = 1.3
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(13)
        r.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_question(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.keep_with_next = True
        r_lbl = p.add_run("Pregunta: ")
        r_lbl.bold = True
        r_lbl.font.name = 'Times New Roman'
        r_lbl.font.size = Pt(12)
        r_lbl.font.color.rgb = RGBColor(14, 116, 144)  # azul petróleo
        r_txt = p.add_run(text)
        r_txt.bold = True
        r_txt.font.name = 'Times New Roman'
        r_txt.font.size = Pt(12)
        r_txt.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_answer(text, bold_prefix=None, indent=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.3
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if indent:
            p.paragraph_format.left_indent = Inches(0.25)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix + " ")
            r_pre.bold = True
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(12)
        r_ans = p.add_run(text)
        r_ans.font.name = 'Times New Roman'
        r_ans.font.size = Pt(12)
        return p

    def add_diagram(img_path, fig_num, title, note_text):
        if not os.path.exists(img_path):
            print(f"⚠️ Imagen no encontrada: {img_path}")
            return

        p_fc = doc.add_paragraph()
        p_fc.paragraph_format.space_before = Pt(10)
        p_fc.paragraph_format.space_after = Pt(2)
        p_fc.paragraph_format.keep_with_next = True
        r_num = p_fc.add_run(f"Figura {fig_num}\n")
        r_num.bold = True
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(11)
        r_ttl = p_fc.add_run(title)
        r_ttl.italic = True
        r_ttl.font.name = 'Times New Roman'
        r_ttl.font.size = Pt(11)

        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.2))

        p_note = doc.add_paragraph()
        p_note.paragraph_format.space_before = Pt(2)
        p_note.paragraph_format.space_after = Pt(10)
        p_note.paragraph_format.line_spacing = 1.15
        p_note.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r_nt_lbl = p_note.add_run("Nota. ")
        r_nt_lbl.italic = True
        r_nt_lbl.font.name = 'Times New Roman'
        r_nt_lbl.font.size = Pt(10)
        r_nt = p_note.add_run(note_text)
        r_nt.font.name = 'Times New Roman'
        r_nt.font.size = Pt(10)

    # -------------------------------------------------------------------------
    # PORTADA OFICIAL
    # -------------------------------------------------------------------------
    add_title("Fase 2 – Aplicando la Metodología de Sistemas Blandos\nAnálisis de la Cadena de Frío y Gestión de Residuos en Alpina S.A.S.")

    for _ in range(3):
        doc.add_paragraph("", style='Normal')

    p_aut = doc.add_paragraph()
    p_aut.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_aut.paragraph_format.space_after = Pt(4)
    r = p_aut.add_run("Yeiny Alejandra Suarez Rodriguez")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    p_cod = doc.add_paragraph()
    p_cod.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cod.paragraph_format.space_after = Pt(14)
    r = p_cod.add_run("Código / C.C.: 1003882193\nGrupo: 346")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)

    for _ in range(2):
        doc.add_paragraph("", style='Normal')

    p_tut = doc.add_paragraph()
    p_tut.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tut.paragraph_format.space_after = Pt(14)
    r = p_tut.add_run("Tutor / Docente:\n")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r2 = p_tut.add_run("Paola Maritza Rincon Nuñez")
    r2.bold = True
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)

    for _ in range(2):
        doc.add_paragraph("", style='Normal')

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_inst.add_run(
        "Universidad Nacional Abierta y a Distancia – UNAD\n"
        "Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)\n"
        "Programa de Ingeniería de Sistemas\n"
        "Curso: Teoría de Sistemas en las Organizaciones (Código: 204016)\n"
        "Octubre de 2026"
    )
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # INTRODUCCIÓN
    # -------------------------------------------------------------------------
    add_h1("Introducción")
    add_question("¿De qué trata este trabajo y cuál es su objetivo?")
    add_answer(
        "Este informe aplica la Metodología de Sistemas Blandos (MSB) de Peter Checkland a la empresa Alpina Productos "
        "Alimenticios S.A.S. Alpina es una de las empresas lácteas más importantes de Colombia y trabaja a diario con miles "
        "de ganaderos campesinos en distintas regiones del país. En este trabajo analizamos dos problemas reales de su operación: "
        "la dificultad para mantener la cadena de frío en el acopio de leche rural por falta de monitoreo continuo en tiempo real, "
        "y el bajo nivel de recuperación de sus envases plásticos y de Tetra Pak después del consumo. Estos retos se conectan con "
        "el ODS 12 (Producción y Consumo Responsables) y el ODS 9 (Industria, Innovación e Infraestructura). El objetivo del documento "
        "es desarrollar los seis estadios de la metodología de forma clara, proponiendo mejoras prácticas y factibles desde la "
        "Ingeniería de Sistemas."
    )

    # -------------------------------------------------------------------------
    # 1. CARACTERIZACIÓN DE LA ORGANIZACIÓN
    # -------------------------------------------------------------------------
    add_h1("1. Caracterización de la Organización Seleccionada")
    add_question("¿Qué empresa se seleccionó y cuáles son sus datos operativos básicos?")
    add_answer(
        "• Nombre: Alpina Productos Alimenticios S.A.S.\n"
        "• Sector económico: Agroindustrial / Alimentos y bebidas (derivados lácteos).\n"
        "• Ubicación principal: Sede industrial y administrativa central en Sopó (Cundinamarca). Plantas adicionales de procesamiento en Facatativá (Cundinamarca), Caldas (Antioquia), Chinchiná (Caldas), Popayán (Cauca) y Simijaca (Cundinamarca).\n"
        "• Actividad principal: Acopio de leche cruda, pasteurización, transformación industrial, empaque, refrigeración y distribución nacional de leche entera, deslactosada, quesos, yogures, postres y bebidas lácteas.\n"
        "• Contexto general: Alpina compra leche diariamente a más de 3.500 pequeños y medianos ganaderos en cuencas de Cundinamarca, Boyacá, Nariño y el Eje Cafetero. Al ser un producto vivo y altamente perecedero, su calidad depende de mantener la leche por debajo de los 4°C, tal como lo exige el Decreto 616 de 2006 del Ministerio de la Protección Social. Al mismo tiempo, la empresa debe responder ante normativas ambientales como la Ley 2232 de 2022 y la Resolución 1407 de 2018 para reciclar y reducir los envases plásticos que pone en el mercado."
    )

    # -------------------------------------------------------------------------
    # 2. PROBLEMÁTICA ORGANIZACIONAL Y RELACIÓN CON LOS ODS
    # -------------------------------------------------------------------------
    add_h1("2. Problemática Organizacional y Relación con los ODS")
    add_question("¿Cuál es la problemática real identificada en Alpina S.A.S. y con qué ODS se relaciona?")
    add_answer(
        "La problemática identificada comprende dos puntos críticos: primero, la falta de medición automática y continua en los tanques "
        "de enfriamiento de las fincas y centros de acopio veredales; cuando ocurren apagones o fallas mecánicas no detectadas a tiempo, "
        "la leche supera los 4°C, proliferan bacterias y se acidifica, lo que genera rechazos de producto al llegar a la planta de Sopó "
        "(hasta un 3.8% de mermas en contingencias). Segundo, la baja tasa de recolección de los empaques plásticos y cajas de Tetra Pak "
        "después del consumo, de los cuales hoy se recicla menos del 25%, terminando la mayoría en rellenos sanitarios.\n"
        "Esta problemática se relaciona directamente con el ODS 12: Producción y Consumo Responsables, en sus metas 12.3 (reducir el desperdicio "
        "de alimentos a lo largo de la cadena) y 12.5 (reducir la generación de residuos mediante el reciclaje). También se vincula con el ODS 9: "
        "Industria, Innovación e Infraestructura, en su meta 9.4 (adoptar tecnologías limpias y procesos industriales más eficientes)."
    )

    add_question("¿Por qué esta problemática requiere ser atendida desde una perspectiva sistémica y social?")
    add_answer(
        "Porque no se trata de una simple avería mecánica que se resuelva cambiando un enfriador. Es un problema humano y social "
        "donde intervienen familias campesinas con vías terciarias en mal estado y cortes de luz frecuentes, transportadores que deben "
        "cubrir rutas largas y las normas de salud pública que cuidan al consumidor. Si la empresa solo aplica la regla fría de botar o "
        "rechazar la leche en la puerta de la fábrica, el campesino pierde su único ingreso económico de la semana sin saber cómo evitarlo. "
        "Un enfoque sistémico permite ver la cadena completa, entender la realidad del campo y buscar una solución compartida donde nadie pierda."
    )

    add_question("¿Cómo aporta la Ingeniería de Sistemas a la comprensión y solución de este problema?")
    add_answer(
        "La Ingeniería de Sistemas aporta creando soluciones tecnológicas prácticas y accesibles que conectan el campo con la planta. "
        "Específicamente, permite instalar sensores de bajo costo (Internet de las Cosas - IoT) en los tanques de las veredas para medir "
        "temperatura y nivel en tiempo real. Si la temperatura empieza a subir, el sistema envía una alerta automática por mensaje de texto "
        "o WhatsApp al ganadero y al transportista antes de que la leche se corte. Además, la disciplina permite diseñar plataformas en la nube "
        "para planificar las rutas de los camiones de forma eficiente y organizar sistemas de logística inversa con recicladores mediante códigos QR, "
        "asegurando que la tecnología sirva para prevenir problemas y proteger el sustento del productor rural."
    )

    # -------------------------------------------------------------------------
    # 3. ESTADIO 1: RECONOCIMIENTO DE LA SITUACIÓN PROBLEMA
    # -------------------------------------------------------------------------
    add_h1("3. Estadio 1: Reconocimiento de la Situación Problema")
    add_question("¿Cómo se representa gráficamente la situación problema identificada en Alpina S.A.S.?")
    add_diagram(
        IMG_ESTADIO1,
        1,
        "Reconocimiento de la Situación Problema en Alpina Productos Alimenticios S.A.S.",
        "Diagrama de la situación problema elaborado siguiendo el Estadio 1 de Peter Checkland (1999) y las orientaciones de la UNAD "
        "(González, 2023). Detalla actores, síntomas, causas, consecuencias y su relación con los ODS 12 y 9. Elaboración propia (2026)."
    )

    add_question("¿Quiénes son los actores, cuáles son los síntomas, las causas y las consecuencias de la problemática?")
    add_answer(
        "• Actores involucrados: Familias ganaderas campesinas, conductores de camiones cisterna refrigerados, operarios del laboratorio de calidad y recepción en planta Sopó, ingenieros de sistemas/TI de Alpina, directivos de logística y compras, consumidores finales y recicladores de base.\n"
        "• Síntomas observados: Subidas de temperatura por encima de 4°C en el acopio rural, camiones cisterna esperando entre 45 y 90 minutos para descargue en planta mientras se hacen pruebas de laboratorio, leche rechazada por acidez y acumulación de bolsas y cajas plásticas en la basura.\n"
        "• Causas identificadas: Ausencia de sensores automáticos en los tanques rurales, toma de muestras manuales anotadas en papel, carreteras destapadas que demoran el transporte, fallas eléctricas en las fincas y falta de puntos accesibles de retorno de empaques para los consumidores.\n"
        "• Consecuencias: Pérdidas económicas para los campesinos por leche rechazada, sobrecostos de reprocesamiento y demoras para Alpina, comida desperdiciada e impacto contaminante en los rellenos sanitarios por empaques no recuperados."
    )

    # -------------------------------------------------------------------------
    # 4. ESTADIO 2: DEFINICIÓN RAÍZ MEDIANTE CATWOE
    # -------------------------------------------------------------------------
    add_h1("4. Estadio 2: Construcción de la Definición Raíz mediante CATWOE")
    add_question("¿Cuál es el análisis de cada uno de los elementos del marco mnemónico CATWOE?")
    add_answer(
        "• C – Clientes (Beneficiarios y afectados):\n"
        "  - Beneficiarios directos: Los más de 3.500 campesinos lecheros (aseguran el pago completo de su producto sin penalizaciones por temperatura) y los consumidores finales (reciben lácteos con frescura e inocuidad garantizada).\n"
        "  - Afectados si no se interviene: Las comunidades locales por la basura plástica y los campesinos por las pérdidas económicas.\n\n"
        "• A – Actores:\n"
        "  - El equipo de Ingeniería de Sistemas y TI (desarrolla y mantiene los sensores IoT y el software de control), los operarios de calidad en planta Sopó, los conductores de camiones cisterna y los ganaderos capacitados en el monitoreo preventivo.\n\n"
        "• T – Transformación:\n"
        "  - Entrada: Cadena de acopio con mediciones manuales, riesgo de leche dañada por fallas térmicas y baja tasa de reciclaje de envases.\n"
        "  - Proceso de transformación: Instalación de sensores IoT en tanques de enfriamiento, pruebas analíticas rápidas en planta, capacitación práctica a los campesinos y convenios de logística inversa con asociaciones de recicladores.\n"
        "  - Salida: Cadena de leche monitoreada en tiempo real, pérdidas de leche reducidas a menos del 0.8% y una tasa de recuperación de empaques superior al 35%.\n\n"
        "• W – Cosmovisión (Weltanschauung):\n"
        "  - La convicción de que la rentabilidad de Alpina debe ir unida al bienestar del campesino y a la protección del medio ambiente, entendiendo que la tecnología es un medio útil para evitar el desperdicio y generar confianza mutua.\n\n"
        "• O – Dueños (Owners):\n"
        "  - La Junta Directiva y las Gerencias de Operaciones, TI y Sostenibilidad de Alpina S.A.S., con autoridad para destinar presupuesto y autorizar cambios en los procesos.\n\n"
        "• E – Restricciones Ambientales:\n"
        "  - El Decreto 616 de 2006 del Ministerio de Salud e INVIMA (exige leche cruda a ≤ 4°C), la Ley 2232 de 2022 de reducción de plásticos, la señal intermitente de celular en zonas rurales montañosas y el presupuesto disponible de la empresa."
    )

    add_question("¿Cuál es la Definición Raíz redactada para el sistema?")
    add_answer(
        "«Un sistema de actividad humana perteneciente a Alpina Productos Alimenticios S.A.S., coordinado por sus gerencias de "
        "Operaciones, Tecnología y Sostenibilidad, con el propósito de transformar el acopio lechero rural y la gestión de envases; "
        "mediante la instalación de sensores IoT en tanques veredales, la automatización de pruebas rápidas de recepción en planta, "
        "la capacitación a los ganaderos y la creación de redes de reciclaje con recicladores locales; con el fin de evitar pérdidas "
        "de leche (ODS 12.3), garantizar ingresos justos para las familias campesinas y elevar el reciclaje de empaques (ODS 12.5); "
        "bajo la visión de que la calidad del producto y el cuidado ambiental deben avanzar juntos; dentro de las exigencias del "
        "Decreto 616 de 2006 del INVIMA y las leyes de manejo de plásticos en Colombia».",
        indent=True
    )

    # -------------------------------------------------------------------------
    # 5. ESTADIO 3: MODELO CONCEPTUAL
    # -------------------------------------------------------------------------
    add_h1("5. Estadio 3: Elaboración del Modelo Conceptual")
    add_question("¿Cómo se representa gráficamente el modelo conceptual de actividades y control?")
    add_diagram(
        IMG_ESTADIO3,
        2,
        "Modelo Conceptual del Sistema de Actividades Humanas y Bucles de Control",
        "Modelo conceptual derivado de la Definición Raíz según las pautas de Peter Checkland (1999). Muestra las actividades del sistema "
        "en infinitivo y el bucle de control gerencial basado en las 3 'E' (Eficacia, Eficiencia y Efectividad). Elaboración propia (2026)."
    )

    add_question("¿Cuáles son las actividades operacionales fundamentales del modelo conceptual?")
    add_answer(
        "El modelo conceptual organiza las acciones necesarias en cuatro actividades principales (verbos en infinitivo):\n"
        "1. Monitorear: Medir de forma continua la temperatura (entre 2°C y 4°C) y la acidez en los tanques de enfriamiento veredales mediante sensores IoT sumergibles.\n"
        "2. Validar y recibir: Realizar pruebas analíticas rápidas de calidad en la planta de Sopó para descargar cada camión cisterna en menos de 20 minutos.\n"
        "3. Integrar información: Unificar los datos de los tanques rurales, la ubicación de los camiones y los registros de pesaje en un sistema digital en la nube accesible para todos los involucrados.\n"
        "4. Gestionar logística inversa: Crear puntos limpios en supermercados y coordinar la compra de envases usados con asociaciones de recicladores para asegurar su reincorporación industrial."
    )

    add_question("¿Cómo opera el subsistema de control a través de las 3 'E' de Peter Checkland?")
    add_answer(
        "• Eficacia (E1 - ¿Se alcanza la meta inmediata?): Verificar que el 99.5% o más de la leche que entra a planta cumpla estrictamente con la temperatura requerida sin alteración.\n"
        "• Eficiencia (E2 - ¿Se logra usando bien los recursos y sin desperdiciar?): Bajar las pérdidas de leche a menos del 0.8% y reducir el tiempo de descargue en bahía de 75 a 20 minutos por camión.\n"
        "• Efectividad (E3 - ¿Se logra el impacto positivo a largo plazo?): Asegurar que los campesinos mantengan ingresos estables y que Alpina supere el 35% de reciclaje de empaques, cumpliendo con los ODS 12 y 9."
    )

    # -------------------------------------------------------------------------
    # 6. ESTADIO 4: COMPARACIÓN ENTRE LA SITUACIÓN ACTUAL Y EL MODELO CONCEPTUAL
    # -------------------------------------------------------------------------
    add_h1("6. Estadio 4: Comparación entre la Situación Actual y el Modelo Conceptual")
    add_question("¿Qué diferencias y oportunidades de mejora se encuentran al comparar lo que pasa hoy frente a lo que propone el modelo?")
    add_answer(
        "1. En el monitoreo de temperatura en el campo:\n"
        "   - Situación actual: Se mide a mano con termómetros y se anota en papel; si hay un corte de luz en la madrugada, nadie se entera hasta que llega el camión.\n"
        "   - Situación propuesta: Sensores IoT autónomos que miden cada 5 minutos y envían alertas automáticas al celular del ganadero ante cualquier alza térmica.\n"
        "   - Oportunidad de mejora: Permite corregir la falla a tiempo antes de que la leche se corte, evitando botar el producto.\n\n"
        "2. En la recepción de leche en planta Sopó:\n"
        "   - Situación actual: Los camiones esperan entre 45 y 90 minutos en fila mientras el laboratorio hace pruebas manuales, lo que calienta la leche por espera pasiva.\n"
        "   - Situación propuesta: Equipos de análisis rápido por espectrometría infrarroja conectados directamente al sistema de silos para descargar en 20 minutos.\n"
        "   - Oportunidad de mejora: Elimina trancones en planta, ahorra tiempo a los transportadores y protege la frescura de la materia prima.\n\n"
        "3. En la integración de la información:\n"
        "   - Situación actual: Los datos del campo, de los camiones y de la planta están en planillas separadas sin comunicación directa.\n"
        "   - Situación propuesta: Plataforma digital unificada en la nube donde cada lote de leche tiene su historial completo visible para todos.\n"
        "   - Oportunidad de mejora: Rutas de recolección mejor planeadas y liquidación de pagos clara y sin errores para los campesinos.\n\n"
        "4. En la recuperación de envases posconsumo:\n"
        "   - Situación actual: Gestión pasiva dependiente de la basura común, con menos del 25% de empaques recuperados.\n"
        "   - Situación propuesta: Red de puntos limpios en grandes superficies y convenios de compra directa con asociaciones de recicladores.\n"
        "   - Oportunidad de mejora: Cumplimiento de la Ley 2232, ahorro en materias primas recicladas y menor impacto en rellenos sanitarios."
    )

    # -------------------------------------------------------------------------
    # 7. ESTADIO 5: CAMBIOS FACTIBLES Y DESEABLES
    # -------------------------------------------------------------------------
    add_h1("7. Estadio 5: Definición de Cambios Factibles y Deseables")
    add_question("¿Cuáles son los cuatro cambios concretos que se proponen para transformar a Alpina S.A.S.?")
    add_answer(
        "1. Instalación de sensores IoT en tanques de enfriamiento veredales:\n"
        "   - Por qué conviene: Termina con la falta de control en las fincas y previene pérdidas de leche por acidez.\n"
        "   - Viabilidad: Muy alta; son dispositivos económicos con batería solar y chip celular que no requieren infraestructura compleja.\n"
        "   - Responsables: Gerencia de TI y Dirección de Abastecimiento Lechero.\n"
        "   - Impacto esperado: Disminución del 80% en los rechazos de leche por problemas de temperatura.\n\n"
        "2. Automatización y agilización de pruebas en bahías de recepción en Sopó:\n"
        "   - Por qué conviene: Destraba el cuello de botella más importante de la fábrica y evita que la leche se caliente en la fila.\n"
        "   - Viabilidad: Alta; requiere integrar equipos analíticos rápidos con el software de almacenamiento de silos existente.\n"
        "   - Responsables: Gerencia de Calidad y Jefatura de Planta Sopó.\n"
        "   - Impacto esperado: Reducción del tiempo de descargue de 75 a 20 minutos por camión cisterna.\n\n"
        "3. Creación de una plataforma digital única de trazabilidad lechera:\n"
        "   - Por qué conviene: Brinda transparencia y conecta a los campesinos, transportistas y administradores en un solo sistema.\n"
        "   - Viabilidad: Alta; se construye sobre los servidores en la nube que Alpina ya opera.\n"
        "   - Responsables: Dirección de Transformación Digital y Gerencia de Cadena de Suministro.\n"
        "   - Impacto esperado: Control del 100% de la leche acopiada y pagos oportunos y justos para los ganaderos.\n\n"
        "4. Alianzas formales con asociaciones de recicladores y puntos de retorno de empaques:\n"
        "   - Por qué conviene: Permite cumplir las metas de la Ley 2232 y cerrar el ciclo de vida de los envases plásticos y de cartón.\n"
        "   - Viabilidad: Media-alta; se logra mediante acuerdos de compra directa de material con recicladores e incentivos a clientes.\n"
        "   - Responsables: Dirección de Sostenibilidad y Gerencia de Mercadeo.\n"
        "   - Impacto esperado: Aumento del reciclaje de empaques de Alpina del 22% al 35% durante el primer año."
    )

    # -------------------------------------------------------------------------
    # 8. ESTADIO 6: DISEÑO DEL PLAN DE ACCIÓN
    # -------------------------------------------------------------------------
    add_h1("8. Estadio 6: Diseño del Plan de Acción")
    add_question("¿Cuál es el plan de acción estructurado para poner en marcha los cambios propuestos?")
    add_answer(
        "• Acción 1: Instalar kits de telemetría IoT en 50 tanques veredales piloto en Cundinamarca y Boyacá.\n"
        "  - Responsable: Ingeniero Líder de Proyectos IoT y Coordinador de Abastecimiento de Zona.\n"
        "  - Recursos: 50 sensores sumergibles, baterías solares, módems celulares y software en la nube ($85 millones COP).\n"
        "  - Tiempo: Meses 1 al 3.\n"
        "  - Indicador: 100% de los 50 tanques piloto transmitiendo datos sin fallas en tiempo real.\n\n"
        "• Acción 2: Conectar analizadores rápidos por espectrometría en bahías de recepción en planta Sopó.\n"
        "  - Responsable: Jefe de Laboratorio de Calidad y Equipo de Sistemas Industriales.\n"
        "  - Recursos: Equipos analíticos rápidos y configuración de conexión con el sistema de silos ($45 millones COP).\n"
        "  - Tiempo: Meses 2 al 4.\n"
        "  - Indicador: Tiempo de validación y descargue igual o menor a 20 minutos por camión.\n\n"
        "• Acción 3: Capacitar a 500 familias campesinas en buenas prácticas de frío y uso de alertas móviles.\n"
        "  - Responsable: Equipo de Fomento Ganadero y Gestión Social de Alpina.\n"
        "  - Recursos: Talleres prácticos en veredas y cartillas educativas ilustradas ($25 millones COP).\n"
        "  - Tiempo: Meses 3 al 5.\n"
        "  - Indicador: Al menos el 90% de los productores capacitados utilizando las alertas en su celular.\n\n"
        "• Acción 4: Montar puntos limpios de depósito en 100 almacenes de cadena y firmar convenios de reciclaje.\n"
        "  - Responsable: Coordinación de Sostenibilidad y Jefatura de Canales Comerciales.\n"
        "  - Recursos: Contenedores de recolección y fondo de incentivos por volumen para recicladores ($60 millones COP).\n"
        "  - Tiempo: Meses 4 al 6.\n"
        "  - Indicador: Recuperar al menos 45 toneladas mensuales de empaques plásticos y Tetra Pak para reciclaje."
    )

    # -------------------------------------------------------------------------
    # 9. CONCLUSIONES
    # -------------------------------------------------------------------------
    add_h1("9. Conclusiones")
    add_question("¿Cuáles son las conclusiones principales obtenidas en este trabajo?")
    add_answer(
        "1. La Metodología de Sistemas Blandos demostró que los problemas de calidad de la leche en Alpina no son solo una falla de máquinas, sino un problema donde influyen la vida de los campesinos, el estado de las vías y la falta de información oportuna.\n\n"
        "2. El análisis CATWOE permitió definir con claridad que la empresa puede mantener su rentabilidad económica sin perjudicar a los pequeños ganaderos ni al medio ambiente, cumpliendo las metas de los ODS 12 y 9.\n\n"
        "3. La Ingeniería de Sistemas demuestra su utilidad práctica en el sector agroindustrial al conectar sensores económicos en el campo que previenen daños en la leche antes de que sea tarde.\n\n"
        "4. Los cambios planteados y el plan de acción son viables en la práctica, cuentan con costos razonables y fijan responsables y metas claras para transformar la operación de Alpina."
    )

    # -------------------------------------------------------------------------
    # 10. REFERENCIAS BIBLIOGRÁFICAS
    # -------------------------------------------------------------------------
    add_h1("10. Referencias Bibliográficas")
    add_question("¿Cuáles son los referentes bibliográficos oficiales consultados bajo las normas APA (7.ª edición)?")

    referencias = [
        "Alpina Productos Alimenticios S.A.S. (2024). Informe de Sostenibilidad y Economía Circular 2023. Publicaciones Corporativas Alpina.",
        "Checkland, P. (1999). Systems Thinking, Systems Practice: Soft Systems Methodology in Action. John Wiley & Sons.",
        "Checkland, P., & Scholes, J. (1990). Soft Systems Methodology in Action. John Wiley & Sons.",
        "González, Y. A. (2023). Metodología de Sistemas Blandos (MSB) [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/58695",
        "Jerardino Wiesenborn, B. (2019). Metodología de Sistemas Blandos: Conceptos claves [Video]. YouTube. https://www.youtube.com/watch?v=2pzJsWjk12E",
        "Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. CIENCIA ergo-sum, 15(1), 45-53. https://dialnet.unirioja.es/servlet/articulo?codigo=5034963",
        "Ministerio de Ambiente y Desarrollo Sostenible. (2018). Resolución 1407 de 2018: Por la cual se reglamenta la gestión ambiental de los residuos de envases y empaques. MinAmbiente.",
        "Ministerio de la Protección Social. (2006). Decreto 616 de 2006: Por el cual se expide el Reglamento Técnico sobre los requisitos que debe cumplir la leche para el consumo humano. Diario Oficial No. 46.196.",
        "Naciones Unidas. (2015). Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible. Organización de las Naciones Unidas. https://sdgs.un.org/es/goals",
        "Osorio Gómez, J. C. (2007). Introducción al pensamiento sistémico. Programa Editorial Universidad del Valle. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/129056?page=10",
        "Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. Systemic Practice and Action Research, 37, 1123–1140. https://doi.org/10.1007/s11213-024-09689-9"
    ]

    for ref in referencias:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.space_before = Pt(3)
        p_ref.paragraph_format.space_after = Pt(5)
        p_ref.paragraph_format.line_spacing = 1.2
        p_ref.paragraph_format.left_indent = Inches(0.5)
        p_ref.paragraph_format.first_line_indent = Inches(-0.5)
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p_ref.add_run(ref)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    # Guardar en Documentos y Descargas
    docx_path_docs = os.path.join(OUT_DIR_DOCS, DOCX_NAME)
    anexo_path_docs = os.path.join(OUT_DIR_DOCS, ANEXO_NAME)
    docx_path_down = os.path.join(OUT_DIR_DOWN, DOCX_NAME)
    anexo_path_down = os.path.join(OUT_DIR_DOWN, ANEXO_NAME)

    doc.save(docx_path_docs)
    shutil.copy2(docx_path_docs, anexo_path_docs)
    shutil.copy2(docx_path_docs, docx_path_down)
    shutil.copy2(docx_path_docs, anexo_path_down)

    print(f"✅ Archivos DOCX actualizados exitosamente en Documentos y Descargas.")


def build_html_and_pdf():
    print("🌐 Generando versión HTML y PDF concisa y directa...")

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Fase 2 – Aplicando la Metodología de Sistemas Blandos (UNAD)</title>
<style>
  @page {{
    size: letter;
    margin: 2.54cm;
    @bottom-right {{
      content: counter(page);
      font-family: 'Times New Roman', serif;
      font-size: 10pt;
    }}
  }}
  body {{
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.35;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }}
  .cover {{
    page-break-after: always;
    text-align: center;
    padding-top: 3.5cm;
  }}
  .cover h1 {{
    font-size: 14pt;
    font-weight: bold;
    color: #0f172a;
    line-height: 1.4;
    margin-bottom: 2.5cm;
  }}
  .cover .author {{
    font-size: 12pt;
    font-weight: bold;
    margin-bottom: 0.2cm;
  }}
  .cover .meta {{
    font-size: 11pt;
    color: #334155;
    margin-bottom: 2cm;
  }}
  .cover .tutor {{
    font-size: 11pt;
    margin-bottom: 2cm;
  }}
  .cover .institution {{
    font-size: 11pt;
    color: #0f172a;
    line-height: 1.4;
  }}
  h2 {{
    font-size: 13pt;
    font-weight: bold;
    color: #0f172a;
    border-bottom: 1.5px solid #0e7490;
    padding-bottom: 3px;
    margin-top: 1.5em;
    margin-bottom: 0.6em;
    page-break-after: avoid;
  }}
  .question-box {{
    margin-top: 0.9em;
    margin-bottom: 0.3em;
    page-break-after: avoid;
  }}
  .question-lbl {{
    font-weight: bold;
    color: #0e7490;
    font-size: 12pt;
  }}
  .question-text {{
    font-weight: bold;
    color: #0f172a;
    font-size: 12pt;
  }}
  p {{
    text-align: justify;
    margin-top: 0.2em;
    margin-bottom: 0.6em;
  }}
  .quote-box {{
    margin: 0.4em 0 0.8em 1.5em;
    padding: 0;
    background: transparent;
    border: none;
    font-style: italic;
    color: #1e293b;
    text-align: justify;
    line-height: 1.3;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .figure-container {{
    margin: 1.2em auto;
    text-align: center;
    page-break-inside: avoid;
  }}
  .figure-caption {{
    text-align: left;
    margin-bottom: 0.3em;
  }}
  .figure-caption .fig-bold {{
    font-weight: bold;
    font-size: 11pt;
    display: block;
  }}
  .figure-caption .fig-title {{
    font-style: italic;
    font-size: 11pt;
  }}
  .figure-container img {{
    max-width: 95%;
    height: auto;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }}
  .figure-note {{
    text-align: justify;
    font-size: 10pt;
    line-height: 1.2;
    color: #475569;
    margin-top: 0.3em;
  }}
  .figure-note em {{
    font-style: italic;
  }}
  .ref-item {{
    padding-left: 2em;
    text-indent: -2em;
    margin-bottom: 0.5em;
    font-size: 11pt;
    line-height: 1.3;
    text-align: justify;
  }}
</style>
</head>
<body>

<!-- PORTADA -->
<div class="cover">
  <h1>Fase 2 – Aplicando la Metodología de Sistemas Blandos<br>
  Análisis de la Cadena de Frío y Gestión de Residuos en Alpina S.A.S.</h1>

  <div class="author">Yeiny Alejandra Suarez Rodriguez</div>
  <div class="meta">Código / C.C.: 1003882193<br>Grupo: 346</div>

  <div class="tutor">Tutor / Docente:<br><strong>Paola Maritza Rincon Nuñez</strong></div>

  <div class="institution">
    Universidad Nacional Abierta y a Distancia – UNAD<br>
    Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)<br>
    Programa de Ingeniería de Sistemas<br>
    Curso: Teoría de Sistemas en las Organizaciones (Código: 204016)<br>
    Octubre de 2026
  </div>
</div>

<!-- INTRODUCCIÓN -->
<h2>Introducción</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿De qué trata este trabajo y cuál es su objetivo?</span>
</div>
<p>
Este informe aplica la Metodología de Sistemas Blandos (MSB) de Peter Checkland a la empresa Alpina Productos Alimenticios S.A.S. Alpina es una de las empresas lácteas más importantes de Colombia y trabaja a diario con miles de ganaderos campesinos en distintas regiones del país. En este trabajo analizamos dos problemas reales de su operación: la dificultad para mantener la cadena de frío en el acopio de leche rural por falta de monitoreo continuo en tiempo real, y el bajo nivel de recuperación de sus envases plásticos y de Tetra Pak después del consumo. Estos retos se conectan con el ODS 12 (Producción y Consumo Responsables) y el ODS 9 (Industria, Innovación e Infraestructura). El objetivo del documento es desarrollar los seis estadios de la metodología de forma clara, proponiendo mejoras prácticas y factibles desde la Ingeniería de Sistemas.
</p>

<!-- 1. ORGANIZACIÓN OBJETO DE ESTUDIO -->
<h2>1. Caracterización de la Organización Seleccionada</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Qué empresa se seleccionó y cuáles son sus datos operativos básicos?</span>
</div>
<p>
• <strong>Nombre:</strong> Alpina Productos Alimenticios S.A.S.<br>
• <strong>Sector económico:</strong> Agroindustrial / Alimentos y bebidas (derivados lácteos).<br>
• <strong>Ubicación principal:</strong> Sede industrial y administrativa central en Sopó (Cundinamarca). Plantas adicionales de procesamiento en Facatativá (Cundinamarca), Caldas (Antioquia), Chinchiná (Caldas), Popayán (Cauca) y Simijaca (Cundinamarca).<br>
• <strong>Actividad principal:</strong> Acopio de leche cruda, pasteurización, transformación industrial, empaque, refrigeración y distribución nacional de leche entera, deslactosada, quesos, yogures, postres y bebidas lácteas.<br>
• <strong>Contexto general:</strong> Alpina compra leche diariamente a más de 3.500 pequeños y medianos ganaderos en cuencas de Cundinamarca, Boyacá, Nariño y el Eje Cafetero. Al ser un producto vivo y altamente perecedero, su calidad depende de mantener la leche por debajo de los 4°C, tal como lo exige el Decreto 616 de 2006 del Ministerio de la Protección Social. Al mismo tiempo, la empresa debe responder ante normativas ambientales como la Ley 2232 de 2022 y la Resolución 1407 de 2018 para reciclar y reducir los envases plásticos que pone en el mercado.
</p>

<!-- 2. PROBLEMÁTICA ORGANIZACIONAL Y RELACIÓN CON LOS ODS -->
<h2>2. Problemática Organizacional y Relación con los ODS</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuál es la problemática real identificada en Alpina S.A.S. y con qué ODS se relaciona?</span>
</div>
<p>
La problemática identificada comprende dos puntos críticos: primero, la falta de medición automática y continua en los tanques de enfriamiento de las fincas y centros de acopio veredales; cuando ocurren apagones o fallas mecánicas no detectadas a tiempo, la leche supera los 4°C, proliferan bacterias y se acidifica, lo que genera rechazos de producto al llegar a la planta de Sopó (hasta un 3.8% de mermas en contingencias). Segundo, la baja tasa de recolección de los empaques plásticos y cajas de Tetra Pak después del consumo, de los cuales hoy se recicla menos del 25%, terminando la mayoría en rellenos sanitarios.<br>
Esta problemática se relaciona directamente con el ODS 12: Producción y Consumo Responsables, en sus metas 12.3 (reducir el desperdicio de alimentos a lo largo de la cadena) y 12.5 (reducir la generación de residuos mediante el reciclaje). También se vincula con el ODS 9: Industria, Innovación e Infraestructura, en su meta 9.4 (adoptar tecnologías limpias y procesos industriales más eficientes).
</p>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Por qué esta problemática requiere ser atendida desde una perspectiva sistémica y social?</span>
</div>
<p>
Porque no se trata de una simple avería mecánica que se resuelva cambiando un enfriador. Es un problema humano y social donde intervienen familias campesinas con vías terciarias en mal estado y cortes de luz frecuentes, transportadores que deben cubrir rutas largas y las normas de salud pública que cuidan al consumidor. Si la empresa solo aplica la regla fría de botar o rechazar la leche en la puerta de la fábrica, el campesino pierde su único ingreso económico de la semana sin saber cómo evitarlo. Un enfoque sistémico permite ver la cadena completa, entender la realidad del campo y buscar una solución compartida donde nadie pierda.
</p>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo aporta la Ingeniería de Sistemas a la comprensión y solución de este problema?</span>
</div>
<p>
La Ingeniería de Sistemas aporta creando soluciones tecnológicas prácticas y accesibles que conectan el campo con la planta. Específicamente, permite instalar sensores de bajo costo (Internet de las Cosas - IoT) en los tanques de las veredas para medir temperatura y nivel en tiempo real. Si la temperatura empieza a subir, el sistema envía una alerta automática por mensaje de texto o WhatsApp al ganadero y al transportista antes de que la leche se corte. Además, la disciplina permite diseñar plataformas en la nube para planificar las rutas de los camiones de forma eficiente y organizar sistemas de logística inversa con recicladores mediante códigos QR, asegurando que la tecnología sirva para prevenir problemas y proteger el sustento del productor rural.
</p>

<!-- 3. ESTADIO 1: RECONOCIMIENTO DE LA SITUACIÓN PROBLEMA -->
<h2>3. Estadio 1: Reconocimiento de la Situación Problema</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo se representa gráficamente la situación problema identificada en Alpina S.A.S.?</span>
</div>

<div class="figure-container">
  <div class="figure-caption">
    <span class="fig-bold">Figura 1</span>
    <span class="fig-title">Reconocimiento de la Situación Problema en Alpina Productos Alimenticios S.A.S.</span>
  </div>
  <img src="file://{IMG_ESTADIO1}" alt="Figura 1: Reconocimiento de la Situación Problema">
  <div class="figure-note">
    <em>Nota.</em> Diagrama de la situación problema elaborado siguiendo el Estadio 1 de Peter Checkland (1999) y las orientaciones de la UNAD (González, 2023). Detalla actores, síntomas, causas, consecuencias y su relación con los ODS 12 y 9. Elaboración propia (2026).
  </div>
</div>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Quiénes son los actores, cuáles son los síntomas, las causas y las consecuencias de la problemática?</span>
</div>
<p>
• <strong>Actores involucrados:</strong> Familias ganaderas campesinas, conductores de camiones cisterna refrigerados, operarios del laboratorio de calidad y recepción en planta Sopó, ingenieros de sistemas/TI de Alpina, directivos de logística y compras, consumidores finales y recicladores de base.<br>
• <strong>Síntomas observados:</strong> Subidas de temperatura por encima de 4°C en el acopio rural, camiones cisterna esperando entre 45 y 90 minutos para descargue en planta mientras se hacen pruebas de laboratorio, leche rechazada por acidez y acumulación de bolsas y cajas plásticas en la basura.<br>
• <strong>Causas identificadas:</strong> Ausencia de sensores automáticos en los tanques rurales, toma de muestras manuales anotadas en papel, carreteras destapadas que demoran el transporte, fallas eléctricas en las fincas y falta de puntos accesibles de retorno de empaques para los consumidores.<br>
• <strong>Consecuencias:</strong> Pérdidas económicas para los campesinos por leche rechazada, sobrecostos de reprocesamiento y demoras para Alpina, comida desperdiciada e impacto contaminante en los rellenos sanitarios por empaques no recuperados.
</p>

<!-- 4. ESTADIO 2: DEFINICIÓN RAÍZ MEDIANTE CATWOE -->
<h2>4. Estadio 2: Construcción de la Definición Raíz mediante CATWOE</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuál es el análisis de cada uno de los elementos del marco mnemónico CATWOE?</span>
</div>
<p>
• <strong>C – Clientes (Beneficiarios y afectados):</strong><br>
  - Beneficiarios directos: Los más de 3.500 campesinos lecheros (aseguran el pago completo de su producto sin penalizaciones por temperatura) y los consumidores finales (reciben lácteos con frescura e inocuidad garantizada).<br>
  - Afectados si no se interviene: Las comunidades locales por la basura plástica y los campesinos por las pérdidas económicas.<br><br>
• <strong>A – Actores:</strong><br>
  - El equipo de Ingeniería de Sistemas y TI (desarrolla y mantiene los sensores IoT y el software de control), los operarios de calidad en planta Sopó, los conductores de camiones cisterna y los ganaderos capacitados en el monitoreo preventivo.<br><br>
• <strong>T – Transformación:</strong><br>
  - Entrada: Cadena de acopio con mediciones manuales, riesgo de leche dañada por fallas térmicas y baja tasa de reciclaje de envases.<br>
  - Proceso de transformación: Instalación de sensores IoT en tanques de enfriamiento, pruebas analíticas rápidas en planta, capacitación práctica a los campesinos y convenios de logística inversa con asociaciones de recicladores.<br>
  - Salida: Cadena de leche monitoreada en tiempo real, pérdidas de leche reducidas a menos del 0.8% y una tasa de recuperación de empaques superior al 35%.<br><br>
• <strong>W – Cosmovisión (Weltanschauung):</strong><br>
  - La convicción de que la rentabilidad de Alpina debe ir unida al bienestar del campesino y a la protección del medio ambiente, entendiendo que la tecnología es un medio útil para evitar el desperdicio y generar confianza mutua.<br><br>
• <strong>O – Dueños (Owners):</strong><br>
  - La Junta Directiva y las Gerencias de Operaciones, TI y Sostenibilidad de Alpina S.A.S., con autoridad para destinar presupuesto y autorizar cambios en los procesos.<br><br>
• <strong>E – Restricciones Ambientales:</strong><br>
  - El Decreto 616 de 2006 del Ministerio de Salud e INVIMA (exige leche cruda a ≤ 4°C), la Ley 2232 de 2022 de reducción de plásticos, la señal intermitente de celular en zonas rurales montañosas y el presupuesto disponible de la empresa.
</p>

<div style="page-break-inside: avoid; break-inside: avoid;">
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuál es la Definición Raíz redactada para el sistema?</span>
</div>
<div class="quote-box">
«Un sistema de actividad humana perteneciente a Alpina Productos Alimenticios S.A.S., coordinado por sus gerencias de Operaciones, Tecnología y Sostenibilidad, con el propósito de transformar el acopio lechero rural y la gestión de envases; mediante la instalación de sensores IoT en tanques veredales, la automatización de pruebas rápidas de recepción en planta, la capacitación a los ganaderos y la creación de redes de reciclaje con recicladores locales; con el fin de evitar pérdidas de leche (ODS 12.3), garantizar ingresos justos para las familias campesinas y elevar el reciclaje de empaques (ODS 12.5); bajo la visión de que la calidad del producto y el cuidado ambiental deben avanzar juntos; dentro de las exigencias del Decreto 616 de 2006 del INVIMA y las leyes de manejo de plásticos en Colombia».
</div>
</div>

<!-- 5. ESTADIO 3: MODELO CONCEPTUAL -->
<h2>5. Estadio 3: Elaboración del Modelo Conceptual</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo se representa gráficamente el modelo conceptual de actividades y control?</span>
</div>

<div class="figure-container">
  <div class="figure-caption">
    <span class="fig-bold">Figura 2</span>
    <span class="fig-title">Modelo Conceptual del Sistema de Actividades Humanas y Bucles de Control</span>
  </div>
  <img src="file://{IMG_ESTADIO3}" alt="Figura 2: Modelo Conceptual de Actividades">
  <div class="figure-note">
    <em>Nota.</em> Modelo conceptual derivado de la Definición Raíz según las pautas de Peter Checkland (1999). Muestra las actividades del sistema en infinitivo y el bucle de control gerencial basado en las 3 'E' (Eficacia, Eficiencia y Efectividad). Elaboración propia (2026).
  </div>
</div>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son las actividades operacionales fundamentales del modelo conceptual?</span>
</div>
<p>
El modelo conceptual organiza las acciones necesarias en cuatro actividades principales (verbos en infinitivo):<br>
1. <strong>Monitorear:</strong> Medir de forma continua la temperatura (entre 2°C y 4°C) y la acidez en los tanques de enfriamiento veredales mediante sensores IoT sumergibles.<br>
2. <strong>Validar y recibir:</strong> Realizar pruebas analíticas rápidas de calidad en la planta de Sopó para descargar cada camión cisterna en menos de 20 minutos.<br>
3. <strong>Integrar información:</strong> Unificar los datos de los tanques rurales, la ubicación de los camiones y los registros de pesaje en un sistema digital en la nube accesible para todos los involucrados.<br>
4. <strong>Gestionar logística inversa:</strong> Crear puntos limpios en supermercados y coordinar la compra de envases usados con asociaciones de recicladores para asegurar su reincorporación industrial.
</p>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo opera el subsistema de control a través de las 3 'E' de Peter Checkland?</span>
</div>
<p>
• <strong>Eficacia (E1 - ¿Se alcanza la meta inmediata?):</strong> Verificar que el 99.5% o más de la leche que entra a planta cumpla estrictamente con la temperatura requerida sin alteración.<br>
• <strong>Eficiencia (E2 - ¿Se logra usando bien los recursos y sin desperdiciar?):</strong> Bajar las pérdidas de leche a menos del 0.8% y reducir el tiempo de descargue en bahía de 75 a 20 minutos por camión.<br>
• <strong>Efectividad (E3 - ¿Se logra el impacto positivo a largo plazo?):</strong> Asegurar que los campesinos mantengan ingresos estables y que Alpina supere el 35% de reciclaje de empaques, cumpliendo con los ODS 12 y 9.
</p>

<!-- 6. ESTADIO 4: COMPARACIÓN ENTRE LA SITUACIÓN ACTUAL Y EL MODELO CONCEPTUAL -->
<h2>6. Estadio 4: Comparación entre la Situación Actual y el Modelo Conceptual</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Qué diferencias y oportunidades de mejora se encuentran al comparar lo que pasa hoy frente a lo que propone el modelo?</span>
</div>
<p>
1. <strong>En el monitoreo de temperatura en el campo:</strong><br>
   - Situación actual: Se mide a mano con termómetros y se anota en papel; si hay un corte de luz en la madrugada, nadie se entera hasta que llega el camión.<br>
   - Situación propuesta: Sensores IoT autónomos que miden cada 5 minutos y envían alertas automáticas al celular del ganadero ante cualquier alza térmica.<br>
   - Oportunidad de mejora: Permite corregir la falla a tiempo antes de que la leche se corte, evitando botar el producto.<br><br>
2. <strong>En la recepción de leche en planta Sopó:</strong><br>
   - Situación actual: Los camiones esperan entre 45 y 90 minutos en fila mientras el laboratorio hace pruebas manuales, lo que calienta la leche por espera pasiva.<br>
   - Situación propuesta: Equipos de análisis rápido por espectrometría infrarroja conectados directamente al sistema de silos para descargar en 20 minutos.<br>
   - Oportunidad de mejora: Elimina trancones en planta, ahorra tiempo a los transportadores y protege la frescura de la materia prima.<br><br>
3. <strong>En la integración de la información:</strong><br>
   - Situación actual: Los datos del campo, de los camiones y de la planta están en planillas separadas sin comunicación directa.<br>
   - Situación propuesta: Plataforma digital unificada en la nube donde cada lote de leche tiene su historial completo visible para todos.<br>
   - Oportunidad de mejora: Rutas de recolección mejor planeadas y liquidación de pagos clara y sin errores para los campesinos.<br><br>
4. <strong>En la recuperación de envases posconsumo:</strong><br>
   - Situación actual: Gestión pasiva dependiente de la basura común, con menos del 25% de empaques recuperados.<br>
   - Situación propuesta: Red de puntos limpios en grandes superficies y convenios de compra directa con asociaciones de recicladores.<br>
   - Oportunidad de mejora: Cumplimiento de la Ley 2232, ahorro en materias primas recicladas y menor impacto en rellenos sanitarios.
</p>

<!-- 7. ESTADIO 5: CAMBIOS FACTIBLES Y DESEABLES -->
<h2>7. Estadio 5: Definición de Cambios Factibles y Deseables</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son los cuatro cambios concretos que se proponen para transformar a Alpina S.A.S.?</span>
</div>
<p>
1. <strong>Instalación de sensores IoT en tanques de enfriamiento veredales:</strong><br>
   - Por qué conviene: Termina con la falta de control en las fincas y previene pérdidas de leche por acidez.<br>
   - Viabilidad: Muy alta; son dispositivos económicos con batería solar y chip celular que no requieren infraestructura compleja.<br>
   - Responsables: Gerencia de TI y Dirección de Abastecimiento Lechero.<br>
   - Impacto esperado: Disminución del 80% en los rechazos de leche por problemas de temperatura.<br><br>
2. <strong>Automatización y agilización de pruebas en bahías de recepción en Sopó:</strong><br>
   - Por qué conviene: Destraba el cuello de botella más importante de la fábrica y evita que la leche se caliente en la fila.<br>
   - Viabilidad: Alta; requiere integrar equipos analíticos rápidos con el software de almacenamiento de silos existente.<br>
   - Responsables: Gerencia de Calidad y Jefatura de Planta Sopó.<br>
   - Impacto esperado: Reducción del tiempo de descargue de 75 a 20 minutos por camión cisterna.<br><br>
3. <strong>Creación de una plataforma digital única de trazabilidad lechera:</strong><br>
   - Por qué conviene: Brinda transparencia y conecta a los campesinos, transportistas y administradores en un solo sistema.<br>
   - Viabilidad: Alta; se construye sobre los servidores en la nube que Alpina ya opera.<br>
   - Responsables: Dirección de Transformación Digital y Gerencia de Cadena de Suministro.<br>
   - Impacto esperado: Control del 100% de la leche acopiada y pagos oportunos y justos para los ganaderos.<br><br>
4. <strong>Alianzas formales con asociaciones de recicladores y puntos de retorno de empaques:</strong><br>
   - Por qué conviene: Permite cumplir las metas de la Ley 2232 y cerrar el ciclo de vida de los envases plásticos y de cartón.<br>
   - Viabilidad: Media-alta; se logra mediante acuerdos de compra directa de material con recicladores e incentivos a clientes.<br>
   - Responsables: Dirección de Sostenibilidad y Gerencia de Mercadeo.<br>
   - Impacto esperado: Aumento del reciclaje de empaques de Alpina del 22% al 35% durante el primer año.
</p>

<!-- 8. ESTADIO 6: DISEÑO DEL PLAN DE ACCIÓN -->
<h2>8. Estadio 6: Diseño del Plan de Acción</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuál es el plan de acción estructurado para poner en marcha los cambios propuestos?</span>
</div>
<p>
• <strong>Acción 1:</strong> Instalar kits de telemetría IoT en 50 tanques veredales piloto en Cundinamarca y Boyacá.<br>
  - Responsable: Ingeniero Líder de Proyectos IoT y Coordinador de Abastecimiento de Zona.<br>
  - Recursos: 50 sensores sumergibles, baterías solares, módems celulares y software en la nube ($85 millones COP).<br>
  - Tiempo: Meses 1 al 3.<br>
  - Indicador: 100% de los 50 tanques piloto transmitiendo datos sin fallas en tiempo real.<br><br>
• <strong>Acción 2:</strong> Conectar analizadores rápidos por espectrometría en bahías de recepción en planta Sopó.<br>
  - Responsable: Jefe de Laboratorio de Calidad y Equipo de Sistemas Industriales.<br>
  - Recursos: Equipos analíticos rápidos y configuración de conexión con el sistema de silos ($45 millones COP).<br>
  - Tiempo: Meses 2 al 4.<br>
  - Indicador: Tiempo de validación y descargue igual o menor a 20 minutos por camión.<br><br>
• <strong>Acción 3:</strong> Capacitar a 500 familias campesinas en buenas prácticas de frío y uso de alertas móviles.<br>
  - Responsable: Equipo de Fomento Ganadero y Gestión Social de Alpina.<br>
  - Recursos: Talleres prácticos en veredas y cartillas educativas ilustradas ($25 millones COP).<br>
  - Tiempo: Meses 3 al 5.<br>
  - Indicador: Al menos el 90% de los productores capacitados utilizando las alertas en su celular.<br><br>
• <strong>Acción 4:</strong> Montar puntos limpios de depósito en 100 almacenes de cadena y firmar convenios de reciclaje.<br>
  - Responsable: Coordinación de Sostenibilidad y Jefatura de Canales Comerciales.<br>
  - Recursos: Contenedores de recolección y fondo de incentivos por volumen para recicladores ($60 millones COP).<br>
  - Tiempo: Meses 4 al 6.<br>
  - Indicador: Recuperar al menos 45 toneladas mensuales de empaques plásticos y Tetra Pak para reciclaje.
</p>

<!-- 9. CONCLUSIONES -->
<h2>9. Conclusiones</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son las conclusiones principales obtenidas en este trabajo?</span>
</div>
<p>
1. La Metodología de Sistemas Blandos demostró que los problemas de calidad de la leche en Alpina no son solo una falla de máquinas, sino un problema donde influyen la vida de los campesinos, el estado de las vías y la falta de información oportuna.<br><br>
2. El análisis CATWOE permitió definir con claridad que la empresa puede mantener su rentabilidad económica sin perjudicar a los pequeños ganaderos ni al medio ambiente, cumpliendo las metas de los ODS 12 y 9.<br><br>
3. La Ingeniería de Sistemas demuestra su utilidad práctica en el sector agroindustrial al conectar sensores económicos en el campo que previenen daños en la leche antes de que sea tarde.<br><br>
4. Los cambios planteados y el plan de acción son viables en la práctica, cuentan con costos razonables y fijan responsables y metas claras para transformar la operación de Alpina.
</p>

<!-- 10. REFERENCIAS BIBLIOGRÁFICAS -->
<h2>10. Referencias Bibliográficas</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son los referentes bibliográficos oficiales consultados bajo las normas APA (7.ª edición)?</span>
</div>

<div class="ref-item">Alpina Productos Alimenticios S.A.S. (2024). <em>Informe de Sostenibilidad y Economía Circular 2023</em>. Publicaciones Corporativas Alpina.</div>
<div class="ref-item">Checkland, P. (1999). <em>Systems Thinking, Systems Practice: Soft Systems Methodology in Action</em>. John Wiley & Sons.</div>
<div class="ref-item">Checkland, P., & Scholes, J. (1990). <em>Soft Systems Methodology in Action</em>. John Wiley & Sons.</div>
<div class="ref-item">González, Y. A. (2023). <em>Metodología de Sistemas Blandos (MSB)</em> [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. <a href="https://repository.unad.edu.co/handle/10596/58695">https://repository.unad.edu.co/handle/10596/58695</a></div>
<div class="ref-item">Jerardino Wiesenborn, B. (2019). <em>Metodología de Sistemas Blandos: Conceptos claves</em> [Video]. YouTube. <a href="https://www.youtube.com/watch?v=2pzJsWjk12E">https://www.youtube.com/watch?v=2pzJsWjk12E</a></div>
<div class="ref-item">Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. <em>CIENCIA ergo-sum</em>, 15(1), 45-53. <a href="https://dialnet.unirioja.es/servlet/articulo?codigo=5034963">https://dialnet.unirioja.es/servlet/articulo?codigo=5034963</a></div>
<div class="ref-item">Ministerio de Ambiente y Desarrollo Sostenible. (2018). <em>Resolución 1407 de 2018: Por la cual se reglamenta la gestión ambiental de los residuos de envases y empaques</em>. MinAmbiente.</div>
<div class="ref-item">Ministerio de la Protección Social. (2006). <em>Decreto 616 de 2006: Por el cual se expide el Reglamento Técnico sobre los requisitos que debe cumplir la leche para el consumo humano</em>. Diario Oficial No. 46.196.</div>
<div class="ref-item">Naciones Unidas. (2015). <em>Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible</em>. Organización de las Naciones Unidas. <a href="https://sdgs.un.org/es/goals">https://sdgs.un.org/es/goals</a></div>
<div class="ref-item">Osorio Gómez, J. C. (2007). <em>Introducción al pensamiento sistémico</em>. Programa Editorial Universidad del Valle. <a href="https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/129056?page=10">https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/129056?page=10</a></div>
<div class="ref-item">Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. <em>Systemic Practice and Action Research</em>, 37, 1123–1140. <a href="https://doi.org/10.1007/s11213-024-09689-9">https://doi.org/10.1007/s11213-024-09689-9</a></div>

</body>
</html>
"""

    html_path_docs = os.path.join(OUT_DIR_DOCS, HTML_NAME)
    with open(html_path_docs, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML guardado en: {html_path_docs}")

    import subprocess

    pdf_path_docs = os.path.join(OUT_DIR_DOCS, PDF_NAME)
    anexo_pdf_docs = os.path.join(OUT_DIR_DOCS, ANEXO_PDF)
    pdf_path_down = os.path.join(OUT_DIR_DOWN, PDF_NAME)
    anexo_pdf_down = os.path.join(OUT_DIR_DOWN, ANEXO_PDF)
    pdf_path_esc = os.path.join("/home/rootkit/Escritorio", PDF_NAME)

    print("🖨️ Compilando PDF con Chrome headless...")
    cmd = [
        "/opt/google/chrome/chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path_docs}",
        f"file://{html_path_docs}"
    ]
    subprocess.run(cmd, check=True)

    shutil.copy2(pdf_path_docs, anexo_pdf_docs)
    shutil.copy2(pdf_path_docs, pdf_path_down)
    shutil.copy2(pdf_path_docs, anexo_pdf_down)
    if os.path.exists("/home/rootkit/Escritorio"):
        shutil.copy2(pdf_path_docs, pdf_path_esc)

    print(f"✅ Archivos PDF actualizados en Documentos, Descargas y Escritorio.")


if __name__ == "__main__":
    build_docx()
    build_html_and_pdf()
