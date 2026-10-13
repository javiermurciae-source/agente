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
   - **Apertura de Archivos**: Cero complicaciones con visores específicos; usar siempre directamente `xdg-open <archivo>` para abrir con la aplicación por defecto del sistema.
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
    - `wallpapers/` (fondos animados MP4 y wallpapers de anime/Catppuccin y Serpantinum)
    - `agente/` (sistema completo del agente listo para restaurar)
  - Al montar `/dev/nvme0n1p2` en el nuevo CachyOS, se accede directamente a los juegos, proyectos, wallpapers y agente de forma 100% aislada, sin mostrar `@`, `@home` ni restos del sistema anterior.


### [2026-10-09] - Unificación Total del Disco y Restauración de Juegos en ~/
- **Instrucción de Camilo**: Mover el backup de juegos para tenerlo normal en el sistema y dejar todo el disco normal sin particiones secundarias.
- **Implementación**:
  - **Limpieza de Subvolúmenes Antiguos**: Se rescataron los documentos académicos IEEE y configuraciones a `Descargas/` y `Documentos/`, y se eliminaron los subvolúmenes obsoletos del viejo sistema en `p2`.
  - **Migración Quirúrgica de CachyOS**: Se clonaron los subvolúmenes limpios (`@`, `@home`, `@root`, `@srv`, `@cache`, `@tmp`, `@log`) desde `p4` hacia `p2` mediante `btrfs send / receive`.
  - **Restauración Instantánea en ~/': Se movieron directamente las carpetas de juegos (`~/juegos/pc`, `~/juegos/switch`, `~/juegos/emuladores`), proyectos (`~/Proyectos`), wallpapers (`~/wallpapers`) y el agente (`~/agente`) dentro de `/home/rootkit/`. Al ser dentro del mismo filesystem Btrfs de `p2`, el movimiento fue inmediato.
  - **Reconfiguración de Fstab y GRUB**: Se actualizó `/etc/fstab` con el UUID de `p2` (`03b4d0e0-7726-4a18-8599-4e7cfb375675`) y se reinstaló GRUB en EFI apuntando nativamente a `(,gpt2)` (`grubx64.efi`).
  - **Eliminación de Partición 3**: Se removió la partición `p3` (75 GB) no utilizada.
  - **Servicio Automatizado de Unificación**: Se preparó el script y servicio `unify-disk.service` para ejecutarse en el siguiente arranque de `p2`: eliminará `p4`, expandirá `p2` al 100% del SSD (~476 GB), redimensionará Btrfs al máximo y se autoeliminará.

### [2026-10-10] - Personalización de Ambxst Shell (Barra Ultra-Fina y Fondos de Video)
- **Instrucción de Camilo**: Reparar reproducción de fondos animados (.mp4/.mov), evitar que la barra superior se auto-oculte y hacer la barra mucho más delgada y fina.
- **Implementación**:
  - **Fondos de Video en Qt 6**: Corregida ruta absoluta en `~/.cache/ambxst/wallpapers.json` y resuelto TypeError en `VideoWallpaper.qml` (`player.position = 0` en vez de `player.seek(0)` no soportado en Qt 6).
  - **Fijación Permanente de Barra**: Modificado `BarContent.qml` para que al estar fijada (`pinned`) no se oculte ante ventanas de ancho completo en Niri.
  - **Barra Ultra-Fina (20px)**:
    - En `config/defaults/bar.js` y `~/.config/ambxst/config/bar.json` se configuró `"height": 20` y `"launcherIconSize": 14`.
    - Ajustado `BarContent.qml` para respetar estrictamente `Config.bar.height`.
    - Modificado `BarBg.qml`: padding a 1px y margen exterior a 0px para dejarla al ras del borde superior sin espacios flotantes.
    - Escalado responsivo y micro-padding dinámico en `Workspaces.qml`, `Clock.qml`, `SysTray.qml`, `SysTrayItem.qml`, `ToggleButton.qml`, `ControlsButton.qml`, `BatteryIndicator.qml` y `LayoutSelectorButton.qml` evitando cortes o textos desbordados.
  - **Eliminación de Iconos de Apps Abiertas y Botón Pin**:
    - Se desactivó `"showPinButton": false` en `~/.config/ambxst/config/bar.json` eliminando el botón de fijar.
    - Se configuró `"showAppIcons": false` y `"showNumbers": true` en `~/.config/ambxst/config/workspaces.json` para que la barra superior no muestre los iconos de las ventanas abiertas (evitando duplicar lo que ya muestra el dock inferior), mostrando en su lugar números limpios de escritorios.
    - Se agregó soporte modular para `showWorkspaces` y `showLayoutSelector` en `config/defaults/bar.js` y `BarContent.qml`.
  - Se sincronizaron los cambios en `~/.local/src/ambxst` y en el repositorio `/home/rootkit/agente/Ambxst`.

### [2026-10-10] - Acceso Directo de Terminal Kitty en Niri
- **Instrucción de Camilo**: "kitty ponlo win + enter para abrir".
- **Implementación**:
  - En `~/.config/niri/config.kdl` se añadió el atajo `Mod+Return { spawn "kitty"; }` (Win + Enter) y se actualizó `Mod+T` a Kitty.
  - Se validó la sintaxis con `niri validate` y se recargó la configuración en vivo con `niri msg action load-config-file`.

### [2026-10-10] - Sincronización Dinámica de Colores de Fondo con Kitty
- **Instrucción de Camilo**: "ayudame a que se vincule con los coleres de fondo".
- **Implementación**:
  - Se creó `~/.config/kitty/kitty.conf` incluyendo la paleta generada dinámicamente por Ambxst (`include ~/.cache/ambxst/kitty.conf`), con tipografía monospace, opacidad 0.90 y shell Fish.
  - Al cambiar de fondo de pantalla (o video wallpaper), Ambxst (`matugen` + `KittyGenerator.qml`) actualiza la paleta en tiempo real y emite `SIGUSR1` para recargar Kitty automáticamente sin reiniciar el terminal.

### [2026-10-11] - Compilación e Instalación Exitosa de aria2-fast
- **Instrucción de Camilo**: "ayudame ainstalar aria2fast".
- **Diagnóstico y Solución**:
  - El paquete AUR de `aria2-fast` fallaba al compilar debido al salto a Nettle 4 en CachyOS/Arch (`nettle 4.0`), cambiando la firma de `hash->digest` en `LibnettleMessageDigestImpl.cc`.
  - Se integró `nettle-4.patch` en `~/.cache/yay/aria2-fast/`, se ajustaron las dependencias en `PKGBUILD` y se compiló limpio en paralelo con los 16 núcleos.
  - Instalado satisfactoriamente `aria2-fast 1.37.0-3` (`/usr/bin/aria2c`).
  - Verificado: parámetro `-x` (`--max-connection-per-server`) deslimitado a `1-*` (listo para 128 conexiones simultáneas).

