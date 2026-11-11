# Pipeline de leads: triage, dueño y próximo paso

Aporte del 10 de noviembre de 2026. Borrador para que lo apruebe Andrés. Responsables, plazos y pesos son **propuestas**, no compromisos.

**Qué resuelve.** El repo ya tiene piezas sueltas: niveles A/B/C para negocios (`prospectos/AGENTS.md`), etapas y reglas de seguimiento en E01 y E02 (`embudos/`), campos de origen en BL-047 y la captura de leads de BL-019. Falta **una sola regla de triage** que sirva para quien escribe por WhatsApp o Instagram y para aliados B2B: puntaje, duplicados, dueño, próximo paso y qué está vencido o estancado. Este documento la propone sin cambiar lo existente: reutiliza sus etapas, niveles y listas.

**Dónde vive el registro.** El registro real va en un entorno privado (hoja con acceso controlado y luego Odoo, BL-011). **No se suben al repo** nombres, teléfonos, chats ni exportaciones de clientes (`AGENTS.md`, `embudos/E02-…/embudo.md` §6). La plantilla de esta carpeta solo trae filas de EJEMPLO.

---

## 1. Esquema del registro de leads

Archivo: [`plantilla-registro-leads.csv`](plantilla-registro-leads.csv). Una fila por lead. Lo que no se sabe: `desconocido` (no es lo mismo que cero).

| Columna | Valores permitidos | De dónde sale |
|---|---|---|
| `id_lead` | `L0001`, `L0002`… No se reutiliza. | Igual que los ID `P001` de `prospectos/` |
| `id_prospecto` | `P###` si vino de `prospectos/`; si no, vacío | `prospectos/prospectos-2026-11-03.csv` |
| `id_cliente` | ID interno si ya compró; si no, vacío | Plan Bogotá, "Datos mínimos" (cliente) |
| `fecha_entrada` | AAAA-MM-DD | — |
| `tipo_lead` | `consumidor` · `tienda` · `veterinaria` · `criadero` · `servicio canino` · `distribuidor` · `otro` | Tipos de `prospectos/AGENTS.md`; "almacén" y "criador" del Excel de ventas |
| `especie` | `perro` · `gato` · `ambos` · `desconocido` | Plan Bogotá (piloto en perros) |
| `canal_entrada` | `WhatsApp` · `Instagram` · `Facebook` · `correo` · `referido` · `aliado` · `prospección` · `otro` | Canales de `CANIVOROS-REFERENCIA-EMPRESA.md` |
| `numero_whatsapp` | Cuál de los números publicados recibió el mensaje, o `desconocido` | Hay 3 números publicados (`CANIVOROS-REFERENCIA-EMPRESA.md`) |
| `origen` | `campaña` · `aliado` · `Omar` · `orgánico` · `desconocido` | BL-047 |
| `codigo_campana_o_aliado` | Código o QR, o vacío | BL-047, plan Bogotá (Experimento 3) |
| `zona` | Localidad de Bogotá, municipio de Sabana o `fuera de zona` · `desconocido` | Plan Bogotá, E01 |
| `contacto_ref` | Referencia interna al chat o cuenta, solo en el registro privado | — |
| `telefono_norm` | Últimos 10 dígitos, sin espacios | Igual que `telefonos()` en `registro.py` |
| `instagram` | Cuenta en minúsculas, sin `@` | Igual que `instagram()` en `registro.py` |
| `correo` | En minúsculas | — |
| `negocio_nombre` | Solo B2B | `prospectos/` |
| `intencion` | `pide pedido` · `pide precio` · `pide información` · `pide condiciones de aliado` · `solo reacciona` · `queja o incidencia` | Hipótesis (§2) |
| `permiso_mensajes` | `sí` · `no` · `desconocido` | BL-058 |
| `pts_intencion` … `pts_datos` | Números (ver §2) | — |
| `puntaje` | 0–100 = suma de los 5 componentes | — |
| `nivel` | `A` · `B` · `C` · `D` | §2 |
| `motivo_descarte` | Obligatorio si `nivel = D` o `estado = Perdido` | Motivos de E02 §6 |
| `estado` | `Nuevo` · `Calificado` · `Oferta enviada` · `Pagado` · `Entregado` · `Recompra` · `En pausa` · `Perdido` · `Baja` | Etapas de E01 y E02 |
| `fecha_estado` | AAAA-MM-DD del último cambio de estado | Para medir estancados |
| `responsable` | Nombre de §4 o `[por asignar]` | §4 |
| `proximo_paso` | Verbo + objeto (p. ej. "enviar precio confirmado") | §4 |
| `fecha_proximo_paso` | AAAA-MM-DD | §4 |
| `fecha_primera_respuesta` | AAAA-MM-DD HH:MM | BL-059 (tiempo de respuesta) |
| `duplicado_de` | `id_lead` principal si se fusionó | §3 |
| `notas` | Texto corto, sin datos de salud del animal ni datos personales extra | — |

