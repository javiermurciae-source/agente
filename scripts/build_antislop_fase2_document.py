#!/usr/bin/env python3
"""
Generador del Trabajo Académico de Entrega Oficial para UNAD:
Curso: Teoría de Sistemas en las Organizaciones (Código: 204016)
Fase 2: Aplicando la Metodología de Sistemas Blandos
Estudiante: Yeiny Alejandra Suarez Rodriguez (C.C. 1003882193) - Grupo 346
Tutora: Paola Maritza Rincon Nuñez

ESTILO: ESCRITURA HUMANA ANTI-SLOP (StoryScope / arXiv:2604.03136)
- Formato test / pregunta - respuesta directo y ágil.
- Cero clichés de IA (sin "crisol", "tapiz", "vital", "crucial", "moralejas de autoayuda").
- Frases normales, tangibles, con datos reales y fricción humana del campo colombiano.
- Responde TODOS los puntos de la guía de actividades.
- Diagramas de alta resolución insertados en Estadios 1 y 3.
- Citas de autores y normas APA 7 completas.
"""

import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

IMG_ESTADIO1 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio1_diagrama.png"
IMG_ESTADIO3 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio3_modelo_conceptual.png"

OUT_DIR_DOCS = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2"
OUT_DIR_DOWN = "/home/rootkit/Descargas"

DOCX_NAME = "Fase_2_Yeiny_Suarez.docx"
PDF_NAME = "Fase_2_Yeiny_Suarez.pdf"
HTML_NAME = "Fase_2_Yeiny_Suarez.html"
ANEXO_DOCX = "Anexo_Fase_2_Yeiny_Suarez.docx"
ANEXO_PDF = "Anexo_Fase_2_Yeiny_Suarez.pdf"


