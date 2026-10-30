# Backlog Canívoros / Growth Partner — orden de ejecución

> 📄 Contenido completo de todas las tareas (BL-001 a BL-058) en un solo archivo: [TODAS-LAS-TAREAS.md](TODAS-LAS-TAREAS.md)

Ordenado por pasos lógicos: primero lo de mayor impacto y prioridad; cada ítem va después de sus dependencias. Las claves BL no cambian; el campo `order` del front-matter indica el paso. Responsables, semanas y esfuerzo son **propuestas** (Andrés ~4 h/semana; Sebastián la parte técnica).

Esfuerzo: S ≈ 1–2 h, M ≈ 3–6 h, L > 6 h.


## Semana 1 (2–8 nov 2026) — Seguridad, acuerdo y línea base

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 1 | [BL-001](BL-001-cambiar-contrasenas-expuestas-y-cerrar-odoo-al-pub.md) | Acción | Cambiar contraseñas expuestas y cerrar Odoo al público | Highest | Alto | — | Sebastián | S |
| 2 | [BL-002](BL-002-llamada-andressebastian-linea-base-de-ventas-y-acu.md) | Acción | Llamada Andrés–Sebastián: línea base de ventas y acuerdo de cobro | Highest | Alto | — | Andrés + Sebastián | S |
| 3 | [BL-052](BL-052-copias-de-seguridad-diarias-probadas.md) | Requisito | Copias de seguridad diarias probadas | Highest | Alto | BL-001 | Sebastián | S |
| 4 | [BL-004](BL-004-calcular-linea-base-con-ventas-canivoros-2026-xlsx.md) | Tarea | Calcular línea base con ventas_canivoros_2026.xlsx | Highest | Alto | — | Andrés | M |
| 5 | [BL-005](BL-005-confirmar-precios-unidades-y-catalogo-definitivo.md) | Tarea | Confirmar precios, unidades y catálogo definitivo | High | Alto | — | Sebastián | S |
| 6 | [BL-003](BL-003-crear-tablero-semanal-y-usar-este-backlog.md) | Tarea | Crear tablero semanal y usar este backlog | High | Medio | — | Andrés | S |

## Semana 2 (9–15 nov) — Entender el negocio desde adentro

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 7 | [BL-006](BL-006-guion-de-entrevistas-voz-del-cliente.md) | Historia | Guion de entrevistas: voz del cliente | High | Alto | — | Andrés | S |
| 8 | [BL-007](BL-007-entrevistar-a-omar-y-a-23-distribuidores-actuales.md) | Tarea | Entrevistar a Omar y a 2–3 distribuidores actuales | High | Alto | BL-006 | Sebastián | M |
| 9 | [BL-008](BL-008-seguir-un-pedido-completo-de-punta-a-punta.md) | Tarea | Seguir un pedido completo de punta a punta | High | Alto | — | Sebastián | M |
| 10 | [BL-009](BL-009-registrar-fallas-de-maquinas-y-cuarto-frio.md) | Tarea | Registrar fallas de máquinas y cuarto frío | High | Alto | — | Omar/Canívoros | S |
| 11 | [BL-036](BL-036-medir-la-capacidad-de-produccion-disponible.md) | Tarea | Medir la capacidad de producción disponible | Highest | Alto | BL-009 | Sebastián | S |
| 12 | [BL-035](BL-035-validar-los-distribuidores-publicados-en-el-sitio.md) | Tarea | Validar los distribuidores publicados en el sitio | High | Alto | — | Omar/Canívoros | S |
| 13 | [BL-010](BL-010-verificar-la-lista-de-134-prospectos-de-bogota.md) | Tarea | Verificar la lista de 134 prospectos de Bogotá | High | Alto | — | Andrés | M |
| 14 | [BL-038](BL-038-responder-las-12-preguntas-pendientes-de-compras-y.md) | Tarea | Responder las 12 preguntas pendientes de compras y recepción | Medium | Medio | — | Sebastián | S |
| 15 | [BL-044](BL-044-registrar-hipotesis-y-criterios-de-decision-antes.md) | Tarea | Registrar hipótesis y criterios de decisión antes de cada experimento | Medium | Medio | — | Andrés | S |

