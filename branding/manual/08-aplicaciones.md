# 08 · Aplicaciones

Manual Canívoros & Gatívoros v1.0 · 10 nov 2026. Especificaciones en texto para que un agente produzca cada pieza. Todos los datos de producto salen de `01-plataforma-estrategia-y-mensajes.md` §3; los claims, de `01` §2.

## 0. Evidencia mínima de toda pieza de venta (OBLIGATORIO)

Fuente: **Competitor Watch, PR #9**, que detectó estas brechas frente a VITA y Pixie. Toda pieza que venda un producto (empaque, catálogo de WhatsApp, post de producto, volante, material para tiendas) debe mostrar estos seis datos o un hueco visible `[falta: …]` en el borrador:

| Dato | Estado hoy | Cómo se muestra |
|---|---|---|
| **Precio** | `[falta: BL-005]` | En catálogo de WhatsApp y volantes. Nunca en empaque |
| **Peso** | 500 g (C05) | Siempre, frente del empaque |
| **Ración** | `[falta: BL-041]` | Tabla en el dorso; «según el peso de tu perro» en redes |
| **Registro ICA visible** | Números conocidos, producto amparado por confirmar (C13) | Dorso del empaque, catálogo, web |
| **Vida útil y conservación** | `[falta: BLOQUEANTE 2]` | Dorso del empaque, catálogo |
| **Un solo WhatsApp** | `[falta: elegir entre tres números]` (C33) | Toda pieza con contacto |

Si falta un dato, la pieza **se queda en borrador**. No se publica con el dato inventado ni se borra el hueco.

## 1. Empaque por producto

### 1.1 Sistema común (todas las referencias)

Medidas reales del empaque: `[falta]`. Proporciones para un empaque vertical (bolsa o caja):

**Frente, de arriba abajo:**
1. **Franja superior (25 % de la altura):** fondo hueso `#FBF6EC` (Canívoros) o plata `#EAEAE9` (Gatívoros). Logo principal centrado con su área de seguridad. En Gatívoros, debajo del logo, «de la casa Canívoros» en Nunito 600, tostado `#804607`, al 6 % de la altura.
2. **Franja central (35 %):** nombre de la proteína en Fredoka 700 MAYÚSCULAS, carbón `#2B2320` (o tostado en Gatívoros), alineado al centro. Debajo, banda tipo **cápsula** en el color del acento con el formato: «Chorizos horneados» o «Hamburguesas horneadas» `[A VALIDAR: C06]` en Nunito 700, con el color de texto que indica `04-color.md` §1.3.
3. **Franja inferior (40 %):** foto real del producto servido o, mientras no exista, ilustración plana del producto. En la base, una línea: «Para perros · Hecho en Sopó» (o «Para gatos»), y a la derecha «500 g» en Nunito 700 grande.
4. **Prohibido en el frente:** sellos de «100 % natural», beneficios de salud, «premium», precio.
5. Máximo 6 palabras más el peso (revisión Copy Humanizer).

**Dorso, bloques en este orden:**
1. **Voz de marca** (máx. 2 frases): «Somos una familia de criadores en Sopó. Esta es la comida que horneamos para nuestros propios perros.» `[A VALIDAR: C07, C08, bloqueantes]`. Alternativa segura si no se valida: «Hecho en Sopó por gente que vive el mundo de los perros.»
2. **Ingredientes** `[falta: etiqueta]`.
3. **Análisis garantizado** (proteína, grasa, humedad, fibra, cenizas…) `[falta]`.
4. **Ración por peso** en tabla `[falta: BL-041]`.
5. **Modo de uso y conservación** `[falta: BLOQUEANTE 2]`. Texto modelo: «Consérvalo [condición]. Una vez abierto, [instrucción]. Sirve según el peso de tu perro.»
6. **Datos legales** (bloque en Nunito 400, tamaño legal): Registro ICA n.º [número] · Titular y fabricante [según registro ICA] · Canivoros S.A.S. [confirmar relación con el titular] · Dirección [oficial a confirmar] · Lote [ ] · Vence [ ] · Peso neto 500 g · «Hecho en Colombia».
7. **Contacto:** un solo WhatsApp y canivoros.com. Ícono de WhatsApp en línea.
8. **Lema** como firma al pie: «Cuídalo cada día, ámalo toda la vida.»
9. Fondo con patrón «salchichas en arco» al 8 % (`06-elementos-graficos.md` §2), nunca detrás de la tabla de ración ni de los datos legales.

