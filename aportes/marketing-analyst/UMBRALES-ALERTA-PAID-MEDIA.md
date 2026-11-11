# Umbrales de alerta para paid media · Canívoros

> Complemento de [PLAN-MEDICION-PAID-MEDIA.md](PLAN-MEDICION-PAID-MEDIA.md)

Las alertas indican cuándo revisar una campaña. Incluyen un **piso silencioso** para evitar reaccionar con datos insuficientes.

---

## Estructura de cada alerta

| Campo | Descripción |
|-------|-------------|
| **Alcance** | Qué nivel de la cuenta afecta (cuenta, campaña, conjunto, anuncio) |
| **Métrica** | Qué se mide |
| **Dirección** | `>` (mayor que) o `<` (menor que) |
| **Límite** | Valor umbral |
| **Ventana** | Período de tiempo para evaluar |
| **Severidad** | `info`, `advertencia`, `crítico` |
| **Piso silencioso** | Volumen mínimo para que la alerta aplique |

---

## Alertas propuestas

### A1. CTR muy bajo (anuncio no relevante)

| Campo | Valor |
|-------|-------|
| Alcance | Anuncio |
| Métrica | CTR (enlace) |
| Dirección | < |
| Límite | `[[por definir con datos reales]]` % |
| Ventana | Últimos 4 días |
| Severidad | advertencia |
| Piso silencioso | ≥ 1.000 impresiones |

**Acción sugerida:** Revisar creative y copy. Pausar si no mejora en 2 días adicionales.

**Nota:** El límite depende del tipo de campaña y audiencia. En E04 se mencionan rangos de CPV y CPF para B2C (líneas 329–331), pero no CTR. Iniciar con observación y ajustar tras las primeras semanas.

---

### A2. CPC muy alto (competencia o segmentación amplia)

| Campo | Valor |
|-------|-------|
| Alcance | Conjunto de anuncios |
| Métrica | CPC (enlace) |
| Dirección | > |
| Límite | `[[por definir]]` COP |
| Ventana | Últimos 4 días |
| Severidad | advertencia |
| Piso silencioso | ≥ 100 clics al enlace |

**Acción sugerida:** Revisar segmentación. Comparar con otros conjuntos. Considerar reducir audiencia o cambiar ubicaciones.

---

### A3. Tasa sitio→WhatsApp muy baja (problema en landing page)

| Campo | Valor |
|-------|-------|
| Alcance | Campaña |
| Métrica | Clics WhatsApp / Clics enlace |
| Dirección | < |
| Límite | `[[por definir]]` % |
| Ventana | Últimos 7 días |
| Severidad | advertencia |
| Piso silencioso | ≥ 200 clics al enlace |

**Acción sugerida:** Revisar la página de destino. ¿El botón de WhatsApp es visible? ¿La propuesta es clara?

---

### A4. CPL muy alto (leads caros)

| Campo | Valor |
|-------|-------|
| Alcance | Campaña |
| Métrica | Costo por lead (clic WhatsApp atribuido) |
| Dirección | > |
| Límite | `[[por definir]]` COP |
| Ventana | Últimos 7 días |
| Severidad | advertencia |
| Piso silencioso | ≥ 20 leads registrados |

**Acción sugerida:** Revisar todo el embudo. ¿El problema está en el anuncio, la landing o el mensaje de WhatsApp?

---

### A5. Tasa de cierre muy baja (leads no calificados)

| Campo | Valor |
|-------|-------|
| Alcance | Campaña |
| Métrica | Ventas / Leads |
| Dirección | < |
| Límite | `[[por definir]]` % |
| Ventana | Últimos 14 días |
| Severidad | advertencia |
| Piso silencioso | ≥ 30 leads registrados Y ≥ 14 días desde el primer lead |

**Acción sugerida:** Revisar calidad de leads. ¿La segmentación atrae al ICP correcto? ¿El equipo responde a tiempo?

**Nota:** La ventana de 14 días permite que los leads tengan tiempo de convertir (el ciclo de compra de alimento puede ser de días a semanas).

---

### A6. CPA supera contribución (cada venta pierde dinero)

| Campo | Valor |
|-------|-------|
| Alcance | Campaña |
| Métrica | Costo por venta |
| Dirección | > |
| Límite | `[[contribución promedio por venta, desconocido]]` COP |
| Ventana | Últimos 14 días |
| Severidad | crítico |
| Piso silencioso | ≥ 5 ventas atribuidas |

