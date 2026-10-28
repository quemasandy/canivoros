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

# Canívoros — Información del audio

## Organización de la empresa

Canívoros cuenta con tres operarios que se encargan de la producción. La responsable de la empresa se ocupa de facturar, procurar que haya materia prima disponible y recibir los pedidos que le transmite el área comercial.

La empresa funciona con un equipo reducido y no considera viable incorporar más empleados en este momento. Organizar y sistematizar la información permitiría reducir la carga administrativa.

La responsable manifiesta interés en recopilar los datos y dejar organizada la empresa. Explica que muchas de las preguntas sobre el negocio ya las ha respondido a publicistas, profesionales relacionados con el ICA, ingenieros industriales e ingenieros de alimentos, pero la información está repartida y necesita organizarse.

## Información de producción que desea organizar

La responsable quiere registrar y sistematizar información sobre los productos, las recetas, los cambios de receta, las cantidades utilizadas por lote y la cantidad de producto terminado que espera obtener.

En la producción se transforma materia prima, se genera merma y se hornea el producto.

El mantenimiento de maquinaria ocupa una parte importante del tiempo. Es necesario conseguir repuestos, buscar técnicos, reparar equipos y, en ocasiones, fabricar piezas que se rompen.

## Comercialización actual

La empresa vende a través de aproximadamente tres o cuatro puntos de distribución y también mediante amigos, conocidos y contactos personales.

La trayectoria en el mundo de los perros y la relación con perros campeones han contribuido a generar confianza y credibilidad entre los compradores.

La responsable quiere identificar con claridad los productos que entregará a Santiago, sus presentaciones y sus gramajes.

## Aspectos comerciales que la responsable quiere estudiar

La responsable menciona interés en conocer:

- La competencia.
- Los productos similares que existen en el mercado.
- Sus precios y beneficios.
- La población a la que se dirigirán.
- La conveniencia de las presentaciones y gramajes actuales.
- Las presentaciones que podrían venderse mejor o dejar mayor ganancia.

Como ejemplos, menciona estudiar presentaciones de 200, 350 o 700 gramos, en lugar de vender únicamente por libra.

Explica que un paquete puede resultar demasiado grande para una mascota pequeña y que los productos en chorizo pueden deteriorarse después de abiertos.

## Experiencia con el producto prémium para perros

La responsable identifica la receta de pollo y salmón en chorizos como un producto prémium. En el audio menciona un precio aproximado de cinco dólares por libra y señala que llevan alrededor de tres años trabajando en su posicionamiento.

Según su experiencia, son pocos los clientes dispuestos a consumir este tipo de producto y ha sido difícil aumentar sus ventas.

Considera que el alimento para mascotas debe comercializarse de forma masiva. También expresa que algunos compradores reducen el presupuesto destinado a la alimentación del perro cuando tienen otros gastos.

La responsable afirma que sus productos tienen una calidad superior a la de sus competidores y señala que dispone de información sobre proteína, grasa y humedad para realizar comparaciones. Relata haber observado cambios en el pelaje y el peso de los animales que consumen sus productos.

## Distribuidores y objetivos de la empresa

Santiago es mencionado como distribuidor de Canívoros. La responsable también hace referencia a otros distribuidores y expresa que desea que puedan vender de forma autónoma.

Su interés principal es que la empresa produzca, esté organizada y pueda elaborar miles de kilos para cumplir con los pedidos de los distribuidores.

## Propuesta de colaboración

La responsable distingue dos trabajos:

1. Organizar la empresa mediante un sistema para pedidos, materias primas, protocolos y registros. Expresa disposición a pagar de alguna manera por esta organización, que considera un ahorro de gastos operativos.
2. Llevar clientes a Santiago. Propone que el resultado económico de esas ventas se comparta entre Santiago y la persona que consiga los clientes.

También ofrece enviar formatos de Excel para mostrar cómo funciona actualmente la empresa.

## Producto para gatos

La responsable considera que el alimento para gatos podría ser un producto de alta rentabilidad.

