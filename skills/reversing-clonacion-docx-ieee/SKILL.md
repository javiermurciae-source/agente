---
name: reversing-clonacion-docx-ieee
description: Ingeniería inversa, deconstrucción, clonación y generación automatizada de informes académicos y profesionales en formato IEEE (.docx) para UNISANGIL (Redes / Comunicación de Datos).
---

# Skill: Reversing y Clonación de Informes IEEE (.docx)

Esta habilidad permite realizar ingeniería inversa a documentos Word (`.docx`), extrayendo su estructura OpenXML, tipografía, imágenes, tablas y estilos de dos columnas (IEEE), para luego replicarlos o generar nuevos informes académicos con máxima fidelidad visual y cero intervención manual.

---

## 🎯 Capacidades Principales

1. **Deconstrucción y Análisis (`docx_extractor.py`)**:
   - Inspecciona archivos `.docx` analizando secciones, división de columnas (1 columna para cabecera, 2 columnas para el cuerpo).
   - Extrae todas las imágenes incrustadas (capturas de PuTTY, diagramas de Packet Tracer, fotos físicas).
   - Extrae tablas de direccionamiento IPv4 y las convierte a estructuras manipulables.
2. **Generación y Clonación de Alta Precisión (`ieee_doc_builder.py`)**:
   - Compila nuevos documentos `.docx` con la plantilla oficial de UNISANGIL.
   - Respeta los estilos IEEE estrictos:
     - Tipografía: *Times New Roman* (24pt Título, 10pt Texto justificado, 9pt Abstract/Keywords, 8pt Tablas y Figuras).
     - Cabecera: Título en Español e Inglés, autores (*Bernal, Dana., Reyes, Andrey y Murcia, Camilo*), filiación (*UNISANGIL*), correos y fechas.
     - Cuerpo: Formato a 2 columnas con separación exacta de 258 dxa.
     - Tablas IEEE: Bordes superior e inferior sólidos, sin líneas verticales, texto centrado a 8pt.
     - Figuras: Centradas con numeración consecutiva (`Fig. 1. ...`).
     - Referencias: Formato numérico IEEE `[1], [2]` con sangría francesa.

---

## 🛠️ Herramientas de la Habilidad

Las herramientas residen en `skills/reversing-clonacion-docx-ieee/scripts/`:

```bash
# 1. Analizar cualquier documento .docx existente
python3 skills/reversing-clonacion-docx-ieee/scripts/docx_extractor.py <archivo.docx> [--out /ruta/reporte]

# 2. Generar un informe nuevo a partir de una especificación JSON
python3 skills/reversing-clonacion-docx-ieee/scripts/ieee_doc_builder.py <spec.json> --out <resultado.docx> [--view]
```

---

## 📋 Estructura de la Especificación JSON

Para crear un nuevo laboratorio, define un archivo JSON con esta estructura:

```json
{
  "title_es": "Configuración de Enrutamiento Dinámico OSPF",
  "title_en": "Dynamic OSPF Routing Configuration in Multi-Area Networks",
  "authors": "Bernal, Dana., Reyes, Andrey y Murcia, Camilo",
  "institution": "Fundación Universitaria de San Gil (UNISANGIL)",
  "course": "Asignatura Comunicación de Datos",
  "city": "San Gil, Colombia",
  "emails": [
    "danabernal222@unisangil.edu.co",
    "andreyreyes@unisangil.edu.co",
    "camilomurcia@unisangil.edu.co"
  ],
  "dates": {
    "reception": "Fecha de Recepción: 6 de octubre de 2026",
    "acceptance": "Fecha de Aceptación: Pendiente"
  },
  "abstract_es": "Resumen en español del laboratorio...",
  "keywords_es": "Cisco IOS, enrutamiento, OSPF, Packet Tracer.",
  "abstract_en": "English abstract...",
  "keywords_en": "Cisco IOS, OSPF, Packet Tracer, routing.",
  "sections": [
    {
      "title": "I. INTRODUCCIÓN",
      "paragraphs": [
        "Primer párrafo explicativo...",
        "Segundo párrafo..."
      ]
    },
    {
      "title": "II. METODOLOGÍA",
      "paragraphs": ["Descripción del procedimiento..."],
      "tables": [
        {
          "title": "TABLA I. ASIGNACIÓN DE DIRECCIONES IP",
          "headers": ["Dispositivo", "Interfaz", "Dirección IP", "Máscara"],
          "rows": [
            ["R1", "G0/0", "192.168.1.1", "255.255.255.0"],
            ["PC-A", "NIC", "192.168.1.10", "255.255.255.0"]
          ]
        }
      ],
      "figures": [
        {
          "image": "/ruta/a/captura_packet_tracer.png",
          "caption": "Fig. 1. Topología lógica implementada en Cisco Packet Tracer.",
          "width_pt": 220,
          "height_pt": 150
        }
      ]
    },
    {
      "title": "III. CONCLUSIONES",
      "paragraphs": ["Conclusión 1...", "Conclusión 2..."]
    }
  ],
  "references": [
    "Cisco Networking Academy, \"CCNA Routing and Switching\", Cisco Press, 2020.",
    "W. Odom, \"CCNA 200-301 Official Cert Guide\", Cisco Press, 2020."
  ]
}
```

---

## 🚀 Flujo de Trabajo para Nuevas Entregas

1. **Recepción del enunciado / guía de laboratorio**: Extraer los requerimientos, topología y comandos.
2. **Generación del borrador o carga de evidencias**: Reunir las capturas de PuTTY / Packet Tracer y la tabla IP.
3. **Compilación automática**: Ejecutar `ieee_doc_builder.py` para producir el `.docx` en menos de 1 segundo.
4. **Verificación visual**: Abrir el documento en WPS Office o visor compatible para revisión final.
