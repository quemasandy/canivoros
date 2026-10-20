### 1. Compras y proveedores

- ¿Quién decide qué comprar y en qué momento?
- ¿Cómo calculan la cantidad necesaria?
- ¿Compran por kilos, unidades, litros u otra medida?
- ¿Un ingrediente puede tener varios proveedores?
- ¿Los precios cambian según cantidad, temporada o proveedor?
- ¿Pagan anticipado, de contado o a crédito? ¿Qué plazos manejan?
- ¿Quién aprueba las compras?
- ¿Qué hacen cuando un proveedor entrega tarde, incompleto o con mala calidad?

### 2. Recepción y almacenamiento

- ¿Quién recibe y verifica la materia prima?
- ¿Comparan lo recibido con lo pedido y facturado?
- ¿Registran peso, temperatura, lote, vencimiento y estado?
- ¿Qué condiciones hacen que rechacen una entrega?
- ¿Dónde guardan cada ingrediente y qué condiciones necesita?
- ¿Cómo saben cuánto inventario queda?
- ¿Cómo deciden qué lote utilizar primero?
- ¿Registran pérdidas por vencimiento, deterioro o diferencias de peso?




Bueno, primo, en cuanto a la materia prima, conseguirla es bastante difícil. Como te explicaba, no es que sea ilegal, sino que se trata de subproductos que, aunque no se destinan al consumo humano o no se comercializan habitualmente en ese mercado, pueden aprovecharse para nuestro proceso productivo.

¿Qué utilizamos? Principalmente, cabezas de pollo, barriga de salmón —que tiene un sabor un poco amargo y, por eso, la gente no suele consumirla—, huesos de cerdo, específicamente la canilla, y vísceras de cerdo.

Trabajamos con varios proveedores, cada uno de los cuales nos suministra diferentes materias primas. Todo llega congelado a la planta y el suministro no es constante, porque depende de la disponibilidad de cada proveedor. Hay ocasiones en las que algunos tienen producto y otros no, por lo que debemos adaptarnos continuamente a esa disponibilidad.

Precisamente por eso contamos con un cuarto frío de gran capacidad. Cuando hay disponibilidad, recibimos cantidades importantes y las almacenamos para tener reservas que nos permitan mantener la operación cuando escasea la materia prima.

Estamos buscando proveedores y recibiendo materia prima permanentemente. Por ejemplo, en el caso del hueso de cerdo, se trata de un subproducto que, de no aprovecharse, podría terminar desechándose. Los establecimientos tendrían que gestionar su disposición y asumir los costos correspondientes. Nosotros, en cambio, lo recibimos y también les pagamos por él a un precio que les resulta favorable.

Así logramos aprovechar materiales que, de otra manera, podrían convertirse en residuos, al tiempo que generamos un beneficio económico para nuestros proveedores y aseguramos, en la medida de lo posible, el abastecimiento de nuestra planta.



Bueno, primo, en cuanto a la materia prima, conseguirla es bastante difícil. Como te explicaba, no es que sea ilegal, sino que se trata de subproductos que, aunque no se destinan al consumo humano o no se comercializan habitualmente en ese mercado, pueden aprovecharse para nuestro proceso productivo.

¿Qué utilizamos? Principalmente, cabezas de pollo, barriga de salmón —que tiene un sabor un poco amargo y, por eso, la gente no suele consumirla—, huesos de cerdo, específicamente la canilla, y vísceras de cerdo.

Trabajamos con varios proveedores, cada uno de los cuales nos suministra diferentes materias primas. Todo llega congelado a la planta y el suministro no es constante, porque depende de la disponibilidad de cada proveedor. Hay ocasiones en las que algunos tienen producto y otros no, por lo que debemos adaptarnos continuamente a esa disponibilidad.

Precisamente por eso contamos con un cuarto frío de gran capacidad. Sin embargo, no manejamos lotes antiguos ni almacenamos la materia prima durante largos periodos. En la práctica, todo lo que llega un viernes se procesa durante la semana siguiente y, a más tardar, el viernes siguiente ya no queda materia prima de ese ingreso. Es decir, la materia prima se consume prácticamente de inmediato y no trabajamos con producto viejo.

