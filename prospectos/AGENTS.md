# Instrucciones para agentes · prospección B2B de Canívoros en Bogotá

> Lee este archivo completo antes de investigar. Aplica a cualquier agente (Claude, ChatGPT, Gemini u otro) que continúe la prospección en esta carpeta.
> Las reglas comunes del proyecto (evidencia, datos personales, mensajes de marca, Git) están en `../AGENTS.md` y también aplican aquí.
> Última actualización: 2026-11-02.

---

## 1. Contexto y objetivo

- **Canívoros** hace alimento natural horneado para perros (hamburguesas y chorizos de pollo, salmón, cerdo y ternera, según la operación; catálogo por confirmar en BL-005) en Sopó, Cundinamarca. **Gatívoros** es su línea para gatos. Ver `../CANIVOROS-REFERENCIA-EMPRESA.md` (lo que dice la marca) y `../erp.md` (cómo opera).
- Hoy vende por WhatsApp, a criadores y por unos pocos aliados. En Bogotá el sitio publica dos: **Clínica Veterinaria Manimal** (noroccidente) y **Sankatin PetShop** (Bosa).
- **Objetivo de esta carpeta:** encontrar y verificar **tiendas, veterinarias, pet shops, centros de entrenamiento y distribuidores de Bogotá** que puedan vender Canívoros, para el experimento de aliados locales del plan (`../CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, experimento 3).
- **Backlog:**

| Tarea | Qué aporta esta carpeta |
|---|---|
| **BL-010** · Verificar la lista de prospectos | 20–30 prospectos de encaje Alto verificados, con fuente y fecha |
| **BL-012** · Prospección mayorista: 10 tiendas | Las 10 tiendas elegidas, con ficha y borrador de mensaje |
| BL-035 · Validar los distribuidores publicados | Estado de los aliados actuales (P001, P002 y la red de fuera de Bogotá) |
| BL-014 · Matriz de microzonas | Densidad de prospectos y aliados por zona |
| BL-021 · Origen de las ventas | Código o QR por tienda para atribuir pedidos |
| BL-026 · Gatívoros en veterinarias | Tiendas de gatos, reservadas para después del piloto de perros |

- **Quién contacta:** el equipo que designe **Andrés Muñoz (Andy)**; en BL-012 son **Omar y el hermano de Sebastián**. **Tú nunca contactas a nadie.**
- **La oferta a tiendas todavía no está definida:** precio a distribuidor, pedido mínimo, presentaciones y condiciones dependen de BL-005. No escribas precios ni condiciones en ningún mensaje.

## 2. Cliente ideal (ICP)

**Incluir:**
- Pet shops y tiendas de alimento para mascotas con local en Bogotá (también con venta online).
- Clínicas veterinarias con punto de venta.
- Centros de entrenamiento, guarderías y criaderos que venden a sus clientes.
- Distribuidores y cadenas (con cautela: el decisor es más difícil de alcanzar y el ciclo es más largo).

**Señales de buen encaje** (anótalas con evidencia):
1. **Ya vende alimento natural:** Pixie, BARF (Peluditos BARF, Vital Doggy, Rawf…), horneado (Kanuto, VITA) u otra línea natural. Su cliente ya conoce la categoría.
2. **Tiene congelador o nevera para alimento natural** (visible en fotos o mencionado en su web). Es relevante porque Canívoros se vende en hamburguesas y chorizos y aún no está confirmado si exige frío en tienda (`desconocido`, BL-005).
3. **Clientela de perros**, no solo de gatos. Las tiendas solo de gatos se marcan para BL-026.
4. **Actividad comercial reciente:** reseñas recientes en Maps, publicaciones en los últimos 60 días, domicilios o presencia en Rappi.
5. **Cerca de una microzona candidata** (§2.1).

### 2.1 Zonas prioritarias

Son propuestas hasta cerrar BL-014:
1. **Norte:** Suba (noroccidente, alrededor de Manimal en la Calle 134) y el vecino Usaquén (Cedritos, calles 134–165).
2. **Sur:** Bosa y Kennedy, alrededor de Sankatin.
3. Después: Chapinero, Engativá, Teusaquillo, Barrios Unidos y Fontibón.

### 2.2 Excluir, salvo que Andrés lo pida

- Negocios cerrados o sin presencia verificable.
- Duplicados de `PROSPECTOS.md` (§3).
- Venta a consumidor final: esta carpeta es B2B.
- Negocios que funcionan en una vivienda sin local comercial: se puede registrar el negocio, pero no su dirección.

### 2.3 Criterios de encaje

| Encaje | Regla |
|---|---|
| **Alto** | Vende alimento natural (señal 1), verificado en una fuente del propio negocio: web, fotos de Maps o Instagram. |
| **Medio** | Vende premium (Taste of the Wild, Acana, Orijen, Nupec, Hill's…) o tiene clientela de alto gasto, pero no se observa natural. |
| **Bajo** | Solo concentrados masivos, o encaje dudoso. |
| **Existente** | Aliado o distribuidor actual de Canívoros (confirmar si sigue activo en BL-035). |

En la lista inicial, el encaje Alto se basa en los **directorios de distribuidores de las marcas** (Pixie, Peluditos BARF, Vital Doggy). Eso es una declaración de la marca (D), no un hecho sobre la tienda: **sigue `por_verificar` hasta confirmarlo en una fuente del negocio**.

## 3. Antes de empezar

1. **Lee `PROSPECTOS.md` completo**, incluida la sección *Alertas de calidad*. Es el único registro de prospectos.
2. **Deduplica** antes de investigar, en este orden: `place_id` de Google Maps → dominio web → Instagram → teléfono normalizado (solo dígitos) → nombre + dirección. Una fila por negocio independiente; las cadenas van en una sola fila con sus sedes listadas (como P019 CEBA).
3. **Revisa que no sea ya cliente o aliado:** compáralo con la *Red actual publicada* de `PROSPECTOS.md` y, si tienes acceso, con los clientes de tipo «almacén» de `../ventas_canivoros_2026.xlsx` (compara solo nombres de negocios; no copies nombres de personas). Si coincide, márcalo `Existente` y avisa a Andrés.
4. **La lista inicial se hizo con ayuda de IA** y tiene muchos campos `desconocido`. Ningún dato suyo es (E) hasta re-verificarlo.
5. **Si no tienes acceso a la web**, no inventes datos: detente y dilo.

## 4. Flujo de trabajo

**Fase 0 · Elegir el lote.** Toma un máximo de **10 prospectos de una misma zona**, empezando por la lista *Candidatos para el próximo lote* de `PROSPECTOS.md`. Así se puede planear la visita o el contacto por zona.

**Fase 1 · Descubrimiento** (prospectos nuevos, unos 2 minutos por negocio): Google Maps por tipo y zona («pet shop Suba», «veterinaria Usaquén», «alimento BARF Bogotá», «comida natural perros Cedritos») y directorios de distribuidores de las marcas naturales. Registra nombre, `place_id`, tipo, zona, dirección comercial, web, Instagram, teléfono comercial público, marcas y fuente.

**Fase 2 · Verificación con mini auditoría comercial** (unos 15 minutos por negocio). Aplica §5.

**Fase 3 · Entrega.** Actualiza `PROSPECTOS.md` según §8 y pasa el checklist de §11.

## 5. Mini auditoría comercial (verificar un prospecto)

Revisa, en este orden:

1. **Google Maps:** que exista y esté abierto; dirección, horario, calificación y **número de reseñas** (y la fecha de la más reciente). En las fotos: marcas en estantería y **congelador o nevera** de alimento natural.
2. **Web o tienda online:** marcas que vende; si tiene categoría «natural», «BARF», «horneado» o «congelados»; si vende online, hace domicilios o está en Rappi.
3. **Instagram o Facebook:** fecha de la última publicación, marcas que publica, si promueve alimento natural, si su público es de perros, de gatos o mixto. Los seguidores y likes son (V).
4. **Teléfono o WhatsApp público:** solo comprueba que tenga formato válido de Colombia (celular `3xx xxx xxxx`, fijo `601 xxx xxxx`). **No escribas ni llames.**

**Entregable por prospecto:**
- **3 hallazgos con evidencia** (URL, fecha y fragmento o descripción exacta). Por ejemplo: «vende Pixie (foto de estantería en Maps, 2026-11-05)», «su web tiene categoría BARF», «tiene congelador de alimento natural (foto en Maps)».
- **Encaje** (Alto, Medio, Bajo) con la regla de §2.3.
- **Primer mensaje redactado y sin enviar** (§7).
- **Por validar (V)** en la conversación, que lleva el equipo y no tú: marcas con mayor salida, pedido mínimo que manejan, frecuencia de reposición, plazo de pago, margen que piden, devoluciones, espacio de congelador o nevera, y si aceptarían un código o QR para registrar ventas.

## 6. Precisión y evidencia

- Usa las etiquetas **(E)**, **(D)**, **(H)** y **(V)** de `../AGENTS.md` §3.
- Aparecer en el directorio de distribuidores de una marca es **(D) de esa marca**; verlo en la estantería o la web del negocio es **(E)**.
- Si no encuentras un dato, escribe `desconocido`. Nunca lo estimes.
- **Afirmaciones de ausencia** («no vende natural») solo si revisaste web, Maps e Instagram, y lo dices.
- **No inventes precios, márgenes, volúmenes ni ventas** de Canívoros ni del prospecto.

## 7. Primer mensaje (borrador; nunca se envía sin aprobación de Andrés)

- **Canal:** WhatsApp comercial público del negocio o visita en persona. Indica cuál sugieres.
- **Estructura:** saludo y quién escribe → **una observación específica y verdadera** del negocio (de un hallazgo E) → propuesta pequeña (conocer sus condiciones o dejar una muestra) → pregunta fácil de responder (con quién hablar de compras).
- **Reglas:**
  - Máximo 4–5 líneas, tono cercano y profesional, de usted o de tú según el estilo del negocio en sus redes.
  - **Habla de perros.** Gatívoros solo si la tienda es de gatos y Andrés lo pide (BL-026).
  - Usa solo los mensajes permitidos de `../AGENTS.md` §3. Sin beneficios de salud, sin «sin subproductos», sin «registro ICA» y **sin precios ni condiciones** (BL-005).
  - **No pongas números ni enlaces de Canívoros:** escribe `[número comercial por definir]`. Hay tres números publicados y falta elegir el principal.
  - Ofrecer muestras tiene costo: márcalo como «requiere aprobación y presupuesto (BL-044)».
  - Nada de presión, urgencia ni escasez falsa.
- **Variante de mensaje:** marca cada borrador como **A (horneado)** o **B (facilidad de uso)** para que BL-020 pueda comparar resultados. Alterna las variantes dentro de un mismo lote.

**Plantillas** (reemplaza lo que está entre corchetes; no envíes):

> **A · horneado:** Hola, ¿cómo están? Les escribe [nombre] de Canívoros, alimento horneado para perros hecho en Sopó con proteína de origen animal. Vimos que en [negocio] manejan [marca natural observada], así que sus clientes ya buscan alimento natural. ¿Les interesaría conocer nuestras condiciones para tiendas? ¿Con quién podríamos hablar de compras?

> **B · facilidad de uso:** Hola, ¿cómo están? Les escribe [nombre] de Canívoros. Hacemos en Sopó alimento natural para perros, horneado y listo para servir. Vimos que en [negocio] [observación verificada]. ¿Les gustaría que les dejáramos una muestra para conocerlo? ¿Con quién podríamos hablar de compras?

## 8. Cómo actualizar `PROSPECTOS.md`

- **Registro:** una fila por prospecto, con ID `P` + tres dígitos (el siguiente libre; no se reutilizan), nombre, tipo, zona, dirección comercial, web/Instagram, teléfono público, marcas según fuente, encaje, estado y fuente.
- **Ficha completa** (formato §9) para cada prospecto auditado de encaje Alto o Medio.
- **Estados:**

```text
Agente:          por_verificar → verificado → listo_para_contactar
                       └───────────→ descartado (con motivo)
Equipo comercial: contactado → respondio → muestra → pedido → reposicion
                       └──────────────────────────────→ perdido (con motivo)
```

  - El agente pone `por_verificar`, `verificado`, `listo_para_contactar` y `descartado`.
  - **Solo el equipo comercial** (Andrés o a quien él designe) pone `contactado`, `respondio`, `muestra`, `pedido`, `reposicion` y `perdido`. **Nunca** cambies esos estados ni sus notas.
  - `listo_para_contactar` = ficha completa + borrador + sin duplicados. Equivale a la etapa «Por contactar» del CRM en Odoo (BL-010). La carga al CRM la hacen Andrés o Sebastián, no el agente.
- **Resumen y métricas BL-012:** recalcula los conteos del *Resumen* después de cada lote. Las métricas comerciales (contactados, respondieron, pedido, reposición, COP, motivo de no compra) las registra el equipo; sin cifras inventadas.
- **Historial:** agrega arriba `### Lote AAAA-MM-DD · <zona>` con búsquedas hechas, prospectos revisados, verificados, descartados, nuevos y limitaciones.

## 9. Formato de ficha

```markdown
#### [P-ID] [Nombre] — Encaje [Alto/Medio]
- Tipo / zona / dirección comercial:
- Web · Maps · Instagram:
- Contacto comercial público:
- Marcas observadas (E):
- Congelador o nevera de alimento natural: sí / no / desconocido
- Público: perros / gatos / mixto
- Decisor: desconocido
- Estado:

**Hallazgos**
1. (E) [hecho] — URL · fecha
   (H) [interpretación]
2. ...
3. ...

**Declaraciones (D):** ...
**Por validar (V):** pedido mínimo, margen requerido, rotación, plazo de pago, espacio de frío, código/QR...

**Borrador de primer mensaje (no enviado) · variante [A/B] · canal sugerido [WhatsApp/visita]:**
> ...
```

## 10. Límites (no negociables)

- **No contactes.** No envíes mensajes, no llames, no llenes formularios, no crees cuentas, no comentes en redes. Todo contacto lo aprueba Andrés y lo hace el equipo que él designe.
- **Solo datos comerciales públicos del negocio.** No guardes datos de dueños, empleados ni clientes (cédulas, celulares personales, direcciones de vivienda, fotos de personas). Rige la Ley 1581 de 2012.
- **No evadas bloqueos** ni hagas scraping contra los términos de servicio. Si una fuente bloquea, marca «No verificado».
- **No subas contraseñas ni tokens** al repositorio.

## 11. Checklist antes de entregar un lote

- [ ] Máximo 10 prospectos, de una misma zona.
- [ ] Deduplicado contra `PROSPECTOS.md`, la red actual y los clientes tipo almacén.
- [ ] Cada prospecto auditado tiene 3 hallazgos con URL y fecha.
- [ ] Hechos, declaraciones, hipótesis y por validar están etiquetados.
- [ ] Ningún precio, margen ni venta inventado; lo que falta dice `desconocido`.
- [ ] Borradores marcados como no enviados, con variante A/B, sin precios ni números de Canívoros.
- [ ] Ningún dato personal ni dirección de vivienda.
- [ ] *Resumen* e *Historial de lotes* actualizados.
