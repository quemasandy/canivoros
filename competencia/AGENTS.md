# Playbook de inteligencia competitiva · Canívoros en Bogotá

> Instrucciones para cualquier agente de IA (Claude, ChatGPT, Gemini u otro) que analice la competencia de Canívoros en Bogotá.
> Trabaja como lo haría una agencia de primer nivel: **se analiza la decisión del comprador, no solo el producto del competidor; cada dato tiene fuente y fecha; cada hallazgo termina en una decisión o una prueba.**
> Las reglas comunes del proyecto (evidencia, datos personales, mensajes de marca, Git) están en `../AGENTS.md` y también aplican aquí.
> Última actualización: 2026-11-02.

---

## 0. En 10 líneas

1. Lee `../AGENTS.md`, este archivo y, si existen, los entregables anteriores en `../resultados/competencia/`.
2. Empieza siempre por la **pregunta de negocio** que vas a responder (§1.2) y escríbela en el informe.
3. Define el **conjunto competitivo** por niveles y por segmento de comprador (§3).
4. Recolecta datos públicos con fuente y fecha (§5), con la ficha de §6.
5. Normaliza antes de comparar: precio por kg, costo diario y mismo perfil de perro (§7).
6. Analiza con los marcos de §8: benchmark, matriz de perfil, posicionamiento, mensajes, voz del cliente, cobertura, recorrido de compra.
7. Clasifica la amenaza de cada competidor (§9).
8. Convierte cada hallazgo en implicación, recomendación y prueba medible (§10).
9. **Nunca contactes** competidores ni hagas compras de prueba sin aprobación de Andrés. Solo información pública.
10. Entrega el registro y un informe ejecutivo en `../resultados/competencia/` (§11).

## 1. Misión, preguntas y alcance

### 1.1 Misión

Entender **por qué un comprador de Bogotá elige otra alternativa en lugar de Canívoros, cuánto le cuesta y dónde puede ganar Canívoros**, para decidir con evidencia el precio, las presentaciones, el mensaje, los canales y las zonas.

### 1.2 Preguntas de negocio

Cada análisis responde una o varias de estas preguntas. Escribe cuál en la primera línea del informe.

| # | Pregunta | Decisión que alimenta | Tarea |
|---|---|---|---|
| 1 | ¿Contra quién compite de verdad Canívoros en cada segmento de comprador? | Foco comercial | BL-015 |
| 2 | ¿Qué promete cada alternativa y con qué pruebas? | Mensaje y afirmaciones | BL-016, BL-020 |
| 3 | ¿Cuánto cuesta por kg y por día alimentar a un perro con cada alternativa? | Precio y presentaciones | BL-005, BL-023, BL-025 |
| 4 | ¿Dónde se consigue cada marca en Bogotá y cómo se entrega? | Zonas y canal | BL-014, BL-022 |
| 5 | ¿Qué ofrecen los competidores a tiendas y distribuidores? | Oferta al canal | BL-012 |
| 6 | ¿Qué valoran y qué critican los compradores? | Mensaje, producto, servicio | BL-006, BL-020 |
| 7 | ¿Qué espacios no está atendiendo nadie bien? | Posicionamiento | BL-028 |
| 8 | ¿Qué movimientos de la competencia pueden afectar a Canívoros? | Riesgos | Radar (§8.9) |

### 1.3 Alcance

- **Geografía:** marcas que se venden en Bogotá, aunque se fabriquen en otra ciudad (por ejemplo, Kanuto en Medellín).
- **Especie:** perros primero. Gatos (Gatívoros) en un análisis aparte cuando llegue BL-026.
- **Fuera de alcance:** datos internos no publicados de los competidores; compras de prueba, llamadas o mensajes sin aprobación; información obtenida haciéndose pasar por cliente o distribuidor.

## 2. Canívoros como punto de referencia

Para comparar en igualdad de condiciones. Todo es declaración de la empresa (D) y está **por confirmar en BL-005** (ver `../erp.md` §5 y `../CANIVOROS-REFERENCIA-EMPRESA.md`).

