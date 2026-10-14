#!/usr/bin/env python3
"""
Plantilla Maestra para creación de videos explicativos estilo Pizarra Animada (Whiteboard Animation).
Ejecutar con el entorno virtual del agente:
    .venv-handanim/bin/python template_clase_pizarra.py
"""

from handanim import (
    Scene, Text, RoundedRectangle, Line, Arrow,
    SketchAnimation, StrokeStyle
)

def create_scene():
    scene = Scene(width=1920, height=1080, fps=24, background_color=(0.98, 0.98, 0.96))

    # Paleta de color
    C_DARK = (0.12, 0.14, 0.18)      # Negro pizarra
    C_BLUE = (0.08, 0.35, 0.75)      # Azul técnico
    C_GREEN = (0.05, 0.52, 0.22)     # Verde cálculo
    C_RED = (0.82, 0.12, 0.15)       # Rojo énfasis
    C_GOLD = (0.75, 0.48, 0.05)      # Dorado regla

    # 1. Encabezado
    title = Text("TITULO DE LA LECCION DIDACTICA", (360, 55), font_size=32, stroke_style=StrokeStyle(color=C_DARK, width=3))
    scene.add(SketchAnimation(start_time=0.5, duration=1.5), title)

    sub = Text("Subtitulo explicativo o resumen del tema a abordar", (480, 95), font_size=19, stroke_style=StrokeStyle(color=(0.4, 0.4, 0.4), width=2))
    scene.add(SketchAnimation(start_time=1.2, duration=1.0), sub)

    div = Line((100, 125), (1820, 125), stroke_style=StrokeStyle(color=C_RED, width=3))
    scene.add(SketchAnimation(start_time=1.8, duration=0.8), div)

    # 2. Bloque 1: Problema o Caso Base
    box1 = RoundedRectangle((100, 150), 540, 240, border_radius=0.06, stroke_style=StrokeStyle(color=C_BLUE, width=3))
    scene.add(SketchAnimation(start_time=2.5, duration=1.2), box1)

    t1 = Text("1. SITUACION INICIAL", (130, 190), font_size=23, stroke_style=StrokeStyle(color=C_BLUE, width=3))
    scene.add(SketchAnimation(start_time=3.0, duration=0.8), t1)

    # 3. Flecha conectora
    arr = Arrow((650, 270), (730, 270), stroke_style=StrokeStyle(color=C_RED, width=3.5))
    scene.add(SketchAnimation(start_time=4.5, duration=0.6), arr)

    # 4. Bloque 2: Solución o Fórmula
    box2 = RoundedRectangle((740, 150), 1080, 240, border_radius=0.06, stroke_style=StrokeStyle(color=C_GREEN, width=3))
    scene.add(SketchAnimation(start_time=5.0, duration=1.5), box2)

    t2 = Text("2. PROCEDIMIENTO Y CALCULO", (770, 190), font_size=23, stroke_style=StrokeStyle(color=C_GREEN, width=3))
    scene.add(SketchAnimation(start_time=5.5, duration=0.8), t2)

    return scene

if __name__ == "__main__":
    scene = create_scene()
    scene.render_snapshot("preview.png", frame_in_seconds=8.0)
    print("Snapshot generado en preview.png")
