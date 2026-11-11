# Playbook de conversación de ventas — Canívoros / Gatívoros

Versión 1 · 10 nov 2026 · Aporte de psicología de ventas (ético) para WhatsApp e Instagram DM.

**Para quién:** quien atiende al dueño de un perro o un gato (hoy, en la práctica, Omar).  
**Para qué:** detectar el estilo de comunicación del comprador, hacer preguntas útiles, responder objeciones sin inflar el producto y cerrar o dar seguimiento sin presión.  
**Qué no es:** no sustituye a `branding/` (voz, mensajes y prohibiciones) ni a los embudos E01–E04. Los complementa en el momento de la conversación. La carpeta `branding/` vive en la rama `branding` del fork; si se une a `develop`, úsala como fuente de tono.

Nada de este documento está aprobado por la empresa. No publicar, no enviar a clientes como PDF de marca y no usar cifras, testimonios ni claims que no estén confirmados.

---

## 1. Cómo usar este playbook

1. Lee primero la sección 2 (reglas) y la 3 (hechos frente a hipótesis).
2. En los primeros intercambios, forma una **hipótesis de perfil** (A, B, C o D). No se la digas al cliente. Si las señales cambian, cambia el tono.
3. Copia los mensajes de ejemplo y reemplaza los placeholders. Si un dato está entre corchetes y no lo tienes, no lo improvises: dilo o pregunta a la empresa.
4. Si el chat es con una tienda, una veterinaria o un criador de volumen, este playbook sirve solo para el tono. Las condiciones comerciales salen de BL-005 y BL-043, todavía sin confirmar.

### Placeholders

| Placeholder | Qué poner | Si no lo tienes |
|---|---|---|
| `[nombre]` | Nombre de la persona | Omítelo |
| `[perro]` / `[gato]` / `[mascota]` | Nombre del animal | «tu perro» / «tu gato» |
| `[producto]` | Nombre y presentación confirmados (ej. chorizos de pollo y salmón 500 g) | Pregunta disponibilidad; no inventes SKU |
| `[precio]` | Precio vigente del canal, confirmado (BL-005) | No cotices. Di que te confirmas y vuelves |
| `[zona]` | Barrio o ciudad | Pregúntala antes de prometer entrega |
| `[fecha de entrega]` | Fecha que operations pueda cumplir | No la adelantes |
| `[instrucción de conservación]` | Cómo guardar ese producto, confirmado por la empresa | No uses la FAQ del sitio como regla universal |
| `[guía de ración]` | Porción según peso, edad y actividad (BL-041) | No inventes gramos ni «te dura X días» |
| `[número ICA]` | Número de registro del producto | Di que tiene registro solo si la empresa lo confirma, y comparte el número únicamente cuando lo tengas |
| `[testimonio]` | Relato real, con permiso de uso (BL-058) | No uses prueba social |
| `[política de cambio o devolución]` | Condición real de la empresa | No prometas devolución si no existe |

---

## 2. Reglas éticas (no negociables)

1. **No diagnostiques a la persona.** A, B, C y D son hipótesis de estilo en un chat, no un perfil psicológico ni un segmento demográfico. No se infieren por edad, género, barrio, estrato ni por la cantidad de palabras.
2. **No inventes.** Precios, presentaciones, tiempos de entrega, raciones, vida útil, márgenes, «pack de prueba», devoluciones o disponibilidad se dicen solo si están confirmados. Si falta el dato: «te lo confirmo y te escribo».
3. **No hagas claims sanitarios o nutricionales sin respaldo.** Quedan fuera, hasta que BL-016 y la ficha técnica lo permitan: «mejora la digestión», «fortalece el sistema inmune», «limpia los dientes», «heces menos olorosas», «salud articular, cerebral u ocular», «elimina bacterias», «100 % natural», «libre de granos», «super premium», «alimento completo y balanceado», «sin subproductos». La materia prima incluye partes como cabeza de pollo, barriga de salmón y vísceras (`erp.md`, BL-016). Si preguntan, sé transparente y usa la redacción que apruebe la empresa.
4. **Ante una condición clínica** (alergia, enfermedad, recuperación, cachorro o gatito con indicación veterinaria, adulto mayor con tratamiento), no indiques dieta. Deriva al veterinario.
5. **No ataques al concentrado ni nombres a un competidor para desprestigiarlo.** Friskies u otras marcas masivas son la costumbre de muchos gatos, no un enemigo. Habla de lo que es Canívoros, no de lo que el otro «hace mal».
6. **Prueba social solo con casos reales y permiso.** Los testimonios del sitio son experiencias individuales, no un resultado prometido. Los perros de competencia de la marca no prueban que «este alimento hace campeones».
7. **No presiones.** Silencio no es un no. No uses urgencia falsa («último paquete», «solo hoy»). Escasez solo si es real (sin stock, ruta de ese día).
8. **Pide y respeta el permiso** antes de recordatorios o recontactos proactivos (BL-058; ley colombiana de datos). En el primer pedido, el seguimiento operativo (factura, entrega) sí corresponde.
9. **Una idea por mensaje. Tutea. Frases cortas.** Un emoji como máximo en WhatsApp. Usa el nombre de la mascota cuando lo sepas. Voz de Colombia, no de laboratorio ni de anuncio genérico. (Criterio de la rama `branding`, archivo `02-personalidad-y-voz.md`.)

