# Aporte: Marketing Analyst (Paid Media Measurement)

> **Especialidad:** Paid media reporting and measurement: KPIs, tracking, weekly/monthly reports, spend thresholds  
> **Fecha:** 2026-11-11  
> **Estado:** Propuesta para revisión de Andrés

---

## Resumen

Este aporte proporciona la **infraestructura de medición técnica** necesaria antes de invertir en anuncios pagados (Meta Ads). Complementa los documentos existentes del repositorio:

- El plan de crecimiento de Bogotá define **qué medir** a nivel de negocio (ventas netas, CAC, recompra).
- Los embudos E03 y E04 definen **la estructura de las campañas**.
- Este aporte define **cómo implementar el tracking** y **cómo reportar los resultados**.

---

## Archivos incluidos

| Archivo | Contenido |
|---------|-----------|
| [PLAN-MEDICION-PAID-MEDIA.md](PLAN-MEDICION-PAID-MEDIA.md) | Plan maestro: tracking por canal, UTMs, atribución de WhatsApp, checklist pre-lanzamiento |
| [ARBOL-KPI-PAID-MEDIA.md](ARBOL-KPI-PAID-MEDIA.md) | Árbol de métricas con fórmulas exactas, desde impresiones hasta ROAS |
| [UMBRALES-ALERTA-PAID-MEDIA.md](UMBRALES-ALERTA-PAID-MEDIA.md) | Reglas de alerta con pisos silenciosos para evitar reaccionar con datos insuficientes |
| [PLANTILLA-REPORTE-SEMANAL.md](PLANTILLA-REPORTE-SEMANAL.md) | Plantilla para generar el reporte semanal de paid media |

---

## Relación con el backlog

| Tarea del backlog | Cómo este aporte la apoya |
|-------------------|---------------------------|
| BL-013 (Tablero semanal de indicadores) | La plantilla de reporte incluye métricas de paid media para integrar al tablero |
| BL-021 (Medir ventas con su origen) | El plan de tracking explica cómo capturar el origen desde el anuncio hasta la venta |
| BL-047 (Plantilla única para registrar ventas) | Se especifican las columnas necesarias para atribución |
| BL-058 (Permiso de datos) | El plan menciona la dependencia de tener permiso antes de rastrear |

---

## Qué NO incluye este aporte

- **Creativos de anuncios:** están en los embudos E03 y E04.
- **Estrategia de campaña:** depende de decisiones de negocio (BL-044: hipótesis antes de experimentar).
- **Presupuesto:** se marca como `[[por definir]]` porque es desconocido.
- **Benchmarks o metas numéricas:** no se inventan cifras; los umbrales se definen con datos reales.
- **Análisis del competidor Friskies BR:** no se pudo obtener contenido público del perfil de Instagram para hacer observaciones útiles.

---

## Prerequisitos para usar este aporte

1. **BL-021 cumplido:** más del 80 % de las ventas del mes con origen registrado.
2. **BL-047 implementado:** plantilla de ventas con columnas de origen.
3. **BL-058 resuelto:** permiso de datos para rastrear usuarios.
4. **Acceso a Business Manager de Meta:** para crear el Pixel y la cuenta publicitaria.
5. **Presupuesto acordado:** para definir los umbrales de gasto.

---

## Hechos vs. hipótesis

Este aporte sigue la regla del repositorio de separar hechos de supuestos.

### Hechos (con fuente)

| Hecho | Fuente |
|-------|--------|
| WhatsApp es el canal principal de venta | `CANIVOROS-REFERENCIA-EMPRESA.md`, `develop` |
| Los embudos E03 y E04 están diseñados para Meta Ads | `embudos/EMBUDOS.md`, `develop` |
| BL-021 exige 80 % de ventas con origen para cobrar porcentaje | `backlog/BL-002-…md`, `develop` |
| Precios, costos y presupuesto son desconocidos | `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, `develop` |

### Hipótesis (a validar)

- Se usará Meta Ads como plataforma principal.
- El sitio WordPress puede recibir el Pixel.
- El equipo puede modificar el botón de WhatsApp para incluir código de atribución.
- Habrá suficiente volumen de conversiones para aplicar los pisos silenciosos.

---

## Cómo usar este aporte

1. **Leer** el plan maestro (`PLAN-MEDICION-PAID-MEDIA.md`) para entender el enfoque.
2. **Completar el checklist** del plan antes de activar campañas.
3. **Usar la plantilla** de reporte semanal cada semana de campaña activa.
4. **Ajustar los umbrales** de alerta después de 2–4 semanas de datos reales.
5. **Registrar los aprendizajes** en la sección correspondiente del reporte.

---

## Próximos pasos sugeridos

1. Revisar si el sitio WordPress tiene Tag Manager o permite insertar código en el `<head>`.
2. Verificar acceso al Business Manager de Meta.
3. Definir presupuesto de prueba inicial con Andrés.
4. Implementar el Pixel y el evento `ClickToWhatsApp`.
5. Ejecutar la primera campaña de E04 con la estructura de $30/día × 8 días.
6. Generar el primer reporte semanal.

---

## Contacto

Este aporte fue generado por un agente de IA especializado en paid media measurement. Para dudas o ajustes, contactar a Andrés.