| Aspecto | Lo que se sabe (D) | Lo que es `desconocido` |
|---|---|---|
| Grupo | Horneado natural: más cerca del cocido u horneado que del BARF crudo | — |
| Formatos | Chorizos (pollo y salmón, la línea que la empresa llama premium) y hamburguesas (cerdo, pollo, ternera) | Formato para gatos confirmado |
| Presentaciones | 500 g o «libra» a cliente final y tiendas; 1,5 kg por kilo a criadores, mínimo relatado de 40 kg | Equivalencia exacta de la «libra» |
| Precio | Relatado, con inconsistencias | **Precio confirmado: no comparar hasta BL-005** |
| Conservación | El sitio dice «lugar fresco y seco»; la empresa relata que los chorizos se deterioran después de abiertos | Si necesita frío en tienda; vida útil |
| Ración | El sitio menciona una guía de raciones | Gramos por día según el peso del perro (BL-041) |
| Canales en Bogotá | WhatsApp, contactos del mundo canino, criadores, dos aliados publicados | Puntos activos hoy (BL-035) |
| Promesa | Horneado, hecho en Sopó, proteína de origen animal, listo para servir; origen en perros de competencia | Soporte de las afirmaciones de salud e ICA (BL-016) |

La responsable de la operación percibe que pocos clientes pagan la línea premium y que algunos compradores recortan el presupuesto de alimento (`../erp.md`). Tenlo presente: parte de la competencia real puede ser el concentrado económico, no solo otras marcas naturales.

## 3. Conjunto competitivo

### 3.1 Niveles

| Nivel | Qué incluye | Ejemplos para empezar (por verificar) |
|---|---|---|
| **Directa** | Alimento natural cocido u horneado: el mismo tipo de producto | Pixie, Kanuto, VITA Alimento Vital |
| **De categoría** | Otras formas de alimentación natural: BARF crudo, precocido | Peluditos BARF, Vital Doggy, Rawf, Dogsy, KENKO Barf, 4DOGS, Bocado Pet Food, Barftender, Santo Barf; Bitute (precocido) |
| **De sustitución** | Lo que compra quien quiere «lo mejor» pero no da natural: concentrados premium y super premium | Taste of the Wild, Acana, Orijen, Nupec, Hill's, Pro Plan, Royal Canin |
| **Alternativa actual** | Lo que hace el comprador sin comprar una marca: cocinar en casa, mezclar comida casera con concentrado | Recetas caseras, carnicerías que venden «carne para perro» |
| **De presupuesto** | Concentrados económicos, cuando el comprador recorta gastos | Marcas masivas que aparezcan en entrevistas o tiendas |

Los ejemplos vienen de una lista previa hecha con ayuda de IA: **confirma que cada marca existe y se vende en Bogotá antes de registrarla**. Agrega marcas nuevas solo si aparecen en tiendas, entrevistas, reseñas o búsquedas reales.

### 3.2 Por segmento de comprador

El mismo competidor pesa distinto según quién compra. Analiza cada segmento por separado:

| Segmento (ver `../prospectos/AGENTS.md` §3) | Contra qué compara el comprador | Qué mirar |
|---|---|---|
| Tutor (cliente final) | Natural horneado o BARF frente a premium seco | Precio por día, comodidad, aceptación del perro, entrega |
| Tiendas y veterinarias | Marcas que ya rotan en su estantería | Margen, rotación, pedido mínimo, apoyo de marca, frío necesario |
| Criaderos | Concentrado por bulto, BARF por volumen | Costo por kg a volumen, entrega programada, constancia de suministro |
| Servicios caninos | Lo que dan hoy a los perros residentes | Practicidad, costo, posibilidad de reventa |

## 4. Proceso en 6 fases

**Fase 1 · Brief.** Escribe la pregunta de negocio, el segmento, el conjunto competitivo y la decisión que se tomará con el resultado. Sin brief no se empieza.

**Fase 2 · Recolección.** Datos públicos con la ficha de §6 y las fuentes de §5. Captura los precios de todas las marcas en la misma semana.

