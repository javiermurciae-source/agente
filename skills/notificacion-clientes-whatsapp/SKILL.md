# Skill: Notificación de Clientes y Canales VIP por WhatsApp

Procedimiento paso a paso para estructurar, validar y enviar avisos de renovación o reportes de Stream Zone.

---

## 🎯 Objetivo
Garantizar que todo mensaje despachado hacia clientes individuales o canales administrativos cumpla la estructura oficial, con personalización de datos y cero margen de error en credenciales.

---

## ⚙️ Procedimiento Paso a Paso

### 1. Preparación del Mensaje
- Extraer los datos específicos del cliente:
  - Nombre
  - Servicio / Plan
  - Fecha de corte
  - Perfil y PIN
- Utilizar la plantilla oficial definida en `contexto/comunicacion.md`.
- Si algún dato falta (ej. PIN no registrado), **aplicar Regla 1**: confirmar antes de despachar.

### 2. Despacho Técnico
- Mediante el conector Baileys (`wasend`):
  ```bash
  # Para clientes individuales:
  wasend --to "<NUMERO_E164>" --msg "<MENSAJE_ESTRUCTURADO>"

  # Para reportes masivos con adjunto al canal oficial:
  wasend --to "Stream Zone Oficial" --file "<RUTA_EXCEL>" --caption "<REPORTE_ESTRUCTURADO>"
  ```

### 3. Verificación de Entrega
- El envío solo se considera exitoso si el comando termina con código de salida `0` y la confirmación de despacho.
- Registrar en el proyecto correspondiente el resultado del envío (`Entregado / Pendiente`).
