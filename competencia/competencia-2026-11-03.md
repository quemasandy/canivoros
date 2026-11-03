# Competencia · 2026-11-03

Responsable: borrador para Andrés (investigación de escritorio) · Uso interno: no publicar.

Archivo de datos: `competencia-2026-11-03.csv` (columna `registro`: 45 filas `marca` y 40 filas `precio`). Este `.md` y ese `.csv` forman el análisis del día y reemplazan a los archivos sueltos anteriores (`COMPETENCIA.md`, `informe-2026-11-03.md`, `observaciones.csv`, `precios-normalizados.csv`, `matriz.csv` y `resenas.csv`).

> **Evidencia:** (E) visto en una fuente, con URL y fecha · (D) lo dice la marca · (H) interpretación · (V) dudoso o sin fecha. Lo que no se sabe: `desconocido`.
>
> **Alcance:** muestra exploratoria de 45 marcas registradas en la sección 3 (38 encontradas con fuentes públicas y 7 candidatas sin resultados), 40 observaciones de precio en el CSV del día (25 entran en la comparación), 0 reseñas y 0 entrevistas. Sirve para descubrir patrones; no es representativa de Bogotá.
>
> **Limitación importante:** la política de red de este entorno bloqueó la apertura de los sitios. Cada dato viene del extracto que el buscador devolvió de esa URL el 2026-11-03. En este informe, (E) significa «visto en ese extracto, con URL y fecha»; la página en sí queda «No verificado». Las fichas que el buscador fecha con más de un año, los rangos ambiguos y los precios atípicos se marcaron (V) y quedan fuera de la comparación.

## 1. Pregunta

- **Pregunta:** ¿quiénes compiten con Canívoros y Gatívoros en Bogotá, qué ofrecen, cuánto cuestan por kg, dónde se consiguen y qué prometen?
- **Decisión que alimenta:** precio y presentación (BL-005, BL-023), mensaje (BL-016, BL-020), canales y prospección mayorista (BL-012) y cómo crecer en Bogotá (BL-028).
- **Segmento y mascota:** compradores de alimento natural o premium para perros; gatos como apartado.
- **Zona:** Bogotá, con entrega a domicilio o punto de venta en la ciudad.
- **Canal:** web propia, apps de domicilio, tiendas en línea, marketplaces, petshops y veterinarias.
- **Periodo de captura:** 2026-11-03 (un solo día).
- **Fuera del alcance:** posición de precio de Canívoros (sus precios no están confirmados; BL-005), costo diario (no hay raciones publicadas en lo revisado), reseñas, entrevistas, compras de prueba y mapa por localidad.

## 2. Resumen de hallazgos

| # | Qué vimos (fuente, fecha, evidencia) | Qué significa | Qué recomendamos probar |
|---|---|---|---|
| 1 | Al menos cinco marcas con venta en Bogotá se presentan como horneadas: Pixie, Kanuto, VITA, Honesto y Kanu Pet Nativo Oven-Baked (E, D; 2026-11-03; ver C01–C05 en la sección 3). | «Horneado» ya no distingue a Canívoros por sí solo (H). | En el experimento de mensajes (BL-020) agregar variantes con otro diferencial: origen en perros de competencia, formato hamburguesa o chorizo, producción en Sopó. |
| 2 | Pixie declara más de 40.000 clientes, 32 ciudades, más de 700 puntos de venta y unas 5 toneladas diarias (D; El Espectador). Se vende en Rappi, Puppis, Agrocampo, Kanu Pet y Animals Veterinaria (E). En Agrocampo, sus porciones de 500 g cuestan entre 23.630 y 31.590 COP/kg (E). | Pixie es la referencia con la que tenderos y compradores compararán a Canívoros (H). | En la prospección mayorista (BL-012), empezar por tiendas que ya venden Pixie y preguntar rotación, margen y quejas de esa marca. |
| 3 | El alimento natural para perros cuesta desde unos 20.000 COP/kg: BARF de 20.000 a 24.000 (Bocado, GRUY), natural congelado de 21.250 a 35.800 (Pixie, Kanuto, Kanu Nativo Fresh) y húmedo estable de 43.600 a 52.800 (Dogo) (E; ver cuentas). Los empaques grandes bajan el precio por kg: Pixie 2 kg a 21.250 frente a 23.630–31.590 en 500 g (E). | Hay un piso de precio de la categoría natural en Bogotá. Dónde queda Canívoros es una pregunta abierta hasta confirmar sus precios (H). | Confirmar precios y unidades de Canívoros (BL-005) y volver a correr `competencia.py precios --propia "Canívoros"`. |
| 4 | Casi todos los naturales se venden congelados o refrigerados (E, D). VITA cobra 39.900 de envío por un paquete de 2,4 kg (D, V). Puppis da envío gratis desde 160.000 y Animals Veterinaria desde 150.000 (E). Dogo es la excepción: estable a temperatura ambiente hasta abrirlo (D). | La cadena de frío encarece la entrega en toda la categoría. Si Canívoros resulta estable o con vida refrigerada larga, sería una ventaja logística; si requiere congelación, competirá en las mismas condiciones (H). | Documentar conservación y vida útil de Canívoros con ficha técnica. Después, probar entregas programadas por microzona (BL-014). |
| 5 | Kanu Pet vende marca propia natural, Nativo Fresh y Nativo Oven-Baked (E). Gabrica lanzó Dogo en 2025 (E). Italcol tiene Chunky Menú Natural BARF, agotado al consultar (E). | Retailers y empresas grandes están entrando al segmento. Un retailer con marca propia puede no impulsar a Canívoros (H). | Priorizar petshops y veterinarias independientes que ya tengan congelador y clientes de alimento natural. Con Kanu Pet, preguntar condiciones antes de depender de ese canal. |

## 3. Registro de marcas

Salida de `python3 .claude/skills/analisis-competencia/scripts/competencia.py marcas competencia/competencia-2026-11-03.csv`.

Primera revisión: 2026-11-03, solo investigación de escritorio. Los sitios de las marcas no se pudieron abrir por la política de red del entorno; los datos vienen de los extractos que devolvió el buscador. Por eso ninguna marca queda como `verificada` todavía: «por verificar (encontrada)» significa que hay fuentes públicas de que existe y vende en Bogotá, pero falta confirmarlo abriendo la página o en campo.

