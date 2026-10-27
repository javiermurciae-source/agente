#!/usr/bin/env python3
"""
Generador automático de plantillas (Scaffold) para nuevas Skills de Antigravity / Gemini.
Crea la estructura modular estándar:
  skills/<name>/
  ├── SKILL.md
  ├── scripts/
  ├── references/
  └── examples/
"""

import sys
import os
import re
import argparse
from pathlib import Path

BASE_SKILLS_DIR = os.environ.get("AGENTE_SKILLS_DIR") or str(Path(__file__).resolve().parents[2])

TEMPLATE_SKILL_MD = """---
name: {name}
description: >-
  {description}
---

# Skill: {title}

{summary}

---

## 🎯 1. Objetivo y Disparadores Operativos
- **Propósito**: {summary}
- **Cuándo activar**: Utilizar esta habilidad cada vez que el usuario solicite...

---

## 📋 2. Reglas Inquebrantables y Estándares Técnicos
- **Regla 1**: ...
- **Regla 2**: ...
- **Dependencias**: ...

---

## ⚙️ 3. Procedimiento de Ejecución (Paso a Paso)
1. **Paso 1: Preparación**: ...
2. **Paso 2: Procesamiento**: ...
3. **Paso 3: Verificación y Entrega**: ...

---

## 🛠️ 4. Scripts y Utilidades
- [`scripts/`](./scripts/): Scripts auxiliares para automatización del flujo.

---

## ✅ 5. Verificación de Éxito
- Comprobación de integridad y verificación sin errores.
"""

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")

def title_case(slug):
    return " ".join(word.capitalize() for word in slug.split("-"))

def create_skill(name, description, summary=None):
    slug = slugify(name)
    if not slug:
        print("❌ Error: Nombre de skill inválido.")
        sys.exit(1)

    skill_dir = os.path.join(BASE_SKILLS_DIR, slug)
    if os.path.exists(skill_dir):
        print(f"⚠️ La carpeta de la skill ya existe: {skill_dir}")
        return skill_dir

    # Crear directorios
    os.makedirs(os.path.join(skill_dir, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(skill_dir, "references"), exist_ok=True)
    os.makedirs(os.path.join(skill_dir, "examples"), exist_ok=True)

    title = title_case(slug)
    desc = description.strip() if description else f"Procedimiento y herramientas para {title}."
    summ = summary.strip() if summary else f"Guía y utilidades especializadas para {title}."

    skill_md_content = TEMPLATE_SKILL_MD.format(
        name=slug,
        description=desc,
        title=title,
        summary=summ
    )

    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(skill_md_content)

    print(f"✨ Skill creada exitosamente:")
    print(f"   📁 Directorio: {skill_dir}")
    print(f"   📄 Archivo maestro: {skill_md_path}")
    print(f"   📂 Subdirectorios: scripts/, references/, examples/")
    return skill_dir

def main():
    parser = argparse.ArgumentParser(description="Generador de nuevas skills para el agente")
    parser.add_argument("name", help="Nombre de la skill (en kebab-case)")
    parser.add_argument("--desc", "-d", default="", help="Descripción detallada para el Frontmatter YAML (indicar qué hace y cuándo usarla)")
    parser.add_argument("--summary", "-s", default="", help="Resumen inicial del propósito de la habilidad")

    args = parser.parse_args()
    create_skill(args.name, args.desc, args.summary)

if __name__ == "__main__":
    main()
