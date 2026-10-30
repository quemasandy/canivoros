---
key: BL-004
issue_type: Tarea
summary: Calcular línea base con ventas_canivoros_2026.xlsx
description: El repo ya tiene ventas de julio a octubre 2026 (hojas JULIO, AGOSTO, SEPT., OCT.) por cliente, fecha y producto. Limpiar nombres de cliente, unificar unidades (lb/kg), separar cliente final, almacén/distribuidor y criador, y sacar kilos por mes, por producto y por tipo de cliente, más recompra (clientes que repiten).
priority: Highest
status: Backlog
assignee: Andrés (propuesta)
effort: M
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- datos
- linea-base
- canivoros
dependencies: []
acceptance_criteria:
- Tabla resumen kilos/mes por producto y por tipo de cliente
- Número de clientes únicos y % que repite en el periodo
- Lista de dudas de datos (unidades, filas sin fecha) para Sara/la prima
- Se marca qué es dato y qué es estimado
sources:
- 'develop: ventas_canivoros_2026.xlsx'
---

# BL-004 · Calcular línea base con ventas_canivoros_2026.xlsx

El repo ya tiene ventas de julio a octubre 2026 (hojas JULIO, AGOSTO, SEPT., OCT.) por cliente, fecha y producto. Limpiar nombres de cliente, unificar unidades (lb/kg), separar cliente final, almacén/distribuidor y criador, y sacar kilos por mes, por producto y por tipo de cliente, más recompra (clientes que repiten).

## Hechos
El archivo tiene registros jul–oct 2026 sin precios.

## Supuestos
Hacen falta precios por canal para convertir kilos a dinero (BL-005).
