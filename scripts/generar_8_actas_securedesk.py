#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de las 8 Actas de Reunión Extendidas de SecureDesk
Formato institucional exacto:
- Desarrollo de temas tratados extenso con apartados obligatorios:
  * Propósito:
  * Alcance del producto / software:
  * Objetivos del proyecto abordados:
  * Funciones requeridas y módulos desarrollados:
  * Tecnologías y arquitectura a utilizar:
  * Metodología de desarrollo y seguimiento en Git:
- 2 firmas manuscritas con fondo blanco al pie de CADA acta:
  1. kevin Mitnick (Consultor de Ciberseguridad / Especialista SOC - Autor)
  2. Ing. Roberto M. Gómez V. (Gerente de Operaciones y Proyectos - Dark Códex)
- 2 reuniones por mes (Agosto, Septiembre, Octubre, Noviembre 2026)
- Hito 50% en Acta 4 y Hito 100% en Acta 8
"""

import io
import os
import zipfile

from generar_firmas import generate_kevin_mitnick_signature, generate_gerente_signature

sig_kevin_path = "scripts/firma_kevin_mitnick.png"
sig_gerente_path = "scripts/firma_gerente.png"

if not os.path.exists(sig_kevin_path):
    generate_kevin_mitnick_signature(sig_kevin_path)
if not os.path.exists(sig_gerente_path):
    generate_gerente_signature(sig_gerente_path)

actas_data = [
    {
        "numero": "1",
        "fecha": "06/08/2026",
        "titulo": "Kick-off, inicio del proyecto SecureDesk y definición de arquitectura base",
        "lugar": "Sala de conferencias Dark Códex / Sesión virtual de ingeniería",
        "autor": "kevin Mitnick",
        "proxima_fecha": "20/08/2026 – Sala de reuniones Dark Códex – 10:00 AM",
        "temas": [
            "Propósito y justificación estratégica del sistema SecureDesk",
            "Alcance del producto e integración con Active Directory",
            "Objetivos del proyecto y metas de ciberseguridad corporativa",
            "Funciones requeridas de la plataforma y módulos base",
            "Tecnologías y arquitectura a utilizar en el ecosistema",
            "Metodología de desarrollo ágil y gestión en Git (Tracker)"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Se formalizó que la organización cliente SigmaEntretenimiento enfrenta desafíos críticos en la detección, registro y seguimiento oportuno de eventos de seguridad que puedan vulnerar la confidencialidad, integridad y disponibilidad de sus activos digitales. El proyecto SecureDesk busca transformar la gestión reactiva de incidentes en una operación centralizada, estructurada y automatizada, ofreciendo trazabilidad completa desde la identificación de una amenaza hasta su resolución y cierre definitivo.")
            ]),
            ("Alcance del producto:", [
                ("p", "SecureDesk será implementado como una plataforma web empresarial diseñada específicamente para registrar, clasificar, monitorear y gestionar incidentes de ciberseguridad para el entorno del Directorio Activo (Active Directory) de SigmaEntretenimiento. El sistema coexistirá armónicamente con la infraestructura de red de Dark Códex y los servidores dedicados de aplicación y base de datos, garantizando accesibilidad desde equipos cliente Windows 10/11, Linux y macOS mediante navegadores modernos.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Centralizar y organizar la gestión de incidentes de ciberseguridad para facilitar su atención y resolución oportuna."),
                ("b", "Mejorar la trazabilidad de los incidentes y facilitar la asignación inequívoca de responsables técnicos."),
                ("b", "Reducir la pérdida de información y habilitar la consulta en tiempo real del estado de cada caso de seguridad."),
                ("b", "Fortalecer la gestión interna de seguridad manteniendo un historial inmutable de eventos para la toma de decisiones estratégicas.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Inicio de sesión y control de acceso seguro mediante autenticación federada."),
                ("b", "Estructuración de roles de usuario iniciales: Empleado (reporte y consulta), Analista SOC (gestión e investigación) y Administrador (políticas y configuración)."),
                ("b", "Módulo base para la captura estructurada de incidentes de seguridad."),
                ("b", "Visualización preliminar del estado de salud del sistema y componentes de red.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Backend: Python con FastAPI / Node.js para servicios web RESTful de alto rendimiento y arquitectura modular."),
                ("b", "Frontend: React con interfaz moderna, adaptable y compatible con Chrome, Microsoft Edge y Firefox."),
                ("b", "Base de datos: PostgreSQL para almacenamiento seguro de usuarios, roles, activos, incidentes y pistas de auditoría."),
                ("b", "Integración de Directorio: Protocolo LDAPS sobre Windows Server Active Directory."),
                ("b", "Control de Versiones: Git bajo la metodología Git Flow administrado en repositorio central por el Tracker.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Se seleccionó la Metodología Ágil (XP - Extreme Programming en conjunto con Scrum) para garantizar máxima adaptabilidad, entregas iterativas por historias de usuario de 6 a 8 días de esfuerzo, programación disciplinada y comunicación permanente con el cliente SigmaEntretenimiento.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Configurar el entorno de desarrollo web e iniciar la programación de los módulos base de autenticación."),
            ("Juan Carlos Marin", "Documentar los requerimientos funcionales y formalizar la matriz de casos de uso de la Historia 1."),
            ("Pedronel GarciaForero Mateus", "Inicializar el repositorio Git con las ramas principales main y develop, estableciendo las políticas de pull requests."),
            ("Daniel Stiven Forero Mateus", "Desplegar el servidor de aplicación y aprovisionar la base de datos para pruebas locales."),
            ("SigmaEntretenimiento", "Suministrar los parámetros de conectividad y directrices de seguridad de la red corporativa.")
        ]
    },
    {
        "numero": "2",
        "fecha": "20/08/2026",
        "titulo": "Autenticación, validación de usuarios con Active Directory y gestión de identidades",
        "lugar": "Sala de juntas Dark Códex – Piso 3",
        "autor": "kevin Mitnick",
        "proxima_fecha": "07/09/2026 – Sala de conferencias Dark Códex – 10:00 AM",
        "temas": [
            "Propósito de la integración de identidades corporativas con Active Directory",
            "Alcance de la sincronización de credenciales y cuentas de dominio",
            "Objetivos abordados en la Iteración 2 (Historia 2 de desarrollo)",
            "Funciones requeridas de autenticación LDAP y control de acceso",
            "Tecnologías y protocolos criptográficos implementados",
            "Metodología de pruebas unitarias y seguimiento del sprint en Git"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Establecer un mecanismo de autenticación centralizado y robusto que permita a los colaboradores de SigmaEntretenimiento acceder a SecureDesk utilizando sus credenciales corporativas existentes de Active Directory, eliminando la duplicidad de contraseñas y mitigando riesgos de suplantación de identidad o almacenamiento inseguro de credenciales.")
            ]),
            ("Alcance del producto:", [
                ("p", "Módulo de enlace directo entre el backend de SecureDesk y el controlador de dominio Active Directory mediante protocolo seguro LDAPS, gestionando la validación en tiempo real de credenciales, mapeo de atributos de usuario y asignación inicial de sesiones seguras.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Validar usuarios y grupos corporativos directamente contra Active Directory sin almacenar claves locales."),
                ("b", "Garantizar el cifrado de todas las transacciones de autenticación mediante canales seguros TLS/SSL."),
                ("b", "Establecer la base para la sincronización automática de metadatos de usuario (nombre, cargo, departamento, equipo)."),
                ("b", "Completar y certificar al 100% la Historia 2 del cronograma general de iteraciones.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Validación de credenciales de usuario contra el catálogo global de Active Directory."),
                ("b", "Emisión y gestión de tokens seguros de sesión JWT con expiración temporal controlada."),
                ("b", "Detección y bloqueo temporal de cuentas ante intentos fallidos reiterados de inicio de sesión."),
                ("b", "Registro automático en bitácora de auditoría de cada intento de acceso exitoso o fallido.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Protocolo de directorio: LDAPS (LDAP sobre SSL/TLS) a través del puerto seguro 636."),
                ("b", "Librerías de autenticación: ldap3 / python-ldap optimizadas para consultas asíncronas."),
                ("b", "Seguridad de sesión: Tokens JWT firmados con algoritmo asimétrico RSA-256."),
                ("b", "Servidor de pruebas: Controlador de dominio simulado en Windows Server 2022.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Desarrollo guiado por pruebas (TDD) implementado por el Programador Camilo Murcia, con verificación formal por el Tester Daniel Stiven mateus Marin (100% de casos de autenticación aprobados) y merge verificado en Git por el Tracker.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Implementar la capa de persistencia para perfiles y metadatos de usuarios sincronizados."),
            ("Daniel Stiven mateus Marin", "Diseñar y ejecutar la batería de pruebas de carga sobre el endpoint de inicio de sesión."),
            ("kevin Mitnick", "Auditar la configuración criptográfica de los certificados SSL y el manejo de tokens JWT."),
            ("Pedronel GarciaForero Mateus", "Aprobar el merge de la rama feature/ad-auth a la rama de integración develop en Git.")
        ]
    },
    {
        "numero": "3",
        "fecha": "07/09/2026",
        "titulo": "Gestión de roles, permisos RBAC y visualización de equipos del dominio",
        "lugar": "Sala de reuniones Dark Códex / Enlace con SigmaEntretenimiento",
        "autor": "kevin Mitnick",
        "proxima_fecha": "25/09/2026 – Sala de juntas Dark Códex – 10:00 AM",
        "temas": [
            "Propósito de la administración de roles RBAC y visualización de activos",
            "Alcance del inventario dinámico de usuarios y equipos del dominio",
            "Objetivos abordados en las Iteraciones 3, 4 y 5 de desarrollo",
            "Funciones requeridas de control de permisos y visualización de computadores",
            "Tecnologías de consulta LDAP y diseño de interfaz gráfica",
            "Metodología ágil y métricas de avance del repositorio en Git"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Garantizar una estricta segregación de funciones mediante el modelo de control de acceso basado en roles (RBAC) y brindar visibilidad en tiempo real de todos los computadores y estaciones de trabajo registradas en el Active Directory, permitiendo correlacionar usuarios con sus equipos físicos para una rápida respuesta ante incidentes.")
            ]),
            ("Alcance del producto:", [
                ("p", "Módulo administrativo que permite consultar y listar usuarios y equipos del dominio corporativo, asociando privilegios específicos para Empleados, Analistas SOC y Administradores, e incorporando vistas de inventario tecnológico conectadas en vivo con Active Directory.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Implementar control de acceso granular asegurando el principio de menor privilegio."),
                ("b", "Visualizar en el panel web los equipos clientes (Windows, Linux, macOS) conectados al dominio."),
                ("b", "Vincular las cuentas de usuario corporativo con sus estaciones de trabajo asignadas."),
                ("b", "Consolidar las Historias 3, 4 e iniciar con éxito la Historia 5 del plan de iteraciones.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Matriz de privilegios diferenciada: Empleado (reporte), Analista SOC (gestión técnica), Administrador (control total)."),
                ("b", "Catálogo visual de computadores del dominio con detalles de sistema operativo, dirección IP y estado."),
                ("b", "Filtros de búsqueda avanzada de activos por departamento, nombre de equipo o usuario asignado."),
                ("b", "Mecanismo de sincronización periódica de objetos de equipo desde Active Directory.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Frontend: Componentes de tablas con paginación reactiva, filtros dinámicos y ordenamiento en React."),
                ("b", "Backend: Consultas de directorio filtradas por objectClass=computer y objectClass=user."),
                ("b", "Base de datos: Tablas relacionales normalizadas para roles, permisos y caché de equipos."),
                ("b", "Seguridad: Middleware de autorización que intercepta cada solicitud HTTP y valida permisos RBAC.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Prácticas de Programación en Parejas (Pair Programming) promovidas por el Coach Ágil Jhon martin perez. El Tracker Pedronel GarciaForero Mateus reportó 52 commits acumulados y cumplimiento del cronograma al 35% sin retrasos.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Comenzar el desarrollo del módulo central de Registro de incidentes (Historias 6 y 7)."),
            ("Juan Carlos Marin", "Definir los campos obligatorios del formulario de reporte de incidentes y taxonomía de categorías."),
            ("Daniel Stiven Forero Mateus", "Optimizar la memoria caché de consultas LDAP para reducir la latencia de respuesta."),
            ("SigmaEntretenimiento", "Revisar y aprobar la interfaz de usuario del inventario de equipos y usuarios.")
        ]
    },
    {
        "numero": "4",
        "fecha": "25/09/2026",
        "titulo": "Evaluación, validación y entrega formal del PRIMER 50% del proyecto SecureDesk",
        "lugar": "Sala de conferencias principal Dark Códex",
        "autor": "kevin Mitnick",
        "proxima_fecha": "09/10/2026 – Sala de reuniones Dark Códex – 10:00 AM",
        "temas": [
            "Propósito y consolidación del PRIMER 50% de desarrollo de SecureDesk",
            "Alcance de los módulos de Registro y Reporte de incidentes de seguridad",
            "Objetivos del proyecto alcanzados en las Historias 1 a 8",
            "Funciones requeridas validadas en la demostración en vivo ante el cliente",
            "Tecnologías de captura de evidencias y almacenamiento transaccional",
            "Metodología, auditoría de calidad y firma del hito intermedio del 50%"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Evaluar formalmente, verificar y entregar a entera satisfacción del cliente SigmaEntretenimiento el primer hito mayor del proyecto (50% de avance físico y funcional), certificando la operatividad de los módulos de autenticación Active Directory, gestión de roles, inventario de activos y el sistema de registro y reporte de incidentes.")
            ]),
            ("Alcance del producto:", [
                ("p", "Entrega y despliegue funcional de la versión beta intermedio de SecureDesk que habilita a cualquier empleado reportar incidentes de seguridad informática, adjuntar evidencias, asociar el computador afectado y consultar el estado preliminar de su caso.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Completar al 100% las 8 primeras historias de usuario e iteraciones planificadas (Hito 50% del proyecto)."),
                ("b", "Permitir el reporte estructurado de eventos de seguridad por parte de los usuarios finales."),
                ("b", "Garantizar la captura fidedigna de evidencias y metadatos técnicos en cada reporte."),
                ("b", "Auditar y certificar la estabilidad general del sistema antes de pasar a la fase de clasificación avanzada.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Formulario intuitivo de reporte de incidentes con categorización preliminar guiada."),
                ("b", "Carga segura de evidencias digitales (capturas de pantalla, archivos de registro) con cálculo de hash SHA-256."),
                ("b", "Notificación automática a la cola de entrada del SOC tras el envío de un incidente."),
                ("b", "Panel de consulta para el empleado donde visualiza el historial de sus casos reportados.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Almacenamiento de archivos: Repositorio encriptado con validación estricta de extensiones y tipos MIME."),
                ("b", "Base de datos: Transacciones ACID en PostgreSQL para registro íntegro de incidentes y archivos adjuntos."),
                ("b", "Control de versiones: Etiqueta de versión oficial v0.5.0-beta creada en la rama main de Git."),
                ("b", "Integración continua: Ejecución automática de pruebas de regresión en cada commit.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Demostración en vivo efectuada por Camilo Murcia ante los directivos de SigmaEntretenimiento y el Big Boss Eduard bernal. El informe de pruebas entregado por el Tester certificó 84 pruebas superadas con éxito. Firma oficial del acta de aprobación del primer 50% del proyecto.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Iniciar la programación de los algoritmos de clasificación y priorización por riesgo (Historias 9 y 10)."),
            ("kevin Mitnick", "Suministrar la matriz técnica de severidad, factores de impacto y reglas de correlación SOC."),
            ("Pedronel GarciaForero Mateus", "Consolidar la rama release/0.5.0 y habilitar las ramas de trabajo para la segunda mitad del proyecto."),
            ("Eduard bernal", "Firmar el acta de conformidad del 50% y autorizar el inicio del segundo ciclo de desarrollo.")
        ]
    },
    {
        "numero": "5",
        "fecha": "09/10/2026",
        "titulo": "Arranque de la Segunda Mitad (Segundo 50%): Clasificación y priorización de incidentes",
        "lugar": "Sala de juntas Dark Códex – Piso 2",
        "autor": "kevin Mitnick",
        "proxima_fecha": "23/10/2026 – Sala de reuniones Dark Códex – 10:00 AM",
        "temas": [
            "Propósito del motor de clasificación y priorización por nivel de riesgo",
            "Alcance del análisis de severidad de amenazas e impacto en el negocio",
            "Objetivos abordados en las Iteraciones 9 y 10 (Segundo 50% del proyecto)",
            "Funciones requeridas de ponderación automática y cola de atención SOC",
            "Tecnologías de algoritmos de scoring y taxonomía de ciberseguridad",
            "Metodología de trabajo conjunto con el especialista SOC y seguimiento en Git"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Iniciar con determinación el segundo 50% de desarrollo implementando la inteligencia de ciberseguridad de SecureDesk, permitiendo al sistema clasificar de forma automatizada los incidentes reportados y priorizar su orden de atención en función de la gravedad técnica de la amenaza y la criticidad del activo comprometido.")
            ]),
            ("Alcance del producto:", [
                ("p", "Motor analítico en backend que clasifica incidentes en cuatro niveles de riesgo (Bajo, Medio, Alto, Crítico) y ordena dinámicamente la cola de trabajo del Centro de Operaciones de Seguridad (SOC) para asegurar que las contingencias graves se atiendan de manera inmediata.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Clasificar incidentes según su nivel de riesgo y vector de ataque (malware, phishing, accesos no autorizados)."),
                ("b", "Priorizar la atención de eventos considerando la importancia del activo en el Active Directory."),
                ("b", "Reducir los tiempos de respuesta inicial ante amenazas críticas que pongan en riesgo la operación."),
                ("b", "Desarrollar y validar formalmente las Historias 9 y 10 del cronograma.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Algoritmo de cálculo de criticidad que combina impacto, probabilidad y criticidad del activo."),
                ("b", "Semáforo visual de severidad (Verde, Amarillo, Naranja, Rojo) en la lista de incidentes del SOC."),
                ("b", "Reordenamiento automático en tiempo real de la bandeja de incidentes pendientes."),
                ("b", "Alertas sonoras y visuales inmediatas para incidentes tipificados como Críticos.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Algoritmo de evaluación: Implementación basada en el estándar CVSS v3.1 adaptado a entornos internos."),
                ("b", "Backend: Servicios de cálculo de severidad con procesamiento en segundo plano."),
                ("b", "Base de datos: Índices optimizados en PostgreSQL para ordenamiento instantáneo por severidad y fecha."),
                ("b", "Frontend: Notificaciones toast reactivas y badges de estado actualizados en tiempo real.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Diseño de matrices de riesgo guiado por el Consultor de Ciberseguridad kevin Mitnick y codificado por Camilo Murcia. Sesión de retrospectiva de iteración facilitada por Jhon martin perez para afinar los tiempos de respuesta del equipo.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Desarrollar los mecanismos de asignación automática y manual de incidentes a analistas SOC."),
            ("Daniel Stiven mateus Marin", "Diseñar pruebas automatizadas simulando ráfagas de incidentes de diferente criticidad."),
            ("Daniel Stiven Forero Mateus", "Configurar índices de alto rendimiento en la base de datos para consultas de ordenación masiva."),
            ("SigmaEntretenimiento", "Definir los tiempos objetivo de atención (SLA) para cada nivel de criticidad.")
        ]
    },
    {
        "numero": "6",
        "fecha": "23/10/2026",
        "titulo": "Asignación, ciclo de vida de incidentes y gestión de activos tecnológicos",
        "lugar": "Sala de reuniones Dark Códex / Sesión virtual con SigmaEntretenimiento",
        "autor": "kevin Mitnick",
        "proxima_fecha": "06/11/2026 – Sala de juntas Dark Códex – 10:00 AM",
        "temas": [
            "Propósito del flujo de trabajo y ciclo de vida de incidentes de seguridad",
            "Alcance de la asignación a analistas SOC, investigación y remediación",
            "Objetivos abordados en las Iteraciones 11 y 12 de desarrollo",
            "Funciones requeridas de asignación de casos, notas forenses y cierre técnico",
            "Tecnologías de máquinas de estado finito y vinculación con activos",
            "Metodología de integración continua y métricas de avance en Git (Tracker)"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Estructurar y estandarizar el ciclo de vida completo de cada incidente de seguridad dentro del SOC, asegurando que cada caso sea asignado a un analista competente, investigado con trazabilidad forense, mitigado con acciones concretas sobre los activos afectados y cerrado formalmente con documentación de causa raíz.")
            ]),
            ("Alcance del producto:", [
                ("p", "Módulo de gestión del ciclo de vida del incidente que soporta transiciones de estado formales, notas de investigación confidenciales, vinculación con el inventario de activos del Active Directory y emisión de recomendaciones preventivas.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Asignar responsables técnicos a cada incidente según disponibilidad y especialidad."),
                ("b", "Permitir el seguimiento del ciclo de vida: Registrado → En Análisis → En Mitigación → Cerrado."),
                ("b", "Asociar las acciones técnicas de contención con los activos tecnológicos de la empresa."),
                ("b", "Completar satisfactoriamente las Historias 11 y 12 alcanzando el 75% del cronograma general.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Asignación de tickets tanto de forma manual por el líder SOC como por asignación balanceada automática."),
                ("b", "Línea de tiempo de eventos con bitácora interna de acciones forenses y hallazgos técnicos."),
                ("b", "Registro de medidas de contención (ej. desconexión de red de estación, bloqueo de usuario en AD)."),
                ("b", "Formulario de cierre formal con categorización de causa raíz y recomendaciones preventivas.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Arquitectura: Máquina de estados finitos (State Machine) implementada en backend para evitar transiciones ilegales."),
                ("b", "Integración con Directorio: Posibilidad de invocar comandos de consulta de estado del equipo en Active Directory."),
                ("b", "Control de versiones: 125 commits consolidados en Git con verificación automática de pruebas en GitHub Actions."),
                ("b", "Frontend: Panel interactivo tipo Kanban y vista de detalle de incidente con historial cronológico.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Flujo continuo de integración y despliegue (CI/CD) supervisado por Pedronel GarciaForero Mateus. Pruebas de usabilidad satisfactorias con los futuros analistas SOC de SigmaEntretenimiento.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Programar los módulos de historial inmutable de auditoría y generación de reportes ejecutivos."),
            ("Juan Carlos Marin", "Diseñar las plantillas corporativas de los reportes gerenciales en formatos PDF y Excel."),
            ("kevin Mitnick", "Definir los indicadores clave de rendimiento (MTTR, MTTD) para el Dashboard SOC."),
            ("Daniel Stiven mateus Marin", "Ejecutar pruebas de regresión sobre todo el ciclo de transición de estados de incidentes.")
        ]
    },
    {
        "numero": "7",
        "fecha": "06/11/2026",
        "titulo": "Historial de auditoría, panel interactivo SOC y generación de reportes",
        "lugar": "Sala de juntas Dark Códex – Piso 3",
        "autor": "kevin Mitnick",
        "proxima_fecha": "19/11/2026 – Sala de conferencias principal Dark Códex – 10:00 AM",
        "temas": [
            "Propósito de las pistas de auditoría inmutables y reportería ejecutiva",
            "Alcance del Dashboard SOC centralizado y exportación de informes",
            "Objetivos abordados en las Iteraciones 13 y 14 de desarrollo",
            "Funciones requeridas de auditoría, visualización analítica y reportes",
            "Tecnologías de exportación de documentos (PDF/Excel) y librerías gráficas",
            "Metodología ágil y preparación integral para las pruebas finales UAT"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Proporcionar a los directivos de Dark Códex y SigmaEntretenimiento un registro histórico transparente, seguro e inalterable de todos los eventos ocurridos en el sistema, junto con capacidades avanzadas de generación de reportes gerenciales y un panel de control interactivo que consolide el estado de ciberseguridad en tiempo real.")
            ]),
            ("Alcance del producto:", [
                ("p", "Módulo de consulta histórica con pistas de auditoría forense, generador de informes descargables en PDF y Excel, y Dashboard interactivo con indicadores clave de rendimiento (KPIs), gráficas de tendencias y estado general del dominio Active Directory.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Mantener un registro inmutable de auditoría para respaldo legal y cumplimiento normativo."),
                ("b", "Generar reportes ejecutivos de seguridad con filtros avanzados por fecha, severidad y activo."),
                ("b", "Desplegar el Panel Principal (Dashboard SOC) con indicadores de amenazas y equipos monitoreados."),
                ("b", "Culminar las Historias 13 y 14, preparando la plataforma para la entrega definitiva del 100%.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Historial completo de acciones con marca de tiempo, usuario actor, dirección IP y detalle de cambios."),
                ("b", "Exportación de informes ejecutivos en formato PDF formal y formato Excel (XLSX) con tablas dinámicas."),
                ("b", "Dashboard con métricas en tiempo real: incidentes abiertos, resueltos, tiempo medio de remediación (MTTR)."),
                ("b", "Gráficas interactivas de distribución de incidentes por tipo de ataque y nivel de riesgo.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Generación de PDF: Motores de renderizado HTML a PDF de alta resolución."),
                ("b", "Generación de Excel: Librería openpyxl / ExcelJS con estilos corporativos y fórmulas automáticas."),
                ("b", "Visualización gráfica: Librerías Chart.js / Recharts integradas en React con diseño responsivo."),
                ("b", "Auditoría en base de datos: Tablas de sólo inserción (append-only) con firmas criptográficas de integridad.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Pruebas de estrés y rendimiento ejecutadas por el Tester Daniel Stiven mateus Marin demostrando generación de reportes masivos en menos de 1.5 segundos. Aprobación técnica de kevin Mitnick sobre la inmutabilidad de los registros forenses.")
            ])
        ],
        "acuerdos": [
            ("Camilo Murcia", "Ajustar detalles menores de diseño visual y optimizar tiempos de carga en el Dashboard principal."),
            ("Daniel Stiven mateus Marin", "Coordinar y ejecutar las pruebas de aceptación de usuario (UAT) junto al personal de SigmaEntretenimiento."),
            ("Daniel Stiven Forero Mateus", "Preparar el entorno definitivo de producción y sincronización final con el controlador de dominio."),
            ("Eduard bernal", "Convocar a la junta directiva para la sesión formal de cierre y entrega final del proyecto.")
        ]
    },
    {
        "numero": "8",
        "fecha": "19/11/2026",
        "titulo": "Cierre definitivo del proyecto SecureDesk, entrega del 100% y aceptación final del cliente",
        "lugar": "Sala de conferencias principal Dark Códex / Auditorio",
        "autor": "kevin Mitnick",
        "proxima_fecha": "Proyecto finalizado con éxito. Sesión de soporte y seguimiento: 19/02/2027",
        "temas": [
            "Propósito de la culminación definitiva y cierre formal de SecureDesk",
            "Alcance total del producto entregado y balance de requerimientos",
            "Objetivos del proyecto consolidados y cumplimiento del 100% del cronograma",
            "Funciones requeridas certificadas en el entorno productivo final",
            "Tecnologías implementadas en producción y seguridad en la nube/on-premise",
            "Metodología ágil, cierre del repositorio Git (v1.0.0) y firma de garantía"
        ],
        "secciones": [
            ("Propósito:", [
                ("p", "Formalizar la culminación exitosa y el cierre definitivo del proyecto SecureDesk, certificando que la plataforma cumple con la totalidad de los requerimientos funcionales y no funcionales contratados, superó todas las pruebas de seguridad y aceptación de usuario (UAT), y se encuentra desplegada y operativa en producción para SigmaEntretenimiento.")
            ]),
            ("Alcance del producto:", [
                ("p", "Entrega formal de la solución integral SecureDesk en versión de producción 1.0.0, compuesta por los módulos de inicio de sesión con Active Directory, control RBAC, inventario de usuarios y equipos, registro de incidentes, clasificación por riesgo, priorización SOC, ciclo de vida de tickets, historial inmutable de auditoría, generación de reportes ejecutivos y Dashboard de monitoreo.")
            ]),
            ("Objetivos del proyecto:", [
                ("b", "Cumplir en su totalidad las 16 historias de usuario e iteraciones planificadas desde el 06/08/2026 al 19/11/2026."),
                ("b", "Desplegar SecureDesk en el entorno productivo con disponibilidad 24/7 y cero defectos críticos."),
                ("b", "Entregar el código fuente completo, documentación técnica de arquitectura y manuales de operación."),
                ("b", "Capacitar formalmente a los usuarios de SigmaEntretenimiento en sus respectivos roles operativos.")
            ]),
            ("Funciones requeridas:", [
                ("b", "Operatividad completa de los 14 objetivos funcionales de software especificados en el documento inicial."),
                ("b", "Sincronización transparente con el controlador de dominio Active Directory de SigmaEntretenimiento."),
                ("b", "Gestión activa de incidentes con respuesta y mitigación asistida por el algoritmo de riesgo."),
                ("b", "Generación autónoma de reportes de auditoría y respaldo periódico automatizado de la base de datos.")
            ]),
            ("Tecnologías a utilizar:", [
                ("b", "Infraestructura: Servidores dedicados con proxy inverso Nginx, certificados SSL de alta seguridad y PostgreSQL clusterizado."),
                ("b", "Control de versiones final: Liberación del release definitivo v1.0.0-final en la rama main de Git por el Tracker Pedronel GarciaForero Mateus (168 commits consolidados)."),
                ("b", "Seguridad: Cifrado integral AES-256 en reposo y TLS 1.3 en tránsito con hardening de puertos."),
                ("b", "Monitoreo: Agentes de supervisión de salud del servidor y registros centralizados.")
            ]),
            ("Metodología de desarrollo:", [
                ("p", "Aceptación formal unánime por el Cliente SigmaEntretenimiento. El Big Boss Eduard bernal clausuró formalmente la etapa de desarrollo felicitando al equipo técnico liderado por el Programador Camilo Murcia. Se activó la ventana de garantía y soporte técnico por seis (6) meses.")
            ])
        ],
        "acuerdos": [
            ("Dark Códex y Camilo Murcia", "Entregar el paquete completo de código fuente, artefactos de despliegue y documentación de arquitectura."),
            ("Daniel Stiven Forero Mateus", "Transferir las credenciales maestras y manuales de administración de infraestructura a SigmaEntretenimiento."),
            ("SigmaEntretenimiento", "Firmar el acta final de recepción a satisfacción y proceder con la liquidación contractual del proyecto."),
            ("Dark Códex", "Activar el acuerdo de nivel de servicio (SLA) para soporte técnico y garantía post-implementación por 6 meses.")
        ]
    }
]

participantes_texto = (
    "Camilo Murcia – Programador\n"
    "SigmaEntretenimiento – Cliente\n"
    "Pedronel GarciaForero Mateus – Encargado de seguimiento (Tracker - Git)\n"
    "Daniel Stiven mateus Marin – Encargado de pruebas (Tester)\n"
    "Juan Daniel Oviedo – Líder de Proyecto (Project Manager)\n"
    "Juan Carlos Marin – Líder de Análisis de Negocio y Requerimientos / Arquitecto\n"
    "Jhon martin perez – Entrenador (Coach Ágil)\n"
    "kevin Mitnick – Consultor de Ciberseguridad (Especialista SOC)\n"
    "Daniel Stiven Forero Mateus – Administrador de Infraestructura y Active Directory (DevOps)\n"
    "Eduard bernal – Big Boss"
)

def build_signature_drawing_xml(r_id, doc_id, name):
    cx = 2011680
    cy = 804672
    return f"""<w:r>
        <w:drawing>
            <wp:inline distT="0" distB="0" distL="0" distR="0">
                <wp:extent cx="{cx}" cy="{cy}"/>
                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                <wp:docPr id="{doc_id}" name="{name}"/>
                <wp:cNvGraphicFramePr>
                    <a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>
                </wp:cNvGraphicFramePr>
                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                    <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
                        <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
                            <pic:nvPicPr>
                                <pic:cNvPr id="{doc_id}" name="{name}"/>
                                <pic:cNvPicPr/>
                            </pic:nvPicPr>
                            <pic:blipFill>
                                <a:blip r:embed="{r_id}"/>
                                <a:stretch><a:fillRect/></a:stretch>
                            </pic:blipFill>
                            <pic:spPr>
                                <a:xfrm>
                                    <a:off x="0" y="0"/>
                                    <a:ext cx="{cx}" cy="{cy}"/>
                                </a:xfrm>
                                <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                            </pic:spPr>
                        </pic:pic>
                    </a:graphicData>
                </a:graphic>
            </wp:inline>
        </w:drawing>
    </w:r>"""

def build_acta_xml(acta, is_first, is_last, acta_idx):
    num = acta["numero"]
    fecha = acta["fecha"]
    titulo = acta["titulo"]
    lugar = acta["lugar"]
    autor = acta["autor"]
    prox_fecha = acta["proxima_fecha"]
    temas = acta["temas"]
    secciones = acta["secciones"]
    acuerdos = acta["acuerdos"]

    doc_id_kevin = 1000 + acta_idx * 2
    doc_id_gerente = 1001 + acta_idx * 2

    drawing_kevin = build_signature_drawing_xml("rId_sig_kevin", doc_id_kevin, f"Firma_Kevin_{acta_idx}")
    drawing_gerente = build_signature_drawing_xml("rId_sig_gerente", doc_id_gerente, f"Firma_Gerente_{acta_idx}")

    # Table 0: Datos del acta y temas tratados
    t0_xml = f"""
    <w:tbl>
        <w:tblPr>
            <w:tblW w:type="auto" w:w="0"/>
            <w:jc w:val="left"/>
            <w:tblLayout w:type="fixed"/>
            <w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/>
        </w:tblPr>
        <w:tblGrid>
            <w:gridCol w:w="3581"/>
            <w:gridCol w:w="3581"/>
            <w:gridCol w:w="3581"/>
        </w:tblGrid>
        
        <!-- Row 0: Header Acta de reunión -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr>
                    <w:tcW w:type="dxa" w:w="10743"/>
                    <w:gridSpan w:val="3"/>
                    <w:shd w:fill="000000"/>
                    <w:vAlign w:val="center"/>
                </w:tcPr>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="60" w:after="60"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="20"/></w:rPr><w:t>Acta de reunión</w:t></w:r>
                </w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 1: Título -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="3581"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Título</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="7162"/><w:gridSpan w:val="2"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{titulo}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 2: Fecha y Número -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="3581"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Fecha</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="3581"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{fecha}</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="3581"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>No.   {num}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 3: Lugar -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="3581"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Lugar</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="7162"/><w:gridSpan w:val="2"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{lugar}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 4: Autor (kevin Mitnick SIEMPRE) -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="3581"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Autor</w:t></w:r></w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="7162"/><w:gridSpan w:val="2"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{autor}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 5: Header Participantes -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:gridSpan w:val="3"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Participantes</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 6: Lista Participantes -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:gridSpan w:val="3"/><w:vAlign w:val="center"/></w:tcPr>
                {"".join([f'<w:p><w:pPr><w:spacing w:before="20" w:after="20"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="15"/></w:rPr><w:t>• {p}</w:t></w:r></w:p>' for p in participantes_texto.splitlines()])}
            </w:tc>
        </w:tr>
        
        <!-- Row 7: Header Temas tratados -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:gridSpan w:val="3"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Temas tratados</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
        
        <!-- Row 8: Lista Temas tratados -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:gridSpan w:val="3"/><w:vAlign w:val="center"/></w:tcPr>
                {"".join([f'<w:p><w:pPr><w:spacing w:before="20" w:after="20"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="15"/></w:rPr><w:t>– {t}</w:t></w:r></w:p>' for t in temas])}
            </w:tc>
        </w:tr>
        
        <!-- Row 9: Header Desarrollo de los temas tratados -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:gridSpan w:val="3"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Desarrollo de los temas tratados</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
    </w:tbl>
    """

    # Table 1: Contenido del desarrollo detallado estructurado con apartados formales
    desarrollo_content = ""
    for sec_title, sec_items in secciones:
        desarrollo_content += f"""
        <w:p><w:pPr><w:spacing w:before="80" w:after="30"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:i/><w:sz w:val="17"/><w:color w:val="111111"/></w:rPr><w:t>{sec_title}</w:t></w:r>
        </w:p>
        """
        for itype, itext in sec_items:
            if itype == "p":
                desarrollo_content += f"""
                <w:p><w:pPr><w:spacing w:before="20" w:after="60"/><w:ind w:left="240"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{itext}</w:t></w:r>
                </w:p>
                """
            elif itype == "b":
                desarrollo_content += f"""
                <w:p><w:pPr><w:spacing w:before="15" w:after="25"/><w:ind w:left="440" w:hanging="200"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="16"/><w:color w:val="23476A"/></w:rPr><w:t>• </w:t></w:r>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{itext}</w:t></w:r>
                </w:p>
                """

    acuerdos_content = ""
    for persona, acuerdo in acuerdos:
        acuerdos_content += f"""
        <w:p><w:pPr><w:spacing w:before="35" w:after="35"/></w:pPr>
            <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="16"/></w:rPr><w:t>{persona}: </w:t></w:r>
            <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/></w:rPr><w:t>{acuerdo}</w:t></w:r>
        </w:p>
        """

    t1_xml = f"""
    <w:tbl>
        <w:tblPr>
            <w:tblW w:type="auto" w:w="0"/>
            <w:jc w:val="left"/>
            <w:tblLayout w:type="fixed"/>
            <w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/>
        </w:tblPr>
        <w:tblGrid>
            <w:gridCol w:w="10743"/>
        </w:tblGrid>
        
        <!-- Row 0: Desarrollo detallado -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:vAlign w:top="true"/></w:tcPr>
                {desarrollo_content}
            </w:tc>
        </w:tr>
        
        <!-- Row 1: Resumen de acuerdos y responsabilidades -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:shd w:fill="000000"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Resumen de acuerdos y responsabilidades</w:t></w:r></w:p>
                {acuerdos_content}
            </w:tc>
        </w:tr>
        
        <!-- Row 2: Fecha tentativa próxima reunión -->
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="10743"/><w:shd w:fill="183D20"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="FFFFFF"/><w:sz w:val="16"/></w:rPr><w:t>Fecha tentativa para una próxima reunión</w:t></w:r></w:p>
                <w:p><w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="16"/><w:color w:val="FFFFFF"/></w:rPr><w:t>{prox_fecha}</w:t></w:r></w:p>
            </w:tc>
        </w:tr>
    </w:tbl>
    """

    # Table 2: Firmas con fondo blanco al pie de cada acta
    t_firmas_xml = f"""
    <w:p><w:pPr><w:spacing w:before="180" w:after="60"/></w:pPr></w:p>
    <w:tbl>
        <w:tblPr>
            <w:tblW w:type="auto" w:w="0"/>
            <w:jc w:val="center"/>
            <w:tblLayout w:type="fixed"/>
            <w:tblBorders>
                <w:top w:val="none"/>
                <w:left w:val="none"/>
                <w:bottom w:val="none"/>
                <w:right w:val="none"/>
                <w:insideH w:val="none"/>
                <w:insideV w:val="none"/>
            </w:tblBorders>
        </w:tblPr>
        <w:tblGrid>
            <w:gridCol w:w="5371"/>
            <w:gridCol w:w="5371"/>
        </w:tblGrid>
        
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="5371"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="40" w:after="0"/></w:pPr>
                    {drawing_kevin}
                </w:p>
            </w:tc>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="5371"/><w:vAlign w:val="center"/></w:tcPr>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="40" w:after="0"/></w:pPr>
                    {drawing_gerente}
                </w:p>
            </w:tc>
        </w:tr>
        
        <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="5371"/><w:vAlign w:val="top"/></w:tcPr>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="20"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:color w:val="444444"/><w:sz w:val="18"/></w:rPr><w:t>________________________________________</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="20" w:after="20"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="18"/><w:color w:val="111111"/></w:rPr><w:t>kevin Mitnick</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="20"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:i/><w:sz w:val="15"/><w:color w:val="333333"/></w:rPr><w:t>Consultor de Ciberseguridad (Especialista SOC)</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="40"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="14"/><w:color w:val="23476A"/></w:rPr><w:t>Autor del Acta — Dark Códex</w:t></w:r>
                </w:p>
            </w:tc>
            
            <w:tc>
                <w:tcPr><w:tcW w:type="dxa" w:w="5371"/><w:vAlign w:val="top"/></w:tcPr>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="20"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:color w:val="444444"/><w:sz w:val="18"/></w:rPr><w:t>________________________________________</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="20" w:after="20"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="18"/><w:color w:val="111111"/></w:rPr><w:t>Ing. Roberto M. Gómez V.</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="20"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:i/><w:sz w:val="15"/><w:color w:val="333333"/></w:rPr><w:t>Gerente de Operaciones y Proyectos</w:t></w:r>
                </w:p>
                <w:p>
                    <w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="40"/></w:pPr>
                    <w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="14"/><w:color w:val="23476A"/></w:rPr><w:t>Aprobación Gerencial — Dark Códex</w:t></w:r>
                </w:p>
            </w:tc>
        </w:tr>
    </w:tbl>
    """

    page_break = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>' if not is_last else ''

    return t0_xml + t1_xml + t_firmas_xml + page_break

def main():
    actas_body_xml = ""
    for idx, acta in enumerate(actas_data):
        is_first = (idx == 0)
        is_last = (idx == len(actas_data) - 1)
        actas_body_xml += build_acta_xml(acta, is_first, is_last, idx)

    complete_doc_xml = f"""<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" 
            xmlns:mo="http://schemas.microsoft.com/office/mac/office/2008/main" 
            xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
            xmlns:mv="urn:schemas-microsoft-com:mac:vml" 
            xmlns:o="urn:schemas-microsoft-com:office:office" 
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" 
            xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" 
            xmlns:v="urn:schemas-microsoft-com:vml" 
            xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" 
            xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" 
            xmlns:w10="urn:schemas-microsoft-com:office:word" 
            xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" 
            xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" 
            xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" 
            xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" 
            xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" 
            xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" 
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" 
            xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" 
            mc:Ignorable="w14 wp14">
