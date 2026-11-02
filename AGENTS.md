# Instrucciones para agentes · Canívoros / Gatívoros

> Aplica a cualquier agente de IA (Claude, ChatGPT, Gemini, Codex, Cursor u otro) que trabaje en este repositorio.
> Si la carpeta en la que vas a trabajar tiene su propio `AGENTS.md`, léelo completo: en lo específico manda sobre este archivo.
> Última actualización: 2026-11-02.

---

## 1. Qué es este proyecto

Este repositorio es el trabajo de **crecimiento comercial y sistematización de Canívoros**, una pyme colombiana de alimento natural para mascotas. El objetivo es **aumentar las ventas rentables y recurrentes en Bogotá con un proceso medible**: medir → diagnosticar → priorizar → experimentar → escalar (ver `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`).

Es también el **primer caso del servicio Growth Partner** de Andrés y Sebastián (ver `pasos_sysmkt.md` y BL-017, BL-030, BL-045): lo que se aprenda aquí debe quedar documentado y medido en COP frente a una línea base.

### La empresa

- **Marcas:** **Canívoros** (perros) y **Gatívoros** (gatos). Lema: «Cuídalo cada día, ámalo toda la vida».
- **Planta:** Sopó (Cundinamarca). **Mercado objetivo de este trabajo:** Bogotá.
- **Origen declarado:** experiencia familiar en la crianza de perros de competencia. Es su principal activo de confianza.
- **Producto según la operación** (`erp.md`, `ventas_canivoros_2026.xlsx`): alimento horneado elaborado sobre todo con subproductos de pollo, salmón y cerdo (también hay una receta de ternera), en formatos de **hamburguesas y chorizos**; el Excel de ventas también registra «NUC.» (significado por confirmar) y orejas. Se vende por **libra / 500 g** al cliente final y a tiendas, y por **kilo** a criadores (venta por volumen, mínimo relatado de 40 kg).
- **Producto según la marca** (`CANIVOROS-REFERENCIA-EMPRESA.md`): «alimento natural horneado, super premium, listo para servir». Ojo: este discurso tiene contradicciones con la operación (§4).
- **Canales actuales:** WhatsApp (Omar), contactos del mundo canino, criadores y unos 3–4 puntos de distribución relatados (el sitio publica 6, dos en Bogotá: Clínica Veterinaria Manimal y Sankatin PetShop).

### Personas

| Persona | Rol en el proyecto |
|---|---|
| **Andrés Muñoz (Andy)** | Growth partner, unas **4 h por semana**. Decide prioridades y **aprueba todo contacto externo y toda publicación**. |
| **Sebastián** | Parte técnica: Odoo, datos, infraestructura. Responsable propuesto de la mayoría de requisitos del backlog. |
| **Omar** | Ventas y atención por WhatsApp; su trayectoria con perros de competencia genera la confianza de los compradores. |
| **Responsable de la operación** | Materia prima, facturación, producción, pedidos, entregas y registro de ventas. En el backlog aparecen «la prima» y Sara como interlocutoras de la operación; nombre y cargo por confirmar (`erp.md` §13). |
| **Tres operarios** | Producción y preparación de pedidos. |
| **Santiago** | Distribuidor. Hay una propuesta de llevarle clientes y compartir el resultado, sin acuerdo cerrado. |
| **Hermano de Sebastián** | Apoyo comercial propuesto para el contacto con tiendas (BL-012, junto con Omar). |

Los responsables y fechas del backlog son **propuestas**, no compromisos.

## 2. Mapa del repositorio y fuentes de verdad

| Ruta | Qué es | Cómo tratarlo |
|---|---|---|
| `CANIVOROS-REFERENCIA-EMPRESA.md` | Lo que **declara la marca** en su sitio (oct 2026) | Declaraciones (D), no hechos verificados |
| `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` | Plan comercial y de sistematización: microzonas, entrevistas, experimentos, indicadores, 90 días | Marco de trabajo; sus umbrales son propuestas |
| `erp.md` | Levantamiento operativo (audios y WhatsApp transcritos): compras, cuarto frío, producción, pedidos, catálogo y precios relatados | Relato de la empresa (D), no auditado. **No lo reescribas**: es un registro de fuentes |
| `ventas_canivoros_2026.xlsx` | Ventas jul–oct 2026 en lb/kg por cliente, fecha y producto (sin precios) | **Contiene nombres de clientes**: usa solo agregados (§3) |
| `metodologias_analisis_competitivo.md` | Métodos de análisis competitivo y QFD | Método base de `competencia/` |
| `pasos_sysmkt.md` | Descubrimiento de producto, funnel y oferta Growth Partner | Contexto del servicio, no de Canívoros |
| `GuiaPesquisa*.md`, `GuiaDesenvolver*.md` | Guías de investigación y desarrollo de productos (ES y PT) | Método para entrevistas, hipótesis y pilotos |
| `QFD.pdf` | Material de referencia de QFD | Insumo de BL-024 |
| `backlog/` | Tareas BL-001 a BL-058 ordenadas por semanas, con dependencias | Fuente de prioridades: `backlog/README.md` |
| `prospectos/` | Solo instrucciones: playbook de investigación de mercado y prospección de clientes en Bogotá | `prospectos/AGENTS.md` |
| `competencia/` | Solo instrucciones: playbook de inteligencia competitiva en Bogotá | `competencia/AGENTS.md` |
| `resultados/` | Entregables de los agentes (`resultados/prospectos/`, `resultados/competencia/`). Se crea al trabajar | Lo definen los playbooks |

