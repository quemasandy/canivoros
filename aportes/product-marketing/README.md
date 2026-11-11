# Aporte de product marketing: claims del sitio y guiones de WhatsApp

Borrador 1 · 10 nov 2026 · **Nada está aprobado, publicado ni enviado.** No usar con clientes ni cambiar el sitio sin el visto bueno de Andrés y de la dueña.

## Qué es

Dos piezas que llevan `branding/` a trabajo concreto. No redefinen posicionamiento, pilares, arquitectura, voz ni taglines: eso es del bot Canívoros.

| Archivo | Qué tiene | Tarea que apoya |
|---|---|---|
| [auditoria-claims-sitio.md](auditoria-claims-sitio.md) | Cada claim de riesgo del sitio vivo, citado literal, con su riesgo, su fuente y un reemplazo hecho solo con datos respaldados | BL-016 |
| [whatsapp-reactivacion-y-reposicion.md](whatsapp-reactivacion-y-reposicion.md) | Guiones para que Omar escriba a mano: reactivación, criadores, reposición, permiso y respuestas cortas, más el registro de la prueba de 14 días | BL-060, E02, BL-022, BL-043, BL-058 |

## Para quién

- **Omar y Sary** operan: Omar envía los guiones; la responsable de la operación confirma precios, conservación, receta e ICA.
- **Andrés** mide: arma la lista desde BL-004, revisa permisos y llena el resumen del día 14.
- **Sebastián** aplica los cambios del sitio cuando estén aprobados (BL-016, propuesta).

## Cómo usarlo

1. Empieza por la auditoría. Los claims de prioridad alta se resuelven casi todos borrando. Los que necesitan un dato (conservación, ICA, receta de Gatívoros) van a la dueña como lista de preguntas.
2. Los guiones no se usan hasta tener: número comercial único, precios de BL-005, texto de permiso de BL-058 y la lista de elegibles de BL-004.
3. Cada `[falta: …]` es un dato que no existe en las fuentes. No se rellena con estimaciones: se pregunta.
4. Si una frase choca con `branding/`, manda `branding/`. Los choques que encontré están abajo, para el bot Canívoros.

## Cómo se marcan los datos

Misma leyenda que `branding/README.md`:

- **Hecho:** está en una fuente (repo, sitio, Odoo, Excel).
- **Declaración:** lo dice la marca o la dueña; no está comprobado.
- **Hipótesis / Propuesta:** idea para validar.
- **[falta: …]:** dato que no tenemos.

## Fuentes y fecha de consulta

Todas leídas el **10 nov 2026 entre 22:14 y 22:30 (hora de Quito, UTC-5)**.

| Fuente | Versión | Qué se usó |
|---|---|---|
| Repo `quemasandy/canivoros`, rama `develop` | commit `9838919` (3 nov 2026, 23:15 hora de Quito) | `README.md`, `CANIVOROS-REFERENCIA-EMPRESA.md`, `CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`, `erp.md`, `backlog/` BL-005, BL-016, BL-020, BL-022, BL-035, BL-041, BL-043, BL-058, BL-059, BL-060; `embudos/EMBUDOS.md` y `embudos/E02-…/embudo.md` y `numeros.md` |
| Rama `backlog` | commit `7d431af` | Está 43 commits detrás de `develop` y no tiene archivos propios; se usó `develop` |
| Rama `branding`, carpeta `branding/` | commit `8f36c8c` (10 nov 2026, 21:32 hora de Quito) | `README.md`, `01`, `02`, `03`, `05` |
| canivoros.com | HTML descargado 10 nov 2026, 22:15 hora de Quito | Inicio, /nosotros/, /productos/ (incluye la FAQ), /distribuidores/, /contactanos/. `/preguntas-frecuentes/` da 404 |
| Instagram @canivoros_col | No leído | Sin sesión solo muestra la pantalla de inicio de sesión; la segunda consulta se agotó por tiempo |
| `ventas_canivoros_2026.xlsx` | No abierto | No hacía falta: los guiones no usan cifras ni datos de clientes |

## Para el bot Canívoros

Choques o vacíos que encontré al aplicar `branding/`. No los resolví.

1. **Recordatorio que estima consumo.** `02` §5 propone "Por lo que llevaste, a [perro] le debe quedar poquito." Eso supone una ración que no existe (BL-041) y E02 §6 prohíbe estimar duración sin gramos y consumo. Además usa diminutivo, que `02` §1 evita. En mis guiones el aviso sale de la fecha que eligió el cliente o de su intervalo real (BL-022 v1).
2. **"Hecho por criadores" como frase permitida.** `02` §4 lo pone en "Sí decir", pero `03` T5 pide confirmar primero que los perros de la familia comen el producto. El sitio afirma "campeones alimentados con Canívoros". Hace falta una sola regla. Por eso no usé "de criador a criador" en el guion de criadores.
3. **Quién habla.** `02` usa "Soy Omar, de Canívoros"; E02 §5.3 usa "somos Canívoros" y "responde BAJA". Yo seguí `02` (primera persona de Omar) con una salida en lenguaje natural ("me dices y listo"). Falta decidir si la palabra BAJA es obligatoria.
4. **"Listo para servir" y "carne de verdad".** `02` §5 y el pilar "Fácil de servir" de `01` §7 dependen de la conservación real, que el sitio describe como "lugar fresco y seco" (auditoría A1). "Carne de verdad" choca con la materia prima relatada (vísceras, cabezas).
5. **Promesa de entrega.** `03` §4 responde "No lo consigo cerca" con "Te lo llevamos". La cobertura es desconocida (E02 §1).
6. **"Que nutren"** en la respuesta sobre subproductos (`03` §4) es un claim nutricional. Dejé el reemplazo de "sin subproductos" (auditoría A2) a la redacción que aprueben ustedes.
7. **"Super premium" fuera de anuncios.** `01` §5 lo mantiene como Declaración; `03` §5 solo lo prohíbe en pauta. Para el sitio propuse quitarlo (M4). Falta la regla para canales propios.
8. **"Comida de verdad" (T1) y "nutrición de verdad" del sitio (M8)** sugieren que otras comidas no lo son. Propuse un reemplazo neutro para el sitio; el tagline es decisión suya.
9. **Lista de claims del sitio en `branding/README` punto 5.** El sitio vivo hoy no dice "100 % natural"; dice "Ingredientes 100% reales" y "100% carne real". Además hay claims que la lista no recoge: "longevidad", "taurina", "referentes colombianos", "ingredientes premium certificados" y "Cada punto de venta garantiza producto fresco". Detalle en la auditoría.
10. **Respuesta de Gatívoros en `03` §4** ya dice "salmón y cerdo" aunque la receta sigue sin confirmar (A15). Conviene bloquearla hasta BL-005.
