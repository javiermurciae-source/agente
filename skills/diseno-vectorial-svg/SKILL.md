---
name: diseno-vectorial-svg
description: Procedimiento y renderizado para crear gráficos corporativos, anuncios y banners en SVG y rasterizarlos a PNG en alta definición. Utilizar cuando se solicite crear piezas visuales, anuncios de Stream Zone, banners o infografías vectoriales.
---

# Skill: Diseño Vectorial SVG y Renderizado a Imagen

Procedimiento paso a paso para crear gráficos corporativos, anuncios y banners en SVG y rasterizarlos a PNG en alta definición.

---

## 🎯 Objetivo
Producir piezas visuales nítidas para anuncios de Stream Zone, listas de precios o infografías sin requerir software de diseño gráfico manual.

---

## ⚙️ Procedimiento Paso a Paso

### 1. Creación del Gráfico Vectorial
- Crear un archivo `.svg` dentro de la subcarpeta del proyecto:
  `proyectos/<encargo>/grafico.svg`
- Utilizar paleta de colores corporativos (azules oscuros, cian, blancos y detalles vibrantes).
- Definir tipografías limpias (`sans-serif`, `system-ui`) y coordenadas proporcionales (`viewBox="0 0 1080 1080"` para cuadrado o `1920 1080` para panorámico).

### 2. Rasterizado Nítido con ImageMagick
- Ejecutar la conversión a PNG con densidad de 300 DPI:
  ```bash
  magick -density 300 proyectos/<encargo>/grafico.svg proyectos/<encargo>/grafico.png
  ```

### 3. Validación y Entrega
- Verificar que el PNG generado tenga colores vivos, legibilidad en los textos y contraste adecuado.
- Guardar la versión final en la carpeta del proyecto para su posterior difusión.
