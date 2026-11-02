# Playbook de investigación de mercado y prospección · Canívoros en Bogotá

> Instrucciones para cualquier agente de IA (Claude, ChatGPT, Gemini u otro) que investigue el mercado y prospecte clientes para Canívoros en Bogotá.
> Trabaja como lo haría una agencia de primer nivel: **primero el mercado, después la lista; primero la evidencia, después el mensaje; pocas cuentas bien elegidas antes que muchas mal elegidas.**
> Las reglas comunes del proyecto (evidencia, datos personales, mensajes de marca, Git) están en `../AGENTS.md` y también aplican aquí.
> Última actualización: 2026-11-02.

---

## 0. En 10 líneas

1. Lee `../AGENTS.md`, este archivo, `INVESTIGACION-MERCADO.md` y `PROSPECTOS.md`, en ese orden.
2. Trabaja **por segmento y por zona**, en lotes de máximo 10 cuentas (S1 y S2 pueden ir juntos porque ambos revenden).
3. Sigue las 5 fases (§4): mapa del mercado → lista → verificación → puntaje → plan de abordaje.
4. Cada dato lleva etiqueta (E)/(D)/(H)/(V) y fuente con fecha. Lo que no sabes es `desconocido`.
5. Prioriza con el modelo de puntaje (§7). Solo los Tier A y B reciben ficha y borrador.
6. Los mensajes son **borradores**. **Tú nunca contactas a nadie.**
7. No prometas precios, condiciones ni beneficios de salud: todavía no están confirmados (§2).
8. Solo datos comerciales públicos de negocios. Nunca datos de personas (Ley 1581 de 2012).
9. Cada hallazgo útil termina en una hipótesis con su prueba comercial (`INVESTIGACION-MERCADO.md` §7) y se mide con el embudo (§10).
10. Al terminar, actualiza los registros y entrega un resumen corto para Andrés (§12).

## 1. Misión y alcance

**Misión:** construir y mantener la lista de cuentas de Bogotá con más probabilidad de **comprar y volver a comprar** Canívoros, con evidencia suficiente para que el equipo comercial contacte solo a las mejores y sepa qué decirles.

**Qué es un cliente posible:** un negocio u organización de Bogotá que compra alimento para perros para:
- **revenderlo** (tiendas, veterinarias, distribuidores);
- **alimentar a sus propios perros** (criaderos, guarderías, centros de entrenamiento, organizaciones con perros de trabajo);
- **recomendarlo** (veterinarias, criaderos que venden cachorros, entrenadores, clubes).

**Alcance geográfico:** Bogotá D.C. y sus 20 localidades. Municipios vecinos (Chía, Cota, La Calera, Sopó, Tabio, Tenjo…) solo si Andrés lo aprueba; se registran con la marca `fuera de Bogotá`.

**Fuera de alcance, por ahora:**
- **Personas naturales** (dueños de perros, criadores particulares sin negocio): no se prospectan una por una. Al consumidor se le investiga de forma agregada (§4, fase transversal).
- **Compras institucionales** (Policía, Ejército, licitaciones públicas) y grandes superficies: fase posterior, con decisión de Andrés.
- **Gatos:** las cuentas de gatos se marcan para BL-026, que va después del piloto de perros.

**Quién contacta:** el equipo que designe **Andrés Muñoz (Andy)**; en BL-012 son **Omar y el hermano de Sebastián**. Andrés aprueba cada contacto.

**No generes más demanda de la que se puede atender.** La capacidad disponible de producción es `desconocido` (BL-036) y las fallas de máquinas interrumpen la operación (BL-009). Si un segmento implica volúmenes grandes (por ejemplo, cientos de kilos al mes), dilo en el resumen para que Andrés lo evalúe antes de contactar.

### Tareas del backlog que atiende esta carpeta

| Tarea | Qué aporta esta carpeta |
|---|---|
| **BL-010** · Verificar la lista de prospectos | Cuentas verificadas con fuente y fecha |
| **BL-012** · Prospección mayorista: 10 tiendas | Las 10 mejores cuentas de S1/S2, con ficha y borradores |
| **BL-043** · Criadores y clientes de alto volumen | Lista de criaderos de S3 y su perfil |
| **BL-014** · Matriz de microzonas | Densidad de cuentas, aliados y competencia por localidad |
| BL-035 · Validar los distribuidores publicados | Estado de la red actual (lo confirma el equipo) |
| BL-006 / BL-007 · Entrevistas | Preguntas y patrones que salen de la investigación |
| BL-020 · Dos mensajes | Borradores marcados con variante A o B |
| BL-021 · Origen de las ventas | Código o QR por cuenta para atribuir pedidos |
| BL-044 · Hipótesis antes de experimentar | Ficha del experimento antes de cada contacto masivo |
| BL-026 · Gatívoros | Cuentas de gatos, reservadas |