**Información obligatoria a confirmar con ICA (OBLIGATORIO):** la lista exacta, el tamaño mínimo de letra y el orden los fija la norma ICA de etiquetado de alimentos para animales. Ningún agente da por cerrada una etiqueta: la dueña la valida con el ICA. Los campos de arriba son la lista de trabajo, no la norma.

### 1.2 Fichas por referencia

| Referencia | Fondo frente | Acento (banda) | Texto en banda | Título | Línea de base | ICA en dorso |
|---|---|---|---|---|---|---|
| Canívoros Pollo y Salmón · Chorizos · 500 g (CAN-PS-500) | Hueso | Salmón `#E8745A` | Carbón | «POLLO Y SALMÓN» | «Para perros · Hecho en Sopó · 500 g» | `[¿22065AL? A VALIDAR]` |
| Canívoros Pollo · Hamburguesas · 500 g (CAN-PO-500) | Hueso | Azul pollo `#2F5DA8` | Blanco | «POLLO» | Ídem | `[falta]` |
| Canívoros Cerdo · Hamburguesas · 500 g (CAN-CE-500) | Hueso | Verde salvia `#5E7F3A` | Blanco (negrita) | «CERDO» | Ídem | `[¿24713AL? A VALIDAR]` |
| Canívoros Ternera · Hamburguesas · 500 g (CAN-TE-500) | Hueso | Vino `#8A2C3B` | Blanco | «TERNERA» | Ídem | `[falta]` |
| Gatívoros · [receta confirmada] · Chorizos · 500 g (CAN-SC-500) | Plata | Azul cielo `#9EC9E2` | Carbón | «[RECETA CONFIRMADA]» (Odoo dice salmón y cerdo; el sitio, salmón y pollo; bloqueado hasta BL-005) | «Para gatos · Hecho en Sopó · 500 g» | `[¿24065AL? A VALIDAR]` |

Gatívoros es la única referencia que puede usar el ángulo carnívoro en el dorso: «El gato es carnívoro. Por eso Gatívoros se hace con [receta confirmada].» (C27; receta bloqueada hasta BL-005).

### 1.3 Programa Criadores (volumen, 1,5 kg)

No es una línea con empaque de góndola. **Etiqueta de bodega**: una tinta tostado `#804607` sobre kraft o blanco, logo monocromo, proteína en Fredoka 700 grande, peso, lote, vencimiento y registro ICA. Sin foto ni bloque de voz. Condiciones del programa `[falta: BL-005, BL-043]`.

## 2. Etiqueta adhesiva (para empaques genéricos mientras no exista el nuevo)

- Rectangular redondeada o en forma de cápsula, `[falta: medida según el empaque actual]`.
- Fondo hueso, logo principal a la izquierda, a la derecha la proteína (Fredoka 700) y el formato (Nunito), franja inferior del color del acento con «500 g».
- Segunda etiqueta para el dorso con los datos legales (§1.1, bloque 6).

## 3. Redes sociales

### 3.1 Perfil de Instagram

- **Nombre visible:** «Canívoros · Comida para perros y gatos» `[Propuesta]`. Hoy es «Comida para perros - Canivoros Colombia» (revisión Market Researcher).
- **Foto de perfil:** isotipo (salchicha con corazón) sobre círculo hueso. Mientras no exista el isotipo, el logo completo centrado con margen amplio.
- **Bio (máx. 150 caracteres) [Propuesta]:** «Hecho por criadores en Sopó 🐾 Chorizos y hamburguesas horneados para perros, y Gatívoros para gatos. Pide por WhatsApp 👇» `[A VALIDAR: C06, C07]`. La bio actual dice «Alimento 100% natural para tu campeón»: «100 % natural» está prohibido (C20) y hay que cambiarla.
- **Enlace:** al único WhatsApp (C33).

### 3.2 Feed