### [2026-10-11] - CLI Autónomo de Consulta del Campus Virtual UNAD
- **Instrucción de Camilo**: Construir un CLI para que el agente pueda ver, leer y consultar cursos y actividades del Campus UNAD sin fricción de DevTools ni cookies manuales.
- **Implementación**:
  - Se creó un entorno virtual aislado en `~/.local/share/unad-env` con Playwright integrado directamente sobre el Chrome nativo del sistema (`/opt/google/chrome/chrome`).
  - Se desarrolló el CLI maestro en `scripts/unad_cli.py` con perfil de sesión persistente en `~/.config/unad-session`.
  - Creado el binario y wrapper en `bin/unad` y enlazado a `~/.local/bin/unad`.
  - Arquitectura desacoplada: Playwright se usa exclusivamente en `unad login` en segundo plano para aprobar ubicación y succionar cookies a `cookies.json`. A partir de ahí, **todo se ejecuta mediante peticiones HTTP 100% humanas con `requests` y headers de navegador real**.
  - Flujo de ingeniería inversa Moodle descubierto:
    - `miscursos.php` lista asignaturas con periodo `2204`.
    - Botón `redirmd(periodo, nav, curso, aula)` genera token SSO dinámico en `redirmd.php`.
    - Auto-POST a Moodle (`https://campus146.unad.edu.co/ses108/login/index.php` o `campus151`) abre directamente el aula virtual sin intervención.
  - Comandos integrados:
    - `unad login`: login autónomo directo sin 2FA y captura de cookies en 2 segundos.
    - `unad cursos`: lista las 5 asignaturas matriculadas con sus códigos oficiales.
    - `unad tareas`: extrae la agenda de actividades pendientes, fechas de corte (alerta si vence hoy) y puntajes.
    - `unad notas`: extrae el historial de notas y calificaciones de retos/fases.
    - `unad momentos <curso>`: desglosa la estructura pedagógica en Momento Inicial, Intermedio y Final, listando guías, bibliografías, OVI, foros y entregas.
    - `unad biblio <curso> [fase]`: extrae referencias bibliográficas exactas, libros, páginas sugeridas, DOIs y enlaces de lectura.
    - `unad descargar <curso> [fase]`: descarga automática de guías PDF y anexos DOCX/ZIP organizados en `~/Documentos/UNAD/<curso>/<fase>/`.
    - `unad leer-guia <pdf|query>`: extracción y lectura en consola del objetivo, entregables y rúbricas de la guía.
    - `unad correo <curso> [id]`: consulta del correo interno de docentes en Moodle (`local/mail`), listando y leyendo mensajes completos vía AJAX.
    - `unad curl`: generador de llamadas `curl` humanas inyectadas con la cookie.

