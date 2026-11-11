# 10 · Plantilla de brief para agente de IA

Manual Canívoros & Gatívoros v1.0 · 10 nov 2026. Copia el bloque, llena los corchetes y bórralos si no aplican. Un brief sin «Producto» o sin «Entregable» no se envía.

## 1. Plantilla

```
# BRIEF · Canívoros & Gatívoros

## 0. Manual
Sigue el manual de marca Canívoros & Gatívoros v1.0
(repo quemasandy/canivoros, rama branding, carpeta branding/manual/).
Obligatorio: 00 §4 (10 reglas) y el registro de claims de 01 §2.
Secciones que aplican a esta pieza: [p. ej. 03-logo §4, 04-color §1.3, 05-tipografia §3, 08-aplicaciones §3.2].
Si el agente no puede leer el repo, pego aquí el texto de esas secciones: [pegar].

## 1. Tarea
Tipo de agente: [generador de imagen | diseñador IA | copywriter IA | video]
Pieza: [post de feed | story | reel | empaque frente | empaque dorso | etiqueta | volante | afiche | catálogo WhatsApp | mensaje WhatsApp | web | tarjeta | sticker]
Entregable: [formato, medidas en px o mm, cantidad de variantes]
Nombre de archivo: [según 09 §5, p. ej. 20261115_canivoros_post_pollo-salmon_ig_v01.png]
Fecha límite: [fecha]

## 2. Marca y producto
Marca: [Canívoros | Gatívoros, de la casa Canívoros]
Producto (nombre exacto de 01 §3): [p. ej. Canívoros Pollo y Salmón · Chorizos · 500 g (CAN-PS-500)]
Acento de color: [HEX de 04 §1.3]
Datos de la ficha que SÍ se pueden usar: [proteína, formato, peso, para perros/gatos, hecho en Sopó]
Datos que faltan (dejar como [falta: …]): [precio, ración, conservación, vida útil, ICA, WhatsApp]

## 3. Público y objetivo
Público (01 §5): [criadores | tutores | tiendas | veterinarias | hogares con gatito]
Canal: [Instagram | WhatsApp | empaque | web | tienda | impreso]
Trato: [tú | usted] (02 §2)
Objetivo de la pieza: [que escriban por WhatsApp | explicar cómo se guarda | presentar un producto | …]
CTA: [p. ej. «Escríbenos por WhatsApp»]

## 4. Mensaje
Mensaje principal (de 01 §9 o §11): [texto]
Claims a usar (IDs de 01 §2, solo PERMITIDOS): [p. ej. C01, C03, C05]
Claims pendientes que se pueden mostrar marcados [A VALIDAR] solo en el borrador: [IDs o «ninguno»]
Lema o tagline: [lema | tagline | ninguno] (nunca los dos en la misma línea, 01 §10)
Texto exacto si ya existe: [texto]

## 5. Visual
Paleta: [p. ej. 60 % hueso #FBF6EC, 30 % oro #C18C36, 10 % carbón #2B2320 + acento]
Tipografía: Fredoka 700 para títulos, Nunito 400/700 para texto
Logo: NO generarlo. Dejar zona libre de [tamaño] en [posición], fondo liso [HEX]
Foto o ilustración: [real existente: ruta | boceto con prompt de 07 §8.X]
Prompt negativo: el de 07 §8.7
Referencias del manual: [secciones]

## 6. Restricciones de esta pieza
[p. ej. sin precio; sin perros de competencia; solo para borrador interno]

## 7. Qué debe devolver el agente
1. La pieza (o el texto) en el formato pedido.
2. La lista de reglas del manual que aplicó (archivo y sección).
3. La lista de datos que dejó como [falta: …] o [A VALIDAR].
4. Cualquier duda, en vez de inventar.
5. Confirmación de que no publicó, envió ni contactó a nadie.
```

## 2. Ejemplo lleno: post de producto para Instagram

```
# BRIEF · Canívoros & Gatívoros

## 0. Manual
Sigue el manual Canívoros & Gatívoros v1.0 (rama branding, branding/manual/).
Obligatorio: 00 §4 y 01 §2. Aplican: 03 §4, 04 §1.3, 05 §3, 06 §6, 07 §8.1, 08 §3.2 (plantilla «producto»).

## 1. Tarea
Tipo de agente: diseñador IA + generador de imagen para el boceto
Pieza: post de feed
Entregable: 1080 × 1350 px, PNG, 2 variantes
Nombre de archivo: 20261115_canivoros_post_pollo-salmon_ig_v01.png
Fecha límite: [fecha]

## 2. Marca y producto
Marca: Canívoros
Producto: Canívoros Pollo y Salmón · Chorizos · 500 g (CAN-PS-500)
Acento: salmón #E8745A (texto carbón encima)
Se puede usar: pollo y salmón, chorizos, 500 g, para perros, hecho en Sopó
Falta: precio, ración, conservación, ICA, WhatsApp único → [falta: …] en el borrador

## 3. Público y objetivo
Público: tutores. Canal: Instagram. Trato: tú.
Objetivo: que escriban por WhatsApp para pedir. CTA: «Escríbenos por WhatsApp».

## 4. Mensaje
Titular sobre imagen (máx. 8 palabras): «Pollo y salmón. Hecho en Sopó.»
Claims: C01, C03, C04, C05. Pendientes: ninguno en la imagen.
Pie de foto: «Chorizos de pollo y salmón para tu perro, hechos en Sopó. ¿Quieres probarlos? Escríbenos por WhatsApp 🐾» + [falta: WhatsApp]
Lema/tagline: ninguno en esta pieza.

## 5. Visual
Paleta: 60 % hueso, 30 % oro, 10 % carbón; banda inferior salmón.
Foto: boceto con el prompt de 07 §8.1 (marcar boceto-ia). Final: foto real del producto.
Logo: no generar; zona libre de 120 px de ancho abajo a la derecha, fondo hueso.
Prompt negativo: 07 §8.7.

## 6. Restricciones
Sin precio, sin «natural», sin beneficios, sin perros de competencia.

## 7. Qué devolver
Pieza + reglas aplicadas + huecos [falta] + dudas + confirmación de no publicación.
```

## 3. Errores frecuentes al escribir un brief

- Pedir «un post bonito de Canívoros» sin producto ni objetivo.
- Pedir que la IA «ponga el logo».
- Dar un claim del sitio viejo («100 % natural», «mejora la digestión») como texto.
- Pedir texto dentro de la imagen generada.
- Olvidar el trato (tú o usted) y el canal.
- No decir qué datos faltan, y que el agente los invente.
