# Entorno del Sistema (PC CachyOS Linux)

Especificaciones técnicas de la estación de trabajo donde opera este agente.

---

## 💻 1. Sistema Operativo y Hardware
- **Distribución**: CachyOS Linux (Arch Linux rolling release, kernel optimizado x86_64).
- **Compositor y GUI**: Wayland con compositor Niri y emulador de terminal Kitty.
- **Shell**: Fish Shell (con bash/zsh disponibles).
- **Audio y Notificaciones**: Servidor PipeWire nativo y demonio de notificaciones de escritorio con `notify-send`.

---

## 🛠️ 2. Herramientas y Runtimes de Desarrollo
- **Gestión de paquetes**: `pacman` y `yay` (AUR) para dependencias de sistema.
- **Runtimes de Scripting**:
  - `python3`: Soporte para automatizaciones, procesamiento de datos y librerías (`openpyxl`, `requests`, `pillow`, etc.).
  - `node` y `bun`: Ejecución ultra-rápida de scripts JavaScript/TypeScript (`.mjs`, `.js`) y herramientas Baileys.
- **Control de Versiones y Nube**:
  - Git y `gh` CLI (autenticado para clonar, crear repositorios y sincronizar).
- **Generación Gráfica y Documental**:
  - `imagemagick` (`magick`), `typst`, `ffmpeg`.
