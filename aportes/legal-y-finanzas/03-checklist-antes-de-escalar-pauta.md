# 03 · Lista de chequeo antes de escalar pauta

> Completa las reglas del [plan Bogotá](../../CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md) ("Reglas para ampliar, ajustar o detener") y de [BL-044](../../backlog/BL-044-registrar-hipotesis-y-criterios-de-decision-antes.md). Los umbrales son **propuestas** para discutir con la gerencia. No son normas ni resultados observados. Por "escalar" entendemos subir el gasto de Meta, o de cualquier pauta, por encima del límite del experimento piloto.

## A. Bloqueantes legales: sin estos puntos, no se pauta

| # | Chequeo | Umbral | Fuente | Estado |
|---|---|---|---|---|
| A1 | Registro ICA de la planta como fabricante | Número vigente en el archivo | Res. ICA 61252/2020, art. 4 (ver 01) | dato pendiente |
| A2 | Registro ICA de **cada producto pautado** | 100 % de los SKU del anuncio tienen registro (o exención confirmada) | arts. 13 y 15 | dato pendiente |
| A3 | Afirmaciones del anuncio y la etiqueta revisadas | Cada claim queda como soportado, reformulado o quitado (BL-016) | Res. ICA, art. 27.1; Ley 1480, arts. 29 y 30 | BL-016 en backlog |
| A4 | Facturación electrónica | Cada venta pautada se puede facturar en el sistema habilitado | Res. DIAN 165/2023 | dato pendiente |
| A5 | Autorización de datos para leads de WhatsApp | Texto de autorización y política publicados | BL-058 | en backlog |
| A6 | Política de cambios y devoluciones publicada | Cubre el retracto (o su excepción por ser perecedero) | Ley 1480, art. 47 | dato pendiente |

## B. Números: sí o no por canal (cliente final y distribuidor por separado)

| # | Indicador | Umbral propuesto para escalar | Por qué |
|---|---|---|---|
| B1 | Precio y costo confirmados | 100 % de las filas de la plantilla con `confirmado = sí`, incluido si el precio lleva IVA | Sin esto, la contribución es una adivinanza |
| B2 | **CM1 por pedido** (antes de captación) | **> 0** en cada producto y canal pautado, contando entrega y comisión | Si cada venta pierde, la pauta multiplica la pérdida |
| B3 | Ticket mínimo vs. costo fijo por pedido | (entrega + frío + cargo fijo de la pasarela) **≤ 25 % del ticket neto** | Los pedidos chicos no pagan su propia entrega (ver 02 §3 y §4) |
| B4 | **CAC máximo permitido** | CAC ≤ CM1 × k, donde **k** es el plazo de payback que acepte la gerencia. Propuesta inicial: **k ≤ 2 pedidos** mientras no haya recompra medida | El plan pide que la gerencia fije el plazo según su caja |
| B5 | Recompra medida | Al menos 1 cohorte de 20 o más clientes nuevos con su ventana de 30 o 60 días cumplida, y la **tasa r observada**, no supuesta | El LTV sin r medido es hipótesis |
| B6 | Payback con r real | CM1 × (1 + r + r²…) ≥ CAC dentro del plazo k | Confirma B4 con datos |
| B7 | Capacidad | Kilos extra que traería la pauta ≤ capacidad libre semanal (BL-036) y materia prima asegurada (BL-039) | No pautar lo que no se puede producir |
| B8 | Caja y cartera | Cartera vencida conocida (BL-040) y la pauta del mes cabe en caja **sin** contar cobros vencidos | Las ventas a crédito no pagan pauta |
| B9 | Servicio | 95 % o más de entregas puntuales y de pedidos completos (umbral del plan) | Si se escala con un mal servicio, la recompra se pierde |
| B10 | Atribución | Cada venta registra su origen (BL-021) | Sin origen no hay CAC por canal |

## C. Regla de decisión (propuesta)

- **Escalar:** todos los puntos de A en verde, y B1, B2, B3, B4, B7, B8 y B10 en verde. B5 y B6 pueden escalar de forma gradual, a +25 % de presupuesto por ciclo, mientras se mide la recompra.
- **Ajustar oferta, no presupuesto:** si B2 o B3 fallan, la solución es precio, ticket mínimo, combos o la forma de entrega, no más pauta.
- **Detener:** si el CM2 acumulado de la cohorte empeora dos ciclos seguidos sin señal de recompra, o si cae cualquier punto de A.

## D. Datos que faltan para dar un sí o un no (hoy, 10 de noviembre de 2026)

Precios confirmados con IVA (BL-005) · costo por kg de 2 productos o más (BL-025) · costo real de entrega en Bogotá · conservación del producto terminado · comisiones reales del medio de pago usado · régimen tributario de la empresa · números de registro ICA · gasto de pauta y clientes nuevos por periodo (CAC) · primera cohorte de recompra · capacidad libre semanal · cartera vencida.

**Conclusión de hoy:** con los datos del repositorio **no se puede dar el sí** para escalar pauta. Se puede correr un piloto con tope de gasto (BL-044) mientras se llenan los puntos A y B1 a B3.