En el audio menciona una ganancia de cuatro millones ochocientos mil por la venta de una tonelada de este producto.

Explica que los gatos consumen menos cantidad y que la aceptación varía: a algunos les gusta el alimento y a otros no.

Considera que sería mejor ofrecer una presentación de 200 gramos, porque después de abrir el paquete el producto pierde frescura. Como ejemplo, relata que sus gatos pueden dejar de aceptarlo si lleva dos días abierto.

Según su experiencia, el precio de dieciséis mil pesos por libra no genera tanta resistencia entre compradores de alimento para gatos, porque están acostumbrados a pagar precios elevados.

La responsable considera difícil cambiar la alimentación de gatos acostumbrados desde pequeños al concentrado. Por eso propone dirigirse a personas que acaban de incorporar un gatito al hogar y promover el consumo del producto desde una edad temprana.

En su explicación, destaca la humedad del alimento y relata beneficios que atribuye a su consumo, como cambios en el pelaje y menor cantidad y olor de las heces.

## Inicio de la organización del sistema

La responsable pregunta cómo se empezará a ingresar la información: si se recopilará mediante preguntas, si otra persona la cargará o si recibirá un usuario y una contraseña para hacerlo directamente.

## Registro de ventas y cuentas pendientes

Omar le pasa los clientes a la responsable, quien elabora la factura. Se recibe la consignación y, una vez realizada la entrega, la venta se registra en Excel.

Algunos clientes habituales reciben el pedido y quedan debiendo. Esas cuentas pendientes se identifican en rojo en el archivo.

La responsable explica que el cuadro de Excel contiene cantidades expresadas en kilos y libras. Los precios se manejan por separado en el programa de facturación.

---
$$$$

# Canívoros — Documento de referencia del negocio

**Fecha de elaboración:** 26 de octubre de 2026  
**Fuente:** transcripción y respuestas escritas proporcionadas por la empresa.  
**Estado:** documento inicial para revisión con la responsable de Canívoros.

> Los datos operativos se presentan según lo relatado; no constituyen una auditoría. Las propuestas, interpretaciones y dudas se identifican por separado. Los precios y condiciones deben confirmarse antes de utilizarlos en un sistema o catálogo comercial.

## 1. Descripción de la empresa

Canívoros elabora y comercializa alimentos para mascotas, principalmente perros, y cuenta también con una receta para gatos. Se mencionan productos en forma de chorizos y hamburguesas.

La empresa combina ventas directas con ventas mediante distribuidores. Su responsable desea concentrarse en organizar la producción, aumentar el volumen y cumplir los pedidos de los canales comerciales.

El crecimiento comercial actual se apoya en relaciones personales, recomendaciones y la credibilidad de Omar en el entorno de los perros. No se documenta todavía una investigación sistemática del mercado.

## 2. Equipo y responsabilidades

El equipo está compuesto por cinco personas: Omar, la responsable de la operación y tres operarios.

| Persona o grupo | Responsabilidades relatadas |
|---|---|
| Omar | Atención por WhatsApp, recepción de pedidos, solicitud de datos de facturación y comunicación de facturas y fechas al cliente. |
| Responsable de la operación — nombre por confirmar | Disponibilidad de materia prima, facturación, programación de producción, coordinación de pedidos y entregas, y registro de ventas y saldos. |
| Tres operarios | Producción y preparación de pedidos. |
| Operaria de enlace | Coordinación frecuente con la responsable para organizar los pedidos. No se confirma que tenga un cargo formal de supervisión. |
| Distribuidores | Comercialización del producto. Santiago es mencionado expresamente como distribuidor. |

La responsable considera que dispone de un excelente equipo humano, pero señala que la ausencia de una persona desorganiza la operación. La asignación exacta del transporte y las entregas debe aclararse: el relato menciona funciones de domiciliario, sin permitir atribuirlas con certeza.

## 3. Herramientas y registros actuales

