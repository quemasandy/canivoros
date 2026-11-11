# Plan de prueba de canales de distribución — Canívoros

**Estado:** borrador · **Fecha:** 11 de noviembre de 2026 · **Aprobación:** pendiente de Andrés.

Este documento propone una secuencia de pruebas de canales de distribución para Canívoros, basada en el contenido del repositorio. Su objetivo es priorizar los experimentos existentes en el backlog según dependencias, riesgo y valor de aprendizaje, para facilitar decisiones de inversión.

---

## 1. Resumen ejecutivo

**Problema:** El backlog contiene múltiples experimentos de distribución (BL-012, BL-019, BL-020, BL-022, BL-060) pero no existe un orden de ejecución que considere las dependencias entre ellos ni las restricciones actuales (presupuesto, capacidad y datos base desconocidos).

**Propuesta:** Secuenciar los experimentos en tres fases según dependencias, empezando por aquellos que no requieren inversión publicitaria y que validan la capacidad de atención antes de generar más demanda.

**Fuentes consultadas:**
| Fuente | Rama/ruta | Fecha de acceso |
|---|---|---|
| CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md | master | 2026-11-11 |
| CANIVOROS-REFERENCIA-EMPRESA.md | master | 2026-11-11 |
| Backlog completo (BL-001 a BL-061) | origin/backlog | 2026-11-11 |
| Embudos E01–E04 | origin/develop (embudos/) | 2026-11-11 |
| BL-044 (criterios de decisión) | origin/backlog | 2026-11-11 |

**Referencia pública no accesible:** Instagram @canivoros_col y @friskiesbr — timeout al intentar acceder (2026-11-11). No se pudieron verificar métricas públicas de seguidores, frecuencia de publicación ni engagement.

---

## 2. Canales identificados en el repositorio

Canales de distribución mencionados en la documentación existente:

| Canal | Fuente en repo | Estado documentado |
|---|---|---|
| **WhatsApp directo** | REFERENCIA-EMPRESA (3 números publicados), BL-059 | Activo; auditoría de consultas pendiente |
| **Distribuidores/aliados** | REFERENCIA-EMPRESA (6 distribuidores listados), BL-035 | Activo; validación pendiente |
| **Tiendas mayoristas B2B** | BL-012 | Propuesto; no ejecutado |
| **Instagram/TikTok Omar** | BL-019 | Propuesto; no ejecutado |
| **Meta Ads (tráfico/conversión)** | E03, E04 | Frameworks clonados; no adaptados |
| **Recuperación de clientes inactivos** | BL-060, E02 | Propuesto; no ejecutado |
| **Reposición proactiva** | BL-022 | Propuesto; no ejecutado |

---

## 3. Restricciones actuales (según el repositorio)

Las siguientes restricciones están documentadas en el backlog y el plan de Bogotá:

| Restricción | Evidencia | Impacto |
|---|---|---|
| Presupuesto comercial desconocido | PLAN-CRECIMIENTO-BOGOTA §Datos pendientes | No se puede dimensionar inversión publicitaria |
| Precios y márgenes no confirmados | BL-005, BL-025 | No se puede calcular contribución por canal |
| Capacidad de producción desconocida | BL-036 | No se puede estimar demanda máxima atendible |
| Línea base de ventas pendiente | BL-004 | No se puede medir variación real |
| Tiempo de respuesta en WhatsApp no medido | BL-059 | No se sabe si el cuello de botella está en atención |
| Distribuidores publicados no validados | BL-035 | No se sabe cuántos están activos |

**Hipótesis implícita:** Antes de invertir en generar más demanda (ads, contenido), conviene validar que la capacidad de atención y entrega no es el cuello de botella actual.

---

## 4. Priorización de canales para prueba

Criterios de priorización (propuestos, no validados):

1. **Dependencias bloqueantes:** ¿Qué datos o sistemas se necesitan antes?
2. **Inversión requerida:** ¿Costo en dinero, tiempo o recursos?
3. **Reversibilidad:** ¿Se puede detener sin pérdida significativa?
4. **Valor de aprendizaje:** ¿Qué se aprende que desbloquee otros experimentos?

### Matriz de priorización (propuesta)

