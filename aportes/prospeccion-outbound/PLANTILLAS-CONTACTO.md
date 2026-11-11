# Plantillas de Contacto y Secuencia de Seguimiento

Plantillas de primer mensaje y secuencia de seguimiento para la prospección B2B de Canívoros. Todos los mensajes son **borradores para revisión humana**; ninguno se envía automáticamente.

**Fecha:** 2026-11-11  
**Aplica a:** Prospectos de `PROSPECTOS-VERIFICADOS.md` de este aporte y del archivo existente `prospectos/prospectos-2026-11-03.md`

---

## Reglas generales (de `prospectos/AGENTS.md`)

**Sí se puede decir:**
- Alimento horneado para perros
- Hecho en Sopó, Cundinamarca
- Con proteína animal (pollo, salmón, cerdo)
- Listo para servir
- Nació en una familia que cría perros de competencia

**No se puede decir:**
- Beneficios de salud específicos (digestión, pelaje, etc.)
- "Sin subproductos", "super premium"
- "Registro ICA" (aunque existe, no está verificado para el mensaje)
- Precios ni condiciones comerciales
- Pedido mínimo

**Contacto:** Usar `[número comercial por definir]` hasta que se defina el canal oficial.

---

## Plantillas por canal

### WhatsApp — Primer contacto

WhatsApp es el canal principal según la operación actual de Canívoros. Los mensajes deben ser:
- Cortos (máximo 3-4 oraciones)
- Personalizados con un detalle del negocio
- Con una pregunta abierta que invite a responder

#### Plantilla para tiendas de mascotas

```
Hola, equipo de [NOMBRE TIENDA]. Les escribe [TU NOMBRE], de Canívoros.

Somos una marca de Sopó que hace alimento horneado para perros con pollo, salmón o cerdo, listo para servir. Vi que [DETALLE VERIFICADO: venden alimento natural / tienen petshop / están en X zona].

¿Con quién podría hablar sobre nuevos productos? Mi WhatsApp es [número comercial por definir].
```

#### Plantilla para veterinarias

```
Buenos días. Le escribe [TU NOMBRE], de Canívoros.

Somos una marca de Sopó que hace alimento horneado para perros con proteína animal, listo para servir; nació en una familia que cría perros de competencia. Vi que en [NOMBRE VETERINARIA] tienen [DETALLE: pet center / punto de venta / consulta nutricional].

¿Tendría unos minutos esta semana para conocer el producto? [número comercial por definir]
```

#### Plantilla para criaderos

```
Hola, [NOMBRE CRIADERO]. Soy [TU NOMBRE], de Canívoros.

Venimos del mundo de los perros de competencia y hacemos en Sopó alimento horneado con pollo, salmón o cerdo, listo para servir. Vi que crían [RAZAS] [DETALLE: con certificación ACCC / en X zona].

¿Cuántos perros manejan hoy? Si le interesa, le cuento cómo le vendemos a criaderos. [número comercial por definir]
```

#### Plantilla para servicios caninos (guarderías, adiestramiento, spas)

```
Hola, equipo de [NOMBRE]. Soy [TU NOMBRE], de Canívoros: alimento horneado para perros, hecho en Sopó y listo para servir.

Vi que tienen [SERVICIO: guardería / colegio canino / spa] en [ZONA]. ¿Les interesaría conocerlo para los perros que atienden o para recomendarlo a sus clientes?

[número comercial por definir]
```

#### Plantilla para espacios pet-friendly (cafés, restaurantes)

```
Hola, [NOMBRE]. Les escribe [TU NOMBRE], de Canívoros: alimento horneado para perros, hecho en Sopó con ingredientes de productores locales, listo para servir.

Vi que tienen [DETALLE: zona pet-friendly / platos para perros en el menú]. ¿Les interesaría conocer nuestro producto para recomendarlo a quienes visitan con su mascota?

[número comercial por definir]
```

---

### Instagram — DM de primer contacto

Usar solo si el negocio tiene Instagram activo y no hay WhatsApp publicado. Más informal, pero igual de profesional.

```
Hola [NOMBRE] 👋

Soy [TU NOMBRE] de @canivoros_col. Hacemos alimento horneado para perros en Sopó, con proteína animal real.

Vi su [DETALLE: tienda / criadero / spa] y pensé que podría encajar con lo que ofrecen. ¿Les puedo contar más?
```

---

### Correo electrónico — Primer contacto

Usar para cadenas, negocios con proceso formal de proveedores, o cuando solo hay correo publicado.

**Asunto:** Canívoros — alimento horneado para perros, hecho en Sopó

```
Buenos días, equipo de [NOMBRE],

Me llamo [TU NOMBRE] y trabajo con Canívoros, una marca colombiana de alimento horneado para perros. Producimos en Sopó, Cundinamarca, con proteína animal (pollo, salmón o cerdo), y el producto llega listo para servir.

Vi que [DETALLE DEL NEGOCIO: ya manejan alimento natural / tienen varias sedes / buscan proveedores locales] y pensé que podríamos explorar una conversación.

¿Con quién podría hablar para presentarles el producto?

Quedo atento.

[TU NOMBRE]
Canívoros
[número comercial por definir]
```

