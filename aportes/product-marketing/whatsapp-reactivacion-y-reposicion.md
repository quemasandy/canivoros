# Guiones de WhatsApp: reactivación y reposición

Borrador 1 · 10 nov 2026 · **Nada de esto está aprobado ni se ha enviado.** Lo envía Omar a mano, uno por uno, desde el número comercial que se defina (BL-059). No es una automatización.

Apoya: BL-060 y embudo E02 (reactivación), BL-022 (reposición), BL-043 (criadores) y BL-058 (permiso). Voz: `branding/02-personalidad-y-voz.md` §2 y §3 (tuteo, frases cortas, una pregunta por mensaje, máximo un emoji). Ninguno de estos mensajes lleva emoji para no gastar el único permitido.

## Antes de enviar cualquier guion

1. **Permiso.** Solo a quien tenga permiso registrado (BL-058; E02 §2). Sin permiso, no se escribe en frío para pedirlo. [falta: texto de autorización aprobado y criterio para clientes que ya le escribieron a Omar antes de BL-058].
2. **Lista.** Sale de BL-004 con criterio escrito. La lista vive en el registro privado (Excel u Odoo), nunca en el repo. Sin nombres, teléfonos ni chats en GitHub.
3. **Sin queja abierta.** Si el cliente tiene una incidencia o un pedido abierto, no se envía.
4. **Datos de la cotización.** Precio, peso neto, costo y fecha de entrega salen de BL-005 y de operaciones el mismo día. Si falta uno, no se cotiza: se dice "lo confirmo y te escribo" (E02 §5.2).
5. **Límites.** Hasta 5 contactos nuevos por día y máximo 2 mensajes proactivos sin respuesta por persona (E02 §6, propuesta). Si dice que no, se registra y se para.
6. **Prueba de 4 preguntas** de `branding/02` §6 antes de usar cualquier variante nueva.

**Cómo leer cada guion.** Las variables van entre corchetes. El conteo de caracteres es del mensaje tal como está escrito, con las variables sin reemplazar; al reemplazarlas cambia. Meta: menos de 300.

**Qué dice la marca en estos mensajes.** A propósito, casi nada. Ningún guion usa beneficios de salud, "sin subproductos", "horneado elimina bacterias", "super premium", ICA ni descuentos. El único dato de marca recurrente es "Canívoros" y el nombre del producto (Hecho: catálogo Odoo, `branding/05`).

---

## (a) Reactivación: cliente final con una sola compra

- **Objetivo:** saber qué pasó después de la primera compra. Vender es secundario.
- **Cuándo:** cliente final (no criador ni tienda) con una compra en jul a oct 2026 (BL-004), permiso registrado y sin pedido abierto. La ventana de espera la define Andrés con BL-004. E02 §2 pide no asumir abandono solo porque pasaron 30 días. [falta: ventana aprobada].
- **Variables:** [nombre], [mes de la compra], [producto], [nombre del perro] (solo si se sabe).

**Mensaje principal (232 caracteres):**
> Hola, [nombre]. Soy Omar, de Canívoros. En [mes de la compra] llevaste [producto] para [nombre del perro] y quería saber cómo le fue. ¿Hubo algo que te frenó para volver a pedir? Si prefieres que no te escriba más, me dices y listo.

**Variante sin nombre del perro (213 caracteres):**
> Hola, [nombre]. Soy Omar, de Canívoros. En [mes de la compra] nos compraste [producto] y quería saber cómo te fue. ¿Hubo algo que te frenó para volver a pedir? Si prefieres que no te escriba más, me dices y listo.

- **Claims:** ninguno. Solo el nombre del producto (Hecho).
- **Siguiente paso:** según la respuesta, ir a (f). Registrar el motivo en la tabla de cierre aunque no compre.

## (b) Reactivación: cliente que repetía y lleva más de 60 días sin pedir

- **Objetivo:** entender por qué paró y, si quiere, facilitar el pedido de siempre.
- **Cuándo:** cliente con 2 o más compras en BL-004, sin compra hace más de 60 días **y** más de 1,5 veces su intervalo habitual (criterio de E02 §2, supuesto de selección). Las dos condiciones a la vez evitan escribirle a quien compra cada 70 días. Revisar uno por uno antes de enviar.
- **Variables:** [nombre], [producto habitual], [nombre del perro].

**Mensaje principal (240 caracteres):**
> Hola, [nombre]. Soy Omar, de Canívoros. Hace rato no te preparamos el [producto habitual] de [nombre del perro]. ¿Pasó algo con el producto, la entrega o el precio que me quieras contar? Si prefieres que no te escriba más, me dices y listo.

- **Claims:** ninguno.
- **Nota:** la pregunta nombra tres motivos concretos para que responder sea fácil. No ofrece nada todavía.

## (c) Criador de volumen

