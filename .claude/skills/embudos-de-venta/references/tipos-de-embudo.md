# Tipos de embudo

Cada tipo describe cuándo usarlo, sus etapas, las piezas que hay que producir, las métricas que lo gobiernan y los fallos más frecuentes. Combina tipos cuando haga falta: casi siempre hay un embudo de adquisición y otro de retención.

## Contenido

1. [Conversacional por WhatsApp / DM](#1-conversacional-por-whatsapp--dm)
2. [Primera compra + recompra (consumo recurrente)](#2-primera-compra--recompra-consumo-recurrente)
3. [E-commerce directo](#3-e-commerce-directo)
4. [Imán de leads + nutrición](#4-imán-de-leads--nutrición)
5. [Oferta de entrada (tripwire) + upsell](#5-oferta-de-entrada-tripwire--upsell)
6. [Clase, webinar o VSL](#6-clase-webinar-o-vsl)
7. [Aplicación + llamada (ticket alto, servicios, consultoría)](#7-aplicación--llamada-ticket-alto-servicios-consultoría)
8. [B2B: tiendas, distribuidores y empresas](#8-b2b-tiendas-distribuidores-y-empresas)
9. [Negocio local con citas](#9-negocio-local-con-citas)
10. [Reactivación de base](#10-reactivación-de-base)
11. [Lanzamiento](#11-lanzamiento)
12. [Referidos](#12-referidos)

---

## 1. Conversacional por WhatsApp / DM

**Cuándo:** el cliente quiere preguntar antes de comprar (precio, entrega, cuál le sirve); ticket bajo a medio; mercados donde WhatsApp es el canal habitual.

**Etapas:** contenido o anuncio con botón "Enviar mensaje" / enlace `wa.me` → mensaje de bienvenida (inmediato) → 2–4 preguntas de calificación → recomendación y oferta concreta (producto, precio, entrega, forma de pago) → objeciones → seguimiento → cierre con instrucciones claras → confirmación, entrega y post-venta → recompra.

**Piezas:** anuncios de clic a WhatsApp o publicaciones con CTA, enlace con texto prellenado que identifique el origen ("Hola, vi el anuncio A"), mensaje de bienvenida, respuestas rápidas, catálogo de WhatsApp Business, guion de calificación, respuestas a objeciones, mensajes de seguimiento, mensaje de cierre con datos de pago y entrega.

**Métricas:** conversaciones iniciadas, tiempo de primera respuesta, % que responde a la calificación, % calificados, % que recibe oferta, % cierre, ticket, costo por conversación, CAC.

**Fallos típicos:** responder horas después; mandar el precio solo sin contexto ni recomendación; no hacer seguimiento; varios números o personas sin registro común; no registrar el origen.

## 2. Primera compra + recompra (consumo recurrente)

**Cuándo:** productos que se acaban (alimento de mascotas, café, suplementos, insumos, cosméticos). La rentabilidad depende de la segunda, tercera y siguientes compras.

**Etapas:** adquisición (cualquier embudo de entrada) → primera compra (a menudo con presentación de prueba o incentivo) → onboarding (cómo usarlo, cómo hacer la transición, qué esperar) → control de satisfacción (a los pocos días) → recordatorio de reposición antes de que se acabe → recompra → suscripción o pedido programado → referidos.

**Cálculo del recordatorio:** días de duración = contenido del empaque ÷ consumo diario confirmado. Programa el recordatorio unos días antes. No inventes raciones o consumos: usa la guía del fabricante o lo que declare el cliente.

**Piezas:** mensaje de bienvenida post-compra, guía de uso, mensaje de control ("¿cómo le fue?"), recordatorio de reposición, oferta de pedido programado o suscripción, solicitud de reseña o referido.

**Métricas:** tasa de segunda compra en 30/60/90 días, intervalo entre compras, compras por cliente en 12 meses, LTV de contribución, bajas de recordatorios, churn de suscripción.

**Fallos típicos:** invertir todo en adquisición y nada en post-venta; descuentos de primera compra que atraen buscadores de promociones que no repiten; recordatorios sin permiso o demasiado frecuentes.

## 3. E-commerce directo

**Cuándo:** catálogo con precios claros, compra sin necesidad de conversación, tráfico de anuncios, buscadores o redes.

**Etapas:** anuncio/búsqueda → página de producto o colección → agregar al carrito → checkout → order bump (complemento en el checkout) → upsell post-compra → confirmación → recuperación de carrito abandonado → post-venta y recompra.

**Piezas:** fichas de producto con beneficios, fotos y prueba social real; checkout corto; políticas visibles de envío, cambios y pagos; emails/WhatsApp de carrito abandonado; ofertas de complemento.

**Métricas:** CTR, costo por visita, tasa de agregar al carrito, tasa de inicio de checkout, tasa de compra, ticket promedio, % que toma el complemento, ROAS, CAC.

**Fallos típicos:** costo de envío revelado tarde, pocas formas de pago locales, página lenta en celular, falta de confianza (sin reseñas, sin datos de contacto).

## 4. Imán de leads + nutrición

**Cuándo:** ticket medio, el cliente necesita entender el problema o confiar antes de comprar, ciclo de decisión de días o semanas.

**Etapas:** contenido o anuncio → página de captura (promesa específica + formulario corto) → página de gracias (entrega + siguiente paso, idealmente una oferta o invitación a conversar) → secuencia de nutrición (4–7 mensajes en 1–2 semanas) → oferta → seguimiento → venta.

**Buenos imanes:** calculadora, checklist, guía corta, diagnóstico o test, plantilla, muestra, mini clase. Deben resolver un problema pequeño **del mismo cliente que comprará la oferta**.

**Métricas:** conversión de la página de captura, costo por lead, apertura y clics de la secuencia, % de leads que pasan a oportunidad, % de venta en 30 días.

**Fallos típicos:** imán genérico ("ebook de consejos") que atrae curiosos; secuencia sin oferta; pedir teléfono, email, empresa y cargo para algo gratuito y pequeño.

## 5. Oferta de entrada (tripwire) + upsell

**Cuándo:** se quiere convertir rápido a interesados en clientes con una compra pequeña, y existe una oferta principal o complementos de mayor valor.

**Etapas:** anuncio → página de oferta de entrada (precio bajo, valor alto y concreto) → checkout con order bump → upsell de un clic o mensaje post-compra → entrega → oferta principal.

**Regla económica:** la oferta de entrada + complementos debería cubrir una parte relevante del costo de adquisición. Calcula con `scripts/calcular_embudo.py` si la primera compra se autofinancia o depende de la recompra.

**Fallos típicos:** precio bajo con margen negativo sin plan de continuidad; producto de entrada sin relación con la oferta principal.

## 6. Clase, webinar o VSL

**Cuándo:** producto o servicio que necesita demostración y explicación (cursos, software, servicios profesionales, programas), ticket medio a alto.

**Etapas:** anuncio/contenido → registro → recordatorios (confirmación, 24 h, 1 h, en vivo) → asistencia → contenido de valor + demostración → oferta con fecha límite real → repetición disponible por tiempo limitado → seguimiento → venta o llamada.

**Estructura de la presentación:** gran promesa → historia o caso → 3 ideas o "secretos" que derriban creencias que bloquean la compra → demostración/prueba → transición a la oferta → oferta con todo lo que incluye → garantía → preguntas → cierre.

**Métricas:** costo por registro, tasa de asistencia, % que ve hasta la oferta, % compra o agenda, ventas por asistente.

**Fallos típicos:** demasiada teoría y oferta apresurada al final; no enviar recordatorios; urgencia inventada.

## 7. Aplicación + llamada (ticket alto, servicios, consultoría)

**Cuándo:** servicios a medida, consultoría, B2B, programas de alto valor; la venta requiere entender el caso del cliente.

**Etapas:** contenido de autoridad (casos, diagnósticos, artículos, video) → oferta de conversación o diagnóstico (gratuito o pagado) → formulario de aplicación con preguntas de calificación → agenda → recordatorios → llamada de diagnóstico → propuesta → seguimiento → cierre → onboarding.

**Calificación:** necesidad, urgencia, presupuesto, quién decide, encaje con el servicio. Un diagnóstico pagado de bajo costo filtra y a la vez es oferta de entrada.

**Guion de llamada:** objetivo de la llamada → situación actual → problema y costo de no resolverlo → situación deseada → obstáculos → ¿qué han intentado? → presentación de la solución ligada a lo dicho → inversión → objeciones → siguiente paso con fecha.

**Métricas:** solicitudes, % calificadas, % que agenda, % asistencia (show rate), % cierre por llamada, ciclo de venta en días, ticket, LTV del contrato.

**Fallos típicos:** agendar con cualquiera; propuestas genéricas; no hacer seguimiento después de la propuesta.

## 8. B2B: tiendas, distribuidores y empresas

**Cuándo:** se vende a puntos de venta, distribuidores, clínicas, gimnasios, empresas; el comprador revende o usa el producto en su operación.

**Etapas:** lista de prospectos verificada y segmentada → primer contacto (visita, llamada, WhatsApp, email) → conversación de descubrimiento (marcas que venden, rotación, margen requerido, pedido mínimo, plazo de pago) → muestra o pedido piloto con condiciones claras → material de apoyo en el punto (exhibición, QR o código por aliado) → seguimiento de venta al consumidor → reposición → ampliación de surtido o zona.

**Piezas:** propuesta comercial de una página (condiciones, margen, apoyo), presentación del producto, material punto de venta, guion de visita, seguimiento de reposición, código de aliado para atribuir ventas directas.

**Métricas:** prospectos contactados, % reunión, % pedido piloto, % reposición a 30/60 días, sell-out (venta al consumidor) cuando se pueda conocer, cartera y días de cobro.

**Fallos típicos:** contar el pedido inicial como éxito sin medir reposición; conflictos entre venta directa y aliados por no definir territorios ni atribución; no cobrar a tiempo.

## 9. Negocio local con citas

**Cuándo:** clínicas, veterinarias, salones, talleres, gimnasios, servicios a domicilio.

**Etapas:** búsqueda local, redes o referidos → consulta (WhatsApp, llamada, web) → oferta de cita → agenda → recordatorios (24 h y 2 h) → asistencia → servicio → solicitud de reseña → recordatorio del siguiente servicio → reactivación.

**Métricas:** consultas, % que agenda, % asistencia, ticket por visita, % que vuelve, reseñas obtenidas.

**Fallos típicos:** no confirmar citas; no pedir reseñas; no programar el siguiente servicio.

## 10. Reactivación de base

**Cuándo:** existe una lista de clientes antiguos o interesados que dejaron de interactuar. Suele ser la fuente más barata de ventas a corto plazo.

**Etapas:** segmentar (por última compra, producto, valor) → verificar permiso de contacto → mensaje de reconexión personal (sin vender de inmediato o con una razón real: novedad, nueva presentación, cambio de zona) → oferta específica → seguimiento → registrar respuestas y motivos de abandono.

**Métricas:** % entregados, % respuesta, % compra, bajas solicitadas, motivos de abandono registrados.

**Fallos típicos:** mensaje masivo genérico; contactar a quien no dio permiso; no aprender de los motivos de abandono.

## 11. Lanzamiento

**Cuándo:** producto o servicio nuevo, nueva cohorte, temporada.

**Etapas:** pre-lanzamiento (contenido que genera expectativa + lista de interesados) → apertura (oferta con fecha) → recordatorios durante el periodo → cierre real → seguimiento post-cierre y onboarding.

**Métricas:** tamaño de la lista de espera, % compra en apertura, ventas por día de carrito abierto.

**Fallos típicos:** reabrir "el último día" varias veces (destruye la confianza); lanzar sin lista previa.

## 12. Referidos

**Cuándo:** clientes satisfechos y producto fácil de recomendar. Funciona como etapa final de cualquier embudo.

**Etapas:** momento de satisfacción (después de un resultado visible) → invitación a recomendar con un mensaje listo para reenviar → incentivo para ambos (si aplica y es sostenible) → seguimiento del referido con su origen registrado.

**Métricas:** % clientes que refieren, referidos por cliente, conversión de referidos, CAC del canal.
