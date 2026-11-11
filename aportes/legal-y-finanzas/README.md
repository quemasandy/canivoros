# Aporte · Legal y Finanzas — Canívoros / Gatívoros

Preparado el 10 de noviembre de 2026 por el especialista de Legal y Finanzas que trabaja para Andrés (Growth Partner).

> **Orientación general, no asesoría legal ni contable.** Antes de decidir, valídalo con un contador público y, si hace falta, con un abogado en Colombia. Las normas y tarifas se consultaron el 10 de noviembre de 2026 y pueden cambiar.

## País de operación: Colombia

Lo dice el propio repositorio:

- La planta está en **Sopó (Cundinamarca)** y el mercado del piloto es **Bogotá** ([README.md](../../README.md), [CANIVOROS-REFERENCIA-EMPRESA.md](../../CANIVOROS-REFERENCIA-EMPRESA.md)).
- La dirección publicada es Transversal 6 # 5 Sur-60, Sopó, y el correo de distribución es `canivorossas@gmail.com`. Eso **sugiere** una S.A.S., pero falta confirmar la razón social y el NIT (dato pendiente).
- Los precios del levantamiento están en pesos colombianos, aunque falta confirmarlo ([erp.md §5](../../erp.md)).

## Qué hay en esta carpeta

| Archivo | Para qué sirve |
|---|---|
| [01-mapa-regulatorio-tributario.md](01-mapa-regulatorio-tributario.md) | Qué exigen el ICA, la DIAN y el Estatuto del Consumidor a un fabricante colombiano de alimento para mascotas. Separa lo verificado de lo que falta confirmar. |
| [02-unit-economics.md](02-unit-economics.md) | Cuentas por pedido y por canal: contribución, CAC, recompra, payback y punto de equilibrio. Incluye las tarifas públicas de Wompi, Bold y Mercado Pago. |
| [unit-economics-plantilla.csv](unit-economics-plantilla.csv) | Plantilla para llenar por producto y canal. Abre en Excel, Google Sheets u Odoo. |
| [03-checklist-antes-de-escalar-pauta.md](03-checklist-antes-de-escalar-pauta.md) | Lista de sí o no con umbrales antes de subir el gasto en Meta u otra pauta. |
| [04-preguntas-abiertas.md](04-preguntas-abiertas.md) | Preguntas para Omar, la responsable de operación y el contador. |

## Lo más importante (hallazgos)

1. **El IVA del alimento para perros y gatos hoy es del 5 %, no del 19 %.** El artículo 468-1 del Estatuto Tributario grava la partida 23.09 al 5 % y la DIAN lo confirmó en el Oficio 906450 de 2022. Hay un proyecto de ley (PL 411 de 2026 Cámara, radicado el 30 de septiembre de 2026) que propone excluirlo del IVA, pero **todavía no es ley**. Falta saber si los precios del catálogo ya incluyen ese IVA.
2. **El registro ICA es doble: uno para el fabricante y uno para cada producto.** La marca dice que tiene registro ICA, pero el repositorio no trae los números. Sin ellos no conviene pautar con ese mensaje. Las golosinas hechas solo de carnaza, cartílago o hueso, sin otro ingrediente, están exentas de registro de producto. Eso podría aplicar a las "orejas" del Excel de ventas, pero hay que confirmarlo.
3. **La etiqueta no puede ser engañosa** (Res. ICA 61252 de 2020, art. 27.1), y la publicidad también responde ante el Estatuto del Consumidor. Los beneficios de salud del sitio necesitan soporte o hay que reformularlos. Esto coincide con BL-016.
4. **En pedidos chicos, el link de pago se come entre el 8 % y el 11 % del ticket.** Un paquete de COP 14.000 pagado con link cuesta entre COP 1.274 (Wompi) y COP 1.569 (Bold), por el cargo fijo por transacción. Con QR Bre-B de Wompi cuesta COP 167 (1,2 %). Conviene un ticket mínimo, combos o cobrar con QR o transferencia.
5. **El costo de entrega puede decidir si un pedido chico es viable.** No conocemos el costo de Canívoros. Como referencia, un competidor de Bogotá publica envío de COP 10.000 (competencia/competencia-2026-11-03.csv, Bigdog/Dogsy). Si Canívoros pagara algo parecido, un pedido de un paquete de COP 14.000 no alcanza a cubrirlo.
6. **Retracto:** en ventas por WhatsApp o web, el consumidor tiene 5 días hábiles para retractarse, pero la ley exceptúa los bienes perecederos o que se deterioran rápido (Ley 1480 de 2011, art. 47). Hay que definir por escrito si el producto entra en esa excepción y publicar una política de cambios.
7. **El régimen tributario de la empresa es desconocido.** Si estuviera en el Régimen Simple, la tarifa por actividad industrial o comercial va del 1,6 % al 4,5 % de los ingresos brutos (ET art. 908). Ese porcentaje debe entrar en la contribución porque se paga sobre ventas, no sobre utilidad.

## Cómo encaja con lo que ya existe

- **Usa las definiciones del plan:** la contribución antes y después de captación, el CAC y la recompra a 30 o 60 días vienen de [CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md](../../CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md). No crea métricas nuevas.
- **Alimenta el backlog:** BL-005 (precios), BL-016 (afirmaciones), BL-025 (costo por producto), BL-040 (cartera), BL-044 (criterios antes de experimentar) y BL-028 (decidir cómo crecer).
- **No toca `branding/`.** Lo de claims y etiqueta va como insumo legal para el bot de marca. Este aporte no redacta mensajes.
- **No inventa cifras.** Los únicos precios citados vienen de [erp.md §5](../../erp.md), y todavía son "por confirmar". Los ejemplos están marcados como **EJEMPLO**.
