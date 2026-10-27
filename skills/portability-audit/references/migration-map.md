# Mapa de migración — equivalencias por SO

Traduce los conteos de la **sección 5** del informe en tareas concretas de port.
Ordenado por lo que más aparece en repos Apple-first.

## macOS / Darwin → Linux

| Bloqueo en el repo | LOC típicos | Reemplazo en Linux | Dificultad |
|---|---|---|---|
| `dispatch_*` (GCD: queues, semaphores, `dispatch_once`) | 5-15% del runtime | `std::thread` / pthreads + `pthread_once`, `sem_t`, cola propia con condvar | 🟢 baja — semántica casi 1:1; **ojo**: GCD ejecuta en la main queue (UI) y Linux no tiene main runloop |
| `mach_vm_allocate` / `mach_vm_read_overwrite` / `mach_vm_remap` | 5-20% | `mmap` / `process_vm_readv` / **`mremap`** o `userfaultfd` | 🟡 media — `mach_vm_remap` (memoria aliasada / zero-copy) **no tiene equivalente directo**: `mremap` mueve, no aliasa. Alternativa: `memfd_create` + `mmap` sobre el mismo fd |
| `mach_absolute_time` / `CACurrentMediaTime` | bajo | `clock_gettime(CLOCK_MONOTONIC)` (ns) | 🟢 trivial |
| `os_unfair_lock` | 1 archivo | `pthread_mutex_t` (o `atomic_flag` en C11) | 🟢 trivial; ojo con su no-recursividad |
| `tpidrro_el0` (TLS del guest, ARM64 Apple) | ensambladores `.S` | Linux ARM64 usa **`tpidr_el0`**; `__thread` / `pthread_getspecific` en x86_64 | 🟡 baja en ARM64, 📕 si cambias de ISA |
| `CC_SHA*` (CommonCrypto) | 5-6 archivos | OpenSSL `EVP_*`, libsodium, o mbedtls | 🟢 trivial |
| **Metal** (`MTLDevice`, `MTLCommandBuffer`, `MTLSharedEvent`, `MTLBuffer`) | **el gordo** | **Vulkan**: `VkDevice`/`VkCommandBuffer`/`VkSemaphore`+`VkFence`/`VkBuffer`. Equivalencias: MTLBuffer→VkBuffer, MTLCommandBuffer→VkCommandBuffer, MTLSharedEvent→timeline semaphore, MTLRenderPass→`VkRenderingInfo` (dynamic rendering), MTLComputePipeline→VkComputePipeline | 🔴 alta — pero **es reescribir el backend, no la capa NVN**, si existe la interfaz C |
| **MetalFX** (upscale + frame gen) | 400-1500 | **AMD FSR2/FSR3** (MIT), Intel XeSS, o `VK_KHR_acceleration_structure`+own | 🟡 media — APIs distintas, mismo trabajo |
| **CoreAudio** / `AudioUnit` / `kAudio[A-Z]` | 1-3% | **PipeWire** (`pw_stream`) o ALSA `snd_pcm`; `portaudio`/`SDL_audio` si se quiere portabilidad | 🟡 media |
| **AppKit / Cocoa / UIKit** (`NSApplication`, `NSWindow`, `NSView`, `NS*`) | 10-30 archivos `.m` | **SDL3** (ventana+input+GL/Vulkan surface) o **GTK4**; en Wayland hay que salir de `NSWindow` | 🟡 media — SDL3 es la ruta corta |
| **GameController** (`GCController`) / CoreHaptics | 3-4 archivos | `SDL_Gamepad` / evdev (`/dev/input/js*`), FF via `EVIOCSFF` | 🟢 baja |
| **CoreText** / **CoreGraphics** (`CTLine`, `CGContext`) | 4-6 archivos | **Pango + Cairo** (texto con shaping completo) | 🟡 media — shaping/emoji son donde duele |
| **Vision** (`VNRequest`), **ImageIO** (`CGImageSource`) | 1-3 archivos | libjansson… no: **OpenCV**, o `stb_image` + ONNX Runtime si era inferencia | 🟡 según uso |
| **IOSurface / CoreVideo / CAMetalLayer** | 1-4 archivos | `VK_KHR_swapchain` + `wl_surface` / SDL3 window | 🟡 media |
| **UniformTypeIdentifiers / CommonCrypto / libkern / objc runtime** | bajo | GIO (GTK) / XDG MIME, OpenSSL, `dlopen` | 🟢 baja |
| Darwin `kqueue` / `kevent` | raro | `epoll` (Linux) o `libevent`/`libuv` | 🟢 baja |
| Rutas `~/Library/...`, bundle `.app`, `codesign` | build/packaging | XDG (`~/.local/share`, `~/.config`), `AppDir`/`.desktop`/Flatpak, `ld` en vez de `codesign` | 🟡 baja-media |

## Windows / Win32 / D3D → Linux

| Bloqueo | Reemplazo | Dificultad |
|---|---|---|
| `HWND`/`HINSTANCE`/`CreateWindowEx`/`WinMain` | SDL3 o GLFW+X11/Wayland | 🟢 baja |
| **Direct3D 11/12** (`D3D11*`, `IDXGI*`) | **Vulkan** (1:1 conceptual) o `DXVK`-invertido… usar **vkd3d-shader** para HLSL→SPIR-V | 🟡 media-alta |
| `CoInitialize` / COM | eliminar (no existe en Linux) | 🟢 trivial |
| `_WIN32`, `__declspec(dllexport)`, `#pragma comment(lib)` | `__attribute__((visibility("default")))`, CMake `target_link_libraries` | 🟢 baja |
| Win32 threads (`CreateThread`, `CRITICAL_SECTION`) | pthreads / `std::thread` + `std::mutex` | 🟢 trivial |
| `RegOpenKeyEx` (registro) | GKeyFile / JSON / XDG config | 🟢 baja |
| `LoadLibrary` / `GetProcAddress` | `dlopen` / `dlsym` | 🟢 trivial |
| Winsock2 | POSIX sockets (casi idénticos, `closesocket`→`close`) | 🟢 trivial |
| WASAPI / XAudio2 | PipeWire / ALSA / SDL_audio | 🟡 baja |
| UTF-16 (`wchar_t` everywhere) | UTF-8; **zona de bugs clásica** | 🟡 media |

## Inteligencia de lectura del informe

- **`hits` altos en POSIX/Linux con `#ifdef __linux__` = 0**: el código ya usa
  APIs portables pero nunca compiló en Linux → port **más barato** de lo que
  sugiere el conteo total.
- **`hits` altos + ifdefs multi-OS > 0**: el repo ya piensa en varios SO → casi
  seguro es cuestión de completar la matriz, no de rediseñar.
- **Un solo archivo concentra >20% del LOC no portable** → es el objetivo de
  ataque: aislarlo tras una interfaz y posponerlo.
- **`.cs` + `SPIR-V` + NativeAOT presentes** = el componente duro ya corre donde
  quieras correrlo; solo falta el backend del SO.
