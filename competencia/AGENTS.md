# Instrucciones para agentes · análisis competitivo de Canívoros

> Lee este archivo completo antes de investigar. Aplica a cualquier agente que continúe el análisis competitivo en esta carpeta.
> Las reglas comunes del proyecto (evidencia, datos personales, mensajes de marca, Git) están en `../AGENTS.md` y también aplican aquí.
> Última actualización: 2026-11-02.

---

## 1. Contexto y objetivo

- **Canívoros** hace alimento natural horneado para perros en Sopó (Cundinamarca); **Gatívoros** es su línea para gatos. Según la operación (`../erp.md` §5), vende **chorizos** (pollo y salmón, la línea que considera «premium») y **hamburguesas** (cerdo, pollo, ternera) en **500 g o «libra»**, y hamburguesas de 1,5 kg **por kilo a criadores** (mínimo relatado de 40 kg). El catálogo y los precios no están confirmados (BL-005).
- La responsable de la operación quiere saber qué productos son comparables, cuánto pagan los compradores y qué presentaciones venden mejor (`../erp.md` §7). Lleva unos tres años intentando hacer crecer la línea premium y percibe que el público dispuesto a pagarla es pequeño.
- **Objetivo de esta carpeta:** entender **por qué un comprador o una tienda elige otra marca, cuánto le cuesta y qué oportunidad puede atender mejor Canívoros**. Método base: `../metodologias_analisis_competitivo.md`.
- **Backlog:**

| Tarea | Qué aporta esta carpeta |
|---|---|
| **BL-015** · Comparar 8–12 alternativas | Tabla con precio por kg, presentación, entrega y mensaje, con fecha y fuente |
| BL-012 · Prospección mayorista | Qué marcas tienen las tiendas y qué condiciones públicas ofrecen los competidores a las tiendas |
| BL-016 · Afirmaciones de marca | Qué afirman los competidores y con qué soporte |
| BL-020 · Dos mensajes (horneado vs facilidad de uso) | Mensajes principales de la categoría |
| BL-023 · Presentación de entrada | Presentaciones y gramajes de la competencia |
| BL-014 · Microzonas | Criterio «oportunidad frente a competidores» (10 % del puntaje) |
| BL-024 · QFD | Paso 8: comparar cómo satisfacen las necesidades los competidores |

- **Tú nunca contactas a nadie**, ni haces compras de prueba, sin aprobación de Andrés.

## 2. Qué competidores incluir

Incluye las alternativas que un comprador o una tienda de Bogotá realmente considera:

| Grupo | Por qué importa | Ejemplos (por verificar) |
|---|---|---|
| **Horneado o cocido natural** | Competencia directa en proceso y en la tienda | Pixie, Kanuto, VITA Alimento Vital |
| **BARF crudo** | Mismo comprador «natural»; muchas tiendas aliadas y domicilio directo | Peluditos BARF, Vital Doggy, Rawf, Dogsy, KENKO, 4DOGS, Bocado, Barftender, Santo Barf |
| **Natural precocido** | Alternativa intermedia | Bitute |
| **Concentrado premium** | Lo que compra el cliente de alto gasto que no da natural | Solo marcas vistas en entrevistas o en tiendas prospecto: Taste of the Wild, Acana, Orijen, Nupec, Hill's, Pro Plan, Royal Canin |
| **Gatos** (más adelante, BL-026) | La línea Gatívoros compite con otro grupo de marcas | Aún no se registra |

## 3. Qué registrar de cada competidor

| Campo | Detalle |
|---|---|
| Producto y formato | Croqueta, chorizo, hamburguesa, porciones BARF, etc. |
| Conservación | Congelado, refrigerado o seco; vida útil si la publican |
| Presentaciones | Gramos o kilos de cada empaque |
| Precio | Regular o promoción, con fecha, fuente y si incluye envío |
| **Precio por kg** | `precio ÷ (gramos ÷ 1.000)`, redondeado al peso |
| Ración publicada | Gramos por día según el peso del perro, si la publican (sirve para el costo diario) |
| Canales en Bogotá | Tiendas, venta directa, online, domicilio, Rappi |
| Entrega | Zonas, días, costo, pedido mínimo |
| Oferta al canal | Lo que publiquen para tiendas o distribuidores: «sé distribuidor», pedido mínimo, material, congelador. Solo información pública |
| Mensaje principal | La promesa de su página de inicio o de su perfil en redes |
| Afirmaciones | Salud, ingredientes, registros (para BL-016), con la cita exacta |
| Reseñas | Cuántas revisaste, de qué fecha y sobre qué temas |

Estos campos coinciden con los del ERP: competidor · producto · zona · canal · fecha · precio regular · promoción · disponibilidad · fuente · observación · nivel de certeza.

## 4. Métodos (de `metodologias_analisis_competitivo.md`)

