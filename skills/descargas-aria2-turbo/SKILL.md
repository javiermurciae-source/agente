---
name: descargas-aria2-turbo
description: Procedimiento de alto rendimiento para descargas extremas multi-hilo con aria2c deslimitado (aria2-fast, hasta 128 conexiones, falloc, caché de disco de 128MB y bypass de cyberlockers).
---

# Skill: Descargas de Máximo Rendimiento con aria2c (Modo Turbo)

Esta habilidad documenta y estandariza el procedimiento de descarga multi-hilo a velocidad extrema (100+ MB/s) utilizando `aria2c` en Linux, optimizado para sistemas de archivos modernos (btrfs, ext4, xfs).

---

## 🎯 1. Principio Fundamental: Enlaces Directos Primero

Los cyberlockers (MediaFire, Google Drive, 1Fichier, Pixeldrain, Mega, etc.) o pastes (BlizzPaste, Pastebin) **NO entregan el archivo binario en su URL pública**. Pasar la URL pública a `aria2c` descargará únicamente una página HTML.

### 🛑 Regla de Oro
**Siempre se debe extraer el enlace directo de descarga (`downloadXXXX...`) antes de ejecutar `aria2c`.**

### Script Python de Extracción Rápida (MediaFire / Enlaces Directos)
```python
import urllib.request, re

urls = [
    "https://www.mediafire.com/file/xxxxx/part1.rar",
    "https://www.mediafire.com/file/yyyyy/part2.rar",
]
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"}

direct_links = []
for u in urls:
    req = urllib.request.Request(u, headers=headers)
    html = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")
    # Buscar el botón o enlace de descarga directa final
    m = re.search(r'href=[\"\'](https?://download\d+\.mediafire\.com/[^\"\']+)[\"\']', html)
    if not m:
        m = re.search(r'id=[\"\']downloadButton[\"\'][^>]*href=[\"\']([^\"\']+)[\"\']', html)
    if m:
        direct_links.append(m.group(1))

with open("links.txt", "w") as f:
    for link in direct_links:
        f.write(link + "\n")
```

---

## 🚀 2. Parámetros Clave para Máximo Rendimiento

Comando deslimitado de alta potencia:

```bash
aria2c -i links.txt \
  -c \
  -x 128 \
  -s 128 \
  -j 3 \
  -k 1M \
  --file-allocation=falloc \
  --disk-cache=128M \
  --user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" \
  --summary-interval=3 \
  --dir="/ruta/de/descarga"
```

### Explicación Quirúrgica de Parámetros:
- `-i links.txt`: Procesa la lista de enlaces en cola secuencial o concurrente.
- `-c` (`--continue=true`): **Reanudación instantánea**. Continúa exactamente en el byte donde quedó si la red se interrumpe.
- `-x 128` (`--max-connection-per-server=128`): Abre múltiples sockets TCP simultáneos por servidor, superando estrangulamientos artificiales de los servidores CDN. *(En versiones estándar usar 16; en binarios parcheados como `aria2-fast` soporta hasta 128)*.
- `-s 128` (`--split=128`): Segmenta cada archivo en 128 bloques concurrentes mediante encabezados HTTP `Range`.
- `-j 3` (`--max-concurrent-downloads=3`): Controla cuántos archivos de la lista se descargan simultáneamente.
- `-k 1M` (`--min-split-size=1M`): Permite fragmentar archivos pequeños a partir de 1 MB.
- `--file-allocation=falloc`: **CRUCIAL EN LINUX**. Usa la llamada al kernel `posix_fallocate` para reservar espacio en disco en **0.001 segundos** en ext4/btrfs/xfs, eliminando congelamientos al crear archivos gigantes de 10-50 GB.
- `--disk-cache=128M`: Almacena bloques en memoria RAM antes de volcar a disco, evitando cuellos de botella de I/O a 100+ MB/s.
- `--user-agent="Mozilla/5.0..."`: Evita bloqueos `403 Forbidden` de CDNs que rechazan clientes que se identifican como "aria2".
- `--summary-interval=3`: Reporta el estado cada 3 segundos sin saturar el búfer de salida.

---

## 🔄 3. Flujo Operativo Completo para el Agente

1. **Crear directorio de destino**:
   ```bash
   mkdir -p ~/Descargas/<NOMBRE_DESTINO>
   ```
2. **Resolver enlaces directos** y guardarlos en `links.txt`.
3. **Disparar la descarga** apuntando a `--dir="~/Descargas/<NOMBRE_DESTINO>"`.
4. **Monitorear progreso** hasta confirmar terminación limpia (`stat:OK`).
5. **Descompresión automática si es multipartes**:
   ```bash
   unrar x -p"PASSWORD" "NOMBRE.part1.rar" "/ruta/destino/"
   ```
6. **Mantenimiento**: Preguntar a Camilo si desea conservar o purgar los archivos `.rar` descargados para liberar espacio.