| Canal | Dependencias | Inversión | Reversibilidad | Aprendizaje | Prioridad sugerida |
|---|---|---|---|---|---|
| Auditoría WhatsApp (BL-059) | Ninguna | Tiempo | Alta | Alto (baseline atención) | **1 — Primero** |
| Validar distribuidores (BL-035) | Ninguna | Tiempo | Alta | Alto (canales activos) | **1 — Primero** |
| Recuperación inactivos (BL-060) | BL-004 (línea base) | Bajo | Alta | Medio (recompra) | **2 — Segundo** |
| Reposición proactiva (BL-022) | BL-004, BL-058 (permiso) | Bajo | Alta | Alto (retención) | **2 — Segundo** |
| Mayoristas B2B (BL-012) | BL-005 (precios), BL-035, BL-044 | Medio | Media | Alto (B2B vs B2C) | **3 — Después** |
| Omar personal brand (BL-019) | BL-011, BL-016, BL-051, BL-058, BL-059 | Medio | Media | Medio | **3 — Después** |
| Meta Ads (E03, E04) | Presupuesto, BL-016, landing | Alto | Baja (gasto) | Alto | **4 — Condicionado** |

---

## 5. Secuencia propuesta de experimentos

### Fase 0: Línea base (pre-requisito)

Antes de cualquier experimento de distribución, ejecutar:

| Tarea | Backlog | Entregable | Aprobación |
|---|---|---|---|
| Calcular ventas base | BL-004 | Kilos/semana, clientes activos, frecuencia | Andrés |
| Confirmar precios y márgenes | BL-005, BL-025 | Catálogo con precio y costo por SKU | Andrés |
| Auditar consultas WhatsApp | BL-059 | Tasa respuesta, tiempo, conversión actual | Andrés |
| Validar distribuidores activos | BL-035 | Lista actualizada con stock/pedidos recientes | Andrés |

**Criterio para avanzar a Fase 1:** Tener al menos BL-004 y BL-059 completados.

---

### Fase 1: Optimizar canales existentes (sin inversión publicitaria)

**Objetivo:** Mejorar conversión de la demanda actual antes de generar más.

| Experimento | Backlog | Hipótesis | Métrica principal | Criterio seguir/parar |
|---|---|---|---|---|
| Mejorar respuesta WhatsApp | BL-059 | Responder en <2h aumenta conversión | Conversión consulta→compra | Seguir si mejora >10% vs línea base |
| Reposición proactiva V1 | BL-022 | Recordatorio aumenta recompra | Recompra a 30 días | Seguir si recompra >20% de contactados |
| Recuperar inactivos | BL-060 | Clientes que dejaron de comprar vuelven con contacto | Reactivaciones | Seguir si ≥3 de 20 contactados compran |

**Gasto máximo propuesto:** Solo tiempo de personal; sin inversión en ads ni descuentos permanentes.

**Criterio para avanzar a Fase 2:** Al menos un experimento de Fase 1 con resultado positivo documentado.

---

### Fase 2: Expandir a canales nuevos de bajo costo

**Objetivo:** Probar canales que no requieren inversión publicitaria significativa.

| Experimento | Backlog | Hipótesis | Métrica principal | Criterio seguir/parar |
|---|---|---|---|---|
| Mayoristas B2B | BL-012 | Tiendas con clientes educados convierten más rápido | Pedido inicial + reposición | Seguir si ≥3/10 reponen en 30 días |
| Omar personal brand | BL-019 | Contenido de perros de competencia genera leads calificados | Leads calificados/mes | Seguir si >10 leads calificados/mes |
| Mensaje horneado vs facilidad | BL-020 | Cambiar mensaje mejora conversión | Compras por variante | Tratar como indicio si <20 compras |

**Gasto máximo propuesto:** Definir antes de iniciar según BL-044; no superar COP X (por definir con Andrés).

**Criterio para avanzar a Fase 3:** Confirmar presupuesto disponible para ads + al menos un canal de Fase 2 funcionando.

---

### Fase 3: Canales con inversión publicitaria

**Objetivo:** Escalar adquisición con inversión controlada.

