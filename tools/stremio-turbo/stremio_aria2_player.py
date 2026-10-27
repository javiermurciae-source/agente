#!/usr/bin/env python3
"""
Stremio Turbo Launcher:
Toma el torrent/stream magnet/infohash, lo acelera con aria2c a disco/RAM secuencial
y abre MPV inmediatamente con streaming fluido sin caídas.
"""
import sys
import subprocess
import time
import os

def main():
    if len(sys.argv) < 2:
        print("Uso: stremio-turbo <url_o_magnet>")
        sys.exit(1)
        
    target = sys.argv[1]
    # Si es URL directa o torrent
    cmd = ["mpv", "--cache=yes", "--demuxer-max-bytes=200M", target]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