**Fase 3 · Normalización.** Precio por kg, costo diario, regular frente a promoción, con y sin envío (§7).

**Fase 4 · Análisis.** Aplica los marcos de §8 que respondan a la pregunta del brief. No todos los análisis necesitan todos los marcos.

**Fase 5 · Síntesis.** Hallazgo → implicación → recomendación → prueba (§10). Máximo 5 hallazgos principales en el resumen ejecutivo.

**Fase 6 · Monitoreo.** Una vez al mes, revisa el radar (§8.9) y registra los cambios.

## 5. Fuentes y fiabilidad

| Fuente | Para qué | Etiqueta habitual |
|---|---|---|
| Web y tienda online de la marca | Productos, presentaciones, precios, ingredientes declarados, raciones, zonas de entrega | Precio y catálogo (E) con fecha; promesas (D) |
| Página de distribuidores o «dónde comprar» | Cobertura en Bogotá | (D) de la marca |
| Rappi, Mercado Libre y tiendas online de terceros | Precio en otros canales, disponibilidad, reseñas | (E) con fecha |
| Google Maps (puntos de venta y fichas de las marcas) | Ubicación, reseñas, fotos de producto en estantería | (E) |
| Instagram, Facebook y TikTok | Mensajes, frecuencia de publicación, promociones, comunidad | Publicaciones (E); seguidores y likes (V) |
| Biblioteca de anuncios de Meta y Centro de transparencia de anuncios de Google | Anuncios activos, mensajes y ofertas que están pagando | (E) con fecha |
| Google Trends y sugerencias del buscador | Interés relativo en «BARF», «comida natural para perros», nombres de marca | (V): es un índice relativo, no volumen |
| Reseñas públicas (Maps, Rappi, web) | Voz del cliente | Patrones agregados (E) con número de reseñas |
| Registros públicos (RUES, estados financieros publicados en Supersociedades, registros ICA si son consultables) | Existencia de la empresa, tamaño, soporte de afirmaciones | (E) si el documento está publicado |
| Estimaciones de tráfico de terceros, índices de búsqueda (exa.ai), directorios | Pistas | (V) hasta confirmar |
| Entrevistas de BL-006 y BL-007 | Percepción, razones de elección | (D) del entrevistado; patrones con número de casos |

## 6. Ficha de datos por marca

| Campo | Detalle |
|---|---|
| Empresa, origen y planta | Ciudad de producción; razón social si es pública |
| Grupo y nivel | Según §3.1 |
| Productos y formato | Croqueta, chorizo, hamburguesa, porciones BARF, etc. |
| Conservación | Congelado, refrigerado o seco; vida útil si la publican |
| Presentaciones | Gramos o kilos de cada empaque |
| Arquitectura de precios | Precio de cada presentación (regular y promoción), descuentos por volumen, suscripción, costo y mínimo de envío, con fecha y fuente |
| **Precio por kg** | `precio ÷ (gramos ÷ 1.000)` |
| Ración publicada | Gramos por día según el peso del perro |
| **Costo diario** | Solo si hay ración publicada (§7) |
| Canales en Bogotá | Tiendas, veterinarias, venta directa, web, WhatsApp, apps |
| Cobertura | Número de puntos publicados en Bogotá y localidades donde están |
| Entrega | Zonas, días, tiempos, costo, pedido mínimo |
| Oferta al canal | Lo que publiquen para tiendas o distribuidores: «sé distribuidor», pedido mínimo, material, congelador |
| Promesa principal | La frase central de su web o de su perfil |
| Afirmaciones | Salud, ingredientes, registros; cita exacta y si muestran soporte |
| Prueba social | Testimonios, número y promedio de reseñas, alianzas con veterinarios o criadores |
| Presencia digital | Redes activas, frecuencia de publicación, anuncios activos |
| Recorrido de compra | Cómo se descubre, se pide, se paga, se recibe y se repite la compra (solo con información pública) |

## 7. Normalización y reglas de comparación