### [2026-10-11] - Ingeniería Inversa de Mensajería Moodle y Resolución de Fase 2 (Alpina S.A.S.)
- **Instrucción de Camilo**: Inspeccionar el correo de los profesores en el campus (`local/mail/view.php?t=inbox&c=91`), enterarse de lo que piden para Fase 2 de Teoría de Sistemas en las Organizaciones (204016) y continuar la resolución.
- **Implementación**:
  - **Ingeniería Inversa de Moodle Mail**:
    - Se identificó la SPA de Svelte en Moodle comunicándose con el endpoint AJAX `/lib/ajax/service.php?sesskey=<sesskey>`.
    - Integrado en `unad_cli.py`: llamadas a `local_mail_search_messages` (búsqueda de correos por `courseid` con filtros de rol) y `local_mail_get_message` (extracción de cuerpo en HTML limpio).
    - Creado el comando `unad correo 204016` (buzón) y `unad correo 204016 <id>` (lectura completa).
  - **Hallazgos Clave de los Docentes**:
    - Mensajes de Tutor Paola Rincón (#41854) y Director Jorge Ramírez (#36549): Exigen explícitamente retomar la organización de la Fase 1, aplicar los 6 estadios de Checkland, conectar con los ODS y citar el OVA de González (2023).
    - Se descubrió en Moodle que en Fase 1 la estudiante trabajó **Alpina Productos Alimenticios S.A.S.** (documento descargado: `Analisis_Sistemico_Alpina_SAS_yeiny_suarez_2.pdf`).
  - **Construcción y Resolución Integral de Fase 2**:
    - **Generación de Diagramas de Alta Resolución (300 DPI)**: Creado `scripts/generate_diagrams.py` para generar `estadio1_diagrama.png` (Reconocimiento del problema con actores, causas, síntomas, consecuencias y ODS 12/9) y `estadio3_modelo_conceptual.png` (Modelo conceptual con 6 actividades en infinitivo y bucle de control de Peter Checkland - 3 Es: Eficacia, Eficiencia, Efectividad).
    - **Diligenciamiento de Plantilla Oficial UNAD**: Desarrollado `scripts/build_fase2_document.py` para poblar `Anexo_Fase_2.docx`:
      - Portada con datos oficiales de Yeiny Alejandra Suarez Rodriguez (1003882193), Grupo 346, Tutora Paola Rincón.
      - Introducción (190 palabras) de alta densidad académica.
      - Caracterización profunda de Alpina S.A.S. (Sopó, agroindustria, sistema abierto).
      - Texto argumentativo (2 párrafos) vinculando la problemática de frío y empaques con ODS 12 (Metas 12.3 y 12.5) y ODS 9 (Meta 9.4) desde la Ingeniería de Sistemas.
      - Estadio 1 con imagen de diagrama insertada y desglose analítico.
      - Estadio 2 con Tabla 1 (CATWOE completo) y Definición Raíz formal (P-Q-R).
      - Estadio 3 con diagrama conceptual insertado y explicación de actividades y 3 Es.
      - Estadio 4 con Tabla 2 comparativa (situación actual vs propuesta vs oportunidades).
      - Estadio 5 con Tabla 3 (4 cambios factibles y deseables multidimensionales).
      - Estadio 6 con Tabla 4 (Plan de acción con responsables, recursos, tiempos y fórmulas de KPIs).
      - Conclusiones (4 conclusiones académicas estructuradas).
      - Referencias bibliográficas en formato APA 7.
    - **Exportación Dual Impecable**:
      - Word: `~/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.docx` (1.1 MB).
      - PDF: `~/Documentos/UNAD/204016_Sistemas/Fase_2/Anexo_Fase_2_Yeiny_Suarez.pdf` (1.1 MB, 10 páginas con maquetación académica limpia generada vía Chromium).

### [2026-10-11] - Purga Radical de Wrappers Residuales de Android/Termux y Restauración de Sudo y Yay
- **Problema Reportado por Camilo**:
  - Al ejecutar `yay -Syy wps-office`, el sistema fallaba con:
    `/home/rootkit/.local/bin/sudo: línea 2: /home/rootkit/bin/rish: No existe el fichero o el directorio -> error refrescando las bases de datos - exit status 127`
- **Causa Raíz Identificada**:
  - En una sesión anterior o al enlazar binarios, se ejecutó `ln -s /home/rootkit/agente/bin/* ~/.local/bin/`.
  - La carpeta `agente/bin/` conservaba scripts heredados del antiguo entorno de teléfono (Termux/Nix-on-Droid/Shizuku): `sudo`, `su`, `fastfetch`, `rish`, `rish_shizuku.dex`, `termux-open`, `viewpic`, `wafind`, `waget`, `wasend`, `freebuff`, `hotspot`, `keelcode`, `agy`, `cline`.
  - Como `~/.local/bin` tiene precedencia en `$PATH` sobre `/usr/bin`, `/home/rootkit/.local/bin/sudo` ensombrecía al binario real del sistema `/usr/bin/sudo`, ejecutando `rish` e impidiendo cualquier operación de privilegios y gestión de paquetes con `yay` o `pacman`.
- **Acción Quirúrgica de Limpieza**:
  - Se eliminaron todos los enlaces simbólicos de wrappers obsoletos en `~/.local/bin/` (`sudo`, `su`, `fastfetch`, `agy`, `cline`, `freebuff`, `hotspot`, `keelcode`, `rish`, `rish_shizuku.dex`, `termux-open`, `viewpic`, `wafind`).
  - Se purgaron definitivamente esos scripts de `agente/bin/`.
  - Se actualizaron `wasend` y `waget` para usar rutas locales y nativas de Linux (`bun $HOME/agente/tools/wasend/wasend.mjs`).
  - Se verificó el funcionamiento de `/usr/bin/sudo` (Sudo 1.9.17p2 funcionando al 100%) y de `/usr/bin/yay`.
  - **Restauración del Binario de `agy`**:
    - El ejecutable nativo de `agy` (205 MB ELF) residía originalmente en `~/.local/bin/agy`, pero había sido sobrescrito por el symlink erróneo hacia `agente/bin/agy`.
    - Al purgar el symlink erróneo, el comando no aparecía en PATH.
    - Se recuperó quirúrgicamente el binario exacto e intacto desde `/proc/21582/exe` (proceso en ejecución) directamente a `/home/rootkit/.local/bin/agy`.
    - Verificado y operativo en Fish: `agy --version` -> `1.3.3`.

### [2026-10-11] - Formato Pregunta – Respuesta para Entregas UNAD y Cero Relleno de Plantilla
- **Preferencia fijada por Camilo**:
  - Para los trabajos de la UNAD (Fase 2 de Teoría de Sistemas en las Organizaciones y similares):
  - **Cero texto de plantilla o relleno innecesario**: Eliminar por completo instrucciones ("Instrucciones: ...", "Incluya...", "Debe expresar..."), abstracts en inglés, tablas de contenido o listas de figuras/tablas si la guía no las pide expresamente.
  - **Formato Pregunta – Respuesta directo**: Formular cada requerimiento de la guía como una pregunta clara y responder puntualmente con rigor conceptual.
  - **Diagramas sí incluidos**: En las secciones que correspondan a diagramas (Estadio 1 y Estadio 3), insertar las figuras en alta resolución con sus respectivas notas explicativas.
  - **Generación y Apertura Instantánea**: Compilar tanto en `.docx` como en `.pdf` y abrir automáticamente en WPS Writer enfocado en Niri.

### [2026-10-11] - Canon de Reglas Inquebrantables de Escritura Humana (StoryScope - arXiv:2604.03136)
- **Instrucción de Camilo**: Analizar el paper `https://arxiv.org/pdf/2604.03136` (*StoryScope: Investigating idiosyncrasies in AI fiction* - Russell et al., COLM 2026) y adoptar cada hallazgo científico de la brecha IA vs. Humano como una regla inquebrantable de redacción.
- **Criterio de Redacción Incorporado**:
  - **1. Prohibido Sobre-explicar la Temática**: Jamás permitir que el narrador o personajes discursen la moraleja o lección aprendida. El subtexto manda; la IA moraliza en 77%, el humano confía en el lector.
  - **2. Subvertir la Linealidad Temporal y Causal**: Evitar relatos planos de A a B. Usar anacronías, saltos temporales, analepsis que fuercen recontextualización retrospectiva y tramas no lineales.
  - **3. Freno a la Hiper-somatización Emocional**: No abusar de metáforas viscerales (pechos oprimidos, nudos en garganta, olores insistentes). Nombrar emociones directamente o mostrarlas en conductas secas y silencios.
  - **4. Anclaje en el Mundo Real e Intertextualidad Directa**: Citar obras, autores, marcas, lugares y referentes culturales reales sin miedo. Romper el aislamiento genérico de la IA.
  - **5. Ambigüedad Moral y Finales con Aristas**: Prohibido arcos de redención pulcros o resoluciones de pura "aceptación interna". Mantener contradicciones humanas y finales que dejen preguntas.
  - **6. Subtramas y Densidad Dialogal**: Integrar subtramas paralelas que contrasten con la trama principal; mayor proporción de diálogo frente a monólogos narrativos.
  - **7. Neutralización de Sesgos por Modelo**: Neutralizar la frialdad plana de Claude, el chisme/rumor obsesivo de GPT, los finales ultra-ordenados y atmósfera 100% lúgubre de Gemini, y el front-loading de backstory de DeepSeek.

### [2026-10-11] - Generación del Documento Fase 2 con Skill Anti-Slop (Formato Test / Pregunta-Respuesta)
- **Solicitud de Camilo**: Generar un nuevo documento para la entrega de la Fase 2 (UNAD - 204016) aplicando rigurosamente la skill `escritura-humana-antislop` (StoryScope / arXiv:2604.03136) en formato tipo test (pregunta directa y respuesta sustentada), erradicando cualquier rastro de tono artificial ("adiós IA") y sin inventar datos.
- **Entregables Producidos**:
  - Script generador: `/home/rootkit/agente/scripts/build_antislop_fase2_document.py`
  - DOCX: `/home/rootkit/Descargas/Fase_2_Yeiny_Suarez_Antislop.docx` (y copia en `Documentos/UNAD/204016_Sistemas/Fase_2/`)
  - PDF: `/home/rootkit/Descargas/Fase_2_Yeiny_Suarez_Antislop.pdf` (10 páginas, maquetación limpia APA 7 con diagramas en alta resolución de Estadios 1 y 3)
  - Abierto directamente en WPS Writer para revisión inmediata.




### [2026-10-12] - Integración de Skills de Video Programático: HyperFrames y Remotion
- **Instrucción de Camilo**: Investigar e integrar las capacidades de generación programática de video (*Code-to-Video*) con HyperFrames y Remotion para el agente.
- **Implementación y Despliegue**:
  - Se instaló la suite completa de **HyperFrames** (21 skills de HeyGen) y de **Remotion** (12 skills oficiales) directamente en `agente/skills/` (reflejadas en `~/.agents/skills/`, `~/.gemini/config/skills/` y `skills/`).
  - **HyperFrames CLI** (`hyperframes v0.8.150` vía Node/NPX) operativo con comandos de previsualización en vivo (`preview`), renderizado a MP4/WebM (`render`), layouts GSAP, detección de beats, transcripción y TTS en local.
  - **Remotion Agent Skills** integradas para compilación y desarrollo en React/TypeScript con soporte de interpolaciones, secuencias y exportación de video.
  - Ambas herramientas quedan disponibles para creación de videos, intros, explicativos y motion graphics bajo demanda desde la terminal.

### [2026-10-12] - Creación de la Skill Maestra Motion Design Elite (Anti-Slop & Sound Design)
- **Instrucción de Camilo**: Investigar a fondo cómo hacer los mejores videos de movimiento eliminando por completo la estética básica de IA, dotando al agente de una habilidad de máximo nivel.
- **Hallazgos Clave y Canon de Estudio**:
  - *Autopsia del Slop de IA*: Se identificaron los vicios que hacen que un video se vea genérico (degradados de texto morado-cian, partículas flotantes sin masa, brillo excesivo, todo centrado sin jerarquía, falta de diseño de sonido o música desconectada).
  - *Los 6 Pilares Élite*:
    1. **Conector Visual Continuo**: Un único elemento u objeto que transporta el momento y viaja por toda la pieza sin transiciones arbitrarias.
    2. **Físicas de Forma Cerrada**: Ecuación analítica de oscilador armónico subamortiguado con sobreimpulso exacto (+22%).
    3. **Composición Suiza y Jerarquía Asimétrica**: Tres capas mínimas, anclaje a bordes, paleta austera con un único acento vibrante.
    4. **Diseño de Sonido Sample-Accurate**: Beat cuantizado a 120 BPM con foley háptico (clics, whooshes, chimes, sub-bass) sincronizado a nivel de fotograma.
    5. **Tipografía Cinética Intencional**: Plegado de caracteres, dispersión orbital y semitonos reactivos.
    6. **Determinismo 60 FPS**: Render puro desde $t$ con bucle perfecto (Seamless Loop).
- **Skill Integrada**: Creada formalmente la skill `motion-design-elite` en `skills/motion-design-elite/SKILL.md` como el estándar obligatorio para futuras producciones de video.

### [2026-10-12] - Web Scraping de Prompts Claude Opus 5.5 (YouMind)
- **Instrucción de Camilo**: Realizar web scraping a la web de prompts interesantes `https://youmind.com/es-419/opus-5-5-prompts`.
- **Implementación y Hallazgos**:
  - Empleo de la skill `web-scraping-automatizacion` con `curl_cffi` (impersonate `chrome120`) y BeautifulSoup con `lxml`.
  - **Ingeniería Inversa de Next.js Flight Stream**: La página utiliza React Server Components con chunks streaming `self.__next_f.push` y referencias indirectas `$ref` (`T<hex_length>`). Se construyó un decodificador y reensamblador que reconstruyó los textos completos de prompts sin truncamiento.
  - **Exploración y Crawling Profundo**: Se procesaron las páginas raíz, exploradores por vistas, me gusta y recientes, y se recorrieron 58 páginas de detalle para compilar un grafo de 61 prompts únicos.
  - **Entregables Generados en `~/Proyectos/youmind-opus-prompts/`**:
    - `prompts_opus_5_5.json` (105 KB): Metadatos completos (ID, autor, links de X/Twitter, URL directa de video MP4 en CDN, prompts en español y original).
    - `prompts_opus_5_5.xlsx` (24 KB): Libro Excel estilizado con plantilla corporativa azul, badges temáticos y enlaces a videos de demostración.
    - `prompts_opus_5_5.md` (97 KB, 1460 líneas): Catálogo estructurado por categorías (3D & WebGPU, Motion Systems, Workflows/HyperFrames, SVG Canvas, Promocional, etc.) con bloques de código listos para copiar y usar en Claude Opus.
  - **Script Automatizado**: Herramienta permanente en `/home/rootkit/agente/scripts/scrape_youmind_opus.py`.

### [2026-10-12] - Extracción Especializada de Diapositivas y Presentaciones IA (YouMind)
- **Instrucción de Camilo**: Investigar y extraer a fondo la parte de diapositivas (`slides` / presentaciones).
- **Hallazgos Clave**:
  - En YouMind coexisten dos motores principales de diapositivas:
    1. **GPT Image 2 Slides**: Generación visual 16:9 con 99% de fidelidad tipográfica, layouts de revista, render en paralelo de deck completo desde artículo/video/PDF y exportación a video con voz clonada. 8 plantillas maestras identificadas: *Year-End Report / Data Storytelling, Memphis Design Retro, Bold Visual Brochure, Kami Design (Papel recortado), Vibrant Handdrawn, Modern Digital, Brutalism y Neo-Brutalism*.
    2. **Presentaciones en Código (HTML Web Decks)**: Archivos únicos `index.html` autónomos con atajos de teclado, barras de progreso y componentes Apple/Notion para grabaciones y pitch decks.
  - Se identificaron y extrajeron 19 habilidades (Skills) especializadas de diapositivas (consultoría MBB/Bain con principio MECE y piramidal, neo-brutalismo para devs, pizarra verde cálida, informe académico de Wang Hong, etc.).
- **Entregables Generados en `~/Proyectos/youmind-slides-prompts/`**:
  - `diapositivas_ia_prompts.md` (20 KB): Guía maestra con las 8 plantillas, prompts base y desglose de las 19 habilidades.
  - `diapositivas_ia_prompts.xlsx` (12 KB): Libro Excel con enlaces clicables a YouMind y estilos visuales.
  - `diapositivas_ia_prompts.json` (56 KB): Dataset estructurado completo.
- **Script Automatizado**: `/home/rootkit/agente/scripts/scrape_slides_catalog.py`.

### [2026-10-12] - Consagración como Agente Creador y Arquitecto de Skills
- **Instrucción de Camilo**: «mira tu tarea es creador de skills un agente creador de skills».
- **Misión e Identidad Consagrada**:
  - El agente asume formalmente el rol primordial de **Creador y Arquitecto Autónomo de Skills (Skill Creator Agent)** para el ecosistema Antigravity / Gemini.
  - Su propósito central es deconstruir flujos complejos, APIs, librerías, papers científicos y necesidades operativas en habilidades modulares de alto rendimiento (`skills/<name>/SKILL.md`) con revelación progresiva (*Progressive Disclosure*), scripts ejecutables listos y cero slop.
- **Implementación y Herramientas Desplegadas**:
  - **Skill Maestra `creador-de-skills`**: Creada en `/home/rootkit/agente/skills/creador-de-skills/SKILL.md` estableciendo la anatomía estándar obligatoria (YAML Frontmatter con triggers precisos, reglas inquebrantables, procedimientos quirúrgicos y scripts auxiliares).
  - **Subagente Especializado `skill-creator`**: Registrado en el sistema mediante `define_subagent` con permisos completos de lectura, escritura y ejecución de comandos para investigar y empaquetar skills complejas en segundo plano.
  - **Herramientas CLI Nativas**:
    - `create-skill` (`bin/create-skill` -> `~/.local/bin/create-skill`): Generación instantánea de la estructura modular completa (`SKILL.md`, `scripts/`, `references/`, `examples/`).
    - `validate-skill` (`bin/validate-skill` -> `~/.local/bin/validate-skill`): Auditor automático de calidad y rendimiento (revisa YAML frontmatter, disparadores, sintaxis de scripts Python/Bash/Node, permisos `+x`, score anti-slop y sincronización).
  - **Estándar de Oro (100/100 Calidad)**: Verificado y aplicado con éxito en `creador-de-skills` y `motion-design-elite`.
  - **Manuales Actualizados**: Sincronizados `AGENTS.md` y `GEMINI.md` reflejando el rol de Creador de Skills.

### [2026-10-12] - Creación de la Skill Maestra y Plantilla Exacta de Presentaciones HTML (16:9)
- **Instrucción de Camilo**: «genial ahora quiero que mires todo lo que ves en la parte de presentaciones aprendas la skill y hagas plantilla exacta».
- **Ingeniería Inversa y Canon de Aprendizaje**:
  - Se analizó la arquitectura completa de presentaciones de YouMind (desde el generador de diapositivas en código `html-presentation` hasta los 8 estilos de `gpt-image-2-slides` y la estética de diapositivas de Wang Hong).
  - Se identificaron los requerimientos inquebrantables de un deck web de nivel producción:
    1. Archivo único independiente `index.html` (HTML5 + CSS + JS, cero dependencias rotas).
    2. Proporción fija 16:9 (1920×1080) con auto-escalado responsive vía `scale` que encaja al milímetro en cualquier monitor sin scrollbars.
    3. Navegación fluida por teclado (`→`, `←`, `Espacio`, `1`-`8`, `F` para pantalla completa, `T` para cambiar tema).
    4. Barra de progreso superior y contador de diapositivas en tiempo real.
    5. Zona segura reservada en la esquina inferior derecha para cámara / talking head en grabaciones de OBS (alternable con `C`).
    6. Estructura narrativa en 8 bloques de impacto (Hook de 5s, Problema, Solución, Bento Grid, Big Data Callout, Roadmap, Comparativa y CTA).
- **Entregables Desplegados**:
  - **Skill Oficial**: `/home/rootkit/agente/skills/presentaciones-elite-html/SKILL.md` (auditada con **100/100 Oro** en `validate-skill`).
  - **Plantilla Exacta**: `/home/rootkit/agente/skills/presentaciones-elite-html/templates/master_presentation.html`.
  - **Compilador CLI `build-deck`**: `/home/rootkit/agente/bin/build-deck` (`scripts/build_presentation.py`) para compilar decks desde JSON/Markdown o generar demos instantáneos con los 4 temas (*Dark Tech, Apple Keynote, Notion Minimal, Neo-Brutalist*).
  - **Visor CLI `preview-deck`**: `/home/rootkit/agente/bin/preview-deck` (`scripts/preview_presentation.py`) para lanzar y enfocar en Chrome nativo.
  - **Manual de Temas y Estilos**: `/home/rootkit/agente/skills/presentaciones-elite-html/references/temas_y_estilos.md`.
  - **Deck Compilado de Demostración**: Generado y disponible en `/home/rootkit/Proyectos/demo-slides/index.html` y en `examples/demo_presentacion_ia.html`.

### [2026-10-12] - Restauración del Pipeline Turbo de Vencimientos Stream Zone
- **Instrucción de Camilo**: «vencimientos https://admin.nuvlyx.com/inventory?variationId=2692898b-c80d-4b76-9e11-a31420f397cc jnsierra@jdc.edu.co Stream_Zone*1 te recuerdo ayudame con todo el flujo lo tienes documentado».
- **Implementación y Hallazgos**:
  - **Autenticación NuVlyx**: Se autenticó contra `POST /api/v1/auth/admin-login` con las credenciales suministradas. Token bearer emitido y persistido en `~/.cache/sz_admin_token.json` (tenant: `stream-zone-6822`).
  - **Pipeline Automatizado (`sz_vencimientos.py` & `bin/vencimientos`)**:
    - Desarrollado script de extracción concurrente con 20 workers en `scripts/sz_vencimientos.py` enlazado a `~/.local/bin/vencimientos`.
    - Mapeo de 63 productos y variaciones, descarga paralela de credenciales desencriptadas (`GET /inventory/licenses/{id}/credential`) y teléfonos de clientes (`GET /users/{clientId}`).
    - Filtro de corte habitual a 0-4 días (12 al 16 de Octubre de 2026): 55 suscripciones detectadas (9 vencen hoy, 11 mañana, 6 en 2 días, 26 en 3 días, 3 en 4 días).
    - Mapeo específico de la variación consultada `HBO MAX ESTÁNDAR PANTALLA` (`2692898b-c80d-4b76-9e11-a31420f397cc`): 3 suscripciones en la ventana de corte.
  - **Generación Excel Corporativo con OpenPyXL**:
    - Generado `reporte_vencimientos_4_dias_2026_10_12.xlsx` (copia en `Descargas/` y `StreamZone/proyectos/corte_2026_10_12/`).
    - Dos hojas: 1) Desglose general de toda la tienda (55 filas), 2) Desglose específico de la variación HBO Max Estándar.
    - Formato oficial: 13 columnas, encabezado azul oscuro (`#1A365D`), cebra (`#F8FAFC`), badges de semáforo (Rojo/Amarillo/Verde) y plantillas de WhatsApp personalizadas.
  - **Archivo de Despacho de WhatsApp**: Preparado `/tmp/pending_notifications.json` con 55 tareas listas para `sz-notify-batch.mjs`.
  - **Visualización**: Abierto automáticamente en WPS Spreadsheets (`et`) y enfocado en Niri.

