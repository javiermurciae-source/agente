# Memoria de Trabajo del Agente

Registro cronológico de criterios, preferencias, correcciones y acuerdos de trabajo con Camilo.

---

## 📌 Criterios y Preferencias Consolidadas

1. **Trato y Género**:
   - Camilo es HOMBRE. Utilizar siempre formas gramaticales masculinas (*tranquilo, listo, contento, estimado*). Nunca femenino.
2. **Estilo Operativo**:
   - Alta autonomía y ejecución proactiva: resolver directamente las tareas técnicas sin pedir confirmación innecesaria en cada paso obvio.
   - Cero rodeos burocráticos: responder con la solución concreta y el entregable listo.
3. **Manejo de Credenciales y Negocio**:
   - Jamás inventar credenciales de clientes, fechas de corte ni datos transaccionales. Si falta un parámetro, aplicar la **Regla 1**: preguntar antes de inventar.
   - Para reportes de cortes y vencimientos, usar siempre el formato desglosado con la plantilla corporativa azul de Stream Zone.
4. **Entorno de Trabajo Exclusivo (PC Linux)**:
   - **Regla estricta**: Ignorar por completo cualquier componente de Termux, Android, Shizuku, Termux Launcher o Nix-on-Droid. 
   - El agente opera de forma 100% nativa en Linux (CachyOS x86_64, Wayland/Niri, Kitty, PipeWire, `pacman`/`yay`).
   - **Herramientas descartadas**: NO usar `chafa` ni `notify-send` (en Niri con config propia no se usa demonio de notificación).
   - **Modo de Voz Conmutable (A Demanda)**:
     - Por defecto: Respuestas en texto en terminal.
     - **Activación de Voz**: Cuando Camilo diga *"habla"*, *"háblame"*, *"activa la voz"*, *"modo voz"*, *"por qué no hablas"*, el agente activa la salida por voz con `hablar "<texto>"`.
     - **Desactivación de Voz (Modo Silencio)**: Cuando Camilo diga *"silencio"*, *"no hables"*, *"modo silencio"*, *"calla"*, el agente responde exclusivamente en texto silencioso.
5. **Descargas Extremas Multi-hilo**:
   - Emplear siempre la skill `descargas-aria2-turbo`: resolver enlaces directos antes de invocar `aria2c`, usar `--file-allocation=falloc`, `--disk-cache=128M` y User-Agent de navegador para evitar cuellos de botella y bloqueos 403.
6. **Control de Ventanas Niri y Gaming**:
   - Hardware de referencia guardado en `contexto/hardware-pc.md` (ASUS TUF i5-12500H, RTX 3050 Laptop 4GB, 16GB RAM, pantalla 144Hz, btrfs).
   - Manipulación de ventanas programática mediante `niri msg action` (`focus-window`, `fullscreen-window`, `maximize-column`, etc.).
   - Rutas de juegos mapeadas: `~/juegos/pc` (Mortal Kombat 11 en Wine/UMU), `~/juegos/switch` (Zelda TotK, Smash Ultimate, Mario Kart 8, Dragon Ball FighterZ).
   - Emuladores de Switch: Eden en `~/.local/bin/eden` y Citron AppImage. Mando Sony PlayStation Wireless Controller.
7. **Web Scraping y Extracción Avanzada**:
   - Skill `web-scraping-automatizacion`: empleo obligatorio de `curl_cffi` con impersonación de navegador para saltar protecciones Cloudflare/TLS, y parseo ultrarrápido con BeautifulSoup4 sobre el parser `lxml`.
8. **Contactos y Grupos VIP de WhatsApp**:
   - Libreta local indexada en `~/.cache/contacts_cache.json` y `~/.cache/groups_cache.json`.
   - Grupo Distribuidores: `Distribuidores Stream Zone 🔥` (`120363425211205411@g.us`).
   - Contactos VIP: Stream Zone Oficial (+573114668309), Aleja (+573212159428), Guatemala (+50241028869), Black (+51905984023), Shadow (+573138188007), Erick (+573124421326).