Este repo **no** es la tienda online, ni el ERP, ni la contabilidad. El código y la configuración de Odoo viven en otros repositorios (`canivorosodoo`, `canivoros-view`). En la rama `backlog` hay propuestas BL-059 a BL-061 que aún no están en `develop`: no las cites como vigentes.

## 3. Reglas comunes (no negociables)

### Evidencia

Usa las mismas etiquetas en todo el repo:

| Etiqueta | Significa | Ejemplo |
|---|---|---|
| **(E)** Hecho verificado | Lo observaste en una fuente, con URL o documento y fecha | «Vende Pixie: foto de estantería en Maps, 2026-11-05» |
| **(D)** Declaración | Lo que dice la marca, un cliente, un aliado o un competidor | «Sin conservantes químicos» (sitio de Canívoros) |
| **(H)** Hipótesis | Tu interpretación; debe poder probarse | «Las tiendas que ya venden BARF reponen más rápido» |
| **(V)** Por validar | Dato dudoso, sin fecha, de fuente secundaria o que exige una conversación | Precio de un competidor sin fecha de captura |

- Lo que no se sabe se escribe **`desconocido`**. Desconocido no es cero.
- **Nunca inventes precios, ventas, márgenes, costos, volúmenes ni raciones.** Un ejemplo numérico solo se usa marcado como **ilustrativo**.
- Las cuentas derivadas (precio por kg, totales, porcentajes) se muestran con su fórmula y heredan la etiqueta del dato de origen.
- No encadenes conclusiones sobre datos (V).

### Contacto y publicación

- **Nunca contactes** a clientes, prospectos, distribuidores, proveedores ni competidores (mensajes, llamadas, formularios, correos, compras de prueba, comentarios en redes) **ni publiques nada** sin aprobación explícita de Andrés. Todo mensaje se entrega como **borrador no enviado**.
- Aunque tengas conectores (correo, Slack, WhatsApp, calendario, redes), no los uses para escribir a terceros.

### Datos y seguridad

- **Nunca escribas contraseñas, tokens, llaves ni IPs de servidores** en el repo, en commits ni en el chat. Si encuentras uno, no lo copies: avísale a Andrés y remite a BL-001.
- **No accedas a Odoo, al VPS ni al hosting**, y no pidas credenciales.
- **Datos personales (Ley 1581 de 2012, Colombia):** no guardes cédulas, celulares personales, direcciones de vivienda, correos personales, nombres de clientes finales ni datos de mascotas ligados a una persona. Solo datos comerciales públicos de negocios.
- `ventas_canivoros_2026.xlsx` tiene nombres de personas: trabaja con **agregados** (kilos por mes, canal o producto; número de clientes; recompra) y no copies nombres de clientes a otros archivos, commits ni PR.

### Mensajes de marca (hasta cerrar BL-016)

| Se puede usar en borradores (D de la marca) | No usar hasta tener soporte (BL-016) |
|---|---|
| Alimento horneado para perros | Beneficios de salud: digestión, pelaje, inmunidad, limpieza dental |
| Hecho en Sopó, Cundinamarca (Colombia) | «Sin subproductos» (la materia prima **sí** son subproductos) |
| Proteína de origen animal: pollo, salmón, cerdo | «Super premium», «la mejor calidad», «nadie compite», «el triple de bueno» |
| Listo para servir | «Registro ICA» sin número de registro verificado |
| Nace de la crianza de perros de competencia | Testimonios presentados como resultados esperables |
|  | Precios, pesos o condiciones no confirmados (BL-005) |

Mensaje base del plan, a validar: «Canívoros: alimento horneado para perros, hecho en Colombia, con proteínas de origen animal y listo para servir».

### Forma de trabajar

- **Prioriza según `backlog/README.md`** y respeta sus dependencias. La seguridad (BL-001, BL-052) va primero.
- **Concentra el piloto en perros.** Gatívoros sigue en el catálogo, pero su experimento (BL-026) va después.
- **Todo hallazgo termina en una prueba comercial medible** con la ficha de BL-044: hipótesis · métrica principal (conversión, recompra o COP) · número de casos · gasto máximo · regla de seguir, ajustar o parar.
- **Separa clientes finales, tiendas/almacenes y criadores:** tienen ciclos, precios y costos distintos.
- **Registra el origen de cada venta o contacto** (campaña, aliado, Omar, orgánico): sin origen no se puede cobrar por resultados (BL-021).
- **Andrés tiene unas 4 h por semana:** entrega resúmenes cortos, máximo 3 decisiones que él deba tomar y lo que queda `desconocido`.

