# 05 · Tipografía

Manual Canívoros & Gatívoros v1.0 · 10 nov 2026. **PROPUESTA.** Ambas familias son gratuitas en Google Fonts (licencia SIL Open Font License) y sirven para impresión, web y redes.

## 1. Familias

| Rol | Familia | Pesos | Por qué |
|---|---|---|---|
| **Títulos, nombres de producto, cifras grandes** | **Fredoka** | SemiBold 600, Bold 700 | Redondeada y gruesa como las letras del logo. Muy legible en empaque |
| **Texto, interfaces, WhatsApp, etiquetas, legal** | **Nunito** | Regular 400, SemiBold 600, Bold 700, Italic 400 | Redondeada, cálida y clara en tamaños pequeños |
| Alternativa a Fredoka | Baloo 2 | 600, 700 | Si una herramienta no tiene Fredoka |

**El logo no se compone con estas fuentes:** sus letras son un dibujo propio (`03-logo.md`).

El sitio hoy carga Aclonica, Holtwood One SC, Open Sans, Muli, Playfair Display, Butcherman, Gravitas One, Goblin One y Abril Fatface. Al rediseñarlo, dejar solo Fredoka y Nunito.

## 2. Alternativas del sistema (cuando no se pueden instalar fuentes)

| En lugar de | Usa | Si tampoco existe |
|---|---|---|
| Fredoka | Arial Rounded MT Bold | Verdana Bold, Arial Bold |
| Nunito | Segoe UI (Windows) / SF Pro (Apple) / Roboto (Android) | Arial |

Pila CSS: `font-family: "Fredoka", "Baloo 2", "Arial Rounded MT Bold", Arial, sans-serif;` y `font-family: "Nunito", "Segoe UI", Roboto, Arial, sans-serif;`

## 3. Jerarquía

Tamaños relativos al cuerpo de texto (1 = tamaño base). Base recomendada: 16 px en web, 28 px en post de 1080 px, 9 pt en empaque.

| Nivel | Familia y peso | Tamaño relativo | Interlineado | Tracking | Caja | Ejemplo |
|---|---|---|---|---|---|---|
| **Display** (titular de post, frente de empaque) | Fredoka 700 | 3,0 – 4,0 | 1,05 | −1 % | Tipo oración o MAYÚSCULAS cortas (≤ 3 palabras) | «POLLO Y SALMÓN» |
| **H1** | Fredoka 700 | 2,5 | 1,1 | −0,5 % | Tipo oración | «Hecho por criadores.» |
| **H2** | Fredoka 600 | 1,75 | 1,2 | 0 | Tipo oración | «Cómo se guarda» |
| **H3** | Nunito 700 | 1,25 | 1,3 | 0 | Tipo oración | «Para perros» |
| **Antetítulo / etiqueta** | Nunito 700 | 0,8 | 1,2 | +12 % | MAYÚSCULAS | «GATÍVOROS · DE LA CASA CANÍVOROS» |
| **Cuerpo** | Nunito 400 | 1,0 | 1,5 | 0 | Tipo oración | Texto corrido |
| **Destacado** | Nunito 700 | 1,0 | 1,5 | 0 | — | Datos: «500 g» |
| **Cita / testimonio** | Nunito Italic 400 | 1,1 | 1,45 | 0 | — | Solo con permiso (C16) |
| **Pie de foto, notas** | Nunito 400 | 0,85 | 1,4 | 0 | — | — |
| **Legal y etiquetado** | Nunito 400 / 600 | 0,75 (nunca menos de 6 pt impreso; la norma ICA puede exigir más, **a confirmar con ICA**) | 1,3 | +1 % | — | Registro, lote, vencimiento |

### Nota de diferenciación

La revisión Market Researcher (10 nov 2026) encontró que la categoría ya usa letra redondeada (Pixie con Dosis, Peluditos con Poppins). Se mantiene Fredoka porque **repite las letras del logo**, que son redondeadas. La diferencia no se busca en la fuente sino en el **oro, el chorizo y la coherencia**: solo dos familias en todas las piezas, también en la web.

## 4. Reglas

1. **OBLIGATORIO:** máximo dos familias por pieza (Fredoka + Nunito).
2. **OBLIGATORIO:** tildes y eñes siempre, también en MAYÚSCULAS («CANÍVOROS», «SALMÓN»).
3. Alinear a la izquierda; centrar solo titulares cortos y frentes de empaque.
4. Líneas de 45 a 75 caracteres en texto corrido.
5. MAYÚSCULAS sostenidas solo en antetítulos y titulares de 3 palabras o menos.
6. No usar cursiva de Fredoka (no existe) ni estirar, condensar o contornear letras.
7. Números con Nunito 700; peso con espacio: «500 g».
8. Color del texto según `04-color.md` §3.

## 5. Cómo pedir tipografía a una IA

- Diseñadores IA: «Títulos en Fredoka Bold 700 color tostado `#804607`; texto en Nunito Regular 400 color carbón `#2B2320`; interlineado 1,5».
- Generadores de imagen: **no les pidas texto dentro de la imagen.** Suelen escribir mal las palabras. Pide la imagen sin texto y agrega el texto después en edición con estas fuentes.
