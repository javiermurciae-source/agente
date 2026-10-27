---
name: android-adb-control
description: Control técnico y automatización para administración, depuración e interacción con dispositivos Android físicos y emuladores. Prioriza el protocolo estándar Mobile Next (MCP mobile) con fallback a comandos nativos de ADB.
---

# Android Control & Automatización (Mobile-MCP Principal + ADB Nativo)

Estándar maestro para interacción, automatización de apps, extracción de datos y control de dispositivos Android en el entorno de Camilo.

---

## 🥇 Protocolo Principal: Mobile MCP Server (`@mobilenext/mobile-mcp`)
Para toda interacción inteligente con aplicaciones, interfaces y flujos de usuario, la herramienta predeterminada y prioritaria es el servidor MCP **`mobile`** (`mcp-server-mobile`), ya que opera por **árbol de accesibilidad semántico** (ahorro masivo de tokens sin quemar visión) y unifica la API:

- **Detección de dispositivos**: `mobile_list_available_devices`
- **Lanzamiento y cierre**: `mobile_launch_app`, `mobile_terminate_app`
- **Gestión de paquetes**: `mobile_install_app`, `mobile_uninstall_app`, `mobile_list_apps`
- **Interacción y Gestos**: `mobile_tap`, `mobile_swipe`, `mobile_input_text`
- **Entorno y Sistema**: `mobile_clipboard`, `mobile_set_orientation`, `mobile_set_location`

---

## ⚡ Fallback y Utilidades de Bajo Nivel: Comandos Nativos ADB (`/usr/bin/adb`)
Se reservan exclusivamente para diagnósticos directos del sistema operativo, conexiones inalámbricas (`adb connect`), logs de bajo nivel (`logcat`) o tareas donde no se requiera el servidor MCP.

---

## 🎯 Disparadores de Activación
- Operaciones con dispositivos móviles Android conectados por cable USB o Wi-Fi.
- Instalación, actualización, extracción o desinstalación de archivos `.apk`.
- Automatización de toques, gestos, teclado y lectura de elementos de interfaz.
- Capturas de pantalla instantáneas y diagnóstico de logs (`logcat`).

---

## ⚡ Comandos Nativos de Shell (Línea Directa)

### 1. Detección y Conexión
```bash
# Ver dispositivos conectados con detalles de modelo y estado
adb devices -l

# Activar modo Wi-Fi en el dispositivo (puerto 5555) y conectar por IP
adb tcpip 5555
adb connect <IP_DISPOSITIVO>:5555

# Desconectar sesión inalámbrica
adb disconnect <IP_DISPOSITIVO>:5555
```

### 2. Gestión Quirúrgica de Aplicaciones (APKs)
```bash
# Instalar APK reemplazando si ya existe y auto-concediendo permisos runtime
adb install -r -g app.apk

# Listar paquetes de usuario (excluye apps del sistema)
adb shell pm list packages -3

# Extraer el instalador APK de una app instalada hacia el PC (en 1 solo comando)
adb shell pm path com.ejemplo.app | head -n1 | cut -d: -f2 | tr -d '\r' | xargs -I{} adb pull {} ./app_extraida.apk

# Forzar cierre inmediato y borrado de caché/datos de una app
adb shell am force-stop com.ejemplo.app
adb shell pm clear com.ejemplo.app

# Lanzar la app directamente por su actividad principal
adb shell am start -n com.ejemplo.app/.MainActivity
```

### 3. Automatización de Pantalla y Teclado (Nativo)
```bash
# Toque en coordenadas X Y
adb shell input tap 540 1200

# Deslizar (Swipe) de (X1, Y1) a (X2, Y2) en ms
adb shell input swipe 540 1600 540 400 250

# Escribir texto directo (los espacios van como %s)
adb shell input text "Texto%sSin%sEspacios%sRotos"

# Teclas del sistema (3: Home, 4: Back, 26: Power, 66: Enter, 187: Apps Recientes)
adb shell input keyevent 3
adb shell input keyevent 4
adb shell input keyevent 66
```

### 4. Captura Instantánea y Volcado de UI (Sin Archivos Temporales)
```bash
# Captura de pantalla directa en stream hacia archivo PNG local
adb exec-out screencap -p > captura.png

# Extraer el árbol jerárquico XML de la pantalla actual para leer botones y textos
adb exec-out uiautomator dump /dev/tty > /dev/null 2>&1 || adb shell uiautomator dump /data/local/tmp/ui.xml && adb pull /data/local/tmp/ui.xml ./ui.xml && adb shell rm -f /data/local/tmp/ui.xml
```

### 5. Diagnóstico de Errores y Logs
```bash
# Volcar únicamente errores críticos y crashes recientes
adb logcat -d *:E

# Limpiar buffer de logs antes de reproducir un fallo
adb logcat -c

# Ver logs en tiempo real filtrados por el proceso de una app
adb logcat --pid=$(adb shell pidof -s com.ejemplo.app)
```

---

Para códigos de tecla detallados y flags de `am`/`pm`, consultar [`references/keycodes_and_intents.md`](file:///home/rootkit/agente/skills/android-adb-control/references/keycodes_and_intents.md).
