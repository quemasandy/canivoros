---
key: BL-004
issue_type: Tarea
summary: Calcular línea base con ventas_canivoros_2026.xlsx
description: El repo ya tiene ventas de julio a octubre 2026 (hojas JULIO, AGOSTO, SEPT., OCT.) por cliente, fecha y producto. Limpiar nombres de cliente, unificar unidades (lb/kg), separar cliente final, almacén/distribuidor y criador, y sacar kilos por mes, por producto y por tipo de cliente, más recompra (clientes que repiten). Convertir kilos a COP cuando BL-005 tenga precios confirmados; hasta entonces reportar kilos y número de clientes. Incluir el intervalo real entre compras por cliente (insumo de BL-022 y BL-060).
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
dependencies:
- BL-005 (solo para la conversión a COP; kilos y clientes no dependen)
acceptance_criteria:
- Tabla resumen kilos/mes por producto y por tipo de cliente
- Número de clientes únicos y % que repite en el periodo
- Lista de dudas de datos (unidades, filas sin fecha) para Sara/la prima
- Se marca qué es dato y qué es estimado
- 'Ingreso estimado por mes, producto y tipo de cliente, con columna "precio confirmado: sí/no" (si no hay precio: desconocido, no se estima)'
- Intervalo real entre compras por cliente y lista de clientes con una sola compra o sin compra reciente
sources:
- 'develop: ventas_canivoros_2026.xlsx'
order: 4
hechos:
- El archivo tiene registros jul–oct 2026 por cliente, fecha y producto, sin precios.
hipotesis:
- Los precios de BL-005 permitirán convertir los kilos históricos a COP.
---

# BL-004 · Calcular línea base con ventas_canivoros_2026.xlsx

El repo ya tiene ventas de julio a octubre 2026 (hojas JULIO, AGOSTO, SEPT., OCT.) por cliente, fecha y producto. Limpiar nombres de cliente, unificar unidades (lb/kg), separar cliente final, almacén/distribuidor y criador, y sacar kilos por mes, por producto y por tipo de cliente, más recompra (clientes que repiten). Convertir kilos a COP cuando BL-005 tenga precios confirmados; hasta entonces reportar kilos y número de clientes. Incluir el intervalo real entre compras por cliente (insumo de BL-022 y BL-060).

## Hechos
El archivo tiene registros jul–oct 2026 sin precios.

## Supuestos
Hacen falta precios por canal para convertir kilos a dinero (BL-005).
