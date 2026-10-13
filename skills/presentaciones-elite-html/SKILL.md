---
name: presentaciones-elite-html
description: >-
  Metodología, motor de compilación y plantilla exacta para crear presentaciones interactivas de nivel profesional en HTML único (16:9).
  Utilizar siempre que se solicite crear diapositivas, presentaciones, decks, pitch decks o storyboards de video,
  garantizando navegación fluida por teclado, barra de progreso superior, área segura para cámara y diseño visual estilo Apple, Notion, Dark Tech o Neo-Brutalist.
---

# Skill: Presentaciones y Decks HTML de Élite (16:9)

Esta habilidad proporciona el estándar de ingeniería y la **plantilla exacta de producción** para generar mazos de diapositivas interactivas en un único archivo web (`index.html`), optimizadas para proyección, defensas de proyectos, pitch decks y grabación de video/streaming.

---

## 🎯 1. Objetivo y Disparadores Operativos

- **Problema que resuelve**: Elimina la rigidez y el slop de herramientas convencionales (PowerPoint pesado, PDFs estáticos, textos deformados de generadores de imagen de baja fidelidad).
- **Cuándo activar**:
  - Cuando el usuario pida: *"hazme unas diapositivas"*, *"crea una presentación"*, *"un pitch deck sobre X"*, *"slides para video explicativo"*, o *"un mazo de diapositivas en HTML"*.

---

## 📋 2. Reglas Inquebrantables de Diseño

1. **Lienzo Determinista 16:9 (1920×1080)**: Todo el mazo se renderiza en relación de aspecto 16:9 perfecta, con auto-escalado proporcional (`Math.min`) para encajar en cualquier resolución sin barras de desplazamiento.
2. **Archivo Único Autocontenido (`index.html`)**: HTML, CSS, JavaScript y tipografías empaquetados en un solo archivo independiente sin servidores backend requeridos.
3. **Navegación Fluida Multi-Modal**:
   - Teclado: `→` / `Espacio` (avanzar), `←` / `Backspace` (retroceder), `F` (pantalla completa), `C` (zona de cámara), `T` (cambiar tema).
   - Táctil: Swipe horizontal para tablets o móviles.
   - Controles flotantes con desvanecimiento automático tras inactividad.
4. **Zona Segura para Cámara (*Talking Head Safety Zone*)**:
   - Espacio reservado de 320×220px en la esquina inferior derecha para que el rostro del presentador en OBS / cámara web nunca tape textos o datos esenciales.

---

## 🏛️ 3. Estructura Narrativa de los 8 Bloques Clave

Toda presentación de alto impacto debe estructurarse siguiendo este orden:

| Slide | Tipo | Propósito | Elementos Clave |
| :---: | :--- | :--- | :--- |
| **01** | **Hero / Hook** | Capturar atención en los primeros 5 segundos | Titular display gigante, subtítulo, badge de categoría, metadatos. |
| **02** | **El Problema** | Generar empatía con el dolor del usuario | 2 tarjetas Bento con síntomas y métricas del fallo actual. |
| **03** | **La Solución** | La gran revelación o nuevo paradigma | Declaración contundente en tarjeta destacada de 8 columnas. |
| **04** | **Bento Grid** | Desglose de las 3 capacidades nucleares | Cuadrícula de 3 tarjetas asimétricas con iconos y explicaciones. |
| **05** | **Big Data** | Prueba cuantitativa de resultados | 3 tarjetas de métricas gigantes (`99.8%`, `60 FPS`, `< 400ms`). |
| **06** | **Roadmap** | Progresión paso a paso de implementación | Línea horizontal de 3 pasos numerados (`PASO 01`, `02`, `03`). |
| **07** | **Contraste** | Antes vs. Después (Método viejo vs. Nuestro) | Tarjeta roja (fallas tradicionales) vs. Tarjeta verde (solución élite). |
| **08** | **Cierre / CTA** | Llamado a la acción claro e inolvidable | Conclusión directa, enlace/código y tecla de acción. |

---

## ⚙️ 4. Procedimiento de Ejecución (Paso a Paso)

### Paso 1: Recopilación o Redacción del Contenido
- Si el usuario suministra un texto, artículo o notas, deconstruir la información mapeándola a los 8 bloques anteriores.
- Preparar un diccionario JSON con las variables o usar el generador directo.

### Paso 2: Compilación de la Presentación
Ejecutar el comando nativo `build-deck`:
```bash
# Compilar deck con datos personalizados:
build-deck -d datos_presentacion.json -t dark-tech -o ~/Proyectos/mi-presentacion/index.html

# O compilar presentación demo instantánea:
build-deck --demo -t apple-keynote -o ~/Proyectos/demo-slides/index.html
```

Temas soportados con flag `-t`:
- `dark-tech` (Predeterminado: estética SaaS / IA, fondo azul noche y acentos cian).
- `apple-keynote` (Fondo blanco puro, minimalismo de evento Cupertino).
- `notion-minimal` (Fondo marfil cálido, líneas limpias y sobrias).
- `neo-brutalist` (Fondo amarillo pastel, bordes negros 3px y sombras duras de 4px).

### Paso 3: Visualización y Verificación
Abrir y enfocar la presentación con `preview-deck`:
```bash
preview-deck ~/Proyectos/mi-presentacion/index.html
```

---

## 🛠️ 5. Recursos y Utilidades de la Skill

- [`templates/master_presentation.html`](./templates/master_presentation.html): Plantilla maestra exacta con todo el CSS, JS, barra de progreso y componentes.
- [`scripts/build_presentation.py`](./scripts/build_presentation.py): Compilador CLI (`build-deck`).
- [`scripts/preview_presentation.py`](./scripts/preview_presentation.py): Visor rápido para navegador (`preview-deck`).
- [`references/temas_y_estilos.md`](./references/temas_y_estilos.md): Manual de referencia con paletas hex y atajos.
- [`examples/demo_presentacion_ia.html`](./examples/demo_presentacion_ia.html): Deck completo de demostración.

---

## ✅ 6. Verificación de Calidad
Comprobar que la skill cumple con el Estándar de Oro ejecutando:
```bash
validate-skill presentaciones-elite-html
```
Salida requerida: **100/100 [🏆 EXCELENCIA (Oro)]**.
