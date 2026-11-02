# Instrucciones para agentes de IA: prospección B2B de Canívoros / Gatívoros

> Lee este archivo completo antes de investigar. Aplica a cualquier agente (Claude, ChatGPT, Gemini u otro) que continúe la prospección en esta carpeta.
> Última actualización: 2026-11-02.

---

## 1. Contexto

- **Canívoros** (perros) y **Gatívoros** (gatos) son alimento natural **horneado**, con proteína animal (pollo, salmón, cerdo), producido en Sopó (Cundinamarca). Ver `../CANIVOROS-REFERENCIA-EMPRESA.md`.
- **Objetivo de esta carpeta:** encontrar y verificar **tiendas, veterinarias, pet shops, centros de entrenamiento y distribuidores de Bogotá** que puedan vender Canívoros/Gatívoros (venta B2B / aliados), según el plan `../CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` (experimento de aliados locales).
- **Andrés Muñoz (Andy)** es el growth partner del proyecto. **Andy (o quien él designe, como Omar) hace el contacto. Tú nunca contactas a nadie.**
- **Backlog:** este trabajo ejecuta **BL-010** (verificar la lista de prospectos de Bogotá) y alimenta **BL-012** (prospección mayorista: 10 tiendas de alimento natural). También sirve a BL-014 (microzonas) y BL-035 (validar distribuidores publicados).

## 2. Cliente ideal (ICP)

**Incluir:**
- Pet shops y tiendas de alimento para mascotas con tienda física u online en Bogotá.
- Clínicas veterinarias con punto de venta.
- Centros de entrenamiento, guarderías y criaderos con venta a clientes.
- Distribuidores y cadenas regionales (con cautela: el decisor es más difícil de alcanzar).

**Zonas prioritarias** (propuesta, por validar en BL-014): noroccidente (Suba, Usaquén, Calle 134 y alrededores) y sur (Bosa, Kennedy), alrededor de los aliados actuales; luego Chapinero, Teusaquillo y Engativá.

**Excluir, salvo que Andy lo pida:**
- Negocios cerrados o sin presencia verificable.
- Negocios ya presentes en `PROSPECTOS.md` (deduplica, §3).
- Venta a consumidor final (esta carpeta es B2B).

### Criterios de encaje

| Encaje | Regla |
|---|---|
| **Alto** | **Ya vende alimento natural**: Pixie, BARF (Peluditos BARF, Vital Doggy, Rawf, etc.), horneado u otra línea natural/premium verificable. Su cliente ya está educado en natural. |
| **Medio** | Vende alimento premium o tiene clientela de alto gasto, pero no se observa natural. |
| **Bajo** | Solo concentrados masivos, o encaje dudoso. |
| **Existente** | Aliado o distribuidor actual de Canívoros (confirmar si sigue activo). |

El encaje "Alto" de la lista inicial se basa en directorios de distribuidores de marcas; es **por verificar** hasta que se confirme en la fuente actual del negocio.

## 3. Antes de empezar

1. **Lee `PROSPECTOS.md` completo.** Es el único registro de prospectos de esta carpeta.
2. **Deduplica** antes de investigar, en este orden: `place_id` de Google Maps, dominio web, Instagram, teléfono normalizado y nombre + dirección. Una entrada por sede.
3. **La lista inicial (`prospectos_bogota.xlsx/csv`) se hizo con ayuda de IA** y tiene muchos campos "desconocido". Ningún dato de esa lista es E hasta re-verificarlo.
4. **Si no tienes acceso a la web**, no inventes datos: detente y dilo.

## 4. Flujo de trabajo

**Fase 1 — Descubrimiento** (unos 2 minutos por negocio): Google Maps por tipo + zona ("pet shop Suba", "veterinaria Usaquén", "alimento BARF Bogotá"), directorios de distribuidores de las marcas naturales (página de distribuidores de Pixie, Peluditos BARF, Vital Doggy, etc.). Registra nombre, `place_id`, tipo, zona, dirección, web, Instagram, teléfono público y marcas observadas.

**Fase 2 — Verificación / mini auditoría comercial** (unos 15 minutos por negocio, máximo 10 por lote). Aplica §5.

**Fase 3 — Entrega:** actualiza `PROSPECTOS.md` según §8.

## 5. Mini auditoría comercial (verificar un prospecto)

Revisa, en este orden:

1. **Google Maps:** existe, está abierto, dirección, horario, calificación y número de reseñas, fotos del local (¿se ven marcas en estantería?).
2. **Web / tienda online:** qué marcas vende, si hay categoría "natural", "BARF" u "horneado", si vende online y si hace domicilio.
3. **Instagram / Facebook:** actividad reciente, marcas que publica, si promueve alimento natural. Los conteos de redes son V (no E).
4. **WhatsApp público:** solo confirmar que el número publicado tiene formato válido de Colombia (celular `3xx xxx xxxx`, 10 dígitos; fijo `601` + 7 dígitos). **No escribas ni llames.**

