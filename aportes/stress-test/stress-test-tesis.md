# Stress-Test de la Tesis · Canívoros

Documento de trabajo para probar la tesis de negocio antes de escalar inversión.

Fecha: 2026-11-11 · Estado: propuesta para revisión de Andrés.

> **Convención:** *Dato* = registrado en el repo con fuente. *Supuesto* = hipótesis a validar. *Desconocido* = sin información.

---

## 1. Tesis actual (en una frase)

> «Aumentar las ventas rentables y recurrentes de Canívoros en Bogotá mediante un proceso que conecte investigación del mercado, captación de clientes, distribución, producción y análisis de resultados.»

**Fuente:** `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, línea 7 (rama `develop`).

La tesis implícita es que existe demanda suficiente de alimento natural horneado para perros en Bogotá, que Canívoros puede captar nuevos clientes de forma rentable más allá de la red actual de Omar, y que la operación puede sistematizarse para crecer.

---

## 2. Qué tiene que ser cierto

Para que la tesis funcione, deben cumplirse **todos** estos supuestos:

| # | Supuesto | Estado actual | Fuente |
|---|---|---|---|
| **A. Cliente** | Existen tutores en Bogotá dispuestos a pagar por alimento horneado, fuera de la red personal de Omar | *Supuesto*; solo hay ventas a conocidos, recomendados y criadores | `erp.md` §6–7; `E01-embudo.md` §2 |
| **B. Problema/trabajo** | Los tutores buscan una alternativa «natural y fácil» al concentrado, sin tener que cocinar ni usar dieta cruda | *Supuesto*; no hay entrevistas documentadas con compradores finales | `BL-006`, `BL-007` (pendientes) |
| **C. Disposición a pagar** | El precio actual (10.000–28.000 COP/kg en 500 g; 6.200 COP/kg a criadores) deja margen positivo tras costos variables | *Desconocido*; no hay costos confirmados | `BL-005`, `BL-025` (pendientes) |
| **D. Recompra** | Los clientes nuevos vuelven a comprar con frecuencia suficiente para recuperar el costo de adquisición | *Dato parcial*: 27 de ~55 clientes repiten (jul–oct), moviendo ~87% de los kg; pero casi todos son criadores o conocidos de Omar, no adquiridos por pauta | `E01-embudo.md` §2; `ventas_canivoros_2026.xlsx` |
| **E. Economía unitaria** | Contribución por pedido > 0 y CAC recuperable en un número de compras que el cliente promedio realiza | *Desconocido*; precio, costo, margen y CAC sin datos | `BL-004`, `BL-005`, `BL-025` |
| **F. Cadena de frío / entrega** | Se puede entregar en Bogotá a un costo que no destruya el margen | *Desconocido*; no hay datos de costo de entrega ni vida útil documentada | `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` §Datos pendientes |
| **G. Canal** | WhatsApp + distribuidores + tiendas pueden escalar sin depender exclusivamente de Omar | *Supuesto*; hoy Omar es el único punto de contacto comercial real | `erp.md` §2; tres números de WhatsApp publicados sin responsable definido |
| **H. Regulación** | El registro ICA está vigente y permite vender el producto como alimento balanceado | *Afirmación de marca*; número de registro no publicado | `CANIVOROS-REFERENCIA-EMPRESA.md` línea 40 |
| **I. Capacidad del fundador** | Omar y el equipo de 5 personas pueden producir más de lo que venden actualmente | *Desconocido*; capacidad adicional por medir; fallas de máquina frecuentes | `BL-036`, `BL-009` (pendientes); `erp.md` §8 |

---

## 3. Evidencia a favor y en contra

### Grado de evidencia

| Grado | Descripción | Qué demuestra |
|---|---|---|
| **A** | Comportamiento con dinero: pagos, pedidos repetidos, compromisos firmados | Validación fuerte |
| **B** | Primaria fuerte: entrevistas sobre comportamiento pasado, datos reales de ventas/precios | Señal fuerte, no validación |
| **C** | Corroborante: reseñas, discusiones, contenido generado por usuarios | Contexto útil |
| **D** | Proxy: reportes de mercado, tendencias de búsqueda, inversión en el sector | Indicio, **no validación** |
| **E** | Afirmación: lo dice la marca, un fundador o un experto sin datos | Hipótesis, **no evidencia** |

### Evidencia disponible

| Supuesto | A favor | Grado | En contra | Grado |
|---|---|---|---|---|
| A. Cliente | Ventas jul–oct a ~55 clientes; ~10.5M COP/mes promedio | B (datos de ventas, pero casi todos son red de Omar) | 52% de ingresos son criadores, 18% tiendas, solo 11% cliente final; casi todos llegan por relación personal | B |
| B. Problema | La marca dice que tutores buscan «natural y fácil»; hay testimonios en el sitio | E (declaración de marca) | No hay entrevistas documentadas con compradores que no sean conocidos de Omar | — |
| C. Disposición a pagar | Competidores venden natural horneado a 21.000–35.000 COP/kg; Canívoros está en rango (10.000–28.000 COP/kg) | B (precios de mercado) | Precio a criadores (6.200 COP/kg) es muy bajo vs. competencia; ¿hay margen? | — |
| D. Recompra | 87% de kg viene de clientes que repiten | A (comportamiento) | Casi todos son criadores con relación personal; no demuestra recompra de clientes adquiridos por pauta | — |
| E. Economía unitaria | — | — | Costos desconocidos; la materia prima incluye subproductos de disponibilidad irregular | — |
| F. Entrega | VITA cobra 39.900 COP de envío por 2.4 kg; Puppis gratis desde 160.000 COP; indica que el envío de natural es caro para todos | D (proxy de mercado) | Costo de entrega de Canívoros: desconocido | — |
| G. Canal | Hay 5 distribuidores publicados y se vende por WhatsApp | B | 3 números de WhatsApp sin responsable claro; la auditoría BL-059 aún no se hace; la conversión es desconocida | — |
| H. Regulación | La marca dice «registro ICA» | E (afirmación) | Número de registro no publicado; usar «sin subproductos» cuando la materia prima incluye cabezas de pollo y vísceras es un riesgo de credibilidad | E / B (ver `erp.md` §1–2) |
| I. Capacidad | Hay cuarto frío de 6 ton, equipo de 5 personas | B | Fallas de máquina frecuentes; capacidad adicional desconocida; materia prima con disponibilidad irregular | B |

### Evidencia que falta y tiene alto valor

1. **Entrevistas con clientes que NO sean conocidos de Omar** — para saber si el problema existe fuera de la red actual.
2. **Costo unitario por producto** — sin esto no hay economía unitaria.
3. **Auditoría de WhatsApp** — para saber cuántas consultas llegan y cuántas se pierden (BL-059).
4. **Número de registro ICA** — para confirmar la afirmación regulatoria.

---

## 4. El supuesto más probable que mate el negocio (Bottleneck Belief)

> **«Canívoros puede adquirir clientes fuera de la red de Omar a un costo que la economía unitaria soporte, con recompra suficiente para que el negocio sea rentable.»**

### Por qué este supuesto es crítico

1. **Concentración extrema:** el top 10 de clientes mueve ~65% de los kg; el cliente más grande, ~24%. Casi todos llegaron por la reputación de Omar en el mundo de perros de competencia. Fuente: `E01-embudo.md` §2.

2. **El motor de tutores (11% de ingresos) no está probado:** los embudos E01–E04 asumen tasas de conversión (60% calificado, 25% compra, CAC ~40.000 COP) que son *supuestos*, no datos. Fuente: `E01-embudo.md` §7.

3. **Sin costos confirmados, no se puede saber si el CAC es recuperable.** Un CAC de 40.000 COP solo es sostenible si la contribución de la primera compra más la recompra lo cubre. Pero la contribución es *desconocida*. Fuente: `BL-025` (pendiente).

4. **La recompra observada es de criadores, no de clientes adquiridos por pauta.** Que un criador compre 40–110 kg cada 2–3 semanas no predice que un tutor adquirido por Meta Ads compre 2 kg cada mes.

### Qué pasa si este supuesto es falso

Si el CAC de adquirir tutores por pauta supera la contribución acumulada que generan (incluyendo recompra), cada peso invertido en crecimiento destruye valor. El negocio quedaría limitado a la red de Omar, sin escala.

---

## 5. Próximo experimento: el más barato que produzca evidencia conductual

### Objetivo

Obtener **evidencia de grado A o B** sobre si clientes fuera de la red de Omar compran y recompran, a un costo que permita medir sin arruinar el negocio.

### Diseño propuesto

| Elemento | Valor |
|---|---|
| **Hipótesis** | Al menos 3 de cada 20 clientes inactivos o de una sola compra (no criadores) vuelven a comprar con un mensaje de reposición y precio claro. |
| **Población** | Clientes de `ventas_canivoros_2026.xlsx` con 1–2 compras, que no sean criadores y cuyo último pedido fue hace >30 días. Excluir criadores y clientes de alto volumen. |
| **Intervención** | Un mensaje por WhatsApp con precio real (requiere BL-005), presentación disponible y fecha de entrega. Solo a quienes tengan permiso (BL-058). |
| **Métrica principal** | Compras completadas (pagadas y entregadas) / contactados, a 14 días. |
| **Métrica secundaria** | Recompra a 30 días después de la primera compra del experimento. |
| **Umbrales de decisión (propuestos, los fija Andrés):** | |
| — Seguir | ≥15% de contactados compran y contribución incremental ≥0. |
| — Ajustar | 5–14% compran o muchas respuestas pero pocos cierres. |
| — Parar | <5% compran o contribución negativa. |
| **Duración** | 14 días para el cierre; +30 días para recompra. |
| **Costo máximo (propuesto)** | 0 COP en pauta; solo tiempo de Omar o la responsable (~4 h). |
| **Qué registrar** | Contactados, respondieron, compraron, motivo de no compra, COP vendidos, contribución (si se conoce el costo). |

### Prerrequisitos

Este experimento **no puede correr** hasta completar:

1. **BL-005** — precios confirmados para cotizar.
2. **BL-058** — permiso de datos para contactar.
3. **BL-004** — lista de clientes con criterio documentado.

El experimento es esencialmente **BL-060** del backlog, con umbrales explícitos.

### Por qué este experimento y no otro

- **No requiere pauta** — minimiza riesgo de perder dinero.
- **Usa datos existentes** — los clientes ya están en el Excel.
- **Produce evidencia A** — comportamiento de compra real.
- **Responde al bottleneck** — ¿compran clientes que no son criadores ni red cercana de Omar?

---

## 6. Qué NO hacer todavía

Acciones del backlog que serían prematuras hasta resolver el bottleneck:

| Backlog | Por qué esperar |
|---|---|
| **BL-019** (marca personal de Omar + captura de leads) | Sin saber si los leads convierten y recompran, invertir en generar más leads puede ser gasto sin retorno. |
| **BL-020** (comparar mensaje horneado vs facilidad) | Optimizar el mensaje antes de saber si la economía unitaria funciona es prematuro; se mejora algo que quizás no vale la pena escalar. |
| **BL-012** (prospección mayorista 10 tiendas) | Colocar producto en tiendas sin conocer el margen puede generar ventas que pierden dinero. La colocación inicial no es demanda; la reposición sí, pero sin margen no hay negocio. |
| **BL-023** (presentación de entrada / caja de prueba) | Crear una presentación nueva requiere entender primero si el producto actual genera recompra en clientes nuevos. |
| **BL-026** (Gatívoros en veterinarias) | Línea secundaria; dispersa el foco antes de validar el negocio principal. |
| **E03, E04** (embudos de anuncios Meta) | Son clones de frameworks con supuestos sin validar. Antes de invertir en pauta, demostrar que la economía unitaria cierra con clientes adquiridos por otro medio. |

**Fuentes de los ítems:** `backlog/README.md`, carpetas `embudos/E03-*` y `embudos/E04-*`.

---

## 7. Preguntas abiertas de mayor valor de información

Ordenadas por impacto en la decisión de invertir o no:

1. **¿Cuál es el costo variable por kg de cada producto?** Sin esto no hay economía unitaria. Depende de BL-025.

2. **¿Cuántas consultas de WhatsApp llegan por semana y qué porcentaje compra?** Sin esto no se sabe si el cuello de botella es tráfico o conversión. Depende de BL-059.

3. **¿Cuál es la vida útil del producto y qué conservación requiere?** Si es congelado, compite con todas las marcas que cobran envío alto; si es estable a temperatura ambiente como Dogo, tiene ventaja logística. No está documentado.

4. **¿El registro ICA está vigente y qué número tiene?** Es una afirmación de marca sin verificar. Un problema regulatorio puede cerrar el negocio.

5. **¿Qué pasa si Omar se enferma o se va?** Toda la comercialización depende de él. No hay persona de respaldo con las relaciones ni el conocimiento.

---

## Fuentes consultadas

- `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` (rama `develop`)
- `CANIVOROS-REFERENCIA-EMPRESA.md` (rama `develop`)
- `erp.md` (rama `develop`)
- `embudos/E01-canivoros-tres-motores-recompra/embudo.md` (rama `develop`)
- `embudos/E02-canivoros-recuperacion-y-recompra/embudo.md` (rama `develop`)
- `backlog/README.md` y archivos BL-004, BL-005, BL-025, BL-036, BL-059, BL-060 (rama `develop`)
- `competencia/competencia-2026-11-03.md` (rama `develop`)

No se pudo acceder a https://www.instagram.com/canivoros_col ni a https://www.instagram.com/friskiesbr (timeout / requieren autenticación).

---

## Historial

| Fecha | Cambio | Autor |
|---|---|---|
| 2026-11-11 | Creación del documento | Aporte stress-test |
