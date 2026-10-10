# Contexto de Negocio: Stream Zone

Información operativa de la tienda, catálogo, categorías e integración de APIs de **Stream Zone**.

---

## 🏷️ 1. Identidad de la Tienda
- **Nombre**: Stream Zone
- **Tenant Slug**: `stream-zone-6822`
- **Plataforma backend**: NuVlyx API (`https://api.nuvlyx.com/api/v1`)
- **Autenticación**: Token bearer persistente almacenado en `~/.cache/sz_admin_token.json`.

---

## 📂 2. Categorías Principales y sus Identificadores

| Categoría | Identificador UUID (`categoryId`) | Servicios Típicos |
| :--- | :--- | :--- |
| **Streaming** | `d3f890b0-f962-46a1-9f10-13509e18800a` | Netflix, Disney+, Max, Prime Video, Spotify, YouTube Premium, Crunchyroll, Paramount+ |
| **Inteligencia Artificial** | `98afc34d-5313-4a2b-a85e-8853f9b07372` | ChatGPT Plus, Claude Pro, Midjourney, Perplexity Pro, Gemini Advanced |
| **Edición y Diseño** | `1355e9cf-37fe-460a-878c-56b693f5ea77` | Canva Pro, CapCut Pro, Freepik, Adobe Creative Cloud |
| **Items del Combo** | `2c66a095-245d-46bd-98ce-16bc21e3bc20` | Servicios combinados en paquetes especiales |

---

## 🔐 3. Estructura de Cuentas y Credenciales de Inventario

Cada licencia o cuenta cargada en inventario para venta sigue la estructura estricta:
```text
Correo: usuario@ejemplo.com; Contraseña: password123; Perfil: 1; Pin: 1234
```
- **Campos obligatorios**:
  - `Correo / Usuario`: Dirección de acceso al servicio.
  - `Contraseña`: Clave sin espacios residuales.
  - `Perfil`: Número o nombre del perfil asignado al cliente.
  - `PIN`: Código numérico de seguridad de 4 dígitos (si el servicio lo requiere).

---

## 👥 4. Contactos y Canales Clave (Objetivos VIP)
- **Stream Zone Oficial**: Canal administrativo primario para reportes diarios, cortes y alertas operativas.
- **Distribuidores**: Grupo mayorista para recargas y despachos masivos.
- **Aleja**, **Guatemala**, **Black**, **Shadow**: Contactos clave asociados a distribución y soporte.

---

## 🌐 5. Endpoints Clave de la API NuVlyx
- **Listado y detalle de productos**: `GET /products`
- **Creación de producto**: `POST /products`
- **Actualización / visibilidad**: `PATCH /products/{productId}`
- **Variaciones de precio y duración**: `POST /products/{productId}/variations`
- **Carga de inventario masivo**: `POST /inventory/licenses/bulk`
- **Gestión de recargas de saldo**: `GET/PATCH /recharges`
