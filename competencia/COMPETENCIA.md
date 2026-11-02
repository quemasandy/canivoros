# Competencia de Canívoros · Bogotá

> **Registro único del análisis competitivo.** Instrucciones en [AGENTS.md](AGENTS.md); reglas comunes en [../AGENTS.md](../AGENTS.md).
> Sembrado el 2026-11-02 desde `competencia_bogota.csv`. Los datos son **observaciones previas sin fecha exacta**: precios y canales son **(V) por validar** hasta re-verificarlos con fecha.
> Alimenta BL-015 (comparar 8–12 alternativas), BL-012, BL-016, BL-020, BL-023 y BL-024.

## Resumen

- **13 filas** registradas (12 marcas y un grupo de 4 marcas BARF pequeñas): 3 de horneado o cocido, 9 de BARF y 1 de precocido.
- **0 fichas completas** (BL-015). Ningún precio tiene fecha de captura.
- Ventas, márgenes y volúmenes de los competidores: **desconocidos**.
- Faltan los **concentrados premium** que pide BL-015 (ver *Próxima revisión*).

## Canívoros (referencia interna, no es un competidor)

Para comparar en igualdad de condiciones. Todo es relato de la empresa (D) y está **por confirmar en BL-005**.

| Aspecto | Canívoros |
|---|---|
| Grupo | Horneado natural, más cerca de Pixie y Kanuto que de BARF |
| Formatos | Chorizos (pollo y salmón, perros; salmón y cerdo, gatos), hamburguesas (cerdo, pollo, ternera) |
| Presentaciones | 500 g o «libra» (cliente final y tiendas); 1,5 kg por kilo a criadores, mínimo relatado de 40 kg |
| Conservación | `desconocido` (el sitio dice «lugar fresco y seco»; la empresa relata que los chorizos se deterioran después de abiertos) |
| Precios | Relatados en `../erp.md` §5, con inconsistencias. **No se comparan aquí hasta BL-005** |
| Ración | `desconocido` (BL-041) |
| Canales en Bogotá | WhatsApp, contactos del mundo canino, criadores, 2 aliados publicados (Manimal y Sankatin) |

## Registro

El precio por kg se calcula como `precio ÷ (gramos ÷ 1.000)` y es (V) porque el precio de origen no tiene fecha.

