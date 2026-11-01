# Canívoros / Gatívoros — repositorio de crecimiento

Repositorio de trabajo para hacer crecer las ventas de **Canívoros** (perros) y **Gatívoros** (gatos) en Bogotá de forma medible: documentación de la empresa, plan comercial, levantamiento operativo para el ERP, metodologías y el backlog de tareas y experimentos.

## Qué es Canívoros / Gatívoros

- Empresa colombiana de **alimento natural horneado** para perros y gatos, con proteína animal (pollo, salmón y cerdo).
- La producción está en **Sopó (Cundinamarca)**; el mercado objetivo de este trabajo es **Bogotá**.
- Vende por WhatsApp, distribuidores y tiendas o clínicas aliadas.
- El detalle está en [CANIVOROS-REFERENCIA-EMPRESA.md](CANIVOROS-REFERENCIA-EMPRESA.md). Lo que ahí aparece es lo que declara la marca, no datos verificados.

## Para quién es este repositorio

| Persona | Rol | Qué usa más |
|---|---|---|
| Andrés | Growth partner: diagnóstico, experimentos comerciales, medición | Plan Bogotá, backlog, línea base |
| Sebastián | Parte técnica: Odoo, datos, infraestructura | `erp.md`, backlog (requisitos y errores) |
| Omar / equipo Canívoros | Operación, producción y venta | Tareas asignadas en el backlog, entrevistas |

Responsables, fechas y esfuerzos del backlog son **propuestas**, no compromisos.

## Estructura

| Ruta | Contenido |
|---|---|
| [CANIVOROS-REFERENCIA-EMPRESA.md](CANIVOROS-REFERENCIA-EMPRESA.md) | Ficha de la empresa: historia, productos, canales, distribuidores publicados |
| [CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md](CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md) | Plan comercial y de sistematización para Bogotá: microzonas, entrevistas, experimentos, indicadores, plan de 90 días |
| [erp.md](erp.md) | Levantamiento operativo para el ERP: compras, recepción, cuarto frío, producción, devoluciones, finanzas, máquinas |
| [metodologias_analisis_competitivo.md](metodologias_analisis_competitivo.md) | Técnicas de análisis de competencia aplicadas a Canívoros |
| [pasos_sysmkt.md](pasos_sysmkt.md) | Notas de descubrimiento de producto y de la oferta Growth Partner |
| [GuiaPesquisaProdutosServicosES.md](GuiaPesquisaProdutosServicosES.md) / [PT](GuiaPesquisaProdutosServicosPT.md) | Guía de investigación de productos y servicios (español / portugués) |
| [GuiaDesenvolverProdutosServicosES.md](GuiaDesenvolverProdutosServicosES.md) / [PT](GuiaDesenvolverProdutosServicosPT.md) | Guía para desarrollar productos o servicios (español / portugués) |
| [QFD.pdf](QFD.pdf) | Material de referencia sobre QFD (despliegue de la función de calidad) |
| `ventas_canivoros_2026.xlsx` | Registro de ventas jul–oct 2026 por cliente, fecha y producto (sin precios) |
| [backlog/](backlog/README.md) | Backlog BL-001 a BL-061 y sus consolidados |

## El backlog

El [backlog](backlog/README.md) tiene 61 ítems (BL-001 a BL-061): acciones, tareas, experimentos, requisitos, errores e ideas. Cada uno es un archivo `backlog/BL-*.md` con metadatos (prioridad, impacto, dependencias, responsable propuesto, criterios de aceptación, hechos e hipótesis).

- **Orden:** por impacto y prioridad, respetando dependencias, agrupado por semanas (desde el 2 de noviembre de 2026). El campo `order` indica el paso.
- **Vista por semanas:** [backlog/README.md](backlog/README.md).
- **Todas las tareas en un archivo:** [backlog/TODAS-LAS-TAREAS.md](backlog/TODAS-LAS-TAREAS.md) (con enlaces y fuentes).
- **Versión limpia:** [backlog/TODAS-LAS-TAREAS-SIN-REFERENCIAS.md](backlog/TODAS-LAS-TAREAS-SIN-REFERENCIAS.md) (sin enlaces ni fuentes).

Los consolidados se generan a partir de los `BL-*.md`: si se edita una tarea, hay que regenerarlos.

### Prioridades actuales

1. **BL-001 — Seguridad:** cambiar las contraseñas expuestas y cerrar Odoo al público. BL-052 (copias de seguridad) va justo después.
2. **BL-002 — Acuerdo y atribución:** acuerdo de cobro con un anexo que define qué venta cuenta como atribuible. No hay cobro por porcentaje hasta que BL-021 registre el origen de más del 80 % de las ventas.
3. **BL-004 / BL-005 — Línea base:** kilos y clientes desde el Excel de ventas; se convierten a COP solo con precios confirmados.
4. **BL-044 — Hipótesis antes de experimentar:** cada experimento lleva ficha con métrica en dinero, gasto máximo y regla de seguir, ajustar o parar.
5. **BL-059 — Auditoría de WhatsApp:** cuántas consultas entran, se responden y compran, antes de automatizar (BL-019).
6. **BL-060 — Recuperar clientes** que dejaron de comprar, y **BL-061 — Bitácora del caso** Canívoros.

### Qué sabemos y qué no

- **Conocido:** hay ventas registradas de julio a octubre de 2026 en kilos, por cliente y producto; hay compras grandes de criadores; hay distribuidores publicados en Bogotá y alrededores.
- **Desconocido por ahora:** precios confirmados por canal y unidad, ventas en COP, costos, márgenes, costo de adquisición, recompra en dinero, volumen de consultas por WhatsApp y capacidad de producción disponible.

Ningún documento del repo debe presentar como dato algo que todavía es hipótesis.

## Cómo contribuir

- **Ramas:** el trabajo se hace en `backlog` (o en una rama derivada como `docs/...`) del fork `quemasandy/canivoros` y se propone por PR hacia `develop` de `segodimor2d2/canivoros`.
- **PR anteriores:** #1 (backlog inicial) y #2 (consolidados) ya están unidos; #3 (ajustes de la auditoría Growth Partner) está en revisión.
- **Reglas:**
  - No subir contraseñas, tokens ni datos personales de clientes.
  - No forzar push sobre ramas compartidas.
  - Marcar como "desconocido" lo que no está medido; no estimar precios ni ventas.
  - Al editar un `BL-*.md`, actualizar `backlog/README.md` y regenerar los consolidados.
- Ver también [backlog/INSTRUCCIONES_GIT.md](backlog/INSTRUCCIONES_GIT.md).

## Qué no es este repositorio

- **No es la tienda online** ni el sitio WordPress de la marca.
- **No es el ERP:** aquí se documentan los requisitos; el código y la configuración de Odoo viven en repositorios relacionados (`canivorosodoo`, `canivoros-view`).
- **No es una fuente contable:** el Excel de ventas es un registro de trabajo, no la contabilidad oficial.
