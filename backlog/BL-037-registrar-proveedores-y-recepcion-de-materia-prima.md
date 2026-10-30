---
key: BL-037
issue_type: Historia
summary: Registrar proveedores y recepción de materia prima
description: 'Aplicar el flujo de erp.md: disponibilidad del proveedor → compra → recepción → cuarto frío → salida a producción. Crear en Odoo o en una hoja el catálogo de materias primas (cabeza de pollo, barriga de salmón, canilla y vísceras de cerdo), los proveedores y un registro por cada ingreso, con fecha, kilos y costo.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- odoo
- abastecimiento
- trazabilidad
dependencies:
- BL-011
acceptance_criteria:
- Catálogo de materias primas y proveedores cargado
- Cada ingreso tiene identificador, fecha, kilos aceptados y costo por kilo
- Se puede saber qué ingreso se usó en un lote de producción
sources:
- erp.md (Compras, recepción y almacenamiento)
order: 24
---

# BL-037 · Registrar proveedores y recepción de materia prima

Aplicar el flujo de erp.md: disponibilidad del proveedor → compra → recepción → cuarto frío → salida a producción. Crear en Odoo o en una hoja el catálogo de materias primas (cabeza de pollo, barriga de salmón, canilla y vísceras de cerdo), los proveedores y un registro por cada ingreso, con fecha, kilos y costo.

## Hechos
La materia prima llega congelada, de varios proveedores, y suele procesarse en la semana siguiente.

## Supuestos
Los criterios de aceptación y temperatura todavía no están definidos.
