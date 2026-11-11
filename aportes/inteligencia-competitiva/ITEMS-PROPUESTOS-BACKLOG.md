# Ítems propuestos para el backlog

**Origen:** Inteligencia competitiva, 9 nov 2026  
**Estado:** Propuestas; no modifican `backlog/` existente  
**Responsable de integración:** Andrés

---

Estos ítems son propuestas derivadas del análisis competitivo. No se agregan al backlog existente; quedan aquí para revisión.

---

## IC-001 · Documentar vida útil y condiciones de conservación

**Tipo:** Requisito  
**Prioridad propuesta:** Alta (precondición para argumentar ventaja sobre congelados)

**Descripción:**  
Crear ficha técnica con: humedad del producto, vida útil cerrado, vida útil después de abrir, temperatura de almacenamiento recomendada, y si requiere o no refrigeración.

**Criterios de aceptación:**
- Ficha técnica escrita con los 5 datos.
- Respaldada por ensayos o por el fabricante.
- Publicable en web si se decide.

**Dependencias:** Ninguna.  
**Conecta con:** BL-041 (guía de raciones), diferenciación frente a Pixie/VITA.

**Hechos:**  
La web de Canívoros dice "conservar en lugar fresco y seco" pero no especifica vida útil ni temperatura.

**Hipótesis:**  
Si el producto es estable a temperatura ambiente, es una ventaja logística frente a competidores que requieren congelador.

---

## IC-002 · Publicar número de registro ICA

**Tipo:** Requisito  
**Prioridad propuesta:** Alta (credibilidad)

**Descripción:**  
Hacer visible el número de registro ICA en la web, redes y empaque. Competidores como BARF Bros (01083002023) y Truit (01515002025) lo publican.

**Criterios de aceptación:**
- Número ICA visible en canivoros.com.
- Incluido en empaque o etiqueta.

**Dependencias:** Ninguna.  
**Conecta con:** BL-016 (afirmaciones de marca).

**Hechos:**  
La web declara "registro ICA" pero no muestra el número.

**Hipótesis:**  
Publicar el número aumenta la credibilidad frente a compradores informados y tenderos.

---

## IC-003 · Unificar canales de WhatsApp

**Tipo:** Tarea  
**Prioridad propuesta:** Media (experiencia de cliente y medición)

**Descripción:**  
Consolidar los tres números de WhatsApp publicados en la web en uno solo. Usar el mismo número en web, redes, empaque y Google Maps.

**Criterios de aceptación:**
- Un solo número publicado en todos los canales.
- Otros números redirigen o se eliminan.

**Dependencias:** Ninguna.  
**Conecta con:** BL-021 (medición de ventas con origen), BL-059 (auditoría de consultas de WhatsApp).

**Hechos:**  
La verificación del 9 nov encontró tres WhatsApp distintos publicados en canivoros.com.

**Hipótesis:**  
Unificar facilita la medición del origen de consultas y reduce confusión del cliente.

---

## IC-004 · Calcular costo diario y comparar con 3 competidores

**Tipo:** Análisis  
**Prioridad propuesta:** Alta (después de BL-005 y BL-041)

**Descripción:**  
Una vez confirmados precio, peso y ración de Canívoros, calcular costo diario para un perro de 15 kg y comparar con:
- VITA Alimento Vital
- Pixie
- Un concentrado premium (ej: Taste of the Wild)

**Criterios de aceptación:**
- Tabla con costo diario en COP para perro de 15 kg.
- Fuentes y cálculos visibles.
- Diferencia porcentual vs. cada competidor.

**Dependencias:** BL-005 (precios), BL-041 (raciones).  
**Conecta con:** BL-015 (comparar alternativas), BL-023 (presentación de entrada).

**Hechos:**  
Sin precio ni ración de Canívoros, no se puede ubicar en el mapa de precios.

**Hipótesis:**  
El costo diario es más relevante para el cliente que el precio por kg.

---

## IC-005 · Probar mensaje "sin refrigerar" en 5 tiendas

**Tipo:** Experimento  
**Prioridad propuesta:** Media (después de IC-001)

**Descripción:**  
Si se confirma que Canívoros no requiere congelador, probar el mensaje en 5 tiendas de Bogotá que NO tengan congelador asignado. Medir interés y objeciones.

**Criterios de aceptación:**
- 5 tiendas contactadas con el mensaje.
- ≥2 muestran interés en probar.
- Registro de objeciones.

**Dependencias:** IC-001 (vida útil confirmada).  
**Conecta con:** BL-012 (prospección mayorista), BL-020 (mensajes).

**Hechos:**  
Pixie y VITA requieren congelador. Muchas tiendas pequeñas no lo tienen.

**Hipótesis:**  
"Sin refrigerar" abre tiendas que hoy no pueden vender comida natural.

---

## IC-006 · Monitorear precios de VITA y Pixie mensualmente

**Tipo:** Tarea recurrente  
**Prioridad propuesta:** Baja (mantenimiento)

**Descripción:**  
Cada mes, verificar precios publicados de VITA y Pixie. Actualizar `competencia/competencia-AAAA-MM-DD.csv` con la fecha del día.

**Criterios de aceptación:**
- CSV actualizado mensualmente.
- Cambios de precio documentados.

**Dependencias:** Ninguna.  
**Conecta con:** competencia/AGENTS.md (guía de análisis).

**Hechos:**  
Los precios de referencia son del 9 nov 2026. Pueden cambiar.

**Hipótesis:**  
Monitorear permite detectar promociones y ajustar mensaje de precio.

---

## IC-007 · Investigar mercado de gatos (Gatívoros)

**Tipo:** Investigación  
**Prioridad propuesta:** Baja (brecha abierta)

**Descripción:**  
La investigación actual se centró en perros. Hacer un análisis similar para gatos: competidores de comida natural para gatos en Bogotá, precios, canales.

**Criterios de aceptación:**
- Informe equivalente para gatos.
- Marcas: Pixie gatos, VITA gatos, comida natural para gatos.
- Precios publicados con fuente.

**Dependencias:** Ninguna.  
**Conecta con:** BL-026 (Gatívoros en veterinarias).

**Hechos:**  
Las referencias indicadas (instagram.com/friskiesbr, instagram.com/canivoros_col) no se pudieron verificar sin navegación logueada.

**Hipótesis:**  
El mercado de gatos puede tener menos competencia natural que el de perros.

---

*Fin de propuestas.*
