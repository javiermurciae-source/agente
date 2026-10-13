# Directorio Central de Plantillas (Templates)

Espacio centralizado del agente para almacenar, versionar y clonar plantillas maestras reutilizables en múltiples proyectos y formatos (.docx, .pptx, .pdf, .html, etc.).

---

## 📂 Organización por Categorías

- `apa7/`
  - Plantillas académicas en formato APA 7ma edición (márgenes de 1 pulgada, interlineado doble, portada institucional, citas y referencias bibliográficas).
- `ieee/`
  - Plantillas de ingeniería y artículos científicos en doble columna (tipografía Times New Roman, espaciado 258 dxa, encabezados numerados y tablas centradas).
  - Incluye `ieee_template_unisangil.docx` para Comunicación de Datos / Redes.
- `documentos/`
  - Plantillas para actas de reunión, contratos, propuestas comerciales, informes técnicos de ciberseguridad (SecureDesk) y reportes ejecutivos.
- `presentaciones/`
  - Plantillas para decks PowerPoint (.pptx / .potx) y presentaciones interactivas web (.html 16:9).

---

## 💡 Cómo usa el agente estas plantillas
1. **Clonación quirúrgica**: Al generar un nuevo documento, el agente no sobrescribe la plantilla maestra; desempaqueta el archivo o clona la estructura y genera la copia final en el directorio de destino (`~/Documentos/`, `~/Descargas/` o el proyecto activo).
2. **Preservación de estilos**: Utiliza las skills correspondientes ([`docx`](file:///home/rootkit/agente/skills/docx/), [`pptx`](file:///home/rootkit/agente/skills/pptx/), [`reversing-clonacion-docx-ieee`](file:///home/rootkit/agente/skills/reversing-clonacion-docx-ieee/)) respetando exactamente la tipografía, jerarquía de títulos y colores institucionales.
