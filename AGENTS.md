# Instrucciones para agentes

Este repositorio es el trabajo de crecimiento comercial de **Canívoros / Gatívoros**. Aplica a cualquier agente de IA (Claude, ChatGPT, Gemini, Cursor u otro). Antes de trabajar en una carpeta que tenga su propio `AGENTS.md`, léelo completo: manda sobre este archivo en lo específico.

## 1. Contexto

- **Canívoros** (perros) y **Gatívoros** (gatos): alimento natural **horneado** con proteína animal (pollo, salmón, cerdo), producido en **Sopó (Cundinamarca)**. Mercado objetivo: **Bogotá**.
- **Equipo:**
  - **Andrés Muñoz**: growth partner, unas 4 h por semana. Decide prioridades y aprueba todo contacto externo.
  - **Sebastián**: parte técnica (Odoo, datos, infraestructura).
  - **Omar / equipo Canívoros**: operación, producción y venta.
- **Objetivo:** aumentar ventas rentables y recurrentes en Bogotá con un proceso medible (medir → diagnosticar → priorizar → experimentar → escalar).

## 2. Mapa del repositorio

| Ruta | Qué es | Instrucciones |
|---|---|---|
| `CANIVOROS-REFERENCIA-EMPRESA.md` | Ficha de la empresa (lo que declara la marca) | — |
| `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md` | Plan comercial y de sistematización para Bogotá | — |
| `erp.md` | Levantamiento operativo para el ERP (compras, cuarto frío, producción, máquinas) | — |
| `metodologias_analisis_competitivo.md` | Métodos de análisis competitivo | — |
| `pasos_sysmkt.md` | Notas de descubrimiento de producto y oferta Growth Partner | — |
| `Guia*.md`, `QFD.pdf` | Guías de investigación y desarrollo de productos; material QFD (si están en la rama) | — |
| `backlog/` | Backlog de tareas BL-* ordenado por impacto, con consolidados | `backlog/README.md` |
| `prospectos/` | Prospección B2B de tiendas, veterinarias y distribuidores de Bogotá | `prospectos/AGENTS.md` |
| `competencia/` | Análisis competitivo (Pixie, BARF, horneados) | `competencia/AGENTS.md` |

Este repo **no** es la tienda online ni el ERP: el código de Odoo vive en otros repositorios relacionados.

## 3. Reglas comunes

**Evidencia**
- Separa **hechos** (verificados, con fuente y fecha), **declaraciones** (lo que dice la marca, un cliente o un competidor) e **hipótesis** (interpretaciones propias).
- Lo que no se sabe se escribe **`desconocido`**. Desconocido no es cero.
- **Nunca inventes precios, ventas, márgenes, costos ni volúmenes.** Un ejemplo numérico solo se usa si se marca como ilustrativo.

**Contacto y publicación**
- **Nunca contactes** clientes, prospectos, distribuidores ni competidores (mensajes, llamadas, formularios, compras de prueba), ni publiques nada, sin aprobación explícita de Andrés. Los mensajes se dejan como borrador.

**Datos y seguridad**
- **Nunca guardes contraseñas, tokens ni claves** en el repo ni en el chat.
- **No guardes datos personales** de clientes, empleados o personas (celulares personales, cédulas, direcciones de vivienda, datos de mascotas asociados a una persona). Solo datos comerciales públicos de negocios. Rige la Ley 1581 de 2012 (Colombia).

**Trabajo**
- Convierte cada hallazgo en una **prueba comercial medible**: conversión, recompra o ingreso en COP, con gasto máximo y regla de seguir, ajustar o parar.
- Prioriza por impacto **respetando el backlog** y sus dependencias. La seguridad (BL-001) va primero.
- Considera que Andrés tiene unas 4 h por semana: propuestas pequeñas y concretas.

## 4. Git

- Trabaja en una rama (`docs/...`, `backlog`, `feat/...`) y propone cambios por **PR hacia `develop`**.
- Un PR por propósito; revisa que el diff solo incluya los archivos esperados.
- No hagas push forzado sobre ramas compartidas ni reescribas historia publicada.
