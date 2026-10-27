#!/usr/bin/env bash
# portaudit.sh — Auditoría de portabilidad de un repositorio (证据 → veredicto).
#
# Uso:
#   portaudit.sh /ruta/al/repo
#   portaudit.sh https://github.com/usuario/repo.git   # clona en temporal y audita
#
# Sale con 0 siempre que produzca informe (el informe es el entregable).
# Requiere: bash, find, grep, sed, awk, wc, sort, uniq. Opcional: git, gh.

set -uo pipefail

# --- directorio de trabajo ---------------------------------------------------
SRC="${1:-}"
if [ -z "$SRC" ]; then
  echo "uso: portaudit.sh <dir|url-git>" >&2
  exit 2
fi
TMPD=""
REPONAME=""
case "$SRC" in
  http://*|https://*|git@*)
    REPONAME="$(printf '%s' "$SRC" | sed -E 's#\.git$##; s#^(https?://|git@)##; s#^[^/]*[/:]##')"
    TMPD="$(mktemp -d /tmp/portaudit.XXXXXX)"
    trap 'rm -rf "$TMPD"' EXIT
    echo "clonando $SRC (en frío)..." >&2
    git clone --depth 1 -q "$SRC" "$TMPD/repo" || { echo "FALLO el clone" >&2; exit 1; }
    SRC="$TMPD/repo"
    ;;
esac
if [ ! -d "$SRC" ]; then echo "no existe: $SRC" >&2; exit 2; fi
cd "$SRC" || exit 2
REPONAME="${REPONAME:-$(basename "$SRC")}"

# extensiones que consideramos "código fuente" para contar LOC
SRC_EXT=(c h cpp hpp cc m mm S asm cs py rs go java kt swift zig dart lua)
build_files=(CMakeLists.txt meson.build Makefile makefile configure.ac BUILD Bazel.build Package.swift *.sln *.vcxproj)

hr() { printf '\n### %s\n\n' "$1"; }
# OJO: BRE trata '|' como literal → siempre -E (esto costó un falso negativo de 0
# en la señal de ifdefs multi-OS: __linux__|_WIN32|__APPLE__ devolvía 0 con __APPLE__ real = 3).
INC=(--include=*.c --include=*.h --include=*.cpp --include=*.hpp --include=*.m
     --include=*.mm --include=*.S --include=*.asm --include=*.cs --include=*.py
     --include=*.rs --include=*.go --include=*.java --include=*.swift --include=*.zig)
cnt()   { grep -rE "$1" . "${INC[@]}" -I 2>/dev/null | wc -l; }
files() { grep -rlE "$1" . "${INC[@]}" -I 2>/dev/null | wc -l; }

echo "# Auditoría de portabilidad — $REPONAME"
echo
echo "- ruta: $SRC"
echo "- fecha: $(date +%Y-%m-%d\ %H:%M)"

# =============================================================================
hr "1. Censo de archivos"
find . -path ./.git -prune -o -type f -print 2>/dev/null \
  | grep -E '\.[A-Za-z0-9_+-]+$' | sed 's/.*\.//' | tr '[:upper:]' '[:lower:]' \
  | sort | uniq -c | sort -rn | head -18 | awk '{printf "%-8s %s\n", $1, $2}'

# =============================================================================
hr "2. Peso por capa (LOC recursivo; se ocultan los dirs que solo heredan el LOC del padre)"
FA=()
for e in "${SRC_EXT[@]}"; do FA+=(-name "*.$e" -o); done
unset 'FA[-1]'
find . -mindepth 1 -maxdepth 4 \( -path ./.git -o -path './.git/*' -o -path './.github' \) -prune -o -type d -print 2>/dev/null \
| grep -vE '^\./(node_modules|build|dist|out|target)' \
| while IFS= read -r d; do
    n=$(find "$d" -path '*/.git/*' -prune -o -type f \( "${FA[@]}" \) -print 2>/dev/null | xargs -r wc -l 2>/dev/null | tail -1 | awk '{print $1}')
    [ -n "$n" ] && [ "$n" -gt 99 ] && printf "%8d LOC  %s/\n" "$n" "${d#./}"
  done | sort -k1,1nr -k3,3 \
| awk 'NR==1{print;prev=$3;prevn=$1;next}
       index($3,prev)==1 && $1==prevn {next}
       {print; prev=$3; prevn=$1}' | head -15