| ID | Marca | Tipo | Origen / planta | Precio observado (V) | Precio por kg (calculado, V) | Canales en Bogotá (D/V) | Web | Fuente |
|---|---|---|---|---|---|---|---|---|
| C01 | Pixie (LPT Pet Company) | Cocido/horneado | Bogotá (Cl. 11A #40-20, no punto de venta) | Pollo 500 g $12.960; pollo 2 kg $85.018 | 500 g: $25.920/kg; 2 kg: $42.509/kg (ver alertas) | ~90 puntos en Bogotá: CEBA, Agrocampo, Laika, Pet Gourmet, Movet, pet shops independientes | https://pixie.net.co/ | https://pixie.net.co/contacto |
| C02 | VITA Alimento Vital | Horneado (pavo/salmón) | desconocido | Sensitive Salmón 5 kg $139.800 | $27.960/kg | Venta directa sin intermediarios; entrega día siguiente Bogotá | https://vitaalimentovital.com/ | https://vitaalimentovital.com/ |
| C03 | Kanuto | Horneado, congelado | Medellín | Pollo 500 g $12.200; Cerdo $14.900 | Pollo: $24.400/kg; Cerdo: desconocido (sin peso) | The Pet House (Suba); envío | https://www.kanuto.com.co/ | https://www.kanuto.com.co/ ; https://thepethouseco.com/collections/alimentos-perros |
| C04 | Peluditos BARF | BARF crudo | Bogotá (Puente Aranda, Cra. 54 #17-48) | desconocido | desconocido | ~50 distribuidores Bogotá + Agrocampo, Laika, Rappi | https://peluditosbarf.com.co/ | https://peluditosbarf.com.co/distribuidores/ |
| C05 | Vital Doggy | BARF crudo | Bogotá | desconocido | desconocido | ~35 distribuidores norte/sur Bogotá | https://vitaldoggy.co/ | https://vitaldoggy.co/distribuidores/ |
| C06 | Rawf | BARF crudo | desconocido | desconocido | desconocido | 10 tiendas propias Rawf Market en Bogotá | https://rawf.co/ | https://rawf.co/pages/tiendas |
| C07 | Dogsy Pet Food | BARF crudo | Bogotá (Cl. 66c Sur #87b-62, según directorio) | Pollo Mix 500 g $5.850 | $11.700/kg | Online, cadena de frío propia Bogotá | https://www.dogsy.com.co/ | https://www.dogsy.com.co/dieta-barf |
| C08 | KENKO Barf | BARF crudo | Bogotá | desconocido | desconocido | Online/domicilio | https://www.kenkobarf.com/ | https://www.kenkobarf.com/ |
| C09 | 4DOGS | BARF | Bogotá | 250 g desde $2.500 | desde $10.000/kg | Entrega semanal directa | https://4dogs.co/ | https://4dogs.co/ |
| C10 | Bocado Pet Food | BARF crudo y cocido | Bogotá | Caja 4 kg $50.000–$90.000 | $12.500–$22.500/kg | Online/domicilio | https://bocadopetfood.com/ | https://bocadopetfood.com/ |
| C11 | Bitute | Natural precocido | Bogotá (Suba) | desconocido | desconocido | Online | https://bitute.co/ | https://bitute.co/ |
| C12 | Barftender | BARF | Bogotá (Teusaquillo, Cra. 33A #25F-12) | desconocido | desconocido | Tienda física | barftender.co (no verificado) | https://www.aiyellow.com/barftender/ |
| C13 | Santo Barf / LokyBarf / Natural Barf / Ecopetfood | BARF | Bogotá (Suba, Fontibón) | desconocido | desconocido | Locales/domicilio | desconocido | https://exa.ai/library/place/6j7f7df6vwk ; https://exa.ai/library/place/w24mgdxwqnl |

## Cobertura en prospectos

Cuántas filas de `../prospectos/PROSPECTOS.md` mencionan cada marca. Casi todas vienen de los directorios de distribuidores de las propias marcas (D): no se ha verificado ninguna en tienda.

| Marca | Filas en prospectos | Puntos que declara la marca (D) |
|---|---|---|
| Pixie (C01) | 77 | ~90 en Bogotá |
| Peluditos BARF (C04) | 23 | ~50 en Bogotá |
| Vital Doggy (C05) | 17 | ~35 en Bogotá |
| Kanuto (C03) | 1 (P104 The Pet House Spa) | desconocido |
| Taste of the Wild | 4 | — |
| Acana / Orijen | 3 / 3 | — |
| Pro Plan | 2 | — |
| Nupec, Hill's, Royal Canin, Diamond | 1 cada una | — |

## Alertas de datos

| Fila | Alerta | Qué hacer |
|---|---|---|
| C01 Pixie | El empaque de 2 kg sale más caro por kg ($42.509) que el de 500 g ($25.920). Es raro: puede ser otra receta, un error o un precio con envío | Re-verificar ambas presentaciones con fecha |
| C03 Kanuto | El precio de cerdo no indica peso | Confirmar presentación antes de calcular |
| C09 4DOGS | «Desde» es un precio mínimo, no el de una presentación concreta | Registrar presentaciones y precios uno por uno |
| C10 Bocado | Rango de precio para una misma caja de 4 kg | Separar por producto o receta |
| C12 Barftender | Web no verificada; la fuente es un directorio de terceros | Confirmar en Maps o en redes |
| C13 | Agrupa 4 marcas; la fuente es un índice de búsqueda | Separar en filas propias al verificar (AGENTS.md §8) |

## Próxima revisión (BL-015)

Orden sugerido (H) para llegar a 8–12 alternativas comparables:

1. **Horneado o cocido, competencia directa:** C01 Pixie, C03 Kanuto, C02 VITA.
2. **BARF con más presencia en tiendas prospecto:** C04 Peluditos BARF, C05 Vital Doggy.
3. **BARF de venta directa con domicilio:** C07 Dogsy o C09 4DOGS (uno de los dos).
4. **Concentrados premium** (aún sin fila; reciben ID al iniciar su ficha): Taste of the Wild, Acana u Orijen y Nupec, por ser los que más aparecen en las tiendas prospecto.

## Matriz de perfil competitivo (plantilla)

Se llena solo con evidencia. Los pesos salen de las entrevistas de BL-006 y BL-007; mientras tanto quedan `por definir`. Puntuación de 1 a 5.

| Factor de éxito | Peso | Canívoros | Pixie | Kanuto | Peluditos BARF | Vital Doggy | Evidencia |
|---|---|---|---|---|---|---|---|
| Disponibilidad en tiendas de Bogotá | por definir | | | | | | |
| Entrega (zonas, tiempo, costo) | por definir | | | | | | |
| Confianza en la marca | por definir | | | | | | |
| Relación precio–valor | por definir | | | | | | |
| Presentaciones adecuadas | por definir | | | | | | |
| Atención y seguimiento | por definir | | | | | | |
| Aceptación del perro | por definir | | | | | | |

## Fichas

_Aún no hay fichas. Usa la plantilla de AGENTS.md §7._

## Hipótesis iniciales (H, por validar)

| Hipótesis | Cómo probarla |
|---|---|
| Pixie y Peluditos BARF compiten sobre todo por **disponibilidad** (muchos puntos de venta declarados), no solo por ingredientes | Preguntar a tiendas en BL-007 por qué rotan esas marcas; cruzar su cobertura con las microzonas de BL-014 |
| Las tiendas que ya venden BARF o Pixie son las de mejor encaje para Canívoros | En BL-012, comparar respuesta y pedido entre tiendas con y sin natural verificado |
| **Kanuto** (horneado y congelado) es el comparable más cercano en proceso y formato | Hacer su ficha primero; comparar precio por kg cuando BL-005 confirme el de Canívoros |
| En el segmento natural, la **entrega directa programada** es lo normal (4DOGS, Dogsy, KENKO, Bocado) | Si se confirma, probar entrega programada o recordatorio de reposición en una microzona (BL-022) y medir recompra |
| BARF parece más barato por kg ($10.000–$22.500/kg) que el horneado o cocido ($24.400–$27.960/kg, sin contar el Pixie de 2 kg), con precios (V) | Re-verificar precios con fecha antes de usarlo para fijar precio o mensaje |

## Historial

### Revisión 2026-11-02 · estructura y cálculos (sin verificación web)
- Se agregaron la referencia interna de Canívoros, el precio por kg calculado, la cobertura en prospectos, las alertas de datos, el orden de la próxima revisión y la plantilla de la matriz de perfil competitivo.
- Ningún precio, canal ni fuente de las 13 filas cambió.

### Siembra 2026-11-02
- Origen: `competencia_bogota.csv` (13 filas). Precios sin fecha de captura: re-verificar antes de usarlos en cualquier comparación.
