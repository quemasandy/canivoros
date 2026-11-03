# Métricas del embudo

Definiciones, fórmulas, cómo fijar metas y cómo diagnosticar fugas. El script `scripts/calcular_embudo.py` hace estos cálculos; esta guía sirve para interpretarlos y explicarlos.

## Contenido

1. [Indicadores por etapa](#1-indicadores-por-etapa)
2. [Economía unitaria](#2-economía-unitaria)
3. [Fijar metas de atrás hacia adelante](#3-fijar-metas-de-atrás-hacia-adelante)
4. [Tablero semanal](#4-tablero-semanal)
5. [Diagnóstico de fugas](#5-diagnóstico-de-fugas)
6. [Experimentos y tamaño de muestra](#6-experimentos-y-tamaño-de-muestra)

---

## 1. Indicadores por etapa

| Indicador | Fórmula | Etapa |
|---|---|---|
| CTR | Clics ÷ impresiones | Atracción |
| Costo por clic (CPC) | Gasto ÷ clics | Atracción |
| CPM | Gasto ÷ impresiones × 1.000 | Atracción |
| Conversión de página | Leads o acciones ÷ visitas | Captación |
| Costo por lead (CPL) | Gasto ÷ leads | Captación |
| Tiempo de primera respuesta | Hora de respuesta − hora del primer mensaje | Calificación |
| Tasa de calificación | Leads calificados ÷ leads | Calificación |
| Asistencia (show rate) | Asistentes ÷ agendados | Llamada / cita / webinar |
| Tasa de cierre | Ventas ÷ oportunidades (u ofertas enviadas) | Cierre |
| Ticket promedio | Ingresos ÷ número de pedidos | Cierre |
| Tasa de segunda compra | Clientes con 2.ª compra en X días ÷ clientes con 1.ª compra en el mismo grupo | Retención |
| Intervalo de recompra | Días promedio entre compras | Retención |
| Churn | Clientes o suscripciones perdidas en el periodo ÷ activos al inicio | Retención |

Cada tasa se mide **contra la etapa anterior** y en el mismo periodo o grupo (cohorte). Mezclar periodos distorsiona las conversiones.

## 2. Economía unitaria

| Indicador | Fórmula | Para qué sirve |
|---|---|---|
| Contribución por compra | Precio − costos variables (producto, empaque, envío, comisiones de pago, comisión de aliado, descuento) | Cuánto deja cada venta para pagar adquisición y gastos fijos |
| Margen de contribución | Contribución ÷ precio | Base del ROAS de equilibrio |
| CAC | Gasto total de adquisición (medios + herramientas + muestras + horas comerciales si se asignan) ÷ clientes nuevos | Cuánto cuesta cada cliente |
| LTV de contribución | Contribución por compra × compras por cliente en el horizonte | Cuánto deja un cliente en, p. ej., 12 meses |
| LTV / CAC | LTV ÷ CAC | Salud del embudo. Regla práctica común: ≥ 3 sano; 1–3 ajustado; < 1 pierde dinero |
| ROAS | Ingresos atribuidos ÷ gasto en anuncios | Rendimiento de la pauta |
| ROAS de equilibrio | 1 ÷ margen de contribución | ROAS mínimo para no perder en la primera compra |
| Recuperación del CAC | CAC ÷ contribución por compra | Cuántas compras se necesitan para recuperar la adquisición |

Usa **contribución**, no ingresos, para el LTV: un cliente que compra mucho con margen cero no paga su adquisición. Si no hay costos variables confirmados, trabaja con un margen supuesto, márcalo y muestra cómo cambia el resultado con escenarios.

## 3. Fijar metas de atrás hacia adelante

1. Meta de clientes nuevos (o de ingresos ÷ ticket).
2. ÷ tasa de cierre = oportunidades u ofertas necesarias.
3. ÷ tasa de calificación = leads necesarios.
4. ÷ conversión de página o de conversación = clics o visitas necesarios.
5. ÷ CTR = impresiones o alcance necesario.
6. × costo por unidad = presupuesto de medios.

Compara el resultado con el presupuesto y la **capacidad de atención y de producción**: si se necesitan 400 conversaciones al mes y una sola persona atiende, el cuello de botella está ahí, no en los anuncios.

Las tasas de conversión varían mucho entre países, sectores, ofertas y canales. Prioriza siempre los datos del propio negocio; si no existen, usa supuestos conservadores, márcalos y define en cuántas semanas se reemplazarán por datos.

## 4. Tablero semanal

Una fila por semana y una columna por etapa (volumen y conversión), más gasto, CPL, CAC, ventas, ticket, recompras y bajas. Mira tendencias de varias semanas, no un día suelto. Revisa en la misma reunión: ¿qué etapa empeoró?, ¿qué experimento está corriendo?, ¿qué decisión se toma?

## 5. Diagnóstico de fugas

| Síntoma | Causas probables | Qué revisar o probar |
|---|---|---|
| Alcance alto, pocos clics (CTR bajo) | Gancho débil, público equivocado, creativo cansado | Nuevos ángulos y ganchos, segmentación, formato (video vs. imagen) |
| Muchos clics, pocos leads o conversaciones | Desconexión anuncio–página, página lenta o confusa, oferta poco clara, formulario largo | Coherencia de mensaje, velocidad en celular, un solo CTA, menos campos |
| Muchos leads, pocos calificados | Imán o anuncio atrae al público equivocado, promesa demasiado amplia | Ajustar el imán a la oferta, calificar en el formulario, mostrar precio o zona antes |
| Leads calificados que no compran | Oferta débil, precio sin contexto, falta de prueba, seguimiento inexistente, respuesta lenta | Tiempo de respuesta, guion de recomendación, objeciones, seguimiento D+1/D+3/D+7, oferta de entrada |
| Agendan pero no asisten | Sin recordatorios, agenda muy lejana, poco compromiso | Recordatorios 24 h y 2 h, agendar en 48–72 h, confirmar por mensaje |
| Compran una vez y no vuelven | Experiencia de entrega, producto no cumplió, nadie les recordó | Encuesta post-venta, recordatorio de reposición, onboarding, motivos de no recompra |
| Vende pero pierde dinero | CAC mayor que la contribución, descuentos excesivos, costos variables subestimados | Economía unitaria, ticket (complementos), recompra, canales más baratos (referidos, base propia) |

Prioriza acciones con un puntaje simple de **impacto × confianza × facilidad** (1–5 cada uno) y empieza por las etapas cercanas a la venta.

## 6. Experimentos y tamaño de muestra

- Escribe antes de lanzar: hipótesis, variable que cambia, métrica principal, periodo, umbral de decisión y presupuesto máximo.
- Cambia una variable a la vez (gancho, oferta, precio, página, guion) y mantén el resto igual.
- Con pocas conversiones el azar pesa mucho: con decenas de ventas por variante, una diferencia pequeña no es concluyente. Si el volumen es bajo, prueba cambios grandes (otra oferta, otro ángulo) en lugar de detalles, y presenta los resultados como indicios.
- Registra el resultado y la decisión aunque el experimento "falle": evita repetir pruebas.