### [2026-10-12] - CLI Maestro 'vencimientos' en Fish Shell (Pipeline Autónomo End-to-End)
- **Instrucción de Camilo**: «crea un bin que cuando haga vencimientos en fish haga todo eso rapido sin tanto pensar pero que cumpla a cabalidad», «y si envio? a streamzone official a los numeros de los que tienen que renovar», «a y antispam 5s ademas pues le envia streamzone official el excel mas la explicacion y ahi si ya sabes», «revisa tiene enviar correo contraseña dias orden pin».
- **Implementación y Reglas Fijadas**:
  - **Binario Maestro**: `/home/rootkit/agente/bin/vencimientos` symlinkeado en `/home/rootkit/.local/bin/vencimientos` (en el `$PATH` de Fish).
  - **Flujo 100% Autónomo en 1 Solo Comando (`vencimientos`)**:
    1. **Extracción y Desglose**: `sz_vencimientos.py` consulta NuVlyx API (0 a 4 días y vencidos recientes) con 20 hilos concurrentes.
    2. **Excel Corporativo**: Genera el libro oficial de 13 columnas en `~/Descargas/` con diseño azul (`#1A365D`), badges y totales.
    3. **Apertura de WPS**: Lanza no bloqueante `/usr/bin/et "$EXCEL_PATH"` en Niri.
    4. **Stream Zone Oficial (+573114668309)**: Envía el archivo `.xlsx` como documento con caption explicativo del estado de corte.
    5. **Clientes (Consolidado + Anti-Spam de 5s)**: Agrupa múltiples cuentas por número para no spamear al cliente. Despacho con retardo de 5.0 segundos.
    6. **Campos Obligatorios Garantizados**: Cada bloque de cuenta enviado al cliente incluye sin excepción:
       - 🧾 **Orden** (`ORD-XXXXX`)
       - ⏳ **Días restantes / Estado** (y fecha de corte)
       - 📧 **Correo / Cuenta**
       - 🔑 **Contraseña**
       - 👤 **Perfil**
       - 🔒 **PIN**
    7. **Grupo de Distribuidores**: Envía aviso de confirmación a `Distribuidores Stream Zone 🔥` (`120363425211205411@g.us`).
  - **Opciones CLI Disponibles**:
    - `vencimientos` (ejecución completa y directa).
    - `vencimientos --dry-run` (simulación en consola de los 3 pasos sin enviar mensajes).
    - `vencimientos --only-excel` / `--no-wa` (generación y WPS únicamente).
    - `vencimientos --delay <seg>` (intervalo anti-spam personalizable).
    - `vencimientos --limit <n>` (límite de clientes a procesar).

