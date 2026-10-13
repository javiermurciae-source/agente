#!/usr/bin/env python3
"""
Compilador de Presentaciones HTML de Alto Rendimiento (16:9).
Inyecta datos estructurados en la plantilla maestra autocontenida
y genera un archivo 'index.html' listo para proyectar, grabar o compartir.
"""

import os
import sys
import json
import argparse
from datetime import datetime

TEMPLATE_PATH = "/home/rootkit/agente/skills/presentaciones-elite-html/templates/master_presentation.html"

DEFAULT_DATA = {
    "DECK_TITLE": "Presentación de Élite con IA — Arquitectura y Rendimiento",
    "DECK_TOPIC": "AI PRESENTATION FRAMEWORK",
    "HERO_TAG": "REVELACIÓN OFICIAL 2026",
    "HERO_TITLE_PRE": "El Futuro de las",
    "HERO_TITLE_HIGHLIGHT": "Presentaciones con IA",
    "HERO_TITLE_POST": "en Código",
    "HERO_SUBTITLE": "Decks interactivos en HTML5 con navegación instantánea por teclado, estética de estudio y cero fricción.",
    "PRESENTER_NAME": "Camilo & Agente Autónomo",
    "PRESENTATION_DATE": datetime.now().strftime("%d/%m/%Y"),
    
    "PROBLEM_TITLE": "¿Por qué fallan las diapositivas tradicionales?",
    "PROBLEM_SUBTITLE": "Las herramientas convencionales de diapositivas crean fricción constante, textos borrosos y diseños rígidos.",
    "PROBLEM_CARD_1_TITLE": "Texto Deformado y Slop Visual",
    "PROBLEM_CARD_1_DESC": "Los generadores de imagen convencionales deforman las palabras, no mantienen proporciones y rompen la estética profesional.",
    "PROBLEM_CARD_2_TITLE": "Falta de Interactividad Real",
    "PROBLEM_CARD_2_DESC": "Exportaciones estáticas en PDF o PPTX que no permiten animaciones fluidas, componentes web ni atajos de teclado para streaming.",

    "SOLUTION_TITLE": "HTML Nativo: Precisión Tipográfica y Flexibilidad",
    "SOLUTION_SUBTITLE": "Un único archivo autónomo de 1920x1080 con render determinista a 60 FPS y control total.",
    "SOLUTION_BIG_TITLE": "Control 100% Determinista",
    "SOLUTION_BIG_DESC": "Todo el contenido corre en tu navegador sin servidores pesados, con barra de progreso superior, temas conmutables y zona segura para cámara.",
    "SOLUTION_SIDE_TITLE": "Bento Grid & Estética Suiza",
    "SOLUTION_SIDE_DESC": "Jerarquía visual estricta inspirada en los eventos de Apple y Notion.",

    "BENTO_TITLE": "Los 3 Pilares del Sistema",
    "BENTO_SUBTITLE": "Ingeniería diseñada específicamente para grabación de video y pitch decks de impacto.",
    "BENTO_1_TITLE": "Navegación Fluida",
    "BENTO_1_DESC": "Teclas de flechas, barra espaciadora, dígitos 1-9 y gestos táctiles con transiciones instantáneas.",
    "BENTO_2_TITLE": "Zona Segura de Cámara",
    "BENTO_2_DESC": "Espacio protegido en la esquina inferior derecha para no tapar contenido clave al grabar explicadores.",
    "BENTO_3_TITLE": "Temas Dinámicos",
    "BENTO_3_DESC": "Cambia con la tecla T entre Dark Tech, Apple Keynote, Notion Minimal y Neo-Brutalist en vivo.",

    "STATS_TITLE": "Métricas de Rendimiento y Calidad",
    "STATS_SUBTITLE": "Parámetros técnicos medibles frente a herramientas convencionales.",
    "STAT_1_NUMBER": "99.8%",
    "STAT_1_LABEL": "Precisión Tipográfica",
    "STAT_1_SUB": "Texto nítido en display 4K sin artefactos ni desenfoques.",
    "STAT_2_NUMBER": "60 FPS",
    "STAT_2_LABEL": "Fluidez Constante",
    "STAT_2_SUB": "Transiciones analíticas con aceleración por hardware.",
    "STAT_3_NUMBER": "< 400ms",
    "STAT_3_LABEL": "Tiempo de Carga",
    "STAT_3_SUB": "Archivo único e independiente sin dependencias rotas.",

    "STEPS_TITLE": "Flujo de Implementación en 3 Pasos",
    "STEPS_SUBTITLE": "De un guion en bruto a una presentación de nivel cinematográfico.",
    "STEP_1_TITLE": "Deconstrucción del Guion",
    "STEP_1_DESC": "Se extrae el gancho inicial de 5s, el problema, la solución y los datos clave en formato estructurado.",
    "STEP_2_TITLE": "Inyección en Plantilla Maestra",
    "STEP_2_DESC": "El compilador empaqueta el contenido en el lienzo 16:9 con componentes Bento y tarjetas métricas.",
    "STEP_3_TITLE": "Grabación o Presentación en Vivo",
    "STEP_3_DESC": "Abre en pantalla completa (tecla F), activa la guía de cámara si grabas video y presenta con confianza.",

    "COMPARE_TITLE": "Contraste Directo de Métodos",
    "COMPARE_SUBTITLE": "La diferencia entre un borrador improvisado y una entrega de nivel estudio.",
    "COMPARE_BEFORE_DESC": "Herramientas pesadas, fuentes que se descuadran entre computadores, plantillas genéricas de internet y sobrecarga visual sin jerarquía.",
    "COMPARE_AFTER_DESC": "Diseño limpio, tipografía escalable, código semántico autocontenido, adaptabilidad a cualquier resolución y control con teclado.",

    "CLOSING_TAG": "LISTO PARA DESPLEGAR",
    "CLOSING_TITLE": "Crea Presentaciones que Dejen Huella",
    "CLOSING_SUBTITLE": "Estructura impecable, estética de estudio y ejecución quirúrgica en segundos.",
    "CTA_PRIMARY": "Iniciar Presentación en Pantalla Completa",
    "CTA_LINK": "Presiona [F] para pantalla completa • [T] para cambiar tema"
}

