#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de firmas manuscritas realistas con fondo blanco puro.
1. Firma de Kevin Mitnick (Consultor de Ciberseguridad / SOC)
2. Firma de Gerente inventado: Ing. Roberto M. Gómez V. (Gerente de Operaciones y Proyectos)
"""

import math
import numpy as np
from PIL import Image, ImageDraw

def bezier_point(p0, p1, p2, p3, t):
    """Calcula un punto en una curva de Bézier cúbica."""
    u = 1.0 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t
    x = uuu * p0[0] + 3 * uu * t * p1[0] + 3 * u * tt * p2[0] + ttt * p3[0]
    y = uuu * p0[1] + 3 * uu * t * p1[1] + 3 * u * tt * p2[1] + ttt * p3[1]
    return (x, y)

def draw_bezier_stroke(draw, p0, p1, p2, p3, color, base_width=6, n_points=80):
    """Dibuja un trazo de Bézier simulando la presión variable de una pluma estilográfica."""
    points = [bezier_point(p0, p1, p2, p3, t) for t in np.linspace(0, 1, n_points)]
    for i in range(len(points) - 1):
        pt1 = points[i]
        pt2 = points[i+1]
        progress = i / float(len(points))
        # Variación de presión: más ancho en el centro, más fino en los extremos
        pressure = math.sin(progress * math.pi) * 0.5 + 0.75
        w = max(2, int(base_width * pressure))
        draw.line([pt1, pt2], fill=color, width=w)

def generate_kevin_mitnick_signature(output_path="firma_kevin_mitnick.png"):
    # Renderizamos a 4x (2400x960) para supersampling y reducción a 600x240
    scale = 4
    w, h = 600 * scale, 240 * scale
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    ink = (12, 35, 68)  # Azul noche estilográfica

    # Trazos para 'K'
    draw_bezier_stroke(draw, (80*scale, 160*scale), (85*scale, 60*scale), (95*scale, 40*scale), (105*scale, 185*scale), ink, 9*scale)
    draw_bezier_stroke(draw, (180*scale, 65*scale), (120*scale, 100*scale), (100*scale, 115*scale), (125*scale, 110*scale), ink, 8*scale)
    draw_bezier_stroke(draw, (120*scale, 110*scale), (150*scale, 130*scale), (185*scale, 175*scale), (210*scale, 180*scale), ink, 8*scale)

    # Bucle 'e-v-i-n'
    draw_bezier_stroke(draw, (200*scale, 140*scale), (220*scale, 105*scale), (240*scale, 160*scale), (255*scale, 125*scale), ink, 7*scale)
    draw_bezier_stroke(draw, (255*scale, 125*scale), (270*scale, 155*scale), (285*scale, 120*scale), (300*scale, 150*scale), ink, 7*scale)
    draw_bezier_stroke(draw, (300*scale, 150*scale), (315*scale, 115*scale), (330*scale, 150*scale), (345*scale, 125*scale), ink, 7*scale)

    # Letra 'M' mayúscula de Mitnick
    draw_bezier_stroke(draw, (340*scale, 170*scale), (350*scale, 50*scale), (365*scale, 45*scale), (380*scale, 165*scale), ink, 9*scale)
    draw_bezier_stroke(draw, (380*scale, 165*scale), (395*scale, 65*scale), (410*scale, 60*scale), (425*scale, 165*scale), ink, 8*scale)

    # Trazos fluidos 'i-t-n-i-c-k'
    draw_bezier_stroke(draw, (425*scale, 165*scale), (440*scale, 120*scale), (455*scale, 160*scale), (475*scale, 125*scale), ink, 7*scale)
    draw_bezier_stroke(draw, (475*scale, 125*scale), (490*scale, 70*scale), (505*scale, 70*scale), (510*scale, 160*scale), ink, 7*scale)  # 't'
    draw_bezier_stroke(draw, (510*scale, 160*scale), (525*scale, 130*scale), (540*scale, 165*scale), (560*scale, 120*scale), ink, 7*scale)

    # Barra de la 't'
    draw_bezier_stroke(draw, (475*scale, 95*scale), (495*scale, 90*scale), (515*scale, 92*scale), (530*scale, 88*scale), ink, 6*scale)

    # Rúbrica inferior / subrayado estilizado
    draw_bezier_stroke(draw, (90*scale, 200*scale), (220*scale, 190*scale), (420*scale, 185*scale), (560*scale, 175*scale), ink, 8*scale)
    draw_bezier_stroke(draw, (560*scale, 175*scale), (575*scale, 170*scale), (550*scale, 195*scale), (510*scale, 205*scale), ink, 6*scale)

    # Redimensionar a alta calidad con ANTIALIAS
    img = img.resize((600, 240), Image.Resampling.LANCZOS)
    img.save(output_path, "PNG", optimize=True)
    print(f"Firma Kevin Mitnick guardada en: {output_path}")

def generate_gerente_signature(output_path="firma_gerente.png"):
    # Renderizamos a 4x (2400x960) para supersampling
    scale = 4
    w, h = 600 * scale, 240 * scale
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    ink = (16, 28, 48)  # Azul oscuro corporativo

    # Firma ejecutiva: Ing. Roberto M. Gómez V.
    # Gran lazada inicial 'R'
    draw_bezier_stroke(draw, (110*scale, 190*scale), (90*scale, 90*scale), (80*scale, 45*scale), (120*scale, 40*scale), ink, 10*scale)
    draw_bezier_stroke(draw, (120*scale, 40*scale), (180*scale, 42*scale), (190*scale, 110*scale), (135*scale, 115*scale), ink, 9*scale)
    draw_bezier_stroke(draw, (135*scale, 115*scale), (160*scale, 130*scale), (200*scale, 180*scale), (225*scale, 190*scale), ink, 9*scale)

    # Bucle medio 'o-b-e-r-t'
    draw_bezier_stroke(draw, (215*scale, 160*scale), (230*scale, 110*scale), (245*scale, 170*scale), (265*scale, 135*scale), ink, 7*scale)
    draw_bezier_stroke(draw, (265*scale, 135*scale), (280*scale, 60*scale), (300*scale, 140*scale), (315*scale, 150*scale), ink, 8*scale)

    # 'Gómez' estilizado con lazo ascendente y descendente
    draw_bezier_stroke(draw, (320*scale, 140*scale), (345*scale, 80*scale), (370*scale, 75*scale), (360*scale, 150*scale), ink, 9*scale)
    draw_bezier_stroke(draw, (360*scale, 150*scale), (340*scale, 215*scale), (375*scale, 220*scale), (400*scale, 140*scale), ink, 8*scale)

    # Letras finales rápidas
    draw_bezier_stroke(draw, (400*scale, 140*scale), (420*scale, 120*scale), (440*scale, 160*scale), (460*scale, 130*scale), ink, 7*scale)
    draw_bezier_stroke(draw, (460*scale, 130*scale), (480*scale, 110*scale), (500*scale, 155*scale), (530*scale, 120*scale), ink, 7*scale)

    # Rúbrica envolvente inferior con bucle y punto final
    draw_bezier_stroke(draw, (70*scale, 160*scale), (180*scale, 215*scale), (380*scale, 210*scale), (540*scale, 190*scale), ink, 9*scale)
    draw_bezier_stroke(draw, (540*scale, 190*scale), (570*scale, 185*scale), (545*scale, 205*scale), (480*scale, 215*scale), ink, 7*scale)

    # Punto final ejecutivo
    draw.ellipse([(555*scale, 195*scale), (565*scale, 205*scale)], fill=ink)

    img = img.resize((600, 240), Image.Resampling.LANCZOS)
    img.save(output_path, "PNG", optimize=True)
    print(f"Firma Gerente guardada en: {output_path}")

if __name__ == "__main__":
    generate_kevin_mitnick_signature("scripts/firma_kevin_mitnick.png")
    generate_gerente_signature("scripts/firma_gerente.png")
