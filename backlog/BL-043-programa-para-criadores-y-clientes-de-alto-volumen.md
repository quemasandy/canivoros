---
key: BL-043
issue_type: Experimento
summary: Programa para criadores y clientes de alto volumen
description: Las ventas de jul–oct muestran compras grandes de criadores (40–520 kg). Identificar los 10 clientes de más kilos, entrevistar a 3 y probar una condición para ellos (pedido programado, precio por volumen o referidos).
priority: Medium
status: Backlog
assignee: Omar/Canívoros + Andrés (datos) (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- ventas
- criadores
- experimento
dependencies:
- BL-004
- BL-044
acceptance_criteria:
- Top 10 clientes por kilos de jul–oct
- 3 conversaciones registradas
- Oferta probada y resultado medido en 4 semanas
- Kilos y COP del grupo en 4 semanas vs sus 4 semanas anteriores (COP solo con precio confirmado)
- '% que acepta la condición y % que repite'
- Ingreso en COP atribuido al experimento (con precio confirmado sí/no)
- Contribución en COP si se conoce el costo; si no, se registra como desconocido
- Gasto máximo definido antes de empezar y gasto real registrado
- Conversión de la etapa medida (p. ej. contactados→respuesta→compra)
- Regla seguir/ajustar/parar escrita en la ficha BL-044 y aplicada al cierre
sources:
- ventas_canivoros_2026.xlsx (columnas 'CRIADOR KG')
order: 37
hechos:
- El Excel separa ventas a cliente, almacén y criador; hay pedidos de criadores de 40 a 520 kg.
hipotesis:
- El segmento criadores es el más rentable (por validar).
---

# BL-043 · Programa para criadores y clientes de alto volumen

Las ventas de jul–oct muestran compras grandes de criadores (40–520 kg). Identificar los 10 clientes de más kilos, entrevistar a 3 y probar una condición para ellos (pedido programado, precio por volumen o referidos).

## Hechos
El Excel separa ventas a cliente, almacén y criador; hay pedidos de criadores de 40 a 520 kg.

Ajuste 31/10/2026 (auditoría Growth Partner): criterios en dinero añadidos; no hay precios, costos ni márgenes confirmados en el backlog.

## Supuestos
Que el segmento criadores sea el más rentable es una hipótesis.