9. **Informes Académicos IEEE (UNISANGIL)**:
   - Skill `reversing-clonacion-docx-ieee`: Deconstrucción y compilación de documentos `.docx` con plantilla oficial IEEE de 2 columnas (Times New Roman, espaciado 258 dxa).
   - Autores estándar: Bernal, Dana., Reyes, Andrey y Murcia, Camilo.
   - Filiación: Fundación Universitaria de San Gil (UNISANGIL), Comunicación de Datos, San Gil, Colombia.
   - Generador automatizado: `ieee_doc_builder.py` para generar reportes en segundos sin desajustes de formato.

---

## ⏱️ Historial Cronológico de Aprendizaje

### [2026-10-04] - Configuración Inicial y Estructuración del Agente
- **Evento**: Camilo instruyó reorganizar todo el conocimiento del agente bajo la metodología de 4 pilares (`contexto/`, `proyectos/`, `memoria/`, `skills/`) con el manual maestro `AGENTS.md`.
- **Acuerdo**: Se adoptan formalmente las dos reglas de oro:
  - *«Si te falta un dato, pregunta en vez de inventar.»*
  - *«Apunta por tu cuenta todo lo que te convenga recordar.»*
- **Entorno**: Se define con firmeza ignorar todo lo referente a Termux/Android; la estación de trabajo y todas las soluciones se ejecutan de manera nativa en Linux PC.
- **Skill Integrada**: Camilo adjuntó la guía de máximo nivel `GUIA_ARIA2_OPENCODE.txt`, convirtiéndose en la skill oficial `descargas-aria2-turbo` con extractor de enlaces directos automatizado.
- **Hardware y Gaming**: Se capturó y archivó el reporte completo de Fastfetch en `contexto/hardware-pc.md` y se creó la skill `control-ventanas-niri-gaming` con helper CLI para Niri IPC y emuladores.

### [2026-10-04] - Regla de Vencimientos y Despacho Oficial a Stream Zone
- **Regla Operativa Registrada**: Cada vez que Camilo diga *"vencimientos"* o solicite cortes, el agente debe generar de inmediato el libro Excel resumen con la plantilla corporativa oficial de 12 columnas utilizando el comando `sz-expiries`.
- **Contacto Stream Zone Oficial**: Confirmado y fijado en `+573114668309` (3114668309).
- **Acción Ejecutada**:
  - Se creó el comando oficial `sz-expiries` en `~/.local/bin/sz-expiries`.
  - Se consultaron todas las licencias de NuVlyx para el mes de octubre de 2026 (190 registros de corte, 146 órdenes).
  - Se descargaron las credenciales de acceso de forma concurrente y se cruzaron los números telefónicos y nombres de clientes.
  - Se generó el archivo `~/StreamZone/proyectos/corte_2026_10/reporte_vencimientos_2026_10.xlsx`.
  - Se despachó por WhatsApp con `wasend` a **Stream Zone Oficial** (+573114668309) con el formato estructurado de agente autónomo.

### [2026-10-04] - Optimización Turbo y Pipeline Unificado de Vencimientos
- **Retroalimentación de Camilo**: Máxima velocidad, agilidad y cero fricción en la ejecución.
- **Mejoras Implementadas**:
  - `sz-expiries` actualizado con HTTP Keep-Alive connection pooling (35 conexiones), 25 hilos concurrentes y caché local de catálogo en `~/.cache/sz_products_cache.json`.
  - Integración nativa de banderas `--view` (apertura y foco instantáneo en WPS) y `--wa <contacto>` (despacho directo por WhatsApp) en un solo proceso.
  - Creado el comando `vencimientos` en `~/.local/bin/vencimientos`: compila el mes, despacha a Stream Zone Oficial y abre en WPS en una sola llamada sin pausas intermedias.
  - Creado el visor ultrarrápido `viewxls` en `~/.local/bin/viewxls`: abre cualquier archivo `.xlsx` en WPS Spreadsheets y lo enfoca en Niri en menos de 400 milisegundos.

