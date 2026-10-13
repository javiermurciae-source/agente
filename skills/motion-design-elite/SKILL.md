---
name: motion-design-elite
description: >-
  Estándar supremo y metodología de diseño de movimiento 2D/3D algorítmico (estilo Buck, Apple, Ordinary Folk, Opus 5.5).
  Utilizar siempre que se solicite crear, dirigir o programar videos, motion graphics, animaciones o intros de alta calidad,
  erradicando el slop de IA mediante elemento conector, físicas de resorte analíticas, diseño suizo, foley/SFX sincronizado y render a 60 FPS.
---

# Skill: Motion Design Elite (Algorítmico & Anti-Slop)

Esta habilidad define el canon supremo para la producción programática de video y motion design con IA. Sustituye la estética barata y repetitiva de plantillas por **diseño de movimiento de nivel cinematográfico/estudio**.

---

## 🚫 1. Prohibiciones Inquebrantables (Eliminación Total del Slop de IA)

Los siguientes patrones son los "tells" automáticos que delatan un video mediocre de IA. **Están estrictamente prohibidos**:

1. **PROHIBIDO el texto con degradado genérico**: Nada de `background-clip: text` morado-cian o dorado en cada titular. Usar color sólido de alto contraste con jerarquía tipográfica real.
2. **PROHIBIDO los fondos negros planos con partículas flotantes**: Partículas aleatorias sin masa ni colisión son relleno perezoso. El fondo debe tener capas estructurales (grillas técnicas, semitonos reactivos, guías, micro-textura o luz volumétrica sutil).
3. **PROHIBIDO los brillos excesivos (glows) y neón genérico**: El impacto visual se logra con ritmo, peso, contraste y composición, no quemando los píxeles con filtros de resplandor.
4. **PROHIBIDO los elementos centrados y flotantes sin anclaje**: No diseñar diapositivas de PowerPoint. Usar composición asimétrica (anclaje a bordes, zonas divididas, reglas estructurales).
5. **PROHIBIDO las entradas arbitrarias**: Nada de elementos que entran con `y: 30, opacity: 0` de la nada. **Cada movimiento debe nacer de algo que ya existe en pantalla.**
6. **PROHIBIDO el video sin sonido o con música genérica desconectada**: Cada impacto visual debe tener su contraparte acústica milimétrica.

---

## 💎 2. Los 6 Pilares de un Video Élite

### Pilar 1: El Conector Continuo (The Visual Motif Anchor)
* En lugar de transiciones arbitrarias (cortes, barridos falsos), **un único elemento geométrico u objeto transporta el momento y conecta toda la película** (ej. un punto conector, una línea tensa, un prisma).
* El conector muta de función orgánicamente:
  * Nace como un control de UI (un switch, un botón).
  * Salta y se convierte en el punto sobre una letra (*tittle*).
  * Se desprende y traza una curva física.
  * Se expande llenando el plano y cambia de estado conservando masa.
  * Regresa en reversa en los últimos fotogramas para lograr un **bucle infinito perfecto (Seamless Loop)**.

### Pilar 2: Físicas Reales de Forma Cerrada (Closed-Form Springs)
No usar curvas CSS de plantilla. Utilizar la ecuación analítica del oscilador armónico subamortiguado:

$$\text{spring}(t) = 1 - e^{-\zeta \omega_n t} \left(\cos(\omega_d t) + \frac{\zeta}{\sqrt{1 - \zeta^2}}\sin(\omega_d t)\right)$$

* $\zeta \approx 0.421 \implies$ **Sobreimpulso exacto del +22%**.
* La trayectoria del objeto y las líneas del gráfico deben ser calculadas por la **misma función matemática**. La velocidad comunica masa; el frenado comunica inercia.

### Pilar 3: Composición Suiza y Jerarquía Asimétrica
* **Mínimo tres capas por escena**:
  1. *Capa Base:* Tratamiento de fondo (cuadrícula milimétrica, coordenadas, semitonos).
  2. *Capa Contenido:* Tipografía audaz (titulares al 60-80% del ancho del cuadro), pesos contrastados (950 Black vs 400 Light).
  3. *Capa Estructura:* Reglas, divisores, marcas de recorte (*crop marks*), metadatos.
* **Paleta austera y disciplinada**:
  * Un lienzo base (Blanco cálido `#f8f7f4` o Negro carbón `#0d0e12`).
  * Un color de texto principal.
  * **Un único color de acento vibrante** (ej. Naranja `#ff5500`, Azul eléctrico, Lima técnico).

### Pilar 4: Diseño de Sonido Muestra por Muestra (Sound Design & Foley)
El audio es el 50% de la energía de la pieza:
1. **Banda Rítmica Cuantizada (Beat Grid):** Compás constante (ej. 120 BPM = 0.5s por beat). Cada evento clave (clic, aterrizaje, pico del resorte, corte) ocurre exactamente en un beat o subdivisión (off-beat).
2. **SFX Táctiles (Foley Sintetizado o Grabado):**
   * *Clics hápticos:* Transitorio de alta frecuencia (2400-3200 Hz) con decaimiento ultrarrápido (30ms).
   * *Desplazamientos y Whooshes:* Barridos de frecuencia en campana.
   * *Resorte armónico:* Tono acústico oscilante que sigue la curva matemática.
   * *Pings y Chimes:* Campanas cristalinas al alcanzar el pico de sobreimpulso.
   * *Sub-bass Impacts:* Golpes de 45-60 Hz con caída exponencial al revelar títulos clave.

### Pilar 5: Tipografía Cinética Cinematográfica
* El texto no solo se lee: **se mueve con intención**.
* Descomposición de palabras en letras individuales con retardos elásticos escalonados (*stagger*).
* Círculos orbitales de texto que se dispersan hacia el exterior, o tickers de alta velocidad que cruzan la pantalla aportando ritmo y dinamismo.

### Pilar 6: Determinismo 60 FPS (`seek(t)`)
* Cada fotograma $0 \le \text{frame} < N$ es una función pura del tiempo $t = \text{frame} / 60.0$.
* Cero dependencias de timers del navegador (`setTimeout`, `setInterval`).
* Independencia de resolución: escalable a 4K sin pérdida vectorial.

---

## 🛠️ 3. Pipeline de Generación Rápida

1. **Definir el Argumento y Conector:** Elegir el elemento continuo, los 3-4 cambios de estado y la duración (típicamente 15s).
2. **Sintetizar el Audio:** Ejecutar el generador algorítmico en Python (`wave` / `struct`) para producir el WAV/MP3 con el beat y los SFX sincronizados al milisegundo.
3. **Programar la Composición 60 FPS:** En Remotion o Canvas determinista con fórmulas analíticas.
4. **Renderizar y Empaquetar:** Compilar a MP4 H.264 Full HD con audio AAC 256k y lanzar reproducción inmediata en VLC.
