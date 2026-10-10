#set page(paper: "us-letter", margin: (x: 1.8cm, top: 1.8cm, bottom: 2.0cm),
  header: align(right)[#text(size: 8pt, fill: rgb("#666666"))[SecureDesk — Dark Códex & SigmaEntretenimiento]],
  footer: [
    #grid(columns: (1fr, 1fr),
      align(left)[#text(size: 8pt, fill: rgb("#777777"))[Proyecto de Ciberseguridad & Gestión SOC]],
      align(right)[#text(size: 8pt, fill: rgb("#777777"))[Página #context counter(page).display("1")]])
  ]
)
#set text(font: "DejaVu Sans", size: 9pt, lang: "es")
#set par(justify: true, leading: 0.65em)

#align(center)[
  #text(size: 19pt, weight: "bold", fill: rgb("#23476A"))[PROYECTO SECUREDESK]
  #v(2pt)
  #text(size: 13pt, weight: "bold", fill: rgb("#333333"))[Asignación de Roles & Actas Oficiales de Reunión]
  #v(2pt)
  #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[Dark Códex (Desarrollador) & SigmaEntretenimiento (Cliente) | Ciclo Agosto – Noviembre 2026]
]
#v(12pt)

== 1. Asignación Oficial de Roles del Proyecto
#v(4pt)
#table(
  columns: (1fr, 1fr),
  fill: (col, row) => if row == 0 { rgb("#23476A") } else if calc.even(row) { rgb("#f8fafc") } else { rgb("#ffffff") },
  stroke: (x, y) => if y == 0 { (bottom: 1.5pt + rgb("#23476A")) } else { (bottom: 0.5pt + rgb("#e2e8f0")) },
  align: (col, row) => if row == 0 { center } else { left },
  table.header([#text(fill: white, weight: "bold")[Roles]], [#text(fill: white, weight: "bold")[Actores]]),
  [*Programador*], [Camilo Murcia],
  [*Cliente*], [SigmaEntretenimiento],
  [*Encargado de seguimiento (Tracker - Git)*], [Pedronel GarciaForero Mateus],
  [*Encargado de pruebas (Tester)*], [Daniel Stiven mateus Marin],
  [*Líder de Proyecto (Project Manager)*], [Juan Daniel Oviedo],
  [*Líder de Análisis de Negocio y Requerimientos*], [Juan Carlos Marin],
  [*Entrenador (Coach Ágil)*], [Jhon martin perez],
  [*Consultor de Ciberseguridad (Especialista SOC)*], [kevin Mitnick],
  [*Administrador de Infraestructura y Active Directory (DevOps)*], [Daniel Stiven Forero Mateus],
  [*Arquitecto de Software y Base de Datos*], [Juan Carlos Marin],
  [*Big Boss*], [Eduard bernal],
)
#v(10pt)
=== Descripción Técnica de Responsabilidades por Rol en SecureDesk
#v(4pt)
*• 1. Programador* (#text(style: "italic", fill: rgb("#23476A"))[Camilo Murcia]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Responsable directo de la construcción, desarrollo y codificación del software SecureDesk. Programa los módulos de registro, reporte, clasificación y atención de incidentes de ciberseguridad, así como la lógica de negocio y la integración con las APIs del sistema.]]
#v(2pt)
*• 2. Cliente* (#text(style: "italic", fill: rgb("#23476A"))[SigmaEntretenimiento]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Organización cliente y destinataria del sistema. Define las necesidades operativas de seguridad de la información, prioriza los requisitos funcionales del software, evalúa los avances entregados en cada iteración y otorga la aceptación formal del producto final.]]
#v(2pt)
*• 3. Encargado de seguimiento (Tracker - Git)* (#text(style: "italic", fill: rgb("#23476A"))[Pedronel GarciaForero Mateus]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Encargado de la trazabilidad y seguimiento del proyecto utilizando Git. Administra el repositorio central, flujo de trabajo en ramas (Git Flow), revisión de commits, pull requests, gestión del tablero de incidencias (issues), hitos (milestones) y métricas de avance del equipo.]]
#v(2pt)
*• 4. Encargado de pruebas (Tester)* (#text(style: "italic", fill: rgb("#23476A"))[Daniel Stiven mateus Marin]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Planifica, diseña y ejecuta los planes de prueba funcionales, unitarias y de integración. Evalúa los flujos de autenticación, la carga de reportes y la gestión del ciclo de vida de los incidentes para garantizar calidad, estabilidad y seguridad sin errores.]]
#v(2pt)
*• 5. Líder de Proyecto (Project Manager)* (#text(style: "italic", fill: rgb("#23476A"))[Juan Daniel Oviedo]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Lidera la coordinación general, asignación de responsabilidades, control de cronograma y mitigación de riesgos del proyecto. Actúa como canal principal de comunicación entre la gerencia de Dark Códex y el cliente SigmaEntretenimiento.]]
#v(2pt)
*• 6. Líder de Análisis de Negocio y Requerimientos* (#text(style: "italic", fill: rgb("#23476A"))[Juan Carlos Marin]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Responsable de la captura, especificación técnica y validación de los requerimientos del sistema. Define las reglas de negocio, los casos de uso, las matrices de clasificación por riesgo y los flujos de trabajo de los incidentes de ciberseguridad.]]
#v(2pt)
*• 7. Entrenador (Coach Ágil)* (#text(style: "italic", fill: rgb("#23476A"))[Jhon martin perez]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Facilita la adopción y cumplimiento de las prácticas metodológicas ágiles en el equipo de desarrollo. Asesora en las reuniones de sincronización, optimiza la productividad colectiva y ayuda a remover impedimentos y bloqueos técnicos u operativos.]]
#v(2pt)
*• 8. Consultor de Ciberseguridad (Especialista SOC)* (#text(style: "italic", fill: rgb("#23476A"))[kevin Mitnick]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Experto en seguridad que asesora en la clasificación de severidad de incidentes, taxonomía de amenazas, monitoreo de alertas, protocolos de contención y políticas defensivas de ciberseguridad para el entorno empresarial. Actúa como Autor de las actas de reunión.]]
#v(2pt)
*• 9. Administrador de Infraestructura y Active Directory (DevOps)* (#text(style: "italic", fill: rgb("#23476A"))[Daniel Stiven Forero Mateus]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Gestiona los servidores de aplicación y base de datos, la configuración del entorno web, la integración con Active Directory (LDAP) para la validación y gestión de usuarios y equipos, así como el despliegue continuo y la seguridad de la red.]]
#v(2pt)
*• 10. Arquitecto de Software y Base de Datos* (#text(style: "italic", fill: rgb("#23476A"))[Juan Carlos Marin]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Diseña la estructura técnica, componentes y patrones de diseño de la aplicación web SecureDesk. Modela el esquema relacional de la base de datos para usuarios, roles, activos tecnológicos, eventos, incidentes y pistas de auditoría.]]
#v(2pt)
*• 11. Big Boss* (#text(style: "italic", fill: rgb("#23476A"))[Eduard bernal]):
#block(inset: (left: 12pt))[#text(size: 8.5pt)[Máxima autoridad ejecutiva y patrocinador principal del proyecto. Define los objetivos estratégicos de alto nivel, asigna el presupuesto y recursos institucionales, y supervisa el cumplimiento global de los acuerdos contractuales.]]
#v(2pt)
#pagebreak()

== 2. Actas Oficiales de Reunión de Seguimiento (Ciclo Completo)
#v(6pt)
=== Acta de Reunión No. 1
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Kick-off, inicio del proyecto SecureDesk y definición de arquitectura base],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [06/08/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 1]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de conferencias Dark Códex / Sesión virtual de ingeniería],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito y justificación estratégica del sistema SecureDesk\
– Alcance del producto e integración con Active Directory\
– Objetivos del proyecto y metas de ciberseguridad corporativa\
– Funciones requeridas de la plataforma y módulos base\
– Tecnologías y arquitectura a utilizar en el ecosistema\
– Metodología de desarrollo ágil y gestión en Git (Tracker)]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Se formalizó que la organización cliente SigmaEntretenimiento enfrenta desafíos críticos en la detección, registro y seguimiento oportuno de eventos de seguridad que puedan vulnerar la confidencialidad, integridad y disponibilidad de sus activos digitales. El proyecto SecureDesk busca transformar la gestión reactiva de incidentes en una operación centralizada, estructurada y automatizada, ofreciendo trazabilidad completa desde la identificación de una amenaza hasta su resolución y cierre definitivo.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[SecureDesk será implementado como una plataforma web empresarial diseñada específicamente para registrar, clasificar, monitorear y gestionar incidentes de ciberseguridad para el entorno del Directorio Activo (Active Directory) de SigmaEntretenimiento. El sistema coexistirá armónicamente con la infraestructura de red de Dark Códex y los servidores dedicados de aplicación y base de datos, garantizando accesibilidad desde equipos cliente Windows 10/11, Linux y macOS mediante navegadores modernos.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Centralizar y organizar la gestión de incidentes de ciberseguridad para facilitar su atención y resolución oportuna.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Mejorar la trazabilidad de los incidentes y facilitar la asignación inequívoca de responsables técnicos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Reducir la pérdida de información y habilitar la consulta en tiempo real del estado de cada caso de seguridad.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Fortalecer la gestión interna de seguridad manteniendo un historial inmutable de eventos para la toma de decisiones estratégicas.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Inicio de sesión y control de acceso seguro mediante autenticación federada.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Estructuración de roles de usuario iniciales: Empleado (reporte y consulta), Analista SOC (gestión e investigación) y Administrador (políticas y configuración).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Módulo base para la captura estructurada de incidentes de seguridad.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Visualización preliminar del estado de salud del sistema y componentes de red.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Backend: Python con FastAPI / Node.js para servicios web RESTful de alto rendimiento y arquitectura modular.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Frontend: React con interfaz moderna, adaptable y compatible con Chrome, Microsoft Edge y Firefox.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Base de datos: PostgreSQL para almacenamiento seguro de usuarios, roles, activos, incidentes y pistas de auditoría.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Integración de Directorio: Protocolo LDAPS sobre Windows Server Active Directory.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Control de Versiones: Git bajo la metodología Git Flow administrado en repositorio central por el Tracker.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Se seleccionó la Metodología Ágil (XP - Extreme Programming en conjunto con Scrum) para garantizar máxima adaptabilidad, entregas iterativas por historias de usuario de 6 a 8 días de esfuerzo, programación disciplinada y comunicación permanente con el cliente SigmaEntretenimiento.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Configurar el entorno de desarrollo web e iniciar la programación de los módulos base de autenticación.\
*Juan Carlos Marin*: Documentar los requerimientos funcionales y formalizar la matriz de casos de uso de la Historia 1.\
*Pedronel GarciaForero Mateus*: Inicializar el repositorio Git con las ramas principales main y develop, estableciendo las políticas de pull requests.\
*Daniel Stiven Forero Mateus*: Desplegar el servidor de aplicación y aprovisionar la base de datos para pruebas locales.\
*SigmaEntretenimiento*: Suministrar los parámetros de conectividad y directrices de seguridad de la red corporativa.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[20/08/2026 – Sala de reuniones Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 2
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Autenticación, validación de usuarios con Active Directory y gestión de identidades],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [20/08/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 2]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de juntas Dark Códex – Piso 3],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito de la integración de identidades corporativas con Active Directory\
– Alcance de la sincronización de credenciales y cuentas de dominio\
– Objetivos abordados en la Iteración 2 (Historia 2 de desarrollo)\
– Funciones requeridas de autenticación LDAP y control de acceso\
– Tecnologías y protocolos criptográficos implementados\
– Metodología de pruebas unitarias y seguimiento del sprint en Git]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Establecer un mecanismo de autenticación centralizado y robusto que permita a los colaboradores de SigmaEntretenimiento acceder a SecureDesk utilizando sus credenciales corporativas existentes de Active Directory, eliminando la duplicidad de contraseñas y mitigando riesgos de suplantación de identidad o almacenamiento inseguro de credenciales.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Módulo de enlace directo entre el backend de SecureDesk y el controlador de dominio Active Directory mediante protocolo seguro LDAPS, gestionando la validación en tiempo real de credenciales, mapeo de atributos de usuario y asignación inicial de sesiones seguras.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Validar usuarios y grupos corporativos directamente contra Active Directory sin almacenar claves locales.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Garantizar el cifrado de todas las transacciones de autenticación mediante canales seguros TLS/SSL.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Establecer la base para la sincronización automática de metadatos de usuario (nombre, cargo, departamento, equipo).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Completar y certificar al 100% la Historia 2 del cronograma general de iteraciones.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Validación de credenciales de usuario contra el catálogo global de Active Directory.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Emisión y gestión de tokens seguros de sesión JWT con expiración temporal controlada.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Detección y bloqueo temporal de cuentas ante intentos fallidos reiterados de inicio de sesión.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Registro automático en bitácora de auditoría de cada intento de acceso exitoso o fallido.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Protocolo de directorio: LDAPS (LDAP sobre SSL/TLS) a través del puerto seguro 636.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Librerías de autenticación: ldap3 / python-ldap optimizadas para consultas asíncronas.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Seguridad de sesión: Tokens JWT firmados con algoritmo asimétrico RSA-256.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Servidor de pruebas: Controlador de dominio simulado en Windows Server 2022.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Desarrollo guiado por pruebas (TDD) implementado por el Programador Camilo Murcia, con verificación formal por el Tester Daniel Stiven mateus Marin (100% de casos de autenticación aprobados) y merge verificado en Git por el Tracker.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Implementar la capa de persistencia para perfiles y metadatos de usuarios sincronizados.\
*Daniel Stiven mateus Marin*: Diseñar y ejecutar la batería de pruebas de carga sobre el endpoint de inicio de sesión.\
*kevin Mitnick*: Auditar la configuración criptográfica de los certificados SSL y el manejo de tokens JWT.\
*Pedronel GarciaForero Mateus*: Aprobar el merge de la rama feature/ad-auth a la rama de integración develop en Git.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[07/09/2026 – Sala de conferencias Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 3
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Gestión de roles, permisos RBAC y visualización de equipos del dominio],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [07/09/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 3]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de reuniones Dark Códex / Enlace con SigmaEntretenimiento],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito de la administración de roles RBAC y visualización de activos\
– Alcance del inventario dinámico de usuarios y equipos del dominio\
– Objetivos abordados en las Iteraciones 3, 4 y 5 de desarrollo\
– Funciones requeridas de control de permisos y visualización de computadores\
– Tecnologías de consulta LDAP y diseño de interfaz gráfica\
– Metodología ágil y métricas de avance del repositorio en Git]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Garantizar una estricta segregación de funciones mediante el modelo de control de acceso basado en roles (RBAC) y brindar visibilidad en tiempo real de todos los computadores y estaciones de trabajo registradas en el Active Directory, permitiendo correlacionar usuarios con sus equipos físicos para una rápida respuesta ante incidentes.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Módulo administrativo que permite consultar y listar usuarios y equipos del dominio corporativo, asociando privilegios específicos para Empleados, Analistas SOC y Administradores, e incorporando vistas de inventario tecnológico conectadas en vivo con Active Directory.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Implementar control de acceso granular asegurando el principio de menor privilegio.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Visualizar en el panel web los equipos clientes (Windows, Linux, macOS) conectados al dominio.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Vincular las cuentas de usuario corporativo con sus estaciones de trabajo asignadas.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Consolidar las Historias 3, 4 e iniciar con éxito la Historia 5 del plan de iteraciones.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Matriz de privilegios diferenciada: Empleado (reporte), Analista SOC (gestión técnica), Administrador (control total).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Catálogo visual de computadores del dominio con detalles de sistema operativo, dirección IP y estado.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Filtros de búsqueda avanzada de activos por departamento, nombre de equipo o usuario asignado.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Mecanismo de sincronización periódica de objetos de equipo desde Active Directory.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Frontend: Componentes de tablas con paginación reactiva, filtros dinámicos y ordenamiento en React.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Backend: Consultas de directorio filtradas por objectClass=computer y objectClass=user.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Base de datos: Tablas relacionales normalizadas para roles, permisos y caché de equipos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Seguridad: Middleware de autorización que intercepta cada solicitud HTTP y valida permisos RBAC.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Prácticas de Programación en Parejas (Pair Programming) promovidas por el Coach Ágil Jhon martin perez. El Tracker Pedronel GarciaForero Mateus reportó 52 commits acumulados y cumplimiento del cronograma al 35% sin retrasos.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Comenzar el desarrollo del módulo central de Registro de incidentes (Historias 6 y 7).\
*Juan Carlos Marin*: Definir los campos obligatorios del formulario de reporte de incidentes y taxonomía de categorías.\
*Daniel Stiven Forero Mateus*: Optimizar la memoria caché de consultas LDAP para reducir la latencia de respuesta.\
*SigmaEntretenimiento*: Revisar y aprobar la interfaz de usuario del inventario de equipos y usuarios.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[25/09/2026 – Sala de juntas Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 4
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Evaluación, validación y entrega formal del PRIMER 50% del proyecto SecureDesk],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [25/09/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 4]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de conferencias principal Dark Códex],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito y consolidación del PRIMER 50% de desarrollo de SecureDesk\
– Alcance de los módulos de Registro y Reporte de incidentes de seguridad\
– Objetivos del proyecto alcanzados en las Historias 1 a 8\
– Funciones requeridas validadas en la demostración en vivo ante el cliente\
– Tecnologías de captura de evidencias y almacenamiento transaccional\
– Metodología, auditoría de calidad y firma del hito intermedio del 50%]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Evaluar formalmente, verificar y entregar a entera satisfacción del cliente SigmaEntretenimiento el primer hito mayor del proyecto (50% de avance físico y funcional), certificando la operatividad de los módulos de autenticación Active Directory, gestión de roles, inventario de activos y el sistema de registro y reporte de incidentes.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Entrega y despliegue funcional de la versión beta intermedio de SecureDesk que habilita a cualquier empleado reportar incidentes de seguridad informática, adjuntar evidencias, asociar el computador afectado y consultar el estado preliminar de su caso.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Completar al 100% las 8 primeras historias de usuario e iteraciones planificadas (Hito 50% del proyecto).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Permitir el reporte estructurado de eventos de seguridad por parte de los usuarios finales.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Garantizar la captura fidedigna de evidencias y metadatos técnicos en cada reporte.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Auditar y certificar la estabilidad general del sistema antes de pasar a la fase de clasificación avanzada.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Formulario intuitivo de reporte de incidentes con categorización preliminar guiada.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Carga segura de evidencias digitales (capturas de pantalla, archivos de registro) con cálculo de hash SHA-256.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Notificación automática a la cola de entrada del SOC tras el envío de un incidente.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Panel de consulta para el empleado donde visualiza el historial de sus casos reportados.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Almacenamiento de archivos: Repositorio encriptado con validación estricta de extensiones y tipos MIME.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Base de datos: Transacciones ACID en PostgreSQL para registro íntegro de incidentes y archivos adjuntos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Control de versiones: Etiqueta de versión oficial v0.5.0-beta creada en la rama main de Git.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Integración continua: Ejecución automática de pruebas de regresión en cada commit.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Demostración en vivo efectuada por Camilo Murcia ante los directivos de SigmaEntretenimiento y el Big Boss Eduard bernal. El informe de pruebas entregado por el Tester certificó 84 pruebas superadas con éxito. Firma oficial del acta de aprobación del primer 50% del proyecto.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Iniciar la programación de los algoritmos de clasificación y priorización por riesgo (Historias 9 y 10).\
*kevin Mitnick*: Suministrar la matriz técnica de severidad, factores de impacto y reglas de correlación SOC.\
*Pedronel GarciaForero Mateus*: Consolidar la rama release/0.5.0 y habilitar las ramas de trabajo para la segunda mitad del proyecto.\
*Eduard bernal*: Firmar el acta de conformidad del 50% y autorizar el inicio del segundo ciclo de desarrollo.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[09/10/2026 – Sala de reuniones Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 5
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Arranque de la Segunda Mitad (Segundo 50%): Clasificación y priorización de incidentes],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [09/10/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 5]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de juntas Dark Códex – Piso 2],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito del motor de clasificación y priorización por nivel de riesgo\
– Alcance del análisis de severidad de amenazas e impacto en el negocio\
– Objetivos abordados en las Iteraciones 9 y 10 (Segundo 50% del proyecto)\
– Funciones requeridas de ponderación automática y cola de atención SOC\
– Tecnologías de algoritmos de scoring y taxonomía de ciberseguridad\
– Metodología de trabajo conjunto con el especialista SOC y seguimiento en Git]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Iniciar con determinación el segundo 50% de desarrollo implementando la inteligencia de ciberseguridad de SecureDesk, permitiendo al sistema clasificar de forma automatizada los incidentes reportados y priorizar su orden de atención en función de la gravedad técnica de la amenaza y la criticidad del activo comprometido.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Motor analítico en backend que clasifica incidentes en cuatro niveles de riesgo (Bajo, Medio, Alto, Crítico) y ordena dinámicamente la cola de trabajo del Centro de Operaciones de Seguridad (SOC) para asegurar que las contingencias graves se atiendan de manera inmediata.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Clasificar incidentes según su nivel de riesgo y vector de ataque (malware, phishing, accesos no autorizados).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Priorizar la atención de eventos considerando la importancia del activo en el Active Directory.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Reducir los tiempos de respuesta inicial ante amenazas críticas que pongan en riesgo la operación.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Desarrollar y validar formalmente las Historias 9 y 10 del cronograma.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Algoritmo de cálculo de criticidad que combina impacto, probabilidad y criticidad del activo.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Semáforo visual de severidad (Verde, Amarillo, Naranja, Rojo) en la lista de incidentes del SOC.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Reordenamiento automático en tiempo real de la bandeja de incidentes pendientes.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Alertas sonoras y visuales inmediatas para incidentes tipificados como Críticos.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Algoritmo de evaluación: Implementación basada en el estándar CVSS v3.1 adaptado a entornos internos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Backend: Servicios de cálculo de severidad con procesamiento en segundo plano.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Base de datos: Índices optimizados en PostgreSQL para ordenamiento instantáneo por severidad y fecha.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Frontend: Notificaciones toast reactivas y badges de estado actualizados en tiempo real.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Diseño de matrices de riesgo guiado por el Consultor de Ciberseguridad kevin Mitnick y codificado por Camilo Murcia. Sesión de retrospectiva de iteración facilitada por Jhon martin perez para afinar los tiempos de respuesta del equipo.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Desarrollar los mecanismos de asignación automática y manual de incidentes a analistas SOC.\
*Daniel Stiven mateus Marin*: Diseñar pruebas automatizadas simulando ráfagas de incidentes de diferente criticidad.\
*Daniel Stiven Forero Mateus*: Configurar índices de alto rendimiento en la base de datos para consultas de ordenación masiva.\
*SigmaEntretenimiento*: Definir los tiempos objetivo de atención (SLA) para cada nivel de criticidad.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[23/10/2026 – Sala de reuniones Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 6
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Asignación, ciclo de vida de incidentes y gestión de activos tecnológicos],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [23/10/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 6]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de reuniones Dark Códex / Sesión virtual con SigmaEntretenimiento],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito del flujo de trabajo y ciclo de vida de incidentes de seguridad\
– Alcance de la asignación a analistas SOC, investigación y remediación\
– Objetivos abordados en las Iteraciones 11 y 12 de desarrollo\
– Funciones requeridas de asignación de casos, notas forenses y cierre técnico\
– Tecnologías de máquinas de estado finito y vinculación con activos\
– Metodología de integración continua y métricas de avance en Git (Tracker)]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Estructurar y estandarizar el ciclo de vida completo de cada incidente de seguridad dentro del SOC, asegurando que cada caso sea asignado a un analista competente, investigado con trazabilidad forense, mitigado con acciones concretas sobre los activos afectados y cerrado formalmente con documentación de causa raíz.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Módulo de gestión del ciclo de vida del incidente que soporta transiciones de estado formales, notas de investigación confidenciales, vinculación con el inventario de activos del Active Directory y emisión de recomendaciones preventivas.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Asignar responsables técnicos a cada incidente según disponibilidad y especialidad.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Permitir el seguimiento del ciclo de vida: Registrado → En Análisis → En Mitigación → Cerrado.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Asociar las acciones técnicas de contención con los activos tecnológicos de la empresa.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Completar satisfactoriamente las Historias 11 y 12 alcanzando el 75% del cronograma general.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Asignación de tickets tanto de forma manual por el líder SOC como por asignación balanceada automática.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Línea de tiempo de eventos con bitácora interna de acciones forenses y hallazgos técnicos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Registro de medidas de contención (ej. desconexión de red de estación, bloqueo de usuario en AD).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Formulario de cierre formal con categorización de causa raíz y recomendaciones preventivas.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Arquitectura: Máquina de estados finitos (State Machine) implementada en backend para evitar transiciones ilegales.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Integración con Directorio: Posibilidad de invocar comandos de consulta de estado del equipo en Active Directory.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Control de versiones: 125 commits consolidados en Git con verificación automática de pruebas en GitHub Actions.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Frontend: Panel interactivo tipo Kanban y vista de detalle de incidente con historial cronológico.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Flujo continuo de integración y despliegue (CI/CD) supervisado por Pedronel GarciaForero Mateus. Pruebas de usabilidad satisfactorias con los futuros analistas SOC de SigmaEntretenimiento.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Programar los módulos de historial inmutable de auditoría y generación de reportes ejecutivos.\
*Juan Carlos Marin*: Diseñar las plantillas corporativas de los reportes gerenciales en formatos PDF y Excel.\
*kevin Mitnick*: Definir los indicadores clave de rendimiento (MTTR, MTTD) para el Dashboard SOC.\
*Daniel Stiven mateus Marin*: Ejecutar pruebas de regresión sobre todo el ciclo de transición de estados de incidentes.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[06/11/2026 – Sala de juntas Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 7
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Historial de auditoría, panel interactivo SOC y generación de reportes],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [06/11/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 7]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de juntas Dark Códex – Piso 3],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito de las pistas de auditoría inmutables y reportería ejecutiva\
– Alcance del Dashboard SOC centralizado y exportación de informes\
– Objetivos abordados en las Iteraciones 13 y 14 de desarrollo\
– Funciones requeridas de auditoría, visualización analítica y reportes\
– Tecnologías de exportación de documentos (PDF/Excel) y librerías gráficas\
– Metodología ágil y preparación integral para las pruebas finales UAT]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Proporcionar a los directivos de Dark Códex y SigmaEntretenimiento un registro histórico transparente, seguro e inalterable de todos los eventos ocurridos en el sistema, junto con capacidades avanzadas de generación de reportes gerenciales y un panel de control interactivo que consolide el estado de ciberseguridad en tiempo real.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Módulo de consulta histórica con pistas de auditoría forense, generador de informes descargables en PDF y Excel, y Dashboard interactivo con indicadores clave de rendimiento (KPIs), gráficas de tendencias y estado general del dominio Active Directory.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Mantener un registro inmutable de auditoría para respaldo legal y cumplimiento normativo.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Generar reportes ejecutivos de seguridad con filtros avanzados por fecha, severidad y activo.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Desplegar el Panel Principal (Dashboard SOC) con indicadores de amenazas y equipos monitoreados.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Culminar las Historias 13 y 14, preparando la plataforma para la entrega definitiva del 100%.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Historial completo de acciones con marca de tiempo, usuario actor, dirección IP y detalle de cambios.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Exportación de informes ejecutivos en formato PDF formal y formato Excel (XLSX) con tablas dinámicas.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Dashboard con métricas en tiempo real: incidentes abiertos, resueltos, tiempo medio de remediación (MTTR).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Gráficas interactivas de distribución de incidentes por tipo de ataque y nivel de riesgo.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Generación de PDF: Motores de renderizado HTML a PDF de alta resolución.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Generación de Excel: Librería openpyxl / ExcelJS con estilos corporativos y fórmulas automáticas.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Visualización gráfica: Librerías Chart.js / Recharts integradas en React con diseño responsivo.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Auditoría en base de datos: Tablas de sólo inserción (append-only) con firmas criptográficas de integridad.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Pruebas de estrés y rendimiento ejecutadas por el Tester Daniel Stiven mateus Marin demostrando generación de reportes masivos en menos de 1.5 segundos. Aprobación técnica de kevin Mitnick sobre la inmutabilidad de los registros forenses.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Camilo Murcia*: Ajustar detalles menores de diseño visual y optimizar tiempos de carga en el Dashboard principal.\
*Daniel Stiven mateus Marin*: Coordinar y ejecutar las pruebas de aceptación de usuario (UAT) junto al personal de SigmaEntretenimiento.\
*Daniel Stiven Forero Mateus*: Preparar el entorno definitivo de producción y sincronización final con el controlador de dominio.\
*Eduard bernal*: Convocar a la junta directiva para la sesión formal de cierre y entrega final del proyecto.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[19/11/2026 – Sala de conferencias principal Dark Códex – 10:00 AM]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)
#pagebreak()