1. **Benchmarking competitivo:** la tabla de §3 con criterios comunes. Es lo primero.
2. **Matriz de perfil competitivo:** factores de éxito con peso y puntuación de 1 a 5, **solo con evidencia**. Factores sugeridos: disponibilidad en tiendas, entrega, confianza, relación precio–valor, presentaciones, atención y aceptación del perro. Los pesos salen de las entrevistas (BL-006, BL-007), no de la intuición; mientras no existan, quedan `por definir`.
3. **Mapa de posicionamiento:** precio percibido frente a confianza o «naturalidad», basado en entrevistas, no en opinión propia.
4. **Análisis de reseñas:** patrones, no comentarios aislados. Registra cuántas reseñas revisaste, su fecha y el tema (aceptación, precio, entrega, empaque, atención).
5. **Mapa de cobertura:** dónde venden en Bogotá (distribuidores publicados), cruzado con `../prospectos/PROSPECTOS.md` y con las microzonas de BL-014.
6. **Compra de prueba:** solo con aprobación de Andrés y gasto máximo definido (BL-044). Si se aprueba, documenta atención, tiempos, empaque y seguimiento.

## 5. Reglas de comparación

- El precio por kg sirve para comparar, pero **no es el costo diario de alimentación**. Compara costo diario solo si hay raciones publicadas para el mismo perfil de perro (por ejemplo, adulto de 10 kg con actividad normal). La ración de Canívoros todavía es `desconocido` (BL-041).
- Separa siempre precio regular y promoción, y precio con y sin envío.
- **No compares precios de Canívoros** hasta que BL-005 los confirme. Los de `../erp.md` §5 son relatados y tienen inconsistencias.
- Compara dentro de cada grupo de §2 antes de comparar entre grupos: un BARF crudo y una croqueta premium no se usan igual.
- **Cada hallazgo termina en una prueba comercial posible** para Canívoros, con métrica y regla de decisión. Ejemplo: «X no entrega en Suba → probar entrega programada en Suba durante 4 semanas y medir conversión y recompra».

## 6. Precisión y evidencia

- **(E) Hecho observado:** lo viste tú (precio en la web, lista de distribuidores, foto de empaque), con URL y fecha.
- **(D) Declaración del competidor:** lo que la marca dice de sí misma («sin conservantes», «+90 puntos de venta»).
- **(H) Hipótesis propia:** interpretación de Canívoros («compiten por disponibilidad más que por ingredientes»).
- **(V) Por validar:** dato dudoso, sin fecha o de fuente secundaria (índices de búsqueda como `exa.ai`, directorios de terceros).
- Ventas, márgenes, costos y volúmenes internos de los competidores son **`desconocido`** salvo fuente pública verificable. No los estimes.
- **Un precio sin fecha es (V).** El precio por kg calculado hereda la etiqueta del precio de origen.

## 7. Plantilla de ficha de competidor

```markdown
### [C-ID] [Marca] — [grupo: horneado / BARF / precocido / premium]
- Empresa / origen o planta:
- Web · Instagram:
- Contacto comercial público:
- Productos, formato y conservación:
- Presentaciones:
- Precio observado (fecha · fuente · regular/promo · con/sin envío):
- Precio por kg (cálculo):
- Ración publicada:
- Canales en Bogotá (tiendas, online, domicilio, apps):
- Entrega (zonas, días, costo, mínimo):
- Oferta pública al canal:
- Mensaje principal:

**Hechos observados (E):**
1. ... — URL · fecha
**Declaraciones del competidor (D):**
- ... (cita exacta)
**Hipótesis (H):**
- ...
**Por validar (V) / desconocido:** ventas, margen, rotación en tiendas...
**Prueba comercial que sugiere para Canívoros:** ... (métrica: conversión, recompra o COP; regla de seguir, ajustar o parar)
```

## 8. Cómo actualizar `COMPETENCIA.md`

- **Registro:** una fila por marca, con ID `C` + dos dígitos (el siguiente libre; no se reutilizan). Si una fila agrupa varias marcas (como C13), sepárala al verificar: la fila original conserva la primera marca y las demás reciben IDs nuevos.
- **Ficha completa** (§7) para cada marca analizada.
- **Cobertura en prospectos:** recalcúlala cuando cambie `../prospectos/PROSPECTOS.md`.
- **Historial:** agrega arriba `### Revisión AAAA-MM-DD` con fuentes revisadas, marcas actualizadas y limitaciones.

## 9. Límites (no negociables)

- No contactes competidores ni hagas compras de prueba sin aprobación de Andrés.
- Solo información pública. No guardes datos personales de empleados, clientes ni autores de reseñas.
- No evadas bloqueos ni hagas scraping contra los términos de servicio.
- No copies contenido protegido (textos largos o fotos): cita la frase corta necesaria y resume.

## 10. Checklist

- [ ] Cada precio tiene fecha, fuente, presentación, regular/promo y precio por kg.
- [ ] Hechos, declaraciones, hipótesis y por validar están separados.
- [ ] Los datos internos de los competidores están marcados como `desconocido`.
- [ ] Ningún precio de Canívoros comparado antes de BL-005.
- [ ] Cada hallazgo relevante tiene una prueba comercial sugerida.
- [ ] *Resumen*, *Cobertura* e *Historial* de `COMPETENCIA.md` actualizados.
