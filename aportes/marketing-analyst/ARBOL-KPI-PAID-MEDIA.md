# Árbol de KPIs para paid media · Canívoros

> Complemento de [PLAN-MEDICION-PAID-MEDIA.md](PLAN-MEDICION-PAID-MEDIA.md)

Este árbol organiza las métricas de paid media en niveles: desde el gasto hasta el resultado de negocio. Cada métrica incluye su fórmula exacta y la fuente de datos.

---

## Niveles del árbol

```
                            ┌─────────────────────┐
                            │   ROAS (retorno)    │
                            │  action_value/spend │
                            └──────────┬──────────┘
                                       │
              ┌────────────────────────┴────────────────────────┐
              │                                                  │
    ┌─────────▼─────────┐                          ┌────────────▼────────────┐
    │  Ingresos (COP)   │                          │   Gasto total (COP)     │
    │  ventas atribuidas │                          │   spend en Meta Ads     │
    └─────────┬─────────┘                          └────────────┬────────────┘
              │                                                  │
    ┌─────────▼─────────┐                          ┌────────────▼────────────┐
    │  # Ventas         │                          │   Costo por venta       │
    │  Purchase events  │                          │   spend / ventas        │
    └─────────┬─────────┘                          └─────────────────────────┘
              │
    ┌─────────▼─────────┐
    │  Tasa de cierre   │
    │  ventas/leads     │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐                          ┌─────────────────────────┐
    │  # Leads          │                          │   CPL (costo por lead)  │
    │  clics WhatsApp   │◄─────────────────────────│   spend / leads         │
    └─────────┬─────────┘                          └─────────────────────────┘
              │
    ┌─────────▼─────────┐                          ┌─────────────────────────┐
    │  # Clics enlace   │                          │   CPC (costo por clic)  │
    │  link_clicks      │◄─────────────────────────│   spend / link_clicks   │
    └─────────┬─────────┘                          └─────────────────────────┘
              │
    ┌─────────▼─────────┐
    │  CTR enlace       │
    │  link_clicks/impr │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐                          ┌─────────────────────────┐
    │  # Impresiones    │                          │   CPM                   │
    │  impressions      │◄─────────────────────────│   spend/impr × 1000     │
    └─────────┬─────────┘                          └─────────────────────────┘
              │
    ┌─────────▼─────────┐
    │  # Alcance        │
    │  reach (personas) │
    └─────────┬─────────┘
              │
    ┌─────────▼─────────┐
    │  Frecuencia       │
    │  impressions/reach│
    └─────────────────────┘
```

---

## Tabla de métricas con fórmulas

### Nivel 1: Exposición

| Métrica | Definición | Fórmula | Fuente de datos |
|---------|------------|---------|-----------------|
| **Impresiones** | Número de veces que se mostró el anuncio | `impressions` (columna de Meta) | Ads Manager |
| **Alcance** | Número de personas únicas que vieron el anuncio | `reach` (columna de Meta) | Ads Manager |
| **Frecuencia** | Promedio de veces que cada persona vio el anuncio | `impressions / reach` | Calculado |
| **CPM** | Costo por cada mil impresiones | `spend / impressions × 1000` | Calculado (COP) |

### Nivel 2: Interacción

| Métrica | Definición | Fórmula | Fuente de datos |
|---------|------------|---------|-----------------|
| **Clics (todos)** | Clics en cualquier parte del anuncio | `clicks` (columna de Meta) | Ads Manager |
| **Clics al enlace** | Clics que llevan al destino (sitio web) | `link_clicks` (columna de Meta) | Ads Manager |
| **CTR (enlace)** | Tasa de clics al enlace sobre impresiones | `link_clicks / impressions × 100` | Calculado (%) |
| **CPC (enlace)** | Costo por cada clic al enlace | `spend / link_clicks` | Calculado (COP) |

### Nivel 3: Conversión (evento ClickToWhatsApp)

| Métrica | Definición | Fórmula | Fuente de datos |
|---------|------------|---------|-----------------|
| **Clics a WhatsApp** | Clics en el botón de WhatsApp del sitio | Evento `ClickToWhatsApp` en el Pixel | Events Manager o GA4 |
| **Tasa sitio→WhatsApp** | % de visitantes que hacen clic en WhatsApp | `clics_whatsapp / link_clicks × 100` | Calculado (%) |
| **Costo por clic WhatsApp** | Costo de cada clic al botón WhatsApp | `spend / clics_whatsapp` | Calculado (COP) |

### Nivel 4: Conversión (Lead calificado)

| Métrica | Definición | Fórmula | Fuente de datos |
|---------|------------|---------|-----------------|
| **Leads** | Conversaciones de WhatsApp iniciadas con código de atribución | Conteo en plantilla de ventas donde `codigo_atribucion` ≠ vacío | Plantilla BL-047 |
| **CPL** | Costo por lead (conversación atribuida) | `spend / leads` | Calculado (COP) |
| **Tasa WhatsApp→Lead** | % de clics WhatsApp que generan conversación registrada | `leads / clics_whatsapp × 100` | Calculado (%) |