| Herramienta | Uso actual |
|---|---|
| WhatsApp | Atención comercial y recepción de pedidos. |
| Chat interno «Pedidos» | Transferencia de pedidos y datos de clientes; seguimiento informal de entregas. |
| Programa de facturación — nombre por confirmar | Emisión de facturas y manejo de precios. |
| Excel | Registro de ventas después de entregar; identificación en rojo de cuentas pendientes. Se mencionan otros formatos, aún no revisados. |
| Memoria de la responsable | Consulta de inventario y evaluación de disponibilidad y fechas. |

Existen registros digitales parciales. Lo que falta, según el relato, es consolidar y mantener la información operativa en un sistema integrado.

## 4. Flujo actual de pedidos

1. El cliente contacta a Omar por WhatsApp.
2. Omar recibe el pedido y solicita nombre completo, número de cédula, teléfono y correo electrónico para facturación.
3. Omar envía el pedido y los datos al chat interno «Pedidos».
4. La responsable evalúa disponibilidad y cuándo se podrá entregar, apoyándose en su conocimiento del inventario y los pedidos pendientes.
5. La responsable crea la factura y se la envía a Omar.
6. Omar comparte la factura y comunica al cliente la fecha prevista de entrega.
7. Se programa la producción necesaria según los pedidos en cola y se coordina la preparación con los operarios.
8. Generalmente se recibe el pago antes del despacho. Algunos clientes antiguos pueden recibir primero y pagar después.
9. Se entrega el pedido.
10. La responsable marca la entrega con ✅ en el chat y registra la venta en Excel. Si existe saldo pendiente, lo identifica en rojo.

**Criterio operativo de pedido terminado:** entrega al cliente. Esto no implica necesariamente que el pedido esté pagado.

**Aspectos por precisar:** cuándo se confirma formalmente el pedido, cuándo se fija la fecha definitiva, cómo se comprueba el pago y quién registra cada cambio.

## 5. Catálogo mencionado

### 5.1. Presentaciones de 500 gramos

Los importes se transcriben sin convertir moneda. El contexto apunta a pesos colombianos, pero debe confirmarse que todos los valores correspondan a COP y aclararse impuestos y transporte.

| Receta | Destino indicado | Forma | Peso informado | Precio al público | Precio a distribuidor | Observación |
|---|---|---|---|---:|---:|---|
| Pollo y salmón | Perros | Chorizos | 500 g | 14.000 | 9.800 | Producto descrito como prémium. |
| Cerdo | Línea canina, por confirmar en ficha | Hamburguesas | 500 g | 5.000 | 35.000 **por confirmar** | El valor a distribuidor parece inconsistente; no se corrige sin validación. |
| Pollo | Línea canina, por confirmar en ficha | Hamburguesas | 500 g | 5.000 | 3.500 | Confirmar condiciones comerciales. |
| Ternera | Línea canina, por confirmar en ficha | No especificada | 500 g | 6.000 | 4.500 | Confirmar forma del producto. |
| Salmón y cerdo | Gatos | Chorizos | 500 g | 16.000 | 11.200 | Confirmar denominación oficial de la receta. |

La fuente alterna «libra» y «500 gramos». Para el catálogo se conserva el peso explícito de 500 g, pendiente de contrastarlo con las etiquetas. La referencia aproximada a cinco dólares para pollo y salmón no se utiliza como precio vigente.

### 5.2. Venta directa por volumen

| Receta | Forma | Presentación informada | Precio informado | Canal |
|---|---|---|---:|---|
| Cerdo | Hamburguesas | 1,5 kg | 6.200 por kg | Directo, sin distribuidores para esta oferta. |
| Pollo | Hamburguesas | 1,5 kg | 6.200 por kg | Directo, sin distribuidores para esta oferta. |

Condiciones relatadas:

- Compra mínima de 40 kg.
- Entrega completa en un solo pedido.
- Oferta disponible en cerdo y pollo; no en ternera.

Pendiente de confirmar:

