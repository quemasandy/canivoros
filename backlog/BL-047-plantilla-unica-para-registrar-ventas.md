---
key: BL-047
issue_type: Mejora
summary: Plantilla única para registrar ventas
description: El Excel de ventas cambia de columnas cada mes (julio 11 columnas, octubre 14), mezcla libras y kilos y tiene filas sin fecha. Definir una sola plantilla (o formulario) con cliente, fecha, producto, presentación, unidad, cantidad, precio y canal, hasta que todo pase a Odoo. Desde ya incluir los campos origen (campaña, aliado, Omar, orgánico, desconocido), canal de cierre (WhatsApp, tienda, distribuidor, otro) y código de aliado/QR, aunque sea en una hoja antes de Odoo.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- mejora
dependencies:
- BL-005
acceptance_criteria:
- Plantilla con columnas fijas y listas desplegables
- Unidad única por producto
- Octubre migrado a la plantilla como prueba
- Campos origen, canal de cierre y código de aliado/QR presentes en la plantilla
- '% semanal de ventas con origen registrado medido desde la semana 2'
sources:
- ventas_canivoros_2026.xlsx
order: 12
hechos:
- Las hojas JULIO, AGOSTO, SEPT. y OCT. tienen columnas distintas y filas sin fecha.
hipotesis:
- Registrar el origen desde la semana 2 permite verificar atribución en BL-021 (semana 6).
---

# BL-047 · Plantilla única para registrar ventas

El Excel de ventas cambia de columnas cada mes (julio 11 columnas, octubre 14), mezcla libras y kilos y tiene filas sin fecha. Definir una sola plantilla (o formulario) con cliente, fecha, producto, presentación, unidad, cantidad, precio y canal, hasta que todo pase a Odoo. Desde ya incluir los campos origen (campaña, aliado, Omar, orgánico, desconocido), canal de cierre (WhatsApp, tienda, distribuidor, otro) y código de aliado/QR, aunque sea en una hoja antes de Odoo.

## Hechos
Las hojas JULIO, AGOSTO, SEPT. y OCT. tienen columnas distintas; hay filas sin fecha (p. ej. un pedido de 520 kg en julio).

## Supuestos
Responsable, plazo y esfuerzo son propuestas.
