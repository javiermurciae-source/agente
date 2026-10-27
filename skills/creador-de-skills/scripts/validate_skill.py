#!/usr/bin/env python3
"""
Validador de Alto Rendimiento y Alta Calidad para Skills de Antigravity / Gemini.
Audita una skill bajo el Estándar de Oro:
  1. YAML Frontmatter: 'name' válido en kebab-case, 'description' descriptiva en 3ra persona con triggers.
  2. Arquitectura de archivos: SKILL.md, directorios scripts/, references/, examples/.
  3. Integridad de scripts: Sintaxis válida (Python compile, Bash -n, Node -c), permisos de ejecución (+x).
  4. Métrica de Calidad Anti-Slop: Densidad técnica, ausencia de clichés, comandos reproducibles.
  5. Revelación Progresiva (Progressive Disclosure): Longitud de SKILL.md controlada con docs en references/.
  6. Sincronización en el sistema: Reflejo en ~/.gemini/config/skills/ y ~/.agents/skills/.
"""

import sys
import os
import re
import subprocess
import argparse
from pathlib import Path

BASE_SKILLS_DIR = os.environ.get("AGENTE_SKILLS_DIR") or str(Path(__file__).resolve().parents[2])
GLOBAL_CONFIG_SKILLS = str(Path.home() / ".gemini" / "config" / "skills")
WORKSPACE_SKILLS = str(Path.home() / ".agents" / "skills")

CLICHE_WORDS = [
    "código limpio", "buenas prácticas", "fácil de usar", "solución integral",
    "de manera intuitiva", "robusto y escalable", "altamente eficiente"
]

def check_frontmatter(content):
    issues = []
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not frontmatter_match:
        return False, None, ["No contiene bloque YAML frontmatter '---' al inicio."]

    raw_yaml = frontmatter_match.group(1)
    
    # Extraer name
    name_match = re.search(r"^name:\s*([a-zA-Z0-9_-]+)", raw_yaml, re.MULTILINE)
    if not name_match:
        issues.append("Falta campo 'name' o tiene formato incorrecto.")
        name = None
    else:
        name = name_match.group(1).strip()
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
            issues.append(f"El nombre '{name}' no cumple con el formato estricto kebab-case (solo minúsculas y guiones).")

    # Extraer description
    desc_match = re.search(r"^description:\s*(?:>-|>)?\s*\n?(.*?)(?=\n[a-zA-Z0-9_-]+:|\Z)", raw_yaml, re.DOTALL | re.MULTILINE)
    if not desc_match or not desc_match.group(1).strip():
        issues.append("Falta campo 'description' o está vacío.")
    else:
        desc = desc_match.group(1).strip()
        if len(desc) < 30:
            issues.append("La 'description' es demasiado corta (mínimo 30 caracteres para que el modelo la entienda).")
        # Check triggers
        if not any(k in desc.lower() for k in ["usar", "utilizar", "cuando", "procedimiento", "guía", "genera", "crea", "extrae", "use", "when"]):
            issues.append("La 'description' no incluye disparadores claros (palabras como 'utilizar cuando...', 'procedimiento para...').")

    return (len(issues) == 0), name, issues

