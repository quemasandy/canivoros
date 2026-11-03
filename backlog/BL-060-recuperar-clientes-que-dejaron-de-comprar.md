---
key: BL-060
issue_type: Experimento
summary: Recuperar clientes que dejaron de comprar
description: Con la base de BL-004, listar clientes con una sola compra o sin compra desde hace más que su intervalo habitual. Contactar solo a quienes tengan permiso (BL-058) con un mensaje de reposición y precio real (BL-005). Medir quiénes compran.
priority: High
status: Backlog
assignee: Andrés (lista y medición) + Omar/Canívoros (contacto) (propuesta)
effort: S
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- retencion
- experimento
- recompra
dependencies:
- BL-004
- BL-005
- BL-044
- BL-058
acceptance_criteria:
- Lista de candidatos desde BL-004 con criterio documentado
- Solo se contacta a clientes con permiso registrado
- Compraron ÷ contactados en 14 días
- COP recuperados (solo con precio confirmado; si no, desconocido)
- Contribución en COP si se conoce el costo; si no, se registra como desconocido
- Gasto máximo definido antes de empezar y gasto real registrado
- Conversión de la etapa medida (p. ej. contactados→respuesta→compra)
- Regla seguir/ajustar/parar escrita en la ficha BL-044 y aplicada al cierre
hechos:
- Existen ventas jul–oct 2026 por cliente y fecha (BL-004).
hipotesis:
- Parte de los clientes inactivos vuelve a comprar con un recordatorio y precio claro.
sources:
- auditoría Growth Partner 31/10/2026
order: 10
---

# BL-060 · Recuperar clientes que dejaron de comprar

Con la base de BL-004, listar clientes con una sola compra o sin compra desde hace más que su intervalo habitual. Contactar solo a quienes tengan permiso (BL-058) con un mensaje de reposición y precio real (BL-005). Medir quiénes compran.

## Hechos
Existen ventas jul–oct 2026 por cliente y fecha (BL-004). No depende de BL-041.

## Supuestos
Hipótesis: parte de los clientes inactivos vuelve a comprar con un recordatorio y precio claro.