- Formato 1080 × 1350 (4:5). Grilla y márgenes en `06-elementos-graficos.md` §6.
- Patrón de 9 posts, repetido:

| | Columna 1 | Columna 2 | Columna 3 |
|---|---|---|---|
| Fila 1 | Producto (cenital, acento del sabor) | Perro real con su tutor (con permiso) | Educación: cómo se sirve / cómo se guarda (fondo hueso, texto) |
| Fila 2 | Detrás de cámaras en Sopó | Experiencia de un cliente, sin claims de salud (C16) | Gatívoros (plata y azul cielo) |
| Fila 3 | Campeones alimentados con Canívoros (solo títulos citables, C30) | Pedido del mes o recordatorio | Comunidad: jornadas, tiendas aliadas |

- Titular sobre imagen: máx. 8 palabras, Fredoka 700, en una caja hueso o directamente sobre zona limpia de la foto.
- Pie de foto: máx. 4 líneas antes de «ver más», máx. 3 emojis, CTA al WhatsApp.
- **Plantilla «producto»:** foto cenital a sangre; abajo, cápsula del color del acento con el nombre oficial; logo abajo a la derecha; peso visible.
- **Plantilla «educación»:** fondo hueso, antetítulo en Nunito 700 tostado, titular Fredoka 700 carbón, 3 pasos con íconos de línea, logo abajo.
- **Plantilla «campeón»:** foto del perro en pose de pista a sangre, banda inferior azul noche `#202A54` con nombre del perro en Fredoka oro claro y su título verificado en Nunito blanco; firma «Campeones alimentados con Canívoros».
- **Plantilla «experiencia de cliente»:** foto del animal, cita en Nunito Italic sobre caja hueso, nombre de pila y ciudad solo con permiso.

### 3.3 Stories

- 1080 × 1920. Zona segura: 250 px arriba y 340 px abajo sin texto.
- 1 frase por pantalla (máx. 8 palabras). Stickers de pregunta o encuesta para conversación.
- Cierre con sticker de enlace al WhatsApp.

### 3.4 Reels

Ver `07-fotografia-y-video.md` §7. Portada del reel: 1080 × 1920 con el titular dentro del recorte central 1080 × 1350 para que se lea en el feed.

### 3.5 Destacadas (highlights)

Hoy: «Salmon», «Pollo 100 %», «Gativoros» y «Destacada» (revisión Market Researcher). «Pollo 100 %» debe confirmarse y «Gativoros» lleva tilde.

**Propuesta de destacadas, en este orden:** Empieza aquí · Productos · Cómo servir · Gatívoros · Criadores · Clientes · Dónde comprar.
**Portadas:** círculo hueso `#FBF6EC` con un ícono de línea tostado `#804607` centrado (huella, bolsa, plato, gato, criador con perro, corazón, ubicación). Sin texto en la portada.

## 4. WhatsApp Business

- **Foto de perfil:** isotipo sobre hueso (o logo completo con margen amplio).
- **Nombre:** «Canívoros».
- **Descripción [Propuesta]:** «Comida horneada para perros y gatos, hecha por criadores en Sopó. Te atiende Omar.» `[A VALIDAR: C06, C07]`.
- **Horario y dirección:** `[falta: confirmar]` (C33).
- **Catálogo:** un ítem por referencia de `01` §3. Cada ítem con foto cenital del producto sobre hueso, nombre oficial, precio `[falta: BL-005]`, descripción de máx. 2 líneas (proteína, formato, peso, para quién), ración y conservación `[falta]`, registro ICA `[A VALIDAR]`. El Programa Criadores no va en el catálogo público.
- **Mensajes:** bienvenida, ausencia y respuestas rápidas con los textos de `02-identidad-verbal.md` §9. Una pregunta por mensaje; máx. 1 emoji; nada de corazones con clientes nuevos.
- **Etiquetas** (organización interna): Nuevo · Pidió precio · Compró · Reposición pendiente · Criador · Tienda · Veterinaria.
- **Mensajes de reposición:** solo a quien lo autorizó (BL-058).

## 5. Web (canivoros.com)

