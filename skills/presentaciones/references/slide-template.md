# Plantilla Maestra y Catálogo de Arquetipos (Slide Template)

Esta guía contiene los dos esqueletos maestros y el catálogo completo de componentes y arquetipos modulares en HTML, CSS y JavaScript para construir presentaciones de alto impacto.

---

## 1. Esqueleto Base Dual-Tone Corporate (Canva Authentic Master)

Usar este esqueleto para propuestas de negocio, consultoría corporativa, informes ejecutivos y presentaciones institucionales de alto nivel.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITULO_PRESENTACION}}</title>
  
  <!-- Tipografía Canva Corporate -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <style>
    :root {
      --navy: #132232;
      --navy-deep: #0C1722;
      --slate: #5B696F;
      --ice-blue: #ADC7EA;
      --petrol: #006D72;
      --border-gray: #E0E6E9;
      --white: #FFFFFF;
      --dark-text: #111827;
      --dark-muted: #4B5563;
      --light-text: #FFFFFF;
      --light-muted: #9DB3C1;
      
      --font-display: 'Oswald', sans-serif;
      --font-body: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    html {
      scroll-snap-type: y mandatory;
      scroll-behavior: smooth;
      overflow-y: scroll;
      height: 100vh;
      background-color: var(--navy);
      font-family: var(--font-body);
      -webkit-font-smoothing: antialiased;
    }

    body { background-color: var(--navy); margin: 0; padding: 0; position: relative; }

    .slide {
      scroll-snap-align: start;
      scroll-snap-stop: always;
      height: 100vh;
      min-height: 100vh;
      max-height: 100vh;
      overflow: hidden;
      position: relative;
      display: flex;
    }

    .title-display {
      font-family: var(--font-display);
      text-transform: uppercase;
      letter-spacing: -0.01em;
      line-height: 1.05;
    }

    /* Píldoras curvas decorativas */
    .pill-top-left {
      position: absolute; top: 0; left: 0;
      width: clamp(260px, 35vw, 500px); height: clamp(80px, 12vh, 140px);
      background: var(--slate); border-bottom-right-radius: 999px; z-index: 1; pointer-events: none;
    }
    .pill-top-left::after {
      content: ''; position: absolute; bottom: -18px; left: 0; width: 85%; height: 18px;
      background: var(--ice-blue); border-bottom-right-radius: 999px;
    }
    .pill-bottom-right {
      position: absolute; bottom: 0; right: 0;
      width: clamp(240px, 32vw, 460px); height: clamp(70px, 11vh, 130px);
      background: var(--ice-blue); border-top-left-radius: 999px; z-index: 1; pointer-events: none;
    }
    .pill-bottom-right::before {
      content: ''; position: absolute; top: -16px; right: 0; width: 75%; height: 16px;
      background: #FFFFFF; border-top-left-radius: 999px;
    }

    /* Líneas decorativas con punto */
    .canva-line { display: flex; align-items: center; width: 100%; margin: 18px 0; }
    .canva-line.right-dot::before { content: ''; flex: 1; height: 1.5px; background: #FFF; opacity: 0.85; }
    .canva-line.right-dot::after { content: ''; width: 7px; height: 7px; border-radius: 50%; background: #FFF; margin-left: 2px; }
    .canva-line.left-dot::before { content: ''; width: 7px; height: 7px; border-radius: 50%; background: #FFF; margin-right: 2px; }
    .canva-line.left-dot::after { content: ''; flex: 1; height: 1.5px; background: #FFF; opacity: 0.85; }

    /* Barra de Progreso y UI */
    .progress-bar { position: fixed; bottom: 0; left: 0; width: 100%; height: 4px; background: rgba(0,0,0,0.1); z-index: 100; }
    .progress-fill { height: 100%; background: var(--ice-blue); width: 0%; transition: width 0.3s ease; }
    .slide-counter {
      position: fixed; bottom: 20px; right: 24px; font-family: var(--font-mono); font-size: 11px;
      color: #111827; background: rgba(255,255,255,0.85); padding: 4px 10px; border-radius: 999px; backdrop-filter: blur(8px); z-index: 100;
    }
    .nav-hints {
      position: fixed; bottom: 20px; left: 24px; font-family: var(--font-mono); font-size: 10px;
      color: rgba(17,24,39,0.6); background: rgba(255,255,255,0.85); padding: 4px 10px; border-radius: 999px; text-transform: uppercase; z-index: 100;
    }
  </style>
</head>
<body>
  <!-- Contenido de Slides aquí -->

  <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
  <div class="slide-counter" id="slideCounter">1 / N</div>
  <div class="nav-hints">&darr; &uarr; o ESPACIO &bull; F para pantalla completa</div>

  <script>
    (function() {
      const slides = Array.from(document.querySelectorAll('.slide'));
      const progressFill = document.getElementById('progressFill');
      const slideCounter = document.getElementById('slideCounter');
      const totalSlides = slides.length;
      let currentIndex = 0;

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const idx = slides.indexOf(entry.target);
            if (idx !== -1) {
              currentIndex = idx;
              if (progressFill) progressFill.style.width = (((idx + 1) / totalSlides) * 100) + '%';
              if (slideCounter) slideCounter.textContent = (idx + 1) + ' / ' + totalSlides;
            }
          }
        });
      }, { threshold: 0.5 });
      slides.forEach(slide => observer.observe(slide));

      function scrollToSlide(idx) {
        if (idx >= 0 && idx < totalSlides) slides[idx].scrollIntoView({ behavior: 'smooth' });
      }

      window.addEventListener('keydown', (e) => {
        switch (e.key) {
          case 'ArrowDown': case 'ArrowRight': case 'PageDown': case ' ':
            e.preventDefault(); scrollToSlide(currentIndex + 1); break;
          case 'ArrowUp': case 'ArrowLeft': case 'PageUp':
            e.preventDefault(); scrollToSlide(currentIndex - 1); break;
          case 'Home': e.preventDefault(); scrollToSlide(0); break;
          case 'End': e.preventDefault(); scrollToSlide(totalSlides - 1); break;
          case 'f': case 'F':
            if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
            else document.exitFullscreen().catch(() => {});
            break;
        }
      });
    })();
  </script>