### [2026-10-12] - Auditoría y Erradicación de Redundancia en el Ecosistema de Skills
- **Instrucción de Camilo**: «revisa tu como agente para que no tengas rebundancia».
- **Diagnóstico Integral**:
  - Se auditaron las 51 skills del sistema en `/home/rootkit/agente/skills/` (enlazadas a `~/.agents/skills`).
  - **Identificación de Fricciones y Redundancias**:
    1. *Falta de Frontmatter en 4 Skills Locales*: `diseno-vectorial-svg`, `gestion-catalogo-streamzone`, `notificacion-clientes-whatsapp` y `reportes-vencimientos-excel` carecían del bloque `---` estándar, provocando advertencias de omisión en el gestor de paquetes.
    2. *Delimitación de Ámbitos (Evitar Canibalismo)*:
       - `xlsx` vs `reportes-vencimientos-excel`: `xlsx` es el motor general de hojas de cálculo y modelos financieros; `reportes-vencimientos-excel` es la lógica de negocio exclusiva de Stream Zone y NuVlyx.
       - `docx` vs `reversing-clonacion-docx-ieee`: `docx` para redlining, comentarios y manipulación general de Word; `reversing-clonacion-docx-ieee` para plantillas académicas formales de UNISANGIL.
       - `presentaciones-elite-html` vs `pptx`: HTML interactivo para presentaciones web y navegador vs archivos `.pptx` binarios editables para Microsoft PowerPoint.
