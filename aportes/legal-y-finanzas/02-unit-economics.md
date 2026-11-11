# 02 · Unit economics por pedido, producto y canal

> Las definiciones vienen del [plan Bogotá](../../CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md), en la sección de indicadores: contribución antes y después de captación, CAC y recompra a 30 o 60 días. Aquí se convierten en una plantilla que se puede llenar. **No tenemos costos reales de Canívoros**, así que cada costo es un *dato pendiente*. Los ejemplos están marcados como **EJEMPLO** y no se deben usar para decidir.

## 1. Datos que sí existen (hechos del repositorio)

| Dato | Valor | Fuente | Estado |
|---|---|---|---|
| Precio al público, chorizo pollo y salmón 500 g | 14.000 | [erp.md §5.1](../../erp.md) | Relato; falta confirmar la moneda (se presume COP) y si incluye IVA |
| Precio a distribuidor, mismo producto | 9.800 | ídem | ídem |
| Público y distribuidor, hamburguesa de pollo 500 g | 5.000 / 3.500 | ídem | ídem |
| Público y distribuidor, ternera 500 g | 6.000 / 4.500 | ídem | ídem |
| Público y distribuidor, Gatívoros salmón y cerdo 500 g | 16.000 / 11.200 | ídem | ídem |
| Hamburguesa de cerdo 500 g | público 5.000; distribuidor "35.000" | ídem | Inconsistente. [BL-005](../../backlog/BL-005-confirmar-precios-unidades-y-catalogo-definitivo.md) registra una corrección a 3.500, con la unidad por confirmar |
| Venta por volumen (criadores), cerdo y pollo | 6.200 por kg, mínimo 40 kg | [erp.md §5.2](../../erp.md) | Relato |
| Canales del Excel de ventas | "cliente" (lb), "almacén" (lb), "criador" (kg) | `ventas_canivoros_2026.xlsx` | Hay kilos y libras, pero no precios |
| Costos, mermas, entrega, CAC | — | — | **Desconocidos** |

## 2. Fórmulas, por pedido

Todo en COP y por pedido entregado. Las letras son las columnas de [unit-economics-plantilla.csv](unit-economics-plantilla.csv).

```
P  = precio cobrado al cliente (IVA incluido)
N  = ingreso neto sin IVA                    = P / (1 + tasa_IVA)      # tasa_IVA = 5 % hoy (ver 01)
D  = descuentos o promociones del pedido

Costos variables por pedido
  I  = ingredientes (materia prima por kg producido × kg del pedido, incluida la merma de proceso)
  E  = empaque y etiqueta
  M  = mano de obra variable (si se paga por lote o turno; si es fija, va en costos fijos)
  F  = cadena de frío (geles, nevera, energía atribuible) — solo si aplica
  L  = entrega de última milla (lo que paga Canívoros, no lo que cobra)
  C  = comisión del medio de pago  = (N_cobrado × %pasarela + fijo) × 1,19   # IVA del 19 % sobre la comisión
  R  = devoluciones o mermas comerciales (promedio por pedido)
  S  = impuesto SIMPLE sobre ingresos, si aplica = N × tarifa_SIMPLE (1,6 % a 4,5 %; ver 01)
  K  = comisión o margen del distribuidor (en el canal distribuidor ya va en el precio)

Contribución antes de captación (CM1)   = N − D − (I + E + M + F + L + C + R + S)
Contribución después de captación (CM2) = CM1 − CAC          # solo en el primer pedido de un cliente nuevo
CAC = gasto de captación del segmento y periodo ÷ clientes nuevos que compraron
      (incluye pauta, muestras, descuentos de bienvenida y horas comerciales; ver plan Bogotá)
```

### Recompra, LTV y payback

```
r  = probabilidad de recompra en el siguiente ciclo (medida en cohortes, BL-022 y BL-060)
n  = pedidos esperados por cliente en el horizonte H (por ejemplo, 6 meses)
     ≈ 1 + r + r² + … (hasta los ciclos que caben en H)
LTV_contribución(H) = CM1 × n          # contribución, no ingresos
Payback (en pedidos) = el menor k en que CM1 × k ≥ CAC
Regla de cuidado: si r no está medido, el LTV es una hipótesis, y no se escala con base en él.
```

### Punto de equilibrio mensual

```
CF = costos fijos del mes (nómina fija, arriendo, energía base del cuarto frío, software, contador…)
Pedidos de equilibrio  = CF ÷ CM1 promedio
Kilos de equilibrio    = CF ÷ (CM1 por kg)
Comprobar siempre: kilos de equilibrio ≤ capacidad disponible (BL-036)
```

## 3. Medios de pago: tarifas públicas reales (consultadas el 10 de noviembre de 2026)