- **Precio por kg** = `precio ÷ (gramos ÷ 1.000)`. Muestra la cuenta. No redondees antes de dividir.
- **Costo diario** = `ración diaria en gramos × precio por kg ÷ 1.000`, solo con la ración publicada por la marca. Usa perfiles fijos para comparar: **perro adulto de 10 kg** y **perro adulto de 25 kg**, actividad normal. Si la marca no publica ración para ese perfil, el costo diario es `desconocido`.
- **Precio por kg no es costo de alimentación:** un kilo de BARF, uno de horneado y uno de croqueta seca no rinden lo mismo.
- Separa siempre **precio regular y promoción**, y **con y sin envío**. Anota si el precio incluye IVA cuando la fuente lo diga.
- **Misma semana:** captura los precios de todas las marcas comparadas en la misma semana, y registra la fecha de cada uno.
- **Compara dentro de cada nivel** de §3.1 antes de comparar entre niveles.
- **Canívoros solo con datos confirmados:** precio (BL-005) y ración (BL-041). Mientras tanto, su columna dice `desconocido`.
- Un precio sin fecha es (V). Un cálculo hereda la etiqueta del dato de origen.

## 8. Marcos de análisis

### 8.1 Benchmark competitivo

Tabla con los campos de §6 para todas las marcas del conjunto. Es la base de todo lo demás.

### 8.2 Matriz de perfil competitivo

| Factor de éxito | Peso | Canívoros | Marca 1 | Marca 2 | … | Evidencia |
|---|---|---|---|---|---|---|
| Disponibilidad en tiendas de Bogotá | | | | | | |
| Entrega (zonas, tiempo, costo) | | | | | | |
| Confianza y prueba social | | | | | | |
| Relación precio–valor | | | | | | |
| Presentaciones adecuadas | | | | | | |
| Atención y seguimiento | | | | | | |
| Aceptación del perro | | | | | | |

- Puntuación de 1 a 5 **solo con evidencia** en la última columna. Sin evidencia, la celda queda vacía.
- Los pesos suman 100 % y salen de las entrevistas (BL-006, BL-007). Mientras no existan, escribe `por definir` y no calcules el total.
- Total ponderado = suma de (peso × puntuación).

### 8.3 Mapa de posicionamiento

- **Ejes sugeridos:** precio por kg (observado) frente a naturalidad percibida; o comodidad de uso frente a naturalidad percibida.
- El eje de precio sale de datos (E). El eje de percepción sale de entrevistas o reseñas, con el número de casos. Si no hay datos de percepción, no dibujes el mapa: entrega solo el eje de precio.
- Entrégalo como tabla de coordenadas (marca, eje X, eje Y, fuente) y una lectura de 3 líneas: dónde hay espacios vacíos.

### 8.4 Matriz de mensajes y afirmaciones

| Marca | Promesa principal | Pruebas que muestra | Público al que habla | Tono | Afirmaciones de salud | ¿Muestra soporte? |
|---|---|---|---|---|---|---|

Resultado: qué promesas están saturadas, cuáles nadie usa (por ejemplo, el origen en perros de competencia) y qué afirmaciones debe evitar o respaldar Canívoros (insumo de BL-016 y BL-020).

### 8.5 Voz del cliente (reseñas)

| Marca | Reseñas revisadas | Rango de fechas | Aceptación del perro | Precio | Entrega | Empaque y conservación | Atención | Disponibilidad |
|---|---|---|---|---|---|---|---|---|

- En cada tema, cuenta menciones positivas y negativas. Reporta patrones con su número de casos, nunca comentarios aislados como si fueran la norma.
- No guardes autores ni textos con datos de personas.

### 8.6 Mapa de cobertura

Marca × localidad: número de puntos de venta publicados. Crúzalo con las microzonas candidatas de BL-014 (noroccidente alrededor de Manimal, sur alrededor de Sankatin) y con los entregables de `../resultados/prospectos/`.

### 8.7 Recorrido de compra comparado