- Paleta: hueso de fondo, oro y tostado para marca, azul noche para el pie y secciones oscuras. **Reemplazar** el azul, amarillo y coral del tema Colibri (revisión Market Researcher).
- Fuentes: solo Fredoka y Nunito; quitar las otras siete.
- Estructura sugerida: Inicio (cuña, productos, botón WhatsApp) · Productos (una ficha por referencia con los seis datos de §0) · Nosotros (criadores, Sopó, personas) · Campeones (solo verificados) · Dónde comprar (solo distribuidores confirmados) · Preguntas frecuentes (sin claims prohibidos) · Contacto (un solo WhatsApp).
- **Corregir antes que nada:** los claims prohibidos de `01` §2.4, «sin subproductos», las erratas «Carnívoros» y «Cativoros», y los tres números de WhatsApp.
- Botón flotante de WhatsApp en oro `#C18C36` con ícono carbón (no el verde de WhatsApp como color dominante).

## 6. Punto de venta y tiendas aliadas

- **Display de mostrador:** caja en forma de arco de salchicha o cartón con base curva; frente hueso, logo principal arriba, cuña «Hecho por criadores.» en Fredoka 700 tostado, las referencias disponibles con su banda de color. QR al WhatsApp con código por tienda (plan de Bogotá, experimento 3).
- **Cenefa o tira de estante:** franja oro `#C18C36` con logo en negativo y la cuña; alto `[falta: medida del estante]`.
- **Afiche:** A3 vertical, foto real de perro a sangre, titular de máx. 8 palabras, logo, QR, «De venta aquí».
- **Ficha para la tienda (A5):** las referencias, ración y conservación `[falta]`, registro ICA, un solo WhatsApp de pedidos. Sin márgenes ni precios hasta BL-005.
- **Material para veterinarias:** ficha técnica sobria, fondo blanco, solo datos de etiqueta. **Ningún beneficio de salud ni «comida de verdad».**

## 7. Volantes

- A5 vertical, 10 mm de margen y 3 mm de sangrado.
- Frente: foto real (perro o producto), titular de máx. 8 palabras, cuña, logo.
- Dorso: las referencias con su banda de color, los seis datos de §0 (o huecos visibles en el borrador), QR al WhatsApp, lema al pie.
- Papel mate; evitar brillo (el oro se ve mejor en mate). Tinta dorada metálica: opcional, **a confirmar con imprenta**.

## 8. Uniforme y vehículo de reparto

- **Camiseta o polo:** color azul noche `#202A54` o carbón `#2B2320`; logo principal en el pecho izquierdo (8–9 cm de ancho), bordado o estampado en oro; en la espalda, la cuña «Hecho por criadores.» en Fredoka, oro claro. Gorra con el isotipo.
- **Delantal de planta:** crema o blanco, logo monocromo tostado.
- **Vehículo:** fondo del color del vehículo (preferible blanco o crema); en los costados, salchicha del logo grande, «Canívoros» y la cuña; en la parte trasera, el único WhatsApp y canivoros.com. El patrón de huellas al 8 % puede cubrir la parte baja. Nada de claims de salud ni «100 % natural». Medidas `[falta: vehículo]`.

## 9. Stickers

- Troquelados con la forma del isotipo (salchicha con corazón) y de la salchicha con el gato (Gatívoros).
- Set de stickers de conversación (para WhatsApp e Instagram): «¡Listo!», «¿Cuánto pesa?», «Pedido en camino», «Hecho en Sopó», con ilustración plana y contornos tostado.
- Sticker de cierre de bolsa: círculo de 4 cm, hueso, logo monocromo tostado y el lema en arco. Sin sellos tipo «100 % natural».

## 10. Tarjetas de presentación

- 90 × 50 mm, 5 mm de margen, 2 mm de sangrado.
- **Frente:** fondo hueso, logo principal centrado con su área de seguridad.
- **Dorso:** fondo azul noche, nombre (Fredoka 700, oro claro), cargo (Nunito, blanco), único WhatsApp, correo, canivoros.com, y la cuña. QR opcional al WhatsApp.
- Papel mate de 300–350 g; oro en tinta plana o *hot stamping* `[a confirmar con imprenta]`.