### Nivel 5: Venta

| Métrica | Definición | Fórmula | Fuente de datos |
|---------|------------|---------|-----------------|
| **Ventas atribuidas** | Ventas con origen confirmado de la campaña | Conteo en plantilla donde `origen_utm_campaign` = campaña | Plantilla BL-047 |
| **Ingresos atribuidos** | Suma de `precio_cop × cantidad_kg` de ventas atribuidas | `SUM(precio_cop)` filtrado | Plantilla BL-047 |
| **Tasa de cierre** | % de leads que se convierten en venta | `ventas / leads × 100` | Calculado (%) |
| **Costo por venta (CPA)** | Gasto dividido entre ventas atribuidas | `spend / ventas` | Calculado (COP) |
| **Ticket promedio** | Ingreso promedio por venta | `ingresos / ventas` | Calculado (COP) |

### Nivel 6: Retorno

| Métrica | Definición | Fórmula | Fuente de datos |
|---------|------------|---------|-----------------|
| **ROAS** | Retorno sobre la inversión publicitaria | `ingresos_atribuidos / spend` | Calculado (×) |
| **Contribución bruta** | Ingresos menos gasto publicitario | `ingresos - spend` | Calculado (COP) |

---

## Notas sobre la fuente de datos

### Columnas de Meta Ads Manager

Al exportar o consultar la API de Meta Ads, las columnas relevantes son:

| Columna API | Nombre en Ads Manager (ES) |
|-------------|---------------------------|
| `impressions` | Impresiones |
| `reach` | Alcance |
| `clicks` | Clics (todos) |
| `link_clicks` | Clics en el enlace |
| `spend` | Importe gastado |
| `cpc` | CPC (coste por clic en el enlace) |
| `cpm` | CPM (coste por 1.000 impresiones) |
| `ctr` | CTR (porcentaje de clics en el enlace) |
| `actions` | Acciones (desglosadas por tipo) |
| `action_values` | Valor de las acciones |

### Eventos personalizados

| Evento | Descripción | Cómo configurar |
|--------|-------------|-----------------|
| `ClickToWhatsApp` | Clic en el botón de WhatsApp | Script en el sitio que dispara `fbq('track', 'ClickToWhatsApp')` |
| `Lead` | Conversación calificada (enviado por CAPI) | Backend o automatización desde la plantilla |
| `Purchase` | Venta cerrada (enviado por CAPI) | Backend o automatización desde la plantilla |

---

## Métricas de la plataforma vs. métricas de negocio

| Tipo | Ejemplos | Fuente |
|------|----------|--------|
| **Plataforma** | Impresiones, clics, CTR, CPC, CPM | Ads Manager (automático) |
| **Híbridas** | Clics WhatsApp, CPL | Pixel + plantilla |
| **Negocio** | Ventas, ingresos, ROAS, tasa de cierre | Plantilla de ventas (manual) |

Las métricas de plataforma están disponibles en tiempo real. Las de negocio requieren que el equipo registre cada venta con su origen (BL-021).

---

## Relación con el tablero del plan Bogotá

El plan de crecimiento (`CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, línea 138) define indicadores de negocio. Este árbol los complementa con métricas específicas de paid media:

| Indicador del plan Bogotá | Métrica equivalente aquí | Diferencia |
|---------------------------|--------------------------|------------|
| CAC | Costo por venta (CPA) | CAC incluye todo el gasto de captación; CPA solo paid media |
| Conversión comercial | Tasa de cierre | Mismo concepto |
| Ventas netas | Ingresos atribuidos | Ventas netas incluye todos los canales; aquí solo atribuidos a ads |
| Contribución después de captación | Contribución bruta | Contribución del plan resta más costos |

---

## Ejemplo ilustrativo (no usar como meta)

> **Advertencia:** Los números de este ejemplo son ficticios y solo muestran cómo se calculan las métricas. No representan resultados esperados de Canívoros.

| Métrica | Valor ejemplo |
|---------|---------------|
| Gasto semanal | `[[por definir]]` COP |
| Impresiones | `[[por definir]]` |
| Clics enlace | `[[por definir]]` |
| Clics WhatsApp | `[[por definir]]` |
| Leads registrados | `[[por definir]]` |
| Ventas atribuidas | `[[por definir]]` |
| Ingresos | `[[por definir]]` COP |
| ROAS | `[[por definir]]` |

---

## Fuentes

- `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` (líneas 138–152), rama `develop`
- `.claude/skills/embudos-de-venta/references/metricas.md`, rama `develop`
- `embudos/E04-…/embudo.md` (KPIs del video, líneas 326–331), rama `develop`
- Documentación de Meta Ads: [Métricas de anuncios](https://www.facebook.com/business/help/447834205249495)
