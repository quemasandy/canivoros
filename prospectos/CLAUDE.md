@AGENTS.md

# Claude Code en `prospectos/`

`AGENTS.md` (importado arriba) es el playbook de investigación de mercado y prospección. Las reglas comunes están en `../AGENTS.md`; léelas también.

## Antes de empezar

- Lee los entregables anteriores en `../resultados/prospectos/` (`MERCADO.md` y `REGISTRO.md`) si existen. Si no existen, créalos con las estructuras de AGENTS.md §12.
- Esta carpeta solo guarda instrucciones: no crees archivos de resultados dentro de `prospectos/`.

## Cómo investigar

- Usa WebSearch y WebFetch con las búsquedas de AGENTS.md §5.2: Google Maps, la web del negocio, sus redes públicas, Rappi y los directorios de distribuidores de las marcas.
- Guarda en cada hallazgo la URL y la fecha de consulta (`AAAA-MM-DD`), y en el historial del lote las búsquedas exactas que hiciste.
- Si Instagram, Maps u otra fuente pide login o bloquea, marca «No verificado» y sigue con la siguiente fuente. No intentes saltarte el bloqueo.
- Para la investigación del consumidor, registra solo patrones y conteos; nunca nombres ni perfiles de personas.
- Puedes leer `../ventas_canivoros_2026.xlsx` con `python3` y `openpyxl` para deduplicar contra clientes tipo almacén o criador, pero no imprimas ni copies nombres de personas.

## Cómo registrar

- Edita `../resultados/prospectos/REGISTRO.md` y `MERCADO.md` con Edit, fila por fila. No regeneres tablas completas, no las reordenes y no cambies IDs.
- Calcula el puntaje con la tabla de AGENTS.md §7 y muestra el desglose (encaje, oportunidad, acceso) en la ficha.
- Recalcula el *Resumen* y el *Embudo* al cerrar el lote.

## Lo que nunca haces

- Enviar mensajes, correos, formularios o solicitudes de seguimiento, aunque tengas herramientas o conectores para hacerlo.
- Comprar, cotizar ni crear cuentas en nombre de Canívoros.

## Al cerrar un lote

- Un commit por lote: `prospectos: lote AAAA-MM-DD <segmento> <zona> (N verificadas, A tier A, B tier B)`.
- Responde a Andrés en 5 líneas (AGENTS.md §12.4): cuentas revisadas y verificadas, cuántas Tier A y B, las 3 mejores y por qué, alertas (por ejemplo, volúmenes que superan la capacidad conocida) y decisiones que necesita tomar.