- Si el mínimo se aplica por receta o al total combinado.
- Si 1,5 kg corresponde al paquete comercial o a otra unidad de producción.
- Cómo se combina el mínimo de 40 kg con paquetes de 1,5 kg: 40 no es múltiplo de 1,5; un mínimo puede superarse, pero la regla debe explicitarse.
- Si esta oferta tiene diferencias de formulación respecto a la presentación de 500 g.

**Recuento provisional:** se identifican cinco recetas en 500 g y dos ofertas en 1,5 kg. Esto no permite fijar todavía el número definitivo de productos o SKU.

## 6. Producción, materias primas y maquinaria

La responsable señala que programa la producción en función de los pedidos pendientes. Esto sugiere una operación orientada a la demanda recibida, aunque falta confirmar cuánto inventario terminado se mantiene.

Se mencionan transformación de materias primas, merma y horneado. No se dispone de una descripción completa del proceso.

La empresa desea organizar información sobre:

- Recetas y sus modificaciones.
- Materias primas y cantidades utilizadas por lote.
- Cantidad de producto terminado esperada y obtenida.
- Mermas del proceso.
- Disponibilidad de insumos y productos.
- Protocolos y formatos de operación.

Las fallas de maquinaria consumen tiempo por búsqueda de técnicos y repuestos, reparación y fabricación de piezas. No se aportan datos de frecuencia, costos o capacidad perdida.

No se conocen todavía capacidad productiva, costos por receta, tiempos de fabricación, vida útil, condiciones de almacenamiento ni trazabilidad actual por lote.

## 7. Comercialización y posicionamiento

### Situación relatada

- Existen aproximadamente tres o cuatro puntos de distribución; confirmar cantidad y actividad actual.
- Una parte de las ventas procede de amigos, conocidos y contactos del entorno canino.
- La confianza y trayectoria de Omar son activos comerciales relevantes.
- La receta de pollo y salmón lleva aproximadamente tres años de trabajo de posicionamiento, según la entrevistada; esto no establece la antigüedad de toda la empresa.
- La responsable percibe dificultades para ampliar el mercado de la oferta prémium para perros y expresa interés en vender mayores volúmenes.

### Preguntas comerciales que la empresa quiere resolver

| Tema | Pregunta de trabajo |
|---|---|
| Competencia | ¿Qué productos son comparables y cómo se comercializan? |
| Precio | ¿Qué paga el comprador por productos y cantidades equivalentes? |
| Presentación | ¿Qué gramaje facilita compra, consumo y rentabilidad? |
| Segmentación | ¿Qué tipos de compradores y mascotas encajan con cada producto? |
| Distribución | ¿Cómo aumentar ventas mediante distribuidores? |
| Recompra | ¿Qué favorece o dificulta que el cliente vuelva a comprar? |

Estas preguntas son necesidades de investigación; el documento no contiene resultados de un estudio de mercado.

## 8. Línea para gatos: oportunidad propuesta

La responsable considera que la receta de salmón y cerdo podría tener alto potencial comercial. Relata que algunos gatos rechazan el alimento y que, tras abrir el paquete, puede perder aceptación conforme disminuye su frescura.

| Propuesta o percepción | Estado |
|---|---|
| Ofrecer paquetes de aproximadamente 200 g. | Idea por evaluar; no es una presentación confirmada del catálogo. |
| Dirigirse a hogares que incorporan un gatito. | Hipótesis de segmentación. |
| Mayor disposición a pagar en compradores de alimento para gatos. | Percepción de la entrevistada; requiere validación. |
| Reducir desperdicio mediante paquetes menores. | Beneficio esperado por medir. |

Antes de decidir el cambio de empaque, conviene conocer consumo por hogar, conservación, aceptación, costo del envase y frecuencia de recompra. No se ha establecido la rentabilidad neta de la línea.

### Aclaración del cálculo comercial

Con los precios informados para el paquete de 500 g:

- Diferencia entre precio público y precio a distribuidor: 16.000 − 11.200 = **4.800 por paquete**.
- Paquetes por tonelada: 1.000 kg ÷ 0,5 kg = **2.000 paquetes**.
- Diferencia comercial teórica por tonelada: 2.000 × 4.800 = **9.600.000**.

