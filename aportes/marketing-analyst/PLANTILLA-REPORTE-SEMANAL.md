# Plantilla de reporte semanal de paid media · Canívoros

> Complemento de [PLAN-MEDICION-PAID-MEDIA.md](PLAN-MEDICION-PAID-MEDIA.md)

Este reporte se genera cada semana (sugerido: lunes) para revisar el desempeño de las campañas de Meta Ads.

---

## Encabezado

| Campo | Valor |
|-------|-------|
| **Semana** | `[[AAAA-WNN]]` (ej. 2026-W46) |
| **Período** | `[[fecha inicio]]` a `[[fecha fin]]` |
| **Responsable del reporte** | `[[nombre]]` |
| **Campañas activas** | `[[lista de campañas]]` |
| **Presupuesto semanal acordado** | `[[monto]]` COP |

---

## 1. Resumen ejecutivo

> Sección para llenado manual: 2–3 oraciones sobre lo más relevante de la semana.

- **Lo que funcionó:**  
  `[[descripción breve]]`

- **Lo que no funcionó:**  
  `[[descripción breve]]`

- **Decisión principal para la próxima semana:**  
  `[[acción concreta]]`

---

## 2. Métricas de plataforma (Meta Ads)

### 2.1 Tabla de resultados por campaña

| Campaña | Gasto (COP) | Impresiones | Alcance | Clics enlace | CTR (%) | CPC (COP) | Clics WA |
|---------|-------------|-------------|---------|--------------|---------|-----------|----------|
| `[[campaña 1]]` | | | | | | | |
| `[[campaña 2]]` | | | | | | | |
| **Total** | | | | | | | |

### 2.2 Fórmulas para calcular

| Métrica | Fórmula |
|---------|---------|
| CTR (%) | `clics_enlace / impresiones × 100` |
| CPC (COP) | `gasto / clics_enlace` |
| CPM (COP) | `gasto / impresiones × 1000` |
| Frecuencia | `impresiones / alcance` |

### 2.3 Variación vs. semana anterior

| Métrica | Semana anterior | Esta semana | Variación (%) |
|---------|-----------------|-------------|---------------|
| Gasto | | | |
| Impresiones | | | |
| Clics enlace | | | |
| CTR | | | |
| CPC | | | |

**Fórmula de variación:** `(esta_semana - semana_anterior) / semana_anterior × 100`

---

## 3. Métricas de conversión

### 3.1 Embudo de la semana

| Etapa | # | Tasa vs. etapa anterior (%) |
|-------|---|----------------------------|
| Clics al enlace | `[[dato de Meta]]` | — |
| Visitas a la página | `[[dato de GA4 o Pixel PageView]]` | `visitas / clics × 100` |
| Clics a WhatsApp | `[[dato del evento ClickToWhatsApp]]` | `clics_wa / visitas × 100` |
| Leads registrados | `[[conteo de plantilla con código]]` | `leads / clics_wa × 100` |
| Ventas atribuidas | `[[conteo de plantilla con origen campaña]]` | `ventas / leads × 100` |

### 3.2 Costos por etapa

| Métrica | Valor (COP) | Fórmula |
|---------|-------------|---------|
| CPC (enlace) | | `gasto / clics_enlace` |
| Costo por clic WhatsApp | | `gasto / clics_wa` |
| CPL | | `gasto / leads` |
| CPA (costo por venta) | | `gasto / ventas` |

### 3.3 Retorno

| Métrica | Valor | Fórmula |
|---------|-------|---------|
| Ingresos atribuidos (COP) | `[[suma de ventas × precio]]` | Desde plantilla de ventas |
| ROAS | | `ingresos / gasto` |
| Contribución bruta (COP) | | `ingresos - gasto` |

---

## 4. Alertas activadas

Revisar la tabla de [UMBRALES-ALERTA-PAID-MEDIA.md](UMBRALES-ALERTA-PAID-MEDIA.md) y marcar las que aplican:

| ID | Alerta | ¿Aplica? | Detalle |
|----|--------|----------|---------|
| A1 | CTR bajo | ☐ Sí / ☐ No | |
| A2 | CPC alto | ☐ Sí / ☐ No | |
| A3 | Tasa sitio→WA baja | ☐ Sí / ☐ No | |
| A4 | CPL alto | ☐ Sí / ☐ No | |
| A5 | Tasa de cierre baja | ☐ Sí / ☐ No | |
| A6 | CPA > contribución | ☐ Sí / ☐ No | |
| A7 | Frecuencia alta | ☐ Sí / ☐ No | |
| A8 | Gasto > presupuesto | ☐ Sí / ☐ No | |