### [2026-10-04] - Filtro Estricto de Vencimientos Próximos (Máximo 4 Días)
- **Criterio de Negocio fijado por Camilo**: Los reportes de vencimientos habituales deben extraer únicamente las suscripciones con fecha de corte de **máximo 4 días** desde hoy (0 a 4 días restantes, además de vencidos recientes).
- **Implementación**:
  - Parámetro por defecto en `sz-expiries`: `--days 4` (24 registros urgentes detectados).
  - Filtrado previo a la descarga de credenciales para procesar el lote completo en menos de 4 segundos.
  - Archivo generado y enviado por WhatsApp a Stream Zone Oficial: `reporte_vencimientos_4_dias.xlsx`.

### [2026-10-06] - Preferencia de Modo Silencioso (Cero Voz)
- **Instrucción de Camilo**: "no hbles please".
- **Acuerdo**: Queda totalmente desactivada la salida por síntesis de voz / TTS (`hablar` / `say`). Todas las comunicaciones se mantienen estrictamente por texto silencioso en consola.

### [2026-10-06] - Evolución de PocketController a Aplicación Gráfica (GUI Nativa)
- **Instrucción de Camilo**: Pasar el sistema de control virtual desde script a aplicación GUI.
- **Implementación**:
  - Aplicación de escritorio nativa en GTK4 y Libadwaita (`pocket_gui.py`) en `~/Proyectos/PocketController/`.
  - Motor backend desacoplado e hilo-seguro (`pocket_backend.py`) con UInput Xbox 360 pad para hasta 4 jugadores simultáneos.
  - Generador dinámico de códigos QR con `qrencode` para enlace Wi-Fi local y Tailscale VPN (para amigos a distancia).
  - Probador interactivo de control real completo (Xbox 360) con visualización de ejes 2D en Cairo, gatillos progresivos y auto-test.
  - Integración en el sistema con ejecutable `pocketcontroller` en `~/.local/bin/` y lanzador `.desktop` con icono SVG.

### [2026-10-06] - APK Android con Escáner QR Integrado y Cero IPs Fijas
- **Instrucción de Camilo**: Eliminar IP fija de la APK y hacer que solicite código QR al abrir.
- **Implementación**:
  - Se eliminó la IP fija hardcodeada. Ahora la APK abre directamente la pantalla de escáner de cámara.
  - Se integró lector de QR ultrarrápido y offline con `jsQR` en WebView con permisos nativos de cámara.
  - Al apuntar la cámara a la pantalla del PC (donde la GUI muestra el QR), detecta la URL al instante, vibra y conecta el gamepad.
  - Se añadió botón permanente «📷 QR» en la barra del mando para cambiar de red/PC en 1 toque.
  - APK compilada y firmada en `~/Proyectos/PocketController/PocketController.apk` (82 KB).

### [2026-10-06] - Reorganización Operativa a ~/agente/
- **Instrucción de Camilo**: Mover todo el sistema del agente a una carpeta unificada en home llamada `agente`.
- **Implementación**:
  - Creado `/home/rootkit/agente/`.
  - Reubicados: `contexto/`, `memoria/`, `skills/`, `tools/`, `bin/`, `scripts/`, `templates/`, `dotfiles/`, `docs/`, `AGENTS.md` y `GEMINI.md`.

### [2026-10-06] - Modo de Voz Dinámico y Conmutable (A Demanda)
- **Instrucción de Camilo**: Habilitar el modo de voz para activarse o desactivarse dinámicamente cuando él lo pida.
- **Implementación**:
  - Se configuró la regla dinámica: cuando Camilo solicite que hable (*"habla"*, *"modo voz"*, *"¿por qué no hablas?"*, *"háblame"*), el agente ejecuta la síntesis por voz (`hablar`).
  - Cuando pida silencio (*"modo silencio"*, *"no hables"*, *"calla"*), se mantiene en texto silencioso en consola.