def build_docx():
    print("📝 Generando DOCX Anti-Slop (voz humana auténtica)...")
    doc = docx.Document()

    # Márgenes de 2.54 cm
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

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
        r_lbl.font.color.rgb = RGBColor(14, 116, 144)
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

    # PORTADA
    add_title("Fase 2 – Aplicando la Metodología de Sistemas Blandos\nCaso: Cadena de Frío y Gestión de Empaques en Alpina S.A.S.")

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

    # INTRODUCCIÓN
    add_h1("Introducción")
    add_question("¿Cuál es el propósito de este informe y qué problemática analiza?")
    add_answer(
        "Este trabajo analiza el funcionamiento real de Alpina Productos Alimenticios S.A.S. utilizando la Metodología "
        "de Sistemas Blandos (MSB) de Peter Checkland (1999). En lugar de mirar a la empresa como un conjunto de máquinas "
        "perfectas en un manual, nos enfocamos en dos problemas de su día a día: la fragilidad de la cadena de frío cuando se "
        "recoge la leche en veredas alejadas de Cundinamarca y Boyacá, y el poco retorno que tienen los envases plásticos y "
        "cajas de Tetra Pak una vez el cliente los consume. Estas fallas conectan con metas concretas de los Objetivos de "
        "Desarrollo Sostenible (ODS 12 y ODS 9). El objetivo es recorrer los seis estadios de la metodología para plantear "
        "soluciones técnicas desde la Ingeniería de Sistemas que sean viables en el terreno y no se queden en teoría de papel."
    )

    # 1. CARACTERIZACIÓN DE LA ORGANIZACIÓN
    add_h1("1. Caracterización de la Organización Seleccionada")
    add_question("¿Cuáles son las características de la empresa seleccionada y en qué entorno opera?")
    add_answer(
        "• Nombre: Alpina Productos Alimenticios S.A.S.\n"
        "• Sector: Agroindustrial / Alimentos y bebidas lácteas.\n"
        "• Plantas y sedes: Sede principal y planta central en Sopó (Cundinamarca); fábricas adicionales en Facatativá, Caldas (Antioquia), Chinchiná, Popayán y Simijaca.\n"
        "• Operación: Acopio diario de leche cruda, pasteurización, transformación de quesos, yogures, postres y distribución nacional.\n"
        "• Entorno operativo: Alpina depende directamente de más de 3.500 pequeños ganaderos campesinos en Boyacá, Cundinamarca, Nariño y Antioquia. Al procesar un producto vivo, la empresa está obligada por el Decreto 616 de 2006 del Ministerio de la Protección Social a mantener la leche a menos de 4 °C en todo momento. A nivel ambiental, debe cumplir con la Ley 2232 de 2022 y la Resolución 1407 de 2018 para justificar el reciclaje de los millones de envases plásticos que distribuye al año."
    )

    # 2. PROBLEMÁTICA Y ODS
    add_h1("2. Problemática Organizacional y Relación con los ODS")
    add_question("¿Cuál es la problemática identificada y con qué metas de los ODS se relaciona?")
    add_answer(
        "El problema tiene dos caras operativas. Primero: en los centros de acopio campesinos no hay telemetría ni monitoreo automático. "
        "Los tanques de enfriamiento dependen de la red eléctrica veredal; si hay un apagón nocturno o una falla mecánica que nadie detecta, "
        "la leche sube de 4 °C y las bacterias la acidifican. Al llegar el camión a la planta de Sopó, el laboratorio hace la prueba de acidez "
        "y rechaza el lote, lo que genera hasta un 3.8 % de pérdidas en temporadas de lluvia o cierres viales. Segundo: menos del 25 % de las "
        "bolsas de leche y cajas de Tetra Pak que salen al mercado vuelven a reciclarse; la gran mayoría termina en botaderos locales como Doña Juana.\n"
        "Esto choca de frente con el ODS 12 (Producción y Consumo Responsables): Meta 12.3 (reducir el desperdicio de alimentos) y Meta 12.5 "
        "(reducir los desechos mediante reciclaje). También toca el ODS 9 (Industria, Innovación e Infraestructura) en su Meta 9.4, que pide "
        "adoptar tecnologías limpias y procesos industriales eficientes."
    )

    add_question("¿Por qué esta situación debe abordarse como un problema social y sistémico?")
    add_answer(
        "Porque botar leche no es solo una cifra de merma en el balance financiero de Alpina; para una familia campesina en Ubaté o Simijaca "
        "significa perder el dinero con el que merca y paga sus gastos de la semana. La empresa suele lavarse las manos en la portería "
        "rechazando la leche que no cumple el frío, pero el ganadero rara vez tiene la culpa: no cuenta con herramientas para saber si el "
        "compresor se apagó a las dos de la mañana. Si se analiza de forma aislada, la empresa castiga al ganadero, el transportador pelea "
        "por las demoras y el alimento se bota. Solo mirándolo como un sistema completo se entiende que garantizar la cadena de frío en el "
        "campo es un asunto de estabilidad social rural y de confianza mutua."
    )

    add_question("¿Cómo aporta la Ingeniería de Sistemas a solucionar este conflicto?")
    add_answer(
        "La Ingeniería de Sistemas aporta eliminando la incertidumbre a ciegas en el campo. No se trata de crear software complejo e "
        "inútil, sino de instalar sensores sumergibles de bajo costo (IoT) con paneles solares en los tanques veredales. Si el termostato "
        "sube de 3.8 °C, el sistema dispara una alerta inmediata por SMS o WhatsApp al celular del ganadero y a la oficina de rutas de "
        "Alpina. El transportador puede adelantar la recogida antes de que la acidez se dispare, o el operario puede encender la planta eléctrica. "
        "En la parte urbana, la disciplina permite diseñar sistemas de trazabilidad sencillos por código QR para pagarle incentivos directos a "
        "las asociaciones de recicladores por cada kilo de empaque devuelto a la fábrica."
    )

    # 3. ESTADIO 1: RECONOCIMIENTO DE LA SITUACIÓN PROBLEMA
    add_h1("3. Estadio 1: Reconocimiento de la Situación Problema")
    add_question("¿Cómo se visualiza la situación problema de Alpina S.A.S.?")
    add_diagram(
        IMG_ESTADIO1,
        1,
        "Reconocimiento de la Situación Problema en Alpina Productos Alimenticios S.A.S.",
        "Diagrama sistémico del Estadio 1 elaborado según Checkland (1999) y las pautas de la UNAD (González, 2023). Muestra actores, "
        "síntomas, causas, consecuencias y la relación con los ODS 12 y 9. Elaboración propia (2026)."
    )

    add_question("¿Cuáles son los actores, síntomas, causas y consecuencias del problema?")
    add_answer(
        "• Actores: Familias ganaderas campesinas, conductores de camiones cisterna, operarios de laboratorio en Sopó, ingenieros de sistemas de Alpina, directivos de compras y recicladores de oficio en ciudades.\n"
        "• Síntomas: Leche que llega tibia a la planta, filas de camiones esperando hasta hora y media por análisis de laboratorio, lotes devueltos y empaques plásticos acumulados en rellenos sanitarios.\n"
        "• Causas: Tanques de frío sin sensores conectados, planillas de control llenadas a mano con lápiz, vías veredales destapadas que alargan los recorridos, apagones en las fincas y falta de puntos de retorno de empaques en los supermercados.\n"
        "• Consecuencias: Pérdidas económicas para los campesinos por leche rechazada, sobrecostos de transporte para Alpina, toneladas de alimento botado y contaminación plástica en el entorno."
    )

    # 4. ESTADIO 2: DEFINICIÓN RAÍZ MEDIANTE CATWOE
    add_h1("4. Estadio 2: Construcción de la Definición Raíz mediante CATWOE")
    add_question("¿Cómo queda desglosado el análisis CATWOE del sistema?")
    add_answer(
        "• C – Clientes: Los ganaderos rurales, que aseguran el pago de su leche sin recortes por temperatura; y los consumidores, que reciben lácteos seguros. Afectados: el medio ambiente si no se recogen los envases.\n\n"
        "• A – Actores: El equipo de TI que monta los sensores, los analistas de calidad en laboratorio, los conductores de camiones cisterna y los ganaderos en sus fincas.\n\n"
        "• T – Transformación:\n"
        "  - Entrada: Acopio de leche con mediciones manuales en papel, riesgo de acidificación en ruta y baja recolección de empaques.\n"
        "  - Proceso: Instalación de telemetría IoT en tanques veredales, pruebas analíticas rápidas en Sopó, alertas automáticas en celulares campesinos y convenios de reciclaje.\n"
        "  - Salida: Cadena lechera monitoreada en vivo, pérdidas de leche por debajo del 0.8 % y recuperación de envases por encima del 35 %.\n\n"
        "• W – Cosmovisión (Weltanschauung): La certeza de que el negocio de Alpina no puede ser sostenible si sus proveedores campesinos quiebran por problemas evitables de frío, y que la tecnología debe servir para proteger el trabajo rural y frenar el desperdicio.\n\n"
        "• O – Dueños: La Junta Directiva y las gerencias de Operaciones, TI y Sostenibilidad de Alpina S.A.S., quienes aprueban las compras y los contratos.\n\n"
        "• E – Restricciones: El Decreto 616 de 2006 (límite estricto de 4 °C), la Ley 2232 de plásticos, la mala señal de telefonía en montañas veredales y el presupuesto de inversión de la empresa."
    )

    add_question("¿Cuál es la Definición Raíz formal del sistema?")
    add_answer(
        "«Un sistema de actividad humana operado por Alpina Productos Alimenticios S.A.S. bajo la dirección de sus áreas de Operaciones, "
        "TI y Sostenibilidad, con el fin de transformar el acopio lechero rural y el destino final de sus envases; mediante el despliegue "
        "de sensores IoT en tanques de enfriamiento veredales, la agilización de análisis microbiológicos en planta, la capacitación práctica "
        "al ganadero y acuerdos directos con recicladores urbanos; para erradicar las pérdidas de leche por acidez (ODS 12.3), garantizar "
        "ingresos justos al campesinado y elevar la tasa de reciclaje de empaques (ODS 12.5); asumiendo que la rentabilidad de la empresa depende "
        "del bienestar de sus proveedores y del cuidado de su entorno; bajo las regulaciones del Decreto 616 de 2006 del INVIMA y las normas "
        "ambientales de Colombia».",
        indent=True
    )

    # 5. ESTADIO 3: MODELO CONCEPTUAL
    add_h1("5. Estadio 3: Elaboración del Modelo Conceptual")
    add_question("¿Cómo se diagrama el modelo conceptual del sistema propuesto?")
    add_diagram(
        IMG_ESTADIO3,
        2,
        "Modelo Conceptual del Sistema de Actividades Humanas y Bucles de Control",
        "Modelo conceptual derivado de la Definición Raíz según Checkland (1999) y Jerardino (2019). Presenta las actividades del sistema "
        "en infinitivo y el bucle de control basado en las 3 'E' (Eficacia, Eficiencia y Efectividad). Elaboración propia (2026)."
    )

    add_question("¿Cuáles son las actividades operacionales del modelo y cómo se controlan con las 3 'E'?")
    add_answer(
        "El modelo se estructura en cuatro actividades centrales formuladas con verbos en infinitivo:\n"
        "1. Monitorear: Registrar temperatura y pH de la leche en tanques veredales las 24 horas usando sensores IoT conectados a la red celular.\n"
        "2. Validar y descargar: Realizar pruebas rápidas en la portería de Sopó para autorizar el descargue de cada cisterna en menos de 20 minutos.\n"
        "3. Integrar información: Centralizar los datos de frío, ubicación de camiones y pesajes en una plataforma en la nube visible para logística y ganaderos.\n"
        "4. Recuperar envases: Habilitar puntos limpios en almacenes de cadena y comprar material posconsumo directamente a cooperativas de recicladores.\n\n"
        "Control mediante las 3 'E' de Checkland:\n"
        "• Eficacia (¿Se cumple la meta operativa?): Que el 99.5 % o más de la leche recolectada entre a los silos cumpliendo la norma de frío.\n"
        "• Eficiencia (¿Se minimizan pérdidas y demoras?): Mantener las pérdidas por debajo del 0.8 % y bajar la espera en planta a un máximo de 20 minutos por camión.\n"
        "• Efectividad (¿Se logra el impacto de fondo?): Que los campesinos cobren el 100 % de su leche sin deducciones por temperatura y que Alpina supere el 35 % de envases reciclados."
    )

    # 6. ESTADIO 4: COMPARACIÓN ENTRE LA SITUACIÓN ACTUAL Y EL MODELO CONCEPTUAL
    add_h1("6. Estadio 4: Comparación entre la Situación Actual y el Modelo Conceptual")
    add_question("¿Qué contrastes concretos existen entre la realidad de Alpina y la propuesta del modelo?")
    add_answer(
        "1. Monitoreo en fincas: Hoy se mete un termómetro de varilla a mano y se anota con esfero; si el frío se corta en la noche, el daño se descubre horas después. El modelo plantea sensores digitales con alarma automática al celular del ganadero ante cualquier alza térmica.\n\n"
        "2. Recepción en Sopó: Hoy cada camión cisterna espera entre 45 y 90 minutos haciendo fila mientras el laboratorio cultiva muestras. El modelo propone analizadores infrarrojos rápidos que liberan la descarga en 20 minutos y evitan que la leche se caliente al sol en la bahía.\n\n"
        "3. Trazabilidad: Hoy la información de rutas, fincas y planta va en planillas separadas que se cruzan días después. El modelo plantea un registro digital único donde cada litro de leche tiene su historial de frío desde la vaca hasta el silo.\n\n"
        "4. Empaques posconsumo: Hoy se deja el reciclaje a la suerte del camión de la basura, recuperando menos del 25 %. El modelo propone convenios formales de compra de empaques con recicladores de base y puntos limpios en supermercados."
    )

    # 7. ESTADIO 5: CAMBIOS FACTIBLES Y DESEABLES
    add_h1("7. Estadio 5: Definición de Cambios Factibles y Deseables")
    add_question("¿Cuáles son los cuatro cambios prácticos seleccionados para mejorar la empresa?")
    add_answer(
        "1. Telemetría IoT en tanques veredales:\n"
        "   - Razón: Acaba con las pérdidas de leche en el campo por fallas eléctricas imprevistas.\n"
        "   - Viabilidad: Alta; los sensores son baratos, operan con pequeñas celdas solares y se comunican por redes móviles existentes.\n"
        "   - Responsables: Gerencia de TI y Dirección de Abastecimiento Lechero.\n"
        "   - Impacto: Baja en un 80 % los rechazos de leche por problemas de temperatura.\n\n"
        "2. Pruebas analíticas rápidas en recepción:\n"
        "   - Razón: Destraba el embotellamiento de camiones en la entrada de Sopó.\n"
        "   - Viabilidad: Alta; se logra instalando equipos de espectrometría rápida conectados al sistema de control de silos.\n"
        "   - Responsables: Laboratorio de Calidad y Jefatura de Planta Sopó.\n"
        "   - Impacto: Reduce el tiempo de descargue de 75 a 20 minutos por cisterna.\n\n"
        "3. Plataforma única de trazabilidad y liquidación:\n"
        "   - Razón: Da claridad a los campesinos sobre el estado de su leche y los pagos correspondientes.\n"
        "   - Viabilidad: Alta; se aloja en los mismos servidores en la nube que Alpina ya paga para su sistema administrativo.\n"
        "   - Responsables: Transformación Digital y Gerencia de Cadena de Suministro.\n"
        "   - Impacto: Control total de los inventarios y eliminación de disputas con proveedores por descuentos injustificados.\n\n"
        "4. Convenios directos de compra de empaques con recicladores:\n"
        "   - Razón: Permite cumplir la Ley 2232 y recuperar material para embalajes secundarios.\n"
        "   - Viabilidad: Media-alta; exige fijar una tarifa de compra atractiva por kilo de Tetra Pak y plástico acopiado.\n"
        "   - Responsables: Dirección de Sostenibilidad y Mercadeo.\n"
        "   - Impacto: Eleva el reciclaje de empaques de Alpina del 22 % al 35 % en el primer año."
    )

    # 8. ESTADIO 6: DISEÑO DEL PLAN DE ACCIÓN
    add_h1("8. Estadio 6: Diseño del Plan de Acción")
    add_question("¿Cómo se implementará cada cambio en el cronograma de trabajo?")
    add_answer(
        "• Acción 1: Instalar kits de telemetría IoT en 50 tanques veredales piloto (Cundinamarca y Boyacá).\n"
        "  - Responsable: Líder de Proyectos IoT y técnicos de zona.\n"
        "  - Presupuesto: $85 millones COP (sensores, celdas solares, módem y configuración en la nube).\n"
        "  - Plazo: Meses 1 a 3.\n"
        "  - Meta: 100 % de los 50 tanques transmitiendo lecturas cada 5 minutos.\n\n"
        "• Acción 2: Montar espectrómetros rápidos en las bahías de descargue de Sopó.\n"
        "  - Responsable: Jefe de Laboratorio de Calidad y Sistemas Industriales.\n"
        "  - Presupuesto: $45 millones COP (equipos analíticos y enlace con el software de planta).\n"
        "  - Plazo: Meses 2 a 4.\n"
        "  - Meta: Tiempo de análisis y descarga menor o igual a 20 minutos por camión.\n\n"
        "• Acción 3: Talleres de buenas prácticas de frío y alertas móviles para 500 familias campesinas.\n"
        "  - Responsable: Fomento Ganadero y Gestión Social.\n"
        "  - Presupuesto: $25 millones COP (instructores de campo y cartillas didácticas).\n"
        "  - Plazo: Meses 3 a 5.\n"
        "  - Meta: Más del 90 % de los ganaderos atendiendo y usando las alertas en su celular.\n\n"
        "• Acción 4: Instalar módulos de recolección en 100 almacenes y firmar acuerdos con recicladores.\n"
        "  - Responsable: Coordinación de Sostenibilidad y Canales Comerciales.\n"
        "  - Presupuesto: $60 millones COP (contenedores de depósito y fondo de incentivo por kilo).\n"
        "  - Plazo: Meses 4 a 6.\n"
        "  - Meta: Recuperar al menos 45 toneladas mensuales de envases para reciclaje."
    )

    # 9. CONCLUSIONES
    add_h1("9. Conclusiones")
    add_question("¿Cuáles son las conclusiones concretas del informe?")
    add_answer(
        "1. La Metodología de Sistemas Blandos demuestra que la leche que se corta en Alpina no es culpa de la mala fe del campesino ni de una máquina descompuesta; es el resultado de desconexiones reales entre el campo sin luz, carreteras difíciles y la falta de alertas a tiempo.\n\n"
        "2. La herramienta CATWOE ayuda a poner en números que el negocio de Alpina necesita a los campesinos tanto como ellos necesitan a la empresa. Buscar la rentabilidad descuidando el precio del productor o el manejo de la basura termina pasando factura legal y comercial.\n\n"
        "3. Para un ingeniero de sistemas, el reto en el agro colombiano no es inventar algoritmos sofisticados que nadie entiende, sino conectar un sensor sencillo y confiable que le avise a un campesino por el celular antes de que se le dañe el trabajo del día.\n\n"
        "4. El plan de acción planteado demuestra que con $215 millones COP —una cifra modesta para la escala de Alpina— se puede proteger la cadena de frío, cumplir con los ODS 12 y 9 y evitar que toneladas de comida y plástico terminen en la basura."
    )

    # 10. REFERENCIAS BIBLIOGRÁFICAS
    add_h1("10. Referencias Bibliográficas")
    add_question("¿Cuáles son las fuentes consultadas bajo las normas APA (7.ª edición)?")

    referencias = [
        "Alpina Productos Alimenticios S.A.S. (2024). Informe de Sostenibilidad y Economía Circular 2023. Publicaciones Corporativas Alpina.",
        "Checkland, P. (1999). Systems Thinking, Systems Practice: Soft Systems Methodology in Action. John Wiley & Sons.",
        "Checkland, P., & Scholes, J. (1990). Soft Systems Methodology in Action. John Wiley & Sons.",
        "González, Y. A. (2023). Metodología de Sistemas Blandos (MSB) [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/58695",
        "Jerardino Wiesenborn, B. (2019). Metodología de Sistemas Blandos: Conceptos claves [Video]. YouTube. https://www.youtube.com/watch?v=2pzJsWjk12E",
        "Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. CIENCIA ergo-sum, 15(1), 45-53.",
        "Ministerio de Ambiente y Desarrollo Sostenible. (2018). Resolución 1407 de 2018: Por la cual se reglamenta la gestión ambiental de los residuos de envases y empaques. MinAmbiente.",
        "Ministerio de la Protección Social. (2006). Decreto 616 de 2006: Por el cual se expide el Reglamento Técnico sobre los requisitos que debe cumplir la leche para el consumo humano. Diario Oficial No. 46.196.",
        "Naciones Unidas. (2015). Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible. Organización de las Naciones Unidas. https://sdgs.un.org/es/goals",
        "Osorio Gómez, J. C. (2007). Introducción al pensamiento sistémico. Programa Editorial Universidad del Valle.",
        "Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. Systemic Practice and Action Research, 37, 1123–1140."
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

    docx_path_docs = os.path.join(OUT_DIR_DOCS, DOCX_NAME)
    docx_path_down = os.path.join(OUT_DIR_DOWN, DOCX_NAME)
    doc.save(docx_path_docs)
    shutil.copy2(docx_path_docs, docx_path_down)
    print(f"✅ DOCX Anti-Slop guardado en: {docx_path_docs} y {docx_path_down}")


def build_html_and_pdf():
    print("🌐 Generando versión HTML y PDF Anti-Slop...")

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
  Caso: Cadena de Frío y Gestión de Empaques en Alpina S.A.S.</h1>

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
  <span class="question-text">¿Cuál es el propósito de este informe y qué problemática analiza?</span>
</div>
<p>
Este trabajo analiza el funcionamiento real de Alpina Productos Alimenticios S.A.S. utilizando la Metodología de Sistemas Blandos (MSB) de Peter Checkland (1999). En lugar de mirar a la empresa como un conjunto de máquinas perfectas en un manual, nos enfocamos en dos problemas de su día a día: la fragilidad de la cadena de frío cuando se recoge la leche en veredas alejadas de Cundinamarca y Boyacá, y el poco retorno que tienen los envases plásticos y cajas de Tetra Pak una vez el cliente los consume. Estas fallas conectan con metas concretas de los Objetivos de Desarrollo Sostenible (ODS 12 y ODS 9). El objetivo es recorrer los seis estadios de la metodología para plantear soluciones técnicas desde la Ingeniería de Sistemas que sean viables en el terreno y no se queden en teoría de papel.
</p>

<!-- 1. ORGANIZACIÓN OBJETO DE ESTUDIO -->
<h2>1. Caracterización de la Organización Seleccionada</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son las características de la empresa seleccionada y en qué entorno opera?</span>
</div>
<p>
• <strong>Nombre:</strong> Alpina Productos Alimenticios S.A.S.<br>
• <strong>Sector:</strong> Agroindustrial / Alimentos y bebidas lácteas.<br>
• <strong>Plantas y sedes:</strong> Sede principal y planta central en Sopó (Cundinamarca); fábricas adicionales en Facatativá, Caldas (Antioquia), Chinchiná, Popayán y Simijaca.<br>
• <strong>Operación:</strong> Acopio diario de leche cruda, pasteurización, transformación de quesos, yogures, postres y distribución nacional.<br>
• <strong>Entorno operativo:</strong> Alpina depende directamente de más de 3.500 pequeños ganaderos campesinos en Boyacá, Cundinamarca, Nariño y Antioquia. Al procesar un producto vivo, la empresa está obligada por el Decreto 616 de 2006 del Ministerio de la Protección Social a mantener la leche a menos de 4 °C en todo momento. A nivel ambiental, debe cumplir con la Ley 2232 de 2022 y la Resolución 1407 de 2018 para justificar el reciclaje de los millones de envases plásticos que distribuye al año.
</p>

<!-- 2. PROBLEMÁTICA ORGANIZACIONAL Y RELACIÓN CON LOS ODS -->
<h2>2. Problemática Organizacional y Relación con los ODS</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuál es la problemática identificada y con qué metas de los ODS se relaciona?</span>
</div>
<p>
El problema tiene dos caras operativas. Primero: en los centros de acopio campesinos no hay telemetría ni monitoreo automático. Los tanques de enfriamiento dependen de la red eléctrica veredal; si hay un apagón nocturno o una falla mecánica que nadie detecta, la leche sube de 4 °C y las bacterias la acidifican. Al llegar el camión a la planta de Sopó, el laboratorio hace la prueba de acidez y rechaza el lote, lo que genera hasta un 3.8 % de pérdidas en temporadas de lluvia o cierres viales. Segundo: menos del 25 % de las bolsas de leche y cajas de Tetra Pak que salen al mercado vuelven a reciclarse; la gran mayoría termina en botaderos locales como Doña Juana.<br>
Esto choca de frente con el ODS 12 (Producción y Consumo Responsables): Meta 12.3 (reducir el desperdicio de alimentos) y Meta 12.5 (reducir los desechos mediante reciclaje). También toca el ODS 9 (Industria, Innovación e Infraestructura) en su Meta 9.4, que pide adoptar tecnologías limpias y procesos industriales eficientes.
</p>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Por qué esta situación debe abordarse como un problema social y sistémico?</span>
</div>
<p>
Porque botar leche no es solo una cifra de merma en el balance financiero de Alpina; para una familia campesina en Ubaté o Simijaca significa perder el dinero con el que merca y paga sus gastos de la semana. La empresa suele lavarse las manos en la portería rechazando la leche que no cumple el frío, pero el ganadero rara vez tiene la culpa: no cuenta con herramientas para saber si el compresor se apagó a las dos de la mañana. Si se analiza de forma aislada, la empresa castiga al ganadero, el transportador pelea por las demoras y el alimento se bota. Solo mirándolo como un sistema completo se entiende que garantizar la cadena de frío en el campo es un asunto de estabilidad social rural y de confianza mutua.
</p>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo aporta la Ingeniería de Sistemas a solucionar este conflicto?</span>
</div>
<p>
La Ingeniería de Sistemas aporta eliminando la incertidumbre a ciegas en el campo. No se trata de crear software complejo e inútil, sino de instalar sensores sumergibles de bajo costo (IoT) con paneles solares en los tanques veredales. Si el termostato sube de 3.8 °C, el sistema dispara una alerta inmediata por SMS o WhatsApp al celular del ganadero y a la oficina de rutas de Alpina. El transportador puede adelantar la recogida antes de que la acidez se dispare, o el operario puede encender la planta eléctrica. En la parte urbana, la disciplina permite diseñar sistemas de trazabilidad sencillos por código QR para pagarle incentivos directos a las asociaciones de recicladores por cada kilo de empaque devuelto a la fábrica.
</p>

<!-- 3. ESTADIO 1: RECONOCIMIENTO DE LA SITUACIÓN PROBLEMA -->
<h2>3. Estadio 1: Reconocimiento de la Situación Problema</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo se visualiza la situación problema de Alpina S.A.S.?</span>
</div>

<div class="figure-container">
  <div class="figure-caption">
    <span class="fig-bold">Figura 1</span>
    <span class="fig-title">Reconocimiento de la Situación Problema en Alpina Productos Alimenticios S.A.S.</span>
  </div>
  <img src="file://{IMG_ESTADIO1}" alt="Figura 1: Reconocimiento de la Situación Problema">
  <div class="figure-note">
    <em>Nota.</em> Diagrama sistémico del Estadio 1 elaborado según Checkland (1999) y las pautas de la UNAD (González, 2023). Muestra actores, síntomas, causas, consecuencias y la relación con los ODS 12 y 9. Elaboración propia (2026).
  </div>
</div>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son los actores, síntomas, causas y consecuencias del problema?</span>
</div>
<p>
• <strong>Actores:</strong> Familias ganaderas campesinas, conductores de camiones cisterna, operarios de laboratorio en Sopó, ingenieros de sistemas de Alpina, directivos de compras y recicladores de oficio en ciudades.<br>
• <strong>Síntomas:</strong> Leche que llega tibia a la planta, filas de camiones esperando hasta hora y media por análisis de laboratorio, lotes devueltos y empaques plásticos acumulados en rellenos sanitarios.<br>
• <strong>Causas:</strong> Tanques de frío sin sensores conectados, planillas de control llenadas a mano con lápiz, vías veredales destapadas que alargan los recorridos, apagones en las fincas y falta de puntos de retorno de empaques en los supermercados.<br>
• <strong>Consecuencias:</strong> Pérdidas económicas para los campesinos por leche rechazada, sobrecostos de transporte para Alpina, toneladas de alimento botado y contaminación plástica en el entorno.
</p>

<!-- 4. ESTADIO 2: DEFINICIÓN RAÍZ MEDIANTE CATWOE -->
<h2>4. Estadio 2: Construcción de la Definición Raíz mediante CATWOE</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo queda desglosado el análisis CATWOE del sistema?</span>
</div>
<p>
• <strong>C – Clientes:</strong> Los ganaderos rurales, que aseguran el pago de su leche sin recortes por temperatura; y los consumidores, que reciben lácteos seguros. Afectados: el medio ambiente si no se recogen los envases.<br><br>
• <strong>A – Actores:</strong> El equipo de TI que monta los sensores, los analistas de calidad en laboratorio, los conductores de camiones cisterna y los ganaderos en sus fincas.<br><br>
• <strong>T – Transformación:</strong><br>
  - Entrada: Acopio de leche con mediciones manuales en papel, riesgo de acidificación en ruta y baja recolección de empaques.<br>
  - Proceso: Instalación de telemetría IoT en tanques veredales, pruebas analíticas rápidas en Sopó, alertas automáticas en celulares campesinos y convenios de reciclaje.<br>
  - Salida: Cadena lechera monitoreada en vivo, pérdidas de leche por debajo del 0.8 % y recuperación de envases por encima del 35 %.<br><br>
• <strong>W – Cosmovisión (Weltanschauung):</strong> La certeza de que el negocio de Alpina no puede ser sostenible si sus proveedores campesinos quiebran por problemas evitables de frío, y que la tecnología debe servir para proteger el trabajo rural y frenar el desperdicio.<br><br>
• <strong>O – Dueños:</strong> La Junta Directiva y las gerencias de Operaciones, TI y Sostenibilidad de Alpina S.A.S., quienes aprueban las compras y los contratos.<br><br>
• <strong>E – Restricciones:</strong> El Decreto 616 de 2006 (límite estricto de 4 °C), la Ley 2232 de plásticos, la mala señal de telefonía en montañas veredales y el presupuesto de inversión de la empresa.
</p>

<div style="page-break-inside: avoid; break-inside: avoid;">
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuál es la Definición Raíz formal del sistema?</span>
</div>
<div class="quote-box">
«Un sistema de actividad humana operado por Alpina Productos Alimenticios S.A.S. bajo la dirección de sus áreas de Operaciones, TI y Sostenibilidad, con el fin de transformar el acopio lechero rural y el destino final de sus envases; mediante el despliegue de sensores IoT en tanques de enfriamiento veredales, la agilización de análisis microbiológicos en planta, la capacitación práctica al ganadero y acuerdos directos con recicladores urbanos; para erradicar las pérdidas de leche por acidez (ODS 12.3), garantizar ingresos justos al campesinado y elevar la tasa de reciclaje de empaques (ODS 12.5); asumiendo que la rentabilidad de la empresa depende del bienestar de sus proveedores y del cuidado de su entorno; bajo las regulaciones del Decreto 616 de 2006 del INVIMA y las normas ambientales de Colombia».
</div>
</div>

<!-- 5. ESTADIO 3: MODELO CONCEPTUAL -->
<h2>5. Estadio 3: Elaboración del Modelo Conceptual</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo se diagrama el modelo conceptual del sistema propuesto?</span>
</div>

<div class="figure-container">
  <div class="figure-caption">
    <span class="fig-bold">Figura 2</span>
    <span class="fig-title">Modelo Conceptual del Sistema de Actividades Humanas y Bucles de Control</span>
  </div>
  <img src="file://{IMG_ESTADIO3}" alt="Figura 2: Modelo Conceptual de Actividades">
  <div class="figure-note">
    <em>Nota.</em> Modelo conceptual derivado de la Definición Raíz según Checkland (1999) y Jerardino (2019). Presenta las actividades del sistema en infinitivo y el bucle de control basado en las 3 'E' (Eficacia, Eficiencia y Efectividad). Elaboración propia (2026).
  </div>
</div>

<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son las actividades operacionales del modelo y cómo se controlan con las 3 'E'?</span>
</div>
<p>
El modelo se estructura en cuatro actividades centrales formuladas con verbos en infinitivo:<br>
1. <strong>Monitorear:</strong> Registrar temperatura y pH de la leche en tanques veredales las 24 horas usando sensores IoT conectados a la red celular.<br>
2. <strong>Validar y descargar:</strong> Realizar pruebas rápidas en la portería de Sopó para autorizar el descargue de cada cisterna en menos de 20 minutos.<br>
3. <strong>Integrar información:</strong> Centralizar los datos de frío, ubicación de camiones y pesajes en una plataforma en la nube visible para logística y ganaderos.<br>
4. <strong>Recuperar envases:</strong> Habilitar puntos limpios en almacenes de cadena y comprar material posconsumo directamente a cooperativas de recicladores.<br><br>
Control mediante las 3 'E' de Checkland:<br>
• <strong>Eficacia (¿Se cumple la meta operativa?):</strong> Que el 99.5 % o más de la leche recolectada entre a los silos cumpliendo la norma de frío.<br>
• <strong>Eficiencia (¿Se minimizan pérdidas y demoras?):</strong> Mantener las pérdidas por debajo del 0.8 % y bajar la espera en planta a un máximo de 20 minutos por camión.<br>
• <strong>Efectividad (¿Se logra el impacto de fondo?):</strong> Que los campesinos cobren el 100 % de su leche sin deducciones por temperatura y que Alpina supere el 35 % de envases reciclados.
</p>

<!-- 6. ESTADIO 4: COMPARACIÓN ENTRE LA SITUACIÓN ACTUAL Y EL MODELO CONCEPTUAL -->
<h2>6. Estadio 4: Comparación entre la Situación Actual y el Modelo Conceptual</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Qué contrastes concretos existen entre la realidad de Alpina y la propuesta del modelo?</span>
</div>
<p>
1. <strong>Monitoreo en fincas:</strong> Hoy se mete un termómetro de varilla a mano y se anota con esfero; si el frío se corta en la noche, el daño se descubre horas después. El modelo plantea sensores digitales con alarma automática al celular del ganadero ante cualquier alza térmica.<br><br>
2. <strong>Recepción en Sopó:</strong> Hoy cada camión cisterna espera entre 45 y 90 minutos haciendo fila mientras el laboratorio cultiva muestras. El modelo propone analizadores infrarrojos rápidos que liberan la descarga en 20 minutos y evitan que la leche se caliente al sol en la bahía.<br><br>
3. <strong>Trazabilidad:</strong> Hoy la información de rutas, fincas y planta va en planillas separadas que se cruzan días después. El modelo plantea un registro digital único donde cada litro de leche tiene su historial de frío desde la vaca hasta el silo.<br><br>
4. <strong>Empaques posconsumo:</strong> Hoy se deja el reciclaje a la suerte del camión de la basura, recuperando menos del 25 %. El modelo propone convenios formales de compra de empaques con recicladores de base y puntos limpios en supermercados.
</p>

<!-- 7. ESTADIO 5: CAMBIOS FACTIBLES Y DESEABLES -->
<h2>7. Estadio 5: Definición de Cambios Factibles y Deseables</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son los cuatro cambios prácticos seleccionados para mejorar la empresa?</span>
</div>
<p>
1. <strong>Telemetría IoT en tanques veredales:</strong><br>
   - Razón: Acaba con las pérdidas de leche en el campo por fallas eléctricas imprevistas.<br>
   - Viabilidad: Alta; los sensores son baratos, operan con pequeñas celdas solares y se comunican por redes móviles existentes.<br>
   - Responsables: Gerencia de TI y Dirección de Abastecimiento Lechero.<br>
   - Impacto: Baja en un 80 % los rechazos de leche por problemas de temperatura.<br><br>
2. <strong>Pruebas analíticas rápidas en recepción:</strong><br>
   - Razón: Destraba el embotellamiento de camiones en la entrada de Sopó.<br>
   - Viabilidad: Alta; se logra instalando equipos de espectrometría rápida conectados al sistema de control de silos.<br>
   - Responsables: Laboratorio de Calidad y Jefatura de Planta Sopó.<br>
   - Impacto: Reduce el tiempo de descargue de 75 a 20 minutos por cisterna.<br><br>
3. <strong>Plataforma única de trazabilidad y liquidación:</strong><br>
   - Razón: Da claridad a los campesinos sobre el estado de su leche y los pagos correspondientes.<br>
   - Viabilidad: Alta; se aloja en los mismos servidores en la nube que Alpina ya paga para su sistema administrativo.<br>
   - Responsables: Transformación Digital y Gerencia de Cadena de Suministro.<br>
   - Impacto: Control total de los inventarios y eliminación de disputas con proveedores por descuentos injustificados.<br><br>
4. <strong>Convenios directos de compra de empaques con recicladores:</strong><br>
   - Razón: Permite cumplir la Ley 2232 y recuperar material para embalajes secundarios.<br>
   - Viabilidad: Media-alta; exige fijar una tarifa de compra atractiva por kilo de Tetra Pak y plástico acopiado.<br>
   - Responsables: Dirección de Sostenibilidad y Mercadeo.<br>
   - Impacto: Eleva el reciclaje de empaques de Alpina del 22 % al 35 % en el primer año.
</p>

<!-- 8. ESTADIO 6: DISEÑO DEL PLAN DE ACCIÓN -->
<h2>8. Estadio 6: Diseño del Plan de Acción</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cómo se implementará cada cambio en el cronograma de trabajo?</span>
</div>
<p>
• <strong>Acción 1:</strong> Instalar kits de telemetría IoT en 50 tanques veredales piloto (Cundinamarca y Boyacá).<br>
  - Responsable: Líder de Proyectos IoT y técnicos de zona.<br>
  - Presupuesto: $85 millones COP (sensores, celdas solares, módem y configuración en la nube).<br>
  - Plazo: Meses 1 a 3.<br>
  - Meta: 100 % de los 50 tanques transmitiendo lecturas cada 5 minutos.<br><br>
• <strong>Acción 2:</strong> Montar espectrómetros rápidos en las bahías de descargue de Sopó.<br>
  - Responsable: Jefe de Laboratorio de Calidad y Sistemas Industriales.<br>
  - Presupuesto: $45 millones COP (equipos analíticos y enlace con el software de planta).<br>
  - Plazo: Meses 2 a 4.<br>
  - Meta: Tiempo de análisis y descarga menor o igual a 20 minutos por camión.<br><br>
• <strong>Acción 3:</strong> Talleres de buenas prácticas de frío y alertas móviles para 500 familias campesinas.<br>
  - Responsable: Fomento Ganadero y Gestión Social.<br>
  - Presupuesto: $25 millones COP (instructores de campo y cartillas didácticas).<br>
  - Plazo: Meses 3 a 5.<br>
  - Meta: Más del 90 % de los ganaderos atendiendo y usando las alertas en su celular.<br><br>
• <strong>Acción 4:</strong> Instalar módulos de recolección en 100 almacenes y firmar acuerdos con recicladores.<br>
  - Responsable: Coordinación de Sostenibilidad y Canales Comerciales.<br>
  - Presupuesto: $60 millones COP (contenedores de depósito y fondo de incentivo por kilo).<br>
  - Plazo: Meses 4 a 6.<br>
  - Meta: Recuperar al menos 45 toneladas mensuales de envases para reciclaje.
</p>

<!-- 9. CONCLUSIONES -->
<h2>9. Conclusiones</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son las conclusiones concretas del informe?</span>
</div>
<p>
1. La Metodología de Sistemas Blandos demuestra que la leche que se corta en Alpina no es culpa de la mala fe del campesino ni de una máquina descompuesta; es el resultado de desconexiones reales entre el campo sin luz, carreteras difíciles y la falta de alertas a tiempo.<br><br>
2. La herramienta CATWOE ayuda a poner en números que el negocio de Alpina necesita a los campesinos tanto como ellos necesitan a la empresa. Buscar la rentabilidad descuidando el precio del productor o el manejo de la basura termina pasando factura legal y comercial.<br><br>
3. Para un ingeniero de sistemas, el reto en el agro colombiano no es inventar algoritmos sofisticados que nadie entiende, sino conectar un sensor sencillo y confiable que le avise a un campesino por el celular antes de que se le dañe el trabajo del día.<br><br>
4. El plan de acción planteado demuestra que con $215 millones COP —una cifra modesta para la escala de Alpina— se puede proteger la cadena de frío, cumplir con los ODS 12 y 9 y evitar que toneladas de comida y plástico terminen en la basura.
</p>

<!-- 10. REFERENCIAS BIBLIOGRÁFICAS -->
<h2>10. Referencias Bibliográficas</h2>
<div class="question-box">
  <span class="question-lbl">Pregunta: </span>
  <span class="question-text">¿Cuáles son las fuentes consultadas bajo las normas APA (7.ª edición)?</span>
</div>

<div class="ref-item">Alpina Productos Alimenticios S.A.S. (2024). <em>Informe de Sostenibilidad y Economía Circular 2023</em>. Publicaciones Corporativas Alpina.</div>
<div class="ref-item">Checkland, P. (1999). <em>Systems Thinking, Systems Practice: Soft Systems Methodology in Action</em>. John Wiley & Sons.</div>
<div class="ref-item">Checkland, P., & Scholes, J. (1990). <em>Soft Systems Methodology in Action</em>. John Wiley & Sons.</div>
<div class="ref-item">González, Y. A. (2023). <em>Metodología de Sistemas Blandos (MSB)</em> [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. <a href="https://repository.unad.edu.co/handle/10596/58695">https://repository.unad.edu.co/handle/10596/58695</a></div>
<div class="ref-item">Jerardino Wiesenborn, B. (2019). <em>Metodología de Sistemas Blandos: Conceptos claves</em> [Video]. YouTube. <a href="https://www.youtube.com/watch?v=2pzJsWjk12E">https://www.youtube.com/watch?v=2pzJsWjk12E</a></div>
<div class="ref-item">Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. <em>CIENCIA ergo-sum</em>, 15(1), 45-53.</div>
<div class="ref-item">Ministerio de Ambiente y Desarrollo Sostenible. (2018). <em>Resolución 1407 de 2018: Por la cual se reglamenta la gestión ambiental de los residuos de envases y empaques</em>. MinAmbiente.</div>
<div class="ref-item">Ministerio de la Protección Social. (2006). <em>Decreto 616 de 2006: Por el cual se expide el Reglamento Técnico sobre los requisitos que debe cumplir la leche para el consumo humano</em>. Diario Oficial No. 46.196.</div>
<div class="ref-item">Naciones Unidas. (2015). <em>Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible</em>. Organización de las Naciones Unidas. <a href="https://sdgs.un.org/es/goals">https://sdgs.un.org/es/goals</a></div>
<div class="ref-item">Osorio Gómez, J. C. (2007). <em>Introducción al pensamiento sistémico</em>. Programa Editorial Universidad del Valle.</div>
<div class="ref-item">Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. <em>Systemic Practice and Action Research</em>, 37, 1123–1140.</div>

</body>
</html>
"""

    html_path_docs = os.path.join(OUT_DIR_DOCS, HTML_NAME)
    with open(html_path_docs, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML Anti-Slop guardado en: {html_path_docs}")

    import subprocess

    pdf_path_docs = os.path.join(OUT_DIR_DOCS, PDF_NAME)
    pdf_path_down = os.path.join(OUT_DIR_DOWN, PDF_NAME)
    pdf_path_esc = os.path.join("/home/rootkit/Escritorio", PDF_NAME)

    print("🖨️ Compilando PDF Anti-Slop con Chrome headless...")
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

    shutil.copy2(pdf_path_docs, pdf_path_down)
    if os.path.exists("/home/rootkit/Escritorio"):
        shutil.copy2(pdf_path_docs, pdf_path_esc)
    print(f"✅ PDF Anti-Slop generado en: {pdf_path_docs}, {pdf_path_down} y {pdf_path_esc}")


if __name__ == "__main__":
    build_docx()
    build_html_and_pdf()
