# 👑 Guía Rápida de Administración de Stream Zone (NuVlyx)

Bienvenido a la guía oficial de administración directa desde la terminal Nix-on-Droid. Con las herramientas integradas puedes controlar productos, stock, clientes, categorías y órdenes en tiempo real sin necesidad de ingresar al navegador web.

---

## 🚀 1. Comando Principal: `sz-admin`

`sz-admin` es la herramienta interactiva oficial de gestión de la tienda. Puedes ejecutarla simplemente escribiendo en tu terminal:

```bash
sz-admin
```
*(O también `sz-admin panel`)*

### 🎮 ¿Qué puedes hacer dentro del Panel Interactivo?
1. **Ver todo el inventario**: Lista los 40+ productos, cuántas cuentas tienen en stock en tiempo real y sus precios.
2. **Consultar cuentas disponibles**: Escribes el número (`#`) del producto para ver las contraseñas, correos y pines desencriptados de las cuentas listas para venta.
3. **Cargar stock ultra-rápido**: Dentro del producto presionas `+` para subir cuentas nuevas con generación automática de pines y perfiles consecutivos.

### 📋 Subcomandos de `sz-admin`:
* **Resumen global del sistema**:
  ```bash
  sz-admin summary
  ```
  *(Muestra total de cuentas, vendidas, reservadas y disponibles).*

* **Monitoreo de órdenes y fechas de corte**:
  ```bash
  sz-admin orders --filter por_vencer
  sz-admin orders --filter vencidos
  sz-admin orders --cred --limit 20
  ```

---

## ⚡ 2. Gestión Rápida por API (Creación y Ajustes Directos)

Para crear productos nuevos, cambiar precios u ocultar servicios, la API de NuVlyx se comunica a través de comandos directos con el token administrativo automático en `~/.cache/sz_admin_token.json`.

### A. 📦 Crear un Producto Nuevo
Para dar de alta un producto en 3 pasos:

1. **Crear el producto base**:
   ```python
   # Endpoint: POST https://api.nuvlyx.com/api/v1/products
   {
     "name": "Nombre del Producto",
     "shortDescription": "Descripción corta",
     "categoryId": "ID_CATEGORIA",  # Streaming, Inteligencia Artificial, etc.
     "coverImageUrl": "URL_IMAGEN_O_DATA_URI",
     "status": "ACTIVE",
     "isVisible": True
   }
   ```

2. **Crear la variación de tiempo y precio**:
   ```python
   # Endpoint: POST https://api.nuvlyx.com/api/v1/products/{PRODUCT_ID}/variations
   {
     "name": "1 mes",        # o "3 meses"
     "price": "10000",       # Precio en pesos COP
     "dependsOnStock": True, # Control estricto de inventario
     "isActive": True,
     "durationDays": 30
   }
   ```

3. **Subir stock (Cuentas o Soporte)**:
   ```python
   # Endpoint VERIFICADO (uno por licencia, responde 201):
   # POST https://api.nuvlyx.com/api/v1/inventory/licenses
   {
     "variationId": "79efc370-e173-464d-ba17-9276f552fe29",   # Netflix Original Pantalla · 1 Mes · $11.000
     "credentialData": "Correo: mvbtykq2977@hotmail.com; Contraseña: https://13-140-173-154.sslip.io/codigos/; Perfil: 1; Pin: 00773"
   }
   # Formato de la credencial: Correo; Contraseña; Perfil: N; Pin  (N = solo el número del perfil)
   # Verificar: GET /inventory/licenses?variationId=…&status=AVAILABLE
   #            GET /inventory/licenses/{id}/credential
   #
   # ⚠️ El endpoint bulk NO funciona (verificado 2026-10-19): pide multipart y
   #    responde 400 "No number after minus sign in JSON at position 1".
   #    Para carga masiva, iterar el endpoint individual en un bucle.
   ```

   **Convenciones de credenciales de la casa:**
   - Cuenta **con clave**: `Contraseña: Stream_Zone*1` + `Perfil: N` + `Pin` de 4 dígitos.
   - Cuenta **sin clave** (entrada por la página de códigos): `Contraseña: CODIGO PAGINA` o la URL real de la página + `Perfil: N` + `Pin` de 5 dígitos.

   **Productos de referencia (verificados 2026-10-19):**
   | Producto | productId | Variación | Precio |
   |---|---|---|---|
   | Netflix Original Pantalla | `2eaae14d-0219-4127-9429-346ad97a9e6a` | `79efc370-e173-464d-ba17-9276f552fe29` (1 Mes) | $11.000 |
   | Netflix Perfil Extra | `d129c69e-6996-4ab2-91ba-9be2103d6b21` | `13cbaae6-8ed8-43dc-9bfd-c28d2a0fd351` (1 mes) | $16.000 |
   | Netflix Renovable | `7fccf67d-5982-4f92-9d01-0c0334e0ee71` | `544c488a-f365-4d8f-a420-56f7ffde3b78` (1 mes) | $11.000 |

> 🔑 **Token**: el `accessToken` de `~/.cache/sz_admin_token.json` caduca. Si la API responde **401**, renovarlo con
> `POST https://api.nuvlyx.com/api/v1/auth/admin-login` → `{"email":"jnsierra@jdc.edu.co","password":"Stream_Zone*1","rememberMe":true}`
> y guardar el nuevo `accessToken` en el mismo archivo.

---

### B. 👁️ Ocultar o Desactivar un Producto
Si no deseas vender un producto o quieres retirarlo temporalmente de la tienda pública:
```bash
# PATCH https://api.nuvlyx.com/api/v1/products/{PRODUCT_ID}
{"status": "INACTIVE", "isVisible": false}
```

### C. 🟢 Reactivar un Producto
Para que vuelva a verse en la tienda pública:
```bash
# PATCH https://api.nuvlyx.com/api/v1/products/{PRODUCT_ID}
{"status": "ACTIVE", "isVisible": true}
```

---

## 📂 3. Categorías Actuales de la Tienda

Cada producto debe tener asociado su `categoryId`:

| Categoría | ID de Categoría | Productos que agrupa |
| :--- | :--- | :--- |
| 🤖 **Inteligencia Artificial** | `98afc34d-5313-4a2b-a85e-8853f9b07372` | QuillBot, iLovePDF, ChatGPT, Gemini, Canva |
| ✂️ **Edición y Diseño** | `1355e9cf-37fe-460a-878c-56b693f5ea77` | CapCut Pro (Perfil), CapCut Pro (Completa) |
| 📺 **Streaming** | `d3f890b0-f962-46a1-9f10-13509e18800a` | Netflix, YouTube, Spotify, DirecTV, Disney, HBO, IPTV |
| 🍱 **Items del combo** | `2c66a095-245d-46bd-98ce-16bc21e3bc20` | Combos multipantalla |

---

## 📢 4. Notificaciones y WhatsApp (`wasend`)

Para avisar a los clientes o al grupo de distribuidores:

* **Enviar mensaje directo al grupo de Distribuidores**:
  ```bash
  wasend --to "Distribuidores Stream Zone 🔥" --msg "Mensaje aquí"
  ```
* **Enviar imagen con comunicado**:
  ```bash
  wasend --to "Distribuidores Stream Zone 🔥" --file "~/storage/pictures/imagen.png" --caption "Texto aquí"
  ```

---

💡 *Stream Zone • Entorno Nix-on-Droid optimizado para Camilo.*