Motivos cerrados de pérdida (de E02 §6): `precio` · `entrega` · `falta de stock` · `aún tiene producto` · `otra marca` · `otro canal` · `experiencia negativa` · `no responde` · `otro` · `desconocido`. Para descartes B2B se agregan los de `prospectos/AGENTS.md`: `cerrado` · `duplicado` · `cliente actual` · `persona sin negocio` · `solo gatos` · `intermediario de cachorros`.

---

## 2. Calificación: puntaje 0–100 y niveles

Antes de puntuar, tres desvíos (no se puntúan):

1. **Queja o incidencia** → se atiende primero, fuera del pipeline de venta (E02 §2: "Atender primero consultas entrantes y quejas").
2. **Pregunta de salud o malestar del animal** → se recomienda consultar al veterinario, como dice la marca en sus preguntas frecuentes (`CANIVOROS-REFERENCIA-EMPRESA.md`). No se responde con beneficios de salud (`prospectos/AGENTS.md`, BL-016).
3. **Ya es cliente** → va al flujo de recompra (E02, ruta B), no a adquisición.

### Componentes (visibles en el registro)

| Componente | Puntos | Regla | ¿Respaldo en el repo? |
|---|---|---|---|
| `pts_intencion` | 0–30 | Pide pedido 30 · pide precio 22 · pide condiciones de aliado 22 · pide información 12 · solo reacciona 3 | **Hipótesis**: medir con BL-059 qué intención termina en compra |
| `pts_segmento` | 0–25 | Criadero o volumen alto 25 · tienda o veterinaria que ya vende natural/BARF 25 · tienda, veterinaria o servicio canino sin señal de natural 15 · consumidor 12 · otro 5 | **Respaldo parcial**: el Excel tiene pedidos de criadores de 40 a 520 kg (BL-043); `prospectos/AGENTS.md` da nivel A a quien ya trabaja natural o tiene volumen. Los puntos exactos son hipótesis |
| `pts_zona` | 0–20 | Bogotá o Sabana Centro con entrega confirmada 20 · Bogotá o Sabana sin confirmar 12 · `desconocido` 6 · fuera de zona 0 | **Respaldo**: el objetivo es Bogotá (plan, E01 incluye Sabana Centro). La cobertura real es `desconocido` (E02 pide confirmarla) |
| `pts_especie` | 0–10 | Perro 10 · ambos 8 · `desconocido` 5 · solo gato 4 | **Respaldo**: el plan concentra el piloto en perros; Gatívoros sigue en catálogo |
| `pts_datos` | 0–15 | +5 respondió al menos una pregunta de calificación (zona, perros, comida actual: E01, Guion 1) · +5 `permiso_mensajes = sí` · +5 origen distinto de `desconocido` | **Respaldo**: E01 (calificación), BL-058 (permiso), BL-021 (origen) |

`puntaje = pts_intencion + pts_segmento + pts_zona + pts_especie + pts_datos`