---

## Secuencia de seguimiento

El objetivo de la secuencia es obtener una respuesta (sí, no, o no ahora), no acosar al prospecto. Máximo 3 intentos antes de pasar al estado "sin respuesta".

### Día 0 — Primer mensaje

- Enviar el mensaje de primer contacto según la plantilla del canal
- Registrar en el archivo de prospectos: estado `contactado`, fecha

### Día 3-4 — Primer seguimiento

Solo si no hubo respuesta. Mensaje corto que no repita todo:

```
Hola [NOMBRE], ¿vieron mi mensaje anterior sobre Canívoros? Si tienen un momento, me encantaría contarles más. Si no es el momento, me avisan y no les vuelvo a escribir. 🙏
```

### Día 7-10 — Segundo seguimiento

Solo si no hubo respuesta al primero. Agregar valor:

```
Hola [NOMBRE]. Sigo por acá por si les interesa conocer Canívoros. Les comparto un dato: [DATO RELEVANTE, ej: "venimos de una familia que cría dóbermans de competencia" o "producimos cerca, en Sopó"].

Si no es un buen momento, entiendo perfectamente. ¿Les escribo más adelante o prefieren que no los contacte?
```

### Sin respuesta después del segundo seguimiento

- Marcar como `sin respuesta` en el archivo de prospectos
- No enviar más mensajes por al menos 60 días
- Puede reactivarse si hay un cambio (nuevo lanzamiento, evento, recomendación)

---

## Manejo de respuestas

### Si responden "Sí, cuéntenme más"

1. Agradecer y preguntar por el mejor canal para una llamada o reunión
2. Preparar información básica: qué es Canívoros, formatos disponibles, origen
3. **No enviar precios ni condiciones** hasta que estén definidos (BL-005)
4. Registrar como `interesado`; pasar a Andrés para aprobación de siguiente paso

### Si responden "No nos interesa"

1. Agradecer el tiempo
2. Preguntar brevemente si hay una razón (ya tienen proveedor, no manejan natural, etc.)
3. Registrar como `descartado: no interesado` con el motivo
4. No volver a contactar salvo que algo cambie

### Si responden "Ahora no, más adelante"

1. Agradecer y preguntar cuándo sería mejor
2. Registrar como `pospuesto` con la fecha tentativa
3. Programar recordatorio para esa fecha

### Si preguntan precio o condiciones

```
Gracias por el interés. Todavía estamos definiendo las condiciones para nuevos aliados. ¿Le parece si les aviso cuando las tengamos listas? Mientras tanto, ¿qué sería importante para ustedes? (volumen, plazo de pago, presentaciones...)
```

Registrar las necesidades del prospecto para informar BL-005.

---

## Registro del estado

Actualizar el estado en el archivo de prospectos después de cada interacción:

| Estado | Significado |
|--------|-------------|
| `por verificar` | Datos no confirmados |
| `verificado` | Datos confirmados; listo para borrador |
| `borrador listo` | Mensaje preparado; pendiente de aprobación |
| `aprobado` | Andrés aprobó el contacto |
| `contactado` | Se envió el primer mensaje |
| `seguimiento 1` | Se envió primer seguimiento |
| `seguimiento 2` | Se envió segundo seguimiento |
| `sin respuesta` | No hubo respuesta después de 2 seguimientos |
| `interesado` | Respondió con interés; en conversación |
| `pospuesto` | Pidió que lo contacten después (fecha) |
| `descartado: [motivo]` | No procede |
| `cliente` | Hizo al menos un pedido |

---

## Ejemplo de flujo completo

**Prospecto:** PO-001 Kumpet (Nivel A)

1. **Verificación:** Sitio web activo, 3 sedes, vende alimento premium, WhatsApp publicado → `verificado`
2. **Borrador:** Se prepara mensaje personalizado → `borrador listo`
3. **Aprobación:** Andrés revisa y aprueba → `aprobado`
4. **Contacto:** Se envía mensaje WhatsApp día 15 nov → `contactado`
5. **Sin respuesta día 19:** Se envía seguimiento 1 → `seguimiento 1`
6. **Responde día 20:** "Sí, cuéntenme más" → `interesado`
7. **Siguiente paso:** Coordinar llamada; pasar a Andrés

---

## Limitaciones

- Los mensajes son **borradores**; cada contacto debe ser aprobado por Andrés.
- No se pueden prometer precios, pedido mínimo ni condiciones hasta que se definan (BL-005).
- La capacidad de producción es desconocida; no comprometer volúmenes grandes.
- Los tiempos de la secuencia son sugeridos; ajustar según la práctica.