---

## 5. Desglose por anuncio (opcional)

Si hay varios anuncios activos, listar los 3 mejores y los 3 peores por CTR o CPC:

### Mejores anuncios

| Anuncio | Campaña | CTR (%) | CPC (COP) | Clics WA |
|---------|---------|---------|-----------|----------|
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |

### Peores anuncios (candidatos a pausar)

| Anuncio | Campaña | CTR (%) | CPC (COP) | Clics WA |
|---------|---------|---------|-----------|----------|
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |

---

## 6. Aprendizajes de la semana

> Sección para documentar observaciones cualitativas.

- **Sobre la audiencia:**  
  `[[qué aprendimos sobre quién responde a los anuncios]]`

- **Sobre el mensaje:**  
  `[[qué copy o creative funcionó mejor]]`

- **Sobre el producto:**  
  `[[qué preguntas hacen los leads, qué objeciones tienen]]`

- **Sobre el proceso:**  
  `[[qué mejorar en el registro, la atención, el seguimiento]]`

---

## 7. Plan para la próxima semana

| Acción | Responsable | Fecha límite |
|--------|-------------|--------------|
| `[[acción 1]]` | `[[nombre]]` | `[[fecha]]` |
| `[[acción 2]]` | `[[nombre]]` | `[[fecha]]` |
| `[[acción 3]]` | `[[nombre]]` | `[[fecha]]` |

---

## 8. Datos faltantes

Listar qué información no se pudo obtener y por qué:

| Dato | Motivo | Impacto |
|------|--------|---------|
| `[[ej. Clics WhatsApp]]` | `[[ej. Evento no configurado]]` | `[[ej. No se puede calcular CPL real]]` |

---

## Instrucciones de llenado

### Fuentes de datos

| Sección | Fuente |
|---------|--------|
| Métricas de plataforma | Exportar de Ads Manager → Campañas → Columnas: Impresiones, Alcance, Clics en el enlace, CPC, CTR, Importe gastado |
| Clics WhatsApp | Events Manager (evento `ClickToWhatsApp`) o GA4 |
| Leads y ventas | Plantilla de ventas (BL-047), filtrar por `origen_utm_campaign` |
| Ingresos | Plantilla de ventas, sumar `precio_cop × cantidad_kg` para ventas atribuidas |

### Periodicidad

- **Generación:** cada lunes, cubriendo lunes a domingo de la semana anterior.
- **Revisión:** en la reunión semanal (BL-003).
- **Archivo:** guardar cada reporte en `aportes/marketing-analyst/reportes/AAAA-WNN.md` o en una carpeta de Drive/Notion acordada.

### Antes del primer reporte

1. Confirmar que el Pixel y el evento `ClickToWhatsApp` están funcionando.
2. Confirmar que la plantilla de ventas tiene las columnas de origen.
3. Definir el presupuesto semanal con Andrés.
4. Ejecutar al menos 1 semana completa de campaña.

---

## Ejemplo de reporte completado

> **Nota:** Los números son ficticios y solo ilustran el formato. No usar como referencia de resultados esperados.

```markdown
# Reporte semanal de paid media · Canívoros

| Campo | Valor |
|-------|-------|
| **Semana** | 2026-W47 |
| **Período** | 18 nov a 24 nov 2026 |
| **Responsable del reporte** | [[nombre]] |
| **Campañas activas** | trafico_bogota_abierta_2026-11 |
| **Presupuesto semanal acordado** | [[por definir]] COP |

## 1. Resumen ejecutivo

- **Lo que funcionó:** El video de 30s sobre el horneado tuvo el mejor CTR.
- **Lo que no funcionó:** El carrusel de productos no generó clics al enlace.
- **Decisión principal:** Pausar el carrusel y duplicar presupuesto del video ganador.

## 2. Métricas de plataforma

| Campaña | Gasto | Impr | Alcance | Clics | CTR | CPC | Clics WA |
|---------|-------|------|---------|-------|-----|-----|----------|
| trafico_bogota_abierta | [[dato]] | [[dato]] | [[dato]] | [[dato]] | [[dato]] | [[dato]] | [[dato]] |

(...)
```

---

## Fuentes

- `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` (línea 165): revisión semanal
- `backlog/BL-003-…md`: crear tablero semanal
- `backlog/BL-013-…md`: tablero semanal de indicadores
- `.claude/skills/embudos-de-venta/references/metricas.md` (línea 64): tablero semanal de embudos
