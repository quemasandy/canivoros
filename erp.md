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




