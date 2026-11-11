# Auditoría de claims del sitio canivoros.com

Borrador 1 · Sitio consultado el **10 nov 2026, 22:15 (hora de Quito, UTC-5)** con descarga directa del HTML. Apoya **BL-016**. Nada de esto se ha cambiado en el sitio.

**Alcance.** Páginas Inicio, Nosotros, Productos (incluye las preguntas frecuentes), Distribuidores y Contáctanos. No existe una página aparte de preguntas frecuentes: `https://canivoros.com/preguntas-frecuentes/` responde 404 y el botón "Ver Información" del inicio lleva a las preguntas de /productos/.

**Cómo se arma el reemplazo.** Solo con lo que ya tiene respaldo en el repo:

| Dato usable | Estado | Fuente |
|---|---|---|
| Se fabrica en Sopó, Cundinamarca (dirección publicada) | Declaración | Sitio; `CANIVOROS-REFERENCIA-EMPRESA.md` |
| Proteínas: pollo, salmón, cerdo (y ternera en Odoo) | Hecho documental | Catálogo Odoo 27/10 en `branding/05`; `erp.md` §5 |
| Formatos: chorizos y hamburguesas de 500 g; volumen 1,5 kg a criadores | Hecho documental, catálogo definitivo pendiente | `erp.md` §5; BL-005 |
| Horneado; no es crudo ni BARF | Declaración | Sitio, FAQ |
| Origen en la crianza familiar de perros de competencia | Declaración | Sitio, Nosotros |
| Atiende Omar por WhatsApp | Hecho | `erp.md` §2 |
| En casos clínicos, consultar al veterinario | Ya publicado | FAQ |

Los textos propuestos aplican `branding/02` §4 ("Qué sí decir y qué no decir") y `branding/03` §5 ("Mensajes prohibidos"). No proponen posicionamiento ni taglines nuevos.

**Prioridad.** Alta: riesgo sanitario, regulatorio o contradicción directa con lo que relata la empresa. Media: superlativo o promesa sin prueba. Baja: forma y confianza.

**Quién confirma.** "Dueña" es la responsable de la operación (nombre por confirmar, `erp.md` §2; BL-005 menciona a "la prima o Sara Ramírez"). Sebastián edita el sitio (BL-016, propuesta).

## Prioridad alta

