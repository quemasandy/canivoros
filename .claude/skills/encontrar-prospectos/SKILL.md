---
name: encontrar-prospectos
description: Encuentra, verifica y prioriza negocios de Bogotá que puedan comprar y volver a comprar Canívoros (pet shops, tiendas de alimento natural o BARF, veterinarias con punto de venta, criaderos, adiestramiento, guarderías, hoteles y peluquerías caninas), por lotes de máximo 10, con fuente y fecha por dato, nivel A/B/C y borradores de mensaje sin enviar, todo en un solo archivo con fecha, prospectos/prospectos-AAAA-MM-DD.md, más su .csv. Úsala siempre que se pida buscar, encontrar, armar, verificar, depurar o priorizar prospectos, clientes potenciales, leads, aliados, distribuidores o puntos de venta para Canívoros; cuando se pregunte "¿qué tiendas venden BARF en Suba?", "¿qué criaderos podrían comprarnos?" o "¿a quién le escribimos primero?"; al trabajar prospectos_bogota.xlsx, el archivo prospectos-AAAA-MM-DD.md o .csv, un lote de prospectos o las tareas BL-010, BL-012 o BL-043, aunque no se diga la palabra "prospecto".
---

# Encontrar prospectos

Esta skill ejecuta la guía del equipo en `prospectos/AGENTS.md`. **Léela primero, junto con `AGENTS.md` de la raíz y `prospectos/CLAUDE.md`: mandan sobre esta skill.** Si algo de aquí las contradice, gana la guía; si la guía cambió, síguela y avisa de la diferencia.

Lo que la skill agrega a la guía: el procedimiento de un lote de principio a fin, la plantilla del archivo de prospectos y un script que prepara el archivo del día, genera el CSV, revisa el registro y detecta duplicados, fuentes faltantes y coincidencias con clientes actuales.

## Archivos de salida: siempre con fecha, siempre .md y .csv

Todo lo que produce la skill va en **un solo par de archivos con la fecha del día** en `prospectos/`:

| Archivo | Qué tiene |
|---|---|
| `prospectos-AAAA-MM-DD.md` | Todo: resumen general, cómo se verificó, la tabla del registro y un bloque `## Lote N` por lote (resumen, búsquedas, notas, fichas A y borradores B) |
| `prospectos-AAAA-MM-DD.csv` | La misma tabla del registro, una fila por negocio, para abrir en Excel o Google Sheets |

Reglas:

- **Siempre con fecha.** Ningún archivo de resultados sin fecha (`REGISTRO.md`, `lote.md`, `prospectos.md`). La fecha es la del día en que se trabaja (AAAA-MM-DD).
- **Siempre los dos formatos.** Cada vez que cambia el `.md`, regenera el `.csv` con `registro.py csv`. El `.csv` no se edita a mano: el `.md` manda.
- **Un solo par en la carpeta.** Si se trabaja otro día, `registro.py preparar prospectos` renombra el par a la fecha de hoy y ahí se agrega lo nuevo. No dejes copias de días anteriores: el historial queda en git.
- `registro.py revisar` marca como bloqueante un archivo sin fecha, un `.csv` que falta o un `.csv` que no coincide con el `.md`.

El objetivo es una lista **corta, real y contactable**. La lista de 134 prospectos de Bogotá se armó con IA y quedó llena de campos desconocidos (BL-010). Diez negocios verificados valen más que cien supuestos: cada dato falso cuesta una llamada perdida y le resta credibilidad a quien llama.

## Qué se pide y qué hacer

| Pedido | Qué hacer |
|---|---|
| "Busca tiendas / veterinarias / criaderos en X" | Un lote nuevo (pasos 1 a 7) |
| "Revisa / completa esta lista" (p. ej. `prospectos_bogota.xlsx`) | Importa la lista al registro (paso 2) y verifica por lotes de 10 de una misma localidad |
| "¿A quién le escribimos primero?" | Revisa el registro (paso 5) y propone los mejores A verificados |
| "Busca negocios parecidos a los que más compran" | Usa solo agregados de `ventas_canivoros_2026.xlsx` (ver "Parecidos") y luego haz un lote |

## 1. Definir el lote

Un lote es **un tipo de negocio y una localidad o barrio de Bogotá, con máximo 10 negocios**. Si piden más, haz varios lotes.

