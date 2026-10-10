#!/usr/bin/env python3
"""
Scraper genérico de alta potencia con bypass anti-bot
Uso: python3 quick_scrape.py <url> [--selector "css_selector"] [-o output.json]
"""
import sys
import json
import argparse
from curl_cffi import requests
from bs4 import BeautifulSoup

def scrape(url, selector=None, output=None):
    headers = {
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    }
    print(f"🌐 Conectando a {url} (impersonando Chrome)...")
    res = requests.get(url, headers=headers, impersonate="chrome120", timeout=20)
    if res.status_code != 200:
        print(f"❌ Error HTTP {res.status_code}", file=sys.stderr)
        return
    
    soup = BeautifulSoup(res.text, "lxml")
    if selector:
        elements = [el.get_text(strip=True) for el in soup.select(selector)]
        print(f"✅ Se encontraron {len(elements)} elementos con el selector '{selector}':")
        for i, el in enumerate(elements[:10], 1):
            print(f"  {i}. {el}")
        if len(elements) > 10:
            print(f"  ... y {len(elements) - 10} más.")
        data = elements
    else:
        title = soup.title.string if soup.title else "Sin título"
        print(f"✅ Página descargada con éxito. Título: {title}")
        data = {"title": title, "length": len(res.text)}

    if output:
        with open(output, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 Guardado en: {output}")

def main():
    parser = argparse.ArgumentParser(description="Scraper con bypass anti-bot")
    parser.add_argument("url", help="URL a extraer")
    parser.add_argument("-s", "--selector", help="Selector CSS a extraer")
    parser.add_argument("-o", "--output", help="Archivo JSON de salida")
    args = parser.parse_args()
    scrape(args.url, args.selector, args.output)

if __name__ == "__main__":
    main()