## Semana 3 (16–22 nov) — Datos, sistema y capacidad

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 16 | [BL-057](BL-057-listas-de-precios-por-canal-y-unidad-en-odoo.md) | Requisito | Listas de precios por canal y unidad en Odoo | High | Alto | BL-005 | Sebastián | M |
| 17 | [BL-047](BL-047-plantilla-unica-para-registrar-ventas.md) | Mejora | Plantilla única para registrar ventas | High | Alto | BL-005 | Sebastián | S |
| 18 | [BL-053](BL-053-usuarios-por-funcion-en-odoo.md) | Requisito | Usuarios por función en Odoo | High | Medio | BL-001 | Sebastián | S |
| 19 | [BL-013](BL-013-tablero-semanal-de-indicadores.md) | Tarea | Tablero semanal de indicadores | Medium | Alto | BL-004 | Andrés | M |
| 20 | [BL-048](BL-048-productos-inactivos-no-aparecen-en-odoo.md) | Error | Productos inactivos no aparecen en Odoo | Medium | Medio | BL-005 | Sebastián | S |
| 21 | [BL-011](BL-011-definir-el-primer-sistema-minimo-de-datos-en-odoo.md) | Historia | Definir el primer sistema mínimo de datos en Odoo | Medium | Medio | BL-005, BL-008, BL-053 | Sebastián | M |
| 22 | [BL-049](BL-049-guardar-precio-y-costo-aplicados-en-cada-venta.md) | Requisito | Guardar precio y costo aplicados en cada venta | High | Alto | BL-011, BL-057 | Sebastián | S |
| 23 | [BL-040](BL-040-ordenar-cobros-y-cartera.md) | Tarea | Ordenar cobros y cartera | High | Alto | BL-011 | Sebastián | S |
| 24 | [BL-037](BL-037-registrar-proveedores-y-recepcion-de-materia-prima.md) | Historia | Registrar proveedores y recepción de materia prima | Medium | Alto | BL-011 | Sebastián | M |
| 25 | [BL-055](BL-055-registro-de-produccion-con-receta-merma-y-costo.md) | Requisito | Registro de producción con receta, merma y costo | Medium | Alto | BL-037 | Sebastián | M |
| 26 | [BL-054](BL-054-inventario-de-producto-terminado-por-lote.md) | Requisito | Inventario de producto terminado por lote | Medium | Alto | BL-011, BL-055 | Sebastián | M |
| 27 | [BL-025](BL-025-costo-y-rentabilidad-por-producto.md) | Tarea | Costo y rentabilidad por producto | Medium | Alto | BL-005, BL-055 | Sebastián | M |
| 28 | [BL-050](BL-050-devoluciones-y-cancelaciones-sin-borrar-la-venta.md) | Requisito | Devoluciones y cancelaciones sin borrar la venta | Medium | Medio | BL-011 | Sebastián | S |
| 29 | [BL-056](BL-056-codigo-de-odoo-en-git-y-pruebas-en-local.md) | Mejora | Código de Odoo en Git y pruebas en local | Medium | Medio | BL-052 | Sebastián | S |
| 30 | [BL-041](BL-041-confirmar-la-guia-de-raciones-por-peso-de-perro.md) | Tarea | Confirmar la guía de raciones por peso de perro | Medium | Medio | — | Omar/Canívoros | S |
| 31 | [BL-014](BL-014-matriz-de-microzonas-para-el-piloto-en-bogota.md) | Tarea | Matriz de microzonas para el piloto en Bogotá | Medium | Medio | BL-007, BL-010 | Andrés | S |
| 32 | [BL-015](BL-015-comparar-812-alternativas-de-la-competencia.md) | Tarea | Comparar 8–12 alternativas de la competencia | Medium | Medio | — | Andrés | S |

## Semana 4 (23–29 nov) — Experimentos de venta

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 33 | [BL-016](BL-016-revisar-afirmaciones-de-marca-y-el-mensaje-sin-sub.md) | Tarea | Revisar afirmaciones de marca y el mensaje 'sin subproductos' | High | Alto | — | Sebastián | S |
| 34 | [BL-012](BL-012-prospeccion-mayorista-10-tiendas-de-alimento-natur.md) | Experimento | Prospección mayorista: 10 tiendas de alimento natural | High | Alto | BL-010, BL-005, BL-035 | Hermano de Sebastián + Omar | M |
| 35 | [BL-058](BL-058-permiso-de-datos-y-comunicaciones-de-clientes.md) | Requisito | Permiso de datos y comunicaciones de clientes | High | Medio | — | Andrés | S |
| 36 | [BL-043](BL-043-programa-para-criadores-y-clientes-de-alto-volumen.md) | Experimento | Programa para criadores y clientes de alto volumen | Medium | Alto | BL-004 | Omar/Canívoros + Andrés (datos) | M |
| 37 | [BL-051](BL-051-evitar-pedidos-duplicados-en-integraciones.md) | Requisito | Evitar pedidos duplicados en integraciones | Medium | Medio | BL-011 | Sebastián | S |
| 38 | [BL-019](BL-019-quick-win-marca-personal-de-omar-captura-de-leads.md) | Experimento | Quick win: marca personal de Omar + captura de leads | Medium | Alto | BL-011, BL-016, BL-058, BL-051 | Sebastián + Omar | M |
| 39 | [BL-020](BL-020-comparar-dos-mensajes-horneado-vs-facilidad-de-uso.md) | Experimento | Comparar dos mensajes: horneado vs facilidad de uso | Medium | Medio | BL-016, BL-019 | Andrés | S |
| 40 | [BL-022](BL-022-recordatorio-de-reposicion-a-clientes.md) | Experimento | Recordatorio de reposición a clientes | Medium | Medio | BL-004, BL-058, BL-041 | Sebastián | M |
| 41 | [BL-023](BL-023-presentacion-de-entrada.md) | Experimento | Presentación de entrada | Low | Medio | BL-005 | Omar/Canívoros | M |

