# Contexto: Canívoros y Gatívoros

Resumen para orientar el análisis. Las fuentes completas están en el repositorio. Si una fuente es más reciente que este resumen, manda la fuente.

## La empresa

- **Qué vende:** alimento natural para perros (Canívoros) y gatos (Gatívoros) con proteínas de pollo, salmón y cerdo. La web lo presenta como horneado, listo para servir y distinto de una dieta cruda o BARF. Las ventas registradas usan formas como hamburguesas, chorizos, nuggets y orejas, vendidas por libra y por kilo.
- **Dónde:** planta en Sopó (Cundinamarca). Distribuidores publicados en Bogotá (noroccidente y Bosa), Chía, Sopó, Zipaquirá y Villavicencio, pendientes de validar (BL-035).
- **Canales:** WhatsApp, distribuidores, petshops y veterinarias aliadas, y venta directa por volumen a criadores.
- **Origen de marca:** crianza de perros de competencia; testimonios y ejemplares de exposición publicados por la marca.

**Antes de elegir competidores, confirma la forma del producto que se analiza.** Un producto húmedo (chorizo, hamburguesa) compite y se compara distinto que una croqueta seca: su precio por kg no es comparable sin pasar por materia seca o por ración.

## Precios propios provisionales

Fuente: `erp.md` §3 y §5 (relato de la responsable). Son `declarado` con certeza media y siguen pendientes de confirmar en BL-005; la moneda parece COP.

| Producto | Forma | Presentación | Público | Distribuidor |
|---|---|---|---:|---:|
| Pollo y salmón, perros | Chorizos | 500 g | 14.000 | 9.800 |
| Cerdo | Hamburguesas | 500 g | 5.000* | 35.000* |
| Pollo | Hamburguesas | 500 g | 5.000 | 3.500 |
| Ternera | Por confirmar | 500 g | 6.000 | 4.500 |
| Salmón y cerdo, gatos | Chorizos | 500 g | 16.000 | 11.200 |
| Cerdo o pollo, volumen | Hamburguesas | 1,5 kg | 6.200 por kg | — |

\* Valor inconsistente en la fuente; según BL-005, el precio de cerdo a distribuidor se corrigió a 3.500. No lo uses sin confirmarlo.

- La fuente alterna «libra» y «500 g»: confirma la equivalencia antes de usar `--libra-g 500`.
- La venta por volumen exige un pedido mínimo de 40 kg.
- No hay raciones confirmadas (BL-041); sin ellas no se puede calcular el costo diario propio.

## Candidatos de competencia

- **BL-015** pide comparar entre 8 y 12 alternativas y menciona Pixie, Kanuto, VITA, BARF y premium secos. Verifica su existencia, oferta y precio actuales; no asumas nada sobre ellas.
- `backlog/README.md` cita una hoja «Competencia» en `prospectos_bogota.xlsx` y un archivo `precios_competencia_bogota.xlsx` que **no están en el repositorio**. Si el usuario los tiene, pídeselos y úsalos como punto de partida, con su fecha.
- Incluye siempre alternativas no comerciales (comida casera, concentrado de siempre) y, para gatos, el concentrado al que el gato está acostumbrado.

## Segmentos de prueba del plan de Bogotá

Compradores de alimento premium; personas interesadas en alimentación natural; tutores de perros activos; tiendas y centros especializados; criadores y clientes de alto volumen (BL-043); para gatos, veterinarias y hogares con gatitos (BL-026). El piloto comercial se concentra en perros.

## Preguntas que la empresa quiere resolver

De `erp.md`: qué productos son comparables y cómo se comercializan; qué paga el comprador por cantidades equivalentes; qué gramaje facilita compra, consumo y rentabilidad (se mencionan 200, 350 y 700 g); qué compradores encajan con cada producto; cómo crecer con distribuidores; qué favorece la recompra.

## Decisiones del backlog que este análisis alimenta

| Tarea | Qué necesita del análisis |
|---|---|
| BL-015 | Tabla de 8–12 alternativas con precio por kg comparable, fecha y fuente |
| BL-014 | Criterio «Oportunidad frente a competidores» (10 %) de la matriz de microzonas |
| BL-012 | Marcas que rotan en tiendas de alimento natural y condiciones que esperan |
| BL-016 | Afirmaciones de competidores frente a las propias («sin subproductos») |
| BL-020 | Territorios de mensaje: horneado frente a facilidad de uso |
| BL-023 | Presentaciones de entrada de la competencia y su precio |
| BL-024 | Comparación competitiva del paso 8 del QFD |
| BL-043 | Ofertas de volumen o para criadores de otras marcas |
| BL-026 | Alternativas para gatos en veterinarias |
| BL-028 | Insumo para decidir cómo crecer en Bogotá |

## Fuentes en el repositorio

- `CANIVOROS-REFERENCIA-EMPRESA.md`: oferta, mensajes, distribuidores y contacto según la web.
- `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`: zonas, segmentos, comparación de alternativas, experimentos e indicadores.
- `metodologias_analisis_competitivo.md`: técnicas priorizadas y campos para el ERP.
- `erp.md`: catálogo, precios relatados, preguntas comerciales y operación.
- `GuiaPesquisaProdutosServicosES.md` y `GuiaDesenvolverProdutosServicosES.md`: ficha de análisis de competencia y método de investigación.
- `backlog/`: tareas BL-001 a BL-058.
- `ventas_canivoros_2026.xlsx`: cantidades vendidas por cliente y mes (sin precios).

## Otros usos en este repositorio

- **Agencia Growth Partner (BL-030, BL-045):** para comparar la oferta de la agencia con agencias de marketing digital, de performance, consultoría comercial, CRM, IA y automatización o RevOps, parte de la tabla de diferencias en `pasos_sysmkt.md`. Usa la misma matriz con factores desde el punto de vista de la pyme que contrata.
- **Diagnóstico de crecimiento para pymes (BL-017, BL-018):** esta skill puede ser el módulo de competencia del diagnóstico; pide al cliente el contexto mínimo del paso 0.
