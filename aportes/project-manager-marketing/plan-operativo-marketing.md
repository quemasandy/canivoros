# Plan Operativo de Marketing y Campaña — Canívoros Bogotá

**Versión 1 · 11 nov 2026 · Propuesta de trabajo para Andrés.** No está aprobado por la empresa. No publicar, imprimir ni enviar a terceros sin revisión.

**Autor:** Aporte de Project Manager Marketing (bot). **Fuentes:** `backlog/TODAS-LAS-TAREAS.md`, `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, `CANIVOROS-REFERENCIA-EMPRESA.md`, `branding/`, `embudos/EMBUDOS.md` (rama `develop` y `branding`, consultadas 11/11/2026).

---

## Propósito del documento

Este plan **no reemplaza** el backlog (61 tareas) ni el plan de crecimiento de 90 días. Los complementa organizando las tareas de marketing en:

1. **Flujos de trabajo (workstreams)** con sus dependencias
2. **Puertas de decisión (gates)** que requieren aprobación explícita
3. **Acciones detalladas de los próximos 7–14 días**
4. **Registro de riesgos y bloqueadores**
5. **Marco de medición** con definiciones y metas propuestas (no cifras inventadas)
6. **Separación explícita de hechos vs hipótesis**

---

## 1. Contexto y supuesto de planificación

### Hechos verificados en el repo

| Hecho | Fuente |
|---|---|
| Canívoros produce alimento horneado para perros en Sopó, Cundinamarca | `CANIVOROS-REFERENCIA-EMPRESA.md` |
| Existen 6 distribuidores publicados (2 en Bogotá) | `CANIVOROS-REFERENCIA-EMPRESA.md` §Distribuidores |
| Hay ventas jul–oct 2026 por cliente, fecha y producto (sin precios) | `ventas_canivoros_2026.xlsx`, citado en BL-004 |
| Se desconocen precios confirmados por canal, costos y márgenes | `backlog/BL-005`, `erp.md` |
| Se desconoce la capacidad de producción adicional | `backlog/BL-036` |
| No hay fecha de lanzamiento establecida | Plan Bogotá, conversación con Andrés |

### Supuesto de planificación

No existe fecha de lanzamiento confirmada. Este plan usa **días relativos** (Día 1 = primer día de ejecución acordado). Si Andrés, Sebastián y la empresa acuerdan una fecha de arranque, los días relativos se convierten en fechas calendario.

**[Propuesta]** Fecha de arranque sugerida: lunes siguiente a la aprobación del acuerdo BL-002. Esto es una propuesta, no un compromiso.

---

## 2. Flujos de trabajo (Workstreams)

El backlog tiene 61 tareas agrupadas en 7 semanas. Para efectos de gestión de marketing, las organizo en 5 flujos de trabajo paralelos:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          PLAN OPERATIVO: 5 WORKSTREAMS                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  WS1: INVESTIGACIÓN      WS2: POSICIONAMIENTO    WS3: LANDING/WEB              │
│  ─────────────────       ──────────────────      ─────────────                 │
│  BL-006 Guion entrev.    BL-016 Afirmaciones     BL-042 WordPress              │
│  BL-007 Entrevistas      BL-020 Test mensajes    BL-029 Dominio                │
│  BL-010 Prospectos       branding/* (ver nota)   BL-019 Omar/IG                │
│  BL-015 Competencia                                                            │
│  BL-024 QFD                                                                    │
│         │                       │                       │                      │
│         ▼                       ▼                       ▼                      │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                    WS4: CAMPAÑAS Y ANUNCIOS                              │   │
│  │  ──────────────────────────────────────────                              │   │
│  │  BL-012 Prospección B2B    BL-022 Recordatorios    embudos/E01–E04       │   │
│  │  BL-023 Presentación       BL-043 Criadores        BL-026 Gatívoros      │   │
│  │  BL-060 Recuperación                                                     │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                       │                                        │
│                                       ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                    WS5: ANALYTICS Y MEDICIÓN                             │   │
│  │  ──────────────────────────────────────                                  │   │
│  │  BL-004 Línea base         BL-013 Tablero          BL-021 Origen ventas  │   │
│  │  BL-061 Bitácora caso      BL-028 Decisión Bogotá                        │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Nota sobre branding/**: El trabajo de marca (posicionamiento, voz, mensajes, identidad visual) está en la rama `branding` y es responsabilidad del bot Canívoros. Este plan de PM **no duplica** ese trabajo; coordina con él. Las tareas BL-016 y BL-020 dependen de que `branding/` esté aprobado antes de publicar anuncios.

---

## 3. Tabla de trabajo (Work-Item Backlog) — Marketing

Filtro de las 61 tareas: solo las relevantes para marketing, ordenadas por dependencias. Columnas añadidas: **Gate** (si requiere aprobación) y **Bloqueador actual** (si existe).

| # | Clave | Workstream | Título | Depende de | Gate requerido | Bloqueador actual |
|---|---|---|---|---|---|---|
| 1 | BL-005 | Base | Confirmar precios, unidades y catálogo | — | G1 | No hay precios confirmados |
| 2 | BL-004 | WS5-Analytics | Calcular línea base (kilos, clientes, recompra) | BL-005 | — | Espera precios |
| 3 | BL-047 | Base | Plantilla única de ventas con origen | BL-005 | — | — |
| 4 | BL-058 | Base | Permiso de datos y comunicaciones | — | G2 | — |
| 5 | BL-059 | WS1-Investigación | Auditoría WhatsApp (2 semanas) | BL-058 | — | — |
| 6 | BL-006 | WS1-Investigación | Guion de entrevistas | — | — | — |
| 7 | BL-007 | WS1-Investigación | Entrevistas Omar + distribuidores | BL-006 | — | — |
| 8 | BL-010 | WS1-Investigación | Verificar 134 prospectos Bogotá | — | — | — |
| 9 | BL-035 | WS1-Investigación | Validar 6 distribuidores del sitio | — | — | — |
| 10 | BL-015 | WS1-Investigación | Comparar 8–12 competidores | — | — | — |
| 11 | BL-014 | WS1-Investigación | Matriz de microzonas | BL-007, BL-010 | — | — |
| 12 | BL-016 | WS2-Posicionamiento | Revisar afirmaciones y claims | — | **G3** | — |
| 13 | BL-020 | WS2-Posicionamiento | Test mensajes: horneado vs facilidad | BL-016, BL-019 | G3 | — |
| 14 | BL-042 | WS3-Landing | Revisar WordPress | BL-005 | — | — |
| 15 | BL-029 | WS3-Landing | Nombre, dominio, subdominio | — | — | — |
| 16 | BL-019 | WS3-Landing | Quick win: Omar + captura leads | BL-011, BL-016, BL-044, BL-051, BL-058, BL-059 | G3 | — |
| 17 | BL-044 | WS4-Campañas | Plantilla hipótesis por experimento | — | — | — |
| 18 | BL-060 | WS4-Campañas | Recuperar clientes inactivos | BL-004, BL-005, BL-044, BL-058 | **G4** | — |
| 19 | BL-012 | WS4-Campañas | Prospección B2B: 10 tiendas | BL-005, BL-010, BL-035, BL-044 | G4 | — |
| 20 | BL-022 | WS4-Campañas | Recordatorio de reposición | BL-004, BL-044, BL-058 | G2 | — |
| 21 | BL-023 | WS4-Campañas | Presentación de entrada | BL-005, BL-044 | G4 | — |
| 22 | BL-043 | WS4-Campañas | Programa criadores alto volumen | BL-004, BL-044 | G4 | — |
| 23 | BL-026 | WS4-Campañas | Gatívoros: piloto veterinarias | BL-025 | G4 | — |
| 24 | BL-013 | WS5-Analytics | Tablero semanal indicadores | BL-004 | — | — |
| 25 | BL-021 | WS5-Analytics | Medir ventas con origen (>80%) | BL-004, BL-011, BL-047, BL-049 | — | — |
| 26 | BL-061 | WS5-Analytics | Bitácora caso Canívoros | BL-002, BL-004 | — | — |
| 27 | BL-028 | WS5-Analytics | Decisión: ampliar/ajustar/detener | BL-013, BL-012 | **G5** | — |

---

## 4. Puertas de decisión (Decision Gates)

**Regla general:** ningún contenido se publica, ningún gasto se ejecuta, y ningún claim de salud/nutrición/regulatorio se usa sin pasar el gate correspondiente.

### G1 — Aprobación de catálogo y precios

| Campo | Valor |
|---|---|
| **Qué se aprueba** | Lista de productos, precios por canal, unidades (kg o lb), catálogo en Odoo |
| **Quién aprueba** | La dueña (prima) o Sara Ramírez, con Sebastián |
| **Cuándo** | Antes de calcular línea base (BL-004) y antes de cualquier oferta comercial |
| **Entregable** | Documento con precios firmado o confirmado por escrito (correo, WhatsApp) |
| **Criterio de paso** | Cada producto tiene precio por canal confirmado; unidad unificada |

### G2 — Aprobación de permisos y comunicaciones

| Campo | Valor |
|---|---|
| **Qué se aprueba** | Texto de autorización para datos y mensajes (ley colombiana); campo en CRM |
| **Quién aprueba** | La dueña (prima) + Andrés (redacción) |
| **Cuándo** | Antes de contactar clientes para recordatorios (BL-022) o recuperación (BL-060) |
| **Entregable** | Texto aprobado; proceso de captura del permiso |
| **Criterio de paso** | Texto revisado; no se contacta a quien no autorizó |

### G3 — Aprobación de claims y mensajes de marca

| Campo | Valor |
|---|---|
| **Qué se aprueba** | Afirmaciones del sitio, empaques y anuncios que impliquen salud, nutrición, calidad o registro ICA |
| **Quién aprueba** | La dueña (prima) para claims de empresa; Andrés para copy; Sebastián para soporte técnico (registro ICA, ficha técnica) |
| **Cuándo** | Antes de publicar cualquier anuncio, post o material con claim |
| **Entregable** | Lista de afirmaciones con estado: **soportada** / **reformular** / **quitar** (ver BL-016 y `branding/03-mensajes.md` §mensajes prohibidos) |
| **Criterio de paso** | Ningún claim sin soporte en la lista publicada; registro ICA con número |

**Claims que requieren este gate (lista de `branding/03-mensajes.md`):**

- «100 % natural»
- «Libre de granos»
- «Super premium»
- «Completo y balanceado»
- «Sin subproductos» (vs. materia prima de cabezas, barrigas, vísceras)
- «Elimina bacterias» (horneado)
- Beneficios de salud: digestión, sistema inmune, limpieza dental
- «Certificado ICA» (requiere número de registro)

### G4 — Aprobación de gasto y experimentos

| Campo | Valor |
|---|---|
| **Qué se aprueba** | Presupuesto máximo por experimento; muestras; descuentos; horas comerciales |
| **Quién aprueba** | Andrés + Sebastián + la dueña (prima) para gastos >$100 USD |
| **Cuándo** | Antes de lanzar cada experimento (BL-012, BL-019, BL-022, BL-023, BL-043, BL-060) |
| **Entregable** | Ficha BL-044 con hipótesis, métricas, casos, gasto máximo y regla seguir/ajustar/parar |
| **Criterio de paso** | Gasto máximo definido por escrito; no se gasta más sin nueva aprobación |

### G5 — Decisión de ampliar, ajustar o detener

| Campo | Valor |
|---|---|
| **Qué se decide** | Continuar piloto, expandir zona, ajustar oferta o detener inversión |
| **Quién decide** | Andrés + Sebastián + la dueña (prima) |
| **Cuándo** | Día 60–90 (semana 7 del backlog), con datos de BL-028 |
| **Entregable** | Documento de decisión con datos (contribución, recompra, capacidad, servicio) |
| **Criterio de paso** | Cohortes con seguimiento suficiente; decisión registrada con motivo |

---

## 5. Acciones detalladas: Días 1–14 (primeras dos semanas)

**Supuesto:** Día 1 = primer día hábil tras aprobar BL-002 (acuerdo Andrés–Sebastián).

### Día 1–3 (WS-Base + WS5-Analytics)

| Día | Tarea | Responsable | Entregable | Gate |
|---|---|---|---|---|
| 1 | BL-001: Cambiar contraseñas, cerrar Odoo al público | Sebastián | Confirmación de cambio (sin escribir claves) | — |
| 1 | BL-002: Llamada acuerdo línea base y cobro | Andrés + Sebastián | Documento 1 página | — |
| 1 | BL-052: Configurar backup diario fuera del VPS | Sebastián | Script + primera copia | — |
| 2 | BL-005: Reunión con prima/Sara para precios | Sebastián | Lista de precios borrador | **G1** |
| 2 | BL-003: Elegir tablero (Kanban Odoo, Taiga o Plane) | Andrés | Tablero con ítems importados | — |
| 3 | BL-005: Confirmar precios por canal y unidades | Sebastián | Lista de precios confirmada | **G1** |

### Día 4–7 (WS1-Investigación)

| Día | Tarea | Responsable | Entregable | Gate |
|---|---|---|---|---|
| 4 | BL-058: Redactar texto de autorización | Andrés | Texto borrador | — |
| 4 | BL-006: Preparar guion de entrevistas | Andrés | Guion 10 preguntas cliente + tienda | — |
| 5 | BL-058: Aprobar texto con prima | Andrés + prima | Texto aprobado | **G2** |
| 5 | BL-044: Crear plantilla de hipótesis | Andrés | Plantilla en backlog/ | — |
| 6 | BL-035: Llamar a los 6 distribuidores publicados | Omar | Lista con estado activo/inactivo | — |
| 6 | BL-010: Empezar verificación de 30 prospectos | Andrés | 10 prospectos verificados | — |
| 7 | BL-007: Primera entrevista con Omar | Sebastián | Notas estructuradas | — |

### Día 8–14 (WS1 + WS5-Analytics)

| Día | Tarea | Responsable | Entregable | Gate |
|---|---|---|---|---|
| 8 | BL-004: Calcular línea base (kilos, clientes) | Andrés | Tabla kilos/mes y clientes únicos | — |
| 8 | BL-059: Empezar auditoría WhatsApp (con Omar) | Andrés + Omar | Plantilla de registro | — |
| 9 | BL-007: Segunda entrevista (distribuidor 1) | Sebastián | Notas estructuradas | — |
| 10 | BL-010: Continuar verificación prospectos | Andrés | 20 prospectos verificados | — |
| 10 | BL-047: Crear plantilla de ventas con origen | Sebastián | Hoja con columnas fijas | — |
| 11 | BL-036: Estimar capacidad de producción | Sebastián | Kilos/semana disponibles | — |
| 12 | BL-007: Tercera entrevista (distribuidor 2) | Sebastián | Notas estructuradas | — |
| 13 | BL-061: Crear bitácora del caso Canívoros | Andrés | Documento vivo | — |
| 14 | BL-004: Completar línea base con recompra | Andrés | Tabla completa con intervalo entre compras | — |

### Checkpoint Día 14

**Revisión:** Andrés + Sebastián (30 min)

| Verificar | Criterio de éxito |
|---|---|
| G1 cerrado | Precios confirmados por canal |
| G2 cerrado | Texto de autorización aprobado |
| Línea base calculada | Kilos/mes, clientes únicos, % recompra |
| Distribuidores validados | 6 con estado activo/inactivo |
| Prospectos verificados | 30 de 134 |
| Auditoría WhatsApp | 1 semana de datos |
| Capacidad producción | Kilos/semana conocidos |

---

## 6. Registro de riesgos y bloqueadores

| ID | Riesgo / Bloqueador | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|---|---|---|---|
| R1 | Precios no confirmados (BL-005) | Alta | Alto | Escalar a Andrés para reunión con prima | Sebastián |
| R2 | Capacidad de producción insuficiente | Media | Alto | No prometer más ventas hasta tener BL-036 | Sebastián |
| R3 | Claims sin soporte (BL-016) | Alta | Alto | Bloquear G3 hasta tener lista aprobada; no publicar | Andrés |
| R4 | Instagram no accesible sin login | Confirmado | Bajo | Usar fuentes públicas; no bypass | — |
| R5 | Distribuidores publicados inactivos | Media | Medio | Actualizar sitio con los activos | Omar |
| R6 | Registro ICA sin número disponible | Media | Alto | Pedir a prima; no usar claim «certificado» sin él | Sebastián |
| R7 | Permisos de clientes no capturados | Alta | Alto | No contactar sin BL-058 cerrado | Andrés |
| R8 | Falta de datos de costos para contribución | Alta | Alto | Calcular solo kilos hasta BL-025; marcar COP como «desconocido» | Andrés |

---

## 7. Marco de medición

### Definiciones de métricas (sin cifras inventadas)

| Métrica | Definición | Fuente | Frecuencia | Meta propuesta (a validar) |
|---|---|---|---|---|
| Ventas netas (kilos) | Kilos vendidos – kilos devueltos | BL-004, BL-047 | Semanal | Establecer línea base primero |
| Ventas netas (COP) | COP vendidos – descuentos – devoluciones | BL-004 + BL-005 | Semanal | Solo con precios confirmados |
| Clientes nuevos | Clientes con primera compra en el período | BL-047 | Semanal | Establecer línea base |
| Recompra 30 días | Clientes con segunda compra ≤30 días / clientes que completaron ventana | BL-004 | Mensual | Establecer línea base |
| Recompra 60 días | Igual, ventana 60 días | BL-004 | Mensual | Establecer línea base |
| Tiempo entre compras | Días entre compras sucesivas por cliente | BL-004 | Mensual | Insumo para BL-022 |
| CAC | Gasto de captación / clientes nuevos compradores | BL-044 + BL-021 | Por experimento | Definir máximo aceptable en G4 |
| Conversión consulta→compra | Consultas que compran / consultas totales | BL-059 | Semanal | Establecer línea base |
| % ventas con origen | Ventas con origen registrado / ventas totales | BL-021 | Semanal | >80% para cobro (BL-002) |
| Contribución | Ventas netas – costos variables (producción, empaque, entrega, comisiones) | BL-025 + BL-049 | Mensual | Requiere costos confirmados |

### Qué NO se mide todavía

- **Ingresos proyectados**: no hay precios confirmados.
- **Margen**: no hay costos por producto.
- **ROI de campaña**: no hay gasto ni ingresos atribuibles.
- **Clientes de la competencia**: Instagram no accesible sin login.

---

## 8. Hechos vs. hipótesis

### Hechos verificados

| # | Afirmación | Fuente |
|---|---|---|
| 1 | Canívoros produce en Sopó, Cundinamarca | `CANIVOROS-REFERENCIA-EMPRESA.md` |
| 2 | Producto horneado, no crudo ni BARF | `CANIVOROS-REFERENCIA-EMPRESA.md` §FAQ |
| 3 | Líneas: perros (Canívoros) y gatos (Gatívoros) | `CANIVOROS-REFERENCIA-EMPRESA.md` §Productos |
| 4 | Sabores: pollo, salmón, cerdo | `CANIVOROS-REFERENCIA-EMPRESA.md` |
| 5 | 6 distribuidores publicados | `CANIVOROS-REFERENCIA-EMPRESA.md` §Distribuidores |
| 6 | 3 números de WhatsApp publicados | `CANIVOROS-REFERENCIA-EMPRESA.md` §Contacto |
| 7 | Existen ventas jul–oct 2026 por cliente y fecha | `ventas_canivoros_2026.xlsx` (citado en BL-004) |
| 8 | Instagram @canivoros_col existe | Búsqueda pública 11/11/2026 |
| 9 | Hay testimonios publicados en el sitio | `CANIVOROS-REFERENCIA-EMPRESA.md` §Testimonios |
| 10 | El sitio menciona registro ICA pero no publica número | `CANIVOROS-REFERENCIA-EMPRESA.md` §FAQ |

### Hipótesis a validar

| # | Hipótesis | Cómo validarla | Tarea relacionada |
|---|---|---|---|
| H1 | Los precios actuales permiten contribución positiva | Confirmar precios y costos | BL-005, BL-025 |
| H2 | Hay capacidad de producción para crecer | Medir kilos/semana disponibles | BL-036 |
| H3 | Se pierden ventas por respuesta lenta en WhatsApp | Auditoría de 2 semanas | BL-059 |
| H4 | Parte de los clientes inactivos vuelve con un recordatorio | Experimento de recuperación | BL-060 |
| H5 | El segmento criadores es el más rentable | Analizar ventas jul–oct | BL-004, BL-043 |
| H6 | Los distribuidores publicados siguen activos | Llamar a los 6 | BL-035 |
| H7 | El mensaje «horneado» convierte mejor que «facilidad de uso» | Test A/B | BL-020 |
| H8 | Un recordatorio de reposición aumenta la recompra | Experimento con permiso | BL-022 |
| H9 | Tiendas que venden Pixie/BARF compran Canívoros más rápido | Prospección B2B | BL-012 |

---

## 9. Coordinación con otros aportes

| Aporte | Rama | Responsable | Dependencia de este plan |
|---|---|---|---|
| Branding | `branding` | Bot Canívoros | G3 (claims y mensajes) requiere `branding/03-mensajes.md` aprobado |
| Copy Humanizer | `aporte/copy-humanizer` | Bot Copy Humanizer | BL-019, BL-020, BL-022 usan la guía de escritura |
| Embudos | `develop` (embudos/) | Bot Embudos | E01–E04 son diseños; este plan coordina su ejecución |

**Regla de coordinación:** antes de publicar cualquier copy o anuncio, verificar con `branding/02-personalidad-y-voz.md` y `aportes/copy-humanizer/guia-de-escritura.md`.

---

## 10. Siguientes pasos sugeridos

1. **Andrés y Sebastián:** revisar este plan y aprobar o ajustar los gates.
2. **Andrés:** agendar BL-002 (llamada acuerdo) para definir Día 1.
3. **Sebastián:** preparar reunión BL-005 con prima/Sara.
4. **Ambos:** importar las tareas de marketing al tablero elegido (BL-003) con la columna «Gate» añadida.

---

## 11. Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 11 nov 2026 | Versión inicial |

---

**Fuentes consultadas el 11 nov 2026:**
- `develop`: `backlog/TODAS-LAS-TAREAS.md`, `backlog/README.md`, `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, `CANIVOROS-REFERENCIA-EMPRESA.md`, `embudos/EMBUDOS.md`
- `branding`: `branding/README.md`, `branding/03-mensajes.md`
- `aporte/copy-humanizer`: `aportes/copy-humanizer/guia-de-escritura.md`
- Instagram: búsqueda pública @canivoros_col, @friskiesbr (no accesibles sin login)

**Límites de acceso:**
- Instagram requiere login; no se hizo bypass.
- No se accedió a datos de competidores más allá de lo público.
- No se inventaron cifras de ventas, precios, costos ni clientes.