| Experimento | Framework | Pre-requisitos | Métrica principal | Criterio seguir/parar |
|---|---|---|---|---|
| Meta Ads tráfico a perfil | E04 | Presupuesto confirmado, BL-016 (mensaje validado), landing list | CPV, CPF, seguidores calificados | Seguir si KPIs dentro de umbrales (E04) |
| Meta Ads adquisición | E03 | Todo lo anterior + formulario + capacidad de llamadas | Leads calificados, costo por lead | Seguir si contribución después de captación >0 |

**Nota:** Los frameworks E03 y E04 son clones de videos externos con cifras que no corresponden a Canívoros. Antes de ejecutar, adaptar los KPIs a la realidad del negocio.

---

## 6. Eventos de medición y KPIs

### KPIs por canal (propuestos)

| Canal | KPI primario | KPI secundario | Frecuencia |
|---|---|---|---|
| WhatsApp | Conversión consulta→compra | Tiempo de respuesta | Semanal |
| Distribuidores | Reposiciones/mes | Stock activo | Quincenal |
| B2B mayorista | Pedidos + reposición | Margen por pedido | Mensual |
| Instagram/Omar | Leads calificados | Costo por lead | Semanal |
| Meta Ads | CPV, CPF, costo por venta | ROAS si se conoce margen | Por cohorte |
| Recuperación | Reactivaciones | LTV post-reactivación | Por cohorte |
| Reposición | Tasa recompra 30d | Frecuencia media | Por cohorte |

### Eventos mínimos a registrar

Para cada contacto/lead:
1. Fecha y canal de origen (WhatsApp, Instagram, distribuidor, ad, referido)
2. Producto consultado
3. Etapa alcanzada (consulta, cotización, pedido, pago, entrega)
4. Motivo de pérdida si aplica
5. Variante de experimento si aplica (ej. mensaje A vs B)

Referencia: BL-011 (sistema mínimo de datos) y BL-021 (ventas con origen).

---

## 7. Puertas de aprobación (approval gates)

| Puerta | Condición | Quién aprueba | Acción si no cumple |
|---|---|---|---|
| **G0: Iniciar Fase 1** | BL-004 y BL-059 completos | Andrés | No iniciar experimentos |
| **G1: Iniciar Fase 2** | ≥1 experimento Fase 1 positivo | Andrés | Repetir o ajustar Fase 1 |
| **G2: Iniciar Fase 3** | Presupuesto confirmado + ≥1 canal Fase 2 funcionando | Andrés + responsable financiero | No invertir en ads |
| **G3: Escalar** | Contribución acumulada positiva en 6+ semanas (BL-028) | Andrés | Ajustar o detener |

---

## 8. Limitaciones de este plan

1. **Datos faltantes:** Precios, márgenes, capacidad y presupuesto no están confirmados en el repositorio. Los criterios numéricos (>10%, ≥3/20) son propuestas a validar con datos reales.

2. **Referencias públicas no verificadas:** No se pudo acceder a las cuentas de Instagram para verificar métricas de audiencia o actividad.

3. **Frameworks no adaptados:** E03 y E04 contienen cifras de videos externos que no aplican a Canívoros. Requieren adaptación antes de ejecutar.

4. **Hipótesis no validadas:** Las hipótesis de cada experimento son supuestos del repositorio, no resultados observados.

5. **Secuencia propuesta, no prescrita:** El orden puede cambiar según prioridades del negocio o descubrimientos en Fase 0.

---

## 9. Conexión con el backlog existente

| Este documento | Backlog relacionado |
|---|---|
| Fase 0 | BL-004, BL-005, BL-025, BL-035, BL-059 |
| Fase 1 | BL-022, BL-060 |
| Fase 2 | BL-012, BL-019, BL-020 |
| Fase 3 | E03, E04 (requiere adaptación) |
| Criterios de decisión | BL-044 |
| Medición | BL-011, BL-013, BL-021 |

---

## 10. Próximos pasos sugeridos

1. Revisar y aprobar este plan con Andrés.
2. Completar BL-004 (línea base de ventas) y BL-059 (auditoría WhatsApp).
3. Decidir orden de Fase 1 según hallazgos de Fase 0.
4. Documentar hipótesis y criterios en BL-044 antes de cada experimento.
5. Actualizar este plan con resultados observados.

---

**Nota:** Este documento es una propuesta de trabajo. Los criterios, umbrales y secuencia requieren validación con datos reales y aprobación de los responsables del negocio.
