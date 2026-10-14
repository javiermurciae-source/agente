# Plantillas Maestras de Presentaciones

Este directorio almacena las plantillas de referencia (Canva, PowerPoint, PDF, HTML) que alimentan la skill `presentaciones`.

---

## 📂 Archivos en este Directorio
- `Presentación Propuesta de Proyecto Negocio Corporativo azul.pptx`: Plantilla corporativa oficial Canva con paleta Dual-Tone (Navy `#132232` + Blanco nítido `#FFFFFF`), tipografía Oswald/Plus Jakarta Sans, arquetipos de agenda con nodos, procesos en 4 fases, matriz 2x2, lista de KPIs y cronograma Gantt matricial.

---

## 🛠️ Comportamiento del Agente
1. Cuando el usuario solicite crear una presentación, el agente inspecciona este directorio para adoptar el ADN de diseño más adecuado al encargo.
2. Si se depositan nuevas plantillas (`.pptx`, `.pdf`, `.html`), el agente extraerá sus colores hexadecimales, tipografías y arquetipos modulares para enriquecer el catálogo interactivo de la skill.
3. Las presentaciones compiladas finales se guardan en `vault/presentaciones/`.
