# Técnicas de análisis competitivo

Cómo aplicar cada técnica: para qué sirve, pasos, resultado y errores comunes. Usa solo las que respondan a la decisión definida en el paso 1.

## Contenido

1. [Comparación de productos y precios](#1-comparación-de-productos-y-precios)
2. [Benchmarking competitivo](#2-benchmarking-competitivo)
3. [Benchmarking funcional](#3-benchmarking-funcional)
4. [Matriz de perfil competitivo](#4-matriz-de-perfil-competitivo)
5. [Mapa de posicionamiento](#5-mapa-de-posicionamiento)
6. [Análisis de mensajes y afirmaciones](#6-análisis-de-mensajes-y-afirmaciones)
7. [Grupos estratégicos](#7-grupos-estratégicos)
8. [Análisis de reseñas](#8-análisis-de-reseñas)
9. [Mapa de cobertura](#9-mapa-de-cobertura)
10. [Análisis de ventas perdidas](#10-análisis-de-ventas-perdidas)
11. [Cinco fuerzas de Porter](#11-cinco-fuerzas-de-porter)
12. [Cadena de valor comparada](#12-cadena-de-valor-comparada)
13. [Análisis de brechas](#13-análisis-de-brechas)
14. [FODA competitivo cruzado](#14-foda-competitivo-cruzado)
15. [Conexión con QFD, Kano y JTBD](#15-conexión-con-qfd-kano-y-jtbd)

---

## 1. Comparación de productos y precios

**Para qué:** saber cuánto paga el comprador por cada alternativa y cuánto le cuesta realmente alimentar a su mascota.

**Pasos**
1. Por alternativa, registra en `competencia-AAAA-MM-DD.csv` (filas `registro=precio`) cada presentación relevante: peso, precio regular, promoción vigente, canal, vendedor, zona, fecha y fuente.
2. Registra también lo que afecta al costo total: costo de envío, pedido mínimo, tiempo de entrega y disponibilidad.
3. Si la etiqueta declara humedad (análisis garantizado), anótala en `humedad_pct`. Si la marca publica una guía de ración, anota los gramos por día para un perro de 10 kg y uno de 25 kg (`racion_10kg_g`, `racion_25kg_g`) y su fuente.
4. Captura todos los precios de la comparación en la misma semana.
5. Corre `competencia.py precios`. Compara precio por kg dentro de cada tipo, no entre tipos con humedades muy distintas. La sección «Cuentas» muestra cada cálculo para incluirlo en el informe.
6. Usa el costo diario como comparación principal cuando haya raciones publicadas para el mismo perfil; el precio por kg de materia seca es un apoyo cuando no las hay.

**Resultado:** tabla de precio por kg con fecha, fuente y marca de evidencia, bandas por tipo, cuentas visibles y, si hay raciones, costo diario y mensual para perros de 10 y 25 kg.

**Errores comunes**
- Comparar precio por kg de un producto húmedo (chorizo, hamburguesa, BARF) con croquetas secas como si fueran equivalentes.
- Inventar raciones o suponer que un kilo de dos productos dura lo mismo.
- Mezclar precio regular y precio en promoción.
- Tomar el precio de un revendedor de marketplace como precio de la marca.
- Convertir «libra» a gramos sin confirmar la equivalencia.
- Ubicar a Canívoros con precios que la empresa no ha confirmado (BL-005).

## 2. Benchmarking competitivo

**Para qué:** comparar con criterios comunes lo que hacen los competidores directos y los resultados que se pueden observar.

**Pasos**
1. Define 6–10 criterios observables ligados a la decisión: precio por kg, presentaciones, canales, tiempo y costo de entrega, atención (tiempo de respuesta), empaque, información en etiqueta, garantías, programa de recompra o suscripción.
2. Mide cada criterio con el mismo método para todos: misma fecha aproximada, misma zona y mismo tipo de fuente.
3. Registra cómo se midió y con qué marca de evidencia («web oficial consultada el 2026-11-03 (D)», «compra de prueba aprobada del 2026-11-05 (E)»).
4. Señala quién lo hace mejor en cada criterio y qué práctica concreta lo explica.

**Resultado:** tabla de criterios por competidor y una lista de prácticas que vale la pena adaptar o superar.

**Errores comunes:** criterios no observables («calidad»), medir a cada competidor con un método distinto o copiar prácticas sin preguntarse si resuelven un problema de nuestros compradores.

## 3. Benchmarking funcional

**Para qué:** aprender de empresas que destacan en una función concreta, aunque sean de otro sector.

**Pasos**
1. Elige una función con problemas o potencial: reposición y recordatorios, suscripciones, atención por WhatsApp, trazabilidad por lote, entregas programadas o programa de distribuidores.
2. Identifica 3–5 referentes que la hagan bien (otros alimentos frescos, cafés de especialidad por suscripción, farmacias a domicilio, etc.).
3. Documenta cómo lo hacen: pasos que vive el cliente, mensajes, frecuencia, condiciones y herramientas visibles.
4. Traduce cada práctica a nuestra operación, con lo que costaría y lo que habría que probar.

**Resultado:** prácticas adaptables con su requisito operativo y una prueba propuesta.

## 4. Matriz de perfil competitivo

**Para qué:** comparar a la marca propia con los competidores principales en los factores que deciden la compra, y encontrar brechas prioritarias.

**Pasos**
1. Elige 5–10 factores clave de éxito desde el punto de vista del comprador (disponibilidad, confianza, relación precio-valor, aceptación de la mascota, facilidad de compra y entrega, atención, información del producto). Para canales, haz una matriz aparte desde el punto de vista del distribuidor (rotación, margen, condiciones y apoyo comercial).
2. Asigna pesos que sumen 1. Lo ideal es derivarlos de entrevistas: pide a cada comprador que ordene los criterios por importancia y promedia las posiciones. Si los propones tú, márcalos como provisionales.
3. Puntúa cada competidor de 1 a 4 en cada factor (1 = debilidad mayor, 2 = debilidad menor, 3 = fortaleza menor, 4 = fortaleza mayor) y escribe la evidencia, con su marca (E), (D), (H) o (V), en la misma fila. Sin evidencia, deja la celda vacía.
4. Corre `competencia.py matriz` (formato largo: una fila por factor y competidor).
5. Lee primero las brechas por factor y después el total. Revisa la sección «Robustez».

**Resultado:** matriz con totales ponderados, cobertura de evidencia, ranking, prueba de sensibilidad y brechas de la marca propia ordenadas por peso.

**Errores comunes:** puntuar por intuición, repartir pesos iguales sin decirlo, sacar conclusiones de diferencias de pocas décimas o rellenar celdas sin datos para que «cierre» el total.

## 5. Mapa de posicionamiento

**Para qué:** ver cómo perciben los compradores a las marcas en dos dimensiones que importan para su decisión y encontrar espacios libres.

**Pasos**
1. Elige dos ejes que los compradores mencionen espontáneamente, por ejemplo precio percibido y confianza, o naturalidad y conveniencia. Evita ejes que solo le importen a la marca.
2. **Mapa perceptual (preferido):** en entrevistas o encuestas, pide a cada persona que califique de 1 a 5 solo las marcas que conoce en cada eje. Promedia y anota el n de cada marca.
3. **Mapa declarado (alternativa de escritorio):** ubica las marcas según lo que comunican (precio publicado, promesas). Rotúlalo como «posicionamiento declarado (D)», no como percepción.
4. Grafica las marcas, con el tamaño del punto según el número de respuestas si lo tienes. Si hace falta un gráfico, usa la skill de visualización de datos disponible; una tabla con las coordenadas también sirve.
5. Busca zonas vacías y pregúntate si están vacías porque nadie las atendió o porque nadie las quiere.

**Resultado:** mapa con su base (perceptual o declarado y n), lectura de espacios libres y una hipótesis de posicionamiento para probar.

## 6. Análisis de mensajes y afirmaciones

**Para qué:** entender qué promete cada marca, cómo lo respalda y qué espacio de comunicación queda (útil para BL-016 y BL-020).

**Pasos**
1. Por marca, recoge la promesa principal (web, empaque, redes, anuncios), las pruebas que ofrece (registro ICA, análisis garantizado, testimonios, certificaciones, veterinarios), el público al que habla y el tono.
2. Clasifica las afirmaciones por tipo: ingrediente, proceso, beneficio de salud, origen, precio, conveniencia o emoción.
3. Marca cuáles están respaldadas por una prueba verificable y cuáles son declaraciones sin soporte visible.
4. Compara con nuestras propias afirmaciones aplicando el mismo criterio.

**Resultado:** tabla de mensajes y una lista de territorios saturados (todos dicen «natural») frente a territorios libres y creíbles para nosotros.

**Error común:** repetir en nuestro informe las afirmaciones de salud de un competidor como si fueran hechos.

## 7. Grupos estratégicos

**Para qué:** agrupar competidores con modelos parecidos para comparar dentro de cada grupo y ver contra quién compite realmente cada oferta.

**Pasos**
1. Elige dos variables estructurales: por ejemplo, precio por kg y tipo de proceso (seco, horneado, crudo), o canal principal (gran superficie, petshop, venta directa) y alcance (nacional, local).
2. Ubica cada alternativa y agrupa las cercanas.
3. Describe cada grupo: público, propuesta, canales y barreras para moverse a otro grupo.
4. Ubica la marca propia y define su grupo de referencia.

**Tipos de partida para Canívoros** (de `competencia/AGENTS.md`): directo (natural cocido u horneado), BARF y precocido, concentrado premium y alternativa casera. Dentro de cada tipo pueden aparecer subgrupos, por ejemplo venta directa por redes frente a tiendas.

## 8. Análisis de reseñas

**Para qué:** identificar necesidades satisfechas y problemas repetidos de cada alternativa desde la voz de sus clientes.

**Pasos**
1. Define la muestra antes de leer: fuentes (Google Maps, marketplaces, redes), criterio (las N más recientes, todas desde una fecha) y periodo. Esto evita elegir solo las reseñas que confirman lo que ya creemos.
2. Codifica cada reseña con uno o más temas de una lista fija: aceptación de la mascota, digestión o heces, pelaje o piel, precio, entrega, disponibilidad, empaque o conservación, atención, información del producto, otro. Usa `tema:negativo` cuando una reseña mezcla sentimientos.
3. Copia solo extractos breves y no guardes nombres de los autores.
4. Corre `competencia.py resenas`.
5. Lee los patrones por marca y, sobre todo, los problemas que se repiten en varias marcas.

**Resultado:** temas por marca con conteos, separación entre patrones y menciones aisladas, y problemas comunes de la categoría.

**Errores comunes:** concluir con pocas reseñas, mezclar periodos muy distintos o tratar testimonios de salud como prueba de eficacia.

## 9. Mapa de cobertura

**Para qué:** ver dónde hay oferta abundante o escasa y elegir zonas o aliados (BL-014, BL-012).

**Pasos**
1. Por zona candidata, ubica puntos de venta de cada alternativa (Google Maps, directorios de las marcas, visitas) y registra la fecha de verificación.
2. Registra las zonas de entrega, el tiempo prometido y el costo de envío de las tiendas en línea y la venta directa, probando direcciones de las zonas candidatas.
3. Marca qué presentaciones hay disponibles en cada punto visitado.
4. Resume por zona: número de puntos por grupo estratégico, entrega disponible y vacíos.

**Resultado:** tabla o mapa por zona que alimenta el criterio «Oportunidad frente a competidores» de la matriz de microzonas.

## 10. Análisis de ventas perdidas

**Para qué:** saber qué competidores y qué barreras nos quitan ventas a nosotros, no al mercado en general.

**Pasos**
1. En cada consulta que no termina en compra, registra fecha, canal, etapa alcanzada, motivo (lista fija: precio, presentación, disponibilidad, entrega, desconfianza, la mascota no lo aceptó, sin respuesta a tiempo, otro) y la alternativa elegida si la persona la menciona.
2. Quien atiende puede preguntar con respeto y sin insistir: «¿Qué decidiste comprar finalmente? ¿Qué te hizo elegirlo?».
3. Revisa los motivos cada mes y crúzalos con el canal y la zona.

**Resultado:** motivos de pérdida con su frecuencia y los competidores que ganan esas ventas. Se apoya en la auditoría de consultas de WhatsApp (BL-059), en la recuperación de clientes (BL-060) y en un campo de motivo de pérdida en el sistema comercial (BL-011).

## 11. Cinco fuerzas de Porter

**Para qué:** evaluar la presión competitiva del sector o de un nicho antes de entrar o invertir.

**Pasos:** para cada fuerza, escribe la evidencia, una intensidad (baja, media o alta) y la implicación.

| Fuerza | Preguntas guía para alimento natural de mascotas |
|---|---|
| Rivalidad | ¿Cuántas marcas compiten en el grupo? ¿Hay guerras de precio o promociones constantes? |
| Nuevos participantes | ¿Qué tan fácil es producir y obtener registro ICA? ¿Aparecen marcas nuevas por redes? |
| Sustitutos | ¿Qué tan fácil es pasar al concentrado tradicional o a la comida casera? |
| Poder de los compradores | ¿Los distribuidores exigen margen, crédito o devoluciones? ¿El consumidor cambia fácilmente? |
| Poder de los proveedores | ¿Hay pocos proveedores de subproductos o de proteína? ¿El suministro es irregular? |

**Error común:** llenar la tabla con opiniones generales sin evidencia ni implicación concreta.

## 12. Cadena de valor comparada

**Para qué:** ver en qué actividades se generan los costos y la diferenciación, y dónde podemos competir.

**Pasos**
1. Lista las actividades: compras, producción, empaque, almacenamiento, distribución, venta, servicio posventa.
2. Para cada competidor, registra solo lo observable (empaque, canales, tiempos de entrega, atención, garantías). Sus costos internos suelen ser desconocidos y así deben quedar.
3. Para la marca propia, usa datos internos medidos (BL-025, BL-055).
4. Identifica actividades donde tenemos ventaja demostrable y otras donde la falta de capacidad limita cualquier estrategia comercial.

## 13. Análisis de brechas

**Para qué:** medir la distancia entre nuestro desempeño y una referencia (el mejor competidor observado o una meta), y priorizar qué cerrar.

**Pasos**
1. Toma los factores con más peso de la matriz o los criterios del benchmarking.
2. Para cada uno, registra nuestra situación medida, la referencia y su fuente, la brecha y la evidencia.
3. Prioriza por peso del factor × tamaño de la brecha × factibilidad.
4. Define una acción o prueba por brecha prioritaria.

**Resultado:** tabla de brechas priorizadas. La salida «Brechas y ventajas» del subcomando `matriz` es un buen punto de partida.

## 14. FODA competitivo cruzado

**Para qué:** sintetizar para la gerencia cómo se relacionan nuestras capacidades con el entorno competitivo.

**Pasos**
1. Fortalezas y debilidades: capacidades internas comparadas con los competidores, con evidencia (matriz, benchmarking, datos internos).
2. Oportunidades y amenazas: hechos externos verificados (huecos de cobertura, problemas comunes de la categoría, movimientos de competidores).
3. Cruza los cuadrantes: FO (usar fortalezas para aprovechar oportunidades), DO (corregir debilidades para aprovecharlas), FA (usar fortalezas para defenderse) y DA (reducir exposición).
4. Convierte cada estrategia cruzada en una decisión o una prueba.

**Error común:** listas largas de adjetivos sin evidencia ni consecuencias. Es mejor un FODA de seis elementos sólidos que uno de treinta débiles.

## 15. Conexión con QFD, Kano y JTBD

- **QFD (BL-024):** el paso 8 de la Casa de la Calidad compara cómo satisfacen las necesidades los competidores. Reutiliza las puntuaciones de la matriz y los datos técnicos observados (humedad, proteína y grasa declaradas, presentaciones).
- **Kano:** ayuda a separar atributos básicos (que todos deben cumplir, como el registro ICA) de los de desempeño (precio, entrega) y los que sorprenden. Un atributo básico no diferencia aunque lo comuniquemos mucho.
- **JTBD:** en las entrevistas, pregunta qué intentaba conseguir el comprador cuando eligió su alimento actual; muchas veces el competidor real es la comodidad o la costumbre, no otra marca.