Estamos buscando proveedores y recibiendo materia prima permanentemente. Por ejemplo, en el caso del hueso de cerdo, se trata de un subproducto que, de no aprovecharse, podría terminar desechándose. Los establecimientos tendrían que gestionar su disposición y asumir los costos correspondientes. Nosotros, en cambio, lo recibimos y también les pagamos por él a un precio que les resulta favorable.

Así logramos aprovechar materiales que, de otra manera, podrían convertirse en residuos, al tiempo que generamos un beneficio económico para nuestros proveedores y aseguramos, en la medida de lo posible, el abastecimiento de nuestra planta.


---
$$$$

Estas respuestas permiten definir **el catálogo de materias primas, la relación con proveedores y el seguimiento de las entradas al cuarto frío**. Todavía faltan datos para establecer las reglas de compra, aceptación y pago.

Tomaría la segunda versión como una aclaración de la primera: **el cuarto frío tiene gran capacidad, pero la materia prima normalmente se procesa durante la semana siguiente a su recepción**. No asumiría que almacenan reservas por periodos largos.

### Información que ya podemos aprovechar

| Información obtenida | Utilidad para el ERP |
|---|---|
| Utilizan cabezas de pollo, barriga de salmón, canilla y vísceras de cerdo | Crear un catálogo inicial de materias primas; confirmar si las vísceras se registran juntas o por tipo |
| Trabajan con varios proveedores | Crear proveedores y relacionarlos con las materias primas que pueden suministrar |
| La disponibilidad cambia y el suministro no es constante | Registrar ofertas y disponibilidad antes de convertirlas en compras |
| Toda la materia prima llega congelada | Incorporar estado de recepción y controles de temperatura, cuyos criterios todavía deben definirse |
| Almacenan en un cuarto frío | Crear una ubicación de inventario y registrar sus entradas y salidas |
| Los ingresos suelen consumirse durante la semana siguiente | Medir tiempo de permanencia y detectar existencias que superan el comportamiento habitual |
| Buscan proveedores permanentemente | Mantener un registro de proveedores potenciales y su evaluación |
| Pagan por los subproductos recibidos | Registrar compra, costo y obligación de pago; no tratarlos como donaciones o entradas gratuitas |

### Cómo se traduce en un flujo del sistema

**Disponibilidad del proveedor → compra acordada → recepción → almacenamiento → salida a producción.**

Cada paso debe conservar información diferente:

| Registro | Datos que conviene guardar |
|---|---|
| **Disponibilidad ofrecida** | Proveedor, materia prima, cantidad disponible, precio ofrecido, fecha y condiciones de entrega |
| **Compra** | Cantidad acordada, unidad, precio, transporte, fecha prevista y condiciones de pago |
| **Recepción** | Fecha real, materia prima, cantidad recibida y aceptada, responsable, condición y resultado de revisión |
| **Ingreso al inventario** | Identificador interno del lote, proveedor, recepción de origen, ubicación y cantidad |
| **Salida a producción** | Lote de materia prima utilizado, cantidad, fecha y lote de fabricación de destino |

**Aunque consuman todo rápidamente, necesitan identificar cada ingreso.** Así podrán reconstruir qué materia prima de qué proveedor se utilizó en un producto terminado. Si el proveedor no identifica sus lotes, el ERP puede asignar un identificador interno de recepción, sin presentarlo como un lote del proveedor.

### Funcionalidades especialmente útiles para esta operación

- **Disponibilidad por proveedor:** consultar quién ofrece cada materia prima y cuándo confirmó que tenía producto.
- **Inventario por ingreso:** conocer cuánto queda de cada recepción, incluso si reciben el mismo ingrediente varias veces por semana.
- **Antigüedad de existencias:** mostrar días desde la recepción. El consumo semanal descrito es una práctica observada; todavía no es una fecha de vencimiento ni un límite de conservación.
- **Comparación de proveedores:** medir diferencias entre cantidades acordadas y aceptadas, puntualidad, rechazos y costo por kilo aceptado.
- **Abastecimiento frente a producción:** comparar las existencias y compras confirmadas con lo necesario para fabricar, cuando estén definidas las recetas y los rendimientos.

La disponibilidad irregular **no debe convertirse automáticamente en permiso para cambiar ingredientes o recetas**. Esa decisión necesita sus propias reglas y responsables.