| # | Página y URL | Texto actual (literal) | Riesgo y fuente | Propuesta de reemplazo | Confirma |
|---|---|---|---|---|---|
| A1 | Productos, FAQ · /productos/ | "Guarda el alimento en un lugar fresco y seco, lejos del sol directo. Una vez abierto, mantén la bolsa bien cerrada o en un recipiente hermético para conservar su aroma y textura." | Instrucción de conservación sin dato de respaldo. La conservación y vida útil de cada producto están pendientes (`erp.md` §13; `branding/README` punto 2). Si chorizos o hamburguesas necesitan frío, esta instrucción es un riesgo para la mascota. | [falta: conservación por producto (congelado, refrigerado o ambiente), vida útil cerrado y abierto]. Mientras tanto: "Guárdalo como indica la etiqueta. Si tienes dudas, escríbenos." | Dueña, con ficha técnica |
| A2 | Inicio · / | "Sin harinas procesadas ni subproductos." | La empresa relata que su materia prima son "subproductos": cabezas de pollo, barriga de salmón, canilla y vísceras de cerdo (`erp.md` §1). BL-016. | "Pollo, salmón y cerdo." La forma de contar la materia prima la decide la dueña (`branding/03` §4, objeción "¿Lleva subproductos?"). | Dueña |
| A3 | Productos, FAQ · /productos/ | "suele ser mejor tolerado que alimentos muy cargados de harinas o subproductos." | Repite "subproductos" y hace un claim de tolerancia digestiva (`erp.md` §12). | "Si tu perro tiene el estómago sensible o una condición clínica, consulta primero con su veterinario. Te contamos qué lleva cada producto para que lo revisen juntos." | Dueña |
| A4 | Inicio · / | "El horneado elimina bacterias y mejora la digestión." | Claim sanitario y funcional sin análisis (`erp.md` §12; `branding/02` §4). | "Horneado en nuestra planta de Sopó." | Dueña |
| A5 | Inicio · / | "Ayuda a limpiar dientes gracias a su textura crocante." | Claim de salud dental. "Crocante" no está confirmado para chorizos y hamburguesas (`branding/01` §1, tensión 2). | Quitar. [falta: evidencia] | Dueña |
| A6 | Inicio · / | "Heces más firmes, menos olorosas y mejor absorción de nutrientes." | Claim de salud digestiva sin respaldo (`branding/03` §5). | Quitar. [falta: evidencia] | Dueña |
| A7 | Inicio · / | "Ideal para perros que no toleran concentrado ni BARF." | Promesa para perros con intolerancias: es un uso clínico. | Quitar. Si se quiere hablar de BARF, usar la Declaración ya publicada en la FAQ: "Canívoros es un alimento horneado." | Dueña |
| A8 | Inicio · / | "Natural, práctica, segura y lista para servir." | "Segura" sin respaldo. "Lista para servir" depende de A1. | "Lista para servir." Solo si A1 lo confirma. [falta: conservación] | Dueña |
| A9 | Productos, FAQ · /productos/ | "Mejora la digestión, ayuda a un pelaje más brillante, aporta energía natural, fortalece el sistema inmune y favorece la condición física, gracias a su contenido de proteína animal y omegas." | Cinco claims de salud sin ficha técnica (`erp.md` §12; `branding/03` §5). | Cambiar la pregunta a "¿Qué lleva Canívoros?" y responder: "Pollo y salmón, o cerdo, según el producto. Viene en chorizos o hamburguesas de 500 g." [falta: ficha con análisis] | Dueña |
| A10 | Productos, FAQ · /productos/ | "porque no es un concentrado ultraprocesado. Canívoros usa proteína animal de calidad (pollo, salmón o cerdo), se hornea y no usa colorantes ni saborizantes artificiales. Eso mejora digestión, aceptación y aprovechamiento del alimento." | Claim funcional ("mejora digestión") y comparación implícita contra concentrados (`branding/02` §4). | "Se hace con pollo, salmón o cerdo, se hornea en Sopó y viene en chorizos o hamburguesas." Lo de colorantes solo con la lista de ingredientes (ver M5). | Dueña |
| A11 | Productos, FAQ · /productos/ | "Sí. Nuestros productos cuentan con registro ICA, lo que asegura que cumplen la normatividad colombiana para alimentos de mascotas y que son seguros para el consumo animal." | Ninguna fuente trae número ni fecha del registro. `erp.md` §12: la transcripción dice "lca" y el estado regulatorio no se puede confirmar. "Asegura que son seguros" es un claim adicional. | "Sí. Registro ICA [número] para [producto]." Sin número, quitar la pregunta. | Dueña, con el documento del ICA |
| A12 | Todas las páginas, pie · / y demás; también en la descripción para buscadores de /contactanos/ | "Certificación ICA vigente." | Mismo vacío que A11. "Certificación vigente" sin número está en la lista de `branding/02` §4. | "Registro ICA [número]." Sin número, quitar. | Dueña |
| A13 | Productos · /productos/ | Perros, salmón: "Refuerza la salud cerebral y ocular", "Apoya la salud articular", "Altamente digestible". Intro: "ideales para mantener la vitalidad, la energía y la salud integral de tu mascota." | Claims de salud y nutrición atribuidos al producto sin ficha (`branding/05` ficha 1: omegas "a validar"). | Por producto: proteína y formato. Ejemplo para la ficha 1 de `branding/05`: "Chorizos de pollo y salmón. Horneados en Sopó. 500 g." [falta: ficha técnica] | Dueña |
| A14 | Productos · /productos/ | Perros, pollo: "Rico en vitaminas del complejo B (B3, B6, B12)", "Contiene fósforo y selenio", "Fácil digestión". Cerdo: "Rico en vitaminas y minerales", "Energía natural y sostenible". | Claims de nutrientes que requieren análisis del producto (`branding/05` fichas 2 y 3). | "Hamburguesas de pollo. 500 g." / "Hamburguesas de cerdo. Otra proteína para variar." (la segunda ya es Declaración del sitio, `branding/05` ficha 3). | Dueña |
| A15 | Productos, Gatívoros · /productos/ | "Salmón y Pollo" y "elaborados con pollo y salmón de alta calidad" | Odoo (CAN-SC-500) y `erp.md` §5 dicen salmón y cerdo (`branding/05`, diferencia 1). El cliente puede recibir algo distinto de lo publicado. | "Gatívoros. [receta confirmada en BL-005]. 500 g." | Dueña |
| A16 | Productos, Gatívoros · /productos/ | "fuentes naturales de proteína, omega 3 y taurina, esenciales para el bienestar diario de tu felino"; salmón: "promueve una piel sana, un pelaje brillante y un sistema inmunológico fuerte", "Salud cerebral y visual", "Defensas equilibradas"; pollo: "Fuente natural de taurina" | Claims de nutrición y salud felina sin ficha. La taurina en gatos es un tema técnico: no se afirma sin análisis (`branding/05` ficha 5). | "Gatívoros, de la casa Canívoros. Para gatos." (arquitectura de `branding/01` §6) + receta confirmada. [falta: ficha técnica] | Dueña |
| A17 | Inicio, testimonios · / | Nala: "A los 9 meses padeció de parvovirus … la pasamos a Canívoros y mejoró su peso, su pelo y su intestino está perfecto!"; Jany: "sufría de gastroenteritis y muchos dolores articulares … desde entonces dejo sus dolores articulares y sus problemas intestinales."; Milo: "su pelaje mejoró, el olor de las heces disminuyó" | Testimonios con desenlaces de enfermedad funcionan como claims de salud de la marca. No consta permiso escrito de los autores (BL-058). | Retirar los que hablan de enfermedad o síntomas hasta tener permiso y revisión. Conservar, con permiso, solo relatos de aceptación, como el de Melcocha ("el olor le llamó la atención … volvió a comer con gusto"). [falta: permisos firmados] | Dueña + Andrés (BL-058) |
| A18 | Nosotros · /nosotros/ | Misión: "alimentos naturales, horneados y balanceados que favorecen la masticación, protegen su sistema digestivo … procesos de alta tecnología que garantizan una nutrición completa y saludable." Visión: "garantiza una digestión saludable y una nutrición completa", "cuidando el sistema digestivo y fortaleciendo la salud de los perros y gatos, incluso aquellos con problemas digestivos" | "Balanceado" y "nutrición completa" no están establecidos (`erp.md` §12). "Garantiza" es una promesa de resultado. | Misión con hechos: "Hacer en Sopó alimento horneado para perros y gatos con pollo, salmón y cerdo, y atender de cerca a quien lo compra." Aplica los pilares "Horneado en Sopó" y "De criadores" de `branding/01` §7. Redacción final de la dueña. | Dueña |
| A19 | Inicio · / | "Alto contenido proteico para músculos fuertes, articulaciones saludables y pelaje brillante." (también en la descripción para buscadores) | Cifra implícita de proteína sin análisis más tres claims de salud. | Quitar. [falta: % de proteína en ficha] | Dueña |
| A20 | Nosotros · /nosotros/ | "un alimento natural que potencia la salud, energía y longevidad de las mascotas" | "Longevidad" es un claim de salud sin respaldo. | "Esta trayectoria nos llevó a hacer el alimento que les damos a nuestros perros." Solo si se confirma que los perros de la familia lo comen (ver nota 2 para el bot Canívoros). | Dueña |