- **Acciones Ejecutadas**:
  - Se añadieron frontmatters YAML estándar y disparadores claros en las 4 skills locales pendientes.
  - Se actualizaron los árboles de arquitectura en `AGENTS.md` y `GEMINI.md` organizando las skills por dominios modulares.
  - El sistema quedó con cero advertencias y cero colisiones funcionales.

### [2026-10-12] - Control Android y ADB Nativo en Arch Linux (Cero Wrappers Python)
- **Instrucción de Camilo**: «no con pythonn yo ya installe android tools en mi arch».
- **Criterio Operativo Fijado**:
  - Prohibido crear o requerir wrappers/capas intermedias de Python para interactuar con Android o ADB.
  - Se utiliza de forma 100% directa el binario nativo de Arch/CachyOS (`/usr/bin/adb`) mediante comandos de shell limpios y tuberías directas (`adb exec-out`, `adb shell input`, `adb install -r -g`, `adb pull`).
  - La skill `android-adb-control` fue refactorizada para basarse exclusivamente en one-liners y comandos directos de shell.

### [2026-10-12] - Apertura de Archivos con xdg-open (Cero Complicaciones)
- **Instrucción de Camilo**: «genial ahora no te tienes que complicar xdg-open y ya eso abre el default».
- **Criterio Operativo Fijado**:
  - Para abrir cualquier archivo (PDFs, imágenes, hojas de cálculo, documentos, URLs), no buscar binarios específicos ni sobrecomplicar la lógica: ejecutar directamente `xdg-open <archivo>`.
  - El sistema operativo y el entorno se encargan de despacharlo a la aplicación predeterminada de Camilo.

