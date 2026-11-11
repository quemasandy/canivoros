# Plan de medición para paid media · Canívoros

> **Especialidad:** Paid Media Reporting & Measurement  
> **Fecha:** 2026-11-11  
> **Estado:** Borrador para revisión de Andrés  
> **Prerequisitos:** BL-021 (más del 80 % de ventas con origen registrado), BL-047 (plantilla de ventas), BL-058 (permiso de datos)

Este documento complementa el plan de crecimiento de Bogotá (`CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`) y los embudos E03/E04 con la infraestructura técnica de medición necesaria antes de invertir en anuncios pagados.

---

## Índice

1. [Contexto y dependencias](#1-contexto-y-dependencias)
2. [Plan de tracking por canal](#2-plan-de-tracking-por-canal)
3. [Convención de UTMs](#3-convención-de-utms)
4. [Atribución de WhatsApp click-to-chat](#4-atribución-de-whatsapp-click-to-chat)
5. [Árbol de KPIs y fórmulas](#5-árbol-de-kpis-y-fórmulas)
6. [Umbrales de alerta con piso silencioso](#6-umbrales-de-alerta-con-piso-silencioso)
7. [Plantilla de reporte semanal](#7-plantilla-de-reporte-semanal)
8. [Checklist pre-lanzamiento](#8-checklist-pre-lanzamiento)
9. [Fuentes](#9-fuentes)

---

## 1. Contexto y dependencias

### Hechos (del repositorio)

| Hecho | Fuente |
|-------|--------|
| Canal principal de venta: WhatsApp | `CANIVOROS-REFERENCIA-EMPRESA.md` (línea ~190), `develop` |
| También vende por distribuidores y tiendas aliadas | `CANIVOROS-REFERENCIA-EMPRESA.md` (línea ~93), `develop` |
| Sitio web: https://canivoros.com | `CANIVOROS-REFERENCIA-EMPRESA.md` (línea ~220), `develop` |
| Instagram: @canivoros_col | `CANIVOROS-REFERENCIA-EMPRESA.md` (línea ~222), `develop` |
| Número WhatsApp enlazado desde el sitio: +57 324 460 8114 | `CANIVOROS-REFERENCIA-EMPRESA.md` (línea ~210), `develop` |
| Embudos E03 y E04 diseñados para Meta Ads, sin métricas reales | `embudos/EMBUDOS.md`, `develop` |
| BL-021 exige 80 % de ventas con origen antes de cobrar porcentaje | `backlog/BL-002-…md` (línea ~8), `develop` |
| Precios, costos y márgenes: desconocido | `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` (línea ~17), `develop` |
| Presupuesto de inversión publicitaria: desconocido | `embudos/E04-…/embudo.md` (línea ~15), `develop` |

### Hipótesis (a validar)

- Se usará Meta Ads como plataforma principal de paid media (basado en E03, E04).
- El sitio WordPress puede recibir el Pixel de Meta.
- El equipo tiene acceso a un Business Manager de Meta.
- El CRM o la plantilla de ventas (BL-047) permitirá registrar el origen de cada contacto.

### Dependencias del backlog

| Tarea | Por qué bloquea |
|-------|-----------------|
| BL-021 | Sin origen registrado no hay atribución |
| BL-047 | La plantilla debe incluir campos de campaña, medio, fuente |
| BL-058 | Sin permiso de datos no se puede rastrear usuarios |
| BL-005 | Sin precios confirmados no se calcula ROAS en COP |

---

## 2. Plan de tracking por canal

### 2.1 Meta Ads (Facebook / Instagram)

#### Pixel de Meta

| Paso | Descripción | Responsable propuesto |
|------|-------------|-----------------------|
| 1 | Crear Pixel en el Business Manager | `[[por definir]]` |
| 2 | Instalar código base en `<head>` del sitio WordPress | `[[por definir]]` |
| 3 | Configurar evento `PageView` automático | Se dispara al cargar el Pixel |
| 4 | Crear evento personalizado `ClickToWhatsApp` (ver sección 4) | `[[por definir]]` |

#### Conversions API (CAPI)

La Conversions API envía eventos del servidor, evitando pérdidas por bloqueadores de anuncios. Requiere desarrollo.

| Evento | Cuándo enviarlo | Método |
|--------|-----------------|--------|
| `Lead` | Al registrar una consulta calificada en la plantilla de ventas | Backend o Zapier/Make desde la plantilla |
| `Purchase` | Al registrar una venta cerrada | Backend o Zapier/Make desde la plantilla |

**Deduplicación:** usar un `event_id` único por evento (UUID o timestamp+cliente) para evitar contar dos veces un mismo evento reportado por Pixel y CAPI.

### 2.2 Google Analytics 4 (opcional)

Si se decide usar GA4 para una visión independiente de Meta:

| Paso | Descripción |
|------|-------------|
| 1 | Crear propiedad GA4 y Data Stream para canivoros.com |
| 2 | Instalar gtag.js o Google Tag Manager |
| 3 | Configurar evento `click_to_whatsapp` con parámetros de UTM |
| 4 | Crear conversión en GA4 para `click_to_whatsapp` |

**Nota:** GA4 no reemplaza el Pixel de Meta para optimizar campañas; sirve como fuente de verdad independiente.

---

## 3. Convención de UTMs

Los parámetros UTM permiten identificar el origen de cada visita y conectarlo con la venta posterior.

### Estructura propuesta

```
?utm_source={plataforma}&utm_medium={tipo}&utm_campaign={nombre_campaña}&utm_content={variante}&utm_term={palabra_o_interes}
```

### Valores estándar

| Parámetro | Valores permitidos | Ejemplo |
|-----------|--------------------| --------|
| `utm_source` | `facebook`, `instagram`, `google`, `whatsapp_status`, `email`, `distribuidor`, `organico` | `facebook` |
| `utm_medium` | `cpc`, `cpm`, `social`, `email`, `referral`, `organic` | `cpc` |
| `utm_campaign` | Nombre descriptivo en snake_case: `{objetivo}_{segmento}_{fecha_inicio}` | `trafico_bogota_abierta_2026-11` |
| `utm_content` | Variante del anuncio: `video_1`, `carrusel_a`, `story_cerdo` | `video_horneado_30s` |
| `utm_term` | Interés o palabra clave (solo si aplica) | `alimento_natural` |

### Ejemplo de URL completa

```
https://canivoros.com/?utm_source=facebook&utm_medium=cpc&utm_campaign=trafico_bogota_abierta_2026-11&utm_content=video_horneado_30s
```

### Reglas

1. **No inventar valores:** usar solo los de la lista o agregarlos al catálogo antes de usarlos.
2. **Registrar en la plantilla de ventas:** cuando el cliente contacte por WhatsApp, preguntar cómo conoció la marca y registrar la campaña si es identificable, o marcar `utm_source=desconocido`.
3. **Minúsculas y sin espacios:** evita duplicados por variación de mayúsculas.

---

## 4. Atribución de WhatsApp click-to-chat

El flujo de Canívoros es:  
`Anuncio → Sitio web → Clic en botón WhatsApp → Conversación → Venta`

El reto es conectar el clic en el botón con la venta posterior.

### Método propuesto

1. **Interceptar clic en el botón de WhatsApp** en el sitio:
   - El enlace actual es `https://wa.me/573244608114`.
   - Agregar un listener de clic que:
     a. Dispare el evento `ClickToWhatsApp` al Pixel de Meta con los UTMs de la sesión.
     b. Envíe el evento a GA4 si se usa.
     c. Genere un código de atribución (ej. `WA-20261111-A1B2`) y lo agregue al mensaje predefinido de WhatsApp.

2. **Mensaje predefinido con código:**
   - URL modificada: `https://wa.me/573244608114?text=Hola,%20vi%20su%20anuncio%20[WA-20261111-A1B2].%20Quiero%20más%20información.`
   - El código permite buscar la sesión de origen si se guardan los eventos.

3. **Registro en la plantilla de ventas:**
   - Al recibir el mensaje, copiar el código a la columna `codigo_atribucion`.
   - Si no hay código, marcar `origen=desconocido`.

### Limitaciones

- Depende de que el usuario use el botón del sitio; si escribe directo al número, no hay código.
- Requiere modificar el sitio (BL-042 propone revisar el WordPress).
- El código no garantiza la venta; solo conecta la conversación con la sesión de anuncio.

---

## 5. Árbol de KPIs y fórmulas

Ver archivo separado: [ARBOL-KPI-PAID-MEDIA.md](ARBOL-KPI-PAID-MEDIA.md)

Resumen de métricas de la plataforma (Meta Ads):

| Métrica | Fórmula / fuente | Unidad |
|---------|------------------|--------|
| Impresiones | Columna `impressions` de Meta | # |
| Alcance | Columna `reach` de Meta | # |
| Clics (todos) | Columna `clicks` de Meta | # |
| Clics al enlace | Columna `link_clicks` de Meta | # |
| CTR (enlace) | `link_clicks / impressions × 100` | % |
| CPC (enlace) | `spend / link_clicks` | COP |
| CPM | `spend / impressions × 1000` | COP |
| Conversiones | Columna `actions` filtrada por el evento de conversión configurado | # |
| Costo por conversión | `spend / conversions` | COP |
| Valor de conversión | Columna `action_value` si se envía valor | COP |
| ROAS | `action_value / spend` | × |

**Nota:** `spend` en Meta Ads está en la moneda de la cuenta (USD o COP). Confirmar moneda antes de calcular.

---

## 6. Umbrales de alerta con piso silencioso

Los umbrales definen cuándo revisar una campaña. El piso silencioso evita alertas con datos insuficientes.

Ver archivo separado: [UMBRALES-ALERTA-PAID-MEDIA.md](UMBRALES-ALERTA-PAID-MEDIA.md)

---

## 7. Plantilla de reporte semanal

Ver archivo separado: [PLANTILLA-REPORTE-SEMANAL.md](PLANTILLA-REPORTE-SEMANAL.md)

---

## 8. Checklist pre-lanzamiento

Antes de activar la primera campaña pagada, verificar:

### Infraestructura de tracking

- [ ] Pixel de Meta instalado y verificado con la extensión Meta Pixel Helper
- [ ] Evento `PageView` disparando en todas las páginas
- [ ] Evento `ClickToWhatsApp` configurado en el botón de WhatsApp
- [ ] (Opcional) CAPI conectado para eventos `Lead` y `Purchase`
- [ ] (Opcional) GA4 configurado con evento `click_to_whatsapp`
- [ ] UTMs definidos y documentados para la primera campaña
- [ ] Mensaje de WhatsApp con código de atribución funcionando

### Registro de ventas

- [ ] Plantilla de ventas (BL-047) con columnas: `fecha`, `cliente`, `producto`, `cantidad_kg`, `precio_cop`, `canal_cierre`, `origen_utm_source`, `origen_utm_campaign`, `codigo_atribucion`
- [ ] Más del 80 % de ventas del mes anterior con origen registrado (criterio de BL-021)
- [ ] Responsable asignado para registrar cada venta con su origen

### Configuración de cuenta

- [ ] Business Manager de Meta con acceso del equipo
- [ ] Cuenta publicitaria creada y con método de pago
- [ ] Página de Facebook e Instagram conectadas
- [ ] Pixel asignado a la cuenta publicitaria
- [ ] Audiencias personalizadas configuradas (si aplica para E04 Lookalike)

### Presupuesto y metas

- [ ] Presupuesto diario acordado con Andrés (actualmente `desconocido`)
- [ ] Meta de CPL o CPA definida (actualmente `desconocido`)
- [ ] Límite de gasto para prueba inicial (sugerido en E04: 8 días a `[[presupuesto]]`)

---

## 9. Fuentes

| Documento | Rama | Uso en este plan |
|-----------|------|------------------|
| `CANIVOROS-REFERENCIA-EMPRESA.md` | `develop` | Canales de venta, contacto, presencia digital |
| `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` | `develop` | KPIs de negocio, tablero para tomar decisiones |
| `embudos/EMBUDOS.md` | `develop` | Estado de E03 y E04 |
| `embudos/E03-…/embudo.md` | `develop` | Embudo de adquisición con Meta Ads |
| `embudos/E04-…/embudo.md` | `develop` | Estructuras de campaña y KPIs del video |
| `backlog/BL-002-…md` | `develop` | Criterio de 80 % de ventas con origen |
| `backlog/BL-021-…md` | `develop` | Tarea de medir ventas con origen |
| `backlog/BL-047-…md` | `develop` | Plantilla única de ventas |
| `.claude/skills/embudos-de-venta/references/metricas.md` | `develop` | Métricas de embudo |

---

**Siguiente paso:** completar los archivos `ARBOL-KPI-PAID-MEDIA.md`, `UMBRALES-ALERTA-PAID-MEDIA.md` y `PLANTILLA-REPORTE-SEMANAL.md` con el detalle necesario.