### Preguntas que siguen pendientes

Para cerrar estos dos módulos, preguntaría:

1. **¿Quién compra y quién autoriza?** ¿Hay un presupuesto o límite de compra?
2. **¿Cómo acuerdan una compra?** ¿Por WhatsApp, llamada u orden escrita?
3. **¿En qué unidad compran y cómo pesan?** ¿Descuentan empaque, hielo u otros componentes?
4. **¿Qué cantidades y precios maneja cada proveedor?**
5. **¿Quién recoge o entrega y quién paga el transporte?**
6. **¿Cómo pagan y cuándo vence cada obligación?**
7. **¿Qué revisan al recibir y cuáles son los criterios de aceptación o rechazo?**
8. **¿Qué identificación, fechas y documentos entrega el proveedor?**
9. **¿Cómo seleccionan qué ingreso utilizar primero?**
10. **¿Qué hacen si una materia prima sigue disponible después de la semana habitual?**
11. **¿Registran descongelación, pérdidas, devoluciones o diferencias de peso?**
12. **¿Cuál es la capacidad útil del cuarto frío y cómo controlan su ocupación?**

También aparece una diferencia importante con el documento anterior: allí se mencionaba **“sin subproductos”**, mientras que esta explicación describe materias primas como subproductos. Conviene aclarar y corregir esa descripción. Para el ERP, la ficha técnica debe reflejar **el ingrediente real utilizado y su especificación**, independientemente del lenguaje comercial.


1 se compra lo que nos vendan el acuerdo con los proveedores es traiganos lo que tengan hay que tener en cuenta que es un subproducto por lo tanto no es ilimitado si necesitamos mas hay que traer mas proveedores


---
$$$$

# Canívoros — levantamiento operativo para el ERP

Este documento organiza las 13 respuestas transcritas de WhatsApp por proceso de la empresa. La fuente es la transcripción proporcionada, sin revisión de los audios originales. Los datos representan prácticas descritas, no procedimientos formalizados ni requisitos aprobados. Las cifras son aproximadas, salvo confirmación posterior.

## 1. Compras y abastecimiento

### Práctica descrita

Existen dos procesos de compra. En el primero, los proveedores ofrecen o entregan materia prima según su disponibilidad. Anteriormente, las entregas se coordinaban por WhatsApp. Actualmente, los proveedores habituales llegan principalmente los viernes y la empresa recibe el material disponible. Los empleados pesan la carga e informan la cantidad al responsable del pago.

En el segundo proceso, el responsable supervisa el consumo de bolsas, empaques, materiales de limpieza y otros insumos, y realiza compras aproximadamente una vez por semana.

El suministro de materia prima es irregular. La empresa busca proveedores continuamente y adapta las compras a la disponibilidad. Las materias primas mencionadas en la explicación anterior son cabezas de pollo, barriga de salmón, hueso de canilla de cerdo y vísceras de cerdo. Los nombres comerciales y las especificaciones de cada material deben confirmarse.

### Cantidades y precios mencionados

| Material | Cantidad mencionada | Observación |
| --- | --- | --- |
| Huesos de cerdo | Aproximadamente 300 kg | No quedó clara la frecuencia ni el alcance de esta cantidad |
| Salmón | Aproximadamente 1.000 kg | Se buscan compras mayores para obtener mejores condiciones |
| Pollo | Objetivo de aproximadamente 1.000 kg o más | Depende de la disponibilidad del proveedor |
| Vísceras y otros materiales de cerdo | Cantidad disponible para entregar | Se indica que el precio no varía por volumen, pero debe confirmarse a qué materiales aplica |

La respuesta sobre los precios de 500 kg y una tonelada contiene una frase confusa. La interpretación probable es que el precio por kilogramo disminuye al aumentar el volumen de pollo y salmón. No se confirmaron precios ni escalas de descuento.

Estas cantidades no deben sumarse como una compra semanal estándar: no se estableció que correspondan al mismo periodo o a la misma entrega.

### Implicaciones propuestas para el ERP