### [2026-10-12] - Creación del Vault Interno del Agente para Proyectos y Talleres
- **Instrucción de Camilo**: «no dentro del propio agente como un vault para recojer eso y compilar y trabajar ahi».
- **Criterio Operativo Fijado**:
  - Centralizar los proyectos en curso, talleres académicos (ej. UNISANGIL, UNAD) y trabajos técnicos en `/home/rootkit/agente/vault/` (con symlink directo en `~/vault`).
  - No dispersar imágenes ni borradores en carpetas genéricas (`~/Documentos` o `~/Descargas`).
  - Cada proyecto en `vault/` contiene su subcarpeta con:
    1. Insumos crudos (`fotos/`, capturas, audios, borradores numerados y limpios).
  - Primer trabajo finalizado y organizado: `vault/laboratorio/` (contiene exclusivamente el entregable final `laboratorio_ipv6.pdf` de 1.4 MB).

### [2026-10-12] - Instalación de Skills Élite: motion-design (LottieFiles) y agent-browser (Vercel)
- **Instrucción de Camilo**: «1 primero y la 3 hazlo» (Opción 1: LottieFiles Motion Design, Opción 3: Vercel Agent Browser).
- **Implementación**:
  - **Motion Design (`motion-design`)**: Instalada desde `LottieFiles/motion-design-skill` en `/home/rootkit/agente/skills/motion-design/`. Aporta directivas universales de animación, 12 reglas de Disney para UI, timing, easing y coreografía de componentes para CSS, Framer Motion, GSAP y React Native.
  - **Web Automation & Scraping (`agent-browser`)**: Instalada desde `vercel-labs/agent-browser` en `/home/rootkit/agente/skills/agent-browser/`. Incluye binario ejecutable en `~/.local/bin/agent-browser` (v0.39.0) para navegación headless, clicks, formularios, capturas e inspección del árbol de accesibilidad.

### [2026-10-12] - Purga Radical de 33 Micro-skills de HyperFrames y Remotion
- **Instrucción de Camilo**: «si purga» (en respuesta a la propuesta de limpieza para no saturar la lista).
- **Acción Quirúrgica**:
  - Se eliminaron las 33 micro-skills fragmentadas de HeyGen/HyperFrames y Remotion que saturaban el catálogo con micro-funciones redundantes.
  - El diseño de movimiento queda consolidado de manera limpia y profesional en:
    1. `motion-design` (LottieFiles / Disney UI universal).
    2. `motion-design-elite` (nuestro estándar 2D/3D con físicas armónicas, audio sincronizado y 60 FPS).
### [2026-10-12] - Incorporación del Trío Maestro de Scraping: ScrapeGraphAI, AgentReach y Scrapling MCP
- **Instrucción de Camilo**: «te voy pasar los que quiero deben estar si o si es scrapeGrapth ai , agenreach ,scrapling mcp».
- **Implementación y Despliegue**:
  1. **ScrapeGraphAI (`just-scrape`)**:
     - Skill instalada en `/home/rootkit/agente/skills/just-scrape/` para extracción inteligente estructurada y monitoreo web con ScrapeGraph AI.
  2. **AgentReach (`agent-reach`)**:
     - Motor y CLI instalado en `~/.local/share/agent-reach-env` y binario en `~/.local/bin/agent-reach` (`v1.5.0`).
     - Skill instalada en `/home/rootkit/agente/skills/agent-reach/`.
     - Capacidad de acceso e investigación en redes y plataformas sin APIs de pago (Twitter/X, Reddit, YouTube, Bilibili, LinkedIn, Jina Reader).
  3. **Scrapling MCP (`scrapling-mcp`)**:
     - Motor `scrapling[ai]` instalado en `~/.local/share/scrapling-env` con Playwright/Patchright Chromium para bypass indetectable de Cloudflare / Akamai / Turnstile.
     - Binarios enlazados: `~/.local/bin/scrapling` y `~/.local/bin/scrapling-mcp`.
     - **Servidor MCP registrado en `~/.gemini/config/mcp_config.json`**: activo en Antigravity (`agy mcp list`), exponiendo `stealthy_fetch`, `make_request`, `open_session`, `fetch` y `screenshot`.
     - Skill documental y operativa en `/home/rootkit/agente/skills/scrapling-mcp/`.

### [2026-10-12] - Incorporación de REA (Reverse Engineer Anything - morluto/rea)
- **Instrucción de Camilo**: «https://github.com/morluto/rea agrega esto».
- **Implementación y Despliegue**:
  1. **CLI y Binarios (`rea-agents` v6.4.0)**:
     - Instalado en `~/.local/bin/rea` y `~/.local/bin/rea-agents`.
     - Permite inspeccionar binarios nativos (ELF, Mach-O, PE), ensamblados .NET (PE/CLI), aplicaciones Electron / ASAR, paquetes Android (APK), firmware y capturas de red/tráfico web sin necesidad de código fuente original.
  2. **Servidor MCP (`rea`)**:
     - Registrado e integrado en `~/.gemini/config/mcp_config.json` (`command: "/home/rootkit/.local/bin/rea", args: ["mcp"]`).
     - 170 herramientas MCP mapeadas y exportadas en `~/.gemini/antigravity-cli/mcp/rea/`.
     - Diagnóstico `rea doctor --client antigravity` 100% verificado y alineado (`state: aligned`).
  3. **Skill Operativa (`reverse-engineer-anything`)**:
     - Desplegada en `/home/rootkit/agente/skills/reverse-engineer-anything/` con referencias bajo demanda (`references/`).
     - Auditada y certificada con puntaje perfecto de **100/100 [🏆 EXCELENCIA (Oro)]**.
     - Catálogo maestro actualizado a **32/32 skills en estado óptimo**.


