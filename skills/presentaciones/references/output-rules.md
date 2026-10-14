# Especificación de Reglas de Salida (Output Rules)

Toda presentación HTML debe cumplir de manera estricta y sin excepciones con las siguientes especificaciones técnicas de diseño, maquetación y arquitectura.

---

## 1. Lienzo, Contenedor y Scroll-Snap (100vh Estricto)

1. **Un solo archivo autocontenido**:
   - Todo el CSS y JS debe estar inline dentro del archivo HTML.
   - La única llamada externa permitida es a Google Fonts en el `<head>`.
   - Prohibido enlazar CDNs de Tailwind, Bootstrap, jQuery o bibliotecas de terceros.

2. **Scroll-Snap Vertical**:
   - El elemento `html` o contenedor maestro debe tener:
     ```css
     html {
       scroll-snap-type: y mandatory;
       scroll-behavior: smooth;
       overflow-y: scroll;
       height: 100vh;
     }
     ```
   - Cada diapositiva (`.slide`) debe tener:
     ```css
     .slide {
       scroll-snap-align: start;
       scroll-snap-stop: always;
       height: 100vh;
       min-height: 100vh;
       max-height: 100vh;
       overflow: hidden;
       box-sizing: border-box;
       display: flex;
       position: relative;
     }
     ```

3. **Arquitecturas de Slide Permitidas**:
   - **Slide Completo Unificado** (`padding: clamp(32px, 5vw, 64px) clamp(32px, 7vw, 120px); flex-direction: column; justify-content: center;`): Utilizado en portadas, divisores de sección, agendas y cierres.
   - **Slide Dual-Tone Split Horizontal**:
     - Banda superior oscura (`height: 28vh; min-height: 28vh; display: flex; flex-direction: column; justify-content: center; padding: 0 clamp(32px, 6vw, 100px);`).
     - Cuerpo inferior blanco (`height: 72vh; background: #FFFFFF; display: flex; align-items: center; padding: 0 clamp(32px, 6vw, 100px);`).
     - Ideal para procesos horizontales, tablas comparativas y cronogramas Gantt.
   - **Slide Dual-Tone Split Vertical**:
     - Sidebar izquierdo oscuro (`width: 35vw; min-width: 35vw; height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 0 clamp(32px, 4vw, 60px);`).
     - Panel derecho blanco (`width: 65vw; height: 100vh; background: #FFFFFF; display: grid;` o `display: flex; flex-direction: column; justify-content: center;`).
     - Ideal para matrices 2x2, cuadrículas de maestros y listas verticales de KPIs numerados.

4. **Tolerancia Cero al Scroll Interno**:
   - Queda terminantemente prohibido que una diapositiva tenga barras de desplazamiento verticales u horizontales internas.
   - Si una tabla o diagrama es denso, se ajustan los paddings y tamaños de fuente mediante `clamp()` o se divide en dos diapositivas consecutivas.

---

## 2. Tipografía Matemática con `clamp()`

Todas las fuentes deben escalar automáticamente según las dimensiones de la pantalla del presentador o proyector:

| Elemento | Fórmula CSS Obligatoria |
| :--- | :--- |
| **Titular Principal (Hero)** | `font-size: clamp(2.8rem, 6.5vw, 6rem); line-height: 1.04; letter-spacing: -0.015em;` |
| **Titular de Slide / Sección** | `font-size: clamp(2.2rem, 4.2vw, 3.8rem); line-height: 1.08;` |
| **Subtítulos y Bajadas** | `font-size: clamp(0.95rem, 1.3vw, 1.25rem); line-height: 1.45;` |
| **Cuerpo de Texto y Bullets** | `font-size: clamp(0.85rem, 1vw, 1.05rem); line-height: 1.5;` |
| **Números de Métrica / Cifras** | `font-size: clamp(3rem, 6vw, 5.5rem); font-weight: 700; line-height: 1;` |
| **Kickers / Badges / Monospace** | `font-size: clamp(10px, 0.85vw, 12px); letter-spacing: 0.12em; text-transform: uppercase;` |

---

## 3. Jerarquía y Reglas de Contenido

1. **Una sola idea por slide**:
   - Cada slide debe responder a un único propósito o mensaje clave.
2. **Máximo 4 a 6 elementos por cuadrícula o lista**:
   - Textos concisos, precisos y con alta densidad informativa.
3. **Alto Contraste Estricto**:
   - En paneles oscuros: texto `#FFFFFF` y acentos en `#ADC7EA` o colores neón.
   - En paneles blancos: texto `#111827` (negro carbón) y secundarios `#4B5563` (gris oscuro legible). Prohibido usar grises claros sobre blanco.
4. **Divisores de Sección Obligatorios**:
   - Separar bloques narrativos con diapositivas de quiebre (cifra gigante o nombre de sección central).
5. **Cierre Ineludible**:
   - Toda presentación concluye con una diapositiva de síntesis, agradecimiento o llamada a la acción con botón de reinicio.

---

## 4. Animaciones Escalonadas (*Staggered*) y Accesibilidad

1. **Animación de entrada sutil**:
   - Elementos interactivos (`.animate-item`) inician en `opacity: 0; transform: translateY(18px);`.
   - Al intersectar con el viewport (`IntersectionObserver`), se les añade la clase `.is-visible` con transiciones suaves escalonadas (`0.08s`, `0.18s`, `0.28s`...).
2. **Respeto a `prefers-reduced-motion`**:
   - Si el sistema del usuario lo solicita, las transiciones se anulan instantáneamente (`opacity: 1; transform: none; transition: none;`).

---

## 5. Navegación y UI Fija

1. **Barra de Progreso Inferior**:
   - Fija en `bottom: 0; left: 0; height: 3px;` avanzando suavemente (`transition: width 0.3s ease;`) en función del slide activo.
2. **Indicador de Slide Flotante**:
   - Badge discreto en la esquina inferior derecha (`X / Total`).
3. **Controles Multicanal**:
   - Teclado: `ArrowDown`, `ArrowRight`, `Space`, `PageDown` avanzan; `ArrowUp`, `ArrowLeft`, `PageUp` retroceden; `Home` al inicio, `End` al final.
   - Pantalla completa nativa con tecla `F`.
   - Soporte táctil/swipe para móviles y tablets.