## 2. Qué puede ofrecer Canívoros hoy (y qué no)

| Se sabe (D de la empresa) | Todavía `desconocido` (no prometer) |
|---|---|
| Alimento horneado para perros, hecho en Sopó, con proteína de origen animal (pollo, salmón, cerdo, ternera), listo para servir | Precio a tiendas y a distribuidores confirmado (BL-005) |
| Formatos relatados: hamburguesas y chorizos de 500 g; hamburguesas de 1,5 kg por kilo para volumen | Pedido mínimo para tiendas, margen, plazo de pago |
| Venta por kilo a criadores, con mínimo relatado de 40 kg | Conservación del producto terminado y necesidad de frío en tienda |
| Origen en la crianza de perros de competencia; credibilidad de Omar en ese mundo | Ración por peso del perro (BL-041) |
| Aliados actuales: Manimal (noroccidente) y Sankatin (Bosa) | Capacidad para atender nuevos clientes (BL-036) |
| Ventas jul–oct 2026 separadas en cliente final, almacén y criador, con pedidos de criadores de 40 a 520 kg | Número comercial principal de WhatsApp |

**Consecuencia:** la investigación y los borradores pueden despertar interés y abrir una conversación, pero **no pueden cerrar condiciones**. Lo que falta se registra como pregunta para el equipo (§8).

## 3. Segmentos y prioridad

| ID | Segmento | Cómo compra | Por qué importa (evidencia) | Prioridad |
|---|---|---|---|---|
| **S1** | Tiendas de mascotas: pet shops, tiendas de alimento natural, cadenas y tiendas online | Reventa | 102 cuentas en la lista; el plan prueba aliados locales (experimento 3) | Alta |
| **S2** | Veterinarias con punto de venta | Reventa y recomendación | Manimal, un aliado actual, es veterinaria; el veterinario influye en la elección del alimento | Alta |
| **S3** | Criaderos con presencia comercial | Consumo propio de alto volumen y recomendación a quienes compran cachorros | Pedidos de criadores de 40–520 kg en el Excel (BL-043); origen de la marca | Alta |
| **S4** | Servicios caninos: entrenamiento y adiestramiento, guarderías, hoteles, colegios caninos, peluquerías y spas | Consumo propio, reventa y recomendación | Club Canes (Villavicencio), un aliado publicado, es centro de entrenamiento; segmento «perros activos» del plan | Media |
| **S5** | Perros de trabajo y deporte: empresas de seguridad con guías caninos, clubes de deporte canino y de raza | Consumo propio de alto volumen y comunidad | (H) sin evidencia todavía; encaja con el origen de la marca | Exploratoria |
| **S6** | Distribuidores mayoristas y almacenes agro | Reventa a otras tiendas | 7 cuentas en la lista; decisor difícil y márgenes `desconocido` | Baja |

Orden de trabajo sugerido (H): **S1 y S2 en las microzonas candidatas → S3 → S4 → S5 → S6.** Andrés puede cambiarlo.

### Propuesta a probar por segmento (H)

| Segmento | Necesidad probable (H) | Propuesta a probar | Evidencia comercial esperada |
|---|---|---|---|
| S1 | Rotación y margen; diferenciarse con una marca natural local | Pedido inicial pequeño, material y QR por tienda | Reposición, no solo el primer pedido |
| S2 | Recomendar con respaldo técnico | Ficha técnica y composición cuando existan (BL-016) | Pedido y recomendación registrada con código |
| S3 | Alimentar muchos perros con calidad y costo predecible | Pedido programado por volumen y referidos a compradores de cachorros (BL-043) | Pedidos recurrentes en kg |
| S4 | Alimento práctico para su rutina; producto para recomendar o vender | Producto listo para servir; muestra para sus perros residentes | Consumo propio y pedidos referidos |
| S5 | Rendimiento y abastecimiento estable | Conversación exploratoria sobre volumen | Solo aprendizaje en esta fase |

