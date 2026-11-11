# Backlog de Marketing — Formato tabular para importación

**Versión 1 · 11 nov 2026 · Complemento de `plan-operativo-marketing.md`**

Este archivo contiene las tareas de marketing del backlog en formato tabular, listo para importar a Taiga, Plane, Jira o una hoja de cálculo.

---

## Instrucciones de importación

1. Copiar la tabla CSV de abajo
2. Pegar en una hoja de Google Sheets o Excel
3. Usar la función «Datos > Dividir texto en columnas» con separador «|»
4. Importar al tablero elegido (BL-003)

---

## Campos

| Campo | Descripción |
|---|---|
| Clave | Identificador único (BL-NNN) |
| Workstream | WS1-Investigación, WS2-Posicionamiento, WS3-Landing, WS4-Campañas, WS5-Analytics, Base |
| Título | Nombre corto de la tarea |
| Tipo | Tarea, Experimento, Requisito, Historia, Mejora, Error, Acción, Idea |
| Prioridad | Highest, High, Medium, Low |
| Impacto | Alto, Medio, Bajo |
| Depende de | Claves de tareas prerequisito (separadas por coma) |
| Semana propuesta | Semana 1–7 o «Sin semana» |
| Responsable propuesto | Andrés, Sebastián, Omar/Canívoros, o combinación |
| Esfuerzo | S (1–2h), M (3–6h), L (>6h) |
| Gate | G1, G2, G3, G4, G5, o vacío |
| Estado | Backlog (inicial) |

---

## Tabla CSV (separador: pipe)

```
Clave|Workstream|Título|Tipo|Prioridad|Impacto|Depende de|Semana|Responsable|Esfuerzo|Gate|Estado
BL-005|Base|Confirmar precios, unidades y catálogo definitivo|Tarea|High|Alto||1|Sebastián|S|G1|Backlog
BL-004|WS5-Analytics|Calcular línea base con ventas_canivoros_2026.xlsx|Tarea|Highest|Alto|BL-005|1|Andrés|M||Backlog
BL-047|Base|Plantilla única para registrar ventas|Mejora|High|Alto|BL-005|2|Sebastián|S||Backlog
BL-058|Base|Permiso de datos y comunicaciones de clientes|Requisito|High|Medio||2|Andrés|S|G2|Backlog
BL-044|WS4-Campañas|Registrar hipótesis y criterios de decisión antes de cada experimento|Tarea|Highest|Medio||2|Andrés|S||Backlog
BL-059|WS1-Investigación|Auditoría de consultas de WhatsApp (2 semanas)|Tarea|Highest|Alto|BL-058|2|Andrés + Omar|S||Backlog
BL-006|WS1-Investigación|Guion de entrevistas: voz del cliente|Historia|High|Alto||2|Andrés|S||Backlog
BL-007|WS1-Investigación|Entrevistar a Omar y a 2–3 distribuidores actuales|Tarea|High|Alto|BL-006|2|Sebastián|M||Backlog
BL-010|WS1-Investigación|Verificar la lista de 134 prospectos de Bogotá|Tarea|High|Alto||2|Andrés|M||Backlog
BL-035|WS1-Investigación|Validar los distribuidores publicados en el sitio|Tarea|High|Alto||2|Omar|S||Backlog
BL-036|WS1-Investigación|Medir la capacidad de producción disponible|Tarea|Highest|Alto|BL-009|2|Sebastián|S||Backlog
BL-061|WS5-Analytics|Bitácora del caso Canívoros|Tarea|High|Medio|BL-002, BL-004|2|Andrés|S||Backlog
BL-060|WS4-Campañas|Recuperar clientes que dejaron de comprar|Experimento|High|Alto|BL-004, BL-005, BL-044, BL-058|2|Andrés + Omar|S|G4|Backlog
BL-013|WS5-Analytics|Tablero semanal de indicadores|Tarea|Medium|Alto|BL-004|3|Andrés|M||Backlog
BL-014|WS1-Investigación|Matriz de microzonas para el piloto en Bogotá|Tarea|Medium|Medio|BL-007, BL-010|3|Andrés|S||Backlog
BL-015|WS1-Investigación|Comparar 8–12 alternativas de la competencia|Tarea|Medium|Medio||3|Andrés|S||Backlog
BL-043|WS4-Campañas|Programa para criadores y clientes de alto volumen|Experimento|Medium|Alto|BL-004, BL-044|3|Omar + Andrés|M|G4|Backlog
BL-016|WS2-Posicionamiento|Revisar afirmaciones de marca y el mensaje 'sin subproductos'|Tarea|High|Alto||4|Sebastián|S|G3|Backlog
BL-012|WS4-Campañas|Prospección mayorista: 10 tiendas de alimento natural|Experimento|High|Alto|BL-005, BL-010, BL-035, BL-044|4|Hermano Seb + Omar|M|G4|Backlog
BL-019|WS3-Landing|Quick win: marca personal de Omar + captura de leads|Experimento|Medium|Alto|BL-011, BL-016, BL-044, BL-051, BL-058, BL-059|4|Sebastián + Omar|M|G3|Backlog
BL-020|WS2-Posicionamiento|Comparar dos mensajes: horneado vs facilidad de uso|Experimento|Medium|Medio|BL-016, BL-019, BL-044|4|Andrés|S|G3|Backlog
BL-022|WS4-Campañas|Recordatorio de reposición a clientes|Experimento|Medium|Medio|BL-004, BL-044, BL-058|4|Sebastián|M|G2|Backlog
BL-023|WS4-Campañas|Presentación de entrada|Experimento|Low|Medio|BL-005, BL-044|4|Omar|M|G4|Backlog
BL-029|WS3-Landing|Nombre provisorio, dominio y subdominio|Tarea|Medium|Bajo||5|Sebastián|S||Backlog
BL-042|WS3-Landing|Revisar el WordPress y decidir si sirve como tienda|Tarea|Low|Medio|BL-005|6|Sebastián|S||Backlog
BL-021|WS5-Analytics|Medir ventas con su origen para poder cobrar porcentaje|Tarea|High|Alto|BL-004, BL-011, BL-047, BL-049|6|Sebastián|M||Backlog
BL-024|WS1-Investigación|Aplicar QFD a Canívoros|Tarea|Medium|Medio|BL-007|6|Sebastián|M||Backlog
BL-028|WS5-Analytics|Decidir cómo crecer en Bogotá|Tarea|Medium|Alto|BL-013, BL-012|7|Andrés + Sebastián|S|G5|Backlog
BL-026|WS4-Campañas|Gatívoros: introducción alimentaria en veterinarias|Experimento|Low|Medio|BL-025|7|Omar + Sebastián|M|G4|Backlog
```