Este cálculo supone vender todo al precio indicado y no incluye transporte, descuentos, pérdidas, comisiones ni otros gastos. No representa utilidad neta ni margen del fabricante. La cifra verbal de 4.800.000 por tonelada debe aclararse con la empresa.

## 9. Dos frentes de colaboración

### A. Organización y sistematización

La empresa expresa interés en ordenar pedidos, materias primas, producción y registros. Espera reducir carga administrativa y mejorar la coordinación del equipo.

Existe disposición verbal a remunerar este trabajo, sin monto, modalidad ni alcance acordados. También se plantea proporcionar formatos de Excel y definir cómo se ingresará la información: mediante preguntas, con apoyo del implementador o directamente por la responsable.

### B. Desarrollo comercial con Santiago

Se propone captar clientes para que Santiago comercialice el producto y compartir entre él y el colaborador parte del resultado de esas ventas.

No se ha definido porcentaje, base del reparto, atribución de clientes, gastos, momento del pago ni tratamiento de la recompra. Las cifras de ingresos mencionadas verbalmente no constituyen una proyección validada ni una garantía.

Estos dos frentes requieren alcances y acuerdos económicos propios.

## 10. Necesidades de sistematización identificadas

| Área | Necesidad identificada | Información mínima a organizar |
|---|---|---|
| Clientes | Evitar datos dispersos en conversaciones. | Identificación, contacto, dirección y condiciones de pago. |
| Productos | Unificar recetas, formatos, unidades y precios. | Código, nombre, peso, presentación, canal y precio validado. |
| Pedidos | Seguir compromisos y entregas. | Productos, cantidades, fechas, responsable y estado. |
| Pagos | Distinguir cobro y entrega. | Importe, abonos, saldo y vencimiento. |
| Producción | Coordinar pedidos con fabricación. | Cantidades pendientes, lotes y fechas previstas. |
| Inventario | Sustituir dependencia de la memoria. | Existencias, entradas, salidas y cantidades comprometidas. |
| Mantenimiento | Documentar fallas e intervenciones. | Equipo, incidencia, reparación y parada. |
| Conocimiento | Reunir respuestas y documentos existentes. | Procedimientos, fichas, formatos y responsables. |

Esta tabla es una síntesis analítica de necesidades, no una lista de funciones ya implementadas.

## 11. Propuesta inicial de sistema

El material adjunto incluye una propuesta de preparar un entorno local de **Odoo Community**, con un primer piloto de clientes, productos y pedidos de venta. El CRM se plantea para consultas que aún no se convierten en pedidos.

**Estado:** propuesta de trabajo; no hay evidencia en la fuente de que el sistema esté instalado o configurado.

Para representar la operación descrita, el piloto debería permitir distinguir:

- Estado del pedido y fecha comprometida.
- Estado de preparación y entrega.
- Estado del pago y saldo pendiente.

Recorrido habitual a documentar: **registrar cliente → crear y confirmar pedido → coordinar producción y pago previo al despacho → despachar → entregar → cerrar seguimiento**.

Excepción: los clientes autorizados a crédito pueden recibir antes de pagar. La secuencia exacta entre producción y cobro debe confirmarse.

La relación con el programa de facturación existente debe definirse antes de sustituir o duplicar registros.

## 12. Afirmaciones y evidencia pendiente

La entrevistada sostiene que sus productos tienen una calidad superior y relata beneficios observados en mascotas. También expresa opiniones sobre alimentos competidores, salud y comportamiento de compra.

Estas declaraciones se registran como percepciones y testimonios. No se consideran demostradas la superioridad frente a todo el mercado, las comparaciones del tipo «tres veces mejor» ni las relaciones causales entre un alimento y enfermedades.

Para evaluar posicionamiento y mensajes comerciales hacen falta fichas técnicas, análisis comparables y respaldo profesional pertinente. El documento no establece que las recetas sean alimentos completos ni confirma su adecuación para todas las etapas de vida.

