---
name: scrapling-mcp
description: High-performance, anti-bot web scraping and structured extraction using Scrapling and Scrapling MCP. Use when the user asks to scrape websites with bot protection (Cloudflare, Akamai, PerimeterX), extract clean structured data without raw HTML bloat, fetch dynamic content with stealth browsers, take screenshots, or run adaptive multi-step scraping sessions.
---

# Scrapling & Scrapling MCP

Scrapling is an adaptive, stealthy web scraping framework that bypasses bot protections (Cloudflare, TLS fingerprinting) and delivers clean structured content without token bloat.

## 🛠️ MCP Tools Available

The Scrapling MCP server runs locally via Stdio (`/home/rootkit/.local/bin/scrapling-mcp`) and exposes:

1. **`stealthy_fetch`**: Fetch URLs through an anti-detection stealth browser engine (Patchright). Use for hard anti-bot walls (Cloudflare Turnstile, Cloudflare Challenge).
2. **`make_request`**: Ultra-fast HTTP request without launching a browser (uses `curl_cffi` impersonation). Use for static pages, JSON APIs, and light protection.
3. **`bulk_get`** / **`bulk_stealthy_fetch`**: Fetch multiple URLs concurrently.
4. **`fetch`**: Headless browser fetch for standard JavaScript rendering and SPAs.
5. **`open_session`** / **`session_fetch`** / **`close_session`**: Maintain persistent browser sessions across multiple steps (logins, pagination, searches).
6. **`screenshot`**: Capture full-page or element screenshots during a session.

---

## ⚡ CLI Usage

Scrapling is also available directly in the terminal:

```bash
# Extract text or structured data from any URL
scrapling extract "https://example.com"

# Interactive scraping shell
scrapling shell "https://example.com"
```

---

## 🐍 Python Usage

```python
import sys
sys.path.insert(0, "/home/rootkit/.local/share/scrapling-env/lib/python3.14/site-packages")
from scrapling import Fetcher, StealthyFetcher

# Fast fetch
fetcher = Fetcher()
response = fetcher.get("https://example.com")
print(response.css("h1::text").get())

# Stealth fetch (Cloudflare bypass)
stealth = StealthyFetcher()
page = stealth.fetch("https://protected-site.com")
print(page.title)
```