## 4. Contradicciones conocidas (no las repitas como hechos)

| Tema | Una fuente dice | Otra fuente dice | Qué hacer |
|---|---|---|---|
| Ingredientes | Sitio: sin harinas procesadas, subproductos ni conservantes químicos | `erp.md`: cabezas de pollo, barriga de salmón, canilla y vísceras de cerdo | No usar «sin subproductos»; describir el ingrediente real (BL-016) |
| Formato y conservación | Sitio: textura crujiente; guardar en lugar fresco y seco | `erp.md`/Excel: hamburguesas y chorizos que se deterioran después de abiertos | Conservación del producto terminado y necesidad de frío en tienda: `desconocido` (BL-005) |
| Unidad de venta | «Libra» | «500 g»; el Excel mezcla lb y kg | No convertir sin confirmar la unidad (BL-005) |
| Precios | `erp.md` §5: precios al público y a distribuidor relatados | El precio a distribuidor del cerdo pasó de 35.000 a 3.500 (corrección de la empresa, 26/10/2026) | Ningún precio de Canívoros en mensajes ni comparaciones hasta BL-005 |
| Receta para gatos | Sitio: salmón y pollo | `erp.md`: salmón y cerdo | Por confirmar con la empresa |
| WhatsApp | Tres números publicados | No hay un número comercial principal definido | No pongas números de Canívoros en borradores: `[número comercial por definir]` |
| Distribuidores | El sitio publica 6 | La empresa relata unos 3–4 puntos activos | Confirmar en BL-035 |
| Registro ICA | La marca afirma tenerlo | No se ha visto número ni soporte | No afirmarlo en material comercial |
| Ganancia de gatos | Audio: 4,8 millones por tonelada | Con los precios relatados la diferencia bruta es 9,6 millones (no es ganancia) | No usar ninguna de las dos cifras |

## 5. Indicadores (definiciones del plan)

- **Ventas netas:** ventas − descuentos − devoluciones.
- **Contribución antes de captación:** ventas netas − producción, empaque, comisiones, medios de pago y entrega variables. No es utilidad neta.
- **Contribución después de captación:** lo anterior − gasto comercial atribuible.
- **CAC:** gasto de captación del segmento y periodo ÷ clientes nuevos compradores.
- **Conversión:** contactos calificados que compran ÷ contactos calificados de la misma cohorte.
- **Recompra a 30 o 60 días:** clientes con segunda compra en la ventana ÷ clientes que ya completaron esa ventana.
- **Rotación de aliados:** venta al consumidor (si se conoce) y frecuencia de reposición, por separado. Una compra inicial de una tienda no demuestra demanda.

## 6. Convenciones de escritura

- **Idioma:** español de Colombia, frases cortas, tablas cuando ayuden. Las guías en portugués (`*PT.md`) son copias de referencia; no hace falta mantenerlas sincronizadas salvo que se pida.
- **Fechas:** `AAAA-MM-DD`. **Dinero:** COP con punto de miles (`$12.960` o `COP 12.960`), indicando presentación (g o kg) y si es precio regular o promoción.
- **Teléfonos de negocios:** celular `3xx xxx xxxx` (10 dígitos), fijo `601 xxx xxxx`.
- **IDs estables:** `BL-###` (backlog), `P###` (prospectos), `C##` (competencia). No se reutilizan ni se renumeran.
- **Backlog:** si editas un `BL-*.md`, actualiza `backlog/README.md` y regenera `TODAS-LAS-TAREAS.md` y `TODAS-LAS-TAREAS-SIN-REFERENCIAS.md`.
- **Documentos fuente** (`erp.md`, `CANIVOROS-REFERENCIA-EMPRESA.md`): no corrijas el relato para que «cuadre». Si algo cambia, agrégalo como nota fechada o en el archivo de trabajo que corresponda.

## 7. Git

- Trabaja en una rama (`docs/...`, `backlog`, `feat/...`, `prospectos/...`) creada desde `develop` y propone cambios por **PR hacia `develop`**.
- **Un PR por propósito.** Antes de abrirlo, revisa que el diff solo incluya los archivos esperados.
- Mensajes de commit en español con prefijo: `docs:`, `backlog:`, `prospectos:`, `competencia:`, `fix:`.
- No hagas push forzado sobre ramas compartidas ni reescribas historia publicada.
- En la descripción del PR di qué cambia, qué no cambia y confirma que **nadie fue contactado** y que no hay datos personales ni secretos.
