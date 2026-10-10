---
name: web-scraping-automatizacion
description: Procedimientos y recetas de alto rendimiento para web scraping, extracción de datos y bypass de protecciones antibot (Cloudflare, TLS fingerprinting) usando curl_cffi, BeautifulSoup4 y lxml.
---

# Skill: Web Scraping y Extracción Avanzada de Datos

Esta habilidad establece los estándares y procedimientos para scraping en la PC, utilizando tanto scraping HTTP de alta velocidad con evasión de protecciones TLS como parseo estructurado de HTML.

---

## 🛡️ 1. Motor de Evasión Anti-Bot: `curl_cffi` (curl-impersonate)

En sitios protegidos con Cloudflare, Datadome o Akamai, las librerías estándar como `requests` o `urllib` son bloqueadas con errores `403 Forbidden` por huellas TLS (JA3/JA4).
En este sistema está instalado **`curl_cffi`**, que falsifica la huella TLS y HTTP/2 de navegadores reales (Chrome, Safari).

### Snippet de Extracción con Bypass:
```python
from curl_cffi import requests
from bs4 import BeautifulSoup

url = "https://ejemplo.com"

# Impersonando Chrome 120 para bypass de Cloudflare
response = requests.get(url, impersonate="chrome120", timeout=15)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    # Extracción de elementos
    titulos = [item.text.strip() for item in soup.select("h2.title")]
    print(f"Extraídos {len(titulos)} elementos.")
else:
    print(f"Error {response.status_code}")
```

---

## ⚙️ 2. Parseo Ultrarrápido con BeautifulSoup y LXML

- **Parser recomendado**: Usar siempre `"lxml"` en lugar de `"html.parser"`. Es entre 5x y 10x más rápido al procesar documentos HTML grandes.
- **Selectores CSS**: Usar `soup.select()` y `soup.select_one()` para consultas precisas.

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, "lxml")
datos = []
for fila in soup.select("table.tabla-datos tr"):
    columnas = [col.text.strip() for col in fila.find_all(["td", "th"])]
    if columnas:
        datos.append(columnas)
```

---

## 📦 3. Extracción y Guardado a Tablas (Pandas / Excel)

Integración directa con el ecosistema de datos instalado en la PC:
```python
import pandas as pd

# Convertir datos scrapeados a DataFrame y exportar a Excel
df = pd.DataFrame(datos[1:], columns=datos[0])
df.to_excel("proyectos/encargo/datos_extraidos.xlsx", index=False)
```
