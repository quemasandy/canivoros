# 00 · Índice y cómo usar este manual con IA

Manual de identidad de **Canívoros & Gatívoros** · versión 1.0 · 10 nov 2026 · Borrador de trabajo de Andrés. **No está aprobado por la empresa.** No publicar ni imprimir piezas finales sin el visto bueno de la sección 09.

Este manual está **solo en texto** a propósito. Está escrito para que un agente de IA (generador de imagen, diseñador IA, copywriter IA) pueda producir piezas correctas **sin ver ninguna imagen**. Cada color tiene HEX, cada forma tiene descripción verbal y cada regla dice si es obligatoria.

## 1. Orden de lectura

| Orden | Archivo | Léelo si vas a… |
|---|---|---|
| 1 | `00-indice-y-como-usar-con-ia.md` (este) | Cualquier tarea |
| 2 | `01-plataforma-estrategia-y-mensajes.md` | Cualquier tarea. Es el «por qué» |
| 3 | `02-identidad-verbal.md` | Escribir cualquier texto |
| 4 | `03-logo.md` | Poner el logo en una pieza |
| 5 | `04-color.md` | Elegir colores |
| 6 | `05-tipografia.md` | Poner texto en una pieza |
| 7 | `06-elementos-graficos.md` | Usar patrones, íconos, formas o grillas |
| 8 | `07-fotografia-y-video.md` | Generar o editar fotos y videos |
| 9 | `08-aplicaciones.md` | Hacer una pieza concreta (empaque, post, volante…) |
| 10 | `09-gobierno-de-marca.md` | Entregar, nombrar o publicar una pieza |
| 11 | `10-plantilla-brief-agente-ia.md` | Encargar una pieza a otro agente |

Documentos de estrategia que este manual resume y no contradice (carpeta `branding/`): `01-estrategia-posicionamiento.md`, `02-personalidad-y-voz.md`, `03-mensajes.md`, `04-identidad-visual.md`, `05-aplicacion-por-producto.md`, `06-analisis-competidor-friskies.md`.

## 2. Jerarquía de reglas (qué manda sobre qué)

Si dos reglas chocan, gana la de número menor:

1. **Ley y regulación:** lo que exija el ICA y la norma colombiana de etiquetado de alimentos para animales, y la ley de protección de datos (Ley 1581 de 2012). Lo que no sepamos de la norma se marca **a confirmar con ICA**.
2. **Reglas de verdad:** no inventar productos, cifras, precios, registros ni beneficios de salud (`02-identidad-verbal.md` §6).
3. **Reglas OBLIGATORIAS** de este manual (marcadas así).
4. **Reglas RECOMENDADAS** de este manual.
5. Lo que pida el brief puntual.
6. El criterio del agente.

## 3. Obligatorio vs recomendado

- **OBLIGATORIO:** no se negocia. Una pieza que lo incumple se rechaza.
- **RECOMENDADO:** es lo normal. Se puede romper con una razón escrita en el brief.
- **PROPUESTA:** decisión nuestra que la empresa todavía no aprobó. Úsala, pero no la presentes como oficial.
- **A VALIDAR:** dato o claim sin respaldo. **No va en piezas públicas** hasta que se valide.

## 4. Las 10 reglas que nunca se rompen (resumen OBLIGATORIO)

1. **No dibujes ni regeneres el logo con IA.** Deja el espacio vacío y se coloca el archivo original después (`03-logo.md` §1).
2. **Solo productos reales:** los 5 del catálogo y el Programa Criadores (`01-plataforma-estrategia-y-mensajes.md` §3). No inventes sabores, tamaños ni líneas.
3. **Nada de precios** salvo que el brief traiga el precio confirmado por la empresa.
4. **Ningún beneficio de salud** («mejora la digestión», «fortalece defensas», «limpia dientes»…), ni «sin subproductos», «100 % natural», «100 % carne real» o «super premium». Para perros, tampoco «carnívoros» como claim (solo para gatos).
5. **Registro ICA:** usa solo los números del listado ICA (22065AL, 24065AL, 24713AL; `01` §2, C13) y solo cuando la dueña confirme qué producto ampara cada uno. Si no, escribe `Reg. ICA [número a confirmar]`. Nunca inventes un número ni digas «certificado».
6. **Colores solo de la paleta** (`04-color.md`). El magenta antiguo está retirado.
7. **Tipografía:** Fredoka para títulos y Nunito para texto.
8. **Perros y gatos reales y sanos**, en luz natural. Nada de carne cruda sangrante.
9. **Español de Colombia, tuteo**, frases cortas.
10. **Toda pieza pasa el checklist** de `09-gobierno-de-marca.md` antes de publicarse.

## 5. Cómo citar el manual en un prompt

Usa este bloque al inicio de cualquier encargo a otro agente. Copia solo las secciones que necesite la tarea:

```
Sigue el manual de marca de Canívoros & Gatívoros v1.0
(repo quemasandy/canivoros, rama branding, carpeta branding/manual/).
Reglas obligatorias: 00 §4.
Para esta pieza aplica: [03-logo §X], [04-color §Y], [05-tipografia §Z], [08-aplicaciones §N].
Producto: [nombre exacto del catálogo, ej. "Canívoros Chorizos de Pollo y Salmón 500 g, CAN-PS-500"].
Si algo no está en el manual, pregunta o márcalo [A VALIDAR]; no lo inventes.
```

Cuando el agente no puede leer el repositorio, pega el texto de las secciones dentro del prompt. Cita siempre por **archivo y sección** (por ejemplo, «04-color §3»), no por número de página.

## 6. Qué esperar del agente que recibe el manual

- Que devuelva la pieza **y** una lista de qué reglas aplicó y qué datos dejó como `[A VALIDAR]`.
- Que no rellene huecos con datos «razonables». Un hueco se entrega como `[falta: …]`.
- Que use los nombres de archivo de `09-gobierno-de-marca.md` §5.

## 7. Estado del manual

| Tema | Estado |
|---|---|
| Logo | Existe en PNG (sitio web). **Falta el vector** y las versiones horizontal, vertical e isotipo |
| Paleta | Núcleo extraído del logo real; soporte y acentos son PROPUESTA |
| Tipografía | PROPUESTA (el sitio hoy usa otras) |
| Catálogo | 5 productos en Odoo + venta por volumen + núcleos y orejas por definir |
| Claims | Casi todos A VALIDAR. Registro completo en `01` §2, con el fact-check Researchy (9 nov 2026, PR #7) |
| Aprobación | Pendiente de Andrés y de la dueña |
