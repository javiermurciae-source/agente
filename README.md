# 🤖 Agente Autónomo - Arquitectura y Respaldo Operativo

Sistema de agente de IA empotrado y automatización avanzada para entorno Linux de alto rendimiento (**CachyOS x86_64**, Wayland con compositor **Niri**, terminal **Kitty** y shell **Fish**).

---

## 🏗️ Cómo Funciona el Agente en Sí

El agente está organizado bajo una arquitectura de **4 pilares maestros + herramientas nativas**, lo que le otorga autonomía, memoria contextual y habilidades técnicas desacopladas:

```text
agente/
├── AGENTS.md                  # Manual maestro: directivas de alto rendimiento y reglas de oro
├── GEMINI.md                  # Espejo de compatibilidad total de instrucciones
├── memoria/                   # Memoria persistente y cronológica del agente
│   └── MEMORIA.md             # Criterios, preferencias, contactos VIP y aprendizajes con Camilo
├── contexto/                  # Base de conocimiento estática y dinámica
│   ├── comunicacion.md        # Protocolos de comunicación y mensajería
│   ├── entorno-pc.md          # Configuración de sistema, Wayland, Fish y utilitarios
│   ├── hardware-pc.md         # Ficha técnica del hardware (ASUS TUF, RTX 3050, 144Hz)
│   └── stream-zone.md         # Lógica de negocio, catálogo y flujos de Stream Zone
├── skills/                    # Habilidades operativas especializadas (recetas autocontenidas)
│   ├── control-ventanas-niri-gaming/    # Manejo de IPC de Niri, gaming y emuladores
│   ├── descargas-aria2-turbo/           # Descargas paralelas ultra-rápidas con aria2c
│   ├── diseno-vectorial-svg/            # Creación y renderizado de assets SVG
│   ├── gestion-catalogo-streamzone/     # Integración con NuVlyx API y licencias
│   ├── notificacion-clientes-whatsapp/  # Notificaciones automáticas de corte y renovación
│   ├── reportes-vencimientos-excel/     # Generación de reportes corporativos XLSX
│   ├── reversing-clonacion-docx-ieee/   # Ingeniería inversa y clonación OpenXML/IEEE
│   └── web-scraping-automatizacion/     # Extracción web evadiendo TLS con curl_cffi
├── bin/                       # Comandos y wrappers ejecutables nativos en terminal
│   ├── wasend / waget         # CLI de WhatsApp multi-dispositivo (Baileys)
│   ├── imgview / viewpic      # Visores CLI de imágenes
│   └── rish / ytdl / ttdl     # Utilidades de shell y descarga
├── tools/                     # Motores y librerías internas
│   └── wasend/                # Motor Node.js/Bun con @whiskeysockets/baileys
├── scripts/                   # Scripts auxiliares y pipelines de procesamiento
├── dotfiles/                  # Configuraciones rápidas (fastfetch, fish, oh-my-posh, yazi)
├── docs/                      # Guías operativas y documentación del sistema
├── install.sh                 # Script de restauración e instalación instantánea
└── .gitignore                 # Exclusión de dependencias pesadas y sesiones sensibles
```

---

## ⚡ Recuperación Rápida en una Nueva Máquina o Reinstalación

Para restaurar el agente al 100% en cuestión de segundos:

```bash
# 1. Clonar el repositorio en tu home
git clone https://github.com/javiermurciae-source/agente.git ~/agente
cd ~/agente

# 2. Ejecutar el script de instalación y restauración
./install.sh
```

El script se encargará automáticamente de:
1. Otorgar permisos ejecutables a todos los scripts y binarios.
2. Enlazar simbióticamente los ejecutables a `~/.local/bin/`.
3. Restaurar las dependencias de Baileys (`tools/wasend/`) usando Bun o Node.js.
4. Dejar el entorno listo para ser usado por el agente de IA de forma inmediata.