# =============================================================================
hr "3. ISA y arquitectura — ¿el CPU objetivo coincide?"
echo '```'
grep -rhoE '\b(aarch64|arm64|__aarch64__|__arm64__|x86_64|__x86_64__|__amd64__|riscv64|__arm__)\b' . 2>/dev/null \
  | sort | uniq -c | sort -rn | head -8
echo '--- ensambladores por ISA ---'
for ext in S s asm; do
  [ -n "$(find . -path ./.git -prune -o -name "*.$ext" -print 2>/dev/null | head -1)" ] && \
  find . -path ./.git -prune -o -name "*.$ext" -print 2>/dev/null | head -8
done
echo '--- ¿hay traducción/JIT/emulación? ---'
grep -rioE '\b(jit|just.in.time|aot|interpret(er|ing)?|emulat(e|or|ion)|rosetta|box64|fex-emu|qemu|unicorn|dyld|binary translation|recompil(e|ation))\b' \
  --include=*.md --include=*.c --include=*.h --include=*.py --include=*.cs . 2>/dev/null \
  | sed 's/.*://' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn | head -8
echo '```'

# =============================================================================
hr "4. Frameworks propietarios (vendor lock-in)"
echo '```'
grep -rhoE '#import <[A-Za-z0-9]+/|#include <[A-Za-z0-9]+/|#include <Q[A-Za-z]' . \
  --include=*.m --include=*.mm --include=*.h --include=*.c --include=*.cpp --include=*.hpp 2>/dev/null \
  | sed -E 's/#(import|include) <//' | tr -d '/' | sort | uniq -c | sort -rn | head -18
echo '```'

# =============================================================================
hr "5. APIs por SO — mapa de migración"
echo '| API del SO | hits | archivos |'
echo '|---|---:|---:|'
while IFS='|' read -r label pattern; do
  [ -z "$label" ] && continue
  h=$(cnt "$pattern" true)
  [ "$h" -gt 0 ] && printf '| %-34s | %5d | %5d |\n' "$label" "$h" "$(files "$pattern")"
done <<'PATRONES'
macOS/Darwin - dispatch_*|dispatch_
macOS/Darwin - mach_*|mach_
macOS/Darwin - os_unfair_lock|os_unfair_lock
macOS/Darwin - mach_absolute_time|mach_absolute_time
macOS/Darwin - CommonCrypto|CC_SHA
macOS/Darwin - NS*/CF*/CG*|NS[A-Z]|CF[A-Z]|CG[A-Z]
macOS - Metal|MTL[A-Z]|#import <Metal/
macOS - CoreAudio/AudioToolbox|AudioUnit|AudioOutputUnit|kAudio[A-Z]
macOS - AppKit/Cocoa|NSApplication|NSWindow|NSView\b
macOS - GameController/GameControllerKit|GCController
macOS - CoreText/CoreGraphics|CTLine|CTFont|CGContext
macOS - Vision/ImageIO|VNRequest|CGImageSource
Linux - POSIX/Linux|clock_gettime|mmap\b|pipe2|epoll|inotify|eventfd|dlopen|pthread_
Linux - PipeWire/ALSA|pw_stream|snd_pcm|pa_stream
Linux - Vulkan|vkCreate|VkDevice|VkBuffer|vkCmd
Linux - X11/Wayland|XOpenDisplay|wl_display|xdg_wm_base
Windows - Win32|HWND|HINSTANCE|CreateWindowEx|WinMain|__declspec|CoInitialize
Windows - D3D|D3D11|D3D12|IDXGI|Direct3D
Windows - MSVC/_WIN32|_WIN32|__MSVC|#pragma comment
Multi-OS ifdef - __linux__|__linux__
Multi-OS ifdef - _WIN32|_WIN32
Multi-OS ifdef - __APPLE__|__APPLE__
PATRONES

# =============================================================================
hr "6. ¿Existe frontera de abstracción? (la pregunta que decide todo)"
echo '```'
echo "-- cabeceras con punteros a función / ops / vtable --"
grep -rlE '\(\*[a-zA-Z_][a-zA-Z0-9_]*\)[[:space:]]*\(|\b(ops|vtable|vtbl|interface|backend|driver|iface)\b' \
  --include=*.h --include=*.hpp --include=*.inc 2>/dev/null | head -20
