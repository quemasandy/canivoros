@AGENTS.md

# Claude Code en `competencia/`

`AGENTS.md` (importado arriba) es el playbook de inteligencia competitiva. Las reglas comunes están en `../AGENTS.md`; léelas también.

## Antes de empezar

- Lee los entregables anteriores en `../resultados/competencia/` si existen. Si no existen, créalos con las estructuras de AGENTS.md §11.
- Escribe el brief (pregunta de negocio, segmento, conjunto competitivo y decisión) antes de buscar datos.

## Cómo investigar

- Usa WebSearch y WebFetch: web y tienda online de cada marca, su página de distribuidores, Rappi, Mercado Libre, Google Maps, redes públicas, la Biblioteca de anuncios de Meta y el Centro de transparencia de anuncios de Google.
- Guarda la URL y la fecha de consulta (`AAAA-MM-DD`) de cada precio, afirmación y anuncio. Captura los precios de todas las marcas en la misma sesión o semana.
- Calcula precio por kg y costo diario con las fórmulas de AGENTS.md §7 y muestra la cuenta.
- Si una página pide login, bloquea o no muestra precio, escribe `desconocido` o «No verificado». No deduzcas un precio de otra presentación.
- Reseñas: cuenta y clasifica por tema; no copies autores ni comentarios completos.

## Lo que nunca haces

- Comprar, pedir cotizaciones, llenar formularios de distribuidor o escribir a una marca, aunque tengas herramientas o conectores para hacerlo.
- Publicar o enviar comparaciones con nombres de competidores.

## Cómo registrar

- Edita `../resultados/competencia/COMPETENCIA.md` con Edit, fila por fila. No reordenes la tabla ni cambies IDs `C##`.
- Cada análisis nuevo va en su propio `informe-AAAA-MM-DD.md`; los cambios del mes, en `RADAR.md`.
- Commit por revisión: `competencia: revisión AAAA-MM-DD (N marcas, M precios con fecha)`.

## Al terminar

Responde a Andrés en 5 líneas: pregunta respondida, los 3 hallazgos principales con su recomendación, competidores de amenaza alta, qué quedó `desconocido` y qué decisión necesita tomar.