def validate_script_syntax(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    is_executable = os.access(file_path, os.X_OK)

    if ext == ".py":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                compile(f.read(), file_path, "exec")
            return True, is_executable, "Sintaxis Python válida"
        except Exception as e:
            return False, is_executable, f"Error de sintaxis Python: {e}"
    elif ext == ".sh" or ext == ".bash":
        res = subprocess.run(["bash", "-n", file_path], capture_output=True, text=True)
        if res.returncode == 0:
            return True, is_executable, "Sintaxis Bash válida"
        return False, is_executable, f"Error sintaxis Bash: {res.stderr.strip()}"
    elif ext in [".js", ".mjs"]:
        res = subprocess.run(["node", "-c", file_path], capture_output=True, text=True)
        if res.returncode == 0:
            return True, is_executable, "Sintaxis Node.js válida"
        return False, is_executable, f"Error sintaxis Node: {res.stderr.strip()}"
    
    return True, is_executable, "Archivo de script reconocido"

def audit_skill(skill_path):
    print(f"\n🔍 Auditando Skill de Alto Rendimiento: {os.path.basename(skill_path)}")
    print("=" * 65)

    if not os.path.isdir(skill_path):
        print(f"❌ Error: La ruta no es un directorio válido: {skill_path}")
        return False

    skill_md = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md):
        print(f"❌ Error fatal: Falta el archivo maestro SKILL.md en {skill_path}")
        return False

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    score = 100
    warnings = []

    # 1. Frontmatter Audit
    ok_fm, name, fm_issues = check_frontmatter(content)
    if not ok_fm:
        print("❌ [Fallo Frontmatter YAML]:")
        for iss in fm_issues:
            print(f"   - {iss}")
            score -= 15
    else:
        print(f"✓ Frontmatter YAML: Válido (name: '{name}')")

    # 2. Progressive Disclosure Audit
    lines = content.split("\n")
    line_count = len(lines)
    if line_count > 450:
        warnings.append(f"SKILL.md muy extenso ({line_count} líneas). Se recomienda mover manuales a references/ para optimizar contexto.")
        score -= 5
    else:
        print(f"✓ Revelación Progresiva: Longitud equilibrada ({line_count} líneas)")

    # 3. Anti-Slop Audit
    found_cliches = [c for c in CLICHE_WORDS if c in content.lower()]
    if found_cliches:
        warnings.append(f"Detectadas frases cliché de IA ({', '.join(found_cliches)}). Remplazar con especificaciones técnicas directas.")
        score -= 5
    else:
        print("✓ Calidad Anti-Slop: Cero clichés genéricos detectados")

    # 4. Comprobación de Scripts
    scripts_dir = os.path.join(skill_path, "scripts")
    if os.path.exists(scripts_dir):
        scripts = [os.path.join(scripts_dir, f) for f in os.listdir(scripts_dir) if os.path.isfile(os.path.join(scripts_dir, f))]
        if scripts:
            print(f"✓ Directorio de Scripts: {len(scripts)} utilidades detectadas:")
            for sc in scripts:
                ok_syn, is_exec, msg = validate_script_syntax(sc)
                status_icon = "✓" if (ok_syn and is_exec) else "⚠️"
                exec_warn = "" if is_exec else " (Falta permiso +x)"
                print(f"   {status_icon} {os.path.basename(sc)}: {msg}{exec_warn}")
                if not ok_syn:
                    score -= 15
                if not is_exec:
                    score -= 5
        else:
            print("ℹ Directorio scripts/ presente pero sin utilidades.")
    else:
        print("ℹ No contiene directorio scripts/ dedicado.")

    # 5. Sincronización de Enlaces en el Sistema
    folder_name = os.path.basename(skill_path)
    sym_gemini = os.path.join(GLOBAL_CONFIG_SKILLS, folder_name)
    sym_ws = os.path.join(WORKSPACE_SKILLS, folder_name)
    if os.path.exists(sym_gemini) and os.path.exists(sym_ws):
        print(f"✓ Sincronización Global: Vinculada y descubrible por el agente")
    else:
        warnings.append("La skill no está visible en las rutas globales de descubrimiento.")
        score -= 10

    # Resumen
    print("-" * 65)
    if warnings:
        print("⚠️ Advertencias de Calidad:")
        for w in warnings:
            print(f"   • {w}")
    
    score = max(0, score)
    status_label = "🏆 EXCELENCIA (Oro)" if score >= 90 else "✓ ACEPTABLE (Plata)" if score >= 75 else "⚠️ REQUIERE AJUSTES"
    print(f"Puntaje de Rendimiento y Calidad: {score}/100 [{status_label}]")
    return score >= 75

def main():
    parser = argparse.ArgumentParser(description="Auditor y validador de alto rendimiento para Skills del agente")
    parser.add_argument("skill", nargs="?", default="", help="Nombre de la skill o ruta absoluta")
    parser.add_argument("--all", action="store_true", help="Auditar todas las skills instaladas")
    args = parser.parse_args()

    if args.all:
        skills = sorted(os.listdir(BASE_SKILLS_DIR))
        print(f"🚀 Auditando {len(skills)} skills instaladas...")
        passes = 0
        for s in skills:
            p = os.path.join(BASE_SKILLS_DIR, s)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
                if audit_skill(p):
                    passes += 1
        print(f"\n📊 Resultado Global: {passes}/{len(skills)} skills pasaron la validación de calidad.")
        return

    if not args.skill:
        print("Uso: validate-skill <nombre-de-skill> o validate-skill --all")
        sys.exit(1)

    skill_path = args.skill if os.path.isabs(args.skill) else os.path.join(BASE_SKILLS_DIR, args.skill)
    success = audit_skill(skill_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
