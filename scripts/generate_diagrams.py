#!/usr/bin/env python3
"""
Generador de diagramas de alta resolución para la Fase 2 de Teoría de Sistemas (UNAD).
Genera:
- estadio1_diagrama.png: Reconocimiento de la situación problema (Alpina S.A.S.)
- estadio3_modelo_conceptual.png: Modelo conceptual derivado de la Definición Raíz
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

OUTPUT_DIR = "/home/rootkit/Documentos/UNAD/204016_Sistemas/Fase_2"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_diagram_estadio1():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Fondo general suave
    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#f8fafc")

    # Título superior
    title_box = patches.FancyBboxPatch((0.5, 7.6), 12.0, 0.7, boxstyle="round,pad=0.1,rounding_size=0.15",
                                       facecolor="#1e3a8a", edgecolor="#172554", linewidth=1.5)
    ax.add_patch(title_box)
    ax.text(6.5, 8.05, "Estadio 1. Reconocimiento de la Situación Problema",
            fontsize=15, fontweight="bold", color="white", ha="center", va="center", fontfamily="sans-serif")
    ax.text(6.5, 7.75, "Caso de Estudio: Alpina Productos Alimenticios S.A.S. | Análisis Sistémico Blando",
            fontsize=10.5, color="#bfdbfe", ha="center", va="center", fontfamily="sans-serif")

    # Bloque Central: Organización y Problema Central
    center_box = patches.FancyBboxPatch((3.8, 3.4), 5.4, 3.8, boxstyle="round,pad=0.15,rounding_size=0.2",
                                        facecolor="#ffffff", edgecolor="#2563eb", linewidth=2.5,
                                        linestyle="-")
    ax.add_patch(center_box)

    # Encabezado Central
    c_header = patches.FancyBboxPatch((3.9, 6.4), 5.2, 0.7, boxstyle="round,pad=0.08,rounding_size=0.1",
                                     facecolor="#dbeafe", edgecolor="#93c5fd", linewidth=1)
    ax.add_patch(c_header)
    ax.text(6.5, 6.85, "ALPINA PRODUCTOS ALIMENTICIOS S.A.S.",
            fontsize=11.5, fontweight="bold", color="#1e3a8a", ha="center", va="center")
    ax.text(6.5, 6.55, "Sector Agroindustrial Lácteo y Bebidas | Planta Sopó",
            fontsize=9, color="#1e40af", ha="center", va="center")

    # Contenido Central (Problemática Central)
    prob_box = patches.FancyBboxPatch((4.0, 3.6), 5.0, 2.65, boxstyle="round,pad=0.1,rounding_size=0.1",
                                     facecolor="#fef2f2", edgecolor="#f87171", linewidth=1.2)
    ax.add_patch(prob_box)
    ax.text(6.5, 6.0, "[!] PROBLEMÁTICA CENTRAL IDENTIFICADA",
            fontsize=10.5, fontweight="bold", color="#991b1b", ha="center", va="center")

    prob_text = (
        "Desarticulación sistémica en la cadena de frío,\n"
        "trazabilidad de leche cruda en centros de acopio rural\n"
        "y baja circularidad en la logística inversa de empaques,\n"
        "lo que genera mermas operacionales, sobrecostos y huella\n"
        "ambiental en la red de suministro agroindustrial."
    )
    ax.text(6.5, 4.85, prob_text, fontsize=9.2, color="#7f1d1d", ha="center", va="center",
            multialignment="center", linespacing=1.35)

    # Columna Izquierda: Actores Involucrados
    actores_box = patches.FancyBboxPatch((0.5, 2.5), 3.0, 4.7, boxstyle="round,pad=0.12,rounding_size=0.15",
                                         facecolor="#ffffff", edgecolor="#0284c7", linewidth=1.8)
    ax.add_patch(actores_box)
    act_hdr = patches.FancyBboxPatch((0.6, 6.6), 2.8, 0.5, boxstyle="round,pad=0.05,rounding_size=0.08",
                                     facecolor="#e0f2fe", edgecolor="#7dd3fc", linewidth=1)
    ax.add_patch(act_hdr)
    ax.text(2.0, 6.85, "ACTORES INVOLUCRADOS", fontsize=10, fontweight="bold", color="#0369a1", ha="center", va="center")

    actores_items = [
        "• Proveedores Ganaderos\n  (Campesinos y fincas lecheras)",
        "• Transportistas de Cisternas\n  (Rutas y acopio refrigerado)",
        "• Operadores y Calidad en Planta\n  (Procesamiento y control)",
        "• Dirección de Logística y TI\n  (Planificación y monitoreo)",
        "• Distribuidores y Retail\n  (Supermercados y tiendas)",
        "• Consumidores Finales\n  (Destino y manejo de empaques)",
        "• Entes de Regulación\n  (INVIMA, MinAmbiente, ANLA)"
    ]
    y_pos = 6.25
    for item in actores_items:
        ax.text(0.7, y_pos, item, fontsize=8.2, color="#0f172a", va="top", linespacing=1.2)
        y_pos -= 0.58

    # Columna Derecha Superior: Síntomas
    sint_box = patches.FancyBboxPatch((9.5, 5.25), 3.0, 1.95, boxstyle="round,pad=0.1,rounding_size=0.12",
                                      facecolor="#ffffff", edgecolor="#f59e0b", linewidth=1.5)
    ax.add_patch(sint_box)
    sint_hdr = patches.FancyBboxPatch((9.6, 6.75), 2.8, 0.38, boxstyle="round,pad=0.05,rounding_size=0.08",
                                      facecolor="#fef3c7", edgecolor="#fde68a", linewidth=1)
    ax.add_patch(sint_hdr)
    ax.text(11.0, 6.94, "SÍNTOMAS VISIBLES", fontsize=9.5, fontweight="bold", color="#b45309", ha="center", va="center")

    sint_text = (
        "• Fluctuación térmica en rutas rurales\n"
        "• Rechazos de leche cruda por acidez\n"
        "• Mermas de producto refrigerado\n"
        "• Baja tasa de retorno de empaques"
    )
    ax.text(9.7, 6.6, sint_text, fontsize=8.2, color="#1e293b", va="top", linespacing=1.3)

    # Columna Derecha Media: Causas
    caus_box = patches.FancyBboxPatch((9.5, 3.1), 3.0, 1.95, boxstyle="round,pad=0.1,rounding_size=0.12",
                                      facecolor="#ffffff", edgecolor="#ea580c", linewidth=1.5)
    ax.add_patch(caus_box)
    caus_hdr = patches.FancyBboxPatch((9.6, 4.6), 2.8, 0.38, boxstyle="round,pad=0.05,rounding_size=0.08",
                                      facecolor="#ffedd5", edgecolor="#fed7aa", linewidth=1)
    ax.add_patch(caus_hdr)
    ax.text(11.0, 4.79, "CAUSAS RAÍZ", fontsize=9.5, fontweight="bold", color="#c2410c", ha="center", va="center")

    caus_text = (
        "• Monitoreo manual sin telemetría IoT\n"
        "• Información fragmentada entre áreas\n"
        "• Brechas formativas en acopio campesino\n"
        "• Débil infraestructura de logística inversa"
    )
    ax.text(9.7, 4.45, caus_text, fontsize=8.2, color="#1e293b", va="top", linespacing=1.3)

    # Columna Derecha Inferior: Consecuencias
    cons_box = patches.FancyBboxPatch((9.5, 0.95), 3.0, 1.95, boxstyle="round,pad=0.1,rounding_size=0.12",
                                      facecolor="#ffffff", edgecolor="#dc2626", linewidth=1.5)
    ax.add_patch(cons_box)
    cons_hdr = patches.FancyBboxPatch((9.6, 2.45), 2.8, 0.38, boxstyle="round,pad=0.05,rounding_size=0.08",
                                      facecolor="#fee2e2", edgecolor="#fecaca", linewidth=1)
    ax.add_patch(cons_hdr)
    ax.text(11.0, 2.64, "CONSECUENCIAS", fontsize=9.5, fontweight="bold", color="#b91c1c", ha="center", va="center")

    cons_text = (
        "• Pérdidas económicas por devoluciones\n"
        "• Sobrecostos y mayor huella de carbono\n"
        "• Tensión en relaciones con ganaderos\n"
        "• Riesgo de sanciones ambientales"
    )
    ax.text(9.7, 2.3, cons_text, fontsize=8.2, color="#1e293b", va="top", linespacing=1.3)

    # Bloque Inferior: Articulación con ODS
    ods_box = patches.FancyBboxPatch((0.5, 0.4), 8.7, 1.8, boxstyle="round,pad=0.1,rounding_size=0.15",
                                     facecolor="#ecfdf5", edgecolor="#10b981", linewidth=1.8)
    ax.add_patch(ods_box)
    ods_hdr = patches.FancyBboxPatch((0.6, 1.8), 8.5, 0.35, boxstyle="round,pad=0.05,rounding_size=0.08",
                                     facecolor="#d1fae5", edgecolor="#6ee7b7", linewidth=1)
    ax.add_patch(ods_hdr)
    ax.text(4.85, 1.97, "ARTICULACIÓN CON LOS OBJETIVOS DE DESARROLLO SOSTENIBLE (ODS)",
            fontsize=9.5, fontweight="bold", color="#047857", ha="center", va="center")

    ods_text = (
        "• ODS 12: Producción y Consumo Responsables (Meta 12.3: Reducir pérdidas de alimentos en cadenas de suministro;\n"
        "  Meta 12.5: Reducir desechos mediante prevención, reducción, reciclado y reutilización de envases y empaques).\n"
        "• ODS 9: Industria, Innovación e Infraestructura (Meta 9.4: Modernizar infraestructura con tecnologías limpias y racionales)."
    )
    ax.text(0.8, 1.6, ods_text, fontsize=8.4, color="#065f46", va="top", linespacing=1.35)

    # Conectores y flechas visuales
    arrow_props = dict(arrowstyle="->", color="#3b82f6", lw=1.8, mutation_scale=15)
    # De Actores a Centro
    ax.annotate("", xy=(3.8, 5.0), xytext=(3.5, 5.0), arrowprops=arrow_props)
    # De Centro a Síntomas, Causas y Consecuencias
    arrow_red = dict(arrowstyle="->", color="#ef4444", lw=1.8, mutation_scale=15)
    ax.annotate("", xy=(9.5, 6.2), xytext=(9.2, 5.5), arrowprops=arrow_red)
    ax.annotate("", xy=(9.5, 4.1), xytext=(9.2, 4.8), arrowprops=arrow_red)
    ax.annotate("", xy=(9.5, 2.0), xytext=(9.2, 3.8), arrowprops=arrow_red)
    # De Centro a ODS
    arrow_green = dict(arrowstyle="->", color="#10b981", lw=1.8, mutation_scale=15)
    ax.annotate("", xy=(4.85, 2.2), xytext=(4.85, 3.4), arrowprops=arrow_green)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "estadio1_diagrama.png")
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ Generado Estadio 1: {out_path}")


def create_diagram_estadio3():
    fig, ax = plt.subplots(figsize=(14, 8.5), dpi=300)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#f8fafc")

    # Título superior
    title_box = patches.FancyBboxPatch((0.5, 7.6), 13.0, 0.7, boxstyle="round,pad=0.1,rounding_size=0.15",
                                       facecolor="#1e3a8a", edgecolor="#172554", linewidth=1.5)
    ax.add_patch(title_box)
    ax.text(7.0, 8.05, "Estadio 3. Modelo Conceptual del Sistema",
            fontsize=15, fontweight="bold", color="white", ha="center", va="center", fontfamily="sans-serif")
    ax.text(7.0, 7.75, "Derivado de la Definición Raíz | Alpina Productos Alimenticios S.A.S.",
            fontsize=10.5, color="#bfdbfe", ha="center", va="center", fontfamily="sans-serif")

    # Contenedor de Actividades del Sistema (6 pasos en flujo horizontal y bucle)
    steps = [
        {
            "num": "1",
            "title": "MONITOREAR",
            "desc": "Monitorear en tiempo real\nvariables de temperatura\ny calidad fisicoquímica\nen acopio rural y cisternas.",
            "sub": "Subsistema Operacional",
            "x": 0.5, "y": 4.5, "w": 3.8, "h": 2.6,
            "color": "#e0f2fe", "edge": "#0284c7"
        },
        {
            "num": "2",
            "title": "RECEPCIONAR Y VALIDAR",
            "desc": "Validar la inocuidad lechera\nmediante analítica rápida\ny protocolos automatizados\nen plantas procesadoras.",
            "sub": "Subsistema Operacional",
            "x": 5.1, "y": 4.5, "w": 3.8, "h": 2.6,
            "color": "#e0f2fe", "edge": "#0284c7"
        },
        {
            "num": "3",
            "title": "INTEGRAR EN LA NUBE",
            "desc": "Sincronizar telemetría IoT\ncon el sistema ERP/Supply\npara visibilidad total de\ninventarios y rutas frías.",
            "sub": "Subsistema Tecnológico TI",
            "x": 9.7, "y": 4.5, "w": 3.8, "h": 2.6,
            "color": "#fef3c7", "edge": "#d97706"
        },
        {
            "num": "4",
            "title": "DISTRIBUIR CON PRECISIÓN",
            "desc": "Despachar y transportar con\ncontrol térmico continuo hasta\ncanales de comercialización\nminoristas e institucionales.",
            "sub": "Subsistema Logístico",
            "x": 9.7, "y": 1.4, "w": 3.8, "h": 2.6,
            "color": "#fef3c7", "edge": "#d97706"
        },
        {
            "num": "5",
            "title": "GESTIONAR CIRCULARIDAD",
            "desc": "Articular logística inversa de\nempaques posconsumo con\nrecicladores y minoristas para\nrecuperación y reciclaje.",
            "sub": "Subsistema de Sostenibilidad",
            "x": 5.1, "y": 1.4, "w": 3.8, "h": 2.6,
            "color": "#dcfce7", "edge": "#16a34a"
        },
        {
            "num": "6",
            "title": "EVALUAR Y MEJORAR",
            "desc": "Monitorear indicadores de\nmerma, huella de carbono y\nreciclaje; aplicar medidas de\nretroalimentación y ajuste.",
            "sub": "Subsistema de Control / 3 Es",
            "x": 0.5, "y": 1.4, "w": 3.8, "h": 2.6,
            "color": "#fee2e2", "edge": "#dc2626"
        }
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], s["y"]), s["w"], s["h"], boxstyle="round,pad=0.1,rounding_size=0.15",
                                     facecolor=s["color"], edgecolor=s["edge"], linewidth=2.0)
        ax.add_patch(box)
        # Encabezado del paso
        ax.text(s["x"] + s["w"]/2, s["y"] + s["h"] - 0.35, f"ACTIVIDAD {s['num']}: {s['title']}",
                fontsize=9.5, fontweight="bold", color="#0f172a", ha="center", va="center")
        ax.text(s["x"] + s["w"]/2, s["y"] + s["h"] - 0.7, f"[{s['sub']}]",
                fontsize=8.0, color="#475569", ha="center", va="center", style="italic")
        # Descripción
        ax.text(s["x"] + s["w"]/2, s["y"] + 0.85, s["desc"],
                fontsize=8.5, color="#1e293b", ha="center", va="center", multialignment="center", linespacing=1.3)

    # Flechas del flujo principal
    arrow_fwd = dict(arrowstyle="->", color="#0284c7", lw=2.5, mutation_scale=20)
    # 1 -> 2
    ax.annotate("", xy=(5.1, 5.8), xytext=(4.3, 5.8), arrowprops=arrow_fwd)
    # 2 -> 3
    ax.annotate("", xy=(9.7, 5.8), xytext=(8.9, 5.8), arrowprops=arrow_fwd)
    # 3 -> 4
    arrow_down = dict(arrowstyle="->", color="#d97706", lw=2.5, mutation_scale=20)
    ax.annotate("", xy=(11.6, 4.0), xytext=(11.6, 4.5), arrowprops=arrow_down)
    # 4 -> 5
    arrow_left = dict(arrowstyle="->", color="#16a34a", lw=2.5, mutation_scale=20)
    ax.annotate("", xy=(8.9, 2.7), xytext=(9.7, 2.7), arrowprops=arrow_left)
    # 5 -> 6
    arrow_left2 = dict(arrowstyle="->", color="#dc2626", lw=2.5, mutation_scale=20)
    ax.annotate("", xy=(4.3, 2.7), xytext=(5.1, 2.7), arrowprops=arrow_left2)
    # 6 -> 1 (Bucle de retroalimentación)
    arrow_up = dict(arrowstyle="->", color="#dc2626", lw=2.5, mutation_scale=20, linestyle="--")
    ax.annotate("", xy=(2.4, 4.5), xytext=(2.4, 4.0), arrowprops=arrow_up)

    # Banner inferior de control y retroalimentación (3 Es de Peter Checkland)
    eval_box = patches.FancyBboxPatch((0.5, 0.25), 13.0, 0.85, boxstyle="round,pad=0.08,rounding_size=0.12",
                                      facecolor="#1e293b", edgecolor="#0f172a", linewidth=1.2)
    ax.add_patch(eval_box)
    ax.text(7.0, 0.78, "[>>] BUCLE DE CONTROL Y RETROALIMENTACIÓN CONTINUA (Criterios de Evaluación de Peter Checkland)",
            fontsize=9.8, fontweight="bold", color="#38bdf8", ha="center", va="center")
    eval_text = (
        "• EFICACIA: ¿Se logra la trazabilidad total en frío y la recolección circular? | "
        "• EFICIENCIA: ¿Se minimizan pérdidas lecheras y costos logísticos con recursos óptimos?\n"
        "• EFECTIVIDAD: ¿Aporta el sistema a la sostenibilidad de largo plazo (ODS 12) y al bienestar de productores y consumidores?"
    )
    ax.text(7.0, 0.45, eval_text, fontsize=8.2, color="#e2e8f0", ha="center", va="center", multialignment="center")

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "estadio3_modelo_conceptual.png")
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ Generado Estadio 3: {out_path}")


if __name__ == "__main__":
    create_diagram_estadio1()
    create_diagram_estadio3()