### Niveles

| Nivel | Puntaje | Qué se hace |
|---|---|---|
| **A** | 70–100 | Responder **el mismo día hábil** |
| **B** | 45–69 | Responder **esta semana** (máx. 5 días hábiles) |
| **C** | 20–44 | **Nutrir**: sin mensajes proactivos sin permiso; revisar una vez al mes |
| **D** | 0–19, o un descarte | **Descartar con motivo** (`motivo_descarte` obligatorio) |

Reglas fijas, sin importar el puntaje:

- **Criadero o volumen alto detectado → pasa a Omar** (E01 §"Reglas de seguimiento"). Avisar si el pedido podría superar la capacidad, que es `desconocido` (`prospectos/AGENTS.md`, BL-036).
- Duplicado → D con motivo `duplicado` y `duplicado_de` lleno (§3).
- Negocio B2B: **nadie lo contacta sin aprobación de Andrés** (`prospectos/AGENTS.md`). Su nivel A/B/C de `prospectos/` se conserva; este puntaje solo ordena dentro del nivel.
- Los cortes 70/45/20 son **hipótesis**. Revisar tras 4 semanas con datos (BL-019, BL-044).

---

## 3. Duplicados: cuándo fusionar

Claves, en este orden. Las tres primeras ya las usa `.claude/skills/encontrar-prospectos/scripts/registro.py` (`claves_duplicado`) para prospectos; aquí se extienden a leads de consumidores y a clientes.

| # | Clave | Normalización | Acción |
|---|---|---|---|
| 1 | Teléfono | Últimos 10 dígitos, sin espacios, puntos ni guiones | Fusión automática |
| 2 | Instagram | Minúsculas, sin `@` ni punto final | Fusión automática |
| 3 | Web o Facebook (B2B) | Dominio sin `www`; `facebook.com/<ruta>` | Fusión automática |
| 4 | Correo | Minúsculas, sin espacios | Fusión automática |
| 5 | Nombre de negocio + localidad | Sin tildes ni palabras genéricas (`nombre_base()` de `registro.py`) | **Revisión humana** |
| 6 | Nombre de persona parecido (p. ej. variantes de escritura) | — | **Nunca automática**: confirmar con quien atiende |

Cómo fusionar:

- Queda como principal el registro **más antiguo**. El otro pasa a `nivel = D`, `motivo_descarte = duplicado`, `duplicado_de = <principal>`. No se borra (mismo criterio que BL-050 para ventas).
- Se conservan el **origen inicial** del principal y el canal del segundo contacto en `notas` (plan Bogotá: "registrar tanto el origen inicial como el canal que cierra la venta").
- Si el duplicado coincide con un cliente del Excel de ventas, va al flujo de recompra y **su nombre no se escribe en el repo** (`encontrar-prospectos/SKILL.md`).
- Un mismo negocio con varias sedes es **un** lead con sedes en `notas`, salvo que compren por separado.

---

## 4. Dueño y próximo paso

Todo lead abierto (`estado` distinto de `Perdido` o `Baja`) debe tener **los tres** campos: `responsable`, `proximo_paso` y `fecha_proximo_paso`. Si falta uno, cuenta como vencido.

| Situación | Responsable propuesto | Fuente del rol |
|---|---|---|
| Consumidor por WhatsApp o Instagram | Omar | `erp.md` §2 "Equipo y responsabilidades": Omar atiende WhatsApp y recibe pedidos |
| Criadero o volumen alto | Omar | E01 |
| Pedido confirmado: factura, pago, entrega | Responsable de la operación (`[nombre por confirmar]`) | `erp.md` §2 |
| Prospecto B2B: aprobar contacto y medir | Andrés | `prospectos/AGENTS.md`; BL-012 |
| Prospecto B2B: hacer el contacto aprobado | Hermano de Sebastián + Omar (`[por confirmar]`) | BL-012 (propuesta) |
| Suplente cuando el responsable no está | `[suplente por definir]` | E02: horario y suplente `desconocido` |