### [2026-10-06] - Pipeline Turbo Unificado de Vencimientos (Cero Esperas)
- **Instrucción de Camilo**: El flujo debe ser ultrarrápido y completarse de una sola vez sin pasos intermedios ni demoras.
- **Implementación**:
  - Paginación concurrente: `sz-expiries` ahora consulta todas las páginas de licencias y credenciales con hilos paralelos (10 y 16 workers), reduciendo el tiempo de generación de 73s a **3.60s** (20x más rápido).
  - Auto-login transparente: si el token de NuVlyx vence (401), se renueva automáticamente sin abortar.
  - Flujo unificado 100%: `vencimientos` ahora tiene la notificación a clientes activa por defecto (`NOTIFY=1`), ejecutando generación, envío a Stream Zone Oficial, despacho a cada cliente y aviso a distribuidores en un solo llamado continuo.
  - Retardo anti-ban acelerado a 2.8s en `sz-notify`, reduciendo el tiempo de despacho a la mitad sin riesgo de bloqueo.

### [2026-10-06] - Skill de Reversing y Clonación de Informes IEEE (.docx)
- **Instrucción de Camilo**: Aprender a replicar archivos al gusto mediante reversing a partir de los documentos de Descargas.
- **Implementación**:
  - Se analizaron los informes de Comunicación de Datos de UNISANGIL (`Laboratorio1_Configuracion_Basica_Router_Switch_IEEE.docx`, `Laboratorio1_IEEE_corregido.docx` y `Laboratorio2_Switch_Conectividad_IEEE.docx`).
  - Se creó la skill `reversing-clonacion-docx-ieee` con:
    - `docx_extractor.py`: Analizador de ingeniería inversa OpenXML (secciones, columnas, estilos, tablas, medios).
    - `ieee_doc_builder.py`: Generador y clonador de alta fidelidad que produce documentos Word en 2 columnas con tipografía y formateo IEEE exactos en menos de 1 segundo.
    - Plantilla base esterilizada `ieee_template_unisangil.docx`.

### [2026-10-06] - Despacho de Cuenta HBO Max Platino a Erick
- **Instrucción de Camilo**: Buscar una cuenta HBO disponible (preferiblemente Platino), extraer correo, contraseña, perfil y PIN, despacharla a Erick por WhatsApp indicando el valor de $12.000 COP e instrucciones de uso.
- **Implementación**:
  - Se consultó el catálogo e inventario en NuVlyx API; se identificó disponibilidad en `HBO MAX PLATINO PANTALLA` (variación 1 mes, stock de 5 cuentas).
  - Se extrajeron las credenciales de la primera licencia disponible: `Cristian2390@streamzone.one`, clave `Stream_Zone*1`, Perfil 1, PIN `9654`.
  - Camilo suministró el número telefónico de Erick (`3124421326` / `+573124421326`).
  - Se despachó el mensaje oficial estructurado vía `wasend` exitosamente.
  - Se indexó a Erick permanentemente en `~/.cache/contacts_cache.json` y en este registro maestro para futuros envíos directos sin requerir consulta previa.

### [2026-10-06] - Despacho de Nueva Cuenta HBO a Erick
- **Instrucción de Camilo**: Buscar una cuenta HBO nueva/disponible (del inventario de HBO Estándar), presentarla simplemente como "HBO" (sin especificar estándar o platino) y enviarla a Erick por WhatsApp con sus datos de acceso.
- **Implementación**:
  - Se consultó el inventario de `HBO MAX ESTÁNDAR PANTALLA` (variación 1 mes, stock de 20 cuentas disponibles).
  - Se extrajeron las credenciales de la licencia disponible: `hboestandar03@streamzone.one`, contraseña `Stream_Zone_1`, Perfil 1, PIN `2541`.
  - Se redactó el mensaje indicando el servicio como *HBO (Pantalla)* de manera directa y cordial, sin términos técnicos.
  - Se despachó por WhatsApp con `wasend` a Erick (+573124421326) con éxito (ID `3EB0E4DD7CF514D9A3046A`).

