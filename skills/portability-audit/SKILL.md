---
name: portability-audit
description: >-
  Auditoría de portabilidad de repositorios: determina en minutos si un proyecto
  (típicamente macOS/Apple o Windows) puede correr en Linux, qué capa es la
  bloqueante, cuánto esfuerzo cuesta y qué atajos de licencia o abstracción
  existen. Mide LOC por capa, detecta frameworks propietarios y APIs del SO,
  localiza la frontera de abstracción que separa lo portable de lo no portable,
  verifica licencias reutilizables y busca en comentarios intentos previos
  fallidos. Disparadores: '¿se puede portar esto a Linux?', '¿lo podemos trabajar
  para Linux', 'analiza este repo para otra plataforma', 'audita dependencias de
  SO', '¿cuánto cuesta portar X', '¿es viable en mi equipo', y en general cuando
  el usuario pegue un enlace a un repositorio preguntando viabilidad técnica en
  un SO o hardware distinto al original.
---

# Skill: Portability Audit

Convierte *"¿corre esto en Linux?"* en un **veredicto medido**: LOC por capa,
mapa de migración de APIs, frontera de abstracción y esfuerzo estimado. Auditoría
**estática** (lee código, no compila) — eso debe declararse en la entrega.

---

## 🎯 1. Objetivo y Disparadores

- **Propósito**: responder con números si un repo es portable a un SO/CPU objetivo,
  dónde está el bloqueo y qué alternativa existe si no lo es.
- **Cuándo activar**: enlace a un repositorio + pregunta de viabilidad
  ("¿lo podemos trabajar para X", "¿corre en mi PC", "¿cuánto cuesta portar",
  "es viable"), o tras revisar un proyecto y querer evaluarlo para otro entorno.

---

## 📋 2. Reglas Inquebrantables

1. **Paso 0 siempre: mirar el CPU/ISA antes que el código.** Si la ISA origen y la
   destino difieren y el repo no tiene traductor (JIT/emulación/AOT), el veredicto
   es ❌ en 10 segundos — no leer 700 archivos para llegar a lo mismo.
2. **Nunca concluir por un solo grep.** Toda señal rara o sospechosa se confirma
   con un comando manual antes de publicarla. *Artefacto real de esta skill: un
   `grep` sin `-E` trataba `|` como literal y devolvió `0` donde el valor real
   era `3` (falso negativo en la señal de ifdefs multi-OS).*
3. **Todo número va con su unidad y su ruta**: `13,165 LOC en nvn_mtl.m`, no
   "la capa gráfica es grande".
4. **Distinguir esfuerzo de viabilidad**: hay ports de 3 días y ports de 3 años;
   son respuestas distintas y ambas deben aparecer.
5. **Si no se ejecutó, no se afirma**: el output es "auditoría estática — no
   compilado ni probado en el SO destino".
6. **Declarar alternativa siempre**, incluso cuando el veredicto sea ✅
   (¿existe algo ya hecho que resuelve el caso de uso?).
7. **Limpiar**: los clones temporales se borran al salir (el script ya lo hace
   vía `trap`); no dejar procesos ni `/tmp` huérfanos.
8. **Si se necesitan credenciales/datos del usuario para ir más allá** (p. ej.
   compilar de verdad), preguntar — nunca inventarlas.
9. **El grep sobreestima; el compilador no.** Toda cifra de "cuánto cuesta portar"
   que salga de contar includes debe contrastarse con un **spike de compilación**
   (Paso 1b). *Artefacto real: la estimación por grep dijo "3,249 LOC casi gratis";
   compilando, eran **408 LOC** y encima sin funcionalidad — los "faltantes" eran
   flags `-I` que faltaban de mi lado, no trabajo de port.*
10. **Validar cualquier clasificador contra un caso concreto**, no contra el total:
    si una clase salta de 18 a 5 entre ejecuciones, el detector está roto, no el repo.

---

## ⚙️ 3. Procedimiento de Ejecución

### Paso 0 — Filtro de arquitectura (el más barato)
Preguntar: ¿la CPU/ISA del proyecto coincide con la del equipo destino?
```bash
# en el repo, o en el README del enlace
grep -rhoE '\b(aarch64|arm64|x86_64|__x86_64__|riscv64)\b' . | sort | uniq -c | sort -rn
find . -name '*.S' -o -name '*.asm'
```
ISA distinta + 0 menciones de JIT/emulación → **❌ cerrar aquí** y ofrecer
alternativa. *(Caso real: MacNativeGames = guest ARM64 nativo en ARM64 → en
x86_64 exigía un JIT AArch64 completo = reconstruir un emulador.)*

### Paso 1 — Ejecutar la auditoría
```bash
# local
/home/rootkit/agente/skills/portability-audit/scripts/portaudit.sh /ruta/al/repo

# o directo desde GitHub (clona en frío en /tmp y limpia al salir)
/home/rootkit/agente/skills/portability-audit/scripts/portaudit.sh https://github.com/usuario/repo.git
```
Salida: informe Markdown con 10 secciones. Guardar en el directorio de trabajo si
el usuario lo pide (`> informe.md`), si no, leerlo en consola.