Próximo paso por estado:

| Estado | Próximo paso típico | Plazo |
|---|---|---|
| Nuevo | Primera respuesta + 2–3 preguntas (zona, perros, comida actual) | Según nivel (abajo) |
| Calificado | Enviar oferta con precio **confirmado** (BL-005); si no hay precio confirmado, decirlo | 1 día hábil |
| Oferta enviada | Seguimiento a las 24 h y a las 72 h; luego `Perdido` con motivo | E01, E02 |
| Pagado | Confirmar fecha de entrega | Responsable de la operación |
| Entregado | Contacto día 3 y día 10; pedir permiso de recordatorio | E01 |
| Recompra | Recordatorio antes de la fecha estimada, solo con permiso | BL-022 |

Ventanas de respuesta por nivel:

| Nivel | Primera respuesta | Nota |
|---|---|---|
| A | Mismo día hábil | E01. E02 propone como meta ≤30 min en horario atendido |
| B | ≤5 días hábiles | Hipótesis |
| C | Sin plazo de venta; revisión mensual | Solo si hay permiso o si la persona vuelve a escribir (E02 §2) |
| D | Cerrar el mismo día con motivo | — |

---

## 5. Vencidos, estancados y revisión semanal

- **Vencido**: lead abierto con `fecha_proximo_paso` anterior a hoy, **o** sin responsable o sin próximo paso, **o** nivel A sin `fecha_primera_respuesta` al cierre del día hábil.
- **Estancado**: 14 días o más en el mismo `estado` (hoy − `fecha_estado` ≥ 14). Excepción: `Entregado` o `Recompra` con fecha de reposición futura no está estancado; los empaques de larga duración necesitan más tiempo (plan Bogotá, "Plan de ejecución de 90 días").
- Un estancado se decide en la revisión: **avanzar** (nuevo próximo paso y fecha), **pausar** (`En pausa`) o **cerrar** (`Perdido` con motivo).

**Revisión semanal (20 min, lunes, responsable `[por asignar]`).** Encaja con el tablero de BL-013.

1. Números de la semana: leads nuevos por `origen` y `canal_entrada`; % con origen distinto de `desconocido` (BL-021 pide >80 % para cobrar por resultados); A/B/C/D.
2. Atención: % de A respondidos el mismo día y tiempo de primera respuesta (línea base de BL-059).
3. Higiene: cuántos abiertos sin responsable o sin próximo paso; cuántos vencidos; cuántos estancados.
4. Decisión por cada estancado: avanzar, pausar o cerrar.
5. Duplicados fusionados en la semana.
6. Una sola mejora para la semana siguiente.

---

## 6. Diagnóstico inicial con los datos del repo

Calculado el 10 de noviembre de 2026 sobre la rama `develop`. Del Excel de ventas solo se dan agregados (`AGENTS.md`).

**`prospectos/prospectos-2026-11-03.csv`**

- 38 registros (P001–P038). Nivel: A 7, B 10, C 17, sin nivel 4.
- Estado: 17 `borrador listo`, 17 `no verificado`, 4 `descartado` (1 por posible cliente actual, 3 por intermediarios).
- 34 registros abiertos. **Ninguno tiene responsable, próximo paso ni fecha de próximo paso**: el formato no trae esas columnas.
- Duplicados: 0 por teléfono o web en la revisión hecha para este aporte. El script `registro.py` ya hace esta revisión en cada lote.
- Los 38 tienen fecha 2026-11-03. Si no cambian de estado, el 17 de noviembre de 2026 cumplen 14 días y quedan **estancados** según §5. Los 17 `borrador listo` esperan la aprobación de Andrés.

**`ventas_canivoros_2026.xlsx`** (hojas JULIO, AGOSTO, SEPT., OCT.)