<w:body>
    <w:p>
        <w:pPr><w:spacing w:after="140"/><w:jc w:val="center"/></w:pPr>
        <w:r>
            <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:color w:val="23476A"/><w:sz w:val="32"/></w:rPr>
            <w:t>SECUREDESK - Actas Oficiales de Reunión de Proyecto</w:t>
        </w:r>
    </w:p>
    <w:p>
        <w:pPr><w:spacing w:after="240"/><w:jc w:val="center"/></w:pPr>
        <w:r>
            <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:i/><w:color w:val="555555"/><w:sz w:val="20"/></w:rPr>
            <w:t>Dark Códex &amp; SigmaEntretenimiento — Gestión Ágil y Seguimiento (Agosto - Noviembre 2026)</w:t>
        </w:r>
    </w:p>
    {actas_body_xml}
    <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
        <w:pgSz w:w="12240" w:h="15840"/>
        <w:pgMar w:top="605" w:right="749" w:bottom="605" w:left="749" w:header="288" w:footer="288" w:gutter="0"/>
        <w:cols w:space="720"/>
        <w:docGrid w:linePitch="360"/>
    </w:sectPr>
</w:body>
</w:document>"""

    base_docx = "Acta_de_reunion_recreada.docx"
    output_docx = "Actas_de_reunion_SecureDesk.docx"

    with open(sig_kevin_path, "rb") as f:
        img_kevin_bytes = f.read()

    with open(sig_gerente_path, "rb") as f:
        img_gerente_bytes = f.read()

    buffer = io.BytesIO()
    with zipfile.ZipFile(base_docx, "r") as zin:
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/document.xml":
                    zout.writestr(item, complete_doc_xml.encode("utf-8"))
                elif item.filename == "[Content_Types].xml":
                    ct_content = zin.read(item.filename).decode("utf-8")
                    if '<Default Extension="png"' not in ct_content:
                        ct_content = ct_content.replace('</Types>', '<Default Extension="png" ContentType="image/png"/></Types>')
                    zout.writestr(item, ct_content.encode("utf-8"))
                elif item.filename == "word/_rels/document.xml.rels":
                    rels_content = zin.read(item.filename).decode("utf-8")
                    if "rId_sig_kevin" not in rels_content:
                        rels_to_add = (
                            '<Relationship Id="rId_sig_kevin" '
                            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                            'Target="media/firma_kevin_mitnick.png"/>'
                            '<Relationship Id="rId_sig_gerente" '
                            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                            'Target="media/firma_gerente.png"/>'
                        )
                        rels_content = rels_content.replace('</Relationships>', rels_to_add + '</Relationships>')
                    zout.writestr(item, rels_content.encode("utf-8"))
                else:
                    zout.writestr(item, zin.read(item.filename))

            zout.writestr("word/media/firma_kevin_mitnick.png", img_kevin_bytes)
            zout.writestr("word/media/firma_gerente.png", img_gerente_bytes)

    with open(output_docx, "wb") as f:
        f.write(buffer.getvalue())

    print(f"Documento extendido generado exitosamente: {output_docx}")

if __name__ == "__main__":
    main()
