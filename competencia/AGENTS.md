# Instrucciones para agentes de IA: análisis competitivo de Canívoros / Gatívoros

> Lee este archivo completo antes de investigar. Aplica a cualquier agente que continúe el análisis competitivo en esta carpeta.
> Última actualización: 2026-11-02.

---

## 1. Contexto

- **Canívoros / Gatívoros:** alimento natural horneado para perros y gatos, producido en Sopó; mercado objetivo Bogotá. Ver `../CANIVOROS-REFERENCIA-EMPRESA.md`.
- **Objetivo:** entender **por qué un comprador o una tienda elige otra marca, cuánto le cuesta y qué oportunidad puede atender mejor Canívoros**. Método base: `../metodologias_analisis_competitivo.md`.
- **Backlog:** ejecuta **BL-015** (comparar 8–12 alternativas) y alimenta BL-012 (prospección mayorista), BL-016 (afirmaciones de marca), BL-020 (mensajes) y BL-023 (presentación de entrada).
- **Tú nunca contactas a nadie** ni haces compras de prueba sin aprobación de Andrés.

## 2. Qué competidores incluir

Alternativas que un comprador realmente considera en Bogotá:

| Grupo | Ejemplos (por verificar) |
|---|---|
| Horneado / cocido natural | Pixie, VITA Alimento Vital, Kanuto |
| BARF crudo | Peluditos BARF, Vital Doggy, Rawf, Dogsy, KENKO, 4DOGS, Bocado, Barftender, Santo Barf |
| Natural precocido | Bitute |
| Concentrado premium | Agregar solo los que aparezcan en entrevistas o en estanterías de prospectos |

## 3. Métodos (de `metodologias_analisis_competitivo.md`)

1. **Benchmarking competitivo:** precio, presentaciones, precio por kg, canales, entrega y disponibilidad con criterios comunes.
2. **Matriz de perfil competitivo:** factores de éxito con peso y puntuación 1–5, **solo con evidencia**.
3. **Mapa de posicionamiento:** precio percibido frente a confianza o "naturalidad", basado en entrevistas (BL-006/BL-007), no en intuición.
4. **Análisis de reseñas:** registrar cuántas se revisaron, fecha y tema (aceptación, precio, entrega, empaque, atención). Patrones, no comentarios aislados.
5. **Mapa de cobertura:** dónde venden en Bogotá (distribuidores publicados), cruzado con `../prospectos/PROSPECTOS.md`.

**Reglas de comparación:**
- El precio por kg sirve para comparar, pero **no** es costo diario de alimentación. Solo compara costo diario si hay guías de ración publicadas para el mismo perfil de perro.
- Cada hallazgo debe terminar en una **prueba comercial posible** para Canívoros (p. ej. "competidor X no entrega en Suba → probar entrega programada en Suba y medir conversión y recompra").

## 4. Precisión y evidencia

- **(E) Hecho observado:** lo viste tú (precio en la web, lista de distribuidores) con URL y fecha.
- **(D) Declaración del competidor:** lo que la marca dice de sí misma ("sin conservantes", "+90 puntos de venta").
- **(H) Hipótesis propia:** interpretación de Canívoros (p. ej. "compiten por disponibilidad más que por ingredientes").
- **(V) Por validar:** dato dudoso o de fuente secundaria.
- **Desconocido:** ventas, márgenes, costos y volúmenes internos de los competidores son **desconocidos** salvo fuente pública verificable. No los estimes.
- **Precios:** siempre con fecha, fuente, presentación (g/kg) y si es regular o promocional. Un precio sin fecha es V.

## 5. Plantilla de ficha de competidor

```markdown
### [Marca] — [grupo: horneado / BARF / precocido / premium]
- Empresa / origen o planta:
- Web · Instagram:
- Contacto comercial público:
- Productos y presentaciones:
- Precio observado (fecha · fuente · regular/promo · precio por kg):
- Canales en Bogotá (tiendas, online, domicilio, apps):
- Entrega (zonas, tiempos, costo):
- Mensaje principal:

**Hechos observados (E):**
1. ... — URL · fecha
**Declaraciones del competidor (D):**
- ...
**Hipótesis (H):**
- ...
**Por validar (V) / desconocido:** ventas, margen, rotación en tiendas...
**Prueba comercial que sugiere para Canívoros:** ... (métrica: conversión o recompra)
```

## 6. Cómo actualizar `COMPETENCIA.md`

- Tabla resumen: una fila por marca (ID `C` + número, no se reutiliza).
- Ficha completa (§5) para cada marca analizada.
- Historial: `### Revisión AAAA-MM-DD` con fuentes revisadas y limitaciones.
- Las observaciones también pueden registrarse en el ERP con los campos: competidor · producto · zona · canal · fecha · precio regular · promoción · disponibilidad · fuente · observación · nivel de certeza.

## 7. Límites (no negociables)

- No contactes competidores ni hagas compras de prueba sin aprobación de Andrés.
- Solo información pública. No guardes datos personales de empleados ni de clientes ni de quienes dejan reseñas.
- No evadas bloqueos ni hagas scraping contra términos de servicio.
- No copies contenido protegido (textos o fotos completas); cita y resume.

## 8. Checklist

- [ ] Cada precio tiene fecha, fuente, presentación y precio por kg.
- [ ] Hechos, declaraciones, hipótesis y por validar separados.
- [ ] Datos internos de competidores marcados como desconocidos.
- [ ] Cada hallazgo relevante tiene una prueba comercial sugerida.