Tipos: directo (natural cocido u horneado) · BARF y precocido · concentrado premium · alternativa casera. Se agrega «concentrado estándar (referencia)» para las marcas masivas que sirven de comparación.

Marcas registradas: 45.

| ID | Marca | Tipo | Origen | Formatos y conservación | Dónde se consigue | Zonas de Bogotá | Estado | Fuentes | Última revisión |
|---|---|---|---|---|---|---|---|---|---|
| C01 | Pixie | directo | Bogotá (Pixie S.A.S., 2014) | Porciones húmedas horneadas de 200 g a 3,5 kg; congelado. Línea gatos, tortas y galletas | Rappi, Puppis, Agrocampo, Kanu Pet, Animals Veterinaria; más de 700 puntos (D) | Toda la ciudad por apps y retailers (E) | por verificar (encontrada) | agrocampo.com.co, puppis.com.co, rappi.com.co, animalsveterinaria.com, elespectador.com | 2026-11-03 |
| C02 | Kanuto | directo | Medellín | Porciones horneadas de 500 g (pollo, res, pescado) y kéfir; congelado al vacío | Web propia, Instagram; despacha a todo Colombia (D) | desconocido | por verificar (encontrada) | kanuto.com.co, instagram.com/kanuto___ | 2026-11-03 |
| C03 | VITA Alimento Vital | directo | Bogotá y Medellín (plantas) | Lingotes horneados de 200 g en paquetes de 2,4 y 5 kg; refrigerado 10 días o congelado 6 meses (D) | Web propia con domicilio; recogida en planta (D) | Bogotá en 24 h; municipios a 40 km lunes, miércoles y viernes (D) | por verificar (encontrada) | vitaalimentovital.com, bluradio.com | 2026-11-03 |
| C04 | Kanu Pet · Nativo | directo (Nativo Fresh) y concentrado premium (Nativo Oven-Baked) | Marca propia del retailer Kanu Pet | Nativo Fresh: porciones cocidas de 500 g (perros) y 175 g (gatos), congelado. Nativo Oven-Baked: croqueta horneada seca | kanu.pet, Kanu Aliados, Addi | Bogotá y Medellín (D) | por verificar (encontrada) | kanu.pet, kanualiados.com, marketplace.addi.com | 2026-11-03 |
| C05 | Honesto | directo | desconocido | «Dieta BARF horneada» de 500 g y BARF crudo para gatos; congelado | Web propia | Entrega en Bogotá, Medellín y Cali (D) | por verificar (encontrada) | tiendahonesto.com | 2026-11-03 |
| C06 | Bigdog (Dogsy Pet Food) | directo | Bogotá (Dogsy, 2016) | Dieta cocida al vapor en paquetes de 5, 10 y 15 kg (500 g por unidad); BARF; Dogsy Cat 250 g; helados. Congelado | Web propia; vehículos refrigerados en Bogotá y Medellín (D) | Bogotá; envío 10.000 (D) | por verificar (encontrada) | dogsy.com.co, bogota.dogsy.com.co, agronegocios.co | 2026-11-03 |
| C07 | Bocado | BARF y precocido | Bogotá | Cajas de 4 kg (16 × 250 g): 1 receta cocida y 4 crudas; congelado a −18 °C hasta 12 meses (D) | Web propia | Bogotá; envíos nacionales (D) | por verificar (encontrada) | bocadopetfood.com | 2026-11-03 |
| C08 | Barf y Alimento | directo | desconocido | Cocido personalizado de 2 kg y BARF a medida | Web propia | desconocido | por verificar (encontrada) | barfyalimento.com | 2026-11-03 |
| C09 | Dogo (Gabrica) | directo | desconocido (Gabrica S.A.S.) | Albóndigas cocidas al vapor de 50, 150 y 500 g; más de 65 % de humedad; ambiente, refrigerar al abrir (D). Lanzado en 2025 | Ceba, Lares, Agroventas, Animal Center, Petit Paws | Animal Center y Ceba entregan en Bogotá (D) | por verificar (encontrada) | ceba.com.co, animalcenter.pet, agroventas.co, petitpaws.com.co, americaretail-malls.com | 2026-11-03 |
| C10 | KIKO Holistic | directo | Colombia | Húmedo natural en pouch de 400 g; snacks deshidratados y liofilizados | Farmatodo | Nacional, entrega 4–5 días (D) | por verificar (encontrada) | farmatodo.com.co | 2026-11-03 |
| C11 | Masvital | directo | desconocido | Alimento natural para perros y gatos | Web propia con domicilio | Bogotá, Cali, Bucaramanga (D) | por verificar (encontrada) | masvital.pet | 2026-11-03 |
| C12 | Hello Dog Colombia | directo | Bogotá | Comida fresca y natural para perros | Web propia con domicilio | Todo Bogotá (D) | por verificar (encontrada) | hellodogcolombia.com | 2026-11-03 |
| C13 | Snouts | BARF y precocido | Medellín | Dieta natural cruda congelada; snacks | Web propia | Medellín, Bogotá, Cali y nacional (D) | por verificar (encontrada) | snouts.com.co, americaretail-malls.com | 2026-11-03 |
| C14 | Pet Gourmet | directo | Colombia | Panadería canina y alimento natural; primera reconocida por el ICA como productora de alimentos para animales en 2013 (Agronegocios) | Tiendas propias y comercio electrónico | desconocido | por verificar (encontrada) | agronegocios.co, semana.com, petfoodindustry.com | 2026-11-03 |
| C15 | Petlikatessen | directo | Bogotá | Alimento natural, café y panadería canina | Local propio | desconocido | por verificar (encontrada) | gust.com | 2026-11-03 |
| C16 | Ecocat (Dogtoo y Biodieta) | directo (Dogtoo) y BARF y precocido (Biodieta) | desconocido | Dogtoo: húmedo natural de 250 a 1.000 g. Biodieta: crudo de ~1 kg para gatos | Web propia | desconocido | por verificar (encontrada) | ecocat.com.co | 2026-11-03 |
| C17 | GRUY | BARF y precocido | Bogotá | BARF de 125 y 250 g; congelado. Declara licencia ICA (D) | Web propia | Bogotá (D) | por verificar (encontrada) | gruy.com.co | 2026-11-03 |
| C18 | Whole Barf | BARF y precocido | desconocido | BARF crudo con 70 % de humedad (D) | Puppis | Bogotá, Medellín, Barranquilla (D) | por verificar (encontrada) | puppis.com.co, eltiempo.com (contenido comercial) | 2026-11-03 |
| C19 | Barf Orígenes | BARF y precocido | desconocido | Menús crudos congelados para perros y gatos | Laika | Bogotá (E) | por verificar (encontrada) | laika.com.co | 2026-11-03 |
| C20 | Peluditos Barf | BARF y precocido | Bogotá | BARF crudo; gatos 100 g | Web propia, Agrocampo | Bogotá (D) | por verificar (encontrada) | peluditosbarf.com.co, agrocampo.com.co | 2026-11-03 |
| C21 | Fortiz Pets | BARF y precocido | Bogotá | BARF por libra, mínimo 6 libras | Sitio Wix | Bogotá; envío 3.000–5.000 (D) | por verificar (encontrada) | fortizpets.wixsite.com | 2026-11-03 |
| C22 | Nutrihuellas Barf | BARF y precocido | Bogotá | BARF crudo | Web propia | Solo Bogotá (D) | por verificar (encontrada) | documento de preguntas frecuentes de la tienda | 2026-11-03 |
| C23 | Pet&Co BARF | BARF y precocido | Bogotá | BARF crudo; declara registro ICA (D) | Web propia | Bogotá | por verificar (encontrada) | petandcobarf.com | 2026-11-03 |
| C24 | Mr. Barf | BARF y precocido | Cali | BARF para perros y gatos | Web propia | desconocido | por verificar | gust.com, mrbarf.com | 2026-11-03 |
| C25 | Pet Natural Food | BARF y precocido | desconocido | BARF | desconocido | desconocido | por verificar | agronegocios.co | 2026-11-03 |
| C26 | Chunky Menú Natural (Italcol) | BARF y precocido | Colombia (Italcol) | BARF crudo en cajas de 10 × 300 g; agotado al consultar | Alimento Animal | desconocido | por verificar | alimentoanimal.com.co | 2026-11-03 |
| C27 | Corleone BARF Premium | BARF y precocido | desconocido | BARF | Facebook | desconocido | por verificar | facebook.com | 2026-11-03 |
| C28 | BeBarf | BARF y precocido | desconocido | Menú mixto de 1 kg (D) | Web propia | desconocido | por verificar | bebarf.com | 2026-11-03 |
| C29 | Nupec | concentrado premium | México (importado) | Croqueta; seco | Farmatodo, Falabella | Nacional | por verificar (encontrada) | farmatodo.com.co, falabella.com.co | 2026-11-03 |
| C30 | Agility Gold | concentrado premium | Colombia | Croqueta; seco | Falabella y otros | Nacional | por verificar (encontrada) | falabella.com.co, farmatodo.com.co | 2026-11-03 |
| C31 | Hill's Science Diet | concentrado premium | Importado | Croqueta; seco | Falabella y otros | Nacional | por verificar (encontrada) | las2orillas.co | 2026-11-03 |
| C32 | Pro Plan | concentrado premium | Importado (Purina) | Croqueta; seco | Farmatodo y otros | Nacional | por verificar | farmatodo.com.co (sin precio visible) | 2026-11-03 |
| C33 | Royal Canin | concentrado premium | Importado | Croqueta; seco | Mercado Libre y otros | Nacional | por verificar | mercadolibre.com.co (sin precio visible) | 2026-11-03 |
| C34 | Taste of the Wild | concentrado premium | Importado | Croqueta; seco | desconocido | desconocido | por verificar | Sin precio en Colombia en la búsqueda | 2026-11-03 |
| C35 | Acana y Orijen | concentrado premium | Importado | Croqueta; seco | desconocido | desconocido | por verificar | Sin precio en Colombia en la búsqueda | 2026-11-03 |
| C36 | Dog Chow | concentrado estándar (referencia) | Purina | Croqueta; seco | Todos los canales | Nacional | por verificar (encontrada) | falabella.com.co, homecenter.com.co, farmatodo.com.co | 2026-11-03 |
| C37 | Chunky | concentrado estándar (referencia) | Colombia (Italcol) | Croqueta; seco | Todos los canales | Nacional | por verificar (encontrada) | falabella.com.co, alkosto.com | 2026-11-03 |
| C38 | Comida casera y carne de carnicería | alternativa casera | desconocido | Cocinar en casa o comprar carne y vísceras | Carnicerías y plazas de mercado | desconocido | por verificar | Sin levantamiento todavía | 2026-11-03 |
| C39 | Vital Doggy | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |
| C40 | Rawf | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |
| C41 | KENKO Barf | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |
| C42 | 4DOGS | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |
| C43 | Barftender | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |
| C44 | Santo Barf | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |
| C45 | Bitute | BARF y precocido | desconocido | desconocido | desconocido | desconocido | por verificar | Candidata de `AGENTS.md`; sin resultados en búsqueda web del 2026-11-03 | 2026-11-03 |

