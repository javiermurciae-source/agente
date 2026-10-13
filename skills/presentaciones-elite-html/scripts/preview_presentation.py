#!/usr/bin/env python3
"""
Lanzador y visor ultrarrápido para presentaciones HTML.
Abre el archivo en Google Chrome / Navegador del sistema y enfoca en Niri.
"""

import sys
import os
import subprocess
import shutil

def preview(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: Archivo no encontrado: {file_path}")
        sys.exit(1)

    abs_path = os.path.abspath(file_path)
    url = f"file://{abs_path}"

    # Si Firefox o Chrome están corriendo, abrir directamente
    if shutil.which("firefox"):
        subprocess.Popen(["firefox", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif shutil.which("google-chrome-stable"):
        subprocess.Popen(["google-chrome-stable", "--ozone-platform=wayland", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.Popen(["xdg-open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"🚀 Presentación abierta en el navegador: {abs_path}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "/home/rootkit/Proyectos/demo-slides/index.html"
    preview(target)
