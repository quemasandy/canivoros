# Métricas del Piloto de Prospección Outbound B2B

Framework para medir el desempeño del piloto de prospección B2B de Canívoros. Las métricas se alinean con el plan de crecimiento en `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` y no inventan tasas esperadas.

**Fecha:** 2026-11-11  
**Alcance:** Piloto de prospección con los prospectos de este aporte y de `prospectos/`

---

## Objetivo del piloto

**Pregunta a responder:** ¿Qué combinación de segmento, zona y canal de contacto genera prospectos B2B que compran y vuelven a comprar?

El piloto de prospección outbound es una actividad de adquisición que alimenta al embudo comercial. No es un fin en sí mismo: una respuesta sin compra no es éxito; un pedido sin recompra tampoco lo es.

---

## Embudo de prospección B2B

```
┌─────────────────────────────────────┐
│  PROSPECTOS IDENTIFICADOS          │  ← Negocios en el registro
├─────────────────────────────────────┤
│  PROSPECTOS VERIFICADOS (Nivel A/B)│  ← Datos confirmados
├─────────────────────────────────────┤
│  CONTACTADOS                        │  ← Se envió primer mensaje
├─────────────────────────────────────┤
│  RESPONDIERON                       │  ← Cualquier respuesta
├─────────────────────────────────────┤
│  INTERESADOS                        │  ← Respuesta positiva
├─────────────────────────────────────┤
│  REUNIÓN / MUESTRA                  │  ← Conversación o prueba
├─────────────────────────────────────┤
│  PRIMER PEDIDO                      │  ← Compra pagada y entregada
├─────────────────────────────────────┤
│  SEGUNDO PEDIDO                     │  ← Recompra
└─────────────────────────────────────┘
```

---

## Métricas de actividad (proceso)

Estas métricas miden la ejecución del proceso de prospección, no el resultado comercial.

| Métrica | Definición | Cómo medirla |
|---------|------------|--------------|
| **Prospectos identificados** | Total de negocios en el registro | Contar filas en `prospectos-AAAA-MM-DD.md` + `PROSPECTOS-VERIFICADOS.md` |
| **Prospectos verificados** | Nivel A + B con datos confirmados | Contar filas con nivel A o B y estado `verificado` o posterior |
| **Tasa de verificación** | Verificados / Identificados | Solo informa calidad de las fuentes |
| **Contactados** | Prospectos a los que se envió mensaje | Contar estado `contactado` o posterior |
| **Tasa de contacto** | Contactados / Verificados aprobados | Solo informa velocidad de ejecución |
| **Seguimientos enviados** | Mensajes de seguimiento 1 o 2 | Contar estados `seguimiento 1` y `seguimiento 2` |

### Actividad semanal sugerida (para seguimiento)

| Indicador | Qué registrar |
|-----------|---------------|
| Lotes trabajados | Número de lotes de prospección completados |
| Prospectos nuevos agregados | IDs agregados al registro |
| Mensajes enviados | Primeros contactos + seguimientos |
| Tiempo invertido | Horas dedicadas a prospección |

---

## Métricas de resultado (comerciales)

Estas métricas miden el impacto comercial de la prospección.

| Métrica | Definición | Cómo medirla |
|---------|------------|--------------|
| **Tasa de respuesta** | Respondieron / Contactados | Cualquier respuesta (sí, no, no ahora) |
| **Tasa de interés** | Interesados / Contactados | Respuestas positivas |
| **Reuniones/muestras** | Prospectos que aceptaron reunión o muestra | Contar estado `reunión` o `muestra` |
| **Tasa de conversión a reunión** | Reuniones / Interesados | Informa qué tan bien se convierte interés en acción |
| **Primer pedido** | Prospectos que hicieron al menos un pedido pagado | Contar estado `cliente` |
| **Tasa de conversión a cliente** | Clientes / Contactados | Métrica principal de efectividad |
| **Kilos del primer pedido** | Volumen del primer pedido en kg | Registrar por prospecto |
| **Valor del primer pedido** | COP del primer pedido (cuando se conozcan precios) | Registrar por prospecto |

### Métricas de recompra (requieren tiempo)

| Métrica | Definición | Ventana |
|---------|------------|---------|
| **Segundo pedido** | Clientes con al menos 2 pedidos | Depende del producto |
| **Tasa de recompra** | Clientes con 2+ pedidos / Clientes con 1+ pedido | Medir a 30, 60, 90 días |
| **Tiempo entre pedidos** | Días promedio entre pedido 1 y pedido 2 | Por cliente |
| **Volumen de recompra** | Kg del segundo pedido vs. el primero | Por cliente |

**Nota:** La recompra B2B depende de la rotación del negocio, no de un ciclo de consumo personal. Un criadero puede reponer en 2 semanas; una tienda pequeña, en 2 meses.

---

## Métricas de atribución

Para entender qué funciona mejor, segmentar todas las métricas por:

| Dimensión | Valores |
|-----------|---------|
| **Segmento** | Tienda, veterinaria, criadero, guardería, spa, café, otro |
| **Zona** | Localidad de Bogotá o municipio de Sabana |
| **Canal de contacto** | WhatsApp, Instagram DM, correo |
| **Nivel del prospecto** | A, B, C |
| **Fuente del prospecto** | Búsqueda propia, referido, competencia |