## 4. Proceso de investigación en 5 fases

Cada lote tiene máximo 10 cuentas de un mismo segmento y una misma zona; S1 y S2 pueden ir juntos. Las fases 2 a 5 se repiten por lote; la fase 1 se actualiza cuando aparece información nueva del mercado.

### Fase 1 · Mapa del mercado (desk research)

Antes de buscar cuentas, entiende el terreno y documéntalo en `INVESTIGACION-MERCADO.md`:
- **Tamaño de referencia:** datos oficiales de tenencia de perros en Bogotá (DANE), con año y enlace. Son referencia histórica, no demanda de Canívoros.
- **Oferta por localidad:** cuántos puntos de venta de mascotas, veterinarias y servicios caninos hay en cada localidad (conteos de Maps con la búsqueda exacta y la fecha).
- **Competencia por localidad:** dónde están los distribuidores publicados de Pixie, Peluditos BARF, Vital Doggy, Rawf y Kanuto (cruza con `../competencia/COMPETENCIA.md`).
- **Microzonas candidatas:** evidencia para los 5 criterios del plan (demanda, contribución, aliados, logística, competencia). No puntúes por intuición ni uses el estrato como sustituto de la disposición a pagar.

### Fase 2 · Construcción de la lista (sourcing)

Usa varias técnicas y anota en la columna *Fuente* cuál produjo cada cuenta:

| Técnica | Cómo se aplica a Canívoros |
|---|---|
| **Distribución de la competencia** | Las páginas de distribuidores de Pixie, Peluditos BARF, Vital Doggy, Rawf y Kanuto muestran quién ya vende natural. Es la fuente más rica de S1 y S2 |
| **Cuentas parecidas a las mejores** | Busca negocios parecidos a los aliados que sí funcionan (Manimal, Sankatin) y al tipo de criador que más compra. Cuando BL-004 identifique los mejores clientes, úsalos como modelo (sin copiar sus nombres si son personas) |
| **Búsqueda por zona** | Google Maps por tipo + localidad + barrio (§5.2), recorriendo la zona de forma sistemática |
| **Comunidades** | Clubes de raza, clubes de deporte canino, exposiciones y eventos caninos, donde están los criaderos (S3) y los entrenadores (S4) |
| **Eventos disparadores** | Aperturas o nuevas sedes, nuevas líneas de alimento natural, quejas por agotados de su marca natural, publicaciones buscando proveedores |
| **Canales digitales** | Rappi (categoría mascotas), tiendas online, perfiles comerciales de Instagram, Facebook y TikTok |

### Fase 3 · Verificación y enriquecimiento

Aplica la mini auditoría de §6 a cada cuenta del lote. Sin verificación no hay puntaje alto ni borrador.

### Fase 4 · Puntaje y tiers

Aplica el modelo de §7. Ordena el lote de mayor a menor puntaje.

### Fase 5 · Plan de abordaje

Para cada cuenta Tier A, escribe una ficha completa (§9.1) con la secuencia de 3 borradores (§9.2). Para Tier B, ficha corta y un borrador. Tier C queda en la lista sin borrador.

### Fase transversal · Investigación del consumidor (siempre agregada)

Sirve para entender qué valoran los dueños de perros y para afinar los mensajes. **Nunca registres personas.**
- **Reseñas** de tiendas y competidores en Maps, Rappi y webs: cuenta cuántas revisaste, de qué fechas y clasifícalas por tema (aceptación del perro, precio, entrega, empaque, atención, disponibilidad).
- **Escucha social:** temas y preguntas frecuentes en publicaciones públicas sobre alimentación natural en Bogotá (BARF, alimento horneado, «comida natural para perros»). Registra patrones, no comentarios aislados ni autores.
- **Resultado:** patrones con número de casos, preguntas nuevas para el guion de BL-006 e hipótesis de mensaje para BL-020.

## 5. Fuentes y búsquedas

### 5.1 Fuentes y su fiabilidad

