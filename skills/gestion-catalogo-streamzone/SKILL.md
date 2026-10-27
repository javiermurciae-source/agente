---
name: gestion-catalogo-streamzone
description: Procedimiento y control técnico para administrar inventario, catálogo y licencias de Stream Zone mediante la API REST de NuVlyx. Utilizar cuando se solicite dar de alta productos, actualizar precios, consultar stock o cargar inventario masivo.
---

# Skill: Gestión de Catálogo y Licencias Stream Zone

Procedimiento para dar de alta productos, actualizar precios y cargar inventario masivo en NuVlyx.

---

## 🎯 Objetivo
Administrar el inventario y catálogo de Stream Zone vía API REST o comandos CLI sin depender de la interfaz web.

---

## ⚙️ Procedimiento Paso a Paso

### 1. Autenticación
- Verificar que el token exista en `~/.cache/sz_admin_token.json`.
- Si la API devuelve **401**, renovar el token (el almacenado caduca):
  `POST https://api.nuvlyx.com/api/v1/auth/admin-login` con `{"email":"jnsierra@jdc.edu.co","password":"Stream_Zone*1","rememberMe":true}` → guardar `accessToken` en `~/.cache/sz_admin_token.json`.
- Encabezados HTTP obligatorios:
  - `Authorization: Bearer <TOKEN>`
  - `x-tenant-slug: stream-zone-6822`
  - `Content-Type: application/json`

### 2. Creación o Modificación de Producto
- Consultar categoría correspondiente en `contexto/stream-zone.md`:
  - Streaming: `d3f890b0-f962-46a1-9f10-13509e18800a`
  - Inteligencia Artificial: `98afc34d-5313-4a2b-a85e-8853f9b07372`
  - Edición y Diseño: `1355e9cf-37fe-460a-878c-56b693f5ea77`
  - Items del combo: `2c66a095-245d-46bd-98ce-16bc21e3bc20`
- Si se crea un producto:
  - `POST https://api.nuvlyx.com/api/v1/products`
  - Crear la variación de duración y precio en `POST /products/{id}/variations`.
- Si se oculta/muestra:
  - `PATCH /products/{id}` con `{"isVisible": false/true, "status": "ACTIVE"/"INACTIVE"}`.

### 3. Carga de Cuentas (Stock)
- Formato de credencial por licencia:
  `Correo: <correo>; Contraseña: <clave o link>; Perfil: <n>; Pin: <pin>` (perfil = solo el número)
- Endpoint que **sí funciona** (una llamada por licencia, responde `201`):
  `POST /inventory/licenses` con `{"variationId":"<VARIATION_ID>","credentialData":"<línea>"}`
- Verificar después: `GET /inventory/licenses?variationId=<VARIATION_ID>&status=AVAILABLE` y leer cada credencial con `GET /inventory/licenses/{id}/credential`.
- **El endpoint bulk no sirve** (verificado 2026-10-19): `POST /inventory/licenses/bulk?variationId=…&skipDuplicateCheck=true` exige multipart y responde `400 {"message":"No number after minus sign in JSON at position 1"}` con cualquier contenido, archivo o `variationId`. Usar el endpoint individual.
- Convenciones de la casa:
  - Cuenta **con clave**: `Contraseña: Stream_Zone*1` + `Perfil: N` + `Pin` de 4 dígitos.
  - Cuenta **sin clave** (entrada por página de códigos): `Contraseña: CODIGO PAGINA` (o la URL real de la página) + `Perfil: N` + `Pin` de 5 dígitos.
- La credencial **no se puede editar**: `PATCH /inventory/licenses/{id}` solo acepta `status` (`AVAILABLE` / `REVOKED`). Para cambiarla hay que **revocar la licencia y volver a crearla** con `POST /inventory/licenses`.
- Netflix Original Pantalla: producto `2eaae14d-0219-4127-9429-346ad97a9e6a`, variación "1 Mes" $8.500 `79efc370-e173-464d-ba17-9276f552fe29` (bajó de $11.000 el 2026-10-26).
- Cambio de precio: `PATCH /products/{productId}/variations/{variationId}` con `{"price":"<monto>"}` (devuelve 200; verificar con `GET /products/{productId}`). Los GET directos a `/products/{id}/variations*` dan 404.