=== Acta de Reunión No. 8
#v(4pt)
#table(
  columns: (2.8cm, 1fr, 2.5cm),
  stroke: 0.5pt + rgb("#000000"),
  align: (col, row) => left,
  table.cell(colspan: 3, fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold", size: 10pt)[Acta de reunión]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Título]], table.cell(colspan: 2)[Cierre definitivo del proyecto SecureDesk, entrega del 100% y aceptación final del cliente],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Fecha]], [19/11/2026], table.cell(fill: rgb("#000000"), align: center)[#text(fill: white, weight: "bold")[No. 8]],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Lugar]], table.cell(colspan: 2)[Sala de conferencias principal Dark Códex / Auditorio],
  table.cell(fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Autor]], table.cell(colspan: 2)[*kevin Mitnick* (Consultor SOC)],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Participantes]],
  table.cell(colspan: 3)[#text(size: 8pt)[• Camilo Murcia – Programador\
• SigmaEntretenimiento – Cliente\
• Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\
• Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\
• Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\
• Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\
• Jhon martin perez – Entrenador (Coach Ágil)\
• kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\
• Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\
• Eduard bernal – Big Boss]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Temas tratados]],
  table.cell(colspan: 3)[#text(size: 8pt)[– Propósito de la culminación definitiva y cierre formal de SecureDesk\
– Alcance total del producto entregado y balance de requerimientos\
– Objetivos del proyecto consolidados y cumplimiento del 100% del cronograma\
– Funciones requeridas certificadas en el entorno productivo final\
– Tecnologías implementadas en producción y seguridad en la nube/on-premise\
– Metodología ágil, cierre del repositorio Git (v1.0.0) y firma de garantía]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Desarrollo de los temas tratados]],
  table.cell(colspan: 3)[*Propósito:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Formalizar la culminación exitosa y el cierre definitivo del proyecto SecureDesk, certificando que la plataforma cumple con la totalidad de los requerimientos funcionales y no funcionales contratados, superó todas las pruebas de seguridad y aceptación de usuario (UAT), y se encuentra desplegada y operativa en producción para SigmaEntretenimiento.]]