La transcripción menciona una autoridad como «lca», posiblemente el ICA; su identificación y los requisitos concretos deben confirmarse. No se aportan registros o permisos que permitan concluir el estado regulatorio de Canívoros.

## 13. Información pendiente de confirmar

- [ ] Nombre y cargo de la responsable; datos básicos y ubicación de la empresa.
- [ ] Catálogo definitivo, recetas, presentaciones y códigos.
- [ ] Precio a distribuidor de cerdo de 500 g.
- [ ] Moneda, impuestos, transporte y vigencia de precios.
- [ ] Correspondencia entre «libra» y peso declarado en etiqueta.
- [ ] Regla de pedido mínimo y unidades de la oferta de 1,5 kg.
- [ ] Nombre y funcionamiento del programa de facturación.
- [ ] Contenido de los Excel mencionados y responsable de mantenerlos.
- [ ] Existencias iniciales, capacidad, rendimientos, mermas y costos.
- [ ] Conservación, vida útil y documentación técnica de los productos.
- [ ] Número y condiciones de distribuidores activos.
- [ ] Responsables de entrega y comprobación de pagos.
- [ ] Clientes con crédito, plazos y saldos actuales.
- [ ] Documentación y registros regulatorios disponibles.
- [ ] Alcance y remuneración del trabajo de sistemas.
- [ ] Condiciones del acuerdo comercial con Santiago.

## 14. Cómo mantener esta referencia

Actualizar cada dato cuando la empresa lo confirme y registrar su fecha y fuente. Mantener las propuestas separadas del catálogo y las condiciones vigentes. Usar este documento como base para entrevistas, revisión de archivos y definición del piloto, sin convertir los datos dudosos en configuración definitiva.

---
$$$$

# Repitiendo análisis de la información arriba

## Canívoros — levantamiento operativo para el ERP

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

---

# aquí tenemos nuevas informaciones sobre la empresa

La transcripción muestra que **Canívoros tiene una operación productiva y comercial en marcha, pero gran parte de su coordinación depende de la memoria, WhatsApp y registros manuales de sus responsables**. Sus necesidades principales son organizar la operación y desarrollar la comercialización, con alcances y acuerdos económicos separados.

A continuación distingo los datos relatados, las oportunidades y lo que falta confirmar.

## 1. Qué es Canívoros y cómo funciona

| Aspecto | Información extraída |
|---|---|
| Actividad | Elaboración y venta de alimentos para mascotas, principalmente perros; también tiene un producto para gatos. |
| Equipo | Cinco personas: Omar, la responsable de la operación y tres operarios. |
| Omar | Atiende consultas y pedidos por WhatsApp y se encarga de las ventas. |
| Responsable de la operación | Gestiona materia prima, facturación, programación de producción y coordinación de pedidos y entregas. |
| Operarios | Elaboran los productos y preparan los pedidos. Una operaria mantiene comunicación directa con la responsable para organizarlos. |
| Distribución | Se mencionan tres o cuatro puntos de distribución, además de ventas a conocidos y contactos. |
| Fortaleza comercial actual | Confianza, credibilidad y trayectoria de Omar en el entorno de los perros. |
| Fragilidad operativa | La ausencia de una sola persona altera considerablemente el funcionamiento. |

**La empresa busca concentrarse en producir volumen y cumplirles a sus distribuidores**, mientras estos desarrollan sus propias ventas.

## 2. Cómo se gestiona hoy una venta

1. El cliente contacta a Omar por WhatsApp.
2. Omar solicita nombre completo, número de identificación, teléfono y correo para facturación.
3. Envía los datos y el pedido a un chat interno llamado **“Pedidos”**.
4. La responsable evalúa disponibilidad y fecha de entrega, apoyándose en su conocimiento del inventario y la producción pendiente.
5. Crea la factura en un programa de facturación y se la envía a Omar.
6. Omar comparte la factura y comunica la fecha de entrega al cliente.
7. Generalmente, el cliente paga **antes del despacho**. Algunos clientes antiguos reciben y pagan después.
8. Los operarios preparan el pedido y se coordina su entrega.
9. Una vez entregado, se marca con ✅ en el chat y se registra la venta en Excel.
10. Los saldos pendientes se señalan en rojo en Excel.