**Entregable por prospecto:**
- **3 hallazgos con evidencia** (URL, fecha, fragmento o descripción exacta), por ejemplo: "vende Pixie (foto de estantería en Maps, fecha)", "su web tiene categoría BARF", "no publica alimento horneado".
- **Encaje** (Alto/Medio/Bajo) con la regla de §2.
- **Primer mensaje redactado, sin enviar** (§7).
- **Por validar (V):** lo que solo se puede confirmar en una conversación (pedido mínimo, margen que piden, rotación, plazo de pago).

## 6. Precisión y evidencia

- **Etiquetas:**
  - **(E) Hecho verificado:** observado por ti en una fuente con URL y fecha.
  - **(D) Declaración:** lo que el negocio o una marca dice de sí mismo (p. ej. "somos distribuidores autorizados").
  - **(H) Hipótesis:** tu interpretación (p. ej. "su cliente ya está educado en natural").
  - **(V) Por validar:** dato dudoso, de fuente legacy, de redes o que requiere conversación.
- **Desconocido:** si no encuentras un dato, escribe `desconocido`. Nunca lo estimes.
- **No inventes precios, márgenes, volúmenes ni ventas** de Canívoros ni del prospecto. Los precios de Canívoros los confirma BL-005; no los cites hasta entonces.
- **Afirmaciones de ausencia** ("no vende natural") solo si revisaste web, Maps e Instagram y lo dices explícitamente.
- No encadenes conclusiones sobre datos V.

## 7. Primer mensaje (borrador, nunca se envía sin aprobación de Andy)

- **Canal:** WhatsApp comercial público del negocio o visita en persona.
- **Estructura:** saludo y quién escribe (Canívoros, alimento horneado hecho en Sopó) → una observación específica y verdadera del negocio (de los hallazgos E) → propuesta concreta y pequeña (p. ej. dejar muestras o conocer sus condiciones) → pregunta fácil de responder.
- **Reglas:**
  - Máximo 4–5 líneas, tono cercano y profesional.
  - Sin afirmaciones de salud no respaldadas (ver BL-016) y sin precios no confirmados.
  - Nada de presión ni escasez falsa.
- **Ejemplo (plantilla):**
  > Hola, soy [nombre] de Canívoros, alimento natural horneado para perros y gatos hecho en Sopó. Vi que en [negocio] manejan [marca natural observada], así que sus clientes ya buscan alimento natural. ¿Les interesaría conocer nuestras condiciones para tiendas y probar con una muestra? ¿Con quién podría hablar sobre compras?

## 8. Cómo actualizar `PROSPECTOS.md`

- **Tabla de registro:** una fila por prospecto, con ID (`P` + número; no se reutilizan), nombre, tipo, zona, marcas observadas, encaje, estado y fuente.
- **Ficha completa** (formato §9) para cada prospecto auditado con encaje Alto.
- **Estados que pone el agente:** `por_verificar`, `verificado`, `listo_para_contactar`, `descartado`.
- **Estados que pone Andy:** `contactado`, `respondio`, `muestra`, `pedido`, `reposicion`, `perdido`. **Nunca** cambies estos ni sus notas.
- **Métricas para BL-012** (las registra Andy): contactados, respondieron, pedido inicial, reposición, motivo de no compra. Sin cifras inventadas.
- **Historial de lotes:** agrega arriba `### Lote AAAA-MM-DD · <zona>` con búsquedas, conteos y limitaciones.

## 9. Formato de ficha

```markdown
#### [P-ID] [Nombre] — Encaje Alto
- Tipo / zona / dirección:
- Web · Maps · Instagram:
- Contacto comercial público:
- Marcas observadas:
- Decisor: desconocido
- Estado:

**Hallazgos**
1. (E) [hecho] — URL · fecha
   (H) [interpretación]
2. ...
3. ...

**Declaraciones (D):** ...
**Por validar (V):** pedido mínimo, margen requerido, rotación, plazo de pago...

**Borrador de primer mensaje (no enviado):**
> ...
```

## 10. Límites (no negociables)

- **No contactes.** No envíes mensajes, no llames, no envíes formularios, no crees cuentas. Todo contacto lo aprueba y lo hace Andy (o quien él designe).
- **Solo datos comerciales públicos del negocio.** No guardes datos personales de dueños, empleados o clientes (cédulas, celulares personales, direcciones de vivienda, fotos de personas). En Colombia rige la Ley 1581 de 2012 de protección de datos.
- **No evadas bloqueos** ni hagas scraping que viole términos de servicio. Si una fuente bloquea, marca "No verificado".
- **No subas contraseñas ni tokens** al repositorio.

## 11. Checklist antes de entregar un lote

- [ ] Deduplicado contra `PROSPECTOS.md`.
- [ ] Cada prospecto auditado tiene 3 hallazgos con URL y fecha.
- [ ] Hechos, declaraciones, hipótesis y por validar están etiquetados.
- [ ] Ningún precio, margen o venta inventado; lo que falta dice `desconocido`.
- [ ] Borradores marcados como no enviados.
- [ ] No hay datos personales sensibles.