*Alcance del producto:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Entrega formal de la solución integral SecureDesk en versión de producción 1.0.0, compuesta por los módulos de inicio de sesión con Active Directory, control RBAC, inventario de usuarios y equipos, registro de incidentes, clasificación por riesgo, priorización SOC, ciclo de vida de tickets, historial inmutable de auditoría, generación de reportes ejecutivos y Dashboard de monitoreo.]]
*Objetivos del proyecto:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Cumplir en su totalidad las 16 historias de usuario e iteraciones planificadas desde el 06/08/2026 al 19/11/2026.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Desplegar SecureDesk en el entorno productivo con disponibilidad 24/7 y cero defectos críticos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Entregar el código fuente completo, documentación técnica de arquitectura y manuales de operación.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Capacitar formalmente a los usuarios de SigmaEntretenimiento en sus respectivos roles operativos.]]
*Funciones requeridas:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Operatividad completa de los 14 objetivos funcionales de software especificados en el documento inicial.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Sincronización transparente con el controlador de dominio Active Directory de SigmaEntretenimiento.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Gestión activa de incidentes con respuesta y mitigación asistida por el algoritmo de riesgo.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Generación autónoma de reportes de auditoría y respaldo periódico automatizado de la base de datos.]]
*Tecnologías a utilizar:*
#block(inset: (left: 14pt))[• #text(size: 8pt)[Infraestructura: Servidores dedicados con proxy inverso Nginx, certificados SSL de alta seguridad y PostgreSQL clusterizado.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Control de versiones final: Liberación del release definitivo v1.0.0-final en la rama main de Git por el Tracker Pedronel GarciaForero Mateus (168 commits consolidados).]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Seguridad: Cifrado integral AES-256 en reposo y TLS 1.3 en tránsito con hardening de puertos.]]
#block(inset: (left: 14pt))[• #text(size: 8pt)[Monitoreo: Agentes de supervisión de salud del servidor y registros centralizados.]]
*Metodología de desarrollo:*
#block(inset: (left: 8pt))[#text(size: 8pt)[Aceptación formal unánime por el Cliente SigmaEntretenimiento. El Big Boss Eduard bernal clausuró formalmente la etapa de desarrollo felicitando al equipo técnico liderado por el Programador Camilo Murcia. Se activó la ventana de garantía y soporte técnico por seis (6) meses.]]],
  table.cell(colspan: 3, fill: rgb("#000000"))[#text(fill: white, weight: "bold")[Resumen de acuerdos y responsabilidades]],
  table.cell(colspan: 3)[#text(size: 8pt)[*Dark Códex y Camilo Murcia*: Entregar el paquete completo de código fuente, artefactos de despliegue y documentación de arquitectura.\
*Daniel Stiven Forero Mateus*: Transferir las credenciales maestras y manuales de administración de infraestructura a SigmaEntretenimiento.\
*SigmaEntretenimiento*: Firmar el acta final de recepción a satisfacción y proceder con la liquidación contractual del proyecto.\
*Dark Códex*: Activar el acuerdo de nivel de servicio (SLA) para soporte técnico y garantía post-implementación por 6 meses.]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white, weight: "bold")[Fecha tentativa para una próxima reunión]],
  table.cell(colspan: 3, fill: rgb("#183D20"))[#text(fill: white)[Proyecto finalizado con éxito. Sesión de soporte y seguimiento: 19/02/2027]],
)
#v(8pt)
#table(
  columns: (1fr, 1fr),
  stroke: none,
  align: center,
  [#image("scripts/firma_kevin_mitnick.png", width: 4.8cm)], [#image("scripts/firma_gerente.png", width: 4.8cm)],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *kevin Mitnick* 
 #text(size: 7.5pt, style: "italic")[Consultor de Ciberseguridad / SOC] 
 #text(size: 7pt, fill: rgb("#23476A"))[Autor del Acta — Dark Códex]],
  [#line(length: 75%, stroke: 0.6pt + rgb("#333333")) 
 *Ing. Roberto M. Gómez V.* 
 #text(size: 7.5pt, style: "italic")[Gerente de Operaciones y Proyectos] 
 #text(size: 7pt, fill: rgb("#23476A"))[Aprobación Gerencial — Dark Códex]],
)