**Acción sugerida:** Pausar campaña y analizar. ¿El CPA bajará con optimización o el canal no es viable para este producto?

**Nota:** Requiere conocer la contribución por venta (BL-025: costo y rentabilidad por producto). Mientras sea `desconocido`, esta alerta no puede activarse.

---

### A7. Frecuencia alta (fatiga de audiencia)

| Campo | Valor |
|-------|-------|
| Alcance | Conjunto de anuncios |
| Métrica | Frecuencia |
| Dirección | > |
| Límite | 3,0 |
| Ventana | Últimos 7 días |
| Severidad | info |
| Piso silencioso | ≥ 5.000 impresiones |

**Acción sugerida:** Ampliar audiencia o rotar creativos. Observar si CTR empieza a bajar.

---

### A8. Gasto diario excede presupuesto

| Campo | Valor |
|-------|-------|
| Alcance | Cuenta |
| Métrica | Gasto diario |
| Dirección | > |
| Límite | `[[presupuesto diario acordado, desconocido]]` COP |
| Ventana | Día actual |
| Severidad | crítico |
| Piso silencioso | Ninguno (aplica siempre) |

**Acción sugerida:** Revisar configuración de presupuesto en Ads Manager. Si es intencional, actualizar el límite.

---

## Tabla resumen

| ID | Métrica | Dirección | Límite | Piso silencioso | Severidad |
|----|---------|-----------|--------|-----------------|-----------|
| A1 | CTR enlace | < | `[[por definir]]` % | ≥ 1.000 impr | advertencia |
| A2 | CPC enlace | > | `[[por definir]]` COP | ≥ 100 clics | advertencia |
| A3 | Tasa sitio→WA | < | `[[por definir]]` % | ≥ 200 clics | advertencia |
| A4 | CPL | > | `[[por definir]]` COP | ≥ 20 leads | advertencia |
| A5 | Tasa de cierre | < | `[[por definir]]` % | ≥ 30 leads, ≥ 14 d | advertencia |
| A6 | CPA | > | `[[contribución]]` COP | ≥ 5 ventas | crítico |
| A7 | Frecuencia | > | 3,0 | ≥ 5.000 impr | info |
| A8 | Gasto diario | > | `[[presupuesto]]` COP | Ninguno | crítico |

---

## Por qué los pisos silenciosos

Con pocas observaciones, las métricas fluctúan mucho. Ejemplos:

- Con 50 impresiones y 0 clics, el CTR es 0 %, pero no significa que el anuncio sea malo; simplemente no hay datos.
- Con 3 leads y 0 ventas, la tasa de cierre es 0 %, pero puede ser que los 3 leads aún estén en proceso.

Los pisos evitan falsos negativos y permiten que el algoritmo de Meta tenga tiempo de optimizar (generalmente 3–7 días para salir de la fase de aprendizaje).

---

## Cómo definir los límites

Los límites marcados como `[[por definir]]` deben establecerse con datos reales después de:

1. **Primeras 2–4 semanas de campaña:** observar el rango natural de cada métrica.
2. **Referencia del video E04:** para campañas de tráfico a perfil, el video menciona rangos de CPV y CPF (líneas 329–331), pero son de otro mercado (B2B/B2C en USD). No copiar directamente.
3. **Acuerdo con Andrés:** el límite de CPA depende de la contribución por venta, que a su vez depende de BL-025.

**Regla:** no fijar un límite sin haber observado al menos 2 semanas de datos. Mejor empezar sin alertas automáticas y revisar manualmente.

---

## Implementación de alertas

### Opción 1: Manual (recomendada al inicio)

Revisar Ads Manager cada 2–3 días y comparar con la tabla. Registrar en el reporte semanal.

### Opción 2: Reglas automatizadas en Meta

Meta Ads permite crear reglas que pausan o notifican automáticamente. Configurar después de tener límites definidos.

Ejemplo de regla en Ads Manager:  
- Condición: `CPC (enlace) > X COP` Y `Clics en el enlace > 100`  
- Acción: Enviar notificación por email

### Opción 3: Herramienta externa

Si se usa una herramienta de reporting (Supermetrics, Funnel, etc.), configurar alertas ahí. Requiere inversión adicional.

---

## Fuentes

- `embudos/E04-…/embudo.md` (líneas 326–331): rangos de CPV y CPF del video
- `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` (línea 172): umbrales operativos propuestos (entrega puntual, pedidos completos)
- Documentación de Meta Ads: [Reglas automatizadas](https://www.facebook.com/business/help/1559687257653168)
