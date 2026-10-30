---
key: BL-051
issue_type: Requisito
summary: Evitar pedidos duplicados en integraciones
description: Cuando WhatsApp, Instagram o formularios creen pedidos o leads automáticamente, un mismo evento no debe crear dos registros.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- requisito
dependencies:
- BL-011
acceptance_criteria:
- 'Prueba: enviar el mismo mensaje dos veces crea un solo registro'
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Primera implementación de software)
order: 37
---

# BL-051 · Evitar pedidos duplicados en integraciones

Cuando WhatsApp, Instagram o formularios creen pedidos o leads automáticamente, un mismo evento no debe crear dos registros.

## Hechos
El plan lo pone como criterio de aceptación del primer sistema.

## Supuestos
Responsable, plazo y esfuerzo son propuestas.