- 137 filas con nombre de cliente (JULIO 29, AGOSTO 29, SEPT. 39, OCT. 40). Otras 9 filas no vacías no tienen nombre: son totales o filas en blanco.
- 80 nombres distintos tal como están escritos; 79 si se ignoran mayúsculas.
- **Duplicados probables**: una comparación automática encuentra 38 pares de nombres parecidos. 6 pares tienen similitud ≥0,9 y parecen variantes de escritura del mismo cliente. Los demás pueden ser personas distintas con el mismo nombre de pila. Hay que confirmar a mano; aquí no se listan los nombres.
- 26 nombres aparecen en más de una fila. Las variantes de escritura pueden ocultar recompras, y eso afecta a BL-004 y BL-060.
- 1 fila con nombre y sin fecha (JULIO), 1 fecha escrita como texto con formato inválido (AGOSTO) y 8 filas con nombre y sin cantidad.
- No hay columnas de origen, canal, responsable ni próximo paso. Los encabezados no vacíos cambian por hoja: 10, 10, 13 y 14 (BL-047 ya lo señala).

**`proximos_pasos_sebastian.xlsx`**

- 10 acciones, las 10 en `Pendiente`, todas con responsable y plazo. La acción 7 ("captura y filtro de leads de WhatsApp/IG hacia el CRM", Sebastián + Omar, nov–dic) es la que este aporte apoya.

**Preguntas abiertas**

1. ¿Cuál de los 3 números de WhatsApp es el comercial? ¿Cuál es el horario y quién es el suplente?
2. ¿Dónde vivirá el registro privado mientras llega Odoo (BL-011)? ¿Quién tiene acceso?
3. ¿Hoy se anota en algún lugar quién escribió por Instagram y no compró? (BL-059 lo medirá).
4. ¿Qué cantidad de kilos cuenta como "volumen alto"? Hoy es `desconocido`.
5. ¿"Almacén" en el Excel significa tienda, veterinaria o distribuidor?
6. ¿Cuáles son las zonas con entrega confirmada?
7. ¿Se aprobó o contactó alguno de los 17 prospectos `borrador listo`?

---

## 7. Hechos (con fuente) e hipótesis

### Hechos (con fuente)

- Omar atiende WhatsApp y recibe pedidos; la responsable de la operación factura y coordina entregas. Fuente: `erp.md` §2 "Equipo y responsabilidades" y §4 "Flujo actual de pedidos".
- Hay 3 números de WhatsApp publicados y no está definido el comercial principal. Fuentes: `CANIVOROS-REFERENCIA-EMPRESA.md`, BL-059.
- Nadie contacta prospectos B2B sin aprobación de Andrés. Fuentes: `AGENTS.md`, `prospectos/AGENTS.md`.
- El registro de prospectos no tiene responsable ni próximo paso. Fuente: `prospectos/prospectos-2026-11-03.csv` (columnas).
- El Excel de ventas no tiene origen ni canal, cambia de columnas por hoja y tiene nombres de cliente con variantes de escritura. Fuentes: `ventas_canivoros_2026.xlsx`, BL-047.
- Hay pedidos de criadores de 40 a 520 kg. Fuente: BL-043, sobre `ventas_canivoros_2026.xlsx`.
- Existen etapas y reglas de seguimiento propuestas (24 h, 72 h, día 3 y día 10). Fuentes: `embudos/E01-…/embudo.md`, `embudos/E02-…/embudo.md`.
- El piloto se concentra en perros y en Bogotá. Fuente: `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`.

### Hipótesis (a validar)

- Los pesos del puntaje y los cortes 70/45/20. Se validan con 4 semanas de registro y con la auditoría BL-059.
- Que pedir precio o pedido predice compra mejor que pedir información.
- Que la ventana B de 5 días hábiles no pierde ventas.
- Que se pierden ventas por respuesta lenta o sin seguimiento (hipótesis de BL-059).
- Que 14 días es el umbral correcto de estancado para cada etapa.
- Los 6 pares de nombres parecidos del Excel son el mismo cliente: falta confirmarlo.
