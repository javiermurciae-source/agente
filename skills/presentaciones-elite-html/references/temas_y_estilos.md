# Manual de Referencia: Temas, Estilos y Especificaciones Técnicas

Este manual complementa la Skill `presentaciones-elite-html`, detallando las especificaciones de diseño, paletas y ergonomía para presentaciones interactivas en HTML5.

---

## 🎨 1. Paletas de Colores de los 4 Temas Maestros

### A. Dark Tech (`data-theme="dark-tech"`) — Predeterminado
- **Fondo General**: `#0A0D14` (Obsidiana)
- **Lienzo 16:9**: `#0E131F` (Azul Noche Profundo)
- **Tarjetas / Contenedores**: `rgba(23, 31, 51, 0.65)` con `backdrop-filter: blur(12px)`
- **Bordes**: `rgba(255, 255, 255, 0.08)`
- **Acento Primario**: `#38BDF8` (Cian Eléctrico)
- **Gradiente de Impacto**: `linear-gradient(135deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%)`
- **Uso Recomendado**: Tecnologías de IA, SaaS, ingeniería de software, arquitectura de sistemas y presentaciones de código.

### B. Apple Keynote Minimal (`data-theme="apple-keynote"`)
- **Fondo General**: `#E5E5EA`
- **Lienzo 16:9**: `#FFFFFF` (Blanco Puro)
- **Tarjetas / Contenedores**: `#F5F5F7` (Gris Perla Suave)
- **Bordes**: `rgba(0, 0, 0, 0.06)`
- **Texto Principal**: `#1D1D1F` (Negro Carbón)
- **Texto Secundario**: `#86868B`
- **Acento Primario**: `#0071E3` (Azul Cupertino)
- **Uso Recomendado**: Lanzamientos de producto, pitch decks a inversores, presentaciones corporativas ejecutivas.

### C. Notion Clean (`data-theme="notion-minimal"`)
- **Fondo General**: `#ECEBE8`
- **Lienzo 16:9**: `#FBFBFA` (Marfil Cálido)
- **Tarjetas**: `#FFFFFF` con borde `#E3E2DE`
- **Texto Principal**: `#37352F`
- **Texto Secundario**: `#787774`
- **Acento**: `#2EAADC`
- **Uso Recomendado**: Documentaciones, manuales paso a paso, capacitaciones internas, resúmenes de equipo.

### D. Neo-Brutalist (`data-theme="neo-brutalist"`)
- **Fondo General**: `#FEEF85` (Amarillo Pastel Eléctrico)
- **Lienzo 16:9**: `#FFFFFF`
- **Tarjetas**: `#FFFDF5` con borde negro sólido `#18181B` de 2-3px
- **Sombras**: Duras sin difuminar (`4px 4px 0px #18181B`)
- **Acento**: `#FF3366` / `#FF9900`
- **Uso Recomendado**: Presentaciones de alto impacto, YouTube, streaming, proyectos indie hacker y comunidades de desarrolladores.

---

## 📐 2. Geometría y Ergonomía Visual (16:9 1920×1080)

1. **Lienzo Base**: 1920 píxeles de ancho por 1080 píxeles de alto.
2. **Auto-Escalado Determinado**: Se calcula `scale = Math.min(windowWidth / 1920, windowHeight / 1080)` para encajar al 100% en cualquier pantalla sin barras de desplazamiento ni desbordes.
3. **Márgenes de Respiro**: Padding lateral de 64px a 100px para que ningún elemento toque el borde del display.
4. **Zona Segura para Cámara (`#safety-zone`)**:
   - Dimensiones: 320px de ancho × 220px de alto.
   - Posición: 36px desde la esquina inferior derecha.
   - Propósito: Asegura que el rostro del presentador (en grabaciones con OBS o cámara web) no tape métricas, títulos ni botones.

---

## ⌨️ 3. Mapa de Atajos de Teclado

| Tecla | Acción |
| :--- | :--- |
| `→` / `↓` / `Espacio` / `Enter` | Avanzar a la siguiente diapositiva |
| `←` / `↑` / `Backspace` | Retroceder a la diapositiva anterior |
| `F` | Alternar pantalla completa (*Fullscreen*) |
| `C` | Mostrar / Ocultar recuadro de zona segura para cámara |
| `T` | Conmutar dinámicamente entre los 4 temas visuales |
| `1` a `8` | Saltar directamente a la diapositiva número N |
| `Home` / `End` | Ir a la primera / última diapositiva |
