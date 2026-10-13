---
name: creador-de-skills
description: >-
  Metodología, estándares y herramientas de ingeniería para concebir, estructurar,
  redactar, probar y desplegar nuevas Skills (habilidades operativas modulares) en el
  sistema de agentes de Camilo. Utilizar siempre que se solicite crear una nueva skill,
  estandarizar un nuevo flujo de trabajo o convertir herramientas/scripts en paquetes de habilidades.
---

# Skill: Creador y Arquitecto de Skills

Esta habilidad gobierna el diseño, empaquetado, validación y despliegue de nuevas capacidades modulares para el agente empotrado de Camilo.

---

## 🎯 1. Filosofía y Propósito

Una **Skill** no es un simple documento de texto: es un **paquete de ejecución modular** que dota al agente de conocimiento procedimental estricto, scripts ejecutables y reglas de decisión para resolver tareas complejas sin fricción ni preguntas redundantes.

### Principios Fundamentales:
1. **Ruta Más Corta y Cero Burocracia**: La skill debe orientar al agente directamente a la solución técnica más eficiente con el menor número de comandos posibles.
2. **Revelación Progresiva (Progressive Disclosure)**:
   - `SKILL.md` debe ser conciso y directo al grano (procedimiento maestro y reglas).
   - Documentación voluminosa, esquemas de datos o manuales de referencia deben residir en `references/`.
   - Lógica compleja repetitiva debe encapsularse en `scripts/`.
3. **Determinismo y Verificabilidad**: Todo procedimiento debe incluir cómo validar que el resultado es correcto (dry-run, salida esperada, chequeo de integridad).

---

## 📁 2. Estructura Estándar de un Paquete de Skill

Toda nueva skill se aloja físicamente en `/home/rootkit/agente/skills/<nombre>/`:

```text
/home/rootkit/agente/skills/<nombre-kebab-case>/
├── SKILL.md                  # OBLIGATORIO: Procedimiento maestro con YAML Frontmatter
├── scripts/                  # RECOMENDADO: Scripts ejecutables testeados (Python, Bash, Node)
│   └── helper.py
├── examples/                 # OPCIONAL: Implementaciones de referencia y plantillas
└── references/               # OPCIONAL: Manuales extensos, esquemas JSON, tablas de APIs
```

Debido a los enlaces simbólicos del sistema, cualquier carpeta creada aquí se refleja automáticamente en:
- `~/.gemini/config/skills/<nombre>/`
- `~/.agents/skills/<nombre>/`
- `~/skills/<nombre>/`

---

## 📝 3. Estándar Obligatorio del `SKILL.md`

Todo `SKILL.md` debe comenzar estrictamente con Frontmatter YAML:

```markdown
---
name: nombre-de-la-skill
description: >-
  Descripción en tercera persona. Debe indicar claramente QUÉ hace la habilidad
  y los DISPARADORES ESPECÍFICOS de CUÁNDO debe activarse.
---

# Skill: Título Descriptivo

Breve resumen de la capacidad y el alcance operativo.

---

## 🎯 Objetivo y Disparadores
Cuándo se activa y qué problema resuelve.

---

## 📋 Reglas Inquebrantables / Estándares Técnicos
- Parámetros obligatorios.
- Dependencias del sistema.
- Criterios de calidad.

---

## ⚙️ Procedimiento Paso a Paso (Workflow)
1. Paso 1 con comando directo o script.
2. Paso 2 con verificación.
3. Paso 3 con entrega del resultado.

---

## 🛠️ Herramientas y Scripts Asociados
- [`scripts/helper.py`](./scripts/helper.py): Utilidad ejecutable para automatizar el paso X.

---

## ✅ Verificación de Éxito
Cómo comprobar que la tarea concluyó satisfactoriamente.
```

---

## 🔄 4. Ciclo de Vida de Creación (Paso a Paso)

Cuando Camilo pida crear una nueva habilidad o estandarizar un flujo:

### Paso 1: Deconstrucción del Conocimiento
- Analizar las fuentes: documentación oficial, repositorios, papers o scripts existentes.
- Extraer dependencias requeridas (binarios del sistema, paquetes Python/Node).
- Identificar los casos borde y comandos que fallan comúnmente.

### Paso 2: Creación del Scaffold
Ejecutar el generador automático:
```bash
create-skill <nombre-kebab-case> --desc "Descripción en tercera persona con triggers"
```
O invocar el script Python:
```bash
python3 /home/rootkit/agente/skills/creador-de-skills/scripts/scaffold_skill.py <nombre> --desc "..."
```

### Paso 3: Redacción del Contenido Quirúrgico
- Escribir `SKILL.md` aplicando el estándar de calidad anti-slop.
- Si hay automatizaciones reutilizables, programar scripts limpios en `scripts/` y darles permisos `chmod +x`.

### Paso 4: Validación y Pruebas
1. Validar que el Frontmatter YAML no tenga errores sintácticos.
2. Ejecutar un test sintáctico o dry-run en los scripts de apoyo.
3. Verificar que los enlaces relativos apunten a ficheros existentes.

### Paso 5: Registro Permanente
- Actualizar `memoria/MEMORIA.md` registrando la nueva skill, su propósito y fecha.
- Actualizar el manual maestro `AGENTS.md` / `GEMINI.md` en el listado de skills si aplica.

---

## 🤖 5. Subagente Especializado `skill-creator`

Para tareas complejas de creación que requieran investigación profunda en segundo plano sin saturar la conversación principal:
```python
invoke_subagent([
    {
        "TypeName": "skill-creator",
        "Role": "Skill Architect",
        "Prompt": "Investiga la API X y construye un paquete de skill completo en agente/skills/api-x/ con SKILL.md y script de prueba."
    }
])
```
