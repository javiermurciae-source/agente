# Skill: Generación de Reportes de Vencimientos en Excel

Procedimiento paso a paso para compilar y formatear la planilla oficial de vencimientos y cortes de Stream Zone.

---

## 🎯 Objetivo
Producir un libro `.xlsx` con la plantilla corporativa azul de Stream Zone a partir de datos de órdenes, con columnas estrictamente desglosadas y fórmulas automatizadas.

---

## 📋 Columnas Obligatorias

Toda tabla de vencimientos debe contener exactamente estas 13 columnas en orden:
1. `#` (Número consecutivo)
2. `Nº ORDEN` (Identificador de orden NuVlyx)
3. `CLIENTE` (Nombre del cliente)
4. `TELÉFONO WHATSAPP` (Número con código de país)
5. `SERVICIO / PLAN` (Nombre del servicio suscrito)
6. `FECHA CORTE` (Fecha de vencimiento en formato DD/MM/AAAA)
7. `DÍAS RESTANTES` (Cálculo dinámico con alerta visual: Rojo = Hoy/Vencido, Amarillo = 1 día / Mañana, Verde = 2 a 4 días)
8. `CUENTA / USUARIO` (Correo o usuario del servicio)
9. `CONTRASEÑA` (Clave de acceso)
10. `PERFIL` (Número de perfil asignado)
11. `PIN` (PIN numérico de 4 dígitos)
12. `ESTADO COBRO` (Pagado / Pendiente / Renovado)
13. `PLANTILLA NOTIFICACIÓN WHATSAPP` (Texto listo para copiar y enviar con desglose de días restantes)

---

## ⚡ Regla Operativa de Alcance (Cortes Habituales)
- Por defecto, el corte habitual se filtra a suscripciones con vencimiento de **máximo 4 días** desde hoy (0 a 4 días restantes).
- Comando directo: `vencimientos` (ejecuta compilación, apertura en WPS Spreadsheets y despacho por WhatsApp a Stream Zone Oficial en una sola llamada).


---

## ⚙️ Procedimiento de Ejecución

1. **Recolección de Datos**:
   - Obtener las órdenes del día o del rango solicitado desde la API NuVlyx (`sz-admin orders`) o desde el archivo de entrada en `proyectos/<encargo>/`.
   - Si falta alguna contraseña o teléfono, **aplicar Regla 1**: consultar antes de inventar.

2. **Generación del Archivo**:
   - Usar el motor de Node.js o Python (`openpyxl` / `exceljs`) dentro de la subcarpeta del proyecto:
     `proyectos/<encargo>/reporte_vencimientos_<fecha>.xlsx`
   - Aplicar el estilo corporativo:
     - Encabezados: Fondo azul oscuro corporativo (`#1A365D`), texto blanco negrita.
     - Filas alternadas (estilo cebra): Blanco y azul tenue.
     - Bordes delgados y alineación centrada para orden, fechas, perfiles y pines.

3. **Verificación**:
   - Comprobar que no existan campos `undefined` o vacíos.
   - Confirmar que la columna de plantilla contenga el mensaje personalizado con el nombre y servicio del cliente.
