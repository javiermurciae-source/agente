---
name: pizarra-animada
description: >-
  Generación programática de animaciones de pizarra blanca (Whiteboard Animation / Hand-Drawn)
  didácticas y explicativas con trazo a mano alzada auténtico, fórmulas matemáticas, diagramas
  y locución sincronizada. Utilizar cuando se solicite crear videos de pizarra, animaciones
  dibujadas a mano, clases explicativas estilo profesor, diagramas animados o tutoriales técnicos
  con handanim (Python/Cairo) o sketchling (Node/Rough.js).
---

# Skill: Pizarra Animada (Whiteboard Animation Engine)

Esta habilidad proporciona el entorno, los flujos de trabajo y las herramientas programáticas para generar videos educativos y didácticos de pizarra blanca con estética de dibujo a mano alzada auténtica (*single-stroke Hershey fonts*, cajas con temblor de marcador, diagramas de flujo, tablas y locución sincronizada).

---

## 🎯 1. Objetivo y Disparadores

### ¿Cuándo usar esta Skill?
- Peticiones de **"video de pizarra"**, **"whiteboard animation"** o **"animación dibujada a mano"**.
- Explicaciones de conceptos técnicos complejos (redes, matemáticas, algoritmos, arquitectura de software, física) con estilo didáctico de profesor.
- Creación de diagramas animados que se dibujan progresivamente al compás de una narración.
- Automatización programática de lecciones en video sin herramientas de pago privativas (VideoScribe/Doodly).

### Motores Soportados:
1. **`handanim` (Recomendado para clases y matemáticas)**:
   - Motor en Python (`.venv-handanim/bin/python`).
   - Usa fuentes monolínea de Hershey (`FeasiblySingleLine`, `Headstay`), renderizado ultra-nítido con PyCairo y fórmulas TeX nativas.
   - Ideal para tablas alineadas, diagramas técnicos, matemáticas y lecciones con múltiples bloques.
2. **`sketchling` (Recomendado para animaciones web y estilo bosquejo libre)**:
   - Motor en Node.js / TypeScript (`npx -y sketchling`).
   - Basado en Rough.js y GSAP con renderizado sin cabeza vía Playwright Chromium.
   - Ideal para ilustraciones sueltas, loops orgánicos y staggers cinéticos.

---

## 📋 2. Reglas Inquebrantables y Estándares de Producción

1. **Resolución y Frame Rate Estándar**:
   - Resolución: 1920 × 1080 (Full HD horizontal 16:9).
   - FPS: 24 fps para dibujo de pizarra (sensación natural de animación) o 30 fps.
2. **Paleta de Marcadores de Pizarra**:
   - Fondo: Blanco cálido o marfil suave (`#fafaf8` o RGB `(0.98, 0.98, 0.96)`).
   - Marcador principal: Azul pizarra (`(0.08, 0.35, 0.75)`) o Negro grafito (`(0.12, 0.14, 0.18)`).
   - Marcador de cálculo/fórmulas: Verde bosque (`(0.05, 0.52, 0.22)`).
   - Marcador de énfasis/alerta: Rojo carmín (`(0.82, 0.12, 0.15)`).
   - Marcador de reglas de oro: Ocre/Dorado (`(0.75, 0.48, 0.05)`).
3. **Sincronización Didáctica Audio-Trazo**:
   - Generar primero la locución (usando el motor local de Kokoro TTS) y obtener las marcas de tiempo exactas (`timeline.json`).
   - Ajustar los `start_time` y `duration` de los elementos visuales para que el trazo coincida con la mención hablada.
4. **Efectos de Sonido Sutiles (SFX)**:
   - Añadir toques sonoros sutiles en momentos clave (chime suave en el título, click suave al trazar cajas, whoosh sutil en flechas conectoras).

---

## ⚙️ 3. Flujo de Trabajo Maestro (Paso a Paso)

```
[1. Guion Didáctico] ──> [2. Locución Kokoro TTS] ──> [3. Mapa de Tiempos] ──> [4. Composición Handanim/Sketchling] ──> [5. Snapshot de Validación] ──> [6. Render & Mux MP4]
```

### Paso 1: Generar la Locución y Mapa de Tiempos
Escribir el guion dividido en secciones (Introducción, Planteamiento, Cálculo/Desarrollo, Tabla/Diagrama, Conclusión).
Sintetizar el audio con Kokoro TTS (`em_alex` o `ef_dora`):

```bash
.venv-handanim/bin/python /home/rootkit/agente/skills/pizarra-animada/scripts/synthesize_speech.py \
  --text "Texto didáctico de la clase" \
  --voice em_alex \
  --output audio_seccion.wav
```

### Paso 2: Diseñar la Escena en Python (`handanim`)
Crear el archivo de escena importando los primitivos necesarios:

```python
from handanim import (
    Scene, Text, RoundedRectangle, Line, Arrow, Table,
    SketchAnimation, StrokeStyle, FillStyle
)

scene = Scene(width=1920, height=1080, fps=24, background_color=(0.98, 0.98, 0.96))

# Título
title = Text("TITULO DE LA LECCION", (330, 50), font_size=32)
scene.add(SketchAnimation(start_time=0.5, duration=1.8), title)

# Caja de contenido
box = RoundedRectangle((100, 135), 560, 250, border_radius=0.06, stroke_style=StrokeStyle(color=(0.08, 0.35, 0.75), width=3))
scene.add(SketchAnimation(start_time=3.5, duration=1.5), box)
```

### Paso 3: Validación Visual Inmediata con Snapshot (Ahorro de Tokens y Tiempo)
Antes de renderizar el video completo, renderizar un snapshot en SVG/PNG para verificar composición y legibilidad:

```python
scene.render_snapshot("snap_preview.png", frame_in_seconds=total_seconds)
```
Convertir y previsualizar con `resvg snap_preview.png snap_preview.png` y revisar con `view_file`.

### Paso 4: Renderizado de Video y Muxing con Audio
Renderizar los fotogramas y combinar con el audio maestro vía FFmpeg:

```bash
# Render de video raw
.venv-handanim/bin/python render_script.py

# Mux con audio sincronizado y compresión óptima
ffmpeg -y -i raw_video.mp4 -i master_audio.wav \
  -c:v libx264 -preset fast -crf 18 -vf "scale=1920:1080" \
  -c:a aac -b:a 192k -shortest output_final_1080p.mp4
```

---

## 🛠️ 4. Herramientas y Scripts del Entorno

- **Entorno Virtual**: `/home/rootkit/agente/.venv-handanim/bin/python` (con handanim, pycairo, kokoro-onnx, soundfile).
- **Tipografías Hershey**: Instaladas y enlazadas en `.venv-handanim/fonts/` (FeasiblySingleLine, HeadstayRegular).
- **Modelos Kokoro TTS**: En `/home/rootkit/.cache/hyperframes/tts/models/kokoro-v1.0.onnx`.
- **Plantilla de referencia**: [`examples/template_clase_pizarra.py`](./examples/template_clase_pizarra.py).
- **Cheatsheet de Primitivos**: [`references/handanim_cheatsheet.md`](./references/handanim_cheatsheet.md).

---

## ✅ 5. Verificación de Éxito

Un video de pizarra animada se considera exitoso cuando:
1. `ffprobe` confirma resolución 1920×1080, framerate constante (24 o 30 fps) y pista de audio AAC.
2. Cada elemento visual aparece y se dibuja exactamente cuando la voz lo menciona.
3. El trazo simula fielmente la escritura de un marcador sobre pizarra sin artefactos de render.
4. Los textos respetan la jerarquía visual y la regla de oro destaca claramente al final.
