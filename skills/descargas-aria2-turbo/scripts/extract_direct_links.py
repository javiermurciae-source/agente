#!/usr/bin/env python3
"""
Extractor de enlaces directos para cyberlockers (MediaFire, etc.)
Uso: python3 extract_direct_links.py <url1> [url2 ...] [-o output_links.txt]
"""
import sys
import re
import urllib.request
import argparse

def extract_mediafire(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"}
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")
        m = re.search(r'href=[\"\'](https?://download\d+\.mediafire\.com/[^\"\']+)[\"\']', html)
        if not m:
            m = re.search(r'id=[\"\']downloadButton[\"\'][^>]*href=[\"\']([^\"\']+)[\"\']', html)
        if m:
            return m.group(1)
    except Exception as e:
        sys.stderr.write(f"Error extrayendo {url}: {e}\n")
    return None

def main():
    parser = argparse.ArgumentParser(description="Extractor de enlaces directos para aria2")
    parser.add_argument("urls", nargs="+", help="URLs públicas a resolver")
    parser.add_argument("-o", "--output", default="links.txt", help="Archivo de salida (defecto: links.txt)")
    args = parser.parse_args()

    direct_links = []
    for u in args.urls:
        link = extract_mediafire(u)
        if link:
            direct_links.append(link)
            print(f"[OK] {link}")
        else:
            print(f"[FALLO] No se pudo resolver: {u}", file=sys.stderr)

    if direct_links:
        with open(args.output, "w") as f:
            for l in direct_links:
                f.write(l + "\n")
        print(f"\n✅ {len(direct_links)} enlaces directos guardados en {args.output}")

if __name__ == "__main__":
    main()