### Paso 1b — Spike de compilación (el número real, no la estimación)
Antes de estimar esfuerzo, **compilar** la capa C con `clang -fsyntax-only -std=gnu11`
+ los `-I` del proyecto. Clasifica cada fallo: `PORT` (API del SO real), `DEP`
(falta librería/include — **casi nunca es trabajo de port**), `ARM` (NEON: pasa en
Linux ARM64), `PASS*` (compila pero su rama `#if TARGET_OS_*` quedó vacía → **no
aporta funcionalidad**). No necesita link, datos del juego ni toolchains del vendor.
Plantilla funcional:
`vault/proyectos/macnativegames-linux/tests/check_linux_compile.sh`.
Si un lenguaje no puede compilar en el destino (p. ej. `.cs` sin `dotnet`), anotarlo
como hallazgo: también es bloqueo del port.

### Paso 2 — Interpretar con la rúbrica
Leer [`references/verdict-rubric.md`](./references/verdict-rubric.md) y decidir
✅ / ⚠️ / ❌. Las tres preguntas que gobiernan el resultado:

| # | Pregunta | Sección del informe |
|---|---|---|
| 1 | ¿La ISA coincide, o hay traductor? | 3 |
| 2 | **¿Hay frontera de abstracción?** (cabeceras con `ops`/fn-ptr) | 6 |
| 3 | ¿Qué % del LOC toca APIs propietarias sin ifdefs multi-OS? | 5 + 10 |

- **Frontera SÍ** → *reimplementar una API* (meses, viable, ordenable por capas).
- **Frontera NO** → *reescribir* (años, casi siempre → ofrecer alternativa).

### Paso 3 — Cruzar mapa de migración
Tabla de equivalencias Darwin/Win32 → Linux en
[`references/migration-map.md`](./references/migration-map.md): sirve para
traducir el conteo de la sección 5 en tareas concretas (`dispatch_*` → pthreads,
`mach_vm_*` → mmap/mremap, CoreAudio → PipeWire, MetalFX → FSR…).

### Paso 4 — Buscar atajos antes de estimar esfuerzo
- **Licencia reutilizable**: `find . -iname 'LICENSE*'` + leer las de
  `third_party/`/`vendor/`. Si el componente duro es MIT/Apache/zlib → crib legal
  posible (caso real: Ryujinx = MIT y resolvía NVN→Vulkan en Linux).
- **IR ya portable**: la sección 7 marca `.py/.cs/.rs`, SPIR-V/GLSL/LLVM y CI
  multi-OS — si lo más difícil ya corre en el SO destino, el port es más corto.
- **Intentos previos**: sección 8. Un comentario que mencione la ruta rival
  ("la ruta x86", "Rosetta", "no soportado") ahorra semanas de redescubrimiento.

### Paso 5 — Entregar veredicto (formato fijo)
```markdown
**VEREDICTO: ✅ viable | ⚠️ viable con condiciones | ❌ no conviene**  — <objetivo>

- **Bloqueo**: <ISA / API propietaria / licencia / ninguno>
- **Capa gorda**: <N> LOC en `<ruta>` (<% del código) → <reimplementar|reescribir>
- **Spike** (si se hizo): <N>/<total> `.c` compilan ya en <SO> · <N> `PORT` de <LOC>
- **Mapa de migración**: <los 3-5 reemplazos principales con sus LOC>
- **Atajos**: <licencias / IR portable / intentos previos>
- **Esfuerzo**: <días | semanas | meses> sobre <N LOC portables>
- **Alternativa hoy**: <qué usar si no se hace el port>
⚠️ Auditoría estática: sin spike = *no compilado ni probado en el SO destino*;
con spike = *solo sintaxis (`-fsyntax-only`): no link-eado ni ejecutado*.
```

---

## 🛠️ 4. Scripts y Utilidades

- [`scripts/portaudit.sh`](./scripts/portaudit.sh): informe de 10 secciones
  (censo, LOC por capa, ISA, frameworks propietarios, mapa de APIs, frontera de
  abstracción, componentes portables, pistas, licencias, señales automáticas).
  Sin dependencias fuera de `find/grep/sed/awk/wc/sort/uniq` (+ `git` si se pasa URL).

---

## ✅ 5. Verificación de Éxito

1. **Sintaxis**: `bash -n scripts/portaudit.sh` sin salida de error.
2. **Prueba de humo** (debe completar y mostrar estas líneas en un repo Apple/C):
   ```bash
   scripts/portaudit.sh /tmp/opencode/MacNativeGames
   # esperado: games/totk/runtime/ ~8420 LOC · ifdefs multi-OS = 3 (no 0)
   #           cabeceras con ops/fn-ptr > 0 · licencia MIT
   ```
   El valor de *ifdefs multi-OS* es el **canario del bug de BRE**: si sale `0`
   en un repo que sí usa `__APPLE__`, el `grep` perdió el `-E`.
3. **Entrega**: formato de la sección 3 completo, con las 4-5 líneas de evidencia
   numérica y la advertencia de auditoría estática.
4. **Limpieza**: `ls /tmp/portaudit.* 2>/dev/null` vacío tras salir.
