# Guía para analizar la competencia de Canívoros en Bogotá

Esta guía es para cualquier agente de IA que investigue la competencia de Canívoros en Bogotá.
Las reglas generales del proyecto están en `../AGENTS.md`.

## Objetivo

Entender **contra quién compite Canívoros en Bogotá, qué ofrece cada competidor, cuánto cuesta y dónde se consigue**, para decidir precio, mensaje, canales y zonas.

## Canívoros en pocas líneas

- Alimento natural **horneado** para perros (y gatos con la marca Gatívoros), hecho en Sopó, Cundinamarca.
- Formatos: chorizos y hamburguesas de pollo, salmón, cerdo y ternera.
- Se vende por WhatsApp, a criadores y en algunas tiendas y veterinarias.
- Precio y ración confirmados: `desconocido`. No compares precios de Canívoros hasta que la empresa los confirme.

Más detalle en `../CANIVOROS-REFERENCIA-EMPRESA.md` y `../erp.md`.

## Paso 1 · Define la pregunta

Antes de buscar, escribe qué quieres responder. Ejemplos:

- ¿Quiénes son los competidores directos en Bogotá?
- ¿Cuánto cuesta por kg cada alternativa?
- ¿Dónde se consigue cada marca y cómo entrega?
- ¿Qué promete cada marca y qué critican sus clientes?

## Paso 2 · Arma la lista de competidores

| Tipo | Qué es | Ejemplos para verificar |
|---|---|---|
| Directo | Alimento natural cocido u horneado | Pixie, Kanuto, VITA Alimento Vital |
| BARF y precocido | Comida natural cruda o precocida | Peluditos BARF, Vital Doggy, Rawf, Dogsy, KENKO Barf, 4DOGS, Bocado Pet Food, Barftender, Santo Barf, Bitute |
| Concentrado premium | Lo que compra quien quiere "lo mejor" en seco | Taste of the Wild, Acana, Orijen, Nupec, Hill's, Pro Plan, Royal Canin |
| Alternativa casera | Cocinar en casa o comprar carne para perro | Recetas caseras, carnicerías |

Los ejemplos no están verificados. Confirma que cada marca existe y se vende en Bogotá antes de incluirla. Agrega marcas nuevas si las encuentras.

## Paso 3 · Recolecta datos públicos

Fuentes:

- Web, tienda online y página de distribuidores de cada marca.
- Rappi, Mercado Libre y otras tiendas online.
- Google Maps: puntos de venta y reseñas.
- Instagram, Facebook y TikTok.
- Biblioteca de anuncios de Meta y Centro de transparencia de anuncios de Google.

Datos por marca:

| Campo | Qué anotar |
|---|---|
| Marca y origen | Ciudad donde se produce |
| Tipo | Según la tabla del paso 2 |
| Productos | Formato (croqueta, porción, chorizo…) y conservación (congelado, refrigerado, seco) |
| Presentaciones y precios | Gramos y precio de cada empaque, regular o promoción, con fecha y URL |
| Precio por kg | `precio ÷ (gramos ÷ 1.000)` |
| Ración | Gramos por día que publica la marca para un perro de 10 kg y uno de 25 kg |
| Costo diario | `ración en gramos × precio por kg ÷ 1.000` |
| Dónde se consigue | Tiendas, veterinarias, web, WhatsApp, apps; localidades de Bogotá |
| Entrega | Zonas, costo, pedido mínimo, tiempos |
| Promesa | La frase principal de la marca |
| Reseñas | Número, promedio y temas que se repiten |
| Redes y anuncios | Redes activas, frecuencia, anuncios activos |

## Paso 4 · Compara

- **Tabla comparativa** con todas las marcas y los campos del paso 3.
- **Precios:** compara por kg y por día, no por empaque. Captura todos los precios en la misma semana.
- **Mensajes:** qué promesas repiten todos y cuáles nadie usa.
- **Reseñas:** qué valoran y qué critican los compradores (precio, entrega, aceptación del perro, conservación, atención).
- **Cobertura:** qué marcas están en cada zona de Bogotá.

## Paso 5 · Saca conclusiones

Para cada hallazgo importante escribe:

1. **Qué viste**, con fuente y fecha.
2. **Qué significa** para Canívoros.
3. **Qué recomiendas** probar.

Máximo 5 hallazgos en el resumen.

## Cómo marcar la evidencia

- **(E)** Lo viste en una fuente, con URL y fecha.
- **(D)** Lo dice la marca de sí misma.
- **(H)** Tu interpretación.
- **(V)** Dato dudoso o sin fecha.
- Lo que no sabes: `desconocido`. Ventas, márgenes y costos internos de los competidores son `desconocido`; no los estimes.

## Dónde guardar los resultados

En esta carpeta, `competencia/`. **Todos los archivos llevan la fecha en el nombre y cada análisis genera siempre un `.md` y un `.csv`:**

- `competencia-AAAA-MM-DD.md`: el informe completo del día. Pregunta, resumen de hallazgos, registro de marcas con ID `C01`, `C02`… (no se reutilizan), tabla comparativa, recomendaciones, qué no se pudo verificar y lista de fuentes.
- `competencia-AAAA-MM-DD.csv`: todos los datos del día en un solo archivo. La columna `registro` dice qué es cada fila: `marca`, `precio`, `matriz` o `resena`.

No crees archivos sin fecha ni archivos sueltos por tipo de dato. Si el par del día ya existe, actualízalo. Un análisis nuevo parte del CSV fechado más reciente, para conservar los IDs y el histórico de precios.

## Límites

- Solo información pública.
- No contactes competidores, no pidas cotizaciones y no hagas compras de prueba sin aprobación de Andrés.
- No te hagas pasar por cliente ni distribuidor.
- Si una página pide login o bloquea, anota "No verificado". No evadas bloqueos.
- No guardes datos personales de autores de reseñas ni empleados.
- No publiques comparaciones con nombres de competidores: los informes son internos.