def build_deck(data_dict, output_path, theme="dark-tech"):
    if not os.path.exists(TEMPLATE_PATH):
        print(f"❌ Error: Plantilla no encontrada en {TEMPLATE_PATH}")
        sys.exit(1)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Combinar datos por defecto con los proporcionados
    final_data = dict(DEFAULT_DATA)
    final_data.update(data_dict)

    # Reemplazar variables
    for key, val in final_data.items():
        placeholder = f"{{{{{key}}}}}"
        html = html.replace(placeholder, str(val))

    # Inyectar tema
    html = html.replace('data-theme="dark-tech"', f'data-theme="{theme}"')

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✨ Presentación generada exitosamente:")
    print(f"   📁 Archivo: {output_path}")
    print(f"   🎨 Tema: {theme}")
    print(f"   📊 Diapositivas: 8 slides completas (16:9 1920x1080)")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Compilador de presentaciones HTML de élite")
    parser.add_argument("-o", "--output", default="/home/rootkit/Proyectos/demo-slides/index.html", help="Ruta del archivo HTML de salida")
    parser.add_argument("-t", "--theme", default="dark-tech", choices=["dark-tech", "apple-keynote", "notion-minimal", "neo-brutalist"], help="Tema visual inicial")
    parser.add_argument("-d", "--data", help="Ruta a archivo JSON con datos personalizados")
    parser.add_argument("--demo", action="store_true", help="Generar presentación de demostración con datos estándar")

    args = parser.parse_args()

    custom_data = {}
    if args.data and os.path.exists(args.data):
        with open(args.data, "r", encoding="utf-8") as f:
            custom_data = json.load(f)

    build_deck(custom_data, args.output, args.theme)

if __name__ == "__main__":
    main()