### [2026-10-08] - Confirmación de Modo Silencioso
- **Instrucción de Camilo**: Confirmar que el agente está en modo silencioso.
- **Estado**: Modo silencioso activo (cero síntesis de voz / TTS). Todas las respuestas se emiten exclusivamente por texto en consola.

### [2026-10-08] - Proyecto SecureDesk: Autor de las Actas de Reunión
- **Preferencia fijada por Camilo**: En todas las actas de reunión de SecureDesk, el **Autor** debe ser SIEMPRE el Consultor de Ciberseguridad (Especialista SOC): **kevin Mitnick**.

### [2026-10-08] - Despacho de Pantalla Disney ESPN a Aleja
- **Instrucción de Camilo**: Buscar el servicio activo de Disney ESPN en la tienda/API y enviarle una pantalla a Aleja (3212159428).
- **Implementación**:
  - Se consultó el catálogo e inventario en NuVlyx API; se identificó el producto activo `Disney Premium 7 ESPN - Pantalla` (`32bfa3ad-8937-40c8-9e8c-44a79a65e3db`).
  - Se extrajeron las credenciales de la licencia disponible (Perfil 2): `carlos123@streamzone.one`, clave `Stream_Zone*1`, Perfil 2, PIN `1459`.
  - Se despachó el mensaje oficial estructurado vía `wasend` a Aleja (+573212159428) con éxito (ID `3EB04D22997C611BA6EB11`).

### [2026-10-09] - Respaldo Integral del Agente en Git y Script de Recuperación
- **Instrucción de Camilo**: Revisar cómo funciona el agente en sí y subirlo a Git para poder recuperarlo rápidamente en caso de contingencia.
- **Implementación**:
  - Se estructuró el repositorio Git en `/home/rootkit/agente/` con configuración de seguridad estricta en `.gitignore` (exclusión de `node_modules`, cachés y sesiones sensibles).
  - Se creó el script maestro de restauración `install.sh` que enlaza automáticamente todos los binarios a `~/.local/bin/`, otorga permisos y restaura dependencias de Baileys/Wasend.
  - Se creó la documentación unificada en `README.md`.
  - Se sincronizó y publicó el repositorio privado en GitHub: `https://github.com/javiermurciae-source/agente`.

### [2026-10-09] - Reestructuración de Particiones NVMe y Aislamiento de Juegos en Btrfs
- **Instrucción de Camilo**: Preparar el sistema para formatear CachyOS salvando los juegos en una partición dedicada limpia (sin home viejo ni basura).
- **Implementación**:
  - **Eliminación de Windows**: Se eliminaron las particiones `/dev/nvme0n1p3` (16 MB Microsoft) y `/dev/nvme0n1p4` (150 GB Windows NTFS).
  - **Partición del Nuevo Sistema**: Se creó `/dev/nvme0n1p3` (150 GB Btrfs, etiqueta `cachyos_new`, UUID `f8895ace-b6f6-49cc-a1c4-97fb66ca00e3`) para instalar y formatear el nuevo CachyOS.
  - **Partición Dedicada de Juegos**: En `/dev/nvme0n1p2` (326 GB Btrfs, etiqueta `JUEGOS`) se creó el subvolumen aislado `@juegos` y se estableció como el subvolumen por defecto (`btrfs subvolume set-default`).
  - **Estructura Limpia de Juegos y Proyectos**: Dentro de `@juegos` residen físicamente:
    - `pc/Mortal Kombat 11` (110 GB)
    - `switch/` (57 GB: Super Smash Bros Ultimate, Zelda TotK, Mario Kart 8 Deluxe, DBZ FighterZ)
    - `emuladores/` (Eden.AppImage)
    - `proyectos/` (PocketController con APK, NouTube, etc.)
  - Al montar `/dev/nvme0n1p2` en el nuevo CachyOS, se accede directamente a los juegos y proyectos de forma 100% aislada, sin mostrar `@`, `@home` ni restos del sistema anterior.