- **Objetivo:** conversación de colega a colega (`branding/02` §2, fila "Criadores y tiendas") para conocer qué le impide reponer. Es la entrevista de BL-043; todavía no se ofrece nada.
- **Cuándo:** criadores del top 10 por kilos de BL-043, con relación activa con Omar. E02 deja a los criadores fuera de su piloto; este guion va por BL-043 y se mide aparte.
- **Variables:** [nombre], [producto habitual].
- **No decir todavía:** precio por kilo, mínimo de compra ni "pedido programado". La regla de mínimo es inconsistente en las fuentes (40 kg frente a paquetes de 1,5 kg, `erp.md`, sección "Catálogo y precios mencionados") y BL-005 no la ha cerrado. `branding/05` ficha 6 dice que las condiciones de volumen no se publican.

**Mensaje principal (280 caracteres):**
> Hola, [nombre]. Soy Omar, de Canívoros. Estoy hablando con los criaderos que nos compran por volumen para entender qué les funciona y qué no. ¿Qué tendríamos que mejorar para que reponer el [producto habitual] te quede más fácil? Si prefieres que no te escriba por esto, me dices.

- **Claims:** ninguno. Evité "de criador a criador" (`branding/03` §3, Propuesta) porque depende de que el origen familiar en crianza esté confirmado como Declaración usable. Si el bot Canívoros lo aprueba, se puede abrir con esa frase.
- **Siguiente paso:** anotar respuesta literal resumida (sin datos personales) para BL-043. Si pide precio: "Te lo confirmo hoy con [responsable de la operación] y te escribo." [falta: precio por volumen vigente BL-005].

## (d) Recordatorio de reposición según el intervalo del cliente

- **Objetivo:** que pedir otra vez le cueste un mensaje.
- **Cuándo:** solo a quien aceptó recordatorios con (e). Versión 1 de BL-022: fecha según el intervalo real del cliente en BL-004 o la fecha que él eligió. **No** se calcula con raciones: la guía no existe (BL-041), así que nada de "ya se te debe estar acabando".
- **Variables:** [nombre], [producto habitual], [nombre del perro].

**Si el cliente eligió la fecha (245 caracteres):**
> Hola, [nombre]. Soy Omar, de Canívoros. Quedamos en escribirte por estos días para el [producto habitual] de [nombre del perro]. ¿Te lo preparo como la última vez o prefieres que te escriba en otra fecha? Si ya no quieres estos avisos, me dices.

**Si la fecha sale de su intervalo habitual (233 caracteres):**
> Hola, [nombre]. Soy Omar, de Canívoros. Por cómo has venido pidiendo, ya se acerca la fecha en que sueles reponer el [producto habitual]. ¿Te lo preparo como la última vez o prefieres esperar? Si ya no quieres estos avisos, me dices.

- **Claims:** ninguno.
- **Siguiente paso:** si dice que sí, cotización completa con (f) "Sí quiero". Si pide otra fecha, cambiarla en el registro y cancelar el aviso anterior (E02 §6).

## (e) Pedir permiso para recordatorios

- **Objetivo:** dejar registrado el permiso (BL-058) para poder usar (d).
- **Cuándo:** solo dentro de una conversación que el cliente ya tiene abierta, después de un pedido entregado sin problemas (E02 §5.5). Nunca como primer mensaje.
- **Variables:** [enlace al aviso de privacidad aprobado]. [falta: aviso de privacidad y texto de autorización aprobados por la empresa; BL-058 pide revisarlo con alguien que conozca la norma colombiana].

**Mensaje principal (266 caracteres):**
> Antes de despedirme: ¿te sirve que te escriba por aquí cuando se acerque la fecha de reponer? Tú me dices cada cuánto y lo cancelas cuando quieras. Ningún pedido sale sin que tú lo confirmes. Aquí está cómo usamos tus datos: [enlace al aviso de privacidad aprobado].

- **Claims:** "Ningún pedido sale sin que tú lo confirmes" es una regla de operación (E02 §3, "sin cobro automático"). Confirmar con la responsable de la operación antes de usarla.
- **Registro:** respuesta (sí o no), fecha, canal y cada cuánto. Un "no" no cambia la atención.

## (f) Respuestas cortas a lo más probable

Las cuatro respuestas vienen de las hipótesis de E02 §2 y §5.4. Cuáles son de verdad las más frecuentes lo dirá la auditoría de BL-059.

### Precio ("está caro")

**Respuesta (225 caracteres):**
> Gracias por decírmelo. Para que compares con calma, este es el total de hoy: [producto] de [peso neto], [precio vigente BL-005], entrega a [zona] [costo de entrega vigente]. ¿Hay algo más que quieras revisar antes de decidir?

