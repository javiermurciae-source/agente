# Rúbrica de veredicto

Tres preguntas, en orden. **La 1 y la 2 deciden; la 3 calibra el esfuerzo.**

---

## Pregunta 1 — ¿La ISA coincide?

Sección 3 del informe: ISAs encontradas vs CPU destino + menciones de traducción.

| Situación | Veredicto | Acción |
|---|---|---|
| ISA coincide (p. ej. `aarch64`→ARM64, `x86_64`→x86_64) | sigue a la 2 | — |
| ISA distinta **y** hay traductor (JIT/AOT/emulador/QEMU/FEX/box64) | sigue a la 2 | verificar que el traductor cubra el código de usuario, no solo un boot |
| ISA distinta **y cero** traductor | **❌** | **cerrar aquí**. Un JIT AArch64 completo = reconstruir un emulador; el valor del port ≈ 0 frente a un emulador que ya existe para el SO destino |

> Caso real: MacNativeGames (guest ARM64 → host ARM64 nativo, cero emulación).
> En x86_64 el truco central desaparece y no queda nada que portar de ventajoso.

---

## Pregunta 2 — ¿Hay frontera de abstracción?

Sección 6: cabeceras con punteros a función / `ops` / `vtable` / `backend` / `iface`.
Confirmar **leyendo 1 cabecera clave**, no solo el conteo.

| Situación | Veredicto | Naturaleza del trabajo |
|---|---|---|
| **Sí hay** frontera (la capa no portable cuelga de una interfaz C/Vtable documentada) | **⚠️→✅** | *Reimplementar una API*: ordenable por capas, atacable de dentro afuera, con la capa de encima intacta |
| **No hay** frontera (APIs del SO repartidas por todo el código) | **❌ o ⚠️ fuerte** | *Reescribir* → a años de escala. Solo justificable si no existe alternativa alguna |

> Caso real: `nvn_mtl.h` exponía `mtl_init/mtl_pool_add/mtl_sub_begin/mtl_sub_event`
> con `nvn_mtl.m` (13,165 LOC) debajo → el port era reimplementar esa API en
> Vulkan, no tocar la capa NVN. Y mitad de `d2r_gfx` no tocaba Metal en absoluto.

**Regla de aislamiento**: si un solo archivo concentra >20% del LOC no portable,
el plan es *aislarlo tras su interfaz y posponerlo*, no migrarlo primero.

---

## Pregunta 3 — Calibración del esfuerzo

Ecuación base con datos del informe (secciones 2, 5 y 10):

```
LOC_portable   = total − Σ(LOC de archivos que tocan APIs propietarias)
LOC_a_reescribir = Σ(LOC de los archivos bloqueados, escalados × 1 si hay
                     frontera, × 1.5-2 si no la hay)
```

| Señal del informe | Multiplica el esfuerzo |
|---|---|
| ifdefs multi-OS = **0** | ×1.5 — nadie compiló jamás en otro SO: habrá sorpresas de build |
| ifdefs multi-OS **> 0** | ×1.0 — la matriz multi-SO ya existe |
| El componente duro es `.py/.cs/.rs/go` o IR (SPIR-V/LLVM) | **×0.3** — ya corre en el destino |
| Licencia MIT/Apache/zlib en un equivalente existente | ×0.3-0.5 — crib legal en vez de escribir |
| CI solo en un SO (`runs-on: macos-latest`) | ×1.2 — sin red de seguridad en el destino |
| Comentario de intento previo fallido en el repo | ×0.7 — hay pista gratis |

**Traducción a tiempo (regla práctica, declárala como estimación):**

| LOC_a_reescribir | Orden de magnitud |
|---|---|
| < 1,000 | días |
| 1,000 – 5,000 | 1-4 semanas |
| 5,000 – 15,000 | 1-3 meses |
| 15,000 – 40,000 | 3-9 meses (1 persona) |
| > 40,000 sin frontera | **no es un port, es un proyecto nuevo** |

---

## Umbrales de salida

| Combinación | Veredicto |
|---|---|
| ISA ok + frontera sí + (LOC_a_reescribir < 5,000 o IR portable) | **✅ viable** |
| ISA ok + frontera sí + LOC_a_reescribir 5,000-40,000 | **⚠️ viable con condiciones** (esfuerzo explícito, orden de ataque por capas) |
| ISA ok + **sin** frontera + LOC_a_reescribir > 15,000 | **❌ no conviene** (salvo que no exista alternativa) |
| ISA distinta sin traductor | **❌** (Pregunta 1) |
| Hardware destino insuficiente (RAM/disco/ISA) | **❌** aunque el código sea portable — verificar contra `contexto/hardware-pc.md` |

---

## Errores de procedimiento que ya costaron (no repetir)

1. **Medir tarde el CPU.** El paso 0 evita leer 700 archivos para concluir lo que
   2 comandos dicen.
2. **`grep` sin `-E`**: `|` es literal en BRE → señales en `0` falsas
   (aquí: ifdefs multi-OS `0` cuando el valor real era `3`). **Canario**: si la
   señal sale `0` y el repo claramente usa `__APPLE__`, falta el `-E`.
3. **Contar LOC sin separar por capa**: el total no dice nada; la pregunta es
   *dónde* está el bloqueo y si ese dir es atacable por separado.
4. **Olvidar la alternativa.** Veredicto ❌ sin "hoy usa X" es un veredicto a
   medias.
5. **Afirmar sin ejecutar**: siempre la línea de "auditoría estática".