**Implicación para el sistema:** el pago y la entrega deben tener estados independientes. El recorrido habitual incluye pago antes del despacho, pero también existe venta a crédito.

## 3. Catálogo y precios mencionados

Los valores siguientes reproducen lo informado. **La moneda debe confirmarse**, aunque por el contexto parece tratarse de pesos colombianos.

| Producto / receta | Forma | Presentación | Precio al público | Precio a distribuidor |
|---|---|---:|---:|---:|
| Pollo y salmón, para perros | Chorizos | 500 g | 14.000 | 9.800 |
| Cerdo | Hamburguesas | 500 g | 5.000* | 35.000* |
| Pollo | Hamburguesas | 500 g | 5.000 | 3.500 |
| Ternera | No queda explícita | 500 g | 6.000 | 4.500 |
| Salmón y cerdo, para gatos | Chorizos | 500 g | 16.000 | 11.200 |
| Cerdo, venta directa por volumen | Hamburguesas | 1,5 kg | 6.200 por kg | No aplica según el relato |
| Pollo, venta directa por volumen | Hamburguesas | 1,5 kg | 6.200 por kg | No aplica según el relato |

\* **El precio de cerdo requiere corrección:** se transcribió “5.000 la libra” al público y “35.000” al distribuidor. No conviene cargar ese dato sin confirmación.

Para las ventas por volumen se indican estas condiciones:

- Pedido mínimo de **40 kg**.
- Entrega completa en un solo pedido.
- Solo pollo y cerdo; **no ternera**.
- Comercialización directa, sin distribuidores.

Hay otra inconsistencia que resolver: **40 kg no equivalen a un número entero de paquetes de 1,5 kg**. Debe aclararse cómo se completa el mínimo y si se pueden combinar recetas.

También conviene unificar unidades: en el relato se alternan **“libra” y “500 gramos”**.

## 4. Necesidades operativas identificadas

| Necesidad | Evidencia del relato | Qué convendría registrar |
|---|---|---|
| Centralizar pedidos | Se coordinan en un chat interno. | Cliente, productos, cantidades, fecha prometida y estado. |
| Controlar inventario | La disponibilidad se consulta “en la mente”. | Materia prima, producto terminado y cantidades comprometidas. |
| Programar producción | Se produce según los pedidos en cola. | Demanda pendiente, prioridad y fecha prevista. |
| Documentar recetas y rendimientos | Se mencionan cantidades por lote, merma y producto esperado. | Receta, insumos consumidos, merma y resultado real por lote. |
| Controlar cobros | Se usan marcas rojas en Excel. | Importe, pagos recibidos, saldo y vencimiento. |
| Organizar mantenimiento | Las averías y la búsqueda de técnicos o repuestos consumen tiempo. | Equipos, incidencias, reparaciones y paradas. |
| Consolidar conocimiento | Las respuestas existen, pero están repartidas entre conversaciones con distintos profesionales. | Documentación central y responsables de actualizarla. |

**No parten de cero en conocimiento: necesitan convertir lo que ya saben en información organizada y utilizable.**

## 5. Necesidades comerciales

La empresa reconoce que todavía no ha estudiado de forma sistemática:

- Competidores y productos comparables.
- Precios y beneficios ofrecidos en el mercado.
- Presentaciones y gramajes más adecuados.
- Segmentos de compradores.
- Rentabilidad por producto y canal.
- Métodos para captar clientes fuera de la red de contactos actual.

El producto de pollo y salmón lleva aproximadamente **tres años de posicionamiento**, según el relato. La responsable percibe que su crecimiento ha sido limitado por el tamaño del público dispuesto a pagar por esa propuesta.