Notas:

- C09: en dogorealfood.com aparece un «Dogo Res x 800 g BARF» congelado, vendido en Cali y Bogotá, con licencia ICA. No se sabe si es la misma marca que el Dogo de Gabrica (V).
- C12: un cliente del registro de ventas 2026 tiene un nombre parecido. Confirmar internamente si es la misma empresa y si revende o reetiqueta producto de Canívoros (H).

Estado: `por verificar`, `verificada` (existe y se vende en Bogotá), `descartada` (con el motivo en Fuentes) o `No verificado` (la página pide login o bloquea). Los IDs no se reutilizan.

## 4. Tabla comparativa

Costo diario: `desconocido` para todas las marcas, porque no se encontraron raciones publicadas para perros de 10 y 25 kg. Reseñas: no se levantaron todavía. El resto de las marcas está en la sección 3.

| ID | Marca | Tipo | Formato y conservación | Precio/kg (filas E) | Costo diario 10 kg | Costo diario 25 kg | Dónde se consigue | Entrega | Promesa | Reseñas |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Pixie | directo | Porción húmeda horneada; congelado | 21.250–31.590 (perros); 37.000 (gatos) | desconocido | desconocido | Rappi, Puppis, Agrocampo, Kanu Pet, Animals Veterinaria | Por retailer; Puppis gratis desde 160.000 (E) | Sin conservantes, colorantes, azúcares ni sales añadidas (D) | sin levantar |
| C02 | Kanuto | directo | Porción horneada; congelado al vacío | 24.400–29.000 | desconocido | desconocido | Web propia, Instagram | Despacha a todo Colombia desde Medellín (D) | Natural, horneado, grado humano, para perros exigentes o con estómago sensible (D) | sin levantar |
| C03 | VITA Alimento Vital | directo | Lingote horneado de 200 g; refrigerado o congelado | Solo filas (V): 27.960–31.125 | desconocido | desconocido | Web propia; recogida en planta | 24 h en Bogotá; 39.900 por 2,4 kg (D, V) | Natural, sin gluten, horneado, completo y balanceado; no crudo (D) | sin levantar |
| C04 | Kanu Pet · Nativo | directo y concentrado premium | Porción cocida congelada; croqueta horneada seca | 31.800–35.800 (Fresh); 59.950 (Oven-Baked); 68.000 (gato) | desconocido | desconocido | kanu.pet, Kanu Aliados | Bogotá y Medellín (D) | 100 % comida real (D) | sin levantar |
| C06 | Bigdog (Dogsy) | directo | Porción cocida al vapor; congelado | Solo fila (V): 14.250 con descuento | desconocido | desconocido | Web propia | Solo Bogotá; 10.000; 1–2 días (D, V) | Natural, sin maíz, trigo ni soya (D) | sin levantar |
| C07 | Bocado | BARF y precocido | Porción de 250 g, 1 cocida y 4 crudas; congelado | 20.000 | desconocido | desconocido | Web propia | Bogotá y nacional (D) | Lista para servir; hasta 12 meses a −18 °C (D) | sin levantar |
| C09 | Dogo (Gabrica) | directo | Albóndiga cocida al vapor; ambiente | 43.600–52.800 (materia seca estimada 124.571–150.857) | desconocido | desconocido | Ceba, Animal Center, Agroventas, Lares | Ceba entrega en Bogotá (D) | Sin conservantes ni colorantes artificiales (D) | sin levantar |
| C17 | GRUY | BARF y precocido | Porción cruda de 125–250 g; congelado | 20.000–24.000 | desconocido | desconocido | Web propia | Bogotá (D) | Licencia ICA (D) | sin levantar |
| C19 | Barf Orígenes | BARF y precocido | Porción cruda; congelado | 38.400 (gatos) | desconocido | desconocido | Laika | Bogotá (E) | desconocido | sin levantar |
| C29 | Nupec | concentrado premium | Croqueta; seco | 38.180–41.849 regular; 33.479 promo | desconocido | desconocido | Farmatodo, Falabella | Nacional, 4–5 días (D) | desconocido | sin levantar |
| C30 | Agility Gold | concentrado premium | Croqueta; seco | 29.749 regular; 23.799 promo | desconocido | desconocido | Falabella | Nacional | desconocido | sin levantar |

