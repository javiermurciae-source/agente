# Referencia Rápida de Handanim (Python)

Guía técnica de primitivos, parámetros y animaciones de `handanim` para construcción de pizarras interactivas.

---

## 🎨 Primitivos y Geometría

### 1. `Scene`
```python
scene = Scene(
    width=1920,
    height=1080,
    fps=24,
    background_color=(0.98, 0.98, 0.96) # Marfil pizarra
)
```

### 2. `Text`
Utiliza fuentes Hershey de trazo simple (renderizadas como un único trazo de pluma continuo, no como tipografías de contorno):
```python
title = Text(
    "TITULO EN MAYUSCULAS",
    (x, y),
    font_size=28,
    stroke_style=StrokeStyle(color=(0.12, 0.14, 0.18), width=3)
)
```

### 3. `RoundedRectangle`
Caja con esquinas redondeadas y temblor orgánico de mano alzada:
```python
box = RoundedRectangle(
    (x, y),
    width,
    height,
    border_radius=0.06,  # Fracción de redondeo (0.0 a 1.0)
    stroke_style=StrokeStyle(color=(0.08, 0.35, 0.75), width=3)
)
```

### 4. `Line` y `Arrow`
```python
divider = Line((x1, y1), (x2, y2), stroke_style=StrokeStyle(color=(0.82, 0.12, 0.15), width=3))
arrow = Arrow((x1, y1), (x2, y2), stroke_style=StrokeStyle(color=(0.82, 0.12, 0.15), width=3.5))
```

### 5. `Table`
```python
from handanim import Table, SketchAnimation

tbl = Table(
    (x, y),
    n_rows=5,
    n_cols=4,
    cell_width=350,
    cell_height=60,
    headers=["COL 1", "COL 2", "COL 3", "COL 4"],
    data=[["A1", "B1", "C1", "D1"], ...],
    cell_font_size=18,
    header_font_size=20
)
reveal = tbl.animate_by_row(SketchAnimation, start_time=10.0, total_duration=8.0)
reveal.add_to_scene(scene)
```

---

## ⏱️ Animaciones Disponibles

- `SketchAnimation(start_time=1.0, duration=2.0)`: Dibuja el objeto progresivamente como un trazo a mano.
- `FadeInAnimation(start_time=1.0, duration=1.0)`: Aparición suave.
- `TranslateFromAnimation(start_time=1.0, duration=1.0, data={"offset": (0, 50)})`: Desplazamiento desde un punto.
- `CameraAnimation(start_time=5.0, duration=2.0, data={"to_xrange": (0, 1920), "to_yrange": (0, 1080)})`: Paneo y zoom de cámara.

---

## 🖼️ Validación Rápida con Snapshots

Para no perder tiempo renderizando miles de fotogramas mientras se ajusta el diseño:
```python
scene.render_snapshot("snap.png", frame_in_seconds=25.0)
```
Convierte el SVG resultante a PNG con:
```bash
resvg snap.png snap_raster.png
```
