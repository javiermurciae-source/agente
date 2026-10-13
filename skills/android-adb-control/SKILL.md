---
name: android-adb-control
description: Procedimiento y control técnico para administración, depuración e interacción con dispositivos Android y aplicaciones móviles mediante comandos nativos directos de ADB. Utilizar cuando se solicite conectar por USB o Wi-Fi, instalar o extraer APKs, capturar pantalla, automatizar toques y teclados, inspeccionar jerarquía de UI o depurar logs con logcat.
---

# Android ADB: Control y Automatización Nativa (Zero-Python)

Procedimiento de ejecución quirúrgica utilizando exclusivamente el binario nativo de Arch/CachyOS (`/usr/bin/adb`). Sin capas intermedias, wrappers ni librerías de Python: comandos directos de shell.

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
