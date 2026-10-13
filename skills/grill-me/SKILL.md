---
name: grill-me
description: >-
  Metodología de interrogación quirúrgica y árbol de decisiones para blindar planes,
  arquitecturas y requerimientos. Evita la pérdida masiva de tokens por retrabajo o
  asunciones erróneas preguntando el frente completo de decisiones en una sola ronda
  con recomendaciones directas. Activar cuando el usuario pida /grill-me, "hazme preguntas",
  "valida mi plan", "interrógate", o antes de tareas complejas con alta ambigüedad.
---

# Skill: grill-me (Entrevista Quirúrgica y Árbol de Decisiones)

Entrevista implacable y estructurada para afinar un plan, arquitectura o conjunto de requerimientos técnicos sin asumir nada a ciegas. Mapea la tarea como un **árbol de diseño (*design tree*)** donde cada decisión desbloquea las decisiones que dependen de ella.

Ahorra cientos de miles de tokens al evitar turnos de chat erráticos, refactorizaciones innecesarias y correcciones tardías.

---

## 🎯 1. Principio Operativo: Rondas por Frente (*Frontier Rounds*)

1. **El Frente (*Frontier*)**: Es el conjunto de todas las decisiones cuyos requisitos previos ya están resueltos. Son las preguntas que se pueden hacer **ahora mismo** sin adivinar respuestas futuras.
2. **Una Sola Ronda Agrupada**: Pregunta todo el frente en una sola tanda numerada.
3. **Respuesta Recomendada Siempre Incluida**: Formula cada pregunta de modo que un simple *"sí"* o *"aprobado"* por parte del usuario acepte tu recomendación.
4. **Búsqueda de Hechos por Cuenta del Agente**:
   - Encontrar hechos en el entorno (archivos, logs, versiones, código) es **trabajo del agente**, jamás del usuario.
   - Solo se pregunta al usuario por **decisiones de negocio o arquitectura**.

---

## 📋 2. Formato Estándar de la Ronda

```markdown
### 🎯 Ronda de Alineación [Frente Activo]

❓ **P1 — <Título de la Decisión>**: <Contexto conciso y opciones A / B / C>.
➡️ **Recomendación**: <Opción sugerida con justificación técnica breve>.

---

❓ **P2 — <Título de la Decisión>**: <Contexto conciso y opciones A / B / C>.
➡️ **Recomendación**: <Opción sugerida con justificación técnica breve>.
```

---

## 🏁 3. Fin de la Sesión

La sesión de *grilling* termina cuando el frente queda vacío: todas las ramas del árbol de diseño están resueltas y no queda ninguna asunción oculta. En ese momento, se procede a la ejecución inmediata sin más preguntas.
