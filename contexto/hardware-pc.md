# Perfil de Hardware y Sistema de la PC (Fastfetch)

Información técnica oficial del equipo para la toma de decisiones sobre rendimiento, renderizado, compilación y asignación de recursos para juegos y modelos.

---

## 💻 1. Especificaciones del Equipo
- **Modelo**: ASUS TUF Gaming F15 (`FX507ZC4_FX507ZC4`)
- **BIOS / Firmware**: `FX507ZC4.312`
- **Sistema Operativo**: CachyOS x86_64 (Arch Linux rolling)
- **Kernel**: Linux `7.2.6-1-cachyos` (Kernel CachyOS optimizado con BORE scheduler)
- **Compositor de Ventanas**: **Niri 26.04** (Wayland, scrollable-tiling)
- **Login / Display Manager**: SDDM 0.21.0
- **Pantalla**: Panel IPS 15.33" FHD (1920x1080 px) @ **144 Hz**

---

## ⚡ 2. Procesador (CPU) y Memoria
- **CPU**: **12th Gen Intel Core i5-12500H**
  - Núcleos: 12 núcleos (4 P-Cores de alto rendimiento + 8 E-Cores de eficiencia) / 16 hilos.
  - Frecuencia base/turbo: hasta 4.50 GHz.
  - Caché: 18 MB L3.
- **Memoria RAM**: **16 GB DDR4/DDR5** (15.24 GiB efectivos)
  - Swap: 15.24 GiB zram0 (compresión ZRAM activa en RAM).
- **Almacenamiento**:
  - Unidad SSD NVMe: **WD PC SN740 SDDPNQD-512G** (512 GB PCIe 4.0).
  - Sistema de archivos: `btrfs` con soporte `falloc` y compresión zstd.

---

## 🎮 3. Gráficos (GPUs) y Aceleración
- **GPU Dedicada (dGPU)**: **NVIDIA GeForce RTX 3050 Laptop GPU** (4 GB GDDR6 VRAM, 2048 CUDA cores).
  - Driver: NVIDIA 615+ con aceleración Vulkan 1.4 y OpenGL 4.6.
- **GPU Integrada (iGPU)**: **Intel Iris Xe Graphics** (80 EUs).
  - Aceleración de video por hardware (VA-API / Intel iHD): Decodificación y codificación HEVC/H.265, H.264, VP9 y decodificación AV1.

---

## 🎮 4. Periféricos y Conectividad
- **Mando Principal**: **Sony PlayStation Wireless Controller** (DualSense / DualShock) conectado por Bluetooth.
- **Gamepad Virtual / Streaming**: `libvirtualhid Mouse` y Sunshine para streaming HDMI / remoto.
- **Red**: Tarjeta Wi-Fi 6 (802.11ax) Intel en banda 5 GHz.
- **Servidor de Sonido**: **PipeWire** con soporte PulseAudio y WirePlumber.