## Prioridad media

| # | Página y URL | Texto actual (literal) | Riesgo y fuente | Propuesta de reemplazo | Confirma |
|---|---|---|---|---|---|
| M1 | Inicio · / | "100% carne real (pollo, cerdo y salmón), cocinada a baja temperatura." y "Ingredientes 100% reales" | "100 %" exige la receta completa. "Baja temperatura" es un dato de proceso sin registro (`erp.md` §6, sin tiempos ni temperaturas). `branding/02` §4 solo admite "100 % pollo" si la receta lo confirma. | "Pollo, cerdo y salmón, horneados en Sopó." | Dueña |
| M2 | Inicio · / | "Natural, sin aditivos y libre de granos" / "Cero conservantes químicos, colorantes artificiales o saborizantes sintéticos. Pura naturaleza." | Sin lista de ingredientes publicada ni en el repo. "Libre de granos" está en `branding/03` §5. | [falta: lista de ingredientes por producto]. Con la lista, decir solo lo que esté en la etiqueta. | Dueña |
| M3 | Nosotros · /nosotros/ | "se consolidan como referentes colombianos en nutrición natural para perros y gatos" | Superlativo sin prueba (`erp.md` §8, "la mejor calidad del mercado" como afirmación de la entrevistada). | "Se hacen en Sopó, Cundinamarca." | Dueña |
| M4 | Nosotros y Productos · /nosotros/, /productos/ | "alimento natural, horneado y super premium"; "Nuestras líneas de productos premium"; "proteínas premium de origen animal" | `branding/03` §5 prohíbe "super premium" en anuncios pagados. En el sitio queda como Declaración sin prueba. | Nombrar el producto por proteína y formato (`branding/01` §6, regla de nombres). | Bot Canívoros + dueña |
| M5 | Nosotros, atributos · /nosotros/ | "Ingredientes premium certificados" | No se sabe qué certificación ni de quién. | "Calidad: [falta: certificación y entidad]." Sin el dato, quitar "certificados". | Dueña |
| M6 | Nosotros, atributos · /nosotros/ | "Con tu mascota y el planeta" / "Producción limpia y responsable" | Claim ambiental sin respaldo. Hay un relato que podría sostener algo concreto: la empresa compra partes que se desecharían (`erp.md` §1). | Esperar la redacción de `branding/03` §4 (subproductos). No escribir un claim ambiental aparte. | Dueña + bot Canívoros |
| M7 | Inicio · / | "algunos campeones alimentados con Canívoros. Estos atletas de cuatro patas demuestran día a día que la nutrición natural marca la diferencia." | Relación causal entre el alimento y los títulos (`branding/02` §4). Uso de perros de terceros sin permiso registrado (`branding/01` §5). | "Algunos de los perros de competencia que comen Canívoros." [falta: confirmar que comen el producto y permiso de sus dueños] | Dueña + Omar |
| M8 | Productos · /productos/ | "Alimento natural horneado para perros campeones que merecen nutrición de verdad." (también en la descripción para buscadores) | Sugiere que es solo para perros de competencia y que otras comidas no nutren. | "Alimento horneado para perros, hecho en Sopó." | Bot Canívoros |
| M9 | Distribuidores · /distribuidores/ | "Cada punto de venta garantiza producto fresco, almacenamiento adecuado y asesoría experta." | Los 6 puntos no se han validado (BL-035). Se promete algo que la marca no controla. | "Estos puntos venden Canívoros. Llama antes para confirmar disponibilidad." + "Lista revisada el [fecha de BL-035]." | Omar (BL-035) |
| M10 | Inicio y Contáctanos · /, /contactanos/; FAQ en /productos/; Distribuidores | Inicio: "WhatsApp: 324 460 8114" (enlace wa.me/573244608114). Contáctanos: "WhatsApp: 350 805 27 12", pero su botón abre wa.me/573244608114. FAQ: "Escríbenos a canivorossas@gmail.com o al 350 655 9910". Distribuidores: botón a wa.link/xx7i4d (destino no verificado). | Tres números y un enlace corto. La persona no sabe a cuál escribir y las consultas se reparten sin registro (BL-059; plan Bogotá, diagnóstico). | Un solo número comercial en todo el sitio. [falta: número principal definido]. Si distribución usa otro, decirlo: "Para ser distribuidor: [número]". | Dueña + Omar |
| M11 | Productos, FAQ · /productos/ | "Actualmente manejamos opciones con pollo y salmón (fuente de omega 3 y 6) y con cerdo magro, todas con excelente digestibilidad y sabor. Según la zona, pueden variar las presentaciones." | El sitio no menciona chorizos, hamburguesas, ternera ni el peso de 500 g. "Excelente digestibilidad" es claim. | "Para perros: chorizos de pollo y salmón, y hamburguesas de pollo y de cerdo [y de ternera, si está disponible]. Para gatos: Gatívoros [receta]. Presentación de 500 g." [falta: catálogo BL-005] | Dueña |
| M12 | Productos, FAQ · /productos/ | "Está recomendado para perros de todas las razas y edades. Es una excelente opción para perros activos, perros con estómago sensible…" | `erp.md` §12: no se confirma adecuación para todas las etapas de vida. "Estómago sensible" es uso clínico. | [falta: etapas de vida según ficha]. Con la ficha: "Para perros [etapas]." | Dueña |
| M13 | Productos, FAQ · /productos/ | "Usa nuestra guía de raciones o solicita la calculadora de porciones. Si tu perro es muy activo o está en recuperación, puede requerir un poco más." | La guía no está publicada (BL-041). "En recuperación" es un caso clínico. | "Escríbenos con el peso y la edad de tu perro y te decimos cuánto darle." Solo cuando exista la guía de BL-041. | Omar + dueña |
| M14 | Productos, FAQ · /productos/ | "El horneado aporta seguridad alimentaria y mantiene el perfil de un alimento de origen animal muy apetecible para el perro." | "Seguridad alimentaria" es claim técnico (igual que A4). | "No. Canívoros es un alimento horneado." | Dueña |
| M15 | Productos, FAQ · /productos/ | "bajo procesos controlados y con estándares de calidad para alimentos de mascotas." | No se sabe qué estándares. | "Canívoros se fabrica en Sopó, Cundinamarca." | Dueña |
| M16 | Inicio · / | "Recuperamos el instinto carnívoro de tu mascota con una fórmula que combina tradición y ciencia nutricional." y "Cada bocado está diseñado con amor y ciencia para nutrir…" | "Ciencia nutricional" sin formulador ni respaldo nombrado. | Quitar "ciencia". [falta: quién formula, si hay asesoría técnica] | Dueña |

