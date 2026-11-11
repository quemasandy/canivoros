# 04 · Color

Manual Canívoros & Gatívoros v1.0 · 10 nov 2026. El **núcleo** sale del logo oficial (cuantización con Pillow del PNG del sitio). **Soporte y acentos son PROPUESTA.** RGB calculado desde el HEX. **CMYK es una conversión aproximada** sin perfil de color: para impresión, pedir prueba a la imprenta. **Pantone: a confirmar con imprenta** para todos los colores.

## 1. Paleta

### 1.1 Primaria (del logo)

| Nombre | HEX | RGB | CMYK aprox. | Pantone | Uso |
|---|---|---|---|---|---|
| **Oro Canívoros** | `#C18C36` | 193, 140, 54 | 0, 27, 72, 24 | a confirmar con imprenta | Color de marca. Bandas, botones, títulos grandes, íconos destacados |
| **Oro claro** | `#E2B560` | 226, 181, 96 | 0, 20, 58, 11 | a confirmar | Brillos, degradados, fondos de acento, subrayados |
| **Tostado** | `#804607` | 128, 70, 7 | 0, 45, 95, 50 | a confirmar | Texto de marca sobre claro, versión monocromo, bordes, íconos |
| **Plata Gatívoros** | `#EAEAE9` | 234, 234, 233 | 0, 0, 0, 8 | a confirmar (evaluar tinta plata metálica) | Base de todo lo de Gatívoros |

Degradado oficial del logo (para elementos que imitan la salchicha, no para redibujar el logo): `#804607` → `#AA7324` → `#C18C36` → `#E2B560`, lineal, de izquierda a derecha o de abajo arriba.

### 1.2 Secundaria y neutros (propuesta)

| Nombre | HEX | RGB | CMYK aprox. | Pantone | Uso |
|---|---|---|---|---|---|
| **Azul noche** | `#202A54` | 32, 42, 84 | 62, 50, 0, 67 | a confirmar | Ya está en el sitio. Fondos oscuros, web, material B2B |
| **Hueso** | `#FBF6EC` | 251, 246, 236 | 0, 2, 6, 2 | a confirmar | Fondo principal en lugar del blanco puro |
| **Carbón** | `#2B2320` | 43, 35, 32 | 0, 19, 26, 83 | a confirmar | Texto principal |
| **Blanco** | `#FFFFFF` | 255, 255, 255 | 0, 0, 0, 0 | — | Texto sobre oscuros, fondos de etiqueta |

### 1.3 Acentos por producto (propuesta)

Pollo y cerdo siguen el código de canastillas de la planta (pollo azul, cerdo verde; `erp.md` §4).

| Producto | Nombre | HEX | RGB | CMYK aprox. | Texto encima |
|---|---|---|---|---|---|
| Canívoros Pollo y Salmón · Chorizos | Salmón | `#E8745A` | 232, 116, 90 | 0, 50, 61, 9 | Carbón |
| Canívoros Pollo · Hamburguesas | Azul pollo | `#2F5DA8` | 47, 93, 168 | 72, 45, 0, 34 | Blanco |
| Canívoros Cerdo · Hamburguesas | Verde salvia | `#5E7F3A` | 94, 127, 58 | 26, 0, 54, 50 | Blanco |
| Canívoros Ternera · Hamburguesas | Vino | `#8A2C3B` | 138, 44, 59 | 0, 68, 57, 46 | Blanco |
| Gatívoros Salmón y Cerdo · Chorizos | Azul cielo (del sitio) | `#9EC9E2` | 158, 201, 226 | 30, 11, 0, 11 | Carbón |
| Programa Criadores (material comercial) | Tostado | `#804607` | 128, 70, 7 | 0, 45, 95, 50 | Blanco |

Pantone de todos los acentos: a confirmar con imprenta. **Núcleos y orejas no tienen color:** están fuera de la arquitectura.

### 1.4 Colores retirados o prohibidos

- Magenta `#B42357` (variante antigua del logo): retirado.
- Coral del sitio `#F66161` y amarillo `#F7E597`: no forman parte de la paleta nueva. Si siguen en la web, reemplazarlos al rediseñarla.
- Rojo sangre, verde fosforescente, negro puro `#000000` en fondos grandes: no.

## 2. Proporciones de uso (60/30/10)

