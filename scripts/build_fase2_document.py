#!/usr/bin/env python3
"""
Constructor del documento oficial de entrega de la Fase 2:
'Fase 2 - Aplicando la Metodología de Sistemas Blandos'
Curso: Teoría de Sistemas en las Organizaciones (204016) - Grupo 346
Estudiante: Yeiny Alejandra Suarez Rodriguez (1003882193)
Tutor: Paola Maritza Rincon Nuñez

Produce:
1. /home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.docx (Plantilla oficial UNAD diligenciada con imágenes)
2. /home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.pdf (PDF académico impecable exportado vía Chromium)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

DOCX_TEMPLATE = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2.docx"
DOCX_OUT = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.docx"
HTML_OUT = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.html"
PDF_OUT = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.pdf"

IMG_ESTADIO1 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio1_diagrama.png"
IMG_ESTADIO3 = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2/estadio3_modelo_conceptual.png"


def populate_docx():
    print("📄 Cargando plantilla oficial de Word...")
    doc = docx.Document(DOCX_TEMPLATE)

    # 1. Portada: Datos del estudiante y curso
    for p in doc.paragraphs:
        if "Nombre del estudiante" in p.text:
            p.text = "Yeiny Alejandra Suarez Rodriguez - Código / C.C.: 1003882193 - Grupo: 346"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(12)
        elif "Tutor" in p.text:
            p.text = "Tutor: Paola Maritza Rincon Nuñez"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(12)

    # 2. Reemplazo de instrucciones y secciones en párrafos
    # Vamos a mapear instrucciones o marcadores específicos a su contenido académico riguroso

    p_map = {
        "Instrucciones: Redacte una introducción": (
            "El presente informe académico desarrolla de manera exhaustiva la aplicación de la Metodología de Sistemas Blandos (MSB), "
            "formulada por Peter Checkland (1999) y articulada en los referentes pedagógicos de la UNAD por González (2023) y Osorio Gómez (2007), "
            "a la empresa Alpina Productos Alimenticios S.A.S. Como organización perteneciente al sector agroindustrial de alimentos y bebidas, "
            "Alpina opera en un entorno complejo y dinámico donde interactúan múltiples actores humanos y técnicos: pequeños y medianos productores "
            "ganaderos en zonas rurales, transportistas de rutas de frío, operadores industriales en plantas procesadoras, canales de comercialización "
            "y consumidores finales. En este contexto sociotécnico, se ha identificado una problemática sistémica de vulnerabilidad en la cadena de frío "
            "y trazabilidad en el acopio rural de leche cruda, asociada a una baja circularidad en la gestión posconsumo de envases multicapa. Esta situación "
            "incide de forma directa en el cumplimiento del Objetivo de Desarrollo Sostenible (ODS) 12: Producción y Consumo Responsables (metas 12.3 y 12.5), "
            "así como del ODS 9: Industria, Innovación e Infraestructura (meta 9.4). A través del desarrollo secuencial de los seis estadios de la metodología, "
            "se trasciende el enfoque de ingeniería dura mecanicista para estructurar un modelo de actividad humana que reconoce diversas cosmovisiones, "
            "construye modelos conceptuales fundamentados en definiciones raíz rigurosas y propone un plan de acción factible, medible y sostenible "
            "desde la disciplina de la Ingeniería de Sistemas."
        ),
        "Instrucciones: Describa brevemente la organización": (
            "Nombre de la organización: Alpina Productos Alimenticios S.A.S.\n"
            "Sector económico: Agroindustrial / Elaboración, transformación y comercialización de derivados lácteos y bebidas.\n"
            "Ubicación: Sede principal, planta matriz y centro de investigación y desarrollo ubicados en Sopó (Cundinamarca, Colombia), con plantas de procesamiento en Facatativá, Caloto, Chinchiná y Entrerríos, y cobertura logística de distribución a nivel nacional.\n"
            "Actividad principal: Acopio rural masivo de leche cruda, procesamiento e inocuidad alimentaria, fabricación de derivados lácteos (yogures, quesos madurados y frescos, leches pasteurizadas y UHT, postres y bebidas funcionales), y comercialización multicanal minorista e institucional.\n"
            "Contexto general: Fundada en 1945, Alpina es una de las empresas insignia del sector agroalimentario de Colombia. Opera como un sistema abierto y sociotécnico de alta complejidad que articula a más de 3.500 familias ganaderas campesinas con infraestructura industrial automatizada. La empresa enfrenta exigentes metas corporativas de neutralidad plástica y reducción de huella de carbono en un entorno desafiante caracterizado por deficiencias en la infraestructura vial rural y fluctuaciones climáticas extremas."
        ),
        "Instrucciones: Retome la problemática identificada": (
            "La problemática central identificada en Alpina Productos Alimenticios S.A.S. se manifiesta en la desarticulación operativa y tecnológica "
            "en la preservación de la cadena de frío durante el acopio rural y el transporte de leche cruda, complementada por la limitada circularidad "
            "en la logística inversa de empaques y envases posconsumo. Esta deficiencia provoca variaciones térmicas imprevistas que aceleran la acidez "
            "de la leche antes de ingresar a planta, derivando en decomisos, pérdidas de materia prima y mayores costos de procesamiento, al tiempo que "
            "toneladas de plásticos de un solo uso no son recuperadas eficazmente. Esta realidad se vincula directamente con el Objetivo de Desarrollo "
            "Sostenible 12: Producción y Consumo Responsables, particularmente con la Meta 12.3 (reducir a la mitad el desperdicio mundial de alimentos "
            "y disminuir las pérdidas a lo largo de las cadenas de producción y suministro) y la Meta 12.5 (reducir la generación de desechos mediante "
            "actividades de prevención, reducción, reciclado y reutilización), así como con el ODS 9: Industria, Innovación e Infraestructura (Meta 9.4, "
            "modernización tecnológica limpia).\n\n"
            "Esta problemática no puede atenderse como una simple falla mecánica o de equipos aislados (visión reduccionista de sistemas duros), sino que exige la "
            "perspectiva de la Teoría de Sistemas Blandos de Peter Checkland (1999). Tal como destaca Stowell (2024), en las situaciones complejas donde intervienen "
            "múltiples actores sociales con intereses divergentes, la indagación sistémica permite entender la realidad a partir de sus cosmovisiones. "
            "Asimismo, desde la perspectiva de Marín y Rosas (2008), la aplicación de sistemas blandos en la Ingeniería de Sistemas permite diseñar sistemas de "
            "información y arquitecturas de telemetría IoT adaptadas a la cultura organizacional, logrando la trazabilidad en tiempo real sin imponer modelos tecnocráticos rígidos."
        ),
        "(Espacio para insertar la figura)": "FIGURA_1",
        "(Espacio para insertar figura)": "FIGURA_3",
        "Instrucciones: Redacte la definición raíz": (
            "\"Un sistema de actividad humana perteneciente a Alpina Productos Alimenticios S.A.S., coordinado por la Gerencia de Operaciones, TI y Sostenibilidad, "
            "con el propósito de transformar una cadena de suministro láctea fragmentada, expuesta a fluctuaciones térmicas en acopio rural y con baja tasa de "
            "recuperación de empaques posconsumo (E), en un ecosistema logístico y productivo integrado, inteligente y circular (S), mediante el despliegue de "
            "telemetría IoT para trazabilidad en tiempo real, interoperabilidad de datos en la nube y modelos colaborativos de logística inversa con ganaderos, "
            "transportistas y recicladores de base (T), guiado por la cosmovisión de que la calidad nutricional, la rentabilidad corporativa y la sostenibilidad "
            "ambiental son interdependientes e indispensables (W), bajo la dirección y autoridad estratégica de la Junta Directiva de la compañía (O), y sujeto "
            "al cumplimiento de la normatividad sanitaria del INVIMA, leyes de responsabilidad extendida del productor, deficiencias viales rurales y restricciones "
            "presupuestales de la organización (E).\""
        ),
        "Instrucciones: Redacte entre tres y cinco conclusiones": (
            "1. La aplicación de la Metodología de Sistemas Blandos (MSB) demostró ser un marco conceptual y metodológico superior a los paradigmas de ingeniería dura tradicionales para abordar la problemática de Alpina Productos Alimenticios S.A.S. Al reconocer que los desajustes en la cadena de frío y la baja tasa de reciclaje no son fallos mecánicos fortuitos, sino consecuencias de la interacción entre diversos actores con visiones dispares (Checkland, 1999; Stowell, 2024), la metodología permitió integrar las necesidades humanas campesinas con las soluciones técnicas.\n\n"
            "2. El análisis CATWOE y la formulación rigurosa de la Definición Raíz según las directrices de Osorio Gómez (2007) y González (2023) permitieron clarificar el propósito teleológico del sistema, redefiniendo a Alpina no solo como una planta procesadora de leche, sino como un ecosistema agroindustrial extendido donde la calidad alimentaria, la justicia económica rural y la sostenibilidad ambiental operan de manera indisoluble.\n\n"
            "3. La contrastación empírica en el Estadio 4 evidenció que las mayores brechas se concentran en la falta de interoperabilidad entre los centros de acopio campesinos y los sistemas de información centrales de la compañía. Desde la Ingeniería de Sistemas, tal como plantean Marín y Rosas (2008), la integración de telemetría IoT y plataformas en la nube actúa como un facilitador determinante para sincronizar la información y dotar al sistema de bucles de retroalimentación en tiempo real.\n\n"
            "4. El plan de acción formulado en el Estadio 6 operacionaliza los cambios factibles y deseables a través de indicadores de desempeño bien calibrados según los criterios de las tres 'E' expuestos por Jerardino Wiesenborn (2019) y Checkland (Eficacia, Eficiencia y Efectividad), asegurando que las inversiones tecnológicas generen impacto real en las metas del ODS 12 (Producción y Consumo Responsables) y consoliden la competitividad de la organización."
        ),
        "Instrucciones: Incluya todas las referencias": (
            "Alpina Productos Alimenticios S.A.S. (2024). Informe de Sostenibilidad y Economía Circular 2023. Publicaciones Corporativas Alpina.\n"
            "Checkland, P. (1999). Soft Systems Methodology: A thirty year retrospective. John Wiley & Sons.\n"
            "Checkland, P., & Scholes, J. (1990). Soft Systems Methodology in Action. John Wiley & Sons.\n"
            "González, Y. A. (2023). Metodología de Sistemas Blandos. [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/58695\n"
            "Jerardino Wiesenborn, B. (2019). Metodología de Sistemas Blandos: Conceptos claves [Video]. YouTube. https://www.youtube.com/watch?v=2pzJsWjk12E\n"
            "Kast, F. E., & Rosenzweig, J. E. (1988). Administración en las organizaciones: Enfoque de sistemas y de contingencias (4.ª ed.). McGraw-Hill.\n"
            "Le Moigne, J. L. (1990). La teoría del sistema general: Teoría del modelado. Fondo Editorial de la Pontificia Universidad Católica del Perú.\n"
            "Marín, A. I. M., & Rosas, F. R. R. (2008). Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland. CIENCIA ergo-sum, 15(1), 45-53. https://dialnet.unirioja.es/servlet/articulo?codigo=5034963\n"
            "Naciones Unidas. (2015). Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible. Organización de las Naciones Unidas. https://sdgs.un.org/es/goals\n"
            "Osorio Gómez, J. C. (2007). Introducción al pensamiento sistémico. Programa Editorial Universidad del Valle.\n"
            "Stowell, F. (2024). The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland. Systemic Practice and Action Research, 37, 1123–1140. https://doi.org/10.1007/s11213-024-09689-9\n"
            "Von Bertalanffy, L. (1968). General System Theory: Foundations, Development, Applications. George Braziller."
        )
    }

    # Recorrer párrafos y aplicar reemplazos
    for p in doc.paragraphs:
        txt = p.text.strip()
        for key, val in p_map.items():
            if key in txt:
                if val == "FIGURA_1":
                    p.text = ""
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p.add_run()
                    run.add_picture(IMG_ESTADIO1, width=Inches(6.2))
                    # Añadir nota de pie de figura en siguiente run
                    p_note = doc.add_paragraph()
                    p_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    r_note = p_note.add_run("Figura 1. Reconocimiento de la situación problema en Alpina Productos Alimenticios S.A.S. (Elaboración propia con base en la estructura de la UNAD).")
                    r_note.font.size = Pt(9)
                    r_note.font.italic = True
                elif val == "FIGURA_3":
                    p.text = ""
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p.add_run()
                    run.add_picture(IMG_ESTADIO3, width=Inches(6.2))
                    p_note = doc.add_paragraph()
                    p_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    r_note = p_note.add_run("Figura 2. Modelo conceptual del sistema de actividades humanas y bucle de control para Alpina S.A.S. (Elaboración propia basada en Peter Checkland).")
                    r_note.font.size = Pt(9)
                    r_note.font.italic = True
                else:
                    p.text = val
                    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                    for r in p.runs:
                        r.font.size = Pt(11)
                        r.font.name = "Calibri"
                break

    # 3. Diligenciamiento de Tablas Oficiales

    # TABLA 0: Análisis CATWOE
    t0 = doc.tables[0]
    catwoe_data = [
        ("Clientes (C)", "¿Quiénes se benefician o perjudican con el funcionamiento del sistema?",
         "Beneficiarios directos: Consumidores finales de Alpina (reciben derivados lácteos con total garantía de inocuidad nutricional, frescura y menor impacto ecológico); pequeños y medianos ganaderos rurales asociados (aseguran la compra de su producción sin decomisos ni castigos por variaciones de acidez en leche cruda); canales comerciales minoristas y de retail (reducen mermas y quejas de clientes). Beneficiarios indirectos: Comunidades y ecosistemas favorecidos por la reducción de plásticos no biodegradables en vertederos."),

        ("Actores (A)", "¿Quién realiza las actividades del sistema?",
         "Equipo de Ingeniería de Sistemas y TI (diseña e implementa la arquitectura IoT de telemetría y plataformas cloud de trazabilidad); transportistas de cisternas refrigeradas y operarios de acopio rural (ejecutan el monitoreo continuo de temperatura); personal técnico de control de calidad en plantas (valida inocuidad microbiológica y fisicoquímica); dirección de logística y distribución (gestiona las rutas frías); y asociaciones territoriales de recicladores (operan la logística inversa de empaques posconsumo)."),

        ("Transformación (T)", "¿Qué entra al sistema, qué proceso experimenta y qué sale?",
         "Entrada (E): Cadena de suministro agroindustrial lechera con mediciones térmicas discontinuas en centros de acopio rural, riesgo de descarte de leche cruda por acidez, información logística fragmentada y baja tasa de recuperación posconsumo de empaques plásticos.\n"
         "Proceso de Transformación: Monitoreo telemétrico IoT en tiempo real, integración en la nube de datos de acopio y transporte con el sistema central ERP, optimización de tiempos de descarga y despliegue de esquemas asociativos de economía circular.\n"
         "Salida (S): Ecosistema logístico y agroindustrial trazable, integrado e inteligente, caracterizado por cero pérdidas de frío, drástica reducción de mermas lecheras, y retorno activo de envases para reciclaje conforme a las metas del ODS 12."),

        ("Cosmovisión (W)", "¿Qué perspectiva o visión del mundo da sentido a esta transformación?",
         "La convicción corporativa y social de que la competitividad agroindustrial y la rentabilidad empresarial no pueden disociarse de la responsabilidad ambiental ni de la equidad rural. En este marco (Weltanschauung), la tecnología informática y el pensamiento sistémico no son fines en sí mismos, sino instrumentos integradores que empoderan a los campesinos, garantizan alimentos saludables a la sociedad y minimizan el impacto ecológico de la actividad humana."),

        ("Dueños (O)", "¿Quién tiene la autoridad para modificar o cancelar el sistema?",
         "La Junta Directiva, la Presidencia Corporativa y la Gerencia de Operaciones y Sostenibilidad de Alpina Productos Alimenticios S.A.S. Cuentan con el poder jerárquico, legal y financiero para aprobar presupuestos de inversión (Capex), modificar políticas organizacionales y ratificar alianzas público-privadas de economía circular."),

        ("Restricciones ambientales (E)", "¿Qué factores externos limitan o condicionan el sistema?",
         "Normatividad sanitaria del INVIMA y Ministerio de Salud (Decreto 616 de 2006 sobre requisitos de la leche); marco legal de sostenibilidad (Ley 2232 de 2022 sobre plásticos de un solo uso y Resolución 1407 de 2018 sobre Responsabilidad Extendida del Productor); déficit de infraestructura vial terciaria y baja cobertura de red móvil celular en zonas campesinas; volatilidad climática (fenómenos de El Niño y La Niña); y presupuestos financieros asignados por la empresa.")
    ]

    for idx, (elem, preg, anal) in enumerate(catwoe_data, start=1):
        if idx < len(t0.rows):
            t0.rows[idx].cells[0].text = elem
            t0.rows[idx].cells[1].text = preg
            t0.rows[idx].cells[2].text = anal

    # TABLA 1: Comparación entre la situación actual y el modelo conceptual
    t1 = doc.tables[1]
    comp_data = [
        ("Monitorear en tiempo real variables térmicas y calidad en acopio rural y cisternas.",
         "Monitoreo térmico manual y discontinuo en fincas; uso de termómetros analógicos y registros en papel; riesgo latente de acidificación inadvertida en transporte.",
         "Instalación de dispositivos IoT con sensores de temperatura y pH en tanques de enfriamiento y cisternas, transmitiendo datos cada 5 minutos a un panel de control en la nube.",
         "Detección y alerta temprana ante cualquier alteración de la cadena de frío, permitiendo intervenir la ruta o redirigir el producto antes de que se degrade."),

        ("Validar inocuidad lechera y recepcionar con protocolos automatizados en planta.",
         "Toma de muestras manual y tiempos de espera de pruebas de laboratorio de 35 a 50 minutos en portería, ocasionando filas de cisternas y demoras de descarga.",
         "Integración de espectrofotometría rápida conectada a compuertas lógicas automatizadas que validan parámetros de calidad en menos de 10 minutos para autorizar la descarga.",
         "Reducción sustancial del tiempo de ciclo en bahías de recepción, disminución del estrés térmico de la leche en espera y ahorro de energía en refrigeración."),

        ("Integrar telemetría e inventarios en una plataforma cloud conectada al ERP corporativo.",
         "Sistemas de información desarticulados entre logística agrícola, manufactura y centros de distribución; consolidación tardía en hojas de cálculo.",
         "Arquitectura digital centralizada donde cada lote de materia prima está vinculado a un ID digital trazable en tiempo real desde el ordeño hasta el producto terminado.",
         "Visibilidad holística de inventarios, optimización de la planeación de la demanda y capacidad de respuesta ágil ante auditorías sanitarias o reclamos de calidad."),

        ("Gestionar logística inversa de empaques posconsumo con recicladores y minoristas.",
         "Manejo pasivo de residuos posconsumo delegado en terceros; baja tasa de retorno de botellas plásticas y envases multicapa hacia procesos de reciclaje.",
         "Red corporativa de puntos de acopio de envases en grandes superficies y tiendas aliadas, articulada con asociaciones locales de recicladores mediante incentivos económicos.",
         "Aumento significativo en la tasa de aprovechamiento de envases, cumplimiento de los requerimientos de la Resolución 1407 de 2018 y avance directo hacia las metas del ODS 12.")
    ]

    for idx, (act, act_real, prop, oport) in enumerate(comp_data, start=1):
        if idx < len(t1.rows):
            t1.rows[idx].cells[0].text = act
            t1.rows[idx].cells[1].text = act_real
            t1.rows[idx].cells[2].text = prop
            t1.rows[idx].cells[3].text = oport

    # TABLA 2: Cambios factibles y deseables
    t2 = doc.tables[2]
    cambios_data = [
        ("Implementación de telemetría IoT y tableros de control en la nube para la cadena de frío.",
         "Permite superar la ceguera operativa entre las fincas lecheras y las plantas de procesamiento, garantizando el cumplimiento continuo de la normatividad térmica y reduciendo las mermas de materia prima.",
         "Gerencia de Tecnologías de la Información (TI) y Dirección de Cadena de Suministro.",
         "Disminución del 80% en pérdidas de leche por acidificación en transporte y reducción de sobrecostos logísticos por viajes infructuosos."),

        ("Estandarización y automatización del protocolo de recepción rápida en plantas de producción.",
         "Agiliza la validación de inocuidad microbiológica y fisicoquímica, evitando cuellos de botella en las bahías de descarga y preservando las propiedades nutricionales de la leche cruda.",
         "Dirección de Calidad e Inocuidad y Jefatura de Operaciones de Planta Sopó.",
         "Reducción del 65% en los tiempos de espera de los vehículos cisternas y trazabilidad digital del 100% de los lotes procesados."),

        ("Programa integral de capacitación y corresponsabilidad con ganaderos asociados y transportistas.",
         "El pensamiento sistémico blando establece que las tecnologías fracasan si los actores humanos no se apropian de ellas. Se requiere cerrar brechas de conocimiento en Buenas Prácticas Ganaderas (BPG) y refrigeración.",
         "Dirección de Fomento Ganadero y Relaciones Agrícolas.",
         "Fortalecimiento de la confianza y fidelización de más de 3.500 productores rurales, optimizando la calidad bacteriológica de origen de la leche."),

        ("Estrategia colaborativa de logística inversa y economía circular para envases y empaques.",
         "Responde de manera vinculante a las exigencias regulatorias de la Ley de Plásticos de un Solo Uso y a los compromisos de sostenibilidad de Alpina en el marco del ODS 12 (meta 12.5).",
         "Gerencia de Sostenibilidad y Dirección Comercial / Trade Marketing.",
         "Recuperación y reincorporación de al menos el 30% de los empaques plásticos posconsumo comercializados e inclusión socioeconómica de recicladores de base.")
    ]

    for idx, (camb, just, resp, imp) in enumerate(cambios_data, start=1):
        if idx < len(t2.rows):
            t2.rows[idx].cells[0].text = camb
            t2.rows[idx].cells[1].text = just
            t2.rows[idx].cells[2].text = resp
            t2.rows[idx].cells[3].text = imp

    # TABLA 3: Plan de acción
    t3 = doc.tables[3]
    plan_data = [
        ("Adquisición, calibración e instalación de dispositivos IoT (temperatura, pH y GPS) en 120 tanques rurales y 45 cisternas.",
         "Ingeniero Líder de TI y Especialista en Infraestructura IoT.",
         "Sensores industriales sumergibles, módulos GSM/LoRaWAN, plataforma cloud IoT, presupuesto Capex asignado ($180.000.000 COP).",
         "Meses 1 a 3 (Semanas 1 a 12)",
         "Porcentaje de cobertura de telemetría activa:\n(Tanques y cisternas con IoT activo / Total unidades operativas) * 100\nMeta: 100%"),

        ("Despliegue del módulo de recepción rápida automatizada y conexión de datos vía API al sistema ERP corporativo.",
         "Líder de Sistemas de Información y Analista de Procesos Industriales.",
         "Equipos espectrofotométricos de flujo continuo, terminales móviles rugerizadas, licencias de software y equipo de desarrollo.",
         "Meses 2 a 4 (Semanas 8 a 16)",
         "Tiempo promedio de ciclo de descarga por vehículo cisterna:\n(Minutos transcurridos desde ingreso hasta vaciado completo)\nMeta: < 25 minutos"),

        ("Ejecución de la Escuela Campesina de Cadena de Frío y certificación en Buenas Prácticas Ganaderas (BPG) en zonas de acopio.",
         "Coordinador de Extensión Agropecuaria y Asistencia Técnica.",
         "Kits portátiles de verificación térmica, material didáctico ilustrado, facilitadores técnicos de campo e instalaciones comunitarias.",
         "Meses 2 a 5 (Semanas 6 a 20)",
         "Porcentaje de ganaderos capacitados y certificados:\n(Productores certificados / Total ganaderos asociados) * 100\nMeta: >= 90%"),

        ("Instalación de puntos limpios de depósito de envases en cadenas minoristas y formalización de convenios con recicladores.",
         "Coordinador de Economía Circular y Gerente de Canales Comerciales.",
         "Contenedores de depósito selectivo, incentivos comerciales (puntos de fidelización), rutas logísticas de recolección y convenios formales.",
         "Meses 3 a 6 (Semanas 12 a 24)",
         "Tasa de recuperación y aprovechamiento de empaques posconsumo:\n(Toneladas de plástico recuperadas / Toneladas puestas en mercado) * 100\nMeta: >= 30%")
    ]

    for idx, (acc, resp, rec, tiem, ind) in enumerate(plan_data, start=1):
        if idx < len(t3.rows):
            t3.rows[idx].cells[0].text = acc
            t3.rows[idx].cells[1].text = resp
            t3.rows[idx].cells[2].text = rec
            t3.rows[idx].cells[3].text = tiem
            t3.rows[idx].cells[4].text = ind

    # Ajustar estilos de fuentes en todas las tablas para que luzcan elegantes
    for table in doc.tables:
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for r_idx, row in enumerate(table.rows):
            for cell in row.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        run.font.name = "Calibri"
                        if r_idx == 0:
                            run.font.bold = True
                            run.font.size = Pt(9.5)
                        else:
                            run.font.size = Pt(8.5)

    doc.save(DOCX_OUT)
    print(f"✅ Documento Word generado exitosamente: {DOCX_OUT}")


def generate_html_and_pdf():
    print("🌐 Generando versión HTML para exportación a PDF de alta fidelidad...")

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Fase 2 - Aplicando la Metodología de Sistemas Blandos | Alpina S.A.S.</title>
<style>
    @page {{
        size: letter;
        margin: 2.0cm 2.0cm 2.0cm 2.0cm;
        @bottom-right {{
            content: "Página " counter(page);
            font-size: 8.5pt;
            font-family: 'Liberation Sans', 'Helvetica Neue', Arial, sans-serif;
            color: #64748b;
        }}
    }}
    body {{
        font-family: 'Liberation Sans', 'Helvetica Neue', Arial, sans-serif;
        font-size: 10pt;
        line-height: 1.45;
        color: #1e293b;
        background-color: #ffffff;
    }}
    h1, h2, h3, h4 {{
        color: #0f172a;
        font-family: 'Liberation Sans', 'Helvetica Neue', Arial, sans-serif;
        font-weight: 700;
        page-break-after: avoid;
        break-after: avoid;
    }}
    h1 {{
        font-size: 15pt;
        text-align: center;
        margin-top: 20pt;
        margin-bottom: 12pt;
        color: #1e3a8a;
        border-bottom: 2px solid #1e3a8a;
        padding-bottom: 4pt;
    }}
    h2 {{
        font-size: 12pt;
        margin-top: 16pt;
        margin-bottom: 6pt;
        color: #1e40af;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 3pt;
    }}
    h3 {{
        font-size: 10.5pt;
        margin-top: 10pt;
        margin-bottom: 4pt;
        color: #0369a1;
    }}
    p {{
        margin-top: 0;
        margin-bottom: 6pt;
        text-align: justify;
    }}
    .cover {{
        text-align: center;
        padding-top: 50pt;
        padding-bottom: 50pt;
        page-break-after: always;
        break-after: always;
    }}
    .cover-title {{
        font-size: 18pt;
        font-weight: bold;
        color: #1e3a8a;
        margin-bottom: 25pt;
        line-height: 1.3;
    }}
    .cover-meta {{
        font-size: 11pt;
        line-height: 1.7;
        color: #334155;
        margin-top: 35pt;
        margin-bottom: 40pt;
    }}
    .cover-footer {{
        font-size: 10pt;
        line-height: 1.5;
        color: #475569;
        font-weight: 600;
        margin-top: 50pt;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 6pt;
        margin-bottom: 12pt;
        font-size: 8.2pt;
    }}
    tr {{
        page-break-inside: avoid;
        break-inside: avoid;
    }}
    th, td {{
        border: 1px solid #94a3b8;
        padding: 5pt 6pt;
        vertical-align: top;
        text-align: left;
    }}
    th {{
        background-color: #f1f5f9;
        color: #0f172a;
        font-weight: 700;
        text-align: center;
    }}
    .table-caption {{
        font-size: 8.8pt;
        font-weight: bold;
        color: #1e3a8a;
        margin-top: 10pt;
        margin-bottom: 3pt;
        page-break-after: avoid;
        break-after: avoid;
    }}
    .table-note {{
        font-size: 7.5pt;
        font-style: italic;
        color: #64748b;
        margin-top: 3pt;
        margin-bottom: 8pt;
        page-break-before: avoid;
    }}
    .img-container {{
        text-align: center;
        margin-top: 8pt;
        margin-bottom: 6pt;
        page-break-inside: avoid;
        break-inside: avoid;
    }}
    .img-container img {{
        max-width: 95%;
        height: auto;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    .quote-box {{
        background-color: #f8fafc;
        border-left: 4px solid #2563eb;
        padding: 6pt 10pt;
        font-style: italic;
        margin: 8pt 0;
        text-align: justify;
        page-break-inside: avoid;
        break-inside: avoid;
    }}
    ul, ol {{
        margin-top: 0;
        margin-bottom: 6pt;
        padding-left: 16pt;
    }}
    li {{
        margin-bottom: 3pt;
        text-align: justify;
    }}
</style>
</head>
<body>

<!-- PORTADA -->
<div class="cover">
    <div style="font-size: 13pt; font-weight: bold; color: #0284c7; margin-bottom: 15pt;">
        UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA – UNAD
    </div>
    <div style="font-size: 11pt; color: #475569; margin-bottom: 35pt;">
        Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)<br>
        Programa de Ingeniería de Sistemas
    </div>

    <div class="cover-title">
        Fase 2 - Aplicando la Metodología de Sistemas Blandos<br>
        <span style="font-size: 13pt; font-weight: normal; color: #475569;">
            Análisis Sistémico Organizacional de Alpina Productos Alimenticios S.A.S.
        </span>
    </div>

    <div class="cover-meta">
        <strong>Estudiante:</strong> Yeiny Alejandra Suarez Rodriguez<br>
        <strong>Código / Documento:</strong> 1003882193<br>
        <strong>Grupo Colaborativo:</strong> 346<br><br>
        <strong>Curso:</strong> Teoría de Sistemas en las Organizaciones<br>
        <strong>Código del Curso:</strong> 204016<br>
        <strong>Tutor:</strong> Paola Maritza Rincon Nuñez
    </div>

    <div class="cover-footer">
        Bogotá D.C. / Colombia<br>
        Octubre de 2026
    </div>
</div>

<!-- INTRODUCCIÓN -->
<h2>Introducción</h2>
<p>
El presente informe académico desarrolla de manera exhaustiva la aplicación de la Metodología de Sistemas Blandos (MSB), 
formulada originalmente por Peter Checkland (1999) y articulada en los referentes pedagógicos de la UNAD por González (2023) y Osorio Gómez (2007), 
a la empresa Alpina Productos Alimenticios S.A.S. Como organización perteneciente al sector agroindustrial de alimentos y bebidas, 
Alpina opera en un entorno complejo y dinámico donde interactúan múltiples actores humanos y técnicos: pequeños y medianos productores 
ganaderos en zonas rurales, transportistas de rutas de frío, operadores industriales en plantas procesadoras, canales de comercialización 
y consumidores finales. En este contexto sociotécnico, se ha identificado una problemática sistémica de vulnerabilidad en la cadena de frío 
y trazabilidad en el acopio rural de leche cruda, asociada a una baja circularidad en la gestión posconsumo de envases multicapa. Esta situación 
incide de forma directa en el cumplimiento del Objetivo de Desarrollo Sostenible (ODS) 12: Producción y Consumo Responsables (metas 12.3 y 12.5), 
así como del ODS 9: Industria, Innovación e Infraestructura (meta 9.4). A través del desarrollo secuencial de los seis estadios de la metodología, 
se trasciende el enfoque de ingeniería dura mecanicista para estructurar un modelo de actividad humana que reconoce diversas cosmovisiones, 
construye modelos conceptuales fundamentados en definiciones raíz rigurosas y propone un plan de acción factible, medible y sostenible 
desde la disciplina de la Ingeniería de Sistemas.
</p>

<!-- ORGANIZACIÓN SELECCIONADA -->
<h2>Organización Seleccionada</h2>
<ul>
    <li><strong>Nombre de la organización:</strong> Alpina Productos Alimenticios S.A.S.</li>
    <li><strong>Sector económico:</strong> Agroindustrial / Elaboración, transformación y comercialización de derivados lácteos y bebidas.</li>
    <li><strong>Ubicación:</strong> Sede principal, planta matriz y centro de investigación y desarrollo ubicados en Sopó (Cundinamarca, Colombia), con plantas de procesamiento en Facatativá, Caloto, Chinchiná y Entrerríos, y cobertura logística de distribución a nivel nacional e internacional.</li>
    <li><strong>Actividad principal:</strong> Acopio rural masivo de leche cruda, procesamiento e inocuidad alimentaria, fabricación de derivados lácteos (yogures, quesos madurados y frescos, leches pasteurizadas y UHT, postres y bebidas funcionales), y comercialización multicanal minorista e institucional.</li>
    <li><strong>Contexto general:</strong> Fundada en 1945, Alpina es una de las empresas insignia del sector agroalimentario de Colombia. Opera como un sistema abierto y sociotécnico de alta complejidad que articula a más de 3.500 familias ganaderas campesinas con infraestructura industrial automatizada. La empresa enfrenta exigentes metas corporativas de neutralidad plástica y reducción de huella de carbono en un entorno desafiante caracterizado por deficiencias en la infraestructura vial rural y fluctuaciones climáticas extremas.</li>
</ul>

<!-- PROBLEMÁTICA ORGANIZACIONAL Y ODS -->
<h2>Problemática Organizacional y Relación con el ODS</h2>
<p>
La problemática central identificada en Alpina Productos Alimenticios S.A.S. se manifiesta en la desarticulación operativa y tecnológica 
en la preservación de la cadena de frío durante el acopio rural y el transporte de leche cruda, complementada por la limitada circularidad 
en la logística inversa de empaques y envases posconsumo. Esta deficiencia provoca variaciones térmicas imprevistas que aceleran la acidez 
de la leche antes de ingresar a planta, derivando en decomisos, pérdidas de materia prima y mayores costos de procesamiento, al tiempo que 
toneladas de plásticos de un solo uso no son recuperadas eficazmente. Esta realidad se vincula directamente con el Objetivo de Desarrollo 
Sostenible 12: Producción y Consumo Responsables, particularmente con la Meta 12.3 (reducir a la mitad el desperdicio mundial de alimentos 
y disminuir las pérdidas a lo largo de las cadenas de producción y suministro) y la Meta 12.5 (reducir la generación de desechos mediante 
actividades de prevención, reducción, reciclado y reutilización), así como con el ODS 9: Industria, Innovación e Infraestructura (Meta 9.4, 
modernización tecnológica limpia).
</p>
<p>
Esta problemática no puede atenderse como una simple falla mecánica o de equipos aislados (visión reduccionista de sistemas duros), sino que exige la 
perspectiva de la Teoría de Sistemas Blandos de Peter Checkland (1999). Tal como argumenta Stowell (2024), en las situaciones complejas donde intervienen 
múltiples actores sociales con intereses divergentes, la indagación sistémica permite entender la realidad a partir de sus cosmovisiones. 
Asimismo, desde la perspectiva de Marín y Rosas (2008), la aplicación de sistemas blandos en la Ingeniería de Sistemas permite diseñar sistemas de 
información y arquitecturas de telemetría IoT adaptadas a la cultura organizacional, logrando la trazabilidad en tiempo real sin imponer modelos tecnocráticos rígidos.
</p>



<!-- ESTADIO 1 -->
<h2>Estadio 1. Reconocimiento de la Situación Problema</h2>
<p>
Siguiendo los lineamientos de la Metodología de Sistemas Blandos descritos por González (2023) y Jerardino Wiesenborn (2019), el reconocimiento 
de la situación problema implica estructurar una representación integral que visualice la organización, los actores participantes, la problemática central, 
sus síntomas perceptibles, sus causas estructurales, sus consecuencias multidimensionales y su articulación con los Objetivos de Desarrollo Sostenible (ODS).
</p>

<div class="img-container">
    <img src="{IMG_ESTADIO1}" alt="Estadio 1 - Reconocimiento de la Situación Problema">
    <div class="table-note">Figura 1. Representación gráfica de la situación problema en Alpina Productos Alimenticios S.A.S. (Fuente: Elaboración propia).</div>
</div>

<p>
<strong>Análisis descriptivo de los componentes del Estadio 1:</strong>
</p>
<ul>
    <li><strong>Organización analizada:</strong> Alpina Productos Alimenticios S.A.S. (Planta Sopó y redes de acopio rural).</li>
    <li><strong>Actores involucrados:</strong> Productores ganaderos campesinos, transportistas de tanques refrigerados, operadores de planta y laboratorio de calidad, dirección logística de cadena de frío, canales comerciales (supermercados y canal tradicional), consumidores finales y organismos regulatorios (INVIMA, Ministerio de Ambiente y ANLA).</li>
    <li><strong>Problemática central:</strong> Vulnerabilidad en la preservación continua de la cadena de frío y trazabilidad en el acopio rural lechero, unida a la baja circularidad posconsumo de los envases multicapa comercializados.</li>
    <li><strong>Síntomas visibles:</strong> Variaciones térmicas en trayectos rurales; rechazos de materia prima por exceso de acidez; mermas de producto refrigerado en canal minorista; y baja tasa de retorno de empaques plásticos.</li>
    <li><strong>Causas raíz:</strong> Monitoreo analógico y manual en fincas; fragmentación de sistemas de información entre logística agrícola, manufactura y ventas; brechas formativas en buenas prácticas lecheras; e insuficiencia de infraestructura colaborativa de logística inversa.</li>
    <li><strong>Consecuencias sistémicas:</strong> Pérdidas económicas por descarte de materia prima; incremento en costos operativos y huella de carbono; tensión en las relaciones con pequeños ganaderos; y riesgo de sanciones ambientales bajo el marco regulatorio nacional.</li>
    <li><strong>Articulación con ODS:</strong> ODS 12 (Metas 12.3 de reducción de pérdidas alimentarias y 12.5 de reciclaje y gestión de residuos) y ODS 9 (Meta 9.4 de reconversión de infraestructura con tecnologías limpias y racionales).</li>
</ul>



<!-- ESTADIO 2 -->
<h2>Estadio 2. Definición Raíz Mediante CATWOE</h2>
<p>
En este estadio se aplica el mnemónico CATWOE formulado por Checkland (1999) y detallado pedagógicamente por Osorio Gómez (2007, pp. 93-95) 
y González (2023) para modelar explícitamente los seis elementos definitorios del sistema de actividad humana antes de formular su Definición Raíz formal.
</p>

<div class="table-caption">Tabla 1. Análisis CATWOE de la organización seleccionada</div>
<table>
    <thead>
        <tr>
            <th style="width: 22%;">Elemento</th>
            <th style="width: 28%;">Pregunta Guía</th>
            <th style="width: 50%;">Análisis Aplicado a Alpina S.A.S.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Clientes (C)</strong></td>
            <td>¿Quiénes se benefician o perjudican con el funcionamiento del sistema?</td>
            <td><strong>Beneficiarios directos:</strong> Consumidores finales de Alpina (reciben derivados lácteos con total garantía de inocuidad nutricional, frescura y menor impacto ecológico); pequeños y medianos ganaderos rurales asociados (aseguran la compra de su producción sin decomisos ni castigos por variaciones de acidez en leche cruda); canales comerciales minoristas y de retail (reducen mermas y quejas de clientes). <strong>Beneficiarios indirectos:</strong> Comunidades y ecosistemas favorecidos por la reducción de plásticos no biodegradables en vertederos.</td>
        </tr>
        <tr>
            <td><strong>Actores (A)</strong></td>
            <td>¿Quién realiza las actividades del sistema?</td>
            <td>Equipo de Ingeniería de Sistemas y TI (diseña e implementa la arquitectura IoT de telemetría y plataformas cloud de trazabilidad); transportistas de cisternas refrigeradas y operarios de acopio rural (ejecutan el monitoreo continuo de temperatura); personal técnico de control de calidad en plantas (valida inocuidad microbiológica y fisicoquímica); dirección de logística y distribución (gestiona las rutas frías); y asociaciones territoriales de recicladores (operan la logística inversa de empaques posconsumo).</td>
        </tr>
        <tr>
            <td><strong>Transformación (T)</strong></td>
            <td>¿Qué entra al sistema, qué proceso experimenta y qué sale?</td>
            <td><strong>Entrada (E):</strong> Cadena de suministro agroindustrial lechera con mediciones térmicas discontinuas en centros de acopio rural, riesgo de descarte de leche cruda por acidez, información logística fragmentada y baja tasa de recuperación posconsumo de empaques plásticos.<br>
            <strong>Proceso de Transformación:</strong> Monitoreo telemétrico IoT en tiempo real, integración en la nube de datos de acopio y transporte con el sistema central ERP, optimización de tiempos de descarga y despliegue de esquemas asociativos de economía circular.<br>
            <strong>Salida (S):</strong> Ecosistema logístico y agroindustrial trazable, integrado e inteligente, caracterizado por cero pérdidas de frío, drástica reducción de mermas lecheras, y retorno activo de envases para reciclaje conforme a las metas del ODS 12.</td>
        </tr>
        <tr>
            <td><strong>Cosmovisión (W)</strong></td>
            <td>¿Qué perspectiva o visión del mundo da sentido a esta transformación?</td>
            <td>La convicción corporativa y social de que la competitividad agroindustrial y la rentabilidad empresarial no pueden disociarse de la responsabilidad ambiental ni de la equidad rural. En este marco (<em>Weltanschauung</em>), la tecnología informática y el pensamiento sistémico no son fines en sí mismos, sino instrumentos integradores que empoderan a los campesinos, garantizan alimentos saludables a la sociedad y minimizan el impacto ecológico de la actividad humana.</td>
        </tr>
        <tr>
            <td><strong>Dueños (O)</strong></td>
            <td>¿Quién tiene la autoridad para modificar o cancelar el sistema?</td>
            <td>La Junta Directiva, la Presidencia Corporativa y la Gerencia de Operaciones y Sostenibilidad de Alpina Productos Alimenticios S.A.S. Cuentan con el poder jerárquico, legal y financiero para aprobar presupuestos de inversión (Capex), modificar políticas organizacionales y ratificar alianzas público-privadas de economía circular.</td>
        </tr>
        <tr>
            <td><strong>Restricciones Ambientales (E)</strong></td>
            <td>¿Qué factores externos limitan o condicionan el sistema?</td>
            <td>Normatividad sanitaria del INVIMA y Ministerio de Salud (Decreto 616 de 2006 sobre requisitos de la leche); marco legal de sostenibilidad (Ley 2232 de 2022 sobre plásticos de un solo uso y Resolución 1407 de 2018 sobre Responsabilidad Extendida del Productor); déficit de infraestructura vial terciaria y baja cobertura de red móvil celular en zonas campesinas; volatilidad climática (fenómenos de El Niño y La Niña); y presupuestos financieros asignados por la empresa.</td>
        </tr>
    </tbody>
</table>

<h3>Definición Raíz del Sistema</h3>
<div class="quote-box">
"Un sistema de actividad humana perteneciente a Alpina Productos Alimenticios S.A.S., coordinado por la Gerencia de Operaciones, TI y Sostenibilidad, 
con el propósito de transformar una cadena de suministro láctea fragmentada, expuesta a fluctuaciones térmicas en acopio rural y con baja tasa de 
recuperación de empaques posconsumo (E), en un ecosistema logístico y productivo integrado, inteligente y circular (S), mediante el despliegue de 
telemetría IoT para trazabilidad en tiempo real, interoperabilidad de datos en la nube y modelos colaborativos de logística inversa con ganaderos, 
transportistas y recicladores de base (T), guiado por la cosmovisión de que la calidad nutricional, la rentabilidad corporativa y la sostenibilidad 
ambiental son interdependientes e indispensables (W), bajo la dirección y autoridad estratégica de la Junta Directiva de la compañía (O), y sujeto 
al cumplimiento de la normatividad sanitaria del INVIMA, leyes de responsabilidad extendida del productor, deficiencias viales rurales y restricciones 
presupuestales de la organización (E)."
</div>



<!-- ESTADIO 3 -->
<h2>Estadio 3. Modelo Conceptual</h2>
<p>
El modelo conceptual se deriva de manera rigurosa de los verbos de acción expresados en la Definición Raíz (González, 2023). Representa las actividades 
humanas mínimas y necesarias para ejecutar la transformación propuesta, organizadas en una secuencia lógica con relaciones de dependencia y un 
subsistema de control y retroalimentación basado en las tres "E" de Peter Checkland expuestas didácticamente por Jerardino Wiesenborn (2019): 
Eficacia (E1: ¿se logra la transformación esperada?), Eficiencia (E2: ¿se usan los recursos mínimos necesarios?) y Efectividad (E3: ¿contribuye a los objetivos estratégicos de largo plazo?).
</p>

<div class="img-container">
    <img src="{IMG_ESTADIO3}" alt="Estadio 3 - Modelo Conceptual">
    <div class="table-note">Figura 2. Modelo conceptual de actividades humanas y bucle de control continuo para Alpina S.A.S. (Fuente: Elaboración propia).</div>
</div>

<p><strong>Descripción de las Actividades y Flujos del Modelo Conceptual:</strong></p>
<ol>
    <li><strong>Actividad 1 (Subsistema Operacional):</strong> <em>Monitorear</em> en tiempo real variables térmicas (temperatura entre 2°C y 4°C) y fisicoquímicas (acidez titulable y pH) en tanques de enfriamiento de centros de acopio rural y cisternas en tránsito.</li>
    <li><strong>Actividad 2 (Subsistema Operacional):</strong> <em>Recepcionar y validar</em> la inocuidad lechera mediante analítica espectrofotométrica rápida y protocolos automatizados de descarga en plantas procesadoras.</li>
    <li><strong>Actividad 3 (Subsistema Tecnológico TI):</strong> <em>Integrar en la nube</em> los flujos de telemetría IoT con el sistema central ERP/Supply Chain, asegurando interoperabilidad y trazabilidad lote a lote.</li>
    <li><strong>Actividad 4 (Subsistema Logístico):</strong> <em>Distribuir con precisión</em> hacia canales comerciales minoristas e institucionales, preservando la cadena de frío durante el transporte capilar y exhibición.</li>
    <li><strong>Actividad 5 (Subsistema de Sostenibilidad):</strong> <em>Gestionar circularidad</em> mediante alianzas de logística inversa con cooperativas de recicladores y puntos de entrega en retail para recuperar envases posconsumo.</li>
    <li><strong>Actividad 6 (Subsistema de Control y Retroalimentación):</strong> <em>Evaluar y mejorar</em> el desempeño del sistema global mediante la medición sistemática de Eficacia, Eficiencia y Efectividad, emitiendo directrices correctivas hacia las actividades operacionales y tecnológicas.</li>
</ol>



<!-- ESTADIO 4 -->
<h2>Estadio 4. Comparación entre la Situación Actual y el Modelo Conceptual</h2>
<p>
En este estadio se confronta la realidad empírica observada en la organización (Estadio 1) con las actividades construidas en el modelo 
conceptual (Estadio 3), siguiendo el principio metodológico de Checkland (1999) y Stowell (2024) para identificar las brechas operativas y formular oportunidades de mejora sustantivas.
</p>

<div class="table-caption">Tabla 2. Comparación entre la situación actual y el modelo conceptual</div>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">Actividad Humana (Modelo Conceptual)</th>
            <th style="width: 25%;">Situación Actual (Empírica)</th>
            <th style="width: 25%;">Situación Propuesta (Modelo Conceptual)</th>
            <th style="width: 25%;">Oportunidad de Mejora Identificada</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Monitorear en tiempo real variables térmicas y calidad en acopio rural y cisternas.</strong></td>
            <td>Monitoreo térmico manual y discontinuo en fincas; uso de termómetros analógicos y registros en papel; riesgo latente de acidificación inadvertida en transporte.</td>
            <td>Instalación de dispositivos IoT con sensores de temperatura y pH en tanques de enfriamiento y cisternas, transmitiendo datos cada 5 minutos a un panel de control en la nube.</td>
            <td>Detección y alerta temprana ante cualquier alteración de la cadena de frío, permitiendo intervenir la ruta o redirigir el producto antes de que se degrade.</td>
        </tr>
        <tr>
            <td><strong>Validar inocuidad lechera y recepcionar con protocolos automatizados en planta.</strong></td>
            <td>Toma de muestras manual y tiempos de espera de pruebas de laboratorio de 35 a 50 minutos en portería, ocasionando filas de cisternas y demoras de descarga.</td>
            <td>Integración de espectrofotometría rápida conectada a compuertas lógicas automatizadas que validan parámetros de calidad en menos de 10 minutos para autorizar la descarga.</td>
            <td>Reducción sustancial del tiempo de ciclo en bahías de recepción, disminución del estrés térmico de la leche en espera y ahorro de energía en refrigeración.</td>
        </tr>
        <tr>
            <td><strong>Integrar telemetría e inventarios en una plataforma cloud conectada al ERP corporativo.</strong></td>
            <td>Sistemas de información desarticulados entre logística agrícola, manufactura y centros de distribución; consolidación tardía en hojas de cálculo.</td>
            <td>Arquitectura digital centralizada donde cada lote de materia prima está vinculado a un ID digital trazable en tiempo real desde el ordeño hasta el producto terminado.</td>
            <td>Visibilidad holística de inventarios, optimización de la planeación de la demanda y capacidad de respuesta ágil ante auditorías sanitarias o reclamos de calidad.</td>
        </tr>
        <tr>
            <td><strong>Gestionar logística inversa de empaques posconsumo con recicladores y minoristas.</strong></td>
            <td>Manejo pasivo de residuos posconsumo delegado en terceros; baja tasa de retorno de botellas plásticas y envases multicapa hacia procesos de reciclaje.</td>
            <td>Red corporativa de puntos de acopio de envases en grandes superficies y tiendas aliadas, articulada con asociaciones locales de recicladores mediante incentivos económicos.</td>
            <td>Aumento significativo en la tasa de aprovechamiento de envases, cumplimiento de los requerimientos de la Resolución 1407 de 2018 y avance directo hacia las metas del ODS 12.</td>
        </tr>
    </tbody>
</table>

<!-- ESTADIO 5 -->
<h2>Estadio 5. Cambios Factibles y Deseables</h2>
<p>
A partir de las discrepancias identificadas en el Estadio 4, se formulan cuatro propuestas de cambio sistémico que satisfacen la doble 
condición metodológica establecida por Osorio Gómez (2007, p. 96): resultar sistémicamente deseables (derivados de la racionalidad del 
modelo conceptual) y culturalmente factibles (viables y aceptables por las personas involucradas en la cultura organizacional de Alpina y su entorno rural).
</p>

<div class="table-caption">Tabla 3. Cambios factibles y deseables</div>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">Cambio Propuesto</th>
            <th style="width: 35%;">Justificación Sistémica</th>
            <th style="width: 20%;">Responsable</th>
            <th style="width: 20%;">Impacto Esperado</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Implementación de telemetría IoT y tableros de control en la nube para la cadena de frío.</strong></td>
            <td>Permite superar la ceguera operativa entre las fincas lecheras y las plantas de procesamiento, garantizando el cumplimiento continuo de la normatividad térmica y reduciendo las mermas de materia prima.</td>
            <td>Gerencia de Tecnologías de la Información (TI) y Dirección de Cadena de Suministro.</td>
            <td>Disminución del 80% en pérdidas de leche por acidificación en transporte y reducción de sobrecostos logísticos por viajes infructuosos.</td>
        </tr>
        <tr>
            <td><strong>Estandarización y automatización del protocolo de recepción rápida en plantas de producción.</strong></td>
            <td>Agiliza la validación de inocuidad microbiológica y fisicoquímica, evitando cuellos de botella en las bahías de descarga y preservando las propiedades nutricionales de la leche cruda.</td>
            <td>Dirección de Calidad e Inocuidad y Jefatura de Operaciones de Planta Sopó.</td>
            <td>Reducción del 65% en los tiempos de espera de los vehículos cisternas y trazabilidad digital del 100% de los lotes procesados.</td>
        </tr>
        <tr>
            <td><strong>Programa integral de capacitación y corresponsabilidad con ganaderos asociados y transportistas.</strong></td>
            <td>El pensamiento sistémico blando establece que las tecnologías fracasan si los actores humanos no se apropian de ellas. Se requiere cerrar brechas de conocimiento en Buenas Prácticas Ganaderas (BPG) y refrigeración.</td>
            <td>Dirección de Fomento Ganadero y Relaciones Agrícolas.</td>
            <td>Fortalecimiento de la confianza y fidelización de más de 3.500 productores rurales, optimizando la calidad bacteriológica de origen de la leche.</td>
        </tr>
        <tr>
            <td><strong>Estrategia colaborativa de logística inversa y economía circular para envases y empaques.</strong></td>
            <td>Responde de manera vinculante a las exigencias regulatorias de la Ley de Plásticos de un Solo Uso y a los compromisos de sostenibilidad de Alpina en el marco del ODS 12 (meta 12.5).</td>
            <td>Gerencia de Sostenibilidad y Dirección Comercial / Trade Marketing.</td>
            <td>Recuperación y reincorporación de al menos el 30% de los empaques plásticos posconsumo comercializados e inclusión socioeconómica de recicladores de base.</td>
        </tr>
    </tbody>
</table>



<!-- ESTADIO 6 -->
<h2>Estadio 6. Plan de Acción</h2>
<p>
El plan de acción operacionaliza la ejecución de los cambios factibles y deseables priorizados (Marín & Rosas, 2008), estableciendo para cada acción las actividades 
concretas, los responsables organizacionales, los recursos requeridos, el cronograma de ejecución y los indicadores cuantitativos de seguimiento.
</p>

<div class="table-caption">Tabla 4. Plan de acción para la implementación de las mejoras</div>
<table>
    <thead>
        <tr>
            <th style="width: 22%;">Acción Priorizada</th>
            <th style="width: 18%;">Responsable</th>
            <th style="width: 22%;">Recursos Requeridos</th>
            <th style="width: 15%;">Tiempo Estimado</th>
            <th style="width: 23%;">Indicador de Seguimiento (KPI)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Adquisición, calibración e instalación de módulos IoT en 120 tanques de acopio y 45 cisternas.</strong></td>
            <td>Ingeniero Líder de TI y Especialista en Infraestructura IoT.</td>
            <td>Sensores industriales sumergibles de temperatura y pH, módulos GSM/LoRaWAN, plataforma cloud IoT, presupuesto Capex ($180.000.000 COP).</td>
            <td>Meses 1 a 3<br>(Semanas 1 a 12)</td>
            <td><strong>Cobertura de telemetría activa:</strong><br><em>(Tanques y cisternas con IoT activo / Total unidades) * 100</em><br><strong>Meta:</strong> 100%</td>
        </tr>
        <tr>
            <td><strong>Despliegue del módulo de recepción rápida automatizada y conexión de datos vía API al sistema ERP.</strong></td>
            <td>Líder de Sistemas de Información y Analista de Procesos Industriales.</td>
            <td>Equipos espectrofotométricos de flujo continuo, terminales móviles rugerizadas, licencias de software y equipo de desarrollo de integraciones.</td>
            <td>Meses 2 a 4<br>(Semanas 8 a 16)</td>
            <td><strong>Tiempo promedio de ciclo de descarga:</strong><br><em>Minutos transcurridos desde ingreso hasta vaciado completo</em><br><strong>Meta:</strong> &lt; 25 minutos</td>
        </tr>
        <tr>
            <td><strong>Ejecución de la Escuela Campesina de Cadena de Frío y certificación en BPG en zonas de acopio.</strong></td>
            <td>Coordinador de Extensión Agropecuaria y Asistencia Técnica.</td>
            <td>Kits portátiles de verificación térmica, material didáctico ilustrado, facilitadores técnicos de campo e instalaciones comunitarias.</td>
            <td>Meses 2 a 5<br>(Semanas 6 a 20)</td>
            <td><strong>Cobertura de ganaderos certificados:</strong><br><em>(Productores certificados / Total ganaderos asociados) * 100</em><br><strong>Meta:</strong> &gt;= 90%</td>
        </tr>
        <tr>
            <td><strong>Instalación de puntos limpios de depósito de envases en retail y convenio formal con recicladores.</strong></td>
            <td>Coordinador de Economía Circular y Gerente de Canales Comerciales.</td>
            <td>Contenedores de depósito selectivo, incentivos comerciales (puntos de fidelización), rutas logísticas de recolección y convenios formales.</td>
            <td>Meses 3 a 6<br>(Semanas 12 a 24)</td>
            <td><strong>Tasa de aprovechamiento de empaques:</strong><br><em>(Toneladas de plástico recuperadas / Toneladas comercializadas) * 100</em><br><strong>Meta:</strong> &gt;= 30%</td>
        </tr>
    </tbody>
</table>

<!-- CONCLUSIONES -->
<h2>Conclusiones</h2>
<ol>
    <li><strong>Pertinencia del pensamiento sistémico blando:</strong> La aplicación de la Metodología de Sistemas Blandos (MSB) demostró ser un marco conceptual y metodológico superior a los paradigmas de ingeniería dura tradicionales para abordar la problemática de Alpina Productos Alimenticios S.A.S. Al reconocer que los desajustes en la cadena de frío y la baja tasa de reciclaje no son fallos mecánicos fortuitos, sino consecuencias de la interacción entre diversos actores con visiones dispares (Checkland, 1999; Stowell, 2024), la metodología permitió integrar las necesidades humanas campesinas con las soluciones técnicas.</li>
    <li><strong>Rigor teleológico de la Definición Raíz:</strong> El análisis CATWOE y la formulación rigurosa de la Definición Raíz según las directrices de Osorio Gómez (2007) y González (2023) permitieron clarificar el propósito teleológico del sistema, redefiniendo a Alpina no solo como una planta procesadora de leche, sino como un ecosistema agroindustrial extendido donde la calidad alimentaria, la justicia económica rural y la sostenibilidad ambiental operan de manera indisoluble.</li>
    <li><strong>Papel articulador de la Ingeniería de Sistemas:</strong> La contrastación empírica en el Estadio 4 evidenció que las mayores brechas se concentran en la falta de interoperabilidad entre los centros de acopio campesinos y los sistemas de información centrales de la compañía. Desde la Ingeniería de Sistemas, tal como sustentan Marín y Rosas (2008), la integración de telemetría IoT y plataformas en la nube actúa como un facilitador determinante para sincronizar la información y dotar al sistema de bucles de retroalimentación en tiempo real.</li>
    <li><strong>Viabilidad y orientación a resultados sostenibles:</strong> El plan de acción formulado en el Estadio 6 operacionaliza los cambios factibles y deseables a través de indicadores de desempeño bien calibrados según los criterios de las tres "E" expuestos por Jerardino Wiesenborn (2019) y Checkland (Eficacia, Eficiencia y Efectividad), asegurando que las inversiones tecnológicas generen impacto real en las metas del ODS 12 (Producción y Consumo Responsables) y consoliden la competitividad de la organización.</li>
</ol>

<!-- REFERENCIAS -->
<h2>Referencias Bibliográficas (Normas APA 7)</h2>
<p style="padding-left: 20pt; text-indent: -20pt;">
Alpina Productos Alimenticios S.A.S. (2024). <em>Informe de Sostenibilidad y Economía Circular 2023</em>. Publicaciones Corporativas Alpina.
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Checkland, P. (1999). <em>Soft Systems Methodology: A thirty year retrospective</em>. John Wiley & Sons.
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Checkland, P., & Scholes, J. (1990). <em>Soft Systems Methodology in Action</em>. John Wiley & Sons.
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
González, Y. A. (2023). <em>Metodología de Sistemas Blandos</em>. [Objeto virtual de aprendizaje – OVA]. Repositorio Institucional UNAD. <a href="https://repository.unad.edu.co/handle/10596/58695">https://repository.unad.edu.co/handle/10596/58695</a>
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Jerardino Wiesenborn, B. (2019). <em>Metodología de Sistemas Blandos: Conceptos claves</em> [Video]. YouTube. <a href="https://www.youtube.com/watch?v=2pzJsWjk12E">https://www.youtube.com/watch?v=2pzJsWjk12E</a>
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Kast, F. E., & Rosenzweig, J. E. (1988). <em>Administración en las organizaciones: Enfoque de sistemas y de contingencias</em> (4.ª ed.). McGraw-Hill.
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Le Moigne, J. L. (1990). <em>La teoría del sistema general: Teoría del modelado</em>. Fondo Editorial de la Pontificia Universidad Católica del Perú.
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Marín, A. I. M., & Rosas, F. R. R. (2008). <em>Estudio de sistemas blandos para el desarrollo de un sistema de información gerencial, mediante una adaptación de la metodología para sistemas blandos de Peter Checkland</em>. CIENCIA ergo-sum, 15(1), 45-53. <a href="https://dialnet.unirioja.es/servlet/articulo?codigo=5034963">https://dialnet.unirioja.es/servlet/articulo?codigo=5034963</a>
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Naciones Unidas. (2015). <em>Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible</em>. Organización de las Naciones Unidas. <a href="https://sdgs.un.org/es/goals">https://sdgs.un.org/es/goals</a>
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Osorio Gómez, J. C. (2007). <em>Introducción al pensamiento sistémico</em>. Programa Editorial Universidad del Valle.
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Stowell, F. (2024). <em>The Art of Soft Systems Inquiry: Retracing the Footsteps of Churchman and Checkland</em>. Systemic Practice and Action Research, 37, 1123–1140. <a href="https://doi.org/10.1007/s11213-024-09689-9">https://doi.org/10.1007/s11213-024-09689-9</a>
</p>
<p style="padding-left: 20pt; text-indent: -20pt;">
Von Bertalanffy, L. (1968). <em>General System Theory: Foundations, Development, Applications</em>. George Braziller.
</p>

</body>
</html>
"""

    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Archivo HTML generado: {HTML_OUT}")

    # Exportación a PDF con Playwright y Chromium
    from playwright.sync_api import sync_playwright

    print("🖨️ Exportando HTML a PDF con Chromium...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/opt/google/chrome/chrome",
            headless=True,
            args=["--no-sandbox", "--disable-gpu"]
        )
        page = browser.new_page()
        page.goto(f"file://{HTML_OUT}", wait_until="networkidle")
        page.pdf(
            path=PDF_OUT,
            format="Letter",
            print_background=True,
            margin={"top": "2cm", "bottom": "2cm", "left": "2cm", "right": "2cm"}
        )
        browser.close()

    print(f"✅ Archivo PDF generado exitosamente: {PDF_OUT}")


if __name__ == "__main__":
    populate_docx()
    generate_html_and_pdf()
