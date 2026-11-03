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
| [backlog/](backlog/README.md) | Backlog BL-001 a BL-058 y sus consolidados |
| [.claude/skills/encontrar-prospectos/](.claude/skills/encontrar-prospectos/SKILL.md) | Skill de Claude Code `/encontrar-prospectos`: ejecuta la guía de `prospectos/AGENTS.md` por lotes, con plantillas de registro y lote, y un script que revisa `prospectos/REGISTRO.md` e importa listas. Guarda los resultados en `prospectos/` |
| [embudos/](embudos/AGENTS.md) | Embudos de venta en borrador: guía (`AGENTS.md`), registro `EMBUDOS.md` y una carpeta por embudo (`E01-…/`) con el documento, las entradas y la salida de la calculadora |
| [.claude/skills/embudos-de-venta/](.claude/skills/embudos-de-venta/SKILL.md) | Skill de Claude Code `/embudos-de-venta`: diseña, calcula y audita embudos de venta. Crea la carpeta de cada embudo con `nuevo_embudo.py`, hace las cuentas con `calcular_embudo.py` y guarda los resultados en `embudos/` |

## El backlog

El [backlog](backlog/README.md) tiene 58 ítems (BL-001 a BL-058): acciones, tareas, experimentos, requisitos, errores e ideas. Cada uno es un archivo `backlog/BL-*.md` con metadatos (prioridad, impacto, dependencias, responsable propuesto y criterios de aceptación) y un cuerpo con hechos y supuestos.

El PR #3 (en revisión) propone sumar BL-059 a BL-061 y ajustar criterios con métricas en dinero y atribución.

- **Orden:** por impacto y prioridad, respetando dependencias, agrupado por semanas (desde el 2 de noviembre de 2026). El campo `order` indica el paso.
- **Vista por semanas:** [backlog/README.md](backlog/README.md).
- **Todas las tareas en un archivo:** [backlog/TODAS-LAS-TAREAS.md](backlog/TODAS-LAS-TAREAS.md) (con enlaces y fuentes).
- **Versión limpia:** [backlog/TODAS-LAS-TAREAS-SIN-REFERENCIAS.md](backlog/TODAS-LAS-TAREAS-SIN-REFERENCIAS.md) (sin enlaces ni fuentes).

Los consolidados se generan a partir de los `BL-*.md`: si se edita una tarea, hay que regenerarlos.

### Prioridades actuales

1. **BL-001 — Seguridad:** cambiar las contraseñas expuestas y cerrar Odoo al público. BL-052 (copias de seguridad) va justo después.
2. **BL-002 — Acuerdo de cobro y línea base:** definir cómo se cobra; un cobro por resultados requiere registrar el origen de las ventas (BL-021).
3. **BL-004 / BL-005 — Línea base:** kilos, clientes y recompra desde el Excel de ventas, y precios y unidades confirmados para poder hablar de dinero.
4. **BL-007 a BL-010 — Entender el negocio:** entrevistas con Omar y distribuidores, seguir un pedido de punta a punta, fallas de máquinas y verificación de prospectos.
5. **BL-044 — Hipótesis antes de experimentar:** criterios y gasto máximo escritos antes de cada experimento.
6. **Propuesto en el PR #3:** BL-059 (auditoría de consultas de WhatsApp antes de automatizar), BL-060 (recuperar clientes que dejaron de comprar) y BL-061 (bitácora del caso).

### Qué sabemos y qué no

- **Conocido:** hay ventas registradas de julio a octubre de 2026 en kilos, por cliente y producto; hay compras grandes de criadores; hay distribuidores publicados en Bogotá y alrededores.
- **Desconocido por ahora:** precios confirmados por canal y unidad, ventas en COP, costos, márgenes, costo de adquisición, recompra en dinero, volumen de consultas por WhatsApp y capacidad de producción disponible.

Ningún documento del repo debe presentar como dato algo que todavía es hipótesis.

## Skills de Claude Code

- [`embudos-de-venta`](.claude/skills/embudos-de-venta/SKILL.md): diseña, calcula y audita embudos de venta (WhatsApp, recompra, e-commerce, B2B, servicios). Guarda cada embudo en `embudos/E01-…/` y lo registra en `embudos/EMBUDOS.md`. Claude Code la usa sola cuando se le pide un embudo o funnel en este repositorio. Los números que produce son supuestos hasta que se midan.

## Skills de Codex

Codex encuentra las tres skills en `.agents/skills/`. Cada carpeta es un enlace simbólico a su versión en `.claude/skills/`, así ambos agentes usan las mismas instrucciones, scripts, referencias y plantillas.

| Skill | Para qué sirve | Ejemplo en Codex |
|---|---|---|
| [`analisis-competencia`](.claude/skills/analisis-competencia/SKILL.md) | Compara competidores, precios, ofertas y posicionamiento con evidencia | `$analisis-competencia compara las alternativas de Canívoros en Bogotá` |
| [`embudos-de-venta`](.claude/skills/embudos-de-venta/SKILL.md) | Diseña, calcula y audita embudos de adquisición y recompra | `$embudos-de-venta diseña un embudo de WhatsApp y recompra para Canívoros` |
| [`encontrar-prospectos`](.claude/skills/encontrar-prospectos/SKILL.md) | Busca y verifica posibles distribuidores por lotes de hasta 10 negocios | `$encontrar-prospectos busca 10 tiendas de alimento natural en Usaquén` |

Abre Codex dentro del repositorio, en una rama que incluya estos cambios. Puedes pedir una skill con `$nombre` o dejar que Codex la elija según el pedido. Las reglas de `AGENTS.md` y las guías de cada carpeta siguen aplicando; los resultados se guardan en `competencia/`, `embudos/` y `prospectos/`.

Los enlaces requieren un checkout que admita enlaces simbólicos. En Windows, habilita el soporte de enlaces simbólicos antes de clonar (por ejemplo, con el Modo de desarrollador y `git clone -c core.symlinks=true <url>`). Si Git materializa el enlace como un archivo de texto, Codex no encontrará la skill.

Para actualizar una skill, edita su carpeta original en `.claude/skills/`. Para agregar otra, crea su carpeta allí y un enlace del mismo nombre en `.agents/skills/`.

## Cómo contribuir

- **Ramas:** el trabajo se hace en `backlog` (o en una rama derivada como `docs/...`) del fork `quemasandy/canivoros` y se propone por PR hacia `develop` de `segodimor2d2/canivoros`.
- **PR anteriores:** #1 (backlog inicial) y #2 (consolidados) ya están unidos; #3 (ajustes de la auditoría Growth Partner) está en revisión; #4 se cerró por mezclar cambios.
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