| Fuente | Para qué | Etiqueta habitual |
|---|---|---|
| Google Maps (ficha, fotos, reseñas) | Existencia, horario, dirección comercial, marcas en estantería, congelador, actividad | (E) si lo ves tú, con fecha |
| Web o tienda online del negocio | Marcas, categorías, domicilios, servicios | (E) |
| Instagram, Facebook o TikTok del negocio | Actividad, marcas, público (perros o gatos), tamaño de la operación | (E) lo publicado; seguidores y likes (V) |
| Directorios de distribuidores de las marcas | Quién vende Pixie, BARF, etc. | (D) de la marca |
| Rappi y marketplaces | Si vende en línea y qué marcas | (E) con fecha |
| RUES (registro mercantil) | Confirmar que el negocio existe como empresa | (E) |
| Clubes caninos, clubes de raza y calendarios de exposiciones | Criaderos y entrenadores (S3, S4) | (D) |
| Índices de búsqueda y directorios de terceros (exa.ai, páginas amarillas) | Pistas | (V) hasta confirmar |

### 5.2 Búsquedas por segmento

Reemplaza `{localidad}`, `{barrio}` y `{raza}`; guarda la búsqueda exacta y la fecha en el historial del lote.

| Segmento | Búsquedas sugeridas |
|---|---|
| S1 | «pet shop {barrio}», «tienda de mascotas {localidad}», «comida natural para perros {localidad}», «BARF {localidad}», «alimento natural perros Bogotá domicilio» |
| S2 | «veterinaria {barrio}», «clínica veterinaria {localidad}», «veterinaria con tienda {localidad}» |
| S3 | «criadero de perros Bogotá», «criadero {raza} Bogotá», «cachorros {raza} Bogotá criadero», perfiles de criaderos enlazados desde clubes de raza |
| S4 | «adiestramiento canino Bogotá», «colegio canino {localidad}», «guardería canina {localidad}», «hotel para perros Bogotá», «peluquería canina {barrio}» |
| S5 | «empresa de seguridad con caninos Bogotá», «club de agility Bogotá», «club de deporte canino Bogotá» |
| S6 | «distribuidor de alimento para mascotas Bogotá», «mayorista mascotas Corabastos» |

## 6. Mini auditoría (verificar una cuenta)

**Para todos los segmentos:**
1. **Existe y opera:** ficha de Maps abierta, reseña reciente o publicación de los últimos 60 días.
2. **Datos comerciales:** dirección comercial (localidad oficial y barrio), web, redes, canal comercial público (WhatsApp o correo del negocio).
3. **Encaje con la categoría:** marcas que vende o que da a sus perros; si trabaja con alimento natural, BARF u horneado.
4. **Público:** perros, gatos o mixto.
5. **Tamaño:** número de sedes, número de reseñas, servicios, perros visibles.
6. **Disparadores:** aperturas, nuevas líneas, quejas por agotados, búsqueda de proveedores.

**Señales específicas:**

| Segmento | Qué más revisar |
|---|---|
| S1 / S2 | Fotos de estantería; congelador o nevera de alimento natural; si hace domicilios o vende en Rappi; en veterinarias, si tiene servicio de nutrición |
| S3 | Razas que cría; si publica camadas con frecuencia; si recomienda un alimento a quienes compran cachorros; si participa en exposiciones |
| S4 | Servicios (entrenamiento, guardería, hotel); si vende productos; capacidad aproximada que publica (perros por día) |
| S5 | Si declara públicamente unidades caninas; tipo de perros de trabajo |
| S6 | Marcas que distribuye; a qué tipo de tiendas despacha; zonas de cobertura |

**Entregable por cuenta verificada:** 3 hallazgos con evidencia (URL, fecha y fragmento o descripción), segmento, encaje, puntaje y tier (§7), y lo que queda por validar en conversación (§8).

## 7. Modelo de puntaje

### 7.1 Filtros previos (si uno se cumple, no se puntúa)

Cerrado o sin presencia verificable · duplicado · ya es cliente o aliado (pasa a `Existente`) · persona natural sin negocio · solo gatos (se marca para BL-026) · fuera de alcance sin aprobación.

### 7.2 Puntaje de 0 a 100

| Bloque | Criterio | Puntos |
|---|---|---|
| **Encaje (45)** | Trabaja con alimento natural, BARF u horneado | 15 |
| | Su público o sus perros son mayoritariamente perros | 10 |
| | Volumen potencial: varias sedes, más de 100 reseñas, criadero o guardería con muchos perros | 10 |
| | Tiene frío para alimento natural (congelador o nevera) | 5 |
| | Maneja marcas premium o naturales de precio alto (no uses el estrato como sustituto) | 5 |
| **Oportunidad (30)** | Actividad reciente: publicación en 60 días o reseña en 30 días | 10 |
| | Evento disparador observado (§4, fase 2) | 10 |
| | Dentro o junto a una microzona candidata (BL-014) | 10 |
| **Acceso (25)** | Canal comercial público verificado | 10 |
| | Rol del decisor identificable en fuente pública (dueño, compras, administrador); solo el rol, sin datos personales | 5 |
| | Puente cálido: aliado, cliente actual, club o red de Omar (lo marca el equipo; el agente escribe `desconocido`) | 10 |