Si no dicen tipo o zona, empieza por tiendas de mascotas y de alimento natural en Usaquén, y sigue con Suba y Chapinero, que son las zonas de BL-010. Dilo en el resumen como supuesto. Si el pedido no es de Canívoros (por ejemplo, pymes para el diagnóstico de Growth Partner), avisa que esta skill no cubre ese caso.

## 2. Revisar lo que ya existe

Los resultados se guardan en la carpeta `prospectos/`, junto a la guía. Primero deja listo el archivo de hoy, desde la raíz del repositorio:

```bash
python3 .claude/skills/encontrar-prospectos/scripts/registro.py preparar prospectos
```

Imprime la ruta del archivo de hoy (`prospectos/prospectos-AAAA-MM-DD.md`). Si no había ninguno, lo crea desde `assets/prospectos.md` con su `.csv`. Si el más reciente es de otro día, lo renombra a la fecha de hoy. Si avisa de archivos del formato anterior (`REGISTRO.md`, `lote-*.md`) o de varios archivos con fecha, unifícalos en el de hoy y bórralos. En los comandos siguientes, `prospectos/prospectos-AAAA-MM-DD.md` es esa ruta.

Luego revisa lo que ya existe:

```bash
python3 .claude/skills/encontrar-prospectos/scripts/registro.py revisar prospectos/prospectos-AAAA-MM-DD.md --excluir ventas_canivoros_2026.xlsx
```

Te da el siguiente ID libre, lo que ya está registrado (para no repetirlo) y los problemas pendientes.

Para traer una lista externa (CSV o XLSX) al registro:

```bash
python3 .claude/skills/encontrar-prospectos/scripts/registro.py importar prospectos_bogota.xlsx --registro prospectos/prospectos-AAAA-MM-DD.md --excluir ventas_canivoros_2026.xlsx
```

Sin `--escribir` solo muestra las filas que agregaría. Con `--escribir` las agrega como nivel C, estado `por verificar` y fuente marcada (V), y actualiza el `.csv`. Omite duplicados del registro, distribuidores publicados y coincidencias con clientes del Excel de ventas. Una lista importada no está verificada: después hay que verificarla por lotes.

## 3. Buscar

Lee `references/busquedas.md`: tiene las localidades, consultas listas para copiar por tipo de negocio, las fuentes de la guía y cómo leer cada una.

- Usa WebSearch y WebFetch (o la herramienta de lectura web disponible). Anota cada búsqueda en la tabla "Búsquedas hechas" del bloque del lote: fecha, fuente, consulta y resultados útiles.
- Junta unos 15 o 20 candidatos para quedarte con 10: muchos se caen al verificar (cerrados, solo accesorios, duplicados, fuera de la zona).
- La mejor pista para tiendas son las páginas "dónde comprar" de marcas naturales: esas tiendas ya venden natural.
- Anota la URL de cada dato en el momento en que lo encuentras. Reconstruir fuentes después casi nunca funciona.

## 4. Verificar

Sigue el paso 3 de la guía (existe y opera, datos comerciales, encaje, tamaño) y la lista de verificación de `references/busquedas.md`.

- **No inventes ni completes datos.** Si un teléfono, una dirección o una marca no aparecen en una fuente, escribe `desconocido`. No deduzcas teléfonos ni marcas por el tipo de tienda, y no conviertas un "probablemente" en dato.
- **Marca la evidencia** como pide la guía: (E) visto en una fuente con URL y fecha, (D) lo dice el negocio de sí mismo, (H) interpretación tuya, (V) dudoso o sin fecha.
- **Solo datos comerciales públicos.** Nada de celulares personales, direcciones de vivienda, cédulas ni nombres de clientes. Muchos criaderos son personas: usa solo el canal que publican para vender.
- **Si una página pide iniciar sesión o bloquea**, anota "No verificado" y sigue. No evadas bloqueos.

## 5. Registrar y priorizar

Agrega cada negocio revisado a la tabla "Registro" de `prospectos-AAAA-MM-DD.md` con el siguiente ID libre (`P001`, `P002`…; nunca se reutilizan) y asígnale nivel según la tabla de la guía:

- **A**: verificado, atiende perros y ya trabaja con alimento natural o maneja mucho volumen.
- **B**: verificado y atiende perros, sin señales claras de alimento natural.
- **C**: datos incompletos o poco encaje.

Registra también los descartados (cerrados, duplicados, solo gatos, personas sin negocio) con estado `descartado: <motivo>` y nivel `—`, para no volver a revisarlos. **Excepción:** si un candidato coincide con un cliente del Excel de ventas, no escribas su nombre en ningún archivo (ni en el `.md` ni en el `.csv`); anota en las notas del lote solo que hubo una coincidencia.

