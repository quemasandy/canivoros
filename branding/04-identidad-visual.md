# 04 · Identidad visual

Versión 1 · 10 nov 2026 · Basada en el logo real publicado en canivoros.com. La paleta de soporte, los acentos por producto y la tipografía son **[Propuesta]**.

## 1. El logo actual (lo que existe)

Fuente: `https://canivoros.com/wp-content/uploads/2025/10/cropped-Canivoros-gativoros.png` y `cropped-icono-270x270.png`, descargados el 10/11/2026. Copia de referencia en `assets/referencia/`.

| Elemento | Canívoros | Gatívoros |
|---|---|---|
| Forma | **Salchicha/chorizo** curvo, con amarres en las puntas y un **corazón** encima | La misma salchicha, con una **cabeza de gato** sonriente encima |
| Color | Salchicha en degradado **oro/cobre**, letras blancas | Salchicha **plata/blanca** con borde oro, letras y gato en **oro** |
| Letras | Mayúsculas redondeadas, gruesas, en arco: «CANÍVOROS» | Minúsculas redondeadas en arco: «Gatívoros» |

**Variante encontrada:** en la imagen `productos.png` del sitio el logo aparece en **magenta** (#B42357 aprox.) con un sello dorado «100 % Natural · Alimento fresco y horneado». **[Hecho]** Recomendamos no usar el magenta en piezas nuevas para no tener dos colores de marca, y retirar el sello «100 % Natural» hasta validarlo.

**Activo más valioso:** la salchicha. Es única en la categoría y conecta con el producto estrella (chorizos). Se protege y se repite.

## 2. Paleta

Colores del logo extraídos con Pillow (cuantización de los píxeles del PNG oficial): #804607, #8D550D, #996112, #AA7324, #C18C36, #D6A246, #E2B560 y la plata #EAEAE9. Colores del sitio leídos del CSS: #303E7A, #202A54, #F7E597, #9EC9E2, #F66161.

### Núcleo (del logo real)

| Nombre | HEX | Origen | Uso | Contraste |
|---|---|---|---|---|
| **Oro Canívoros** | `#C18C36` | Logo (tono medio) | Color de marca. Salchicha, botones, títulos grandes | Texto carbón encima: 5,2:1 ✅. Blanco solo en títulos grandes (3,0:1) |
| **Oro claro** | `#E2B560` | Logo (brillo) | Degradados, detalles, fondos de acento | Texto carbón: 8,1:1 ✅ |
| **Tostado** | `#804607` | Logo (sombra) | Texto de marca sobre crema, bordes, íconos | Sobre hueso: 7,0:1 ✅ |
| **Plata Gatívoros** | `#EAEAE9` | Logo Gatívoros | Base de todo lo de gatos | Texto carbón: 12,8:1 ✅ |

### Soporte [Propuesta]

| Nombre | HEX | Uso |
|---|---|---|
| **Hueso** | `#FBF6EC` | Fondo principal (en vez de blanco puro) |
| **Carbón** | `#2B2320` | Texto principal. 14,3:1 sobre hueso |
| **Azul noche** | `#202A54` | Ya está en el sitio. Fondos oscuros, web, piezas B2B. El oro resalta encima |

### Acentos por producto [Propuesta]

Sirven para distinguir sabores en empaque y posts. Pollo y cerdo siguen el código de canastillas que ya usa la planta (pollo azul, cerdo verde; `erp.md` §4), para que el equipo los reconozca sin aprender nada nuevo.

| Producto | Acento | HEX | Texto encima |
|---|---|---|---|
| Chorizos Pollo y Salmón | Salmón | `#E8745A` | Carbón (5,2:1) |
| Hamburguesas de Pollo | Azul pollo | `#2F5DA8` | Blanco (6,5:1) |
| Hamburguesas de Cerdo | Verde salvia | `#5E7F3A` | Blanco (4,6:1) |
| Hamburguesas de Ternera | Vino | `#8A2C3B` | Blanco (8,4:1) |
| Gatívoros Salmón y Cerdo | Azul cielo (del sitio) | `#9EC9E2` | Carbón (8,7:1) |
| Volumen criadores / Núcleos / Orejas | Tostado | `#804607` | Blanco (7,5:1) |

Proporción sugerida en una pieza: **60 % hueso, 25 % oro, 10 % carbón o azul noche, 5 % acento del producto.**

Archivos: `assets/paleta.svg` y `assets/paleta.png`.

## 3. Tipografía (Google Fonts, gratuitas)

| Uso | Fuente | Por qué |
|---|---|---|
| Títulos y nombres de producto | **Fredoka** (SemiBold 600 / Bold 700) | Redondeada y gruesa como las letras del logo. Se lee bien en empaque |
| Texto, WhatsApp, web, fichas | **Nunito** (Regular 400 / Bold 700) | Redondeada, cálida y muy legible en pantalla y en letra pequeña |
| Alternativa a Fredoka | Baloo 2 | Si se necesita más peso o compatibilidad |

El sitio hoy carga **Aclonica, Holtwood One SC, Open Sans, Muli, Playfair Display, Butcherman, Gravitas One, Goblin One y Abril Fatface** **[Hecho: CSS del sitio]**. Son demasiadas y no se parecen al logo. Recomendación: dejar solo Fredoka + Nunito.

Jerarquía:
- H1: Fredoka 700, 48–64 px (post) / 28–36 pt (empaque).
- H2: Fredoka 600, 28–36 px.
- Texto: Nunito 400, 16–18 px. Mínimo 7 pt en etiqueta.
- Datos (peso, lote): Nunito 700.

## 4. Reglas del logo

- **Usar siempre el archivo original.** No redibujar ni cambiar las letras. Pedir a la empresa el **vector original** (AI, SVG o PDF): solo tenemos PNG del sitio.
- **Espacio libre:** alrededor del logo, al menos la altura del corazón (o de la cabeza del gato).
- **Tamaño mínimo:** 30 mm de ancho impreso / 160 px en pantalla. En el ícono de 32 px las letras no se leen; para favicon y foto de perfil usar solo la salchicha con el corazón **[Propuesta: pedir esa versión al diseñador]**.
- **Fondos permitidos:** hueso, blanco, azul noche, fotos con zona limpia. **No** sobre fondos oro (se pierde) ni sobre fotos con mucho detalle.
- **Versiones:** 1) oro sobre claro (principal); 2) oro sobre azul noche; 3) una tinta tostado para sellos y facturas; 4) blanco sobre foto oscura.
- **No hacer:** estirar, rotar, cambiar colores (incluido el magenta), poner sombras, separar la salchicha de las letras, juntar los logos de Canívoros y Gatívoros más cerca que su espacio libre.