**Peso de la evidencia:** un criterio con (E) suma todos sus puntos; con (D), la mitad; con (V) o `desconocido`, cero. Así una cuenta solo sube de verdad cuando se verifica.

### 7.3 Tiers

| Tier | Puntaje | Qué se entrega |
|---|---|---|
| **A** | 70 o más | Ficha completa y secuencia de 3 borradores personalizados. Candidata a visita |
| **B** | 50 a 69 | Ficha corta y un borrador |
| **C** | 30 a 49 | Queda en la lista, sin borrador |
| — | Menos de 30 | `descartado` con motivo, o en reserva si Andrés lo pide |

**Calibración:** los pesos son una propuesta. Al cerrar las 4 semanas de BL-012, compara respuesta y pedido por tier. Si un tier bajo convierte igual que uno alto, ajusta los pesos y anótalo en el historial de `PROSPECTOS.md`.

## 8. Calificación en la conversación (la hace el equipo, no el agente)

El agente deja estas preguntas como **(V) por validar** en la ficha. Marco N-E-D-A:

| Letra | Qué confirmar | Preguntas sugeridas |
|---|---|---|
| **N** · Necesidad | ¿Tienen un problema que Canívoros resuelve? | ¿Qué alimento natural venden o dan hoy? ¿Qué les piden los clientes que no consiguen? ¿Qué falla con su proveedor actual? |
| **E** · Encaje operativo | ¿Pueden manejar el producto? | ¿Tienen espacio de congelador o nevera? ¿Cuánto venden o consumen al mes? ¿Cada cuánto reponen? |
| **D** · Decisor | ¿Quién decide y cómo? | ¿Quién decide qué marcas entran? ¿Cómo prueban una marca nueva? |
| **A** · Acuerdo | ¿Qué condiciones necesitan? | Pedido mínimo, margen, plazo de pago, devoluciones, material de venta, si aceptan un código o QR para registrar ventas |

## 9. Plan de abordaje

### 9.1 Ficha de cuenta

```markdown
#### [P-ID] [Nombre] — [Segmento] · Tier [A/B] · [puntaje]/100
- Tipo / localidad (barrio) / dirección comercial:
- Web · Maps · Instagram:
- Canal comercial público:
- Marcas o alimento observado (E):
- Frío para alimento natural: sí / no / desconocido
- Público: perros / gatos / mixto · Tamaño:
- Rol del decisor: desconocido
- Puente cálido: desconocido (lo marca el equipo)
- Estado:

**Por qué esta cuenta (3 hallazgos)**
1. (E) [hecho] — URL · fecha
   (H) [qué significa para Canívoros]
2. ...
3. ...

**Ángulo de entrada (H):** [la necesidad probable y cómo se conecta con Canívoros]
**Puntaje:** encaje __/45 · oportunidad __/30 · acceso __/25
**Por validar (N-E-D-A):** ...

**Secuencia de borradores (no enviados) · variante [A/B] · canal sugerido [WhatsApp/visita/correo]:**
1. Toque 1: > ...
2. Toque 2 (días 3–4): > ...
3. Toque 3 (días 8–10): > ...
```

### 9.2 Reglas de la secuencia

- **Máximo 3 toques.** Si la cuenta dice que no, se marca `perdido` con el motivo y no se insiste.
- **Toque 1:** presentación + una observación verdadera y específica + propuesta pequeña + pregunta fácil.
- **Toque 2:** aporta algo útil (qué es el producto, cómo se usa, propuesta de muestra), sin repetir el primer mensaje.
- **Toque 3:** cierre amable que deja la puerta abierta.
- **Personalización:** al menos un hecho (E) de la cuenta en el toque 1. Nada genérico.
- **Variantes:** marca cada borrador como **A (horneado)** o **B (facilidad de uso)** y altérnalas dentro del lote (BL-020).
- **Contenido permitido:** solo los mensajes de `../AGENTS.md` §3. Sin beneficios de salud, sin «sin subproductos», sin «registro ICA», **sin precios ni condiciones** y sin números de Canívoros (`[número comercial por definir]`).
- **Muestras:** tienen costo; márcalas «requiere aprobación y presupuesto (BL-044)».
- **Tono:** cercano y profesional, de 4 a 5 líneas. Sin presión ni escasez falsa. Horario comercial, nunca domingos ni festivos. Las reglas exactas de contacto comercial en Colombia deben confirmarse con alguien que conozca la norma (BL-058).