## Prioridad baja

| # | Página y URL | Texto actual (literal) | Riesgo | Propuesta | Confirma |
|---|---|---|---|---|---|
| B1 | Todas, pie | "Created for free using WordPress and Colibri" | Resta confianza y está en inglés. | Quitar. | Sebastián |
| B2 | Inicio, testimonio de Jany | "consume 100% Carnívoros" | Nombre de marca mal escrito dentro de un testimonio publicado. | Corregir solo con permiso del autor, o retirar (ver A17). | Dueña |
| B3 | Productos, FAQ; Distribuidores | "Gativoros"; "canivoros & gativoros" | Marca sin tilde y en minúscula. | "Gatívoros"; "Canívoros & Gatívoros". | Sebastián |
| B4 | Inicio, perro Juanito | "número en el ranking de la raza en Colombia 2024 y 2025" | Falta la posición. | "[posición] en el ranking…" [falta: dato] | Omar |
| B5 | Productos, FAQ | "porque no es un concentrado ultraprocesado." | Empieza en minúscula. Se resuelve con A10. | Ver A10. | Sebastián |
| B6 | Productos, textos alternativos de imágenes | "salmón canivoros comida perros natural" y similares | Sin tildes y sin nombre de producto real. | "Chorizos de pollo y salmón Canívoros" cuando haya foto por producto. | Sebastián |

## Lo que el sitio no dice y debería decir

Antes de cualquier anuncio, el sitio no permite comprar con información completa (E02 §3: "total y entrega claros"):

- Formatos y pesos por producto. [falta: catálogo BL-005]
- Cómo se guarda cada producto. [falta: A1]
- Zonas y días de entrega. [falta: cobertura real]
- Un solo número para pedir. [falta: M10]

## Orden sugerido de corrección

1. A1, A11, A12, A15: conservación, ICA y receta de Gatívoros. Son datos que la dueña tiene o puede pedir. Sin ellos, cualquier otro texto queda incompleto.
2. A2 a A10, A13, A14, A16 a A20: quitar claims de salud. Casi todos se resuelven borrando, sin esperar a nadie.
3. M10: un solo número. Es requisito de BL-059 y del piloto E02.
4. El resto, junto con la versión aprobada de `branding/`.
