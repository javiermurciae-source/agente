# Guía de Branding y Extracción de Identidad

Toda presentación construida con esta skill debe incorporar la identidad visual auténtica del proyecto, la marca o la plantilla de referencia.

---

## 1. Procedimiento de Inspección y Extracción

Cuando el usuario mencione una marca, una URL o apunte a una plantilla:

1. **Inspección de Plantillas Locales (`plantillas/presentaciones/`)**:
   - Si existe un archivo `.pptx` o `.pdf` en `plantillas/presentaciones/`:
     - Inspeccionar su estructura interna (XML de colores, tipografías y geometría).
     - Extraer su paleta exacta de colores primarios, secundarios y acentos.
     - Identificar las tipografías correspondientes en Google Fonts.
     - Adoptar sus arquetipos característicos (ej. curvas *racetrack*, tablas Gantt, matrices 2x2, listas verticales de nodos).

2. **Inspección de Páginas Web en Vivo**:
   - Si se da una URL (ej. `https://marca.com`), leer el HTML y hojas de estilo.
   - Extraer variables `--primary`, `--accent`, `--bg`, tipografías y logos.

3. **Fallbacks Oficiales de Alta Gama**:
   - Si no hay URL ni plantilla específica, utilizar una de las 5 paletas maestras siguientes.

---

## 2. Paletas Maestras Oficiales

### Paleta A: Canva Corporate Slate Blue (Dual-Tone Master)
- **Concepto**: Presentaciones corporativas de alta dirección, propuestas de negocio, consultoría e investigación histórica. Contraste arquitectónico dual-tone (Navy institucional + paneles de datos en blanco puro).
- **`--navy`**: `#132232` (Azul marino profundo corporativo)
- **`--navy-deep`**: `#0C1722` (Sombra y sidebars)
- **`--slate`**: `#5B696F` (Gris pizarra para curvas y elementos secundarios)
- **`--ice-blue`**: `#ADC7EA` (Azul hielo para acentos, píldoras y bloques de progreso)
- **`--petrol`**: `#006D72` (Verde petróleo para fases intermedias)
- **`--white`**: `#FFFFFF` (Fondo nítido para cuadrículas, tablas y procesos)
- **`--dark-text`**: `#111827` (Texto principal en paneles blancos)
- **`--dark-muted`**: `#4B5563` (Texto secundario en paneles blancos)
- **`--border-gray`**: `#E0E6E9` (Líneas divisorias sutiles)
- **`--font-display`**: `'Oswald', sans-serif` (Mayúsculas condensadas imponentes)
- **`--font-body`**: `'Plus Jakarta Sans', sans-serif` o `'Glacial Indifference'`

---

### Paleta B: ProductByTom Amber Gold (Dark Tech Predeterminada)
- **Concepto**: Estética premium, producto digital, autoridad y calidez de alto contraste.
- **`--bg`**: `#070707` (Negro carbón profundo)
- **`--bg-card`**: `#0F0F0F` (Superficie secundaria)
- **`--bg-card-hover`**: `#161616`
- **`--border`**: `rgba(255, 255, 255, 0.08)`
- **`--border-accent`**: `rgba(255, 184, 0, 0.25)`
- **`--accent`**: `#FFB800` (Oro ámbar brillante)
- **`--text`**: `#F4F1EA` (Blanco marfil cálido)
- **`--text-muted`**: `rgba(244, 241, 234, 0.60)`
- **`--font-display`**: `'Space Grotesk', sans-serif`
- **`--font-mono`**: `'JetBrains Mono', monospace`

---

### Paleta C: Vercel / Electric Cyan
- **Concepto**: Infraestructura, herramientas de desarrollo, SaaS de velocidad extrema.
- **`--bg`**: `#000000`
- **`--bg-card`**: `#0A0A0A`
- **`--border`**: `rgba(255, 255, 255, 0.12)`
- **`--accent`**: `#0070F3` (Azul eléctrico) / `#00DFD8` (Cian láser)
- **`--text`**: `#EDEDED`
- **`--text-muted`**: `#888888`
- **`--font-display`**: `'Inter', sans-serif`
- **`--font-mono`**: `'JetBrains Mono', monospace`

---

### Paleta D: Antigravity AI Violet
- **Concepto**: Inteligencia artificial, modelos de lenguaje, investigación avanzada.
- **`--bg`**: `#08080C`
- **`--bg-card`**: `#111118`
- **`--border`**: `rgba(255, 255, 255, 0.08)`
- **`--accent`**: `#8B5CF6` (Púrpura neón)
- **`--text`**: `#F8FAFC`
- **`--text-muted`**: `#94A3B8`
- **`--font-display`**: `'Space Grotesk', sans-serif`
- **`--font-mono`**: `'JetBrains Mono', monospace`

---

### Paleta E: Cyber Emerald / Growth
- **Concepto**: Finanzas, ciberseguridad, métricas operativas y retorno de inversión.
- **`--bg`**: `#040806`
- **`--bg-card`**: `#0B140F`
- **`--border`**: `rgba(16, 185, 129, 0.15)`
- **`--accent`**: `#10B981` (Verde esmeralda vibrante)
- **`--text`**: `#ECFDF5`
- **`--text-muted`**: `#6EE7B7`
- **`--font-display`**: `'Space Grotesk', sans-serif`
- **`--font-mono`**: `'JetBrains Mono', monospace`