### Ejemplo de análisis de atribución

> "De los 15 prospectos Nivel A contactados, 8 eran tiendas y 7 criaderos. Las tiendas respondieron 5/8 (62%) y los criaderos 2/7 (29%). Sin embargo, los criaderos que respondieron hicieron pedidos más grandes (promedio 120 kg vs. 15 kg). Conclusión: criaderos convierten menos pero valen más."

---

## Registro de datos

### Campos a registrar por prospecto

Agregar a la tabla del registro de prospectos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `fecha_contacto` | Fecha | Día del primer mensaje |
| `canal_contacto` | Texto | WhatsApp / Instagram / Correo |
| `fecha_respuesta` | Fecha | Día de la primera respuesta (si hubo) |
| `tipo_respuesta` | Texto | interesado / no interesado / no ahora / sin respuesta |
| `fecha_reunion` | Fecha | Día de la reunión o entrega de muestra |
| `fecha_primer_pedido` | Fecha | Día del primer pedido pagado |
| `kg_primer_pedido` | Número | Kilos del primer pedido |
| `fecha_segundo_pedido` | Fecha | Día del segundo pedido |
| `kg_segundo_pedido` | Número | Kilos del segundo pedido |
| `notas_comerciales` | Texto | Observaciones del proceso |

### Herramienta sugerida

Durante el piloto, mantener el registro en el archivo `.md` y `.csv` existente. Cuando el volumen crezca, migrar a una tabla estructurada (hoja de cálculo o CRM básico) que permita filtrar y agregar.

---

## Cómo medir (sin inventar tasas)

### Lo que NO hacer

- ❌ Inventar "tasa esperada de respuesta: 15%"
- ❌ Proyectar ventas basadas en tasas de industria
- ❌ Declarar éxito porque hubo muchas respuestas sin pedidos
- ❌ Comparar con benchmarks de otros mercados

### Lo que SÍ hacer

- ✅ Registrar cada dato real: fecha, respuesta, pedido
- ✅ Calcular tasas con los datos propios después de N contactos
- ✅ Comparar segmentos entre sí (no contra un benchmark externo)
- ✅ Esperar suficiente tiempo antes de concluir sobre recompra

---

## Umbrales de decisión (a definir con Andrés)

Los umbrales no se inventan; deben acordarse antes de ejecutar y ajustarse con los primeros datos.

| Pregunta | Umbral propuesto | Acción si no se cumple |
|----------|------------------|------------------------|
| ¿Cuántos contactos antes de evaluar un canal? | Mínimo 20 | No concluir antes |
| ¿Cuántos días esperar respuesta antes de seguimiento? | 3-4 días | Ajustar según práctica |
| ¿Después de cuántos seguimientos marcar "sin respuesta"? | 2 | Pausar ese prospecto |
| ¿Cuántos interesados para justificar el esfuerzo de un segmento? | A definir | Reasignar recursos |
| ¿Qué volumen mínimo de primer pedido es rentable? | Depende de costos | Calcular contribución |

---

## Revisión del piloto

### Revisión semanal (durante ejecución)

- Actividad: ¿cuántos prospectos se contactaron?
- Respuestas: ¿cuántos respondieron y con qué resultado?
- Bloqueos: ¿qué impide avanzar? (aprobaciones, capacidad, información)
- Ajustes: ¿hay que cambiar el mensaje, el canal o el segmento?

### Revisión al cierre del piloto

| Pregunta | Cómo responderla |
|----------|------------------|
| ¿Qué segmento convirtió mejor? | Tasa de cliente por segmento |
| ¿Qué canal de contacto funcionó mejor? | Tasa de respuesta y conversión por canal |
| ¿Qué nivel de prospecto (A/B) valió la pena? | Comparar esfuerzo de verificación vs. conversión |
| ¿Cuánto costó conseguir un cliente? | Horas invertidas / Clientes conseguidos (no hay gasto de pauta) |
| ¿Los clientes volvieron a comprar? | Tasa de recompra (si pasó suficiente tiempo) |
| ¿Qué aprendimos para escalar? | Documentar lecciones |

---

## Relación con el backlog existente

Este framework de métricas se relaciona con:

- **BL-021** (registrar origen de ventas): asegurar que los pedidos de prospectos outbound se marquen con su fuente
- **BL-044** (hipótesis antes de experimentar): definir umbrales antes de ejecutar
- **BL-005** (confirmar precios y condiciones): necesario para calcular contribución
- **BL-007** (entrevistar distribuidores): entender si hay conflicto de canal

---

## Limitaciones de este framework

1. **No hay línea base de prospección B2B anterior:** Todos los datos serán nuevos; no hay comparación histórica.
2. **Precios y condiciones desconocidos (BL-005):** No se puede calcular contribución hasta que se definan.
3. **Capacidad de producción desconocida:** No se sabe cuántos clientes nuevos puede absorber la operación.
4. **Tiempo de recompra B2B variable:** Un criadero repone diferente a una tienda pequeña.
5. **Muestra pequeña al inicio:** Las tasas con pocos datos son inestables; no concluir antes de tiempo.