Para cada marca, con información pública: cómo se descubre → cómo se informa el comprador → cómo pide y paga → cómo recibe → cómo repite (suscripción, recordatorio, entrega programada). Marca dónde hay fricción o ventaja frente a Canívoros (insumo de BL-022).

### 8.8 FODA competitivo de Canívoros

Solo con elementos que tengan evidencia y fuente. Cada fortaleza o debilidad se compara contra competidores concretos; cada oportunidad o amenaza viene de un hallazgo de §8.1 a §8.7.

### 8.9 Radar competitivo (monitoreo mensual)

| Fecha | Marca | Cambio observado | Evidencia (URL) | Implicación para Canívoros |
|---|---|---|---|---|

Revisa: precios y promociones, productos o presentaciones nuevas, nuevos distribuidores en Bogotá, anuncios activos, marcas nuevas en la ciudad.

## 9. Nivel de amenaza por competidor

| Criterio | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Solapamiento de comprador | Otro público | Poco | Parcial | El mismo comprador y segmento |
| Cobertura en las microzonas candidatas | Ninguna | Baja | Media | Alta |
| Cercanía de la propuesta | Muy distinta | Algo parecida | Parecida | Casi igual (natural horneado o cocido) |
| Fuerza de marca | Sin prueba social | Poca | Media | Mucha (reseñas, comunidad, alianzas) |

- Peso de la evidencia: criterio con (E) cuenta completo; con (D), la mitad; con (V) o `desconocido`, cero.
- **Amenaza alta:** 9 a 12 · **media:** 5 a 8 · **baja:** 0 a 4.
- Las fichas completas (§12) van primero para las amenazas altas.

## 10. Del hallazgo a la decisión

Cada hallazgo relevante se escribe así:

| Hallazgo (E) | Implicación (H) | Recomendación | Prueba (ficha BL-044) | Tarea |
|---|---|---|---|---|
| Qué se observó, con fuente y fecha | Qué significa para Canívoros | Qué haría el equipo | Hipótesis · métrica · casos · gasto máximo · regla de seguir, ajustar o parar | BL-### |

Ejemplo **ilustrativo** (no es un hallazgo real): «Tres marcas BARF entregan a domicilio con día fijo en Suba (E) → el comprador natural espera entrega programada (H) → ofrecer entrega programada en la microzona noroccidente → probar 4 semanas con 20 clientes, medir recompra a 30 días, gasto máximo por definir, seguir si la recompra supera a la del grupo sin entrega programada → BL-022».

## 11. Entregables y dónde guardarlos

Estas carpetas (`competencia/`) solo contienen instrucciones. **Los resultados se guardan en `../resultados/competencia/`**; créala si no existe.

| Archivo | Contenido |
|---|---|
| `../resultados/competencia/COMPETENCIA.md` | Registro vivo: tabla de marcas, fichas completas, nivel de amenaza e historial de revisiones |
| `../resultados/competencia/informe-AAAA-MM-DD.md` | Informe de cada análisis (estructura abajo) |
| `../resultados/competencia/RADAR.md` | Registro mensual de cambios de la competencia (§8.9) |

**Registro (`COMPETENCIA.md`).** Una fila por marca, con ID `C` + dos dígitos (el siguiente libre; no se reutiliza ni se renumera):

