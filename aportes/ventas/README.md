# Aporte de Ventas · Canívoros

Versión 1 · 10 nov 2026 · **Borrador.** Lo aprueba Andrés. Nada de esto se ha enviado a clientes.

Este aporte no repite lo que ya existe. El repo ya tiene guiones de WhatsApp, objeciones, seguimiento, recompra y métricas en E01, E02 y `branding/03-mensajes.md`. Aquí va lo que falta para **vender mejor en la conversación**:

| Archivo | Qué resuelve | Para quién |
|---|---|---|
| [01-reglas-unificadas-del-chat.md](01-reglas-unificadas-del-chat.md) | E01, E02 y branding dan instrucciones distintas para la misma situación. Propone una sola regla por caso. | Andrés decide; Omar aplica |
| [02-descubrimiento-spin.md](02-descubrimiento-spin.md) | Preguntas para entender qué necesita la persona antes de recomendar. Hoy solo se pregunta zona, perro y qué come. | Omar y quien atienda WhatsApp |
| [03-entrenamiento-y-rubrica.md](03-entrenamiento-y-rubrica.md) | Juegos de rol, una rúbrica para revisar chats y una práctica semanal de 20 minutos. | Andrés entrena; Omar practica |

## Fuentes y supuestos

### Hechos (con fuente)

Revisión de `develop` en el commit `9838919`, 10 nov 2026.

- Omar atiende WhatsApp y cierra la venta. La responsable factura. Hoy Omar pide nombre, cédula, teléfono y correo para facturar. Fuente: `erp.md`, secciones «Flujo actual de pedidos» y «Cómo se gestiona hoy una venta».
- La confianza y la trayectoria de Omar con perros son el activo comercial principal. Fuente: `erp.md`, sección «Comercialización y posicionamiento».
- Jul–oct 2026: los criadores pesan cerca del 52 % de los ingresos y los clientes que repiten mueven cerca del 87 % de los kilos. Son cifras *sin depurar*. Fuente: `embudos/E01-canivoros-tres-motores-recompra/embudo.md` §2.
- Hay pedidos de criadores de 40 a 520 kg. Fuente: `backlog/BL-043-…md`.
- Productos mencionados: chorizos y hamburguesas horneados, de pollo, cerdo, salmón y ternera. Precios y unidades **no confirmados**. Fuente: `erp.md`, sección «Catálogo mencionado», y `backlog/BL-005-…md`.
- La responsable dice que los chorizos pueden deteriorarse después de abiertos y que un paquete puede ser grande para un perro pequeño. Fuente: `erp.md`, sección «Aspectos comerciales que la responsable quiere estudiar».
- La responsable considera difícil cambiar a gatos acostumbrados al concentrado. Fuente: `erp.md`, sección «Producto para gatos».
- Hay tres números de WhatsApp publicados y no hay uno comercial definido. Fuente: `CANIVOROS-REFERENCIA-EMPRESA.md` y `backlog/BL-059-…md`.
- Afirmaciones prohibidas hasta tener respaldo. Fuente: E01 §5.4 y `branding/03-mensajes.md` §5 (rama `branding`).

### Lo que no se pudo leer

- Instagram de la marca y de Friskies Brasil: piden iniciar sesión (intento del 10 nov 2026). No uso nada de ahí. El análisis de Friskies está en `branding/06-analisis-competidor-friskies.md` (rama `branding`).
- No abrí `ventas_canivoros_2026.xlsx` ni chats reales. No hay datos de clientes en este aporte.

### Hipótesis (por validar)

- **H1.** Parte de las consultas no compra porque nadie entiende qué necesita la persona: se cotiza sin preguntar o se pregunta sin cotizar. Se valida con BL-059.
- **H2.** Unificar las reglas del chat reduce errores (promesas no respaldadas, seguimientos de más) sin bajar las ventas.
- **H3.** Con los criadores, una conversación de descubrimiento antes de ofrecer una condición (BL-043) produce una oferta que sí aceptan.
- **H4.** Practicar 20 minutos por semana mejora el puntaje de la rúbrica en los chats reales.

### Datos que faltan

Todo lo marcado **[POR CONFIRMAR CON SEBASTIÁN/ANDRÉS]**. Los más importantes: precios y presentaciones vigentes (BL-005), guía de raciones (BL-041), conservación por producto, número de registro ICA, número comercial único y datos mínimos de facturación.

## Reglas de este aporte

- Los guiones son ilustrativos. Andrés y Sebastián deciden y envían.
- Nada de afirmaciones de salud. Si hay síntomas o una condición clínica, se deriva al veterinario y se pausa la venta.
- Sin urgencia falsa, sin descuentos ni regalos no aprobados.
- No se suben al repo nombres, teléfonos ni chats.