Después genera el `.csv` y vuelve a revisar:

```bash
python3 .claude/skills/encontrar-prospectos/scripts/registro.py csv prospectos/prospectos-AAAA-MM-DD.md
python3 .claude/skills/encontrar-prospectos/scripts/registro.py revisar prospectos/prospectos-AAAA-MM-DD.md --excluir ventas_canivoros_2026.xlsx
```

Corrige lo que marque como bloqueante: archivo sin fecha, `.csv` que falta o no coincide, duplicados, A o B sin verificar, verificados sin URL o sin fecha, verificaciones de más de 90 días, coincidencias con distribuidores o clientes. Si cambias el `.md`, vuelve a generar el `.csv`. Las coincidencias son **posibles**, no seguras: si confirmas que no es cliente, escribe `no es cliente` en la columna Notas y el script deja de marcarla.

## 6. Preparar el abordaje

Lee `references/abordaje.md`. Para cada **A**: 2 o 3 hechos con fuente que expliquen por qué es buen cliente, qué le puede interesar de Canívoros, preguntas para la primera conversación y un borrador de mensaje. Para cada **B**, solo el borrador. Los **C** quedan en el registro.

Los borradores no llevan precios, condiciones, beneficios de salud, "sin subproductos", "super premium" ni "registro ICA", y usan `[número comercial por definir]` como contacto. **Nunca contactes a nadie** ni uses conectores (correo, WhatsApp, Slack, redes) para escribir: Andrés aprueba cada contacto.

## 7. Cerrar el lote

Agrega el lote al mismo `prospectos-AAAA-MM-DD.md`, como un bloque `## Lote N · AAAA-MM-DD · <tipo> · <zona> (P0xx–P0yy)` debajo del registro, con la estructura de `assets/prospectos.md` (resumen, búsquedas, notas, fichas A, borradores B). No crees archivos de lote aparte. Actualiza el "Resumen general" del inicio (totales, mejores y decisiones pendientes), regenera el `.csv` y corre `revisar` hasta que no queden bloqueantes.

Responde en el chat con el resumen de 5 líneas que pide `prospectos/CLAUDE.md`:

```markdown
1. Revisados: N negocios de <tipo> en <localidad> (P0xx–P0yy).
2. Resultado: A a · B b · C c · descartados d (motivo principal).
3. Los 3 mejores: <nombre> (por qué, en una frase con el hecho clave) · <nombre> (…) · <nombre> (…).
4. Quedó `desconocido`: <qué datos faltaron y en cuántos negocios>.
5. Debe decidir Andrés: <aprobaciones de contacto, dudas de clientes actuales, avisos de volumen grande>.
```

Agrega al final la ruta de los dos archivos (`.md` y `.csv`) y los supuestos que hiciste (tipo, zona). No hagas commit ni push de los resultados salvo que te lo pidan.

## Parecidos a los mejores clientes

`ventas_canivoros_2026.xlsx` separa compras de cliente final, almacén y criador por columnas (`HAM. CRIADOR KG`, `HAM. ALMACEN LB`…), una hoja por mes. Usa **solo agregados**: kilos o libras por tipo de comprador y mes, número de compradores por tipo, frecuencia. En julio–octubre de 2026 hubo compras de criadores de 40 a 520 kg (BL-043), lo que apunta a criaderos de razas grandes. Describe el patrón sin nombres y busca negocios con ese patrón que no estén en el Excel. Respeta la unidad de cada columna (libras o kilos).

Si un prospecto podría pedir volúmenes muy grandes, avísalo en la línea 5 del resumen: la capacidad de producción es `desconocido`.

## Errores frecuentes

- Entregar muchos nombres sin canal ni fuente. Mejor 10 verificados y las búsquedas para el siguiente lote.
- Guardar resultados en archivos sin fecha, en archivos de lote sueltos o solo en `.md`: todo va en `prospectos-AAAA-MM-DD.md` y su `.csv`.
- Tomar el barrio o el estrato como prueba de demanda. El encaje se demuestra con lo que vende el negocio y su actividad reciente.
- Registrar a un distribuidor o cliente actual como prospecto, o a una tienda que ya compra a un aliado, sin avisar.
- Incluir negocios solo de gatos: la guía los descarta.
- Prometer precios, pedido mínimo o condiciones: son `desconocido` hasta que se confirmen (BL-005).