```markdown
| ID | Marca | Empresa / origen | Nivel | Formato y conservación | Presentación de referencia | Precio (fecha · fuente · regular/promo) | Precio por kg | Canales en Bogotá | Puntos publicados en Bogotá | Amenaza | Estado | Fuentes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Estados: `por_verificar` (solo se conoce el nombre o un dato sin fecha), `verificado` (ficha con datos E de la última revisión), `inactivo` (ya no se consigue en Bogotá).

**Informe (`informe-AAAA-MM-DD.md`).** Estructura:

1. **Pregunta de negocio y brief** (segmento, conjunto competitivo, decisión que se tomará).
2. **Resumen ejecutivo:** máximo 5 hallazgos, cada uno con evidencia, implicación y recomendación. Debe poder leerse en 2 minutos.
3. **Conjunto competitivo** por niveles.
4. **Benchmark** y normalización de precios.
5. Los marcos de §8 que se usaron.
6. **Nivel de amenaza** por competidor.
7. **Recomendaciones y pruebas** con su ficha BL-044.
8. **Limitaciones:** qué no se pudo verificar y por qué.
9. **Anexo de fuentes:** URL y fecha de cada dato.

## 12. Ficha completa de competidor

```markdown
### [C-ID] [Marca] — [nivel] · amenaza [alta/media/baja] ([puntaje]/12)
- Empresa / origen o planta:
- Web · Instagram · tienda online:
- Contacto comercial público:
- Productos, formato y conservación:
- Presentaciones y precios (fecha · fuente · regular/promo · con/sin envío):
- Precio por kg (cuenta):
- Ración publicada y costo diario (perro de 10 kg / 25 kg):
- Canales y cobertura en Bogotá (puntos publicados por localidad):
- Entrega (zonas, días, costo, mínimo):
- Oferta pública al canal:
- Promesa principal:
- Prueba social (reseñas: número y promedio; alianzas):
- Presencia digital (redes activas, frecuencia, anuncios activos):
- Recorrido de compra (descubrir → pedir → recibir → repetir):

**Hechos observados (E):**
1. ... — URL · fecha
**Declaraciones del competidor (D):**
- ... (cita exacta y corta)
**Hipótesis (H):**
- ...
**Por validar (V) / desconocido:** ventas, margen, rotación en tiendas...
**Qué significa para Canívoros:** ... → prueba sugerida (métrica y regla de decisión)
```

## 13. Precisión y evidencia

- Usa las etiquetas **(E)**, **(D)**, **(H)** y **(V)** de `../AGENTS.md` §3.
- **(E)** es lo que viste tú (precio en la web, lista de distribuidores, anuncio activo, foto de empaque), con URL y fecha.
- **(D)** es lo que la marca dice de sí misma («sin conservantes», «+90 puntos de venta»).
- Ventas, márgenes, costos y volúmenes internos de los competidores son **`desconocido`** salvo un documento público verificable. No los estimes.
- Interés en buscadores, seguidores y estimaciones de tráfico son (V): sirven para comparar tendencias, no para medir tamaño.
- No encadenes conclusiones sobre datos (V). Si un hallazgo depende de un dato (V), dilo.

## 14. Límites (no negociables)

- **No contactes** competidores, no pidas cotizaciones, no llenes formularios de distribuidor y no hagas compras de prueba sin aprobación de Andrés y un gasto máximo definido (BL-044).
- **Nunca te hagas pasar** por cliente, tienda o distribuidor para obtener información.
- **Solo información pública.** No guardes datos personales de empleados, clientes ni autores de reseñas (Ley 1581 de 2012).
- **No evadas bloqueos** ni hagas scraping contra los términos de servicio. Si una página bloquea o pide login, marca «No verificado».
- **No copies contenido protegido** (textos largos, fotos, creatividades completas): cita la frase corta necesaria, describe y enlaza.
- **No publiques** comparaciones con nombres de competidores: los informes son internos. Cualquier comparación pública necesita revisión de Andrés y soporte (BL-016).

## 15. Checklist antes de entregar

- [ ] El informe empieza con la pregunta de negocio y el brief.
- [ ] Conjunto competitivo definido por niveles y por segmento.
- [ ] Cada precio tiene fecha, fuente, presentación, regular/promo, con/sin envío y precio por kg; todos de la misma semana.
- [ ] Costo diario solo con ración publicada; si no, `desconocido`.
- [ ] Ningún precio de Canívoros comparado antes de BL-005.
- [ ] Hechos, declaraciones, hipótesis y por validar separados; datos internos de competidores en `desconocido`.
- [ ] Nivel de amenaza calculado con el peso de la evidencia.
- [ ] Cada hallazgo principal tiene implicación, recomendación y prueba con ficha BL-044.
- [ ] Resumen ejecutivo de máximo 5 hallazgos.
- [ ] Ningún dato personal; nada publicado ni enviado.