Comparar por kg entre grupos tiene un límite: un concentrado seco tiene poca humedad y los naturales declaran mucha (Dogo más del 65 %, Whole Barf 70 %) (D). Un kilo de cada uno no alimenta lo mismo. La comparación justa es el costo diario con ración publicada.

### Precios y cuentas

Salida de `python3 .claude/skills/analisis-competencia/scripts/competencia.py precios competencia/competencia-2026-11-03.csv --hoy 2026-11-03 --libra-g 453.6` (filas `registro=precio`). Los números de línea se refieren al CSV del día. Se usó `--libra-g 453.6` porque las dos filas en libras son de una bolsa importada (Hill's, 4,5 lb) y de Fortiz Pets; ambas están marcadas (V) y quedan fuera de la comparación. Ninguna fila de Canívoros entra en el archivo.

#### Precio por kg (de menor a mayor)

| # | Marca | Producto | Tipo | Peso | Precio regular | Precio/kg | Precio/kg promo | Precio/kg materia seca* | Canal · vendedor | Fecha | Fuente | Evidencia | Avisos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C07 · Bocado | Caja Res y Pez (16 x 250 g) | BARF y precocido | 4 kg | 80.000 | 20.000 | — | — | web propia · Bocado | 2026-11-03 | bocadopetfood.com | (E) | — |
| 2 | C17 · GRUY | BARF res, pollo, hígado y zanahoria | BARF y precocido | 250 g | 5.000 | 20.000 | — | — | web propia · GRUY | 2026-11-03 | gruy.com.co | (E) | — |
| 3 | C01 · Pixie | Dieta horneada pollo | directo | 2 kg | 42.500 | 21.250 | — | — | tienda en línea · Puppis | 2026-11-03 | puppis.com.co | (E) | — |
| 4 | C01 · Pixie | Comida para perros pollo al horno | directo | 500 g | 11.815 | 23.630 | — | — | tienda en línea · Agrocampo | 2026-11-03 | agrocampo.com.co | (E) | — |
| 5 | C17 · GRUY | BARF res, pollo, hígado y zanahoria | BARF y precocido | 125 g | 3.000 | 24.000 | — | — | web propia · GRUY | 2026-11-03 | gruy.com.co | (E) | — |
| 6 | C02 · Kanuto | Kanuto pollo | directo | 500 g | 12.200 | 24.400 | — | — | web propia · Kanuto | 2026-11-03 | kanuto.com.co | (E) | — |
| 7 | C02 · Kanuto | Kanuto res | directo | 500 g | 12.900 | 25.800 | — | — | web propia · Kanuto | 2026-11-03 | kanuto.com.co | (E) | — |
| 8 | C01 · Pixie | Comida para perros carne baja en grasa | directo | 500 g | 12.960 | 25.920 | 23.328 | — | tienda en línea · Agrocampo | 2026-11-03 | agrocampo.com.co | (E) | — |
| 9 | C02 · Kanuto | Kanuto pescado | directo | 500 g | 14.500 | 29.000 | — | — | web propia · Kanuto | 2026-11-03 | kanuto.com.co | (E) | — |
| 10 | C01 · Pixie | 7 dietas sabores surtidos | directo | 3,5 kg | 102.604 | 29.315 | 26.384 | — | tienda en línea · Agrocampo | 2026-11-03 | agrocampo.com.co | (E) | — |
| 11 | C30 · Agility Gold | Grandes adultos | concentrado premium | 15 kg | 446.237 | 29.749 | 23.799 | — | marketplace · Provipets (Falabella) | 2026-11-03 | falabella.com.co | (E) | — |
| 12 | C01 · Pixie | Comida monoproteica trucha al horno | directo | 500 g | 15.386 | 30.772 | — | — | tienda en línea · Agrocampo | 2026-11-03 | agrocampo.com.co | (E) | — |
| 13 | C01 · Pixie | Comida para perros cordero al horno | directo | 500 g | 15.795 | 31.590 | — | — | tienda en línea · Agrocampo | 2026-11-03 | agrocampo.com.co | (E) | — |
| 14 | C04 · Kanu Pet · Nativo | Nativo Fresh pollo y quinoa | directo | 500 g | 15.900 | 31.800 | — | — | web propia del retailer · Kanu Pet | 2026-11-03 | kanu.pet | (E) | — |
| 15 | C04 · Kanu Pet · Nativo | Nativo Fresh res, hígado y remolacha | directo | 500 g | 16.900 | 33.800 | — | — | marketplace · Addi / Kanu Aliados | 2026-11-03 | marketplace.addi.com | (E) | — |
| 16 | C04 · Kanu Pet · Nativo | Nativo Fresh salmón y wakame | directo | 500 g | 17.900 | 35.800 | — | — | web propia del retailer · Kanu Pet | 2026-11-03 | kanu.pet | (E) | — |
| 17 | C01 · Pixie | Dieta horneada gatito pescado | directo | 200 g | 7.400 | 37.000 | — | — | app de domicilios · Rappi | 2026-11-03 | rappi.com.co | (E) | — |
| 18 | C29 · Nupec | Nupec mature raza grande | concentrado premium | 15 kg | 572.700 | 38.180 | — | — | droguería en línea · Farmatodo | 2026-11-03 | farmatodo.com.co | (E) | — |
| 19 | C19 · Barf Orígenes | Menú gatos | BARF y precocido | 200 g | 7.680 | 38.400 | — | — | tienda en línea · Laika | 2026-11-03 | laika.com.co | (E) | — |
| 20 | C29 · Nupec | Nupec cachorro | concentrado premium | 15 kg | 627.740 | 41.849 | 33.479 | — | marketplace · Provipets (Falabella) | 2026-11-03 | falabella.com.co | (E) | — |
| 21 | C09 · Dogo (Gabrica) | Dogo albóndigas de res | directo | 500 g | 21.800 | 43.600 | — | 124.571 | tienda en línea · Ceba | 2026-11-03 | ceba.com.co | (E) | — |
| 22 | C09 · Dogo (Gabrica) | Dogo comida real pollo | directo | 500 g | 22.900 | 45.800 | — | 130.857 | tienda en línea · Agroventas | 2026-11-03 | agroventas.co | (E) | — |
| 23 | C09 · Dogo (Gabrica) | Dogo albóndigas de cerdo | directo | 500 g | 26.400 | 52.800 | — | 150.857 | petshop · Animal Center | 2026-11-03 | animalcenter.pet | (E) | — |
| 24 | C04 · Kanu Pet · Nativo | Nativo Oven-Baked K-booster carne, cerdo y salmón | concentrado premium | 2 kg | 119.900 | 59.950 | — | — | web propia del retailer · Kanu Pet | 2026-11-03 | kanu.pet | (E) | — |
| 25 | C04 · Kanu Pet · Nativo | Nativo Fresh pollo para gato | directo | 175 g | 11.900 | 68.000 | — | — | web propia del retailer · Kanu Pet | 2026-11-03 | kanu.pet | (E) | — |

\* Materia seca calculada con la humedad declarada (normalmente un máximo de etiqueta): es una estimación para comparar productos de distinta humedad, no un costo de alimentación.

##### Filas fuera de la comparación

Les falta peso, precio, fecha o fuente, están marcadas (V) o (H), o tienen un dato sospechoso. Complétalas o corrígelas y vuelve a correr el script; no se rellenan con supuestos.

| Línea | Marca | Producto | Peso | Precio regular | Motivo |
|---|---|---|---|---|---|
| 57 | C03 · VITA Alimento Vital | VITA Sensitive Salmón (12 lingotes de 200 g) | 2,4 kg | 73.500 | marcado (V): dato dudoso o sin fecha |
| 58 | C03 · VITA Alimento Vital | VITA Sensitive Salmón (25 lingotes de 200 g) | 5 kg | 139.800 | marcado (V): dato dudoso o sin fecha |
| 59 | C03 · VITA Alimento Vital | VITA Sensitive Pavo (12 lingotes de 200 g) | 2,4 kg | 74.700 | marcado (V): dato dudoso o sin fecha |
| 65 | C05 · Honesto | Dieta BARF horneada pollo con verduras | 500 g | 35.000 | marcado (V): dato dudoso o sin fecha |
| 66 | C06 · Bigdog (Dogsy Pet Food) | Bigdog Res Mix dieta cocida (10 x 500 g) | 5 kg | desconocido | marcado (V): dato dudoso o sin fecha; sin precio regular |
| 67 | C06 · Bigdog (Dogsy Pet Food) | Dogsy Cat dieta cocida | 250 g | 6.000 | marcado (V): dato dudoso o sin fecha |
| 69 | C08 · Barf y Alimento | Alimento cocido perros y gatos | 2 kg | 27.360 | marcado (V): dato dudoso o sin fecha |
| 73 | C10 · KIKO Holistic | Húmedo natural monoproteico cerdo (pouch) | 400 g | 17.000 | marcado (V): dato dudoso o sin fecha |
| 77 | C20 · Peluditos Barf | Barf Cat Gourmet | 100 g | 4.000 | marcado (V): dato dudoso o sin fecha |
| 78 | C21 · Fortiz Pets | Dieta BARF | 453,6 g | 2.000 | marcado (V): dato dudoso o sin fecha |
| 79 | C16 · Ecocat | Biodieta crudo original gatos (unas 32 porciones) | 1 kg | desconocido | marcado (V): dato dudoso o sin fecha; sin precio regular |
| 83 | C31 · Hill's Science Diet | Small Paws adulto raza mini | 2,04 kg | desconocido | marcado (V): dato dudoso o sin fecha; sin precio regular |
| 84 | C37 · Chunky | Pollo adultos | 9 kg | desconocido | sin precio regular |
| 85 | C36 · Dog Chow | Triple proteína adultos | 8 kg | desconocido | sin precio regular |
| 86 | C36 · Dog Chow | Adultos medianos y grandes | 22,7 kg | 358.850 | marcado (V): dato dudoso o sin fecha |

#### Resumen por tipo

| Tipo | n | Mínimo/kg | Mediana/kg | Máximo/kg |
|---|---|---|---|---|
| BARF y precocido | 4 | 20.000 | 22.000 | 38.400 |
| directo | 17 | 21.250 | 31.590 | 68.000 |
| concentrado premium | 4 | 29.749 | 40.015 | 59.950 |

Con pocas filas por tipo, la mediana describe la muestra levantada, no el mercado.

#### Costo diario (solo con ración documentada)

No hay raciones documentadas con fuente y perfil de mascota: no se calcula costo diario. El precio por kg no equivale al costo de alimentar, porque cada producto tiene su propia ración.

#### Cuentas

- C07 · Bocado · Caja Res y Pez (16 x 250 g): 80.000 ÷ (4.000 g ÷ 1.000) = 20.000/kg
- C17 · GRUY · BARF res, pollo, hígado y zanahoria: 5.000 ÷ (250 g ÷ 1.000) = 20.000/kg
- C01 · Pixie · Dieta horneada pollo: 42.500 ÷ (2.000 g ÷ 1.000) = 21.250/kg
- C01 · Pixie · Comida para perros pollo al horno: 11.815 ÷ (500 g ÷ 1.000) = 23.630/kg
- C17 · GRUY · BARF res, pollo, hígado y zanahoria: 3.000 ÷ (125 g ÷ 1.000) = 24.000/kg
- C02 · Kanuto · Kanuto pollo: 12.200 ÷ (500 g ÷ 1.000) = 24.400/kg
- C02 · Kanuto · Kanuto res: 12.900 ÷ (500 g ÷ 1.000) = 25.800/kg
- C01 · Pixie · Comida para perros carne baja en grasa: 12.960 ÷ (500 g ÷ 1.000) = 25.920/kg; promo 11.664 ÷ (500 g ÷ 1.000) = 23.328/kg
- C02 · Kanuto · Kanuto pescado: 14.500 ÷ (500 g ÷ 1.000) = 29.000/kg
- C01 · Pixie · 7 dietas sabores surtidos: 102.604 ÷ (3.500 g ÷ 1.000) = 29.315/kg; promo 92.344 ÷ (3.500 g ÷ 1.000) = 26.384/kg
- C30 · Agility Gold · Grandes adultos: 446.237 ÷ (15.000 g ÷ 1.000) = 29.749/kg; promo 356.989 ÷ (15.000 g ÷ 1.000) = 23.799/kg
- C01 · Pixie · Comida monoproteica trucha al horno: 15.386 ÷ (500 g ÷ 1.000) = 30.772/kg
- C01 · Pixie · Comida para perros cordero al horno: 15.795 ÷ (500 g ÷ 1.000) = 31.590/kg
- C04 · Kanu Pet · Nativo · Nativo Fresh pollo y quinoa: 15.900 ÷ (500 g ÷ 1.000) = 31.800/kg
- C04 · Kanu Pet · Nativo · Nativo Fresh res, hígado y remolacha: 16.900 ÷ (500 g ÷ 1.000) = 33.800/kg
- C04 · Kanu Pet · Nativo · Nativo Fresh salmón y wakame: 17.900 ÷ (500 g ÷ 1.000) = 35.800/kg
- C01 · Pixie · Dieta horneada gatito pescado: 7.400 ÷ (200 g ÷ 1.000) = 37.000/kg
- C29 · Nupec · Nupec mature raza grande: 572.700 ÷ (15.000 g ÷ 1.000) = 38.180/kg
- C19 · Barf Orígenes · Menú gatos: 7.680 ÷ (200 g ÷ 1.000) = 38.400/kg
- C29 · Nupec · Nupec cachorro: 627.740 ÷ (15.000 g ÷ 1.000) = 41.849/kg; promo 502.192 ÷ (15.000 g ÷ 1.000) = 33.479/kg
- C09 · Dogo (Gabrica) · Dogo albóndigas de res: 21.800 ÷ (500 g ÷ 1.000) = 43.600/kg; materia seca 43.600 ÷ (1 − 65,0 %) = 124.571/kg
- C09 · Dogo (Gabrica) · Dogo comida real pollo: 22.900 ÷ (500 g ÷ 1.000) = 45.800/kg; materia seca 45.800 ÷ (1 − 65,0 %) = 130.857/kg
- C09 · Dogo (Gabrica) · Dogo albóndigas de cerdo: 26.400 ÷ (500 g ÷ 1.000) = 52.800/kg; materia seca 52.800 ÷ (1 − 65,0 %) = 150.857/kg
- C04 · Kanu Pet · Nativo · Nativo Oven-Baked K-booster carne, cerdo y salmón: 119.900 ÷ (2.000 g ÷ 1.000) = 59.950/kg
- C04 · Kanu Pet · Nativo · Nativo Fresh pollo para gato: 11.900 ÷ (175 g ÷ 1.000) = 68.000/kg

Filas sin precio regular: Chunky 9 kg (133.956) y Dog Chow Triple Proteína 8 kg (143.271) solo muestran el precio con descuento, unos 14.900 y 17.900 COP/kg; se dejan como referencia (V) del concentrado estándar.

## 5. Mensajes

| Marca | Promesa principal | Prueba que ofrece | Tipo de afirmación | Evidencia |
|---|---|---|---|---|
| Pixie | Sin conservantes, colorantes, azúcares ni sales añadidas | Escala y presencia en retail | Ingredientes | (D) |
| Kanuto | Natural, horneado, grado humano, para perros exigentes o con estómago sensible | Empacado al vacío y congelado | Proceso y beneficio digestivo | (D) |
| VITA | Natural, sin gluten, horneado, completo y balanceado | Contenido de blog sobre riesgos de la dieta BARF | Proceso, balance nutricional, seguridad frente a lo crudo | (D) |
| Kanu Pet Nativo | 100 % comida real | Marca del retailer | Ingredientes | (D) |
| Dogo | Sin conservantes ni colorantes artificiales; el vapor conserva los nutrientes | desconocido | Ingredientes y proceso | (D) |
| Bocado | Porciones listas para servir | Caja de 16 porciones de 250 g | Comodidad | (D) |
| GRUY | Carne magra de res, pollo, hígado y zanahoria | Licencia ICA | Ingredientes y respaldo regulatorio | (D) |
| Whole Barf | Dos proteínas animales en cada receta | desconocido | Ingredientes | (D) |

**Promesas que repiten todos:** natural, carne real, sin conservantes ni aditivos artificiales. Las horneadas suman el proceso de horneado; VITA y Canívoros comparten el «no crudo».

**Promesas que nadie usa en lo revisado (H):** origen en perros de competencia o de alto rendimiento; formato hamburguesa o chorizo; economía para perros grandes o criadores. La muestra es pequeña y no se revisaron redes ni anuncios, así que esto es una hipótesis.

## 6. Cobertura en Bogotá

No se levantó cobertura por localidad. Lo observado es por canal:

| Zona | Marcas presentes | Entrega disponible | Vacíos |
|---|---|---|---|
| Toda Bogotá por domicilio | Pixie (Rappi, Puppis, Agrocampo), Kanu Pet Nativo, VITA, Bigdog, Bocado, GRUY, Barf Orígenes (Laika), Hello Dog, Masvital (D, E) | Sí, con cadena de frío; envío gratis desde 150.000–160.000 en retailers (E) | desconocido |
| Calle 73 # 20-65 (Animals Veterinaria) | Pixie (E) | Bogotá y Sabana, gratis desde 150.000 (E) | desconocido |
| Municipios a 40 km (Chía, Zipaquirá, Soacha) | VITA (D) | Lunes, miércoles y viernes (D) | desconocido |

## 7. Gatos (Gatívoros)

| Marca | Tipo | Presentación y precio | COP/kg | Evidencia |
|---|---|---|---:|---|
| Pixie gatito pescado | Horneado, congelado | 200 g desde 7.400 | 37.000 | (E) |
| Barf Orígenes | BARF, congelado | 200 g a 7.680 | 38.400 | (E) |
| Kanu Pet Nativo Fresh gato | Cocido, congelado | 175 g a 11.900 | 68.000 | (E) |
| Dogsy Cat | Cocido al vapor, congelado | 250 g a 6.000 | 24.000 | (V) |
| Peluditos Barf Cat Gourmet | BARF, congelado | 100 g a 4.000 | 40.000 | (V) |

Las marcas para gatos usan porciones de 100 a 250 g (E). Coincide con lo que dice la responsable de Canívoros en `erp.md`: 500 g es mucho para un gato y el producto pierde frescura al abrirlo. Apoya probar una presentación de 200 g (BL-023, BL-026) (H).

## 8. Recomendaciones y pruebas

| Hallazgo (evidencia) | Hipótesis | Prueba | Métrica | Criterio de decisión | Límite de gasto o tiempo |
|---|---|---|---|---|---|
| Cinco marcas usan «horneado» (E, D) | Un diferencial distinto al horneado convierte mejor (H) | Agregar variantes de mensaje en BL-020: «origen en perros de competencia» y «formato hamburguesa» | Contactos calificados que compran, por variante | Elegir la variante con más compras pagadas; si hay pocas compras, tratar como indicio | Tope acordado con Andrés; 4 semanas |
| Pixie está en las tiendas especializadas (E) | Las tiendas con congelador y clientes naturales aceptan un segundo natural si deja margen (H) | En BL-012, priorizar 10 tiendas que vendan Pixie o BARF congelado | Tiendas que hacen pedido inicial; reposición a 30 días | Seguir con el canal si al menos una parte repone sin descuento; umbral en pesos a definir con Andrés | Pedido inicial controlado; 6 semanas |
| Piso de precio natural de unos 20.000 COP/kg (E) | Conocer la posición propia cambia la estrategia de precio (H) | Confirmar precios de Canívoros (BL-005) y correr el script con `--propia` | Posición por kg dentro de cada grupo | Decidir precio y presentación con la posición confirmada | Sin gasto; 1 semana |
| Cadena de frío y envío caro en toda la categoría (E, D) | Una entrega programada por zona reduce el costo por pedido (H) | Entregas programadas en una microzona (BL-014) | Costo de entrega por kg; recompra a 30 días | Ampliar si la contribución después de entrega es positiva | Tope acordado con Andrés; 4 semanas |
| Porciones de gatos de 100–250 g (E) | Una presentación de 200 g de Gatívoros reduce el desperdicio y facilita la primera compra (H) | Presentación de 200 g en 3–5 veterinarias (BL-026) | Compras y recompra por veterinaria | Mantener si hay recompra con contribución positiva | Lote pequeño; 6 semanas |

Registrar hipótesis y criterios antes de lanzar cada prueba (BL-044).

## 9. Qué no se pudo verificar

| Dato | Por qué importa | Cómo obtenerlo | Necesita aprobación de Andrés |
|---|---|---|---|
| Contenido real de todas las páginas citadas | Los datos vienen de extractos del buscador | Abrir cada URL desde un entorno con acceso a esos dominios o a mano | No |
| Precios y unidades confirmados de Canívoros | Sin ellos no se puede ubicar a Canívoros en la comparación | BL-005 | No |
| Conservación y vida útil de Canívoros | Define si compite con los congelados o con los estables | Ficha técnica de la empresa | No |
| Raciones de cada marca para perros de 10 y 25 kg | Sin raciones no hay costo diario | Etiquetas, fichas técnicas, compras de prueba | Sí, si se compra |
| Reseñas (Google Maps, Mercado Libre, redes) | Qué valoran y critican los compradores | Agregar filas `registro=resena` al CSV del día y correr `competencia.py resenas` | No |
| Matriz de perfil competitivo | Necesita pesos que salgan de los compradores | Entrevistas BL-006 y BL-007; filas `registro=matriz` del CSV del día | No |
| Precios de VITA, Bigdog, Barf y Alimento, Honesto y KIKO | Están marcados (V) y fuera de la comparación | Revisar la página actual | No |
| Compras de prueba de Pixie, Kanuto, VITA, Bigdog, Bocado, Kanu Nativo Fresh y Dogo | Atención, entrega, empaque, etiqueta y ración reales | Protocolo de `references/levantamiento.md` de la skill | Sí |
| Candidatas sin resultados (C39–C45) | Podrían ser competidores relevantes | Buscar en Instagram y Google Maps | No |
| Cobertura por localidad | Alimenta el criterio de competidores de la matriz de microzonas | Google Maps y retailers por zona (BL-014) | No |
| Cliente del registro de ventas con nombre parecido a Hello Dog (C12) | Podría ser a la vez cliente y competidor | Revisión interna | No |

## 10. Qué debe decidir Andrés

- Confirmar precios, unidades y conservación de Canívoros (BL-005) para autorizar la comparación con la marca propia.
- Aprobar o no las compras de prueba de la sección 8 y su presupuesto.
- Elegir las 8–12 alternativas que se seguirán cada mes. Propuesta (H): Pixie, Kanuto, VITA, Kanu Pet Nativo, Bigdog, Bocado, Dogo, GRUY, Nupec, Agility Gold y una alternativa casera.
- Decidir si se habilita el acceso a los dominios de las marcas en el entorno de trabajo o si la verificación de las páginas se hace a mano.
- Definir si Kanu Pet se trata como canal, como competidor o como ambos.

## 11. Fuentes

Todas consultadas el 2026-11-03 mediante el buscador. Estado «No verificado»: la página no se pudo abrir desde este entorno. Las URL de cada precio están en `competencia-2026-11-03.csv`.

| # | Fuente (URL o descripción) | Fecha de consulta | Estado |
|---|---|---|---|
| 1 | https://www.elespectador.com/economia/emprendimiento-y-liderazgo/esta-es-la-marca-colombiana-que-promueve-la-nutricion-natural-para-mascotas/ | 2026-11-03 | No verificado |
| 2 | https://www.agronegocios.co/mascotas/conozca-a-pixie-el-alimento-natural-horneado-para-su-perro-2854678 | 2026-11-03 | No verificado |
| 3 | https://americaretail-malls.com/retail-especializado/mascotas/pixie-la-marca-colombiana-que-revoluciona-la-alimentacion-natural-de-mascotas/ | 2026-11-03 | No verificado |
| 4 | https://www.agronegocios.co/mascotas/el-mercado-de-los-alimentos-naturales-para-las-mascotas-un-sector-que-esta-creciendo-4142605 | 2026-11-03 | No verificado |
| 5 | https://www.bluradio.com/sociedad/esta-marca-de-comida-es-para-todos-los-perros-alejandra-giraldo-cofundadora-de-vita | 2026-11-03 | No verificado |
| 6 | https://vitaalimentovital.com/pages/faq | 2026-11-03 | No verificado |
| 7 | https://www.kanuto.com.co/ | 2026-11-03 | No verificado |
| 8 | https://kanu.pet/collections/alimentos-kanu-pet | 2026-11-03 | No verificado |
| 9 | https://www.rappi.com.co/shopping/pixie | 2026-11-03 | No verificado |
| 10 | https://www.puppis.com.co/alimento-congelado-para-perro-pixie-dieta-horneada-pollo/p | 2026-11-03 | No verificado |
| 11 | https://www.animalsveterinaria.com/alimentos/pixie/361?map=c%2Cb%2CproductClusterIds | 2026-11-03 | No verificado |
| 12 | https://www.agrocampo.com.co/perros/comida/gatsy_program_attack_pixie_basic-farm_max_simba_equilibrio_pedigree_nutriss | 2026-11-03 | No verificado |
| 13 | https://bocadopetfood.com/ | 2026-11-03 | No verificado |
| 14 | https://www.dogsy.com.co/dieta-barf | 2026-11-03 | No verificado |
| 15 | https://www.agronegocios.co/mascotas/dogsy-pet-food-empresa-que-vende-paletas-para-perros-con-registro-ica-desde-3-000-3525986 | 2026-11-03 | No verificado |
| 16 | https://americaretail-malls.com/retail-especializado/mascotas/gabrica-presenta-dogo-el-alimento-natural-para-mascotas-en-albondigas-cocidas-al-vapor/ | 2026-11-03 | No verificado |
| 17 | https://petitpaws.com.co/products/dogo-cerdo | 2026-11-03 | No verificado |
| 18 | https://gruy.com.co/product/barf/ | 2026-11-03 | No verificado |
| 19 | https://www.puppis.com.co/whole-barf | 2026-11-03 | No verificado |
| 20 | https://www.eltiempo.com/contenido-comercial/alimento-whole-barf-para-su-mascota-632506 | 2026-11-03 | No verificado (contenido comercial) |
| 21 | https://snouts.com.co/producto/alimento-a-base-de-pollo-para-perros/ | 2026-11-03 | No verificado |
| 22 | https://www.petandcobarf.com/ | 2026-11-03 | No verificado |
| 23 | https://masvital.pet/ | 2026-11-03 | No verificado |
| 24 | https://hellodogcolombia.com/ | 2026-11-03 | No verificado |
| 25 | https://www.agronegocios.co/mascotas/mayor-energia-entre-ventajas-de-la-barf-3402020 | 2026-11-03 | No verificado |
| 26 | https://www.semana.com/amp/pet-gourmet-es-considerada-la-primera-panaderia-para-perros-en-colombia/218650 | 2026-11-03 | No verificado |
| 27 | https://www.mallyretail.com/actualidad/mall-y-retail-boletin-541-noticia-3 | 2026-11-03 | No verificado |
| 28 | https://www.ica.gov.co/areas/pecuaria/servicios/alimentos-para-animales/listado-fabricantes-registrados.aspx | 2026-11-03 | No verificado (pendiente cruzar con las marcas) |
