# Automatización, CRM y atribución

Cómo convertir el mapa del embudo en un proceso que se pueda operar y medir. Regla general: **primero un proceso manual con registro, luego automatizar lo repetitivo.** Automatizar un proceso que no se entiende solo produce errores más rápido.

## Contenido

1. [Etapas del CRM](#1-etapas-del-crm)
2. [Campos mínimos](#2-campos-mínimos)
3. [Reglas de seguimiento](#3-reglas-de-seguimiento)
4. [Herramientas por nivel](#4-herramientas-por-nivel)
5. [Atribución: saber de dónde vino cada venta](#5-atribución-saber-de-dónde-vino-cada-venta)
6. [Agentes de IA y bots](#6-agentes-de-ia-y-bots)
7. [Permisos y cumplimiento](#7-permisos-y-cumplimiento)

---

## 1. Etapas del CRM

Las etapas del pipeline son **estados del contacto**, en el mismo orden que el embudo. Ejemplo para venta conversacional:

| Etapa | Entra cuando… | Sale cuando… |
|---|---|---|
| Nuevo | Escribe, deja datos o es cargado | Recibe la primera respuesta |
| Contactado | Se le respondió | Responde la calificación o pasan N días |
| Calificado | Cumple los criterios definidos | Recibe la oferta |
| Oferta enviada | Tiene precio y condiciones | Acepta, objeta o no responde |
| Seguimiento / negociación | Tiene dudas u objeciones | Compra o se pierde |
| Ganado | Confirmó y pagó (o pedido confirmado) | Se entrega |
| Perdido | No compra (registrar **motivo**) | Se reactiva en el futuro |
| Cliente activo | Recibió el producto | Llega la fecha de reposición |
| Recompra pendiente | Se acerca la fecha estimada | Recompra o pasa a inactivo |
| Inactivo | Sin compra en X días | Se reactiva |

Usa una lista cerrada de **motivos de pérdida** (precio, envío/zona, no responde, eligió otra marca, no era el momento, no califica, otro) para encontrar patrones.

## 2. Campos mínimos

- Identificador único (teléfono normalizado con código de país, p. ej. +57…, para evitar duplicados).
- Nombre, teléfono, email (si aplica), ciudad/zona.
- **Origen:** canal, campaña, anuncio o pieza, aliado/código, fecha de entrada.
- Etapa actual, responsable, próxima acción y fecha.
- Producto de interés, valor estimado.
- Motivo de pérdida.
- **Permiso de comunicaciones:** sí/no, fecha, medio y texto con el que se otorgó.
- Para recompra: fecha de compra, producto, cantidad y fecha estimada de reposición.

## 3. Reglas de seguimiento

| Disparador | Acción | Automatizable |
|---|---|---|
| Nuevo contacto | Respuesta de bienvenida inmediata + tarea al responsable | Sí |
| Sin respuesta del contacto en 24 h | Seguimiento D+1, luego D+3 y D+7; después, a nutrición o perdido | Sí, con plantillas |
| Oferta enviada sin respuesta 48 h | Seguimiento con valor nuevo | Sí / manual |
| Pide hablar con una persona o tiene una objeción compleja | Pasar a humano con el historial | Alerta |
| Ganado | Confirmación, datos de entrega, mensaje post-venta a los X días | Sí |
| X días antes de la reposición estimada | Recordatorio con opción de responder SÍ/NO | Sí |
| Sin compra en 60–90 días (según ciclo) | Reactivación | Sí |
| Pide no recibir mensajes | Marcar sin permiso y excluir de todos los envíos | Sí, obligatorio |

Define también: **tiempo máximo de primera respuesta** (en horario laboral), quién cubre fuera de horario y qué mensaje recibe quien escribe de noche.

## 4. Herramientas por nivel

Elige lo mínimo que resuelva el volumen actual. Menciona herramientas como ejemplos, no como requisito; verifica precios y funciones vigentes antes de recomendarlas en firme.

| Nivel | Cuándo | Ejemplos de herramientas |
|---|---|---|
| 0 — Manual ordenado | Pocos contactos al día, validando el proceso | Hoja de cálculo con validaciones + WhatsApp Business (app) con etiquetas, respuestas rápidas, mensaje de bienvenida y catálogo + formularios |
| 1 — CRM | Varias personas atienden o se pierden seguimientos | CRM con pipeline (p. ej. Odoo CRM, HubSpot, Kommo, Pipedrive), email marketing (p. ej. Brevo, Mailchimp, MailerLite), agenda en línea (p. ej. Cal.com, Calendly) |
| 2 — Integrado | Volumen alto, varios canales, recompra programada | WhatsApp Business Platform (API) mediante un proveedor, chatbots (p. ej. ManyChat para Instagram/Messenger/WhatsApp), integraciones (p. ej. Make, Zapier, n8n), conexión con ERP y tienda online |

Si el negocio ya usa un ERP o CRM (p. ej. Odoo), diseña dentro de él antes de sumar otra herramienta.

Al integrar sistemas: cada evento (formulario, mensaje, pedido) debe tener un identificador para que un reintento no cree contactos o pedidos duplicados.

## 5. Atribución: saber de dónde vino cada venta

- **UTM** en todos los enlaces: `utm_source` (facebook, instagram, google, aliado), `utm_medium` (cpc, social, email, qr), `utm_campaign` (nombre de la campaña), `utm_content` (variante del anuncio).
- **WhatsApp:** enlace `https://wa.me/<número>?text=<mensaje prellenado codificado>` con un texto distinto por campaña o aliado ("Hola, vengo del anuncio A1"). El responsable registra el origen según ese texto. Los anuncios de clic a WhatsApp también muestran el origen en la herramienta de anuncios.
- **Aliados y puntos de venta:** código o QR único por aliado; acuerda por escrito cómo se atribuyen las ventas directas que genera.
- **Píxel / API de conversiones** de la plataforma de anuncios en la página de gracias o confirmación de compra, si hay tienda online.
- **Pregunta de respaldo:** "¿Cómo nos conociste?" en el formulario o en la conversación, con opciones cerradas.

## 6. Agentes de IA y bots

Útiles para responder al instante, calificar y agendar. Definir siempre:

- Qué puede hacer (responder preguntas frecuentes, calificar, mostrar catálogo, agendar) y qué no (prometer precios especiales, dar consejos médicos o veterinarios, cerrar acuerdos fuera de la política).
- Fuente de información aprobada (catálogo, precios vigentes, zonas, políticas).
- Criterios de **traspaso a humano** (pide una persona, objeción compleja, cliente de alto valor, queja) y tiempo máximo hasta que la persona responda.
- Que el usuario sepa que habla con un asistente automático cuando corresponda.
- Revisión semanal de conversaciones para corregir respuestas.

## 7. Permisos y cumplimiento

- Guarda el **permiso** para enviar mensajes comerciales: cuándo, por qué medio y con qué texto. Quien escribe primero por WhatsApp abre una conversación, pero los envíos posteriores de recordatorios o promociones requieren su aceptación.
- **WhatsApp Business Platform (API):** fuera de la ventana de atención al cliente (24 h desde el último mensaje del usuario) solo se pueden enviar plantillas aprobadas y con opt-in. Respeta la política comercial de WhatsApp.
- **Datos personales:** en Colombia, Ley 1581 de 2012 (habeas data) y su reglamentación: autorización previa e informada, política de tratamiento publicada y canal para consultas y supresión. En Brasil, LGPD; en otros países, la norma local. Recomienda revisión legal cuando el uso de datos sea intensivo.
- **Publicidad:** las afirmaciones deben ser veraces y comprobables (en Colombia, Estatuto del Consumidor, Ley 1480 de 2011).
- Toda comunicación incluye una forma simple de darse de baja, y la baja se respeta en todos los sistemas.