## 5. Fotografía

Lo que ya funciona en el sitio **[Hecho]**: perros reales, en exteriores verdes, con luz natural; perros de exposición posando; perros de casa mirando a cámara.

Reglas [Propuesta]:
1. **Perros y gatos reales**, no de banco de imágenes. Clientes solo con permiso escrito (BL-058).
2. **Luz natural cálida**, verdes de la Sabana. Evitar flash y fondos de estudio grises.
3. **Producto como comida:** chorizo o hamburguesa en plato o en mano, se ve la carne. Primer plano, fondo de madera o hueso.
4. **Proceso en Sopó:** manos, horno, planta. Solo lo que la empresa apruebe mostrar.
5. **Personas con nombre:** Omar con los perros. Él es la cara de la marca.
6. Nada de perros comiendo de forma desagradable ni carne cruda sangrante: el mensaje es «horneado, listo para servir».

## 6. Iconografía

- Estilo: línea redondeada de 2 px, puntas redondas, en tostado o carbón. Igual de gordita que las letras del logo.
- Set mínimo: huella, corazón (del logo), horno, hoja/Sopó, calendario (reposición), WhatsApp, camión (entrega), copo (si el producto va congelado), balanza (porción por peso).
- Los íconos de proteína (pollo, pez, cerdo, res) van en el **acento del producto**.
- No usar íconos que impliquen beneficios de salud (corazón con cruz, escudo, diente brillante) hasta validarlos.

## 7. Grilla de Instagram

Formato 1080 × 1350 (4:5). Margen de 64 px. El logo va en una esquina inferior a 120 px de ancho.

Patrón de 3 columnas que se repite cada 9 posts [Propuesta]:

| Columna 1 | Columna 2 | Columna 3 |
|---|---|---|
| **Producto** (foto de comida, acento del sabor) | **Perro o gato real** (cliente o perro de la familia) | **Educación** (cómo servir, cómo guardar, qué es horneado) — fondo hueso con texto |
| **Detrás de cámaras en Sopó** | **Testimonio** con permiso (cita + foto) | **Gatívoros** (plata y azul cielo) |
| **Criadores / campeones** (con datos que dé la empresa) | **Oferta o recordatorio** (pedido del mes) | **Comunidad** (jornadas, eventos, tiendas aliadas) |

Reglas: máximo 12 palabras sobre la imagen; títulos en Fredoka; nunca dos posts seguidos del mismo tipo; cada post de beneficio pasa la prueba de `02-personalidad-y-voz.md` §6.

Ver un ejemplo en `assets/lamina-branding.png`.