| Proporción | Canívoros | Gatívoros |
|---|---|---|
| **60 %** dominante | Hueso `#FBF6EC` (o foto) | Plata `#EAEAE9` o hueso |
| **30 %** de marca | Oro `#C18C36` + oro claro + tostado | Oro (logo y títulos) + azul cielo `#9EC9E2` |
| **10 %** contraste y acento | Carbón o azul noche para texto, **máx. 5 % del acento del producto** | Carbón para texto |

En material oscuro (web, B2B) se invierte: 60 % azul noche, 30 % oro, 10 % hueso o blanco para el texto.

## 3. Combinaciones permitidas y contraste WCAG 2.1

AA exige 4,5:1 para texto normal y 3:1 para texto grande (≥ 24 px, o ≥ 18,5 px en negrita). AAA exige 7:1.

| Texto | Fondo | Contraste | Resultado | Uso |
|---|---|---|---|---|
| Carbón `#2B2320` | Hueso `#FBF6EC` | 14,3:1 | AAA | Texto principal |
| Carbón | Blanco | 15,4:1 | AAA | Etiquetas |
| Carbón | Plata `#EAEAE9` | 12,8:1 | AAA | Gatívoros |
| Carbón | Oro claro `#E2B560` | 8,1:1 | AAA | Bandas claras |
| Carbón | Oro `#C18C36` | 5,2:1 | AA | Bandas de marca |
| Carbón | Azul cielo `#9EC9E2` | 8,7:1 | AAA | Gatívoros |
| Carbón | Salmón `#E8745A` | 5,2:1 | AA | Pollo y Salmón |
| Tostado `#804607` | Hueso | 7,0:1 | AAA | Títulos de marca |
| Tostado | Plata | 6,2:1 | AA | Gatívoros |
| Blanco | Tostado | 7,5:1 | AAA | Sellos, programa criadores |
| Blanco | Azul noche `#202A54` | 13,8:1 | AAA | Web oscura |
| Oro claro | Azul noche | 7,2:1 | AAA | Titulares sobre oscuro |
| Oro | Azul noche | 4,7:1 | AA | Titulares sobre oscuro |
| Blanco | Azul pollo `#2F5DA8` | 6,5:1 | AA | Pollo |
| Blanco | Vino `#8A2C3B` | 8,4:1 | AAA | Ternera |
| Blanco | Verde salvia `#5E7F3A` | 4,6:1 | AA (justo) | Cerdo. Texto en negrita |
| Blanco | Oro | 3,0:1 | Solo texto grande | Titulares grandes; nunca texto pequeño |

**Combinaciones prohibidas (no pasan AA):** blanco sobre oro claro (1,9), blanco sobre azul cielo (1,8), blanco sobre plata (1,2), oro sobre hueso (2,8), tostado sobre oro (2,5), carbón sobre tostado (2,1), carbón sobre azul pollo (2,4), carbón sobre vino (1,8), tostado sobre azul noche (1,8).

## 4. Diferenciación frente a la categoría

Fuente: revisión Market Researcher, 10 nov 2026 (colores leídos del CSS de cada sitio).

- La categoría natural en Bogotá usa **verde** (Pixie `#428330`, Peluditos `#4c9f38`) o **rojo** (Vital Doggy `#d20133`, Rawf `#d32300`, Purina `#e91c24`).
- **Ninguna usa dorado.** El oro del logo es el color propio de Canívoros: **OBLIGATORIO** que domine sobre cualquier acento.
- El verde salvia y el vino son solo acentos de producto (máx. 5 %). **Prohibido** usar verde o rojo como color dominante de una pieza.
- La web actual usa la paleta del tema Colibri (azul `#303e7a`, amarillo `#f7e597`, coral `#f66161`), que no tiene relación con el logo. Al rediseñarla, llevar el oro y el tostado a la web; el azul noche `#202A54` se conserva como fondo oscuro.

## 5. Cómo pedir color a una IA

- Nombra el color **y** su HEX: «fondo hueso `#FBF6EC`», no «fondo crema».
- En fotos, pide **paleta cálida** con tonos madera, crema y dorado; el acento del producto aparece en un objeto (servilleta, plato, banda) y no domina.
- Indica proporciones: «60 % hueso, 30 % oro, 10 % carbón».
- No pidas el degradado del logo para el logo: el logo no se genera (`03-logo.md` §1).
