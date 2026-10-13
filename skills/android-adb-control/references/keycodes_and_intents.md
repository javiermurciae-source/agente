# Referencia Rápida: Keycodes e Intents para Android ADB

## Códigos de Tecla Habituales (Keyevents)

| Código | Nombre Android | Acción |
| :--- | :--- | :--- |
| `3` | `KEYCODE_HOME` | Ir a la pantalla de inicio |
| `4` | `KEYCODE_BACK` | Botón Atrás |
| `24` | `KEYCODE_VOLUME_UP` | Subir volumen |
| `25` | `KEYCODE_VOLUME_DOWN` | Bajar volumen |
| `26` | `KEYCODE_POWER` | Bloquear/Encender pantalla |
| `66` | `KEYCODE_ENTER` | Tecla Enter |
| `67` | `KEYCODE_DEL` | Tecla Borrar / Backspace |
| `82` | `KEYCODE_MENU` | Botón Menú |
| `187` | `KEYCODE_APP_SWITCH` | Pantalla de apps recientes |
| `224` | `KEYCODE_WAKEUP` | Despertar pantalla |
| `223` | `KEYCODE_SLEEP` | Suspender pantalla |

---

## Comandos Críticos de Activity Manager (`am`)

- **Lanzar Activity**:
  ```bash
  adb shell am start -n <package>/<activity>
  ```
- **Lanzar por Acción con Datos (URL)**:
  ```bash
  adb shell am start -a android.intent.action.VIEW -d "https://example.com"
  ```
- **Forzar Cierre de App**:
  ```bash
  adb shell am force-stop <package>
  ```
- **Lanzar y medir tiempo de arranque**:
  ```bash
  adb shell am start -W -n <package>/<activity>
  ```

---

## Comandos Críticos de Package Manager (`pm`)

- **Ruta de instalación de un APK**:
  ```bash
  adb shell pm path <package>
  ```
- **Borrar caché y datos de app**:
  ```bash
  adb shell pm clear <package>
  ```
- **Listar solo apps de usuario**:
  ```bash
  adb shell pm list packages -3
  ```
- **Conceder permiso de tiempo de ejecución**:
  ```bash
  adb shell pm grant <package> android.permission.CAMERA
  ```

---

## Conexión Inalámbrica (ADB over Wi-Fi)

1. Conectar dispositivo por USB temporalmente.
2. Habilitar puerto TCP:
   ```bash
   adb tcpip 5555
   ```
3. Desconectar cable USB y conectar por IP local:
   ```bash
   adb connect 192.168.1.X:5555
   ```
4. Para desconectar:
   ```bash
   adb disconnect
   ```