| Medio | Tarifa publicada | Fuente |
|---|---|---|
| Wompi: link de pago, Nequi, Daviplata | 2,65 % + COP 700 + IVA sobre la comisión | [wompi.com, ventas físicas](https://www.wompi.com/es/co/ventas-fisicas/), [planes](https://wompi.com/es/co/planes-tarifas/) |
| Wompi: QR Bre-B | 1 % + IVA | [Bancolombia, 30 de septiembre de 2026](https://prensa.bancolombia.com/noticias/productos-servicios/reduccion-tarifa-qr-wompi) |
| Wompi: tarjeta presencial (app) | 1,98 % + COP 700 + IVA + retenciones | [wompi.com](https://www.wompi.com/es/co/ventas-fisicas/) |
| Bold: link de pago, tarjeta nacional | desde 2,99 % + COP 900 (sin IVA ni retenciones) | [bold.co](https://bold.co/pagos-en-linea/link-de-pago) |
| Bold: PSE y billeteras | desde 2,89 % + COP 900 | ídem |
| Mercado Pago: link, dinero al instante | 3,29 % + COP 800 + IVA | [mercadopago.com.co](https://www.mercadopago.com.co/herramientas-para-vender/link-de-pago) |
| Mercado Pago: link, dinero a 14 días | 2,79 % + COP 800 + IVA | ídem. Ojo: las preguntas frecuentes de esa misma página muestran los porcentajes sin el cargo de COP 800. Confírmalo al abrir la cuenta. |

**Cuánto pesa la comisión según el ticket.** El cálculo usa las tarifas de arriba y un IVA del 19 % sobre la comisión. No incluye retenciones. Los tickets son precios relatados en erp.md o múltiplos de ellos, y siguen pendientes de confirmar.

| Ticket | Wompi link | Wompi QR Bre-B | Bold link | Mercado Pago (al instante) |
|---:|---:|---:|---:|---:|
| 14.000 (1 chorizo 500 g) | 1.274 (9,1 %) | 167 (1,2 %) | 1.569 (11,2 %) | 1.500 (10,7 %) |
| 16.000 (1 Gatívoros 500 g) | 1.338 (8,4 %) | 190 (1,2 %) | 1.640 (10,3 %) | 1.578 (9,9 %) |
| 50.000 (EJEMPLO de combo) | 2.410 (4,8 %) | 595 (1,2 %) | 2.850 (5,7 %) | 2.910 (5,8 %) |
| 248.000 (40 kg × 6.200, criador) | 8.654 (3,5 %) | 2.951 (1,2 %) | 9.895 (4,0 %) | 10.661 (4,3 %) |

**Qué hacer con esto:**

- **Los cargos fijos castigan los pedidos chicos.** Ofrece QR Bre-B o transferencia como opción por defecto en WhatsApp y deja el link para quien lo pida.
- **Fija un ticket mínimo o arma combos** que diluyan el cargo fijo y la entrega.
- **Si se cobra con link a distribuidores y criadores**, la comisión pesa entre el 3,5 % y el 4,3 %. Negocia transferencia directa.
- **La transferencia bancaria directa** no tiene comisión de pasarela, pero cuesta tiempo de conciliación. Ese costo ya aparece en el flujo actual, donde se recibe la consignación ([erp.md](../../erp.md)).

## 4. EJEMPLO ilustrativo (no son datos de Canívoros)

> Todos los costos de este ejemplo son **inventados para mostrar el cálculo**. Reemplázalos con BL-025 y BL-055. El precio es el relatado en erp.md, y suponemos que incluye IVA.

Pedido de 2 chorizos de pollo y salmón de 500 g, cliente final en Bogotá, pagado con link de Wompi:

| Concepto | Cálculo | COP |
|---|---|---:|
| P (cobrado, IVA incluido) | 2 × 14.000 | 28.000 |
| N (sin IVA del 5 %) | 28.000 ÷ 1,05 | 26.667 |
| I + E + M (EJEMPLO: 40 % de N) | supuesto | −10.667 |
| F (EJEMPLO) | supuesto | −1.500 |
| L (EJEMPLO: igual a la tarifa pública de Bigdog, ver 01 §4) | supuesto | −10.000 |
| C (Wompi link sobre 28.000) | (28.000 × 2,65 % + 700) × 1,19 | −1.716 |
| R (EJEMPLO: 3 % de N) | supuesto | −800 |
| S (SIMPLE 1,6 %, si aplica) | 26.667 × 1,6 % | −427 |
| **CM1** | | **≈ 1.557** |
| CAC (EJEMPLO de 35.000, mismo valor que el ejemplo del plan Bogotá) | supuesto | −35.000 |
| **CM2 del primer pedido** | | **≈ −33.443** |
| Payback | 35.000 ÷ 1.557 | **≈ 23 pedidos** |

**Lectura:** con esos supuestos, la entrega se come casi toda la contribución de un pedido chico y ningún CAC razonable se recupera. Si el mismo cliente comprara 4 kg (8 paquetes) con una sola entrega, CM1 subiría a unos COP 43.000 por pedido con los mismos supuestos (la entrega, el frío y el cargo fijo de la pasarela se pagan una sola vez por pedido), y el payback bajaría a 1 pedido. **El tamaño del pedido y el costo de entrega probablemente importen más que la pauta.** Hay que confirmarlo con datos reales antes de decidir.

## 5. Cómo llenar la plantilla

1. Una fila por **producto × canal** (cliente final, distribuidor o almacén, criador por volumen).
2. Llena primero los precios confirmados (BL-005) y marca `confirmado = sí/no`.
3. Saca el costo por kg de un lote real (BL-025 y BL-055): ingredientes, merma, kg obtenidos y horas.
4. Agrega la entrega real de las últimas 10 entregas a Bogotá (BL-008).
5. Deja `desconocido` donde no haya dato. No pongas cero.