</body>
</html>
```

---

## 2. Catálogo de Arquetipos Modulares (Canva Corporate)

### Arquetipo A: Portada Hero con Curvas y Líneas
```html
<section class="slide" style="flex-direction: column; justify-content: center; padding: 0 clamp(32px, 8vw, 140px); background: var(--navy);">
  <div class="pill-top-left"></div>
  <div class="pill-bottom-right"></div>
  <div style="max-width: 900px; position: relative; z-index: 2;">
    <div class="canva-line right-dot"></div>
    <h1 class="title-display" style="font-size: clamp(3.2rem, 7.8vw, 6.8rem); color: #FFF; margin-bottom: 8px;">
      {{TITULO_PROYECTO}}
    </h1>
    <div style="font-size: clamp(0.95rem, 1.2vw, 1.2rem); font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; color: #FFF; opacity: 0.9;">
      {{SUBTITULO_O_AUTOR}}
    </div>
    <div class="canva-line left-dot"></div>
  </div>
</section>
```

### Arquetipo B: Índice / Agenda con Nodos Verticales
```html
<section class="slide" style="flex-direction: row; align-items: center; padding: 0 clamp(32px, 8vw, 140px); gap: clamp(40px, 8vw, 120px); background: var(--navy);">
  <div style="flex: 1; max-width: 420px;">
    <h2 class="title-display" style="font-size: clamp(3rem, 5.5vw, 5.2rem); color: #FFF; line-height: 0.98;">
      ÍNDICE DEL<br>DOCUMENTO
    </h2>
  </div>
  <div style="flex: 1.4; position: relative; padding-left: 32px;">
    <!-- Línea vertical conectora -->
    <div style="position: absolute; left: 7px; top: 10px; bottom: 12px; width: 1.5px; background: #FFF; opacity: 0.6;"></div>
    
    <div style="position: relative; margin-bottom: 28px;">
      <div style="position: absolute; left: -32px; top: 4px; width: 16px; height: 16px; border-radius: 50%; background: #FFF;"></div>
      <div style="font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #FFF;">01. INTRODUCCIÓN</div>
      <div style="font-size: 0.9rem; color: var(--light-muted);">Nuestra metodología y contexto</div>
    </div>
    <!-- Repetir bloques para 02, 03, 04, 05 -->
  </div>