### [2026-10-12] - Motor y CLI de DramaBox (Búsqueda, Extracción y Descarga)
- **Instrucción de Camilo**: «2 porque ya sabe como es piroba gancho o safarrancho» (crear el scraper/bot de DramaBox para extracción automática de series y capítulos).
- **Implementación**:
  - Se analizó la arquitectura web y móvil de DramaBox (`dramaboxdb.com` y `sapi.dramaboxvideo.com`).
  - Se descubrió que la plataforma web expone metadatos completos y los primeros 8-15 episodios con enlaces directos MP4 en 720p H.264 (9:16 vertical) sin DRM ni encriptación, con entrega por CDN CloudFront/Huawei.
  - Se programó [`scripts/dramabox_tool.py`](file:///home/rootkit/agente/scripts/dramabox_tool.py) con bypass TLS (curl_cffi chrome120) y descargas multi-hilo aceleradas con `aria2c`.
  - Se vinculó el comando ejecutable global en `~/.local/bin/dramabox` con subcomandos: `trending`, `latest`, `search`, `info`, `episodes` y `download`.
  - Almacenamiento organizado de series, metadatos JSON y posters en `vault/dramabox/<nombre_serie>/`.
- **Corrección de Detección de Capítulos**:
  - Se eliminó la dependencia de APIs intermediarias inestables.
  - El CLI ahora scrapea directamente los canales oficiales de DramaBox (`/channel/trending`, `/channel/must-sees`, `/search?searchValue=`).
  - Mapeo exacto de `chapterCount`, `totalChapterNum` y `freeChapterNum`, mostrando el total de capítulos y los episodios libres en HD de forma instantánea.

### [2026-10-12] - Investigación y Resolución del «Camino 2» en DramaBox (100% Episodios)
- **Instrucción de Camilo**: «camino 2 investiga» (estrategia para descargar la totalidad de los 60 a 90 episodios superando el bloqueo VIP oficial).
- **Conclusiones Técnicas del Análisis**:
  1. *Servidor Oficial (Camino 1)*: DramaBox entrega de 8 a 15 episodios libres en MP4 720p sin cifrar vía CDN. Los episodios 16+ están bloqueados en servidor web (`unlock: false`, sin URL) y en app móvil (`sapi`) requieren firma criptográfica RSA y cifrado AES-128 con saldo de monedas del lado del servidor.
  2. *Espejos y Agregadores Comunitarios (Camino 2)*: Las comunidades y canales de microdramas compilan la totalidad de los episodios (60–90 micro-capítulos) en películas continuas (*Full Movies*) de 1h30m a 3h45m en alta definición (1080p/720p), tanto en audio original subtitulado como con doblaje latino.
- **Integración en CLI `dramabox`**:
  - Se añadieron los subcomandos `dramabox find-full <query_o_id>` y `dramabox download-full <query_o_id> [--select N]` usando `yt-dlp`.
  - Permite resolver por ID numérico de DramaBox o por nombre, localizando y bajando el 100% de la historia corrida en un solo archivo MP4 directamente en `vault/dramabox/<nombre_serie>/`.
- **Soporte Oficial para Catálogo en Español y Doblaje Latino**:
  - *Causa del idioma en inglés*: Series como *Deny Me, Dragon King* son producciones anglosajonas filmadas originalmente en inglés por DramaBox (`Idioma: ENGLISH`).
  - *Solución*: Se integró soporte para el catálogo nativo en español (`dramaboxdb.com/es`) mediante las banderas `--es` en `trending`, `latest`, `search`, `info`, y la bandera `--latino` en `find-full` y `download-full` para ubicar las películas continuas de 3h+ dobladas al español latino.

### [2026-10-12] - Scraper Web e Indexador de Catálogo Directo (Carátulas HD + Info Literal)
- **Instrucción de Camilo**: «haz un scrapper web con search que indexe directo si n necesidad de descargar per o tome caraturas y info literal del api».
- **Implementación**:
  1. *Motor Scraper e Indexador*: [`scripts/dramabox_indexer.py`](file:///home/rootkit/agente/scripts/dramabox_indexer.py) y binario en PATH `~/.local/bin/dramabox-indexer` (integrado también en `dramabox index-*`).
  2. *Base de Datos y Almacenamiento*: Ubicado en `vault/dramabox/index/` (`dramabox_catalog.db`, `catalog.json` y `covers/*.jpg`).
  3. *Cero Descarga de Video*: No descarga los archivos de video; indexa metadatos exactos de la API (almacenando el payload `raw_json` íntegro) y descarga las carátulas originales en alta resolución (600x800).
  4. *Dashboard Web con Buscador Visual*: Servidor HTTP integrado ([`scripts/dramabox_server.py`](file:///home/rootkit/agente/scripts/dramabox_server.py)) con interfaz estilo Apple TV / Netflix, buscador instantáneo, filtrado por idioma, sincronización en vivo y visor del JSON literal del API.
  5. *Servicio Persistente en localhost:8080*: Desplegado como servicio systemd de usuario en `~/.config/systemd/user/dramabox-web.service` (`systemctl --user start/stop/restart dramabox-web`). Acceso directo y abierto en el navegador en [http://localhost:8080](http://localhost:8080).

### [2026-10-13] - Incorporación del Trío Maestro de Ahorro de Tokens: Caveman, RTK y Grill-Me
- **Instrucción de Camilo**: «skills caveman, rtk-ai/rtk, mattpocock/skills/grill-me esto ayuda para tokens investiga una por una y mira como la integramos para que realmente ayuden muccho».
- **Implementación y Despliegue**:
  1. **Caveman (`skills/caveman/`)**:
     - Compresión extrema de tokens de salida.
     - Aplica el patrón *Answer-First*, elimina toda ceremonia de chat ("Claro, con gusto"), utiliza palabras cortas y fragmentos técnicos exactos.
  2. **RTK (Rust Token Killer - `rtk-ai/rtk`)**:
     - Binario nativo v0.52.0 instalado en `~/.local/bin/rtk`.
     - Reduce del 60% al 90% los tokens de entrada de la terminal filtrando y compactando outputs de `git status`, `git diff`, `git log`, `ls`, `grep`, `pytest`, `npm test` y `cargo`.
     - Integrado en `install.sh` y documentado en `skills/rtk-token-killer/`.
  3. **Grill-Me (`skills/grill-me/`)**:
     - Metodología de interrogación quirúrgica y árbol de decisiones de Matt Pocock.
     - Evita el desperdicio de tokens por retrabajo o suposiciones erróneas formulando todo el frente de decisiones pendientes en una sola ronda con opciones y recomendación previa.

### [2026-10-13] - Incorporación de Graphify (Knowledge Graph AST Multimodal)
- **Instrucción de Camilo**: «https://github.com/Graphify-Labs/graphify opina» y «hazlo y ayudame».
- **Implementación y Despliegue**:
  1. **Motor Python e Instalación**:
     - Instalado `graphifyy` (v0.9.89) con parsers de Tree-sitter y NetworkX en entorno aislado `~/.local/share/graphify-env/`.
     - Binario enlazado a `~/.local/bin/graphify`.
  2. **Integración con Google Antigravity**:
     - Ejecutado `graphify antigravity install`: genera reglas en `~/.agents/rules/graphify.md`, flujos en `~/.agents/workflows/graphify.md` y skill nativa en `skills/graphify/`.
  3. **Ahorro de Contexto (71x menos tokens)**:
     - Indexación local determinista vía AST sin costo de API (`graphify .` o `graphify extract . --code-only`).
     - Generación de Wiki local en Markdown (`graphify-out/wiki/index.md`) y exportación interactiva a `graph.html` y Obsidian.