---

## 3. Hechos, declaraciones e hipótesis

### 3.1 Hechos (con fuente)

| Hecho | Fuente |
|---|---|
| Canívoros (perros) y Gatívoros (gatos) son alimento natural horneado, hecho en Sopó, Cundinamarca. El lema del sitio es «Cuídalo cada día, ámalo toda la vida.» | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md`, `README.md` |
| El sitio declara proteínas de pollo, salmón y cerdo; no es crudo ni BARF; está listo para servir. La marca declara registro ICA, sin número en el contenido revisado. | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md` |
| La venta al cliente final se hace sobre todo por WhatsApp. Omar recibe la consulta, toma el pedido y comparte factura y fecha. Por lo general se paga antes del despacho; algunos clientes antiguos pagan después. | `develop`: `erp.md` §2–4 y §2 de la síntesis |
| Hay tres números de WhatsApp publicados; no está definido cuál es el comercial principal: +57 324 460 8114 (inicio), +57 350 805 2712 (Contáctanos), +57 350 655 9910 (distribución, FAQ). | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md`; `backlog/BL-059` |
| Instagram de la marca: https://www.instagram.com/canivoros_col/. Sitio: https://canivoros.com. | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md` |
| El catálogo operativo mencionado incluye, en 500 g: chorizos de pollo y salmón (perros); hamburguesas de pollo y de cerdo; ternera (forma a confirmar); chorizos de salmón y cerdo para gatos. Hay una oferta directa por volumen (pollo y cerdo, 1,5 kg, mínimo relatado de 40 kg). | `develop`: `erp.md` §5; rama `branding`: `branding/05-aplicacion-por-producto.md` |
| El sitio presenta Gatívoros como salmón y pollo; Odoo y `erp.md` como salmón y cerdo. Hay que validarlo. | `develop`: ambas fuentes; `branding/05` |
| Precios, unidades (libra vs 500 g), costos y catálogo definitivo **no están confirmados** para uso comercial. Hay precios *relatados* en `erp.md`, con inconsistencias. No se usan en este playbook. | `develop`: `erp.md` §5 y §9; `backlog/BL-005`; `README.md` («Qué sabemos y qué no») |
| El sitio invita a una guía de raciones, pero no publica cantidades. | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md`; `backlog/BL-041` |
| El sitio indica guardar el producto en un lugar fresco y seco, la bolsa bien cerrada. Eso no está confirmado para chorizos y hamburguesas. La responsable relató que el chorizo puede deteriorarse después de abierto, y que sus gatos pueden dejar de aceptarlo si lleva un par de días abierto. Vida útil y cadena de frío por producto: `desconocido`. | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md`; `erp.md` (audio, producto para gatos y aspectos comerciales); `branding/03` |
| Un paquete de 500 g puede resultar grande para una mascota pequeña. Una presentación de ~200 g es una *idea* a evaluar, no un producto del catálogo. No debe ofrecerse un «pack de prueba» o un gramaje menor hasta que existan. | `develop`: `erp.md`; `backlog/BL-023`; plan Bogotá, Experimento 1 |
| La materia prima incluye cabeza de pollo, barriga de salmón y vísceras. El mensaje «sin subproductos» del sitio está en revisión (BL-016). | `develop`: `backlog/BL-016` |
| Hay testimonios y perros de competencia publicados por la marca. Son experiencias individuales. El permiso de uso en chats no está resuelto (BL-058). | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md`; `backlog/BL-058` |
| El plan de Bogotá concentra el piloto comercial en perros. Gatívoros sigue en el catálogo. | `develop`: `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` |
| Distribuidores publicados (por validar, BL-035): Manimal (Bogotá noroccidente), Sankatin (Bosa), Malcriados (Chía), Terranova (Sopó), Pets & Company (Zipaquirá), Club Canes (Villavicencio). | `develop`: `CANIVOROS-REFERENCIA-EMPRESA.md` |
| Hay ventas registradas jul–oct 2026 por cliente, fecha y producto, sin precios en el Excel del repo. | `develop`: `README.md`; `ventas_canivoros_2026.xlsx` |
| Instagram de @canivoros_col y @friskiesbr **no se pudo leer** en esta entrega (WebFetch agotó tiempo; la rama `branding` documentó el mismo límite el 10 nov 2026, sin iniciar sesión). El análisis de Friskies en `branding/06` se usó solo como referencia de posicionamiento, no como dato de feed. | Intento propio, 10 nov 2026 (America/Guayaquil); rama `branding`: `branding/06-analisis-competidor-friskies.md` |

### 3.2 Hipótesis de este playbook (no son datos)

- Se pierden ventas por respuesta lenta o falta de seguimiento en WhatsApp (`backlog/BL-059`).
- Adaptar el tono al estilo del comprador baja resistencia y sube el cierre, sin cambiar el producto ni el precio.
- El perfil B y el D necesitan más reducción de riesgo (un primer paquete, tiempo, evidencia) que el A y el C.
- En gatos adultos acostumbrados a concentrado, el cambio es más difícil; el público de entrada más razonable es un gatito nuevo (`erp.md` §8; hipótesis de la responsable).
- Friskies (concentrado masivo de gatos) no compite en el mismo estante, pero es la costumbre que Gatívoros tiene que cruzar con honestidad, no con ataque (`branding/06`, hipótesis estratégica).

---

## 4. Los cuatro estilos (hipótesis de trabajo)

Dos ejes: **extrovertido–introvertido** (quiere conversar y decidir en voz alta, o prefiere ir despacio y por escrito) y **emocional–lógico** (decide por cómo se va a sentir la mascota y la confianza, o por datos, costo y proceso).

| Perfil | Ejes | Qué busca | Cómo le hablas |
|---|---|---|---|
| **A** | Extrovertido + emocional | Entusiasmo, la imagen de su mascota contenta, una historia cercana | Cálido, con el nombre de la mascota, sin ficha técnica delante |
| **B** | Introvertido + emocional | Confianza, seguridad, no equivocarse con su animal | Calma, empatía, un paso pequeño, sin urgencia |
| **C** | Extrovertido + lógico | Resultado concreto y una decisión rápida | Directo: qué es, qué incluye, cuánto, cuándo llega |
| **D** | Introvertido + lógico | Ingredientes, proceso, riesgos, costo y evidencia | Datos verificables, documentos, tiempo para revisar |

Si no puedes decidir todavía, usa un tono **neutro**: una pregunta, un hecho, una invitación. No arranques con un discurso largo ni con el precio suelto.

---

## 5. Cómo detectar el perfil en el chat

Mira **qué pregunta, qué comparte y cómo reacciona a tu siguiente mensaje**. No cuentes palabras. No uses edad, género ni «parece de estrato X». Forma la hipótesis en los primeros dos o tres intercambios y corrígela si aparece una señal fuerte en otro sentido.

### Señales de A

- Manda foto o video de la mascota sin que se lo pidas.
- Cuenta una anécdota («hoy no quiso desayunar», «es muy mañoso»).
- Pregunta si «le va a encantar» o cómo se lo va a imaginar comiendo, más que la receta.
- Responde rápido, en varios mensajes seguidos, y sostiene la conversación.
- Usa el nombre de la mascota con cariño y pide recomendación personal («tú qué le darías»).

### Señales de B

- Entra con duda o cuidado: «tengo miedo de cambiarle», «no quiero que le caiga mal», «mejor lo pienso».
- Pregunta si es seguro, si otros lo han dado, o si puede empezar «con poquito».
- Mensajes cortos, pero con carga emocional; no rellena con datos.
- Se apaga si sientes prisa, si tiras un precio de entrada o si lo empujas a decidir ya.
- Menciona al veterinario desde la precaución, no desde la exigencia de un análisis.

### Señales de C

- Va al grano: «¿cuánto cuesta?», «¿qué manejan?», «¿en cuánto me llega a [zona]?».
- Pide una recomendación cerrada: «dime cuál y ya».
- Compara opciones o marcas de forma práctica, no sentimental.
- Se impacienta con preámbulos, emojis de más o preguntas que no avanzan el pedido.
- Quiere condiciones claras: presentación, precio, entrega, forma de pago.

### Señales de D

- Pregunta ingredientes, porcentajes, proceso de horneado, conservación, vida útil, registro, ficha técnica o si es alimento completo.
- Pide evidencia, no opiniones: «¿tienen análisis?», «¿me mandas la tabla?».
- Calcula o anticipa costo al mes, ración, merma, riesgos del cambio de dieta.
- Quiere leer con calma y volver después. No es evasión: es su forma de decidir.
- Detecta una generalización («es el mejor», «100 % natural») y pide precisión.

### Combinaciones y cambios

- Alguien puede abrir como C («¿precio?») y pasar a B cuando aparece el miedo a que no coma. Sigue el miedo: ahí está la objeción real.
- Si mandas un dato y te responden con una historia, prueba tono A. Si te responden con otra pregunta técnica, prueba tono D.
- En duda entre B y D: no presiones y ofrece un dato concreto más un paso pequeño. El D te pedirá el documento; el B te dirá que lo quiere pensar por su mascota.

---

## 6. Preguntas de descubrimiento

Haz **una o dos por turno**, no un cuestionario. Empieza por lo que la persona ya trajo. El objetivo es recomendar bien y no prometer lo que no puedes cumplir (entrega, ración, producto para una condición clínica).

### Núcleo (todos los perfiles, dueños de perros o gatos)

1. «¿Es para perro o para gato? ¿Cómo se llama?»
2. «¿Cuánto pesa, más o menos, y qué edad tiene?»
3. «¿Qué le estás dando hoy?»
4. «¿Qué te hizo buscar otra comida?»
5. «¿En qué barrio o ciudad estás?» (antes de hablar de entrega)
6. Si aparece un tema de salud: «¿Tu veterinario ya te indicó algo sobre su dieta? Si es un caso clínico, lo mejor es que lo revisen con él o ella antes de cambiar.»

No inventes la ración a partir del peso. Si BL-041 no está confirmada, ofrece pasar la consulta a la empresa o al veterinario.

### Cómo preguntar según el perfil

**A.** Apóyate en la mascota.  
«¡Hola, [nombre]! ¿Cómo se llama tu [perro] y qué le gusta más de lo que come hoy?»  
Luego: «Cuéntame qué te gustaría que cambiara en su día a día, y te armo una recomendación sencilla.»

**B.** Da permiso para ir despacio.  
«Con gusto te ayudo, sin apuro. Para no equivocarnos: ¿cómo se llama, qué come hoy y hay algo que te preocupe del cambio?»

**C.** Sé breve y útil.  
«Te oriento en un momento. ¿Perro o gato, peso aproximado, zona de entrega y si ya tienes un producto en mente?»

**D.** Abre con precisión y ofrece evidencia después.  
«Para recomendarte bien: especie, peso, edad, qué come hoy y si necesitas ficha, conservación o registro. Te mando solo lo que esté documentado.»

### Preguntas que evitas

- No preguntes «¿cuánto estás dispuesto a gastar?» como filtro. Si el precio aparece, explícalo con contexto (sección 8).
- No pidas cédula, correo ni datos de facturación hasta que haya intención clara de pedido (`erp.md`: esos datos entran al armar el pedido).
- No preguntes «¿por qué no le das BARF?» ni «¿todavía le das concentrado?» con tono de reproche.

---

## 7. Flujo de la conversación

Orden que no debes invertir: **escuchar → entender el caso → explicar el producto en resultados o hechos (según perfil) → precio con contexto → cierre o siguiente paso.**

Un precio sin contexto pesa más de lo que debería. Un discurso técnico antes de saber si es perro o gato, también.

### Paso 1 · Apertura (respuesta rápida)

Preséntate, agradece el mensaje y haz una sola pregunta útil. No sueltes el catálogo completo.

**Neutro / si aún no hay perfil**

> Hola, [nombre]. Soy [tu nombre], de Canívoros. ¿Es para perro o para gato, y cómo se llama?

**A**

> ¡Hola! Qué gusto que nos escribas. Soy [tu nombre], de Canívoros. ¿Cómo se llama tu peludo y qué te gustaría mejorar en su comida?

**B**

> Hola, [nombre]. Soy [tu nombre], de Canívoros. Con calma te cuento y tú decides. ¿Cómo se llama tu mascota y qué come hoy?

**C**

> Hola, [nombre]. Soy [tu nombre], de Canívoros. Dime peso, zona y si es perro o gato, y te paso la opción concreta con precio y entrega.

**D**

> Hola, [nombre]. Soy [tu nombre], de Canívoros. Te respondo con datos. ¿Qué necesitas primero: ingredientes, conservación, presentaciones o cómo hacer el pedido?

### Paso 2 · Encaje del producto (sin claims)

Hechos que sí puedes usar, como declaración de la marca, mientras no se contradigan con la ficha: es comida horneada en Sopó, con proteína animal (pollo, salmón, cerdo; ternera solo si la empresa confirma disponibilidad), no es crudo ni BARF, llega listo para servir. Elige el producto según especie y lo que la persona busque (variar proteína, gato, volumen). No prometas un beneficio de salud.

**A** — pinta el momento, no la receta:  
> Canívoros es comida de verdad, horneada en Sopó, lista para servir. Para [perro] yo empezaría con [producto]. ¿Te cuento cómo se lo sirves?

**B** — seguridad y un paso chico:  
> Es un alimento horneado, no crudo. Para empezar con calma, lo habitual es un paquete de [producto] y ver cómo lo acepta [mascota]. Si quieres, te explico también cómo guardarlo.

**C** — tres líneas y una pregunta de cierre:  
> [Producto], presentación [peso confirmado]. Horneado en Sopó, listo para servir. Precio: [precio]. Entrega a [zona]: [fecha de entrega o «te confirmo la fecha»]. ¿Te armo el pedido?

**D** — hechos y oferta de documento:  
> [Producto]: proteína [X], formato [chorizo/hamburguesa], [peso], hecho en Sopó. No es dieta cruda. Conservación: [instrucción de conservación]. Si quieres, te comparto la ficha o el registro cuando los tenga a la mano. ¿Qué punto quieres revisar primero?

### Paso 3 · Cierre (pedir el pedido o el siguiente paso)

Nunca cuelgues la conversación en un «cualquier cosa me dices». Deja un sí concreto o una cita de seguimiento.

- **A:** «¿Te reservo [producto] para [mascota] y te paso los datos del pedido?»
- **B:** «Si te parece bien, podemos empezar con un paquete de [producto] y hablamos cuando lo pruebe. ¿Lo armamos?»
- **C:** «¿Lo dejamos en [producto] a [precio], entrega [fecha]? Si sí, te pido los datos de factura.»
- **D:** «Cuando revises [ficha / receta / conservación], me dices y armamos el pedido. ¿Te queda bien si te escribo el [día] por si surgió alguna duda?»

### Datos del pedido (cuando hay un sí)

Según el flujo actual (`erp.md`): nombre completo, cédula, teléfono y correo para facturar; luego factura y fecha de entrega. Pídelos **después** del sí, no en el saludo. Confirma producto, cantidad, precio, zona y fecha.

> Perfecto. Para la factura necesito nombre completo, cédula, teléfono y correo. En cuanto la tenga, te la comparto con la fecha de entrega.

---

## 8. Objeciones, por perfil

Responde la objeción real. Si alguien dice «está caro» pero detrás hay miedo a que no coma, trata el miedo. En todos los casos: un hecho, una frase de contexto, una pregunta. Sin claims.

### 8.1 «Está caro» / «sale más que el concentrado» (tipo Friskies u otra croqueta)

Contexto honesto: no es el mismo tipo de comida (carne horneada frente a concentrado). No compares costo diario hasta tener guía de ración confirmada (BL-041) y precio confirmado (BL-005). No inventes «te rinde más» ni «al mes te sale lo mismo».

**A**  
> Entiendo. Es otra comida: carne horneada, no croqueta. Si quieres, empezamos con [producto] para [perro] y ves cómo lo recibe. El precio de esa presentación es [precio]. ¿Lo vemos así?

**B**  
> Tiene sentido que lo mires con cuidado: es una decisión por [mascota]. El precio de [producto] es [precio]. No hace falta que armes el mes completo: puedes empezar con un paquete y decidir después. ¿Te queda más cómodo así?

**C**  
> [Producto] cuesta [precio]. Es alimento horneado, no concentrado; por eso no se compara kilo a kilo sin la ración. Si quieres el cálculo del mes, lo hacemos con la guía de porciones de la empresa. ¿Te lo armo con el peso de [mascota]?

**D**  
> El precio de [producto] es [precio] por [presentación]. Para compararlo con un concentrado hace falta el costo por día, con ración de ambos. Todavía debo confirmarte la guía de Canívoros; no quiero darte un número inventado. ¿Te paso primero la ficha y, cuando tenga la ración, el cálculo?

Si el precio aún no está confirmado:  
> Te cotizo el valor exacto y te lo mando enseguida. No quiero darte una cifra que después no se cumpla.

### 8.2 Conservación y logística («¿cómo lo guardo?», «¿y si no tengo congelador?», «¿me llega bien?»)

No repitas en automático «lugar fresco y seco» del sitio: puede no aplicar igual a chorizos y hamburguesas. Usa la instrucción confirmada por producto. No prometas cobertura que no exista.

**A**  
> Te digo exactamente cómo guardar [producto] para que [mascota] lo reciba bien: [instrucción de conservación]. ¿Me confirmas tu zona para darte la fecha de entrega?

**B**  
> Es una buena pregunta, porque nadie quiere que se dañe. Para [producto] la indicación es: [instrucción de conservación]. Si al abrirlo te queda mucho, te explico cómo porcionarlo. ¿En qué barrio estás, para revisar la entrega?

**C**  
> Conservación de [producto]: [instrucción de conservación]. Entrega a [zona]: [fecha o «te confirmo»]. ¿Hay alguna restricción de horario o de refrigeración en casa?

**D**  
> Conservación y vida útil las tengo que darte por producto, no con una frase genérica. Para [producto]: [instrucción de conservación]. Vida útil: [dato confirmado o «te confirmo el dato de etiqueta»]. Si no tienes [congelador/espacio], lo vemos antes de armar el pedido. ¿Quieres también el dato de cómo viaja?

Si la conservación aún no está confirmada:  
> Prefiero no indicarte un almacenamiento que después no coincida con la etiqueta. Te lo confirmo con la empresa y te escribo hoy.

### 8.3 Transición de dieta («¿cómo se lo cambio?»)

No indiques un protocolo médico. No digas que el cambio «no tiene riesgo». Si hay condición clínica, veterinario primero. Un esquema gradual solo si la empresa tiene uno escrito; si no, dilo y deriva.

**A**  
> Se puede pasar poco a poco, para que [perro] se vaya acostumbrando al sabor y a la textura. Te comparto la pauta que usa la empresa: [pauta de transición confirmada]. Si [perro] tiene alguna condición de salud, lo revisamos con tu veterinario antes.

**B**  
> Es normal que te preocupe el cambio. Lo más prudente es hacerlo gradual y, si [mascota] está en tratamiento o tiene el estómago sensible por indicación médica, hablarlo primero con tu veterinario. Yo te acompaño en el pedido y en cómo servirlo. ¿Tiene alguna indicación especial hoy?

**C**  
> Transición: [pauta confirmada, o «te confirmo la pauta escrita de la empresa»]. Si hay un tema clínico, tu veterinario define el ritmo. ¿Empezamos con [producto] y te dejo la indicación junto con el pedido?

**D**  
> No hay una regla universal que yo deba improvisar. La pauta de la empresa es [pauta o «pendiente de confirmar»]. En un caso clínico, la transición la indica el veterinario. ¿Quieres que te mande lo documentado antes de comprar?

### 8.4 «Mi mascota no lo va a comer»

No prometas que le va a gustar. No ofrezcas devolución si no hay política. Reduce riesgo con un primer paquete de una presentación que **sí exista** (hoy, en el relato, 500 g; no ofrezcas 200 g ni un «kit de prueba» inventado).

**A**  
> Puede pasar: cada [perro] tiene su gusto. Por eso mejor empezamos con [producto] y me cuentas cómo le fue. Si no le llama la atención, vemos otra proteína o cómo servirlo. ¿Probamos con esa?

**B**  
> Entiendo el miedo: no quieres comprar por gusto y que [mascota] ni lo olfatee. Podemos empezar con un solo paquete de [producto], sin armarte un pedido grande. [política de cambio o devolución, solo si existe]. ¿Te parece un buen primer paso?

**C**  
> No te puedo garantizar el paladar. Lo práctico es un primer paquete de [producto] a [precio] y, según cómo lo acepte, armamos el mes. ¿Lo hacemos así?

**D**  
> La aceptación varía; en gatos, la responsable de la empresa ha relatado que no todos lo aceptan, sobre todo si el paquete lleva abierto un tiempo. Por eso importa la conservación y empezar con una cantidad que exista hoy: [producto]. No tengo un estudio de palatabilidad para mostrarte. ¿Quieres empezar con un paquete y registramos cómo le va?

### 8.5 «No los conozco» / «es una marca nueva para mí»

Apóyate en hechos: origen en Sopó, familia de criadores (declaración de la marca), horneado, canales de compra, registro ICA **con número**. No uses «somos los mejores». Testimonio solo con permiso.

**A**  
> Somos una empresa de Sopó. Hacemos comida horneada y nacimos del trabajo con perros de competencia. Si quieres, te cuento de [producto] y cómo lo pedimos por WhatsApp. [testimonio, solo si hay permiso].

**B**  
> Tiene sentido pedirnos trayectoria. Fabricamos en Sopó y atendemos directo por este chat. Puedes empezar con un paquete y yo te acompaño en la entrega y en cómo guardarlo. Si prefieres recogerlo en un punto, te confirmo los distribuidores que estén activos cerca de ti.

**C**  
> Planta en Sopó, venta por WhatsApp y puntos aliados (te confirmo el más cercano). [Producto] a [precio], entrega [fecha]. ¿Sigues con el pedido o quieres primero el punto de retiro?

**D**  
> Hechos que sí te puedo documentar: origen en Sopó, proceso horneado (no crudo), presentaciones [lista confirmada] y registro ICA [número ICA o «te comparto el número en cuanto lo tenga a la mano»]. Ficha técnica: [la adjunto / te confirmo cuándo te la envío]. ¿Qué te falta para evaluarnos con tranquilidad?

### 8.6 «Lo voy a consultar con el veterinario»

Eso no es un rechazo. Ayúdalo a consultar bien. No pidas que ignore al veterinario. No le des un argumento para «convencer» al profesional con claims.

**A**  
> Perfecto, que lo mire tu veterinario. Si quieres, le compartes qué es: alimento horneado de [proteína], hecho en Sopó. Cuando te dé el visto, me escribes y armamos el pedido de [mascota].

**B**  
> Me parece una buena idea, sobre todo si hay algún antecedente de salud. Yo te dejo la información clara para que se la lleves, y quedo atento. ¿Quieres que te escriba en unos días, solo para saber si te quedó alguna duda?

**C**  
> Sí. Te mando en un solo mensaje: producto, ingredientes declarados, presentación y precio. Tú lo revisas con tu veterinario y me dices si seguimos. ¿Te lo envío ahora?

**D**  
> Te armo un paquete de información para tu veterinario: ficha técnica [si existe], registro ICA [si hay número], conservación e ingredientes. No voy a adelantar un beneficio de salud que el profesional deba evaluar. ¿Te lo mando en PDF o por acá?

---

## 9. Técnicas éticas (cómo aplicarlas aquí)

Usar psicología de ventas no es manipular. Es quitar fricción y decir la verdad en el orden que el otro puede oír.

1. **Reducción de riesgo.** Ofrece el paso más pequeño que **exista**: un paquete de la presentación actual, no un pack de prueba inventado. Alternativa de pedido: si no quiere el mes, el primer paquete; si no quiere delivery, un punto aliado *activo* (BL-035). Política de cambio: solo si la empresa la tiene.
2. **Compromiso y coherencia.** Si la persona ya dijo «quiero darle comida más natural» o «no quiero crudo», conecta el cierre con esa frase, sin atraparla: «Como quieres algo listo para servir y no crudo, [producto] encaja. ¿Empezamos con un paquete?»
3. **Prueba social real.** Un testimonio publicado, con permiso, o un caso de criadero si la marca autoriza nombrarlo. Nunca «a todos les funciona». Nunca cifras de clientes o de recompra que el repo no tenga medidas.
4. **Autoridad honesta.** Omar y la trayectoria en perros de competencia son un activo relatado. El veterinario es la autoridad en salud. El ICA es autoridad regulatoria solo con el número. Tú no eres nutricionista del animal salvo que lo seas y lo declares.
5. **Reciprocidad útil.** Dale información práctica (cómo se pide, cómo se guarda, qué no es este alimento) aunque aún no compre. Eso no incluye raciones inventadas ni comparativos de precio falsos.
6. **Escasez verdadera.** «Esta semana la ruta a [zona] sale el [día]» está bien si es cierto. «Quedan dos» solo con inventario real.
7. **Contraste con Friskies / concentrado, sin ataque.** Diferencia de categoría: ellos son concentrado masivo, de muchos sabores y amplia distribución; Canívoros es horneado, de pocas recetas, venta cercana. El cliente práctico no es «tonto por comprar concentrado». En gatos, reconoce que el cambio de costumbre puede ser difícil y sugiere veterinario y, si la empresa lo confirma, un público de gatito nuevo.

---

## 10. Mensajes listos (plantillas)

Sustituye placeholders. No envíes un bloque de texto enorme por WhatsApp: parte en burbujas cortas.

### 10.1 Primer contacto desde Instagram (el cliente llega del perfil)

> Hola, [nombre]. Vi que nos escribiste desde Instagram. Soy [tu nombre], de Canívoros. ¿Es para perro o para gato, y cómo se llama?

### 10.2 Recomendación de producto

> Para [mascota], te sugiero [producto]. Es horneado en Sopó y llega listo para servir. El precio es [precio]. ¿Quieres que te arme ese pedido o prefieres que te cuente otra proteína?

### 10.3 Cotización (solo con precio confirmado)

> [Producto] — [presentación]  
> Precio: [precio]  
> Entrega a [zona]: [fecha de entrega]  
> Pago: [condición real; el flujo habitual es pago antes de despachar]  
> Si te parece bien, te pido los datos de factura y lo dejamos listo.

### 10.4 El cliente pide «algo barato para probar»

> Hoy la presentación con la que podemos empezar es [producto / presentación existente] a [precio]. No tengo un empaque de prueba más pequeño para ofrecerte sin inventarlo. Si te sirve empezar con esa, la armamos y ves cómo le va a [mascota].

### 10.5 El cliente es de una zona sin cobertura confirmada

> Te confirmo si llegamos a [zona] o si hay un punto aliado activo cerca. No quiero darte una fecha que después no cumplamos. Te escribo en cuanto lo valide.

### 10.6 Gatívoros

> Para gatos tenemos Gatívoros, en [receta confirmada: salmón y cerdo u la que valide la empresa], presentación [peso]. Si [gato] ya come concentrado desde hace tiempo, lo ideal es que el cambio lo mire tu veterinario. Si es un gatito que está empezando, te cuento cómo iniciar con el producto que sí tenemos hoy. ¿Cuál es el caso de [gato]?

### 10.7 Criador o volumen (solo tono; condiciones por confirmar)

> Si es para varios perros, hay una oferta directa por volumen en pollo y cerdo. Las condiciones (mínimo, presentación, precio) te las confirmo con la empresa antes de cotizarte, para no darte un número que no esté vigente. ¿Me dices cuántos perros y qué proteína te interesa?

---

## 11. Seguimiento

Silencio no es rechazo. Puede estar en el veterinario, esperando el sueldo, comparando o simplemente ocupado. Tampoco es un sí: no insistas a diario.

### Si acepta

1. Confirma por escrito: producto, cantidad, precio, zona, fecha, forma de pago.
2. Pide datos de factura y envía la factura cuando la tengas.
3. Avisa el día de despacho o de ruta.
4. Después de la entrega (un mensaje, no una encuesta):  
   > [nombre], ya quedó [producto] con [mascota]. Cualquier duda de cómo servirlo o guardarlo, aquí estoy.
5. Recordatorio de reposición **solo con permiso** (BL-058, BL-022). Mientras no haya ración confirmada, no calcules «te debe estar durando X días». Si más adelante hay un intervalo real de compra del cliente, úsalo (versión 1 de BL-022).

### Si duda

Deja un siguiente paso con fecha, no un vacío.

- **A:** «Cuando quieras le armamos el pedido a [perro]. Si te sirve, te escribo el [día] por si te quedó alguna gana de probarlo.»
- **B:** «Queda en tus manos, sin apuro. ¿Te viene bien si te escribo el [día] solo para resolver dudas, no para presionarte?»
- **C:** «Te dejo el resumen: [producto], [precio], [entrega]. Si te encaja, me dices y lo cerramos. Si no, también me dices y no te molesto.»
- **D:** «Te dejé [ficha / datos]. Revísalo con calma o con tu veterinario. Te escribo el [día] por si surgió una pregunta puntual.»

### Si deja en visto

Espera antes de reescribir. Propón tres toques y luego un cierre suave. No cambies el precio ni inventes una promoción para «despertarlo».

| Toque | Cuándo (orientativo) | Intención |
|---|---|---|
| 1 | Al día siguiente, en horario laboral | Recupera la pregunta abierta, no el cierre |
| 2 | A los 2–3 días | Un dato útil (conservación, presentación, punto de entrega) + pregunta sí/no |
| 3 | A los 6–8 días | Cierre suave: la puerta queda abierta, sin más seguimiento |

**Toque 1 (neutro)**  
> [nombre], te dejo por acá por si se te pasó el mensaje. ¿Sigues interesado en [producto] para [mascota], o quieres que te aclare algo?

**Toque 2, según perfil**

- **A:** «Estaba pensando en [perro]. Si quieres, te armo un primer paquete de [producto] cuando te quede bien.»
- **B:** «Solo para no dejarte con la duda. Si prefieres esperarte o consultarlo, no hay problema. ¿Te ayudo en algo más?»
- **C:** «Te reenvío lo concreto: [producto] a [precio], entrega a confirmar en [zona]. ¿Lo armamos o lo dejamos hasta otra?»
- **D:** «Si estás revisando la información, sin apuro. ¿Te falta algún dato (ficha, conservación, registro) para decidir?»

**Toque 3 (cierre suave, todos)**  
> [nombre], no te escribo más por este pedido para no llenarte el chat. Si más adelante quieres probar [producto] para [mascota], aquí estaré. ¡Que estén muy bien!

Si la persona pidió explícitamente que no le escribas, no hay toque 2 ni 3.

### Recontactar a quien ya compró y dejó de comprar (BL-060)

Solo con permiso y con precio real confirmado. No uses este playbook para mensajes masivos improvisados.

> Hola, [nombre]. Soy [tu nombre], de Canívoros. Te escribo porque [mascota] ya no pide desde [periodo aproximado, si está en tu registro]. Si quieres reponer [producto], el precio actual es [precio] y te armo la entrega a [zona]. Si no es el momento, no hay problema.

---

## 12. Mini guía de 30 segundos (para tener a la vista)

1. Responde pronto. Saluda. Una pregunta.
2. Detecta: ¿historia y cariño (A), miedo y cuidado (B), precio y rapidez (C), datos y evidencia (D)?
3. Recomienda un producto que exista. Hechos, no beneficios de salud.
4. Precio solo confirmado, y después del encaje.
5. Cierra con un paquete, una fecha o una pregunta de sí/no.
6. Si hay salud de por medio: veterinario.
7. Si se queda en visto: tres toques, luego se cierra con respeto.

---

## 13. Preguntas abiertas para la marca

Estas respuestas desbloquean mensajes que hoy van con placeholder. No hay que adivinarlas.

1. **Precios y catálogo (BL-005):** precio público y a distribuidor por producto y canal; unidad (500 g o libra); vigencia; qué productos se pueden ofrecer hoy (incluida ternera y la receta final de Gatívoros).
2. **Conservación y vida útil por SKU:** ¿ambiente, refrigerado o congelado? ¿Qué se le dice al cliente al abrir el paquete, en especial chorizos y Gatívoros?
3. **Guía de raciones (BL-041):** por peso, edad y actividad, perro y gato. Sin eso no hay costo diario ni recordatorio por duración del empaque.
4. **Pauta de transición** escrita, si existe, y qué hacer si la mascota no acepta el alimento.
5. **Política de cambio, devolución o reposición** si no le gusta o si llega en mal estado. Si no existe, no se promete.
6. **¿Existe o existirá una presentación de entrada** (por ejemplo ~200 g) o un pack de primera compra? Hoy no debe ofrecerse (BL-023).
7. **Número de registro ICA por producto** y ficha técnica (proteína, grasa, humedad, si es alimento completo). Hasta entonces, no se envían esos claims.
8. **Redacción aprobada** para cuando pregunten por subproductos o partes del animal (BL-016).
9. **Número de WhatsApp comercial principal** y quién firma (Omar u otra persona).
10. **Cobertura de entregas** (barrios, días de ruta, costo de domicilio) y cuáles de los seis distribuidores publicados siguen activos (BL-035).
11. **Permiso** para usar testimonios del sitio, fotos y perros de competencia en el chat (BL-058).
12. **Condiciones de volumen** para criadores (mínimo, precio, presentaciones) antes de cotizar (BL-043).

---

## 14. Cómo encaja con el resto del repo

| Recurso | Relación con este playbook |
|---|---|
| Rama `branding/`, sobre todo `02` y `03` | Manda la voz, los mensajes prohibidos y las objeciones genéricas. Aquí se añade la adaptación por estilo A–D y el seguimiento si deja en visto. |
| `embudos/E01` y `E02` | Diseñan adquisición, recompra y recuperación. Este documento es el guion de la conversación viva, no el diagrama del embudo. |
| `backlog/BL-016` | Hay que respetar su lista de afirmaciones hasta que haya evidencia. |
| `backlog/BL-019`, `BL-020` | Si se captan leads o se prueban mensajes (horneado vs facilidad de uso), el cierre sigue este tono por perfil. |
| `backlog/BL-059` | Una auditoría de chats de 2 semanas permitirá ajustar estas plantillas con motivos reales de pérdida. Hasta entonces, no se declaran tasas. |
| `backlog/BL-022`, `BL-058`, `BL-060` | Gobiernan recordatorios y recontacto. Este playbook no los automatiza. |

Cuando la empresa confirme precios, raciones, conservación e ICA, hay que sustituir placeholders y revisar la sección 3. Hasta esa fecha, un mensaje con cifra inventada hace más daño que un «te lo confirmo».
