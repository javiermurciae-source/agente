#!/usr/bin/env python3
"""
Helper CLI para control de ventanas Niri y lanzador rápido de juegos
Uso:
  python3 niri_window.py list
  python3 niri_window.py focus <titulo_o_id>
  python3 niri_window.py fullscreen
  python3 niri_window.py play-switch "<nombre_juego>"
"""
import sys
import json
import subprocess
import os

def run_cmd(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def list_windows():
    res = run_cmd(["niri", "msg", "-j", "windows"])
    if res.returncode != 0:
        print("Error consultando Niri:", res.stderr)
        return []
    windows = json.loads(res.stdout)
    for w in windows:
        print(f"[{w['id']}] {w.get('app_id', 'desconocido')}: {w.get('title', 'Sin título')} (WS: {w.get('workspace_id')})")
    return windows

def focus_window(query):
    windows = json.loads(run_cmd(["niri", "msg", "-j", "windows"]).stdout)
    target_id = None
    if query.isdigit():
        target_id = int(query)
    else:
        for w in windows:
            title = w.get('title', '').lower()
            app = w.get('app_id', '').lower()
            if query.lower() in title or query.lower() in app:
                target_id = w['id']
                break
    if target_id:
        subprocess.run(["niri", "msg", "action", "focus-window", "--id", str(target_id)])
        print(f"✅ Ventana enfocada: ID {target_id}")
    else:
        print(f"❌ No se encontró ventana que coincida con '{query}'")

def main():
    if len(sys.argv) < 2:
        print("Uso: niri_window.py [list | focus <query> | fullscreen | center | shot]")
        sys.exit(1)
    
    action = sys.argv[1].lower()
    if action == "list":
        list_windows()
    elif action == "focus" and len(sys.argv) > 2:
        focus_window(sys.argv[2])
    elif action in ["shot", "screenshot"]:
        from datetime import datetime
        out_dir = os.path.expanduser("~/Pictures/Screenshots")
        os.makedirs(out_dir, exist_ok=True)
        filename = f"Screenshot_{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.png"
        target = os.path.join(out_dir, filename)
        subprocess.run(["grim", target])
        print(f"📸 Captura guardada en: {target}")
    elif action in ["fullscreen", "center", "close"]:
        cmd_map = {
            "fullscreen": "fullscreen-window",
            "center": "center-column",
            "close": "close-window"
        }
        subprocess.run(["niri", "msg", "action", cmd_map[action]])
        print(f"✅ Acción ejecutada: {cmd_map[action]}")
    else:
        print(f"Comando no reconocido: {action}")

if __name__ == "__main__":
    main()
