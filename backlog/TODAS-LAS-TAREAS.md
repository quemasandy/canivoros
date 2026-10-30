# Backlog Canívoros — todas las tareas (BL-001 a BL-058)

Archivo consolidado con el contenido completo de cada tarea individual, en orden de clave. Los archivos `BL-*.md` siguen siendo la fuente de cada ítem; el orden de ejecución está en [README.md](README.md). Responsables, semanas y esfuerzo son **propuestas**.

## Índice

- [BL-001 · Cambiar contraseñas expuestas y cerrar Odoo al público](#bl-001)
- [BL-002 · Llamada Andrés–Sebastián: línea base de ventas y acuerdo de cobro](#bl-002)
- [BL-003 · Crear tablero semanal y usar este backlog](#bl-003)
- [BL-004 · Calcular línea base con ventas_canivoros_2026.xlsx](#bl-004)
- [BL-005 · Confirmar precios, unidades y catálogo definitivo](#bl-005)
- [BL-006 · Guion de entrevistas: voz del cliente](#bl-006)
- [BL-007 · Entrevistar a Omar y a 2–3 distribuidores actuales](#bl-007)
- [BL-008 · Seguir un pedido completo de punta a punta](#bl-008)
- [BL-009 · Registrar fallas de máquinas y cuarto frío](#bl-009)
- [BL-010 · Verificar la lista de 134 prospectos de Bogotá](#bl-010)
- [BL-011 · Definir el primer sistema mínimo de datos en Odoo](#bl-011)
- [BL-012 · Prospección mayorista: 10 tiendas de alimento natural](#bl-012)
- [BL-013 · Tablero semanal de indicadores](#bl-013)
- [BL-014 · Matriz de microzonas para el piloto en Bogotá](#bl-014)
- [BL-015 · Comparar 8–12 alternativas de la competencia](#bl-015)
- [BL-016 · Revisar afirmaciones de marca y el mensaje 'sin subproductos](#bl-016)
- [BL-017 · Empaquetar el Diagnóstico de crecimiento (150–300 USD)](#bl-017)
- [BL-018 · Ofrecer el diagnóstico a 5 pymes](#bl-018)
- [BL-019 · Quick win: marca personal de Omar + captura de leads](#bl-019)
- [BL-020 · Comparar dos mensajes: horneado vs facilidad de uso](#bl-020)
- [BL-021 · Medir ventas con su origen para poder cobrar porcentaje](#bl-021)
- [BL-022 · Recordatorio de reposición a clientes](#bl-022)
- [BL-023 · Presentación de entrada](#bl-023)
- [BL-024 · Aplicar QFD a Canívoros](#bl-024)
- [BL-025 · Costo y rentabilidad por producto](#bl-025)
- [BL-026 · Gatívoros: introducción alimentaria en veterinarias](#bl-026)
- [BL-027 · Monitoreo de la máquina](#bl-027)
- [BL-028 · Decidir cómo crecer en Bogotá](#bl-028)
- [BL-029 · Nombre provisorio, dominio y subdominio](#bl-029)
- [BL-030 · Definir oferta de Growth Partner y diferencial](#bl-030)
- [BL-031 · Estación de trabajo VR con celular](#bl-031)
- [BL-032 · App para concursos de perros](#bl-032)
- [BL-033 · Asistente de IA local con notas](#bl-033)
- [BL-034 · Extensiones de Chrome propias](#bl-034)
- [BL-035 · Validar los distribuidores publicados en el sitio](#bl-035)
- [BL-036 · Medir la capacidad de producción disponible](#bl-036)
- [BL-037 · Registrar proveedores y recepción de materia prima](#bl-037)
- [BL-038 · Responder las 12 preguntas pendientes de compras y recepción](#bl-038)
- [BL-039 · Buscar nuevos proveedores de subproductos](#bl-039)
- [BL-040 · Ordenar cobros y cartera](#bl-040)
- [BL-041 · Confirmar la guía de raciones por peso de perro](#bl-041)
- [BL-042 · Revisar el WordPress y decidir si sirve como tienda](#bl-042)
- [BL-043 · Programa para criadores y clientes de alto volumen](#bl-043)
- [BL-044 · Registrar hipótesis y criterios de decisión antes de cada experimento](#bl-044)
- [BL-045 · Plan de negocio corto de la agencia Growth Partner](#bl-045)
- [BL-046 · Explorar el Clúster de Bienestar Animal de la CCB](#bl-046)
- [BL-047 · Plantilla única para registrar ventas](#bl-047)
- [BL-048 · Productos inactivos no aparecen en Odoo](#bl-048)
- [BL-049 · Guardar precio y costo aplicados en cada venta](#bl-049)
- [BL-050 · Devoluciones y cancelaciones sin borrar la venta](#bl-050)
- [BL-051 · Evitar pedidos duplicados en integraciones](#bl-051)
- [BL-052 · Copias de seguridad diarias probadas](#bl-052)
- [BL-053 · Usuarios por función en Odoo](#bl-053)
- [BL-054 · Inventario de producto terminado por lote](#bl-054)
- [BL-055 · Registro de producción con receta, merma y costo](#bl-055)
- [BL-056 · Código de Odoo en Git y pruebas en local](#bl-056)
- [BL-057 · Listas de precios por canal y unidad en Odoo](#bl-057)
- [BL-058 · Permiso de datos y comunicaciones de clientes](#bl-058)

---

<a id="bl-001"></a>
## BL-001 · Cambiar contraseñas expuestas y cerrar Odoo al público

Archivo: [BL-001-cambiar-contrasenas-expuestas-y-cerrar-odoo-al-pub.md](BL-001-cambiar-contrasenas-expuestas-y-cerrar-odoo-al-pub.md)

```yaml
key: BL-001
issue_type: Acción
summary: Cambiar contraseñas expuestas y cerrar Odoo al público
description: Cambiar las claves del panel de hosting, del acceso root al VPS y del usuario de Odoo, que se compartieron en el chat. Activar acceso por llave SSH, desactivar login por contraseña y cerrar el puerto 8069 o ponerlo detrás de HTTPS/Tailscale.
priority: Highest
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- seguridad
- infra
dependencies: []
acceptance_criteria:
- Las tres claves fueron cambiadas (sin escribirlas en el repo ni en el chat)
- El VPS solo acepta llave SSH
- Odoo no responde en http://IP:8069 desde internet sin VPN o HTTPS
- Nunca más se comparten claves por WhatsApp; se usa un gestor de contraseñas
sources:
- chat 26/10 y 27/10
- informe ejecutivo, sección E
order: 1
```

Cambiar las claves del panel de hosting, del acceso root al VPS y del usuario de Odoo, que se compartieron en el chat. Activar acceso por llave SSH, desactivar login por contraseña y cerrar el puerto 8069 o ponerlo detrás de HTTPS/Tailscale.

### Hechos
Las claves se pegaron en texto plano en el chat; Odoo estaba accesible por IP pública y HTTP.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-002"></a>
## BL-002 · Llamada Andrés–Sebastián: línea base de ventas y acuerdo de cobro

Archivo: [BL-002-llamada-andressebastian-linea-base-de-ventas-y-acu.md](BL-002-llamada-andressebastian-linea-base-de-ventas-y-acu.md)

```yaml
key: BL-002
issue_type: Acción
summary: 'Llamada Andrés–Sebastián: línea base de ventas y acuerdo de cobro'
description: 'Llamada de 60 min para fijar: (1) ventas actuales por mes de Canívoros, (2) cómo se cobra (porcentaje, tarifa fija o mixto) y desde cuándo, (3) reparto entre Andrés y Sebastián, (4) preguntas para Omar y distribuidores. Dejarlo por escrito en el repo (sin datos sensibles).'
priority: Highest
status: Backlog
assignee: Andrés + Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- acuerdo
- cobro
- growth-partner
dependencies: []
acceptance_criteria:
- Existe un documento de 1 página con el acuerdo propuesto
- Se definió la línea base inicial (o se decide usar BL-004)
- Queda acordado quién presenta la propuesta a la prima
sources:
- informe ejecutivo, F
- erp.md §7 (acuerdo pendiente)
order: 2
```

Llamada de 60 min para fijar: (1) ventas actuales por mes de Canívoros, (2) cómo se cobra (porcentaje, tarifa fija o mixto) y desde cuándo, (3) reparto entre Andrés y Sebastián, (4) preguntas para Omar y distribuidores. Dejarlo por escrito en el repo (sin datos sensibles).

### Hechos
El acuerdo con la prima es solo verbal; erp.md dice que no hay acuerdo económico cerrado.

### Supuestos
Que la prima acepte un esquema por resultados medibles.

---

<a id="bl-003"></a>
## BL-003 · Crear tablero semanal y usar este backlog

Archivo: [BL-003-crear-tablero-semanal-y-usar-este-backlog.md](BL-003-crear-tablero-semanal-y-usar-este-backlog.md)

```yaml
key: BL-003
issue_type: Tarea
summary: Crear tablero semanal y usar este backlog
description: 'Elegir un solo tablero (Kanban de Odoo, Taiga o Plane) e importar estos ítems. Revisión semanal de 30 min: qué se hizo, qué sigue.'
priority: High
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Medio
sprint: Semana 1 (2–8 nov 2026)
labels:
- organizacion
dependencies: []
acceptance_criteria:
- Todos los ítems BL están en el tablero con su semana
- Hay una revisión semanal agendada
sources:
- chat 27–28/10 (Jira, Taiga, Plane, Kanboard)
order: 6
```

Elegir un solo tablero (Kanban de Odoo, Taiga o Plane) e importar estos ítems. Revisión semanal de 30 min: qué se hizo, qué sigue.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-004"></a>
## BL-004 · Calcular línea base con ventas_canivoros_2026.xlsx

Archivo: [BL-004-calcular-linea-base-con-ventas-canivoros-2026-xlsx.md](BL-004-calcular-linea-base-con-ventas-canivoros-2026-xlsx.md)

```yaml
key: BL-004
issue_type: Tarea
summary: Calcular línea base con ventas_canivoros_2026.xlsx
description: El repo ya tiene ventas de julio a octubre 2026 (hojas JULIO, AGOSTO, SEPT., OCT.) por cliente, fecha y producto. Limpiar nombres de cliente, unificar unidades (lb/kg), separar cliente final, almacén/distribuidor y criador, y sacar kilos por mes, por producto y por tipo de cliente, más recompra (clientes que repiten).
priority: Highest
status: Backlog
assignee: Andrés (propuesta)
effort: M
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- datos
- linea-base
- canivoros
dependencies: []
acceptance_criteria:
- Tabla resumen kilos/mes por producto y por tipo de cliente
- Número de clientes únicos y % que repite en el periodo
- Lista de dudas de datos (unidades, filas sin fecha) para Sara/la prima
- Se marca qué es dato y qué es estimado
sources:
- 'develop: ventas_canivoros_2026.xlsx'
order: 4
```

El repo ya tiene ventas de julio a octubre 2026 (hojas JULIO, AGOSTO, SEPT., OCT.) por cliente, fecha y producto. Limpiar nombres de cliente, unificar unidades (lb/kg), separar cliente final, almacén/distribuidor y criador, y sacar kilos por mes, por producto y por tipo de cliente, más recompra (clientes que repiten).

### Hechos
El archivo tiene registros jul–oct 2026 sin precios.

### Supuestos
Hacen falta precios por canal para convertir kilos a dinero (BL-005).

---

<a id="bl-005"></a>
## BL-005 · Confirmar precios, unidades y catálogo definitivo

Archivo: [BL-005-confirmar-precios-unidades-y-catalogo-definitivo.md](BL-005-confirmar-precios-unidades-y-catalogo-definitivo.md)

```yaml
key: BL-005
issue_type: Tarea
summary: Confirmar precios, unidades y catálogo definitivo
description: 'Resolver con la prima o Sara Ramírez los 5 puntos de erp.md §9: precios y unidades por producto y canal, catálogo y presentaciones, regla de venta mínima (40 kg vs paquetes de 1,5 kg), programa de facturación usado y responsables de registrar.'
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- datos
- odoo
- canivoros
dependencies: []
acceptance_criteria:
- Lista de precios por producto y canal (cliente, distribuidor, criador)
- Unidades unificadas (kg o lb)
- Catálogo cargado igual en Odoo
sources:
- 'develop: erp.md §3 y §9'
order: 5
```

Resolver con la prima o Sara Ramírez los 5 puntos de erp.md §9: precios y unidades por producto y canal, catálogo y presentaciones, regla de venta mínima (40 kg vs paquetes de 1,5 kg), programa de facturación usado y responsables de registrar.

### Hechos
El precio de cerdo a distribuidor ya fue corregido a 3.500 COP (problemas.md).

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-006"></a>
## BL-006 · Guion de entrevistas: voz del cliente

Archivo: [BL-006-guion-de-entrevistas-voz-del-cliente.md](BL-006-guion-de-entrevistas-voz-del-cliente.md)

```yaml
key: BL-006
issue_type: Historia
summary: 'Guion de entrevistas: voz del cliente'
description: 'Preparar guion corto para Omar, 2–3 distribuidores y clientes, usando la guía de investigación del repo (guion de necesidad: qué compran, cuánto gastan, por qué eligen, qué les impide cambiar, recompra). Preguntar antes de mostrar Canívoros.'
priority: High
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- investigacion
- voz-del-cliente
dependencies: []
acceptance_criteria:
- Guion de máx. 10 preguntas para cliente final y otro para tienda
- Plantilla para registrar respuestas (hoja o Odoo)
sources:
- 'develop: GuiaPesquisaProdutosServicosES.md §9'
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (entrevistas)
order: 7
```

Preparar guion corto para Omar, 2–3 distribuidores y clientes, usando la guía de investigación del repo (guion de necesidad: qué compran, cuánto gastan, por qué eligen, qué les impide cambiar, recompra). Preguntar antes de mostrar Canívoros.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-007"></a>
## BL-007 · Entrevistar a Omar y a 2–3 distribuidores actuales

Archivo: [BL-007-entrevistar-a-omar-y-a-23-distribuidores-actuales.md](BL-007-entrevistar-a-omar-y-a-23-distribuidores-actuales.md)

```yaml
key: BL-007
issue_type: Tarea
summary: Entrevistar a Omar y a 2–3 distribuidores actuales
description: 'Entrevistas con Omar (vende y distribuye) y distribuidores como Manimal, Sankatin o Terranova: rotación, pedido mínimo, margen requerido, quejas de clientes, reposición.'
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- investigacion
- voz-del-cliente
- canivoros
dependencies:
- BL-006
acceptance_criteria:
- Mínimo 3 entrevistas registradas
- 'Resumen de 1 página: problemas y objeciones repetidas'
- Hechos separados de opiniones
sources:
- chat 29/10
- 'plan Bogotá: entrevistas con establecimientos'
order: 8
```

Entrevistas con Omar (vende y distribuye) y distribuidores como Manimal, Sankatin o Terranova: rotación, pedido mínimo, margen requerido, quejas de clientes, reposición.

### Hechos
Ver fuentes.

### Supuestos
Omar y los distribuidores aceptan conversar.

---

<a id="bl-008"></a>
## BL-008 · Seguir un pedido completo de punta a punta

Archivo: [BL-008-seguir-un-pedido-completo-de-punta-a-punta.md](BL-008-seguir-un-pedido-completo-de-punta-a-punta.md)

```yaml
key: BL-008
issue_type: Tarea
summary: Seguir un pedido completo de punta a punta
description: 'Documentar un pedido real: qué se pidió, qué se prometió, qué se produjo, qué se entregó y qué se cobró, con fechas y responsables. Sirve como mapa del flujo actual (service blueprint simple).'
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- procesos
- odoo
dependencies: []
acceptance_criteria:
- Diagrama del flujo (draw.io o Markdown) con herramientas usadas en cada paso
- Lista de puntos donde se pierde información
sources:
- 'canivoros-view: problemas.md ''Por dónde empezaría'' 2'
- 'metodologias: Service Blueprint'
order: 9
```

Documentar un pedido real: qué se pidió, qué se prometió, qué se produjo, qué se entregó y qué se cobró, con fechas y responsables. Sirve como mapa del flujo actual (service blueprint simple).

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-009"></a>
## BL-009 · Registrar fallas de máquinas y cuarto frío

Archivo: [BL-009-registrar-fallas-de-maquinas-y-cuarto-frio.md](BL-009-registrar-fallas-de-maquinas-y-cuarto-frio.md)

```yaml
key: BL-009
issue_type: Tarea
summary: Registrar fallas de máquinas y cuarto frío
description: 'Hoja simple para cada falla: fecha, equipo, duración, kilos afectados, costo y causa. Es el primer paso para decidir qué reparar primero.'
priority: High
status: Backlog
assignee: Omar/Canívoros (propuesta)
effort: S
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- produccion
- mantenimiento
dependencies: []
acceptance_criteria:
- Plantilla creada y entregada
- Al menos 4 semanas de registros antes de decidir inversiones
sources:
- problemas.md (máquinas y cuarto frío)
order: 10
```

Hoja simple para cada falla: fecha, equipo, duración, kilos afectados, costo y causa. Es el primer paso para decidir qué reparar primero.

### Hechos
La empresa identifica las máquinas como su mayor problema; el cuarto frío ya causó pérdidas sin cuantificar.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-010"></a>
## BL-010 · Verificar la lista de 134 prospectos de Bogotá

Archivo: [BL-010-verificar-la-lista-de-134-prospectos-de-bogota.md](BL-010-verificar-la-lista-de-134-prospectos-de-bogota.md)

```yaml
key: BL-010
issue_type: Tarea
summary: Verificar la lista de 134 prospectos de Bogotá
description: 'Revisar a mano o con 1–2 IA los 20–30 prospectos de encaje ''Alto'' más cercanos (Usaquén, Suba, Chapinero, noroccidente): que existan, teléfono, Instagram, marcas que venden.'
priority: High
status: Backlog
assignee: Andrés (propuesta)
effort: M
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- prospeccion
- bogota
dependencies: []
acceptance_criteria:
- 30 prospectos verificados con fuente y fecha
- Campos 'desconocido' reducidos en esos 30
- Cargados en el CRM con etapa 'Por contactar'
sources:
- prospectos_bogota.xlsx (25/10)
order: 13
```

Revisar a mano o con 1–2 IA los 20–30 prospectos de encaje 'Alto' más cercanos (Usaquén, Suba, Chapinero, noroccidente): que existan, teléfono, Instagram, marcas que venden.

### Hechos
La lista fue hecha con IA y tiene muchos campos desconocidos.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-011"></a>
## BL-011 · Definir el primer sistema mínimo de datos en Odoo

Archivo: [BL-011-definir-el-primer-sistema-minimo-de-datos-en-odoo.md](BL-011-definir-el-primer-sistema-minimo-de-datos-en-odoo.md)

```yaml
key: BL-011
issue_type: Historia
summary: Definir el primer sistema mínimo de datos en Odoo
description: 'Configurar solo lo que permita reconstruir un pedido: clientes, productos con precio por canal, pedidos, pagos y entregas. Nada de automatizaciones todavía.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- odoo
- datos
dependencies:
- BL-005
- BL-008
- BL-053
acceptance_criteria:
- Un pedido real se puede seguir de consulta a cobro en Odoo
- Ventas concilian con cobros de una semana
- Sara o la prima lo usan sin ayuda
sources:
- 'plan Bogotá: Qué sistematizar primero'
- erp.md §9
order: 21
```

Configurar solo lo que permita reconstruir un pedido: clientes, productos con precio por canal, pedidos, pagos y entregas. Nada de automatizaciones todavía.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-012"></a>
## BL-012 · Prospección mayorista: 10 tiendas de alimento natural

Archivo: [BL-012-prospeccion-mayorista-10-tiendas-de-alimento-natur.md](BL-012-prospeccion-mayorista-10-tiendas-de-alimento-natur.md)

```yaml
key: BL-012
issue_type: Experimento
summary: 'Prospección mayorista: 10 tiendas de alimento natural'
description: Contactar 10 tiendas que ya venden Pixie o BARF con una oferta mayorista clara (precio distribuidor, pedido mínimo, material y QR por tienda). Medir respuesta, pedidos y reposición.
priority: High
status: Backlog
assignee: Hermano de Sebastián + Omar (propuesta)
effort: M
impact: Alto
sprint: Semana 4 (23–29 nov)
labels:
- ventas
- b2b
- bogota
- experimento
dependencies:
- BL-010
- BL-005
- BL-035
acceptance_criteria:
- 10 tiendas contactadas y registradas en el CRM
- Tasa de respuesta y de pedido medida
- Al menos 1 reposición observada o razón de no compra registrada
sources:
- prospectos_bogota.xlsx
- 'plan Bogotá: Experimento 3 aliados locales'
order: 34
```

Contactar 10 tiendas que ya venden Pixie o BARF con una oferta mayorista clara (precio distribuidor, pedido mínimo, material y QR por tienda). Medir respuesta, pedidos y reposición.

### Hechos
Ver fuentes.

### Supuestos
Hipótesis: tiendas con clientes ya educados en natural compran más rápido que el consumidor final.

---

<a id="bl-013"></a>
## BL-013 · Tablero semanal de indicadores

Archivo: [BL-013-tablero-semanal-de-indicadores.md](BL-013-tablero-semanal-de-indicadores.md)

```yaml
key: BL-013
issue_type: Tarea
summary: Tablero semanal de indicadores
description: 'Hoja o tablero con: ventas netas, kilos, clientes nuevos, recompra 30/60 días, entregas a tiempo, fallas de máquina. Origen del cliente separado del canal de cierre.'
priority: Medium
status: Backlog
assignee: Andrés (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- datos
- kpi
dependencies:
- BL-004
acceptance_criteria:
- Se actualiza cada semana
- Indicadores definidos como en el plan Bogotá
sources:
- 'plan Bogotá: Tablero para tomar decisiones'
order: 19
```

Hoja o tablero con: ventas netas, kilos, clientes nuevos, recompra 30/60 días, entregas a tiempo, fallas de máquina. Origen del cliente separado del canal de cierre.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-014"></a>
## BL-014 · Matriz de microzonas para el piloto en Bogotá

Archivo: [BL-014-matriz-de-microzonas-para-el-piloto-en-bogota.md](BL-014-matriz-de-microzonas-para-el-piloto-en-bogota.md)

```yaml
key: BL-014
issue_type: Tarea
summary: Matriz de microzonas para el piloto en Bogotá
description: 'Puntuar 3–5 microzonas (p. ej. noroccidente/Manimal y sur/Bosa-Sankatin) con los criterios y pesos del plan: demanda, contribución, aliados, logística, competencia. Con evidencia, no intuición.'
priority: Medium
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- bogota
- estrategia
dependencies:
- BL-007
- BL-010
acceptance_criteria:
- Tabla con puntaje 0–100 y evidencia por criterio
- 2 zonas elegidas para el piloto
sources:
- 'plan Bogotá: Selección de zonas'
order: 31
```

Puntuar 3–5 microzonas (p. ej. noroccidente/Manimal y sur/Bosa-Sankatin) con los criterios y pesos del plan: demanda, contribución, aliados, logística, competencia. Con evidencia, no intuición.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-015"></a>
## BL-015 · Comparar 8–12 alternativas de la competencia

Archivo: [BL-015-comparar-812-alternativas-de-la-competencia.md](BL-015-comparar-812-alternativas-de-la-competencia.md)

```yaml
key: BL-015
issue_type: Tarea
summary: Comparar 8–12 alternativas de la competencia
description: Levantar precio por kg, presentación, entrega y mensaje de Pixie, Kanuto, VITA, BARF y premium secos. Base para precio y posicionamiento.
priority: Medium
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- competencia
- precios
dependencies: []
acceptance_criteria:
- Tabla con fecha y fuente de cada precio
- Precio por kg comparable
sources:
- prospectos_bogota.xlsx hoja Competencia
- 'plan Bogotá: Comparación de alternativas'
- metodologias_analisis_competitivo.md
order: 32
```

Levantar precio por kg, presentación, entrega y mensaje de Pixie, Kanuto, VITA, BARF y premium secos. Base para precio y posicionamiento.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-016"></a>
## BL-016 · Revisar afirmaciones de marca y el mensaje 'sin subproductos

Archivo: [BL-016-revisar-afirmaciones-de-marca-y-el-mensaje-sin-sub.md](BL-016-revisar-afirmaciones-de-marca-y-el-mensaje-sin-sub.md)

```yaml
key: BL-016
issue_type: Tarea
summary: Revisar afirmaciones de marca y el mensaje 'sin subproductos'
description: Listar afirmaciones del sitio y de la prima que requieren evidencia (salud, 'la mejor calidad', registro ICA, 'sin subproductos' vs materia prima de subproductos). Corregir antes de cualquier anuncio.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 4 (23–29 nov)
labels:
- marca
- persuasion-etica
dependencies: []
acceptance_criteria:
- 'Lista de afirmaciones con estado: soportada / quitar / reformular'
- Propuesta de texto corregido para el sitio
sources:
- erp.md §8
- CANIVOROS-REFERENCIA-EMPRESA.md
- informe ejecutivo
order: 33
```

Listar afirmaciones del sitio y de la prima que requieren evidencia (salud, 'la mejor calidad', registro ICA, 'sin subproductos' vs materia prima de subproductos). Corregir antes de cualquier anuncio.

### Hechos
La materia prima incluye cabezas de pollo, barriga de salmón y vísceras.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-017"></a>
## BL-017 · Empaquetar el Diagnóstico de crecimiento (150–300 USD)

Archivo: [BL-017-empaquetar-el-diagnostico-de-crecimiento-150300-us.md](BL-017-empaquetar-el-diagnostico-de-crecimiento-150300-us.md)

```yaml
key: BL-017
issue_type: Historia
summary: Empaquetar el Diagnóstico de crecimiento (150–300 USD)
description: 'Convertir lo hecho con Canívoros en un producto: entrevista, revisión de datos, mapa del flujo, 3 problemas principales y roadmap priorizado. Precio de entrada 150–300 USD. Incluye 1 página de oferta y caso Canívoros.'
priority: High
status: Backlog
assignee: Andrés (propuesta)
effort: M
impact: Alto
sprint: Semana 5 (30 nov–6 dic)
labels:
- growth-partner
- oferta
- diagnostico
dependencies:
- BL-002
- BL-008
acceptance_criteria:
- Documento de oferta de 1 página
- Plantilla de entregable (informe + roadmap)
- Precio y condiciones definidos
sources:
- informe ejecutivo D1
- pasos_sysmkt.md (Diagnóstico de procesos y sistemas)
order: 42
```

Convertir lo hecho con Canívoros en un producto: entrevista, revisión de datos, mapa del flujo, 3 problemas principales y roadmap priorizado. Precio de entrada 150–300 USD. Incluye 1 página de oferta y caso Canívoros.

### Hechos
Ver fuentes.

### Supuestos
Precio tomado de la referencia compartida el 28/10, no validado con clientes.

---

<a id="bl-018"></a>
## BL-018 · Ofrecer el diagnóstico a 5 pymes

Archivo: [BL-018-ofrecer-el-diagnostico-a-5-pymes.md](BL-018-ofrecer-el-diagnostico-a-5-pymes.md)

```yaml
key: BL-018
issue_type: Experimento
summary: Ofrecer el diagnóstico a 5 pymes
description: Andrés ofrece el diagnóstico pagado a 5 negocios (pymes) de su red de contactos. Medir cuántos aceptan una llamada y cuántos pagan.
priority: High
status: Backlog
assignee: Andrés (propuesta)
effort: M
impact: Alto
sprint: Semana 5 (30 nov–6 dic)
labels:
- ventas
- growth-partner
- experimento
dependencies:
- BL-017
acceptance_criteria:
- 5 ofertas hechas
- 'Resultado registrado: llamada sí/no, pago sí/no, objeción principal'
sources: []
order: 43
```

Andrés ofrece el diagnóstico pagado a 5 negocios (pymes) de su red de contactos. Medir cuántos aceptan una llamada y cuántos pagan.

### Hechos
Ver fuentes.

### Supuestos
Existen al menos 5 pymes contactables dispuestas a escuchar la oferta (por validar).

---

<a id="bl-019"></a>
## BL-019 · Quick win: marca personal de Omar + captura de leads

Archivo: [BL-019-quick-win-marca-personal-de-omar-captura-de-leads.md](BL-019-quick-win-marca-personal-de-omar-captura-de-leads.md)

```yaml
key: BL-019
issue_type: Experimento
summary: 'Quick win: marca personal de Omar + captura de leads'
description: 'Optimizar Instagram/TikTok de Omar (perros de concurso) y conectar WhatsApp/IG a un flujo: saludo, pedir datos, 2–3 preguntas para filtrar, pasar a humano. Registrar todo en el CRM.'
priority: Medium
status: Backlog
assignee: Sebastián + Omar (propuesta)
effort: M
impact: Alto
sprint: Semana 4 (23–29 nov)
labels:
- marketing
- whatsapp
- crm
- experimento
dependencies:
- BL-011
- BL-016
- BL-058
- BL-051
acceptance_criteria:
- Flujo activo con un número comercial único
- Leads registrados con origen
- 'Medición de 4 semanas: leads, leads calificados, ventas'
sources:
- chat 29/10
- 'plan Bogotá: definir número comercial principal'
order: 38
```

Optimizar Instagram/TikTok de Omar (perros de concurso) y conectar WhatsApp/IG a un flujo: saludo, pedir datos, 2–3 preguntas para filtrar, pasar a humano. Registrar todo en el CRM.

### Hechos
Ver fuentes.

### Supuestos
Omar acepta mostrarse y tiene tiempo para responder leads calificados.

---

<a id="bl-020"></a>
## BL-020 · Comparar dos mensajes: horneado vs facilidad de uso

Archivo: [BL-020-comparar-dos-mensajes-horneado-vs-facilidad-de-uso.md](BL-020-comparar-dos-mensajes-horneado-vs-facilidad-de-uso.md)

```yaml
key: BL-020
issue_type: Experimento
summary: 'Comparar dos mensajes: horneado vs facilidad de uso'
description: Mismo producto, zona y precio; dos mensajes. Registrar variante por contacto y medir compras.
priority: Medium
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- marketing
- experimento
dependencies:
- BL-016
- BL-019
acceptance_criteria:
- Dos variantes publicadas
- Registro de variante por lead
- Resultado tratado como indicio si hay pocas compras
sources:
- 'plan Bogotá: Experimento 2'
order: 39
```

Mismo producto, zona y precio; dos mensajes. Registrar variante por contacto y medir compras.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-021"></a>
## BL-021 · Medir ventas con su origen para poder cobrar porcentaje

Archivo: [BL-021-medir-ventas-con-su-origen-para-poder-cobrar-porce.md](BL-021-medir-ventas-con-su-origen-para-poder-cobrar-porce.md)

```yaml
key: BL-021
issue_type: Tarea
summary: Medir ventas con su origen para poder cobrar porcentaje
description: Asegurar que cada venta tenga origen (campaña, aliado, Omar, orgánico) y canal de cierre, comparable con la línea base. Es la condición para un cobro por resultados.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 6 (7–13 dic)
labels:
- datos
- cobro
- odoo
dependencies:
- BL-004
- BL-011
- BL-049
acceptance_criteria:
- Más del 80% de las ventas del mes con origen registrado
- Comparación mes actual vs línea base
sources:
- informe ejecutivo D3
- 'plan Bogotá: Tablero'
order: 46
```

Asegurar que cada venta tenga origen (campaña, aliado, Omar, orgánico) y canal de cierre, comparable con la línea base. Es la condición para un cobro por resultados.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-022"></a>
## BL-022 · Recordatorio de reposición a clientes

Archivo: [BL-022-recordatorio-de-reposicion-a-clientes.md](BL-022-recordatorio-de-reposicion-a-clientes.md)

```yaml
key: BL-022
issue_type: Experimento
summary: Recordatorio de reposición a clientes
description: Con permiso del cliente, enviar recordatorio antes de que se acabe el empaque (según peso y ración confirmada). Medir recompra y bajas.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- retencion
- experimento
dependencies:
- BL-004
- BL-058
- BL-041
acceptance_criteria:
- Lista de clientes con permiso
- Recordatorios enviados y recompra medida en 30 días
sources:
- 'plan Bogotá: Experimento 4'
order: 40
```

Con permiso del cliente, enviar recordatorio antes de que se acabe el empaque (según peso y ración confirmada). Medir recompra y bajas.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-023"></a>
## BL-023 · Presentación de entrada

Archivo: [BL-023-presentacion-de-entrada.md](BL-023-presentacion-de-entrada.md)

```yaml
key: BL-023
issue_type: Experimento
summary: Presentación de entrada
description: Probar una presentación o condición de entrada viable en costo frente a la habitual. Medir compra, contribución y recompra.
priority: Low
status: Backlog
assignee: Omar/Canívoros (propuesta)
effort: M
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- producto
- experimento
dependencies:
- BL-005
acceptance_criteria:
- Costo de la presentación confirmado
- Resultados de 4 semanas
sources:
- 'plan Bogotá: Experimento 1'
order: 41
```

Probar una presentación o condición de entrada viable en costo frente a la habitual. Medir compra, contribución y recompra.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-024"></a>
## BL-024 · Aplicar QFD a Canívoros

Archivo: [BL-024-aplicar-qfd-a-canivoros.md](BL-024-aplicar-qfd-a-canivoros.md)

```yaml
key: BL-024
issue_type: Tarea
summary: Aplicar QFD a Canívoros
description: 'Con las entrevistas, construir una casa de la calidad simple en una hoja: necesidades del cliente (voz del cliente) vs características del producto/servicio, con pesos. Complementar con Kano para separar básicos de diferenciales.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Medio
sprint: Semana 6 (7–13 dic)
labels:
- metodologia
- producto
- qfd
dependencies:
- BL-007
acceptance_criteria:
- Matriz QFD en hoja de cálculo
- Top 3 características a priorizar
sources:
- 'develop: QFD.pdf (ejemplo BIOLAV)'
- metodologias_analisis_competitivo.md
order: 48
```

Con las entrevistas, construir una casa de la calidad simple en una hoja: necesidades del cliente (voz del cliente) vs características del producto/servicio, con pesos. Complementar con Kano para separar básicos de diferenciales.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-025"></a>
## BL-025 · Costo y rentabilidad por producto

Archivo: [BL-025-costo-y-rentabilidad-por-producto.md](BL-025-costo-y-rentabilidad-por-producto.md)

```yaml
key: BL-025
issue_type: Tarea
summary: Costo y rentabilidad por producto
description: 'Reconstruir un lote real: ingredientes, merma, producto obtenido y costo; calcular contribución por producto y canal. Aclarar el cálculo de 4,8 M vs 9,6 M por tonelada en gatos.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- finanzas
- produccion
dependencies:
- BL-005
- BL-055
acceptance_criteria:
- Costo por kg de al menos 2 productos
- Contribución por canal estimada y marcada como estimado
sources:
- problemas.md
- erp.md §6
order: 27
```

Reconstruir un lote real: ingredientes, merma, producto obtenido y costo; calcular contribución por producto y canal. Aclarar el cálculo de 4,8 M vs 9,6 M por tonelada en gatos.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-026"></a>
## BL-026 · Gatívoros: introducción alimentaria en veterinarias

Archivo: [BL-026-gativoros-introduccion-alimentaria-en-veterinarias.md](BL-026-gativoros-introduccion-alimentaria-en-veterinarias.md)

```yaml
key: BL-026
issue_type: Experimento
summary: 'Gatívoros: introducción alimentaria en veterinarias'
description: 'Piloto con 2–3 veterinarias o tiendas de gatos (Cat Mania, Catkitten, Felicette) y fundaciones: muestras para gatitos, presentación pequeña (p. ej. 200 g, propuesta). Medir aceptación y recompra.'
priority: Low
status: Backlog
assignee: Omar/Canívoros + Sebastián (propuesta)
effort: M
impact: Medio
sprint: Semana 7 (14–20 dic)
labels:
- gatos
- experimento
dependencies:
- BL-025
acceptance_criteria:
- 2–3 aliados aceptan el piloto
- Registro de aceptación y desperdicio
- 'Decisión: seguir, ajustar o pausar'
sources:
- chat 25/10
- erp.md §6
order: 51
```

Piloto con 2–3 veterinarias o tiendas de gatos (Cat Mania, Catkitten, Felicette) y fundaciones: muestras para gatitos, presentación pequeña (p. ej. 200 g, propuesta). Medir aceptación y recompra.

### Hechos
El plan Bogotá recomienda concentrar el piloto en perros primero; por eso queda en semana 6.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-027"></a>
## BL-027 · Monitoreo de la máquina

Archivo: [BL-027-monitoreo-de-la-maquina.md](BL-027-monitoreo-de-la-maquina.md)

```yaml
key: BL-027
issue_type: Experimento
summary: Monitoreo de la máquina
description: Pedir modelo, ficha técnica y manual de la máquina. Con la IA, proponer un monitoreo simple (alertas, sensores o registro) y un análisis de fallas (FMEA).
priority: Low
status: Backlog
assignee: Sebastián (propuesta)
effort: L
impact: Medio
sprint: Semana 7 (14–20 dic)
labels:
- produccion
- iot
- experimento
dependencies:
- BL-009
acceptance_criteria:
- Ficha técnica obtenida
- FMEA de la máquina con 5 fallas priorizadas
- Propuesta de monitoreo con costo estimado
sources:
- chat 29/10
- 'metodologias: FMEA'
order: 52
```

Pedir modelo, ficha técnica y manual de la máquina. Con la IA, proponer un monitoreo simple (alertas, sensores o registro) y un análisis de fallas (FMEA).

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-028"></a>
## BL-028 · Decidir cómo crecer en Bogotá

Archivo: [BL-028-decidir-como-crecer-en-bogota.md](BL-028-decidir-como-crecer-en-bogota.md)

```yaml
key: BL-028
issue_type: Tarea
summary: Decidir cómo crecer en Bogotá
description: Con datos de 4–6 semanas, decidir ampliar, ajustar o detener según las reglas del plan (contribución, recompra, capacidad, servicio).
priority: Medium
status: Backlog
assignee: Andrés + Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 7 (14–20 dic)
labels:
- estrategia
- bogota
dependencies:
- BL-013
- BL-012
acceptance_criteria:
- Documento de decisión con datos
- Siguiente ciclo de 6 semanas planeado
sources:
- 'plan Bogotá: Reglas para ampliar, ajustar o detener'
order: 50
```

Con datos de 4–6 semanas, decidir ampliar, ajustar o detener según las reglas del plan (contribución, recompra, capacidad, servicio).

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-029"></a>
## BL-029 · Nombre provisorio, dominio y subdominio

Archivo: [BL-029-nombre-provisorio-dominio-y-subdominio.md](BL-029-nombre-provisorio-dominio-y-subdominio.md)

```yaml
key: BL-029
issue_type: Tarea
summary: Nombre provisorio, dominio y subdominio
description: Elegir nombre provisorio para la agencia, comprar dominio y apuntar un subdominio a Odoo con HTTPS.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Bajo
sprint: Semana 5 (30 nov–6 dic)
labels:
- marca
- infra
dependencies: []
acceptance_criteria:
- Nombre elegido
- Dominio con HTTPS activo
sources:
- chat 28–29/10
order: 45
```

Elegir nombre provisorio para la agencia, comprar dominio y apuntar un subdominio a Odoo con HTTPS.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-030"></a>
## BL-030 · Definir oferta de Growth Partner y diferencial

Archivo: [BL-030-definir-oferta-de-growth-partner-y-diferencial.md](BL-030-definir-oferta-de-growth-partner-y-diferencial.md)

```yaml
key: BL-030
issue_type: Tarea
summary: Definir oferta de Growth Partner y diferencial
description: 'Usar pasos_sysmkt.md para definir las 5 líneas de servicio, qué se promete y qué no, y el diferencial: conectar captación con compra, entrega y recompra. Alinear con los precios de Bogotá.'
priority: Medium
status: Backlog
assignee: Andrés + Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 5 (30 nov–6 dic)
labels:
- growth-partner
- oferta
dependencies: []
acceptance_criteria:
- Página de 1 hoja con oferta, precios y diferencial
sources:
- 'develop: pasos_sysmkt.md'
- precios_competencia_bogota.xlsx
order: 44
```

Usar pasos_sysmkt.md para definir las 5 líneas de servicio, qué se promete y qué no, y el diferencial: conectar captación con compra, entrega y recompra. Alinear con los precios de Bogotá.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-031"></a>
## BL-031 · Estación de trabajo VR con celular

Archivo: [BL-031-estacion-de-trabajo-vr-con-celular.md](BL-031-estacion-de-trabajo-vr-con-celular.md)

```yaml
key: BL-031
issue_type: Idea
summary: Estación de trabajo VR con celular
description: Hobby de Sebastián; sin cliente que pague ahora.
priority: Low
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Bajo
sprint: Sin semana (ideas en pausa)
labels:
- idea
- pausa
dependencies: []
acceptance_criteria:
- Se retoma solo después del primer ingreso
sources:
- chat oct 2026
order: 55
```

Hobby de Sebastián; sin cliente que pague ahora.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-032"></a>
## BL-032 · App para concursos de perros

Archivo: [BL-032-app-para-concursos-de-perros.md](BL-032-app-para-concursos-de-perros.md)

```yaml
key: BL-032
issue_type: Idea
summary: App para concursos de perros
description: Inscripción, fotos y transmisión; posible herramienta de marketing para Omar.
priority: Low
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Bajo
sprint: Sin semana (ideas en pausa)
labels:
- idea
- pausa
dependencies: []
acceptance_criteria:
- Se retoma solo después del primer ingreso
sources:
- chat oct 2026
order: 56
```

Inscripción, fotos y transmisión; posible herramienta de marketing para Omar.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-033"></a>
## BL-033 · Asistente de IA local con notas

Archivo: [BL-033-asistente-de-ia-local-con-notas.md](BL-033-asistente-de-ia-local-con-notas.md)

```yaml
key: BL-033
issue_type: Idea
summary: Asistente de IA local con notas
description: Modelo offline que responde con notas propias.
priority: Low
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Bajo
sprint: Sin semana (ideas en pausa)
labels:
- idea
- pausa
dependencies: []
acceptance_criteria:
- Se retoma solo después del primer ingreso
sources:
- chat oct 2026
order: 57
```

Modelo offline que responde con notas propias.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-034"></a>
## BL-034 · Extensiones de Chrome propias

Archivo: [BL-034-extensiones-de-chrome-propias.md](BL-034-extensiones-de-chrome-propias.md)

```yaml
key: BL-034
issue_type: Idea
summary: Extensiones de Chrome propias
description: Transferir archivos celular–PC o raspar datos de competencia.
priority: Low
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Bajo
sprint: Sin semana (ideas en pausa)
labels:
- idea
- pausa
dependencies: []
acceptance_criteria:
- Se retoma solo después del primer ingreso
sources:
- chat oct 2026
order: 58
```

Transferir archivos celular–PC o raspar datos de competencia.

### Hechos
Ver fuentes.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-035"></a>
## BL-035 · Validar los distribuidores publicados en el sitio

Archivo: [BL-035-validar-los-distribuidores-publicados-en-el-sitio.md](BL-035-validar-los-distribuidores-publicados-en-el-sitio.md)

```yaml
key: BL-035
issue_type: Tarea
summary: Validar los distribuidores publicados en el sitio
description: Llamar a los 6 distribuidores que publica el sitio (Manimal y Sankatin en Bogotá, Malcriados en Chía, Terranova en Sopó, Pets & Company en Zipaquirá, Club Canes en Villavicencio) y confirmar si siguen activos, qué venden, cada cuánto reponen y qué piden. Actualizar el sitio con los que sigan.
priority: High
status: Backlog
assignee: Omar/Canívoros (propuesta)
effort: S
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- distribuidores
- b2b
dependencies: []
acceptance_criteria:
- '6 distribuidores con estado: activo, inactivo o sin respuesta'
- Frecuencia de reposición y producto principal de cada activo
- Lista corregida para el sitio web
sources:
- CANIVOROS-REFERENCIA-EMPRESA.md (Distribuidores publicados)
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (confirmar operación de distribuidores)
order: 12
```

Llamar a los 6 distribuidores que publica el sitio (Manimal y Sankatin en Bogotá, Malcriados en Chía, Terranova en Sopó, Pets & Company en Zipaquirá, Club Canes en Villavicencio) y confirmar si siguen activos, qué venden, cada cuánto reponen y qué piden. Actualizar el sitio con los que sigan.

### Hechos
El sitio publica 6 distribuidores; el plan pide confirmar su operación antes de elegir zonas.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-036"></a>
## BL-036 · Medir la capacidad de producción disponible

Archivo: [BL-036-medir-la-capacidad-de-produccion-disponible.md](BL-036-medir-la-capacidad-de-produccion-disponible.md)

```yaml
key: BL-036
issue_type: Tarea
summary: Medir la capacidad de producción disponible
description: Calcular cuántos kilos adicionales por semana se pueden producir hoy, con la máquina, el personal y la materia prima actuales. Sin este dato no se puede prometer más ventas.
priority: Highest
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 2 (9–15 nov)
labels:
- produccion
- capacidad
dependencies:
- BL-009
acceptance_criteria:
- Kilos producidos por semana (promedio de 4 semanas)
- Kilos adicionales posibles por semana y qué los limita (máquina, personas o materia prima)
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Datos pendientes)
- problemas.md (abastecimiento irregular)
order: 11
```

Calcular cuántos kilos adicionales por semana se pueden producir hoy, con la máquina, el personal y la materia prima actuales. Sin este dato no se puede prometer más ventas.

### Hechos
El plan dice que se desconoce la capacidad disponible; problemas.md dice que vender más no garantiza poder producir más.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-037"></a>
## BL-037 · Registrar proveedores y recepción de materia prima

Archivo: [BL-037-registrar-proveedores-y-recepcion-de-materia-prima.md](BL-037-registrar-proveedores-y-recepcion-de-materia-prima.md)

```yaml
key: BL-037
issue_type: Historia
summary: Registrar proveedores y recepción de materia prima
description: 'Aplicar el flujo de erp.md: disponibilidad del proveedor → compra → recepción → cuarto frío → salida a producción. Crear en Odoo o en una hoja el catálogo de materias primas (cabeza de pollo, barriga de salmón, canilla y vísceras de cerdo), los proveedores y un registro por cada ingreso, con fecha, kilos y costo.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- odoo
- abastecimiento
- trazabilidad
dependencies:
- BL-011
acceptance_criteria:
- Catálogo de materias primas y proveedores cargado
- Cada ingreso tiene identificador, fecha, kilos aceptados y costo por kilo
- Se puede saber qué ingreso se usó en un lote de producción
sources:
- erp.md (Compras, recepción y almacenamiento)
order: 24
```

Aplicar el flujo de erp.md: disponibilidad del proveedor → compra → recepción → cuarto frío → salida a producción. Crear en Odoo o en una hoja el catálogo de materias primas (cabeza de pollo, barriga de salmón, canilla y vísceras de cerdo), los proveedores y un registro por cada ingreso, con fecha, kilos y costo.

### Hechos
La materia prima llega congelada, de varios proveedores, y suele procesarse en la semana siguiente.

### Supuestos
Los criterios de aceptación y temperatura todavía no están definidos.

---

<a id="bl-038"></a>
## BL-038 · Responder las 12 preguntas pendientes de compras y recepción

Archivo: [BL-038-responder-las-12-preguntas-pendientes-de-compras-y.md](BL-038-responder-las-12-preguntas-pendientes-de-compras-y.md)

```yaml
key: BL-038
issue_type: Tarea
summary: Responder las 12 preguntas pendientes de compras y recepción
description: 'Hacer a la responsable de compras las 12 preguntas que deja erp.md: quién compra y autoriza, unidades, precios por proveedor, transporte, pagos, criterios de rechazo, orden de uso, pérdidas y capacidad útil del cuarto frío.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 2 (9–15 nov)
labels:
- abastecimiento
- entrevista
dependencies: []
acceptance_criteria:
- Las 12 preguntas tienen respuesta o se marcan como 'no se sabe'
- Respuestas guardadas en el repo
sources:
- erp.md (Preguntas que siguen pendientes)
order: 14
```

Hacer a la responsable de compras las 12 preguntas que deja erp.md: quién compra y autoriza, unidades, precios por proveedor, transporte, pagos, criterios de rechazo, orden de uso, pérdidas y capacidad útil del cuarto frío.

### Hechos
erp.md lista 12 preguntas abiertas sobre compras y recepción.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-039"></a>
## BL-039 · Buscar nuevos proveedores de subproductos

Archivo: [BL-039-buscar-nuevos-proveedores-de-subproductos.md](BL-039-buscar-nuevos-proveedores-de-subproductos.md)

```yaml
key: BL-039
issue_type: Experimento
summary: Buscar nuevos proveedores de subproductos
description: 'La materia prima limita el crecimiento: ''si necesitamos más hay que traer más proveedores''. Hacer una lista de 10 posibles proveedores (plantas de pollo, pescaderías, porcícolas) cerca de Sopó y contactar 5. Medir cuántos pueden entregar, cuánto y a qué precio.'
priority: Medium
status: Backlog
assignee: Omar/Canívoros + Andrés (investigación) (propuesta)
effort: M
impact: Alto
sprint: Semana 6 (7–13 dic)
labels:
- abastecimiento
- experimento
dependencies:
- BL-036
acceptance_criteria:
- Lista de 10 posibles proveedores con fuente
- 5 contactados con resultado registrado
- Kilos extra por semana que se podrían conseguir
sources:
- erp.md (relato de materia prima)
- problemas.md (abastecimiento irregular)
order: 47
```

La materia prima limita el crecimiento: 'si necesitamos más hay que traer más proveedores'. Hacer una lista de 10 posibles proveedores (plantas de pollo, pescaderías, porcícolas) cerca de Sopó y contactar 5. Medir cuántos pueden entregar, cuánto y a qué precio.

### Hechos
La empresa compra lo que los proveedores tengan; para tener más materia prima necesitan más proveedores.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-040"></a>
## BL-040 · Ordenar cobros y cartera

Archivo: [BL-040-ordenar-cobros-y-cartera.md](BL-040-ordenar-cobros-y-cartera.md)

```yaml
key: BL-040
issue_type: Tarea
summary: Ordenar cobros y cartera
description: Pasar las ventas a crédito, que hoy se marcan en rojo en Excel, a un registro con importe, pagos recibidos, saldo y fecha de vencimiento. Revisar cada semana quién debe.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- finanzas
- cobros
- odoo
dependencies:
- BL-011
acceptance_criteria:
- Lista de cuentas por cobrar con saldo y vencimiento
- Total de cartera vencida conocido
- Revisión semanal agendada
sources:
- 'erp.md (Necesidades operativas: controlar cobros)'
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (pagos y entregas son estados distintos)
order: 23
```

Pasar las ventas a crédito, que hoy se marcan en rojo en Excel, a un registro con importe, pagos recibidos, saldo y fecha de vencimiento. Revisar cada semana quién debe.

### Hechos
Los cobros se controlan con marcas rojas en Excel y hay clientes a crédito.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-041"></a>
## BL-041 · Confirmar la guía de raciones por peso de perro

Archivo: [BL-041-confirmar-la-guia-de-raciones-por-peso-de-perro.md](BL-041-confirmar-la-guia-de-raciones-por-peso-de-perro.md)

```yaml
key: BL-041
issue_type: Tarea
summary: Confirmar la guía de raciones por peso de perro
description: Conseguir o validar con la empresa la tabla de porciones por peso, edad y actividad que menciona el sitio. Se necesita para calcular cuánto dura un empaque y para el recordatorio de reposición.
priority: Medium
status: Backlog
assignee: Omar/Canívoros (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- producto
- retencion
dependencies: []
acceptance_criteria:
- Tabla de raciones confirmada por la empresa
- Días que dura cada presentación según el peso del perro
sources:
- CANIVOROS-REFERENCIA-EMPRESA.md (Uso y conservación)
- 'CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Experimento 4: sin inventar dosis)'
order: 30
```

Conseguir o validar con la empresa la tabla de porciones por peso, edad y actividad que menciona el sitio. Se necesita para calcular cuánto dura un empaque y para el recordatorio de reposición.

### Hechos
El sitio invita a consultar la guía de raciones pero no publica cantidades.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-042"></a>
## BL-042 · Revisar el WordPress y decidir si sirve como tienda

Archivo: [BL-042-revisar-el-wordpress-y-decidir-si-sirve-como-tiend.md](BL-042-revisar-el-wordpress-y-decidir-si-sirve-como-tiend.md)

```yaml
key: BL-042
issue_type: Tarea
summary: Revisar el WordPress y decidir si sirve como tienda
description: 'Revisar si el comercio electrónico del WordPress actual está configurado o solo tiene contenido de demostración. Decidir: catálogo con pedido por WhatsApp, tienda simple o nada por ahora.'
priority: Low
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 6 (7–13 dic)
labels:
- web
- ecommerce
dependencies:
- BL-005
acceptance_criteria:
- 'Informe corto: qué funciona y qué no'
- Decisión tomada y anotada
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Primera implementación de software)
order: 49
```

Revisar si el comercio electrónico del WordPress actual está configurado o solo tiene contenido de demostración. Decidir: catálogo con pedido por WhatsApp, tienda simple o nada por ahora.

### Hechos
El respaldo del sitio tiene contenido de demostración; no hay que asumir que la tienda funciona.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-043"></a>
## BL-043 · Programa para criadores y clientes de alto volumen

Archivo: [BL-043-programa-para-criadores-y-clientes-de-alto-volumen.md](BL-043-programa-para-criadores-y-clientes-de-alto-volumen.md)

```yaml
key: BL-043
issue_type: Experimento
summary: Programa para criadores y clientes de alto volumen
description: Las ventas de jul–oct muestran compras grandes de criadores (40–520 kg). Identificar los 10 clientes de más kilos, entrevistar a 3 y probar una condición para ellos (pedido programado, precio por volumen o referidos).
priority: Medium
status: Backlog
assignee: Omar/Canívoros + Andrés (datos) (propuesta)
effort: M
impact: Alto
sprint: Semana 4 (23–29 nov)
labels:
- ventas
- criadores
- experimento
dependencies:
- BL-004
acceptance_criteria:
- Top 10 clientes por kilos de jul–oct
- 3 conversaciones registradas
- Oferta probada y resultado medido en 4 semanas
sources:
- ventas_canivoros_2026.xlsx (columnas 'CRIADOR KG')
order: 36
```

Las ventas de jul–oct muestran compras grandes de criadores (40–520 kg). Identificar los 10 clientes de más kilos, entrevistar a 3 y probar una condición para ellos (pedido programado, precio por volumen o referidos).

### Hechos
El Excel separa ventas a cliente, almacén y criador; hay pedidos de criadores de 40 a 520 kg.

### Supuestos
Que el segmento criadores sea el más rentable es una hipótesis.

---

<a id="bl-044"></a>
## BL-044 · Registrar hipótesis y criterios de decisión antes de cada experimento

Archivo: [BL-044-registrar-hipotesis-y-criterios-de-decision-antes.md](BL-044-registrar-hipotesis-y-criterios-de-decision-antes.md)

```yaml
key: BL-044
issue_type: Tarea
summary: Registrar hipótesis y criterios de decisión antes de cada experimento
description: 'Antes de lanzar BL-012, BL-019, BL-020 y los demás experimentos, escribir en 5 líneas: hipótesis, qué se mide, con cuántos casos, qué resultado lleva a seguir, ajustar o parar, y el gasto máximo.'
priority: Medium
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Medio
sprint: Semana 2 (9–15 nov)
labels:
- metodologia
- experimentos
dependencies: []
acceptance_criteria:
- Plantilla de hipótesis en backlog/
- Cada experimento activo la tiene llena antes de empezar
sources:
- GuiaPesquisaProdutosServicosES.md (§4 Registrar hipótesis y criterios de decisión)
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Control del gasto)
order: 15
```

Antes de lanzar BL-012, BL-019, BL-020 y los demás experimentos, escribir en 5 líneas: hipótesis, qué se mide, con cuántos casos, qué resultado lleva a seguir, ajustar o parar, y el gasto máximo.

### Hechos
La guía pide registrar hipótesis y criterios antes de recopilar datos; el plan pide un límite de gasto por experimento.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-045"></a>
## BL-045 · Plan de negocio corto de la agencia Growth Partner

Archivo: [BL-045-plan-de-negocio-corto-de-la-agencia-growth-partner.md](BL-045-plan-de-negocio-corto-de-la-agencia-growth-partner.md)

```yaml
key: BL-045
issue_type: Historia
summary: Plan de negocio corto de la agencia Growth Partner
description: Usar la Guía para desarrollar productos o servicios (oportunidad, público, competencia, propuesta de valor, viabilidad, marketing) para escribir un plan de negocio de 2–3 páginas de la agencia. Hosana ofreció ayudar si existe un plan.
priority: Low
status: Backlog
assignee: Sebastián + Andrés (propuesta)
effort: M
impact: Medio
sprint: Semana 7 (14–20 dic)
labels:
- growth-partner
- plan-de-negocio
dependencies:
- BL-030
- BL-017
acceptance_criteria:
- Documento de 2–3 páginas con las 13 secciones resumidas
- Revisado por Hosana
sources:
- GuiaDesenvolverProdutosServicosES.md
- pasos_sysmkt.md (Que sabemos hacer bien)
order: 53
```

Usar la Guía para desarrollar productos o servicios (oportunidad, público, competencia, propuesta de valor, viabilidad, marketing) para escribir un plan de negocio de 2–3 páginas de la agencia. Hosana ofreció ayudar si existe un plan.

### Hechos
La guía tiene 13 secciones, de la oportunidad al resumen ejecutivo.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-046"></a>
## BL-046 · Explorar el Clúster de Bienestar Animal de la CCB

Archivo: [BL-046-explorar-el-cluster-de-bienestar-animal-de-la-ccb.md](BL-046-explorar-el-cluster-de-bienestar-animal-de-la-ccb.md)

```yaml
key: BL-046
issue_type: Idea
summary: Explorar el Clúster de Bienestar Animal de la CCB
description: Consultar si la iniciativa del Clúster de Protección y Bienestar Animal de la Cámara de Comercio de Bogotá sigue activa y si ofrece contactos con distribuidores o ruedas de negocio.
priority: Low
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Bajo
sprint: Semana 7 (14–20 dic)
labels:
- aliados
- bogota
dependencies: []
acceptance_criteria:
- Estado actual de la iniciativa confirmado
- 'Si está activa: siguiente evento o contacto anotado'
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Qué sabemos del mercado)
order: 54
```

Consultar si la iniciativa del Clúster de Protección y Bienestar Animal de la Cámara de Comercio de Bogotá sigue activa y si ofrece contactos con distribuidores o ruedas de negocio.

### Hechos
La CCB lanzó la iniciativa en 2024; se desconoce su oferta vigente.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-047"></a>
## BL-047 · Plantilla única para registrar ventas

Archivo: [BL-047-plantilla-unica-para-registrar-ventas.md](BL-047-plantilla-unica-para-registrar-ventas.md)

```yaml
key: BL-047
issue_type: Mejora
summary: Plantilla única para registrar ventas
description: El Excel de ventas cambia de columnas cada mes (julio 11 columnas, octubre 14), mezcla libras y kilos y tiene filas sin fecha. Definir una sola plantilla (o formulario) con cliente, fecha, producto, presentación, unidad, cantidad, precio y canal, hasta que todo pase a Odoo.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- mejora
dependencies:
- BL-005
acceptance_criteria:
- Plantilla con columnas fijas y listas desplegables
- Unidad única por producto
- Octubre migrado a la plantilla como prueba
sources:
- ventas_canivoros_2026.xlsx
order: 17
```

El Excel de ventas cambia de columnas cada mes (julio 11 columnas, octubre 14), mezcla libras y kilos y tiene filas sin fecha. Definir una sola plantilla (o formulario) con cliente, fecha, producto, presentación, unidad, cantidad, precio y canal, hasta que todo pase a Odoo.

### Hechos
Las hojas JULIO, AGOSTO, SEPT. y OCT. tienen columnas distintas; hay filas sin fecha (p. ej. un pedido de 520 kg en julio).

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-048"></a>
## BL-048 · Productos inactivos no aparecen en Odoo

Archivo: [BL-048-productos-inactivos-no-aparecen-en-odoo.md](BL-048-productos-inactivos-no-aparecen-en-odoo.md)

```yaml
key: BL-048
issue_type: Error
summary: Productos inactivos no aparecen en Odoo
description: En Odoo los productos cargados no se ven en ventas porque no están activos o publicados. Revisar y activar el catálogo confirmado.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- error
dependencies:
- BL-005
acceptance_criteria:
- Todos los productos del catálogo confirmado se ven y se pueden vender en Odoo
sources:
- chat 27/10 ('como los productos no están activos no aparecen')
order: 20
```

En Odoo los productos cargados no se ven en ventas porque no están activos o publicados. Revisar y activar el catálogo confirmado.

### Hechos
Sebastián lo reportó el 27/10.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-049"></a>
## BL-049 · Guardar precio y costo aplicados en cada venta

Archivo: [BL-049-guardar-precio-y-costo-aplicados-en-cada-venta.md](BL-049-guardar-precio-y-costo-aplicados-en-cada-venta.md)

```yaml
key: BL-049
issue_type: Requisito
summary: Guardar precio y costo aplicados en cada venta
description: Cada línea de venta debe guardar el precio y el costo de ese momento, para que un cambio de catálogo no altere la rentabilidad histórica.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- requisito
dependencies:
- BL-011
- BL-057
acceptance_criteria:
- Cambiar un precio no modifica ventas anteriores
- Reporte de contribución por venta
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Datos mínimos)
order: 22
```

Cada línea de venta debe guardar el precio y el costo de ese momento, para que un cambio de catálogo no altere la rentabilidad histórica.

### Hechos
El plan lo pide explícitamente.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-050"></a>
## BL-050 · Devoluciones y cancelaciones sin borrar la venta

Archivo: [BL-050-devoluciones-y-cancelaciones-sin-borrar-la-venta.md](BL-050-devoluciones-y-cancelaciones-sin-borrar-la-venta.md)

```yaml
key: BL-050
issue_type: Requisito
summary: Devoluciones y cancelaciones sin borrar la venta
description: Registrar devoluciones y cancelaciones como movimientos con motivo (incluidas las que van al criadero), sin borrar la venta original.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- requisito
dependencies:
- BL-011
acceptance_criteria:
- Una devolución deja la venta original y un movimiento con motivo
- Ventas netas = ventas − devoluciones
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md
- problemas.md (devoluciones al criadero)
order: 28
```

Registrar devoluciones y cancelaciones como movimientos con motivo (incluidas las que van al criadero), sin borrar la venta original.

### Hechos
problemas.md menciona devoluciones destinadas al criadero sin tratamiento claro.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-051"></a>
## BL-051 · Evitar pedidos duplicados en integraciones

Archivo: [BL-051-evitar-pedidos-duplicados-en-integraciones.md](BL-051-evitar-pedidos-duplicados-en-integraciones.md)

```yaml
key: BL-051
issue_type: Requisito
summary: Evitar pedidos duplicados en integraciones
description: Cuando WhatsApp, Instagram o formularios creen pedidos o leads automáticamente, un mismo evento no debe crear dos registros.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- requisito
dependencies:
- BL-011
acceptance_criteria:
- 'Prueba: enviar el mismo mensaje dos veces crea un solo registro'
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (Primera implementación de software)
order: 37
```

Cuando WhatsApp, Instagram o formularios creen pedidos o leads automáticamente, un mismo evento no debe crear dos registros.

### Hechos
El plan lo pone como criterio de aceptación del primer sistema.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-052"></a>
## BL-052 · Copias de seguridad diarias probadas

Archivo: [BL-052-copias-de-seguridad-diarias-probadas.md](BL-052-copias-de-seguridad-diarias-probadas.md)

```yaml
key: BL-052
issue_type: Requisito
summary: Copias de seguridad diarias probadas
description: Respaldo diario de la base de Odoo y adjuntos fuera del VPS, conservando 7 días, y una prueba de restauración.
priority: Highest
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Alto
sprint: Semana 1 (2–8 nov 2026)
labels:
- requisito
dependencies:
- BL-001
acceptance_criteria:
- Respaldo automático diario fuera del servidor
- Una restauración probada y anotada
sources:
- chat 26/10 (recomendación del servidor)
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (respaldo probado)
order: 3
```

Respaldo diario de la base de Odoo y adjuntos fuera del VPS, conservando 7 días, y una prueba de restauración.

### Hechos
Odoo ya corre en un VPS con datos del cliente.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-053"></a>
## BL-053 · Usuarios por función en Odoo

Archivo: [BL-053-usuarios-por-funcion-en-odoo.md](BL-053-usuarios-por-funcion-en-odoo.md)

```yaml
key: BL-053
issue_type: Requisito
summary: Usuarios por función en Odoo
description: Crear usuarios para Sara, la prima y Omar con permisos según su trabajo (ventas, compras, producción). Nadie usa la cuenta de administrador para el día a día.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- requisito
dependencies:
- BL-001
acceptance_criteria:
- Cada persona tiene su usuario
- Permisos revisados por función
- Historial de cambios activo
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (usuarios por función, historial)
order: 18
```

Crear usuarios para Sara, la prima y Omar con permisos según su trabajo (ventas, compras, producción). Nadie usa la cuenta de administrador para el día a día.

### Hechos
Sara Ramírez mantiene los Excel (problemas.md).

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-054"></a>
## BL-054 · Inventario de producto terminado por lote

Archivo: [BL-054-inventario-de-producto-terminado-por-lote.md](BL-054-inventario-de-producto-terminado-por-lote.md)

```yaml
key: BL-054
issue_type: Requisito
summary: Inventario de producto terminado por lote
description: Registrar lotes con fecha de producción y vencimiento, ubicación, entradas y salidas, y cantidades comprometidas en pedidos.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- requisito
dependencies:
- BL-011
- BL-055
acceptance_criteria:
- Stock por lote consultable
- Se sabe qué lote se entregó en cada pedido
sources:
- problemas.md (inventario de memoria)
- erp.md
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md
order: 26
```

Registrar lotes con fecha de producción y vencimiento, ubicación, entradas y salidas, y cantidades comprometidas en pedidos.

### Hechos
Hoy el inventario se consulta de memoria.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-055"></a>
## BL-055 · Registro de producción con receta, merma y costo

Archivo: [BL-055-registro-de-produccion-con-receta-merma-y-costo.md](BL-055-registro-de-produccion-con-receta-merma-y-costo.md)

```yaml
key: BL-055
issue_type: Requisito
summary: Registro de producción con receta, merma y costo
description: 'Por cada lote: receta, materia prima usada (por ingreso), cantidad producida, merma y costo.'
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- requisito
dependencies:
- BL-037
acceptance_criteria:
- Un lote real registrado completo
- Merma y rendimiento por receta calculados
sources:
- erp.md (recetas y rendimientos)
- problemas.md
order: 25
```

Por cada lote: receta, materia prima usada (por ingreso), cantidad producida, merma y costo.

### Hechos
Se mencionan cantidades por lote y merma sin registro sistemático.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-056"></a>
## BL-056 · Código de Odoo en Git y pruebas en local

Archivo: [BL-056-codigo-de-odoo-en-git-y-pruebas-en-local.md](BL-056-codigo-de-odoo-en-git-y-pruebas-en-local.md)

```yaml
key: BL-056
issue_type: Mejora
summary: Código de Odoo en Git y pruebas en local
description: Mantener la personalización de Odoo en el repo canivorosodoo y probar cada cambio en local antes de subirlo al servidor.
priority: Medium
status: Backlog
assignee: Sebastián (propuesta)
effort: S
impact: Medio
sprint: Semana 3 (16–22 nov)
labels:
- mejora
dependencies:
- BL-052
acceptance_criteria:
- Todo cambio en el servidor viene de un commit
- Procedimiento corto documentado en el repo
sources:
- chat 26/10 y 28/10 (repo canivorosodoo)
order: 29
```

Mantener la personalización de Odoo en el repo canivorosodoo y probar cada cambio en local antes de subirlo al servidor.

### Hechos
Sebastián ya creó el repo canivorosodoo.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-057"></a>
## BL-057 · Listas de precios por canal y unidad en Odoo

Archivo: [BL-057-listas-de-precios-por-canal-y-unidad-en-odoo.md](BL-057-listas-de-precios-por-canal-y-unidad-en-odoo.md)

```yaml
key: BL-057
issue_type: Requisito
summary: Listas de precios por canal y unidad en Odoo
description: Configurar precios por cliente final, almacén/distribuidor y criador, y por libra o kilo, que hoy Sebastián no encuentra cómo modelar en Odoo.
priority: High
status: Backlog
assignee: Sebastián (propuesta)
effort: M
impact: Alto
sprint: Semana 3 (16–22 nov)
labels:
- requisito
dependencies:
- BL-005
acceptance_criteria:
- Tres listas de precios activas
- Un pedido de prueba por canal toma el precio correcto
sources:
- chat audio 29/10 (precios por libra, kilo y tipo de cliente)
- ventas_canivoros_2026.xlsx
order: 16
```

Configurar precios por cliente final, almacén/distribuidor y criador, y por libra o kilo, que hoy Sebastián no encuentra cómo modelar en Odoo.

### Hechos
El Excel separa cliente, almacén y criador.

### Supuestos
Responsable, plazo y esfuerzo son propuestas.

---

<a id="bl-058"></a>
## BL-058 · Permiso de datos y comunicaciones de clientes

Archivo: [BL-058-permiso-de-datos-y-comunicaciones-de-clientes.md](BL-058-permiso-de-datos-y-comunicaciones-de-clientes.md)

```yaml
key: BL-058
issue_type: Requisito
summary: Permiso de datos y comunicaciones de clientes
description: Guardar el permiso de cada cliente para recibir mensajes y tratar sus datos (ley colombiana de protección de datos), antes de automatizar WhatsApp o recordatorios.
priority: High
status: Backlog
assignee: Andrés (propuesta)
effort: S
impact: Medio
sprint: Semana 4 (23–29 nov)
labels:
- requisito
dependencies: []
acceptance_criteria:
- Texto de autorización corto aprobado por la empresa
- Campo de permiso en el registro del cliente
sources:
- CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md (permiso de comunicaciones)
order: 35
```

Guardar el permiso de cada cliente para recibir mensajes y tratar sus datos (ley colombiana de protección de datos), antes de automatizar WhatsApp o recordatorios.

### Hechos
El plan pide registrar el permiso de comunicaciones.

### Supuestos
Hay que confirmar los requisitos legales exactos con alguien que conozca la norma colombiana.