Distinguir las compras de materia prima de las compras de otros insumos. Permitir tanto una compra planificada como el registro de una entrega no programada, sujeta a verificación. Relacionar cada proveedor con los materiales que suministra, sus precios con fecha de vigencia y las condiciones de compra. Guardar por separado la cantidad informada por el proveedor, la cantidad pesada y la cantidad aceptada.

### Por confirmar

Quién decide y aprueba las compras; identificación de los proveedores; unidad y precio de cada material; frecuencia de las cantidades mencionadas; límites de compra; descuentos por volumen; y tratamiento de las entregas no acordadas previamente.

**Origen:** respuestas 2 y 4, con contexto de la explicación anterior sobre materias primas.

## 2. Transporte y pago

### Práctica descrita

Los proveedores transportan la mercancía hasta la fábrica y, según lo explicado, no cobran el flete por separado debido a las cantidades compradas. El pago es inmediato después del pesaje y la recepción.

La ausencia de un cobro separado de flete no demuestra que el precio del material no incluya un costo logístico.

### Implicaciones propuestas para el ERP

Registrar el responsable del transporte, el flete cobrado por separado y las condiciones comerciales. Vincular el pago con la compra y la recepción correspondientes, incluyendo importe, fecha, medio de pago y comprobante. Mantener la distinción entre recibido, aceptado y pagado, aunque estos eventos ocurran el mismo día.

### Por confirmar

Quién realiza los pagos; medios utilizados; existencia de factura, recibo u otro documento; verificación entre el peso aceptado y el importe pagado; y posibles excepciones al pago inmediato.

**Origen:** respuestas 5 y 6.

## 3. Recepción e inspección

### Práctica descrita

Los empleados pesan el material en kilogramos. También verifican que esté frío, su coloración y su aspecto de frescura. Existe preocupación por evitar la recepción de material inadecuado ofrecido como materia prima aprovechable.

La transcripción menciona una apariencia rosada, pero no aclara a qué material corresponde. Tampoco se informó si la temperatura se mide con un instrumento, si se registra el resultado o si existe una persona formalmente responsable de aprobar la recepción.

En la explicación anterior, los materiales se describieron como entregados congelados. En esta transcripción también aparecen las palabras «frío» y «fresco». Debe aclararse el estado esperado de recepción de cada material: «fresco» podría haberse utilizado para describir su calidad y no su temperatura.

### Identificación

Según la respuesta, el material llega sin etiqueta. Esto no permite concluir si existe o no otra identificación o documentación del proveedor.

### Implicaciones propuestas para el ERP

Crear un registro de recepción con proveedor, material, fecha y hora, pesos informados y verificados, responsable y resultado de la inspección. Contemplar aprobación, rechazo o evaluación pendiente. Las condiciones aceptables y los límites de temperatura deben definirse antes de configurar reglas automáticas.

Generar una identificación interna por ingreso y material, vinculada al lote del proveedor cuando exista. La identificación interna no debe presentarse como una identificación emitida por el proveedor. Permitir adjuntar documentos, fotografías y observaciones.

### Por confirmar

Peso bruto, tara y peso neto; instrumentos utilizados; criterios de aceptación por material; documentos recibidos; tratamiento de rechazos parciales o totales; y posibles lotes o fechas de origen informados por el proveedor.

**Origen:** respuestas 3, 7 y 8.

## 4. Almacenamiento y movimientos

### Práctica descrita

El cuarto frío tiene una capacidad declarada de seis toneladas. La empresa informa entradas de aproximadamente cuatro toneladas de materia prima por semana y una alta rotación. El procesamiento suele comenzar el mismo día de la llegada o al día siguiente, pasando por los molinos.

La mayor parte de la materia prima se consume rápidamente. Se mencionan permanencias ocasionales de ocho a diez días. Por tanto, no corresponde establecer el consumo en un máximo de siete días como una regla sin excepciones.

Los materiales se separan en canastillas de diferentes colores:

| Material | Color indicado |
| --- | --- |
| Pollo | Azul |
| Cerdo | Verde |
| Salmón | Blanco |

Anteriormente, se utilizaba primero el material ubicado más cerca de la puerta. Actualmente, se destaca la circulación rápida del inventario, sin describir una regla formal de selección por fecha de ingreso o vencimiento.

### Conservación e incidentes

