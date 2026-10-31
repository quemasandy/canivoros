---
key: BL-022
issue_type: Experimento
summary: Recordatorio de reposición a clientes
description: 'Con permiso del cliente, enviar recordatorio antes de la siguiente compra esperada. V1: usar el intervalo real entre compras de cada cliente (BL-004). V2: ajustar con peso del empaque y ración confirmada (BL-041). Medir recompra y bajas.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- retencion
- experimento
dependencies:
- BL-004
- BL-044
- BL-058
acceptance_criteria:
- Lista de clientes con permiso
- Recordatorios enviados y recompra medida en 30 días
- V1 basada en intervalo real de BL-004, sin depender de BL-041
- Recompra a 30 días de quienes recibieron recordatorio vs quienes no
- Solicitudes de baja registradas
- Ingreso en COP atribuido al experimento (con precio confirmado sí/no)
- Contribución en COP si se conoce el costo; si no, se registra como desconocido
- Gasto máximo definido antes de empezar y gasto real registrado
- Conversión de la etapa medida (p. ej. contactados→respuesta→compra)
- Regla seguir/ajustar/parar escrita en la ficha BL-044 y aplicada al cierre
sources:
- 'plan Bogotá: Experimento 4'
order: 43
hipotesis:
- Un recordatorio antes de la fecha esperada aumenta la recompra.
- Raciones (BL-041) quedan para la v2.
---

# BL-022 · Recordatorio de reposición a clientes

Con permiso del cliente, enviar recordatorio antes de la siguiente compra esperada. V1: usar el intervalo real entre compras de cada cliente (BL-004). V2: ajustar con peso del empaque y ración confirmada (BL-041). Medir recompra y bajas.

## Hechos
Ver fuentes.

Ajuste 31/10/2026 (auditoría Growth Partner): criterios en dinero añadidos; no hay precios, costos ni márgenes confirmados en el backlog.

## Supuestos
Responsable, plazo y esfuerzo son propuestas.
