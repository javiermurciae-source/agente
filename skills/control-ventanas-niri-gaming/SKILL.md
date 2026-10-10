---
name: control-ventanas-niri-gaming
description: Procedimiento y control técnico para manipulación de ventanas mediante Niri IPC, lanzamiento y gestión de juegos en PC (Lutris), emuladores de Switch (Eden, Citron) y configuración de controles.
---

# Skill: Control de Ventanas en Niri y Gestión de Juegos (PC & Emuladores)

Esta habilidad documenta y automatiza el control programático del compositor **Niri** (Wayland) y el lanzamiento de juegos nativos, Lutris y emuladores de Nintendo Switch (**Eden**, **Citron**).

---

## 🪟 1. Control de Ventanas con Niri IPC (`niri msg`)

Niri expone una interfaz IPC nativa de alta velocidad que permite manipular la sesión gráfica sin necesidad de atajos de teclado manuales.

### A. Inspección de Ventanas y Estado
```bash
# Listar todas las ventanas abiertas (ID, título, App ID, Workspace, PID):
niri msg windows

# Inspección estructurada en JSON (ideal para scripts):
niri msg -j windows | jq '.[] | {id: .id, title: .title, app: .app_id, ws: .workspace_id}'

# Conocer la ventana actualmente enfocada:
niri msg focused-window
```

### B. Acciones de Control Directo (`niri msg action`)
- **Enfocar una ventana específica**:
  ```bash
  niri msg action focus-window --id <WINDOW_ID>
  ```
- **Alternar pantalla completa (Fullscreen)**:
  ```bash
  niri msg action fullscreen-window
  ```
- **Cerrar ventana**:
  ```bash
  niri msg action close-window
  ```
- **Maximizar / expandir columna**:
  ```bash
  niri msg action maximize-column
  ```
- **Centrar columna en pantalla**:
  ```bash
  niri msg action center-column
  ```
- **Mover ventana entre columnas**:
  ```bash
  niri msg action move-column-left
  niri msg action move-column-right
  ```
- **Alternar modo flotante**:
  ```bash
  niri msg action toggle-window-floating
  ```
- **Cambiar de espacio de trabajo**:
  ```bash
  niri msg action focus-workspace <NUMERO_WORKSPACE>
  ```
- **Lanzar una aplicación**:
  ```bash
  niri msg action spawn -- <COMANDO> [ARGUMENTOS...]
  ```

### C. Capturas de Pantalla (Screenshots en Niri)
- **Captura Silenciosa del Agente (Vía `grim`)**:
  Permite al agente capturar la pantalla completa en milisegundos para diagnóstico visual o guardado automático:
  ```bash
  grim ~/Pictures/Screenshots/Screenshot_$(date +%Y-%m-%d-%H%M%S).png
  ```
- **Captura y Copia al Portapapeles (Wayland)**:
  ```bash
  grim - | wl-copy --type image/png
  ```
- **Captura Nativa de Niri IPC**:
  ```bash
  # Capturar toda la pantalla:
  niri msg action screenshot-screen

  # Capturar solo la ventana enfocada:
  niri msg action screenshot-window
  ```
- **Atajos de Teclado del Usuario (Configurados con `serpantinum`)**:
  - `Print`: Captura de área seleccionada (`serpantinum screenshot`).
  - `Shift+Print`: Captura de área con editor interactivo (`satty`).
  - `Super+Print`: Captura de pantalla completa (`serpantinum screenshot --full`).
  - `Super+Shift+Print`: Captura completa con editor.

---

## 🎮 2. Rutas del Ecosistema Gaming en el Sistema

### Directorios Principales
- **Raíz de juegos**: `/home/rootkit/juegos/`
- **Juegos de PC**: `/home/rootkit/juegos/pc/`
  - Ejemplo: `Mortal Kombat 11` -> `/home/rootkit/Games/umu/umu-default/drive_c/Games/Mortal Kombat 11`
- **Juegos de Nintendo Switch**: `/home/rootkit/juegos/switch/` *(con symlink en `~/emuladores`)*
  - Títulos instalados:
    - `Dragon Ball FighterZ`
    - `Mario Kart 8 Deluxe`
    - `Super Smash Bros. Ultimate`
    - `The Legend of Zelda - Tears of the Kingdom`

---

## 🕹️ 3. Lanzamiento y Control de Emuladores

### A. Emulador Eden (Switch)
- **Binario ejecutable**: `/home/rootkit/.local/bin/eden`
- **Ruta de configuración**: `/home/rootkit/.config/eden/` (`qt-config.ini`, claves en `keys/prod.keys`).
- **Lanzamiento directo de ROM**:
  ```bash
  # Iniciar juego directamente:
  /home/rootkit/.local/bin/eden -g "/home/rootkit/juegos/switch/<CARPETA>/<JUEGO>.nsp"

  # Iniciar en pantalla completa automática:
  /home/rootkit/.local/bin/eden -f -g "/home/rootkit/juegos/switch/<CARPETA>/<JUEGO>.nsp"
  ```

### B. Emulador Citron (Switch)
- **AppImage**: `/home/rootkit/juegos/switch/citron_nightly-2f653f19f-linux-x86_64-use-nopgo.AppImage`
- **Lanzamiento**:
  ```bash
  /home/rootkit/juegos/switch/citron_nightly-2f653f19f-linux-x86_64-use-nopgo.AppImage "/ruta/al/juego.nsp"
  ```

### C. Lutris (Juegos de PC y Wine)
- **Binario**: `/usr/bin/lutris`
- **Listar juegos configurados**:
  ```bash
  lutris -l
  ```
- **Ejecutar juego por ID o Slug**:
  ```bash
  lutris lutris:rungame/<ID_O_SLUG>
  ```

---

## 🎮 4. Control de Mandos y Streaming
- **Mando Bluetooth**: Sony PlayStation Wireless Controller (DualSense / DualShock) conectado y mapeado automáticamente en Eden y Lutris.
- **Sunshine / HDMI Streaming**: Script de servicio para transmisión y gamepad virtual:
  ```bash
  bash /home/rootkit/sunshine-hdmi.sh
  ```
