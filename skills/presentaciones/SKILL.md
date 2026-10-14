---
name: presentaciones
description: Procedimiento y motor de construcción para generar presentaciones HTML interactivas y autocontenidas con el branding de tu marca (estándar ProductByTom y plantillas corporativas Canva). Utilizar siempre que se solicite crear presentaciones, diapositivas, slides, decks de producto, pitch decks, propuestas de negocio o storyboards interactivos en HTML con scroll-snap, animaciones escalonadas, tipografía clamp() y alto contraste (Dark Tech o Dual-Tone corporativo).
---

# Constructor de Presentaciones (ProductByTom & Canva Master)

Esta skill genera un **único archivo HTML de presentación autocontenido** combinando la interactividad fluida de ProductByTom (100vh scroll-snap, animaciones por `IntersectionObserver`, barra de progreso) con la apropiación estética de plantillas maestras corporativas (Canva Pro / PPTX / Brand Kits).

---

## 📂 Directorio de Plantillas Maestras
Las plantillas de referencia residen en:
```text
plantillas/presentaciones/
```
- Cuando el usuario solicite una presentación basada en una plantilla o estilo de negocio, inspeccioná de inmediato los archivos en `plantillas/presentaciones/` (archivos `.pptx`, `.pdf` o `.html`).
- **Apropiación del diseño**: Extraé y adoptá los colores hexadecimales reales, tipografías, geometría decorativa (pills, curvas, líneas con punto) y arquetipos modulares de la plantilla, en lugar de forzar una sola plantilla genérica.
- Las presentaciones generadas se compilan en:
  ```text
  vault/presentaciones/<nombre-tema>.html
  ```

---

## 🚀 Flujo de Trabajo

1. **Recopilá el contenido y la intención visual**:
   - Confirmá el tema, audiencia y cantidad aproximada de slides.
   - Detectá el estilo visual deseado:
     - **Modo Dark-Tech (ProductByTom)**: Fondo 100% oscuro (`#070707`), tarjetas capa 2, acento neón/ámbar/violeta.
     - **Modo Dual-Tone Corporate (Canva)**: Fondos mixtos de alto contraste (portadas, índices y divisores en azul marino profundo `#132232`; procesos, cuadrículas 2x2, comparativas y tablas en blanco nítido `#FFFFFF`).
     - **Plantilla Personalizada**: Si hay un archivo en `plantillas/presentaciones/`, leé sus activos y cloná su ADN.

2. **Extraé el branding o ADN de la plantilla**:
   - Si se da una URL: inspeccionala en vivo (`read_url_content`) para extraer paleta y tipografía.
   - Si se da o existe una plantilla en `plantillas/presentaciones/`: usá sus valores exactos documentados en [`references/branding.md`](./references/branding.md).
   - Fallback oficial: seleccioná la paleta que mejor calce con el tono del encargo.

3. **Planificá la estructura con Arquetipos Modulares**:
   - **Una sola idea por slide**.
   - Mapeá el contenido seleccionando del catálogo de arquetipos:
     - *Hero / Portada* (Dark Tech o Canva Racetrack Pills + Dot Lines).
     - *Índice / Agenda* (Línea vertical continua con nodos `o---o---o`).
     - *Divisor de Sección* (Cifra gigante + titulares en Oswald).
     - *Proceso Horizontal en Fases* (Dual-tone: header oscuro + 4 pasos sobre blanco).
     - *Matriz 2x2* (Dual-tone: sidebar lateral oscuro 35vw + 4 celdas sobre blanco 65vw).
     - *Comparativa 4 Columnas Hairline* (Grid limpio separado por líneas finas).
     - *Lista de KPIs Numerados* (Nodos circulares sólidos `1, 2, 3, 4` en vertical).
     - *Cronograma Gantt Matricial* (Tabla de fases temporales con bloques de avance en color).
     - *Bento Grid Asimétrico* o *Big Stats* (Cifras gigantes con contexto).
     - *Cierre / CTA / Badge Tipográfico*.

4. **Escribí el HTML**:
   - Seguí cada regla de [`references/output-rules.md`](./references/output-rules.md) y [`references/slide-template.md`](./references/slide-template.md).
   - El archivo debe ser 100% autocontenido (CSS + JS inline, Google Fonts como única dependencia externa).

5. **Guardá y abrí el entregable**:
   - Guardalo en `vault/presentaciones/<tema>.html`.
   - Entregá el enlace directo y ofrece abrirlo de inmediato con `setsid -f xdg-open ...`.

---

## 🎨 Modos de Diseño y Branding

1. **Apropiación Flexible del Diseño**:
   - Prohibido encasillarse en una sola estética cuando el proyecto pide la identidad de una plantilla específica.
   - Si la plantilla usa contrastes dual-tone (fondos navy combinados con áreas de datos en blanco puro), **replicalo con fidelidad milimétrica**. El contraste blanco/oscuro bien estructurado aporta sofisticación corporativa.

2. **Tipografías recomendadas por modo**:
   - **Canva Corporate**: `Oswald` (display mayúsculas condensado) + `Plus Jakarta Sans` / `Glacial Indifference` (cuerpo).
   - **ProductByTom Dark**: `Space Grotesk` (display) + `JetBrains Mono` / `Inter` (cuerpo).

Consultá [`references/branding.md`](./references/branding.md) para detalles completos de paletas.

---

## 🛑 Reglas de Output (No Negociables)

- **Un único archivo HTML autocontenido**, con todo el CSS y JS inline.
- **Sin dependencias externas** excepto Google Fonts.
- **Todos los tamaños de fuente usan `clamp()`** para escalado responsive matemático.
- **Cada slide ocupa exactamente `100vh`**, sin scroll dentro de un slide.
- **Una idea por slide**, máximo 5–6 bullets o bloques concisos.
- **Animaciones sutiles de entrada escalonadas (*staggered*)** para elementos hijos (`.animate-item`).
- **`scroll-snap` vertical** obligatorio entre slides.
- **Navegación completa**: Flechas de teclado (`↑`, `↓`, `←`, `→`), barra espaciadora, `PageUp`/`PageDown` y touch/swipe. Tecla `F` para pantalla completa.
- **Barra de progreso** inferior con indicador numérico (`X / N`).
- **Respeto estricto por `prefers-reduced-motion`**.
- **Slide de título fuerte al inicio, cierre/CTA claro al final**.
- **Divisores de sección** entre los bloques temáticos.

---

## 📐 Plantilla y Arquetipos
[`references/slide-template.md`](./references/slide-template.md) contiene el esqueleto base y el catálogo completo de arquetipos modulares listos para copiar y combinar.

---

## ❌ Errores Comunes a Evitar
- **No ignores la plantilla de referencia**: Si el usuario entrega o apunta a una plantilla en `plantillas/presentaciones/`, cloná sus componentes característicos (Gantt, splits, nodos, etc.).
- **No generes scroll vertical interno en ningún slide**: Si un diagrama o tabla es grande, ajustá sus márgenes con `clamp()` o dividilo en dos slides.
- **No uses bibliotecas externas pesadas** (Tailwind CDN, Bootstrap, jQuery). Todo debe ser CSS y JavaScript puro inline.
