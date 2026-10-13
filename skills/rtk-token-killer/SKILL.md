---
name: rtk-token-killer
description: >-
  Optimización extrema de tokens de entrada mediante el proxy de terminal RTK (Rust Token Killer).
  Filtra y comprime entre un 60% y un 90% la salida de comandos comunes (git status/diff/log,
  ls, grep, cat, cargo, pytest, npm test, docker) antes de ser leída por el agente de IA.
  Activar cuando se ejecuten comandos de inspección en terminal, git, pruebas o revisión de código.
---

# Skill: rtk-token-killer (Filtro y Compresión de Tokens en Terminal)

Proxy CLI de ultra-alto rendimiento escrito en Rust (`rtk`, binario nativo en `~/.local/bin/rtk`) que intercepta y comprime salidas de terminal antes de ingresar al contexto de la IA.

---

## 🚀 1. Comandos Comprimidos vs Salida Tradicional

| Operación | Comando Nativo | Equivalente RTK (Ahorro 60-90%) |
|---|---|---|
| **Estado Git** | `git status` | `rtk git status` |
| **Diferencias Git** | `git diff` | `rtk git diff` |
| **Historial Git** | `git log -n 10` | `rtk git log -n 10` |
| **Búsqueda código** | `grep -rn "patron"` | `rtk grep "patron"` o `rtk rg "patron"` |
| **Estructura** | `tree` / `ls -la` | `rtk ls` |
| **Pruebas** | `pytest` / `npm test` | `rtk pytest` / `rtk npm test` |

---

## 📊 2. Métricas y Verificación de Ahorro

- Ver estadísticas acumuladas de tokens ahorrados:
  ```bash
  rtk gain
  ```
- Desactivar o consultar telemetría:
  ```bash
  export RTK_TELEMETRY_DISABLED=1
  ```
