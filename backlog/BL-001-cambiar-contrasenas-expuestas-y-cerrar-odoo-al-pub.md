---
key: BL-001
issue_type: Acción
summary: Cambiar contraseñas expuestas y cerrar Odoo al público
description: Cambiar las claves del panel de hosting, del acceso root al VPS y del usuario de Odoo, que se compartieron en el chat. Activar acceso por llave SSH, desactivar login por contraseña y cerrar el puerto 8069 o ponerlo detrás de HTTPS/Tailscale.
priority: Highest
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- seguridad
- infra
dependencies: []
acceptance_criteria:
- Las tres claves fueron cambiadas (sin escribirlas en el repo ni en el chat)
- El VPS solo acepta llave SSH
- Odoo no responde en http://IP:8069 desde internet sin VPN o HTTPS
- Nunca más se comparten claves por WhatsApp; se usa un gestor de contraseñas
sources:
- chat 26/10 y 27/10
- informe ejecutivo, sección E
---

# BL-001 · Cambiar contraseñas expuestas y cerrar Odoo al público

Cambiar las claves del panel de hosting, del acceso root al VPS y del usuario de Odoo, que se compartieron en el chat. Activar acceso por llave SSH, desactivar login por contraseña y cerrar el puerto 8069 o ponerlo detrás de HTTPS/Tailscale.

## Hechos
Las claves se pegaron en texto plano en el chat; Odoo estaba accesible por IP pública y HTTP.

## Supuestos
Responsable, plazo y esfuerzo son propuestas.