</section>
```

### Arquetipo C: Proceso en 4 Fases (Dual-Tone Split Horizontal)
```html
<section class="slide" style="flex-direction: column;">
  <!-- Header Marino (30vh) -->
  <div style="height: 30vh; background: var(--navy); display: flex; flex-direction: column; justify-content: center; padding: 0 clamp(32px, 7vw, 120px);">
    <h2 class="title-display" style="font-size: clamp(2.2rem, 4.2vw, 3.8rem); color: #FFF; margin-bottom: 6px;">{{TITULO_METODOLOGIA}}</h2>
    <div style="font-size: 0.95rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ice-blue);">{{SUBTITULO_FASES}}</div>
  </div>
  <!-- Cuerpo Blanco (70vh) con 4 columnas conectadas por línea horizontal -->
  <div style="height: 70vh; background: #FFF; display: flex; align-items: center; padding: 0 clamp(32px, 7vw, 120px); position: relative;">
    <div style="position: absolute; top: 60px; left: 8%; right: 8%; height: 1px; background: var(--dark-text); opacity: 0.4;"></div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; width: 100%; position: relative; z-index: 2;">
      <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <div style="width: 24px; height: 24px; border-radius: 50%; background: var(--navy); margin-bottom: 20px; border: 3px solid #FFF; box-shadow: 0 0 0 1px var(--navy);"></div>
        <div style="font-weight: 700; text-transform: uppercase; color: var(--dark-text); margin-bottom: 8px;">FASE 01</div>
        <div style="font-size: 0.85rem; color: var(--dark-muted); line-height: 1.5;">Descripción del hito.</div>
      </div>
      <!-- Repetir para Fases 2, 3, 4 -->
    </div>
  </div>
</section>
```

### Arquetipo D: Matriz 2x2 (Dual-Tone Split Vertical)
```html
<section class="slide" style="flex-direction: row;">
  <!-- Sidebar Izquierdo Navy (35vw) -->
  <div style="width: 35vw; height: 100vh; background: var(--navy); display: flex; flex-direction: column; justify-content: center; padding: 0 clamp(32px, 4.5vw, 70px);">
    <h2 class="title-display" style="font-size: clamp(2.8rem, 5vw, 4.6rem); color: #FFF; line-height: 1; margin-bottom: 14px;">{{TITULO_SECCION}}</h2>
    <div style="font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: #FFF; margin-bottom: 12px;">{{KICKER_SUB}}</div>
    <div style="font-size: 0.95rem; color: var(--light-muted); line-height: 1.5;">{{TEXTO_CONTEXTO}}</div>
  </div>
  <!-- Cuadrícula 2x2 Blanca (65vw) -->
  <div style="width: 65vw; height: 100vh; background: #FFF; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;">
    <div style="padding: 40px; border-right: 1px solid var(--border-gray); border-bottom: 1px solid var(--border-gray); display: flex; flex-direction: column; justify-content: center;">
      <h3 style="font-family: var(--font-display); font-size: 1.8rem; color: var(--dark-text); margin-bottom: 6px;">Pilar A</h3>
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--slate); margin-bottom: 8px;">CATEGORÍA</div>
      <div style="font-size: 0.88rem; color: var(--dark-muted); line-height: 1.5;">Detalle del cuadrante.</div>
    </div>
    <!-- Celdas 2, 3, 4 respetando bordes -->
  </div>
</section>
```

### Arquetipo E: Cronograma Gantt Matricial
```html
<section class="slide" style="flex-direction: column;">
  <div style="height: 28vh; background: var(--navy); display: flex; flex-direction: column; justify-content: center; padding: 0 clamp(32px, 6vw, 100px);">
    <h2 class="title-display" style="font-size: clamp(2.2rem, 4.2vw, 3.8rem); color: #FFF;">CALENDARIO</h2>
    <div style="font-size: 0.95rem; font-weight: 600; text-transform: uppercase; color: var(--ice-blue);">DEFINICIÓN TEMPORAL DE ACTIVIDADES</div>
  </div>
  <div style="height: 72vh; background: #FFF; display: flex; align-items: center; justify-content: center; padding: 0 clamp(32px, 6vw, 100px);">
    <table style="width: 100%; border-collapse: collapse; border: 1px solid #111827;">
      <thead>
        <tr>
          <th style="border: 1px solid #111827; padding: 10px; width: 18%;">Actividad</th>
          <th style="border: 1px solid #111827;">Sem 1</th>
          <th style="border: 1px solid #111827;">Sem 2</th>
          <th style="border: 1px solid #111827;">Sem 3</th>
          <th style="border: 1px solid #111827;">Sem 4</th>
          <th style="border: 1px solid #111827;">Sem 5</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #111827; padding: 12px; font-weight: 600;">Fase A</td>
          <td style="border: 1px solid #111827; background: #132232;"></td>
          <td style="border: 1px solid #111827; background: #132232;"></td>
          <td style="border: 1px solid #111827;"></td>
          <td style="border: 1px solid #111827;"></td>
          <td style="border: 1px solid #111827;"></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
```