echo "-- total de cabeceras: $(find . -path ./.git -prune -o \( -name '*.h' -o -name '*.hpp' \) -print 2>/dev/null | wc -l) --"
echo '```'

# =============================================================================
hr "7. Componentes ya portables de fábrica"
echo '| Señal | detalle |'
echo '|---|---|'
p=$(find . -path ./.git -prune -o \( -name '*.py' -o -name '*.go' -o -name '*.rs' \) -print 2>/dev/null | wc -l)
echo "| .py/.go/.rs (corren en cualquier SO) | $p archivos |"
p=$(find . -path ./.git -prune -o -name '*.cs' -print 2>/dev/null | wc -l)
echo "| .cs (.NET, multiplataforma con NativeAOT) | $p archivos |"
p=$(grep -rl 'CMakeLists.txt\|meson.build' --include=*.md . 2>/dev/null | wc -l)
b=""
for f in "${build_files[@]}"; do find . -path ./.git -prune -o -name "$f" -print 2>/dev/null; done | head -5 | tr '\n' ' '
echo
echo "| build multiplataforma (CMake/Meson) | ver línea arriba |"
p=$(grep -rioE 'SPIR-V|SPIRV|GLSL|HLSL|WGSL|LLVM|bitcode|wasm' --include=*.md --include=*.c --include=*.h --include=*.cs . 2>/dev/null | sed 's/.*://' | tr '[:upper:]' '[:lower:]' | sort -u | tr '\n' ' ')
echo "| representación intermedia portable | $p |"
p=$(grep -rhoE 'runs-on:[[:space:]]*(ubuntu|macos|windows)[a-z0-9-]*' .github/workflows/*.yml 2>/dev/null | sort -u | tr '\n' ' ')
echo "| CI multi-OS | $p |"

# =============================================================================
hr "8. Pistas en comentarios/documentación (intentos previos)"
echo '```'
grep -rniE 'x86|linux|rosetta|not supported|unsupported|only.*(mac|windows)|todo|wip|route|ruta|port(a|ing)?\b' \
  --include=*.md --include=*.h --include=*.c --include=*.txt 2>/dev/null | head -18
echo '```'

# =============================================================================
hr "9. Licencias y linaje"
find . -path ./.git -prune -o \( -iname 'LICENSE*' -o -iname 'COPYING*' \) -print 2>/dev/null | head -8
echo
grep -rhoiE '(MIT|Apache[ -]2\.0|GPL-[23]|LGPL|MPL-2\.0|BSD-[23]-Clause|Unlicense|CC0|proprietary|all rights reserved)' \
  README* docs/*.md 2>/dev/null | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn | head -8

# =============================================================================
hr "10. Señales automáticas (para el veredicto, no es el veredicto)"
isa=$(grep -rhoE '\b(aarch64|arm64|x86_64|__x86_64__|riscv64)\b' . 2>/dev/null | sort -u | tr '\n' ' ')
jit=$(grep -rliE '\b(jit|emulat|interpret|rosetta|box64|fex-emu|qemu|unicorn)\b' --include=*.md --include=*.c --include=*.py . 2>/dev/null | wc -l)
vend_hits=0
for p in 'MTL[A-Z]' 'AudioUnit' 'NSApplication' 'GCController' 'HWND' 'D3D1[12]' 'CreateWindowEx'; do
  vend_hits=$(( vend_hits + $(cnt "$p" true) ))
done
multi=$(cnt '__linux__|_WIN32|__APPLE__' true)
bord=$(grep -rlE '\(\*[a-zA-Z_][a-zA-Z0-9_]*\)[[:space:]]*\(|\b(ops|vtable|backend|iface)\b' --include=*.h 2>/dev/null | wc -l)

echo "| señal | valor | lectura |"
echo "|---|---|---|"
echo "| ISAs encontradas | \`$isa\` | ¿coinciden con el CPU objetivo? |"
echo "| menciones JIT/emulación | $jit archivos | si la ISA no coincide y $jit = 0 → bloqueo duro |"
echo "| hits de API propietaria | $vend_hits | alto + sin ifdefs multi-OS = port costoso |"
echo "| ifdefs multi-OS (\`__linux__\`/\`_WIN32\`/\`__APPLE__\`) | $multi | >0 = el repo ya piensa en varios SO |"
echo "| cabeceras con ops/fn-ptr | $bord | >0 = existe frontera → reimplementar, no reescribir |"
