# 09 · Gobierno de marca

Manual Canívoros & Gatívoros v1.0 · 10 nov 2026. Cómo se revisa, aprueba, nombra y versiona todo lo que sale con la marca.

## 1. Quién aprueba

| Tipo de pieza | Prepara | Revisa | Aprueba | Publica |
|---|---|---|---|---|
| Texto o imagen para redes | Agente IA o persona | Andrés (checklist §2) | Andrés | Quien maneje la cuenta, con visto bueno de Andrés |
| Mensajes de WhatsApp (plantillas) | Agente IA | Andrés | Andrés + Omar (es su voz) | Omar |
| Empaque y etiqueta | Diseñador | Andrés | **La dueña**, tras validarla con el ICA (Res. ICA 61252/2020, arts. 27 a 33) | Imprenta |
| Cambios en el sitio web | Agente IA o Sebastián | Andrés | La dueña | Sebastián |
| Material para tiendas y veterinarias | Agente IA o diseñador | Andrés | La dueña | Omar |
| Anuncios pagados | Agente IA | Andrés (solo claims PERMITIDOS) | Andrés + la dueña (presupuesto) | Andrés |
| Cambios en este manual | Agente IA | Andrés | Andrés (estrategia) y la dueña (hechos, claims, logo) | Commit en la rama `branding` |

**Ningún agente de IA publica, envía, imprime ni contacta a nadie.** Entrega borradores.

## 2. Checklist antes de publicar (OBLIGATORIO)

Una pieza que falla un punto vuelve a borrador.

**Verdad y claims**
- [ ] Cada afirmación está en el registro de claims (`01` §2) como PERMITIDA. Nada PENDIENTE ni PROHIBIDO.
- [ ] Ningún beneficio de salud, ni dicho ni insinuado (tampoco en fotos de «antes y después»).
- [ ] Ninguna cifra, precio, plazo, descuento o promesa de entrega que no esté confirmada.
- [ ] Registro ICA solo con número, y solo para el producto que ampara.
- [ ] Productos solo del catálogo (`01` §3). Gatívoros sin receta mientras no se confirme.
- [ ] Testimonios, fotos de clientes y perros de terceros con permiso escrito (BL-058).
- [ ] Sin nombres de competidores.

**Evidencia mínima (piezas de venta, `08` §0)**
- [ ] Precio, peso, ración, ICA, vida útil y un solo WhatsApp, o los huecos visibles en el borrador.

**Verbal**
- [ ] Trato correcto para el canal (tú o usted, `02` §2).
- [ ] Longitud y emojis dentro del límite (`02` §3).
- [ ] Sin palabras prohibidas (`02` §5). «Canívoros» y «Gatívoros» con tilde.
- [ ] Lema y tagline no van en la misma línea (`01` §10).
- [ ] Pasa la prueba de 4 preguntas (`02` §10). Una persona lo releyó.

**Visual**
- [ ] Logo original, no generado; con área de seguridad y sobre fondo permitido (`03`).
- [ ] Colores de la paleta, proporción 60/30/10, contraste AA (`04`).
- [ ] Solo Fredoka y Nunito (`05`).
- [ ] Fotos reales, o bocetos marcados como «imagen generada» (`07`).
- [ ] Nada de lo que `07` §6 prohíbe.

**Archivo**
- [ ] Nombre de archivo según §5 y versión correcta.

## 3. Versionado del manual

- Versión **MAYOR.MENOR** (por ejemplo, 1.0, 1.1, 2.0).
- **MENOR:** se corrige un dato, se agrega una pieza o se valida un claim.
- **MAYOR:** cambia la cuña, la arquitectura, el logo o la paleta.
- Todo cambio se registra en la tabla de cambios de `01` §0, con fecha y quién lo pidió.
- Cuando la dueña valide un claim, se cambia su estado en `01` §2 y se anota la fecha y el documento que lo respalda.

## 4. Versionado de piezas

- `v01`, `v02`… para borradores. `FINAL` solo cuando está aprobada según §1.
- Nunca se sobrescribe una versión aprobada: se crea la siguiente.

## 5. Nombres de archivo

Formato: `AAAAMMDD_marca_tipo_producto_canal_version.ext`, en minúscula, sin tildes ni espacios (guion bajo entre bloques, guion medio dentro de un bloque).

| Bloque | Valores |
|---|---|
| `marca` | `canivoros`, `gativoros` |
| `tipo` | `post`, `story`, `reel`, `empaque-frente`, `empaque-dorso`, `etiqueta`, `volante`, `afiche`, `tarjeta`, `catalogo`, `foto`, `boceto-ia`, `logo` |
| `producto` | `pollo-salmon`, `pollo`, `cerdo`, `ternera`, `gativoros`, `criadores`, `general` |
| `canal` | `ig`, `wa`, `web`, `impreso`, `tienda` |
| `version` | `v01`, `v02`, `final` |

Ejemplos: `20261115_canivoros_post_pollo-salmon_ig_v01.png` · `20261120_gativoros_empaque-frente_gativoros_impreso_v02.pdf` · `20261112_canivoros_boceto-ia_cerdo_ig_v01.png`.

Las imágenes generadas por IA llevan siempre `boceto-ia` en el nombre.

## 6. Dónde se guarda

- Este manual y los activos de marca: repositorio `quemasandy/canivoros`, rama `branding`, carpeta `branding/`.
- Logos originales: `branding/assets/referencia/` (hoy solo PNG del sitio).
- Piezas aprobadas: `[falta: definir carpeta compartida con la empresa]`.
- Nada de datos personales de clientes en el repositorio.

## 7. Entregables pendientes

| # | Entregable | Responsable | Bloquea |
|---|---|---|---|
| 1 | **Vector original del logo** (AI, SVG o PDF), Canívoros y Gatívoros | Dueña / su diseñador | Versiones, impresión, isotipo |
| 2 | Versiones horizontal, vertical, isotipo, monocromo y negativo | Diseñador humano | Avatar, sellos, uniformes |
| 3 | Etiqueta actual de cada producto (foto) y análisis garantizado | Dueña | Empaque nuevo, claims de composición |
| 4 | Qué producto ampara cada registro ICA y vigencia; relación titular–empresa | Dueña | Dorso del empaque, C13 |
| 5 | Conservación y vida útil por producto | Dueña | Mensajes de facilidad, H-POS-1, dorso |
| 6 | Guía de raciones (BL-041) | Dueña | Tablas, objeción de precio |
| 7 | Precios por canal (BL-005) | Dueña | Catálogo de WhatsApp, volantes |
| 8 | Un solo WhatsApp y dirección oficial | Dueña + Omar | Todas las piezas con contacto |
| 9 | Medidas reales de empaques, estantes y vehículo | Dueña / Omar | Plantillas de impresión |
| 10 | Fotos reales: producto, planta, Omar con perros, perros de clientes con permiso | Omar | Feed, web, empaque |
| 11 | Pruebas de títulos y permisos de los perros de competencia | Omar | Serie de campeones |
| 12 | Pantone de cada color y prueba de color | Imprenta | Impresos |
| 13 | Aprobación formal de este manual | Andrés + dueña | Todo lo marcado PROPUESTA |
