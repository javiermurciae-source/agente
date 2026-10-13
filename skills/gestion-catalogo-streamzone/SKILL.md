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
- Encabezados HTTP obligatorios:
  - `Authorization: Bearer <TOKEN>`
  - `x-tenant-slug: stream-zone-6822`
  - `Content-Type: application/json`

### 2. Creación o Modificación de Producto
- Consultar categoría correspondiente en `contexto/stream-zone.md`:
  - Streaming: `d3f890b0-3f41-42ce-9069-b788a107310f`
  - Inteligencia Artificial: `98afc34d-17e9-4e50-93bf-478627e1f4ba`
  - Edición y Diseño: `1355e9cf-fc9d-4008-8e6d-e962bb133f38`
- Si se crea un producto:
  - `POST https://api.nuvlyx.com/api/v1/products`
  - Crear la variación de duración y precio en `POST /products/{id}/variations`.
- Si se oculta/muestra:
  - `PATCH /products/{id}` con `{"isVisible": false/true, "status": "ACTIVE"/"INACTIVE"}`.

### 3. Carga Masiva de Cuentas (Stock)
- Formato por línea:
  `Correo: <correo>; Contraseña: <clave>; Perfil: <perfil>; Pin: <pin>`
- Endpoint:
  `POST /inventory/licenses/bulk?variationId={VARIATION_ID}&skipDuplicateCheck=true`
- Validar respuesta `200/201` y verificar cantidad de licencias insertadas.