El entrevistado describe el almacenamiento como «supercongelación» y afirma que el material podría permanecer un año en esas condiciones. Esta afirmación no establece una vida útil técnica y no debe convertirse en un plazo automático en el ERP. Faltan la temperatura, las especificaciones de los materiales y las condiciones documentadas de conservación.

También se mencionan fallas del cuarto frío que ocasionaron el descarte de material. No se informaron frecuencia, cantidades perdidas ni criterios utilizados para decidir el descarte.

### Control actual

No se describe una medición sistemática de la ocupación. La percepción del inventario y de la operación se apoya en el movimiento frecuente, los pagos a proveedores y las ventas posteriores. Estos valores financieros no sustituyen el saldo físico por material.

### Implicaciones propuestas para el ERP

Controlar ingresos, transferencias, consumo y pérdidas por material e identificación interna. Registrar el paso por la molienda como una etapa de producción o transformación, conservando la relación entre la materia prima recibida y el material procesado. La separación por colores ayuda a organizar los materiales, pero no identifica el ingreso de origen.

Mostrar existencias, antigüedad de los ingresos y peso almacenado simultáneamente. Las cuatro toneladas recibidas por semana representan un flujo; las seis toneladas representan la capacidad declarada. No deben dividirse estas cifras para calcular una tasa de ocupación, porque la ocupación depende de las entradas y salidas a lo largo del tiempo.

Contemplar el registro de fallas de refrigeración, materiales afectados y descartes. La política de selección del inventario debe definirse antes de automatizarla.

### Por confirmar

Capacidad útil del cuarto frío, ubicaciones internas, temperaturas utilizadas y medidas, registros de conservación, criterios de vida útil, identificación durante la molienda, regla de selección de materiales e historial de pérdidas.

**Origen:** respuestas 1, 9, 10 y 12. La respuesta 1 está incompleta y no permite establecer una regla independiente de consumo.

## 5. Producción, pesaje y rendimiento

### Práctica descrita

La materia prima se recibe en kilogramos y los productos se venden por kilogramos y libras. Debe confirmarse el valor en gramos de la unidad comercial «libra» antes de registrar conversiones.

Para un ingreso de 50 kg, se mencionó una pérdida aproximada de 4 a 6 kg. La empresa utiliza 5 kg como referencia y estima una salida de 45 kg. En este ejemplo, el rendimiento de referencia es del 90 %, con una pérdida del 10 %. El intervalo mencionado equivale a pérdidas del 8 % al 12 %, pero no constituye una tasa confirmada para todos los productos o etapas.

La explicación sobre el peso de los empaques, las hamburguesas y el secado en el horno es ambigua. No permite determinar el punto exacto del pesaje ni atribuir toda la diferencia de peso al horno.

### Implicaciones propuestas para el ERP

Separar el rendimiento previsto del rendimiento medido. Registrar, por lote de producción, los ingredientes realmente consumidos, la cantidad producida, el producto en proceso, las pérdidas y el destino de los materiales. Diferenciar pérdidas del proceso, descartes, diferencias de pesaje y peso de empaque, de acuerdo con los procedimientos definidos por la empresa.

El sistema no debe registrar automáticamente 5 kg de pérdida por cada 50 kg sin una medición o un cierre de producción. El valor mencionado puede servir como estimación inicial, identificada como tal.

### Por confirmar

A qué recetas aplica el ejemplo; si los 50 kg representan todos los ingredientes de la mezcla; puntos de pesaje; efecto de la molienda y del horno; peso neto y bruto; recetas; tiempos; y cantidad por presentación.

**Origen:** respuesta 3.

## 6. Devoluciones y consumo del criadero

### Práctica descrita

Las devoluciones se consideran poco frecuentes. Según la explicación, el alimento devuelto se destina a los perros del criadero y se descuenta de la cantidad que la fábrica les suministraría.

Se mencionó una referencia de 130 kg mensuales para los perros. Como ejemplo, las devoluciones podrían reducir el retiro adicional a 120 kg o 115 kg. La cantidad de perros varía, lo que dificulta el control. También se hace referencia a una mensualidad pagada por el criadero a la empresa de alimentos y a descuentos relacionados con las devoluciones.