Esto sugiere una pregunta comercial central: **¿qué combinación de producto, presentación, público y canal permite vender de forma rentable y recurrente?**

## 6. Oportunidad del producto para gatos

La responsable identifica el alimento para gatos como una posible línea de mayor rentabilidad, pero también relata dificultades de aceptación y frescura después de abrir el empaque.

| Dato u observación | Oportunidad por validar |
|---|---|
| Presentación actual de 500 g | Probar una presentación menor, por ejemplo de 200 g. |
| Algunos gatos rechazan el producto después de abierto | Medir consumo por empaque, conservación y desperdicio. |
| Se percibe menor resistencia al precio | Comprobar disposición de pago con compradores reales. |
| Se propone captar hogares con gatitos | Evaluar ese segmento y la recompra, con orientación nutricional veterinaria. |

**La presentación de 200 g es una propuesta, todavía no una decisión validada.**

Además, la rentabilidad mencionada en el audio no coincide con los precios informados:

- Diferencia por paquete: 16.000 − 11.200 = **4.800**.
- Una tonelada contiene **2.000 paquetes de 500 g**.
- Diferencia comercial teórica: **9.600.000 por tonelada**, antes de gastos y descuentos.

El audio habla de 4.800.000 por tonelada. Debe confirmarse la unidad o el acuerdo utilizado. **La diferencia entre precio de compra y venta tampoco equivale a ganancia neta.**

## 7. Dos servicios distintos que te están solicitando

| Frente | Resultado esperado por Canívoros | Acuerdo pendiente |
|---|---|---|
| **Organización y sistemas** | Ordenar pedidos, producción, materias primas, inventario y registros; reducir carga administrativa. | Alcance, implementación, alimentación de datos, soporte y remuneración. |
| **Desarrollo comercial** | Llevar clientes a Santiago y aumentar las ventas de distribución. | Cómo se atribuyen ventas y cómo se reparte el margen entre tú y Santiago. |

**No hay un acuerdo económico cerrado en la transcripción.** Existe disposición a remunerar la organización de la empresa y una propuesta de compartir resultados comerciales, pero faltan condiciones concretas.

## 8. Afirmaciones que requieren evidencia

La responsable expresa convicción sobre la calidad del producto. Sin embargo, estas declaraciones deben conservarse como **afirmaciones de la entrevistada**, no como conclusiones demostradas:

- “La mejor calidad del mercado” o “nadie en Colombia compite”.
- Ser “casi el triple de buenos”.
- Mejoras de salud, peso o pelaje atribuidas al alimento.
- Relaciones causales entre otros alimentos y enfermedades.

Para convertirlas en argumentos comerciales hacen falta fichas técnicas, análisis comparables y respaldo profesional pertinente. La transcripción tampoco permite confirmar el estado de los registros o permisos de la empresa.

## 9. Primer paso recomendado

**Documentar un pedido real completo y construir un piloto con clientes, productos, pedidos, pagos y entregas.** La producción bajo pedido y la existencia de clientes a crédito deben quedar reflejadas desde el inicio.

Antes de cargar el catálogo, resolvería cinco puntos:

1. Precios y unidades exactas de cada producto.
2. Catálogo definitivo y presentaciones disponibles.
3. Regla de venta mínima para los paquetes de 1,5 kg.
4. Programa de facturación utilizado y datos que ya contiene.
5. Responsables de registrar pedidos, pagos, producción y entregas.

Con estos datos se puede definir el primer sistema alrededor de la operación real de Canívoros y, en paralelo, preparar una investigación comercial con preguntas concretas.


---
$$$$

[10:50, 26/10/2026] Sary Crispina: Mas que decir forma seria mejor decir presentacion
[10:52, 26/10/2026] Sary Crispina: En cuanto a destino indicado las recetas de cerdo pollo y ternera son para perros de todas las razas y todas las edades
[10:52, 26/10/2026] Sary Crispina: Y claro en la de cerdo el precio a distribuidor es 3.500