- Sin precio por día, sin "rinde más", sin comparar con concentrado: no hay ración confirmada (BL-041) ni costo por kilo comparable.
- No ofrecer descuento. Si la empresa autoriza uno, se agrega con su condición escrita. [falta: política de descuentos].
- Si existe una presentación menor en el catálogo vigente, mencionarla. Hoy las fuentes solo muestran 500 g y 1,5 kg (BL-005).

### No le gustó o le cayó mal

**Primera respuesta (84 caracteres):**
> Gracias por contarme, me sirve mucho. ¿Qué pasó: no se lo quiso comer o le cayó mal?

**Si le cayó mal (180 caracteres):**
> Lo reviso con el equipo. Si [nombre del perro] sigue con malestar, consúltalo con su veterinario antes de cambiarle la comida. No te vuelvo a ofrecer pedido hasta que lo aclaremos.

- Registrar como incidencia y avisar a la responsable de la operación con el lote si se conoce. Omar no da consejo veterinario (E02 §6). El sitio ya remite al veterinario en casos clínicos (FAQ en /productos/).
- Si no se lo quiso comer: anotar producto y especie. Para Gatívoros, la dueña ya relató rechazo cuando el paquete lleva días abierto (`erp.md`, "Oportunidad del producto para gatos"). No prometer cambio ni devolución. [falta: política de devoluciones].

### Ya compro otra marca

**Primera respuesta (64 caracteres):**
> Entiendo, gracias por contarme. ¿Qué fue lo que te hizo cambiar?

**Cierre (102 caracteres):**
> Gracias, lo anoto. No te escribo más por esto. Si un día quieres volver a pedir, me escribes por aquí.

- No hablar mal de la otra marca (`branding/02` §4; `branding/03` §5).
- Si dice que compra Canívoros en una tienda, registrar "otro canal" y no tratarlo como perdido (E02 §5.4).

### Sí quiero

**Cotización (204 caracteres):**
> ¡Listo! Te confirmo: [cantidad] de [producto], [precio vigente BL-005], entrega a [zona] [costo de entrega vigente]. Total: [total en COP]. Te llega el [fecha confirmada por operaciones]. ¿Te lo dejo así?

**Cuando confirma (80 caracteres):**
> Perfecto. Te mando [medio de pago autorizado] y te aviso cuando salga el pedido.

- Se envía solo con todos los datos reales (E02 §5.2). Si falta uno, "lo confirmo y te escribo".
- Datos de facturación (nombre, cédula, teléfono, correo, según `erp.md` §4) solo si son nuevos o cambiaron. No pedir datos de tarjeta por chat.
- Pago y entrega se registran por separado: la venta cuenta cuando está pagada **y** entregada.

---

## Cómo medir la prueba de 14 días

Ventana: 14 días desde el primer mensaje de cada persona (BL-060). Este archivo no pone metas ni tasas esperadas. La meta propuesta está en E02 §1 y la aprueba Andrés.

**Reglas de conteo**
- Personas únicas. Un mensaje que no llegó sigue contando como contactado y se anota aparte.
- "Respondió" es cualquier respuesta, incluso "no me interesa".
- "Pedido pagado y entregado" exige las dos fechas.
- Las compras por cualquier canal dentro de los 14 días cuentan, aunque no haya respondido (E02 §7).
- Motivos de no compra con la lista cerrada de E02 §6: precio, entrega, falta de stock, aún tiene producto, otra marca, otro canal, experiencia negativa, no responde, otro, desconocido.
- Este registro se llena en el Excel u Odoo privado. Al repo solo suben los totales.

### Registro por contacto (privado)

| ID interno | Guion (a/b/c/d) | Fecha 1.er mensaje | ¿Llegó? | ¿Respondió? (fecha) | Motivo dicho | Cotizado (fecha) | Pagado (fecha) | Entregado (fecha) | Pidió no recibir más | Notas sin datos personales |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

### Resumen al día 14 (este sí puede ir al repo)

| Guion | Contactados | Mensajes que no llegaron | Respondieron | Cotizados | Pagados y entregados | Bajas | Kilos entregados | COP (solo con precio confirmado) |
|---|---|---|---|---|---|---|---|---|
| (a) una compra | | | | | | | | |
| (b) repetidor inactivo | | | | | | | | |
| (c) criador | | | | | | | | |
| (d) reposición | | | | | | | | |

### Motivos de no compra

| Motivo | (a) | (b) | (c) | (d) |
|---|---|---|---|---|
| Precio | | | | |
| Entrega | | | | |
| Falta de stock | | | | |
| Aún tiene producto | | | | |
| Otra marca | | | | |
| Otro canal | | | | |
| Experiencia negativa | | | | |
| No responde | | | | |
| Otro | | | | |
| Desconocido | | | | |

Con pocos contactos, el resultado se toma como indicio (criterio de BL-020). La decisión de seguir, ajustar o parar se escribe antes de empezar en la ficha de BL-044.
