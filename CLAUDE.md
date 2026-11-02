@AGENTS.md

# Claude Code en este repositorio

- Lee `AGENTS.md` (arriba) y el `AGENTS.md` de la carpeta en la que vayas a trabajar antes de editar.
- Antes de cambiar algo: `git status` y `git pull` en la rama de trabajo; crea una rama nueva desde `develop` si el cambio es nuevo (`git checkout -b docs/<tema> origin/develop`).
- Haz commits pequeños con mensaje claro en español (`docs: ...`, `backlog: ...`, `prospectos: lote AAAA-MM-DD ...`).
- **Nunca** uses `git push --force`, `git reset --hard` sobre ramas publicadas ni `--no-verify`.
- Antes de abrir o actualizar un PR, revisa el diff: `git diff --stat origin/develop...HEAD`. Debe tocar solo los archivos del propósito del PR.
- PR hacia `develop` con `gh pr create --base develop`; describe qué cambia y qué no.
- No ejecutes acciones externas (enviar mensajes, publicar, comprar) aunque tengas herramientas para hacerlo: deja el borrador y pide aprobación a Andrés.