### 9.3 Plantillas de toque 1 por segmento

Reemplaza lo que está entre corchetes. **No se envían.**

> **S1 · Tienda · A (horneado):** Hola, ¿cómo están? Les escribe [nombre] de Canívoros, alimento horneado para perros hecho en Sopó con proteína de origen animal. Vimos que en [tienda] manejan [marca natural observada], así que sus clientes ya buscan alimento natural. ¿Les interesaría conocer nuestras condiciones para tiendas? ¿Con quién podríamos hablar de compras?

> **S1 · Tienda · B (facilidad de uso):** Hola, ¿cómo están? Les escribe [nombre] de Canívoros. Hacemos en Sopó alimento natural para perros, horneado y listo para servir. Vimos que en [tienda] [observación verificada]. ¿Les gustaría que les dejáramos una muestra para conocerlo? ¿Con quién podríamos hablar de compras?

> **S2 · Veterinaria:** Hola, doctor(a) o equipo de [veterinaria]. Les escribe [nombre] de Canívoros, alimento horneado para perros hecho en Sopó con proteína de origen animal. Vimos que [observación verificada: punto de venta, servicio de nutrición]. Nos gustaría presentarles el producto. ¿Con quién podríamos coordinar una visita corta? *(La ficha técnica depende de BL-016: no la ofrezcas hasta que exista.)*

> **S3 · Criadero:** Hola, ¿cómo están? Les escribe [nombre] de Canívoros. Nacimos en la crianza de perros de competencia y hacemos en Sopó alimento horneado con proteína de origen animal. Vimos que en [criadero] crían [raza observada]. ¿Les interesaría conocer cómo trabajamos con criaderos que compran por volumen?

> **S4 · Servicio canino:** Hola, ¿cómo están? Les escribe [nombre] de Canívoros, alimento horneado para perros, hecho en Sopó y listo para servir. Vimos que en [negocio] [servicio observado: entrenamiento, guardería, hotel]. ¿Les gustaría probarlo con sus perros o conocerlo para recomendarlo a sus clientes? ¿Con quién podríamos hablar?

## 10. Métricas del embudo

| Etapa | Quién la registra | Métrica |
|---|---|---|
| Identificadas | Agente | Cuentas nuevas por segmento y localidad |
| Verificadas | Agente | Verificadas ÷ revisadas; descartadas y motivo |
| Tier A / B | Agente | Distribución por tier |
| Listas para contactar | Agente | Fichas con borradores aprobables |
| Contactadas | Equipo | Contactadas ÷ listas |
| Respondieron | Equipo | Respuesta ÷ contactadas, por tier y por variante A/B |
| Reunión o muestra | Equipo | Muestras ÷ respuestas |
| Primer pedido | Equipo | Pedidos ÷ contactadas; COP solo con precio confirmado |
| Reposición | Equipo | Reposición ÷ primer pedido. **Es la métrica que importa** |

- Antes de cualquier contacto masivo debe existir la ficha de BL-044: hipótesis, métrica principal, número de casos, gasto máximo y regla de seguir, ajustar o parar.
- Una compra inicial no demuestra demanda: mide la reposición.
- Cada pedido debe quedar con su origen (cuenta, lote, variante, código o QR) para BL-021.

## 11. Evidencia y calidad de datos