No quedó claro si el descuento se realiza solamente en kilogramos, en dinero o en ambos, ni quién recibe el ajuste financiero de la venta original. Tampoco se aclararon los motivos y las condiciones de los productos devueltos.

### Implicaciones propuestas para el ERP

Separar tres eventos: devolución comercial del cliente, evaluación y destino físico del producto, y suministro o cobro al criadero. Cada evento debe tener cantidad, motivo, responsable y vínculo con el movimiento de origen cuando esté disponible.

No automatizar la liberación de cualquier devolución para consumo. La condición del producto y la decisión sobre su destino deben registrarse antes de la salida. Mantener el inventario devuelto separado del inventario disponible hasta tomar esa decisión.

Registrar al criadero como destinatario identificable. Confirmar si la relación es una venta, una transferencia u otra operación antes de definir su tratamiento. Evitar descontar la misma devolución dos veces, una del suministro físico y otra del cobro, sin una regla explícita.

### Por confirmar

Quién devuelve; motivos; condición y trazabilidad del producto; decisión sobre su destino; restitución al cliente; naturaleza de la mensualidad; precio del suministro; y fórmula del descuento al criadero.

**Origen:** respuesta 11.

## 7. Control financiero e inventario

### Práctica descrita

El entrevistado relaciona el pago de la materia prima con el cobro de las ventas durante la semana siguiente. Esto indica seguimiento de la circulación del dinero, pero no demuestra un método formal de cálculo de costos o conciliación física del inventario.

El fragmento «si pagué en este mes tres meses en materia prima» parece contener un error de transcripción. La mención posterior a nueve o diez millones en ventas no permite determinar con seguridad el importe de compra, la moneda expresada en el audio o una relación fija entre costo e ingresos. No debe calcularse ningún indicador a partir de esta frase sin confirmación.

### Implicaciones propuestas para el ERP

Mantener controles separados de inventario físico, costos, ventas, cuentas por pagar y cobros. Relacionarlos mediante documentos y movimientos. Una venta registrada, un importe cobrado y una salida física son eventos diferentes.

### Por confirmar

Texto correcto de la respuesta; periodo, importes y moneda del ejemplo; significado de «ya me pagaron»; costos considerados; y forma actual de verificar pagos y cobros.

**Origen:** respuesta 12.

## 8. Máquinas y mantenimiento

### Práctica descrita

El funcionamiento y la confiabilidad de las máquinas se señalaron como el mayor problema de la empresa y la principal causa de interrupción del ciclo operativo.

### Implicaciones propuestas para el ERP

Incluir mantenimiento en el alcance inicial del análisis. Registrar equipos, fallas, paradas, duración, causas identificadas, reparaciones, repuestos, costos e impacto en los lotes. El historial permitirá identificar qué equipos interrumpen más la producción.

No asumir que existe un plan preventivo. Construirlo a partir de los equipos, los manuales, las condiciones de uso y los responsables definidos por la empresa.

### Por confirmar

Qué máquinas fallan; frecuencia y duración de las paradas; efectos sobre la producción y la conservación; asistencia disponible; mantenimiento actual; repuestos críticos; y responsables.

**Origen:** respuesta 13.

## 9. Prioridades sugeridas para la próxima conversación

1. Entender las fallas de las máquinas y del cuarto frío, pues ya se asociaron con interrupciones y pérdidas.
2. Acompañar una recepción real: material, proveedor, peso, inspección, identificación y pago.
3. Reconstruir un lote real de fabricación, vinculando los ingredientes utilizados con el producto final y su rendimiento.
4. Aclarar las devoluciones y los descuentos al criadero, separando movimientos físicos y financieros.
5. Confirmar precios, cantidades, unidades y documentos para completar el diseño de compras y costos.

## 10. Límites de este levantamiento

Todavía no están definidos los responsables y niveles de aprobación, los criterios técnicos de aceptación, las recetas, la vida útil, la conversión de libras, los precios, los proveedores identificados y los procedimientos de descarte. El ERP debe apoyar la formalización de estas decisiones sin presentar hipótesis como reglas existentes.

La descripción operativa de los subproductos también debe conciliarse con la comunicación anterior de la marca, que mencionaba la ausencia de subproductos. El registro técnico debe representar los materiales realmente utilizados.
