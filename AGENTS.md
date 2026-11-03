# Instrucciones para agentes · Canívoros

Repositorio de trabajo comercial de **Canívoros** (alimento natural horneado para perros y gatos, Sopó, Cundinamarca). Objetivo: aumentar las ventas en Bogotá.

## Dónde está cada cosa

- Empresa: `CANIVOROS-REFERENCIA-EMPRESA.md` (lo que dice la marca) y `erp.md` (la operación).
- Plan: `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`.
- Tareas y prioridades: `backlog/README.md`.
- Si la carpeta tiene su propio `AGENTS.md`, léelo: manda sobre este.

## Reglas

- No contactes a nadie ni publiques nada sin aprobación de Andrés. Entrega borradores.
- No inventes datos. Lo que no se sabe se escribe `desconocido`.
- No guardes secretos ni datos personales. De `ventas_canivoros_2026.xlsx` usa solo agregados.
- Escribe en español, con frases cortas.

## Skills para Codex

- Usa las skills de `.agents/skills/`: `analisis-competencia`, `embudos-de-venta` y `encontrar-prospectos`.
- Cada carpeta es un enlace simbólico a la skill correspondiente en `.claude/skills/`. Esa es la fuente compartida de instrucciones, referencias, plantillas y scripts.
- Lee el `SKILL.md` completo de la skill elegida y las guías `AGENTS.md` que indique. Resuelve sus referencias relativas desde la carpeta de esa skill y ejecuta los comandos desde la raíz del repositorio.
- Cuando una skill mencione `WebSearch` o `WebFetch`, usa las herramientas de búsqueda y lectura web disponibles en Codex. Si no hay acceso, deja el dato como `desconocido`.
- Al editar una skill, modifica su fuente en `.claude/skills/`; el enlace de Codex refleja el mismo cambio.

## Git

- Rama desde `develop` y PR hacia `develop`.
- Commits en español con prefijo (`docs:`, `backlog:`, `fix:`).