- Etiquetas **(E)**, **(D)**, **(H)** y **(V)** de `../AGENTS.md` §3. Lo que no sabes: `desconocido`.
- Aparecer en el directorio de distribuidores de una marca es **(D) de esa marca**; verlo en la estantería o en la web del negocio es **(E)**.
- **Afirmaciones de ausencia** («no vende natural») solo si revisaste web, Maps y redes, y lo dices.
- **Normaliza:** zona = localidad oficial + barrio; teléfonos de Colombia (celular `3xx xxx xxxx`, fijo `601 xxx xxxx`); URLs completas; `place_id` de Maps cuando lo tengas.
- **Deduplica** en este orden: `place_id` → dominio web → Instagram → teléfono (solo dígitos) → nombre + dirección. Las cadenas van en una sola fila con sus sedes listadas.
- **Revisa que no sea ya cliente:** compara con la *Red actual publicada* de `PROSPECTOS.md` y con los clientes de tipo «almacén» y «criador» de `../ventas_canivoros_2026.xlsx` (solo nombres de negocios; no copies nombres de personas). Si coincide, márcalo `Existente` y avisa a Andrés.
- **No inventes** precios, márgenes, volúmenes, ventas ni número de perros.

## 12. Cómo actualizar los archivos

- **`INVESTIGACION-MERCADO.md`:** hallazgos de la fase 1 y de la investigación del consumidor, con fuente y fecha.
- **`PROSPECTOS.md`:**
  - **Registro:** una fila por cuenta, con ID `P` + tres dígitos (el siguiente libre; no se reutiliza), segmento, tipo, zona, dirección comercial, web/Instagram, teléfono público, marcas según fuente, encaje, puntaje, estado y fuente.
  - **Fichas:** las de Tier A y B, en la sección *Fichas verificadas*.
  - **Resumen, conteos por segmento y métricas:** recalcúlalos después de cada lote.
  - **Historial:** agrega arriba `### Lote AAAA-MM-DD · <segmento> · <zona>` con búsquedas exactas, cuentas revisadas, nuevas, verificadas, descartadas y limitaciones.
- **Estados:**

```text
Agente:           por_verificar → verificado → listo_para_contactar
                        └───────────→ descartado (con motivo)
Equipo comercial: contactado → respondio → muestra → pedido → reposicion
                        └──────────────────────────────→ perdido (con motivo)
```

  - El agente pone `por_verificar`, `verificado`, `listo_para_contactar` y `descartado`.
  - **Solo el equipo comercial** (Andrés o a quien él designe) pone `contactado`, `respondio`, `muestra`, `pedido`, `reposicion` y `perdido`. **Nunca** cambies esos estados ni sus notas.
  - `listo_para_contactar` = Tier A o B, ficha completa, borradores y sin duplicados. Equivale a la etapa «Por contactar» del CRM en Odoo (BL-010). La carga al CRM la hacen Andrés o Sebastián.
- **Resumen para Andrés** al cerrar un lote, en 5 líneas: cuentas revisadas y verificadas, cuántas Tier A y B, las 3 mejores y por qué, alertas (por ejemplo, volúmenes que superan la capacidad conocida) y decisiones que necesita tomar.

## 13. Límites (no negociables)

- **No contactes.** No envíes mensajes, no llames, no llenes formularios, no crees cuentas, no sigas ni comentes en redes. Todo contacto lo aprueba Andrés y lo hace el equipo que él designe.
- **Solo datos comerciales públicos de negocios.** No guardes nombres, cédulas, celulares personales, direcciones de vivienda ni fotos de dueños, empleados, clientes o criadores particulares. Si un negocio funciona en una vivienda, registra el negocio sin su dirección. Rige la Ley 1581 de 2012.
- **Reseñas y redes:** usa patrones agregados; no guardes autores ni comentarios con datos de personas.
- **No evadas bloqueos** ni hagas scraping contra los términos de servicio. Si una fuente bloquea o pide login, marca «No verificado».
- **No compres** ni pidas cotizaciones haciéndote pasar por cliente.
- **No subas contraseñas ni tokens** al repositorio.

## 14. Checklist antes de entregar un lote

- [ ] Máximo 10 cuentas, de un mismo segmento (o S1/S2) y una misma zona.
- [ ] Deduplicado contra `PROSPECTOS.md`, la red actual y los clientes actuales.
- [ ] Cada cuenta verificada tiene 3 hallazgos con URL y fecha.
- [ ] Puntaje calculado con el peso de la evidencia; tier asignado.
- [ ] Fichas Tier A con secuencia de 3 borradores; Tier B con 1 borrador.
- [ ] Borradores sin precios, sin beneficios de salud, sin números de Canívoros, con variante A/B.
- [ ] Ningún dato personal ni dirección de vivienda.
- [ ] *Resumen*, conteos, *Historial* y, si aplica, `INVESTIGACION-MERCADO.md` actualizados.
- [ ] Resumen de 5 líneas para Andrés.
