@AGENTS.md

# Claude Code en este repositorio

Las reglas del proyecto están en `AGENTS.md` (importado arriba). Este archivo solo agrega cómo aplicarlas con Claude Code.

## Antes de editar

- Lee el `AGENTS.md` de la carpeta en la que vas a trabajar (`prospectos/`, `competencia/`). Sus `CLAUDE.md` lo importan, pero léelo completo antes del primer cambio.
- Revisa `backlog/README.md` para saber en qué semana y con qué dependencias está la tarea BL que vas a tocar.
- `git status` y `git fetch origin`. Si el cambio es nuevo, crea una rama desde `develop`: `git checkout -b docs/<tema> origin/develop`.

## Herramientas

- **Investigación web** (WebSearch, WebFetch): anota en el archivo la URL y la fecha de consulta (`AAAA-MM-DD`). Si una página bloquea, pide login o no carga, marca `No verificado`; no busques formas de saltarte el bloqueo.
- **Excel** (`ventas_canivoros_2026.xlsx`): léelo con `python3` y `openpyxl` (`data_only=True`). Muestra y guarda solo agregados; no imprimas nombres de clientes en respuestas, archivos, commits ni PR. Las columnas mezclan lb y kg: no sumes unidades distintas.
- **PDF** (`QFD.pdf`): léelo por páginas; es material de referencia, no datos de Canívoros.
- **Conectores** (Gmail, Slack, Calendar, Notion, WhatsApp u otros): no los uses para escribir a prospectos, clientes, distribuidores ni competidores, ni para publicar. Si Andrés pide un borrador, entrégalo en el chat o en el archivo correspondiente.
- **Odoo, VPS y hosting:** fuera de alcance. Si una tarea los requiere, descríbela y déjala para Sebastián.

## Al editar

- Haz cambios puntuales con Edit. No reordenes tablas ni renumeres IDs (`BL-###`, `P###`, `C##`).
- Mantén el estilo del repo: español de Colombia, frases cortas, tablas, etiquetas (E)/(D)/(H)/(V) y `desconocido`.
- No reescribas `erp.md` ni `CANIVOROS-REFERENCIA-EMPRESA.md` para corregirlos: son registros de fuentes.
- Si cambias un `BL-*.md`, actualiza `backlog/README.md` y regenera los dos consolidados de `backlog/`.

## Git y PR

- Commits pequeños en español con prefijo (`docs:`, `backlog:`, `prospectos: lote AAAA-MM-DD <zona>`, `competencia: revisión AAAA-MM-DD`).
- **Nunca** uses `git push --force`, `git reset --hard` sobre ramas publicadas ni `--no-verify`.
- Antes de abrir o actualizar un PR: `git diff --stat origin/develop...HEAD`. Debe tocar solo los archivos del propósito del PR.
- PR hacia `develop`. En la descripción: qué cambia, qué no, qué queda `desconocido` y confirmación de que nadie fue contactado.

## Al terminar una tarea

Responde en pocas líneas:

1. Qué cambió (archivos y conteos, por ejemplo «8 prospectos verificados, 2 descartados»).
2. Qué sigue `desconocido` o (V).
3. Qué necesita aprobación o decisión de Andrés (máximo 3 puntos).