## Semana 5 (30 nov–6 dic) — Oferta y diagnóstico

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 42 | [BL-017](BL-017-empaquetar-el-diagnostico-de-crecimiento-150300-us.md) | Historia | Empaquetar el Diagnóstico de crecimiento (150–300 USD) | High | Alto | BL-002, BL-008 | Andrés | M |
| 43 | [BL-018](BL-018-ofrecer-el-diagnostico-a-5-pymes.md) | Experimento | Ofrecer el diagnóstico a 5 pymes | High | Alto | BL-017 | Andrés | M |
| 44 | [BL-030](BL-030-definir-oferta-de-growth-partner-y-diferencial.md) | Tarea | Definir oferta de Growth Partner y diferencial | Medium | Medio | — | Andrés + Sebastián | S |
| 45 | [BL-029](BL-029-nombre-provisorio-dominio-y-subdominio.md) | Tarea | Nombre provisorio, dominio y subdominio | Medium | Bajo | — | Sebastián | S |

## Semana 6 (7–13 dic) — Medición y cobro

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 46 | [BL-021](BL-021-medir-ventas-con-su-origen-para-poder-cobrar-porce.md) | Tarea | Medir ventas con su origen para poder cobrar porcentaje | High | Alto | BL-004, BL-011, BL-049 | Sebastián | M |
| 47 | [BL-039](BL-039-buscar-nuevos-proveedores-de-subproductos.md) | Experimento | Buscar nuevos proveedores de subproductos | Medium | Alto | BL-036 | Omar/Canívoros + Andrés (investigación) | M |
| 48 | [BL-024](BL-024-aplicar-qfd-a-canivoros.md) | Tarea | Aplicar QFD a Canívoros | Medium | Medio | BL-007 | Sebastián | M |
| 49 | [BL-042](BL-042-revisar-el-wordpress-y-decidir-si-sirve-como-tiend.md) | Tarea | Revisar el WordPress y decidir si sirve como tienda | Low | Medio | BL-005 | Sebastián | S |

## Semana 7 (14–20 dic) — Crecimiento y nichos

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 50 | [BL-028](BL-028-decidir-como-crecer-en-bogota.md) | Tarea | Decidir cómo crecer en Bogotá | Medium | Alto | BL-013, BL-012 | Andrés + Sebastián | S |
| 51 | [BL-026](BL-026-gativoros-introduccion-alimentaria-en-veterinarias.md) | Experimento | Gatívoros: introducción alimentaria en veterinarias | Low | Medio | BL-025 | Omar/Canívoros + Sebastián | M |
| 52 | [BL-027](BL-027-monitoreo-de-la-maquina.md) | Experimento | Monitoreo de la máquina | Low | Medio | BL-009 | Sebastián | L |
| 53 | [BL-045](BL-045-plan-de-negocio-corto-de-la-agencia-growth-partner.md) | Historia | Plan de negocio corto de la agencia Growth Partner | Low | Medio | BL-030, BL-017 | Sebastián + Andrés | M |
| 54 | [BL-046](BL-046-explorar-el-cluster-de-bienestar-animal-de-la-ccb.md) | Idea | Explorar el Clúster de Bienestar Animal de la CCB | Low | Bajo | — | Andrés | S |

## Sin semana (ideas en pausa) — Ideas en pausa

| # | Clave | Tipo | Título | Prioridad | Impacto | Depende de | Responsable | Esfuerzo |
|---|---|---|---|---|---|---|---|---|
| 55 | [BL-031](BL-031-estacion-de-trabajo-vr-con-celular.md) | Idea | Estación de trabajo VR con celular | Low | Bajo | — | Sebastián | M |
| 56 | [BL-032](BL-032-app-para-concursos-de-perros.md) | Idea | App para concursos de perros | Low | Bajo | — | Sebastián | M |
| 57 | [BL-033](BL-033-asistente-de-ia-local-con-notas.md) | Idea | Asistente de IA local con notas | Low | Bajo | — | Sebastián | M |
| 58 | [BL-034](BL-034-extensiones-de-chrome-propias.md) | Idea | Extensiones de Chrome propias | Low | Bajo | — | Sebastián | M |

## Fuentes
- Rama `develop`/`backlog`: CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md, CANIVOROS-REFERENCIA-EMPRESA.md, erp.md, pasos_sysmkt.md, metodologias_analisis_competitivo.md, guías ES, QFD.pdf, ventas_canivoros_2026.xlsx.
- canivoros-view `master`: problemas.md.
- Informe ejecutivo del chat (29/10/2026), prospectos_bogota.xlsx, precios_competencia_bogota.xlsx.

No contiene contraseñas ni secretos.