---

## Diagrama de dependencias (texto)

```
Semana 1:
BL-005 (Precios) ─┬─► BL-004 (Línea base)
                  ├─► BL-047 (Plantilla ventas)
                  ├─► BL-042 (WordPress)
                  └─► BL-023 (Presentación entrada)

Semana 2:
BL-058 (Permisos) ──► BL-059 (Auditoría WhatsApp)
                  └─► BL-022 (Recordatorios)
                  └─► BL-060 (Recuperar clientes)

BL-006 (Guion) ────► BL-007 (Entrevistas)
                  └─► BL-014 (Matriz zonas)
                  └─► BL-024 (QFD)

BL-010 (Prospectos) ─► BL-014 (Matriz zonas)
                    └─► BL-012 (Prospección B2B)

BL-004 (Línea base) ─┬─► BL-013 (Tablero)
                     ├─► BL-021 (Origen ventas)
                     ├─► BL-043 (Criadores)
                     ├─► BL-060 (Recuperar)
                     └─► BL-061 (Bitácora)

Semana 4:
BL-016 (Claims) ────► BL-019 (Omar leads)
                  └─► BL-020 (Test mensajes)

BL-044 (Hipótesis) ─► Todos los experimentos

Semana 7:
BL-013 (Tablero) + BL-012 (Prospección) ──► BL-028 (Decisión Bogotá)
```

---

## Notas para el tablero

1. **Columna Gate:** añadir como etiqueta o campo personalizado para filtrar tareas que requieren aprobación.
2. **Bloqueos:** si una dependencia no está cerrada, la tarea queda en «Bloqueado».
3. **Revisión semanal:** filtrar por semana para ver el trabajo del sprint.
4. **Experimentos:** todos los de tipo «Experimento» requieren ficha BL-044 antes de empezar.

---

**Fuente:** `develop` rama `backlog/` (11 nov 2026). Solo tareas relevantes para marketing.
