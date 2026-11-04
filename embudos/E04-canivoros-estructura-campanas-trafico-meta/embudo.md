# E04 · Canívoros: estructura de campañas de tráfico en Meta (clon exacto del video)

- **Fuente:** YouTube «Cómo pasé de $0 a $95K en 6 meses con UN solo funnel (nadie habla de esto)» — https://www.youtube.com/watch?v=pSi2YN5NNSQ (47:05). Llamada grabada (Felipe Carvajal, Marcos Poole, José Antonio García Jordán) con un tablero Miro «TRAINING».
- **Tipo:** clon fiel, no adaptación. Lo propio de Canívoros queda como `[[ ]]` o `desconocido`.
- **Estado:** borrador · Creado 2026-11-03.
- **Leyenda de origen:** 🟦 **leído en pantalla** · 🗣️ **dicho por el narrador** · ⚠️ **supuesto**.

El tablero muestra **4 diagramas** (el video no presenta páginas, formularios ni anuncios: es la estructura de prueba y escalado de campañas de tráfico a perfil):

1. Estructuras de campaña por presupuesto: $30/día, $100/día, $250/día (árboles Campaña → Conjunto → Anuncio, coloreados a mano verde/amarillo/rojo).
2. Business Manager (Segmentación Abierta) — flujo de prueba de 8 días y escalado.
3. Business Manager (Segmentación Intereses) — mismo flujo, otros KPI.
4. Requerimientos → Business Manager (Segmentación Lookalike) — mismo flujo.

Las cifras ($, KPI) que aparecen son **las del tablero del video** (🟦), no de Canívoros. Para Canívoros: presupuesto `[[presupuesto diario Canívoros]]`, KPI `desconocido`.

## 1. Estructuras por presupuesto

![E04-1](E04-1-estructuras-presupuesto.png)

```mermaid
flowchart LR
  classDef caja fill:#ffffff,stroke:#222,stroke-width:2px,color:#111,font-weight:bold
  classDef verde fill:#3fd35a,stroke:#222,color:#111
  classDef amarillo fill:#ffe033,stroke:#222,color:#111
  classDef rojo fill:#f0505a,stroke:#222,color:#111
  classDef nota fill:#ffe033,stroke:#222,color:#111,font-weight:bold
  classDef rosa fill:#f9c9cc,stroke:#222,color:#111,font-weight:bold
  classDef verdeclaro fill:#b6f5c4,stroke:#222,color:#111,font-weight:bold
  classDef titulo fill:#ffffff,stroke:#ffffff,color:#111,font-size:18px

  subgraph S30["$30/día"]
    direction TB
    P30["$30/día"]:::caja
    C30["Campaña"]:::caja
  P30 --> C30
      J30_0["Conjunto"]:::caja
  C30 --> J30_0
    A30_0["Anuncio"]:::verde
  J30_0 --> A30_0
    A30_1["Anuncio"]:::amarillo
  J30_0 --> A30_1
    A30_2["Anuncio"]:::rojo
  J30_0 --> A30_2
  end
  subgraph S100["$100/día"]
    direction TB
    P100["$100/día"]:::caja
    C100["Campaña"]:::caja
  P100 --> C100
      J100_0["Conjunto"]:::caja
      J100_1["Conjunto"]:::caja
  C100 --> J100_0
  C100 --> J100_1
    A100_0["Anuncio"]:::verde
  J100_0 --> A100_0
    A100_1["Anuncio"]:::amarillo
  J100_0 --> A100_1
    A100_2["Anuncio"]:::verde
  J100_1 --> A100_2
    A100_3["Anuncio"]:::amarillo
  J100_1 --> A100_3
  end
  subgraph S250["$250/día"]
    direction TB
    P250["$250/día"]:::caja
    C250["Campaña"]:::caja
  P250 --> C250
      J250_0["Conjunto"]:::caja
      J250_1["Conjunto"]:::caja
      J250_2["Conjunto"]:::caja
  C250 --> J250_0
  C250 --> J250_1
  C250 --> J250_2
    A250_0["Anuncio"]:::verde
  J250_0 --> A250_0
    A250_1["Anuncio"]:::rojo
  J250_0 --> A250_1
    A250_2["Anuncio"]:::amarillo
  J250_0 --> A250_2
    A250_3["Anuncio"]:::verde
  J250_1 --> A250_3
    A250_4["Anuncio"]:::rojo
  J250_1 --> A250_4
    A250_5["Anuncio"]:::amarillo
  J250_1 --> A250_5
    A250_6["Anuncio"]:::verde
  J250_2 --> A250_6
    A250_7["Anuncio"]:::rojo
  J250_2 --> A250_7
    A250_8["Anuncio"]:::amarillo
  J250_2 --> A250_8
  end
  S30 ~~~ S100
  S100 ~~~ S250
  J100_0 <==> J100_1
  linkStyle 27 stroke:#f0505a,stroke-width:7px
```

## 2. Business Manager (Segmentación Abierta)

![E04-2](E04-2-bm-segmentacion-abierta.png)

```mermaid
flowchart TB
  classDef caja fill:#ffffff,stroke:#222,stroke-width:2px,color:#111,font-weight:bold
  classDef verde fill:#3fd35a,stroke:#222,color:#111
  classDef amarillo fill:#ffe033,stroke:#222,color:#111
  classDef rojo fill:#f0505a,stroke:#222,color:#111
  classDef nota fill:#ffe033,stroke:#222,color:#111,font-weight:bold
  classDef rosa fill:#f9c9cc,stroke:#222,color:#111,font-weight:bold
  classDef verdeclaro fill:#b6f5c4,stroke:#222,color:#111,font-weight:bold
  classDef titulo fill:#ffffff,stroke:#ffffff,color:#111,font-size:18px

  T["<b>Business Manager</b><br/>(Segmentación Abierta)"]:::titulo --> CP["Cuenta<br/>Publicitaria"]:::caja
  CP --> CT["Campaña de<br/>Tráfico"]:::caja
  CT --> SG["Segmentación<br/>Abierta"]:::caja
  SG --> P30["$30/día"]:::caja
    V1["$10/día"]:::caja
    V2["$10/día"]:::caja
    V3["$10/día"]:::caja
  P30 --> V1
  P30 -- "Ángulo" --> V2
  P30 --> V3
  V1 --> D4["$120"]:::caja
  V2 -- "Dia 4<br/>(Total)" --> D4
  V3 --> D4
  D4 --> SI["Si cumple los<br/>KPI's"]:::caja
  D4 --> NO["No cumple los<br/>KPI's"]:::caja
  NO --> AP["Apágalo"]:::caja
  SI -- "Día 8" --> IG["Identifica el<br/>anuncio<br/>ganador"]:::caja
  IG --> AP
    W1["$10/día"]:::caja
    W2["$10/día"]:::caja
    W3["$10/día"]:::caja
  IG --> W1
  IG --> W2
  IG --> W3
  W2 --> DP["Distribuir el<br/>presupuesto<br/>al anuncio ganador"]:::caja
  DP --> G30["$30/día"]:::caja
    AN1["Anuncio 1"]:::rosa
    AN2["Anuncio 2"]:::rosa
    AN3["Anuncio 3"]:::verdeclaro
  G30 --> AN3
  G30 ~~~ AN1
  G30 ~~~ AN2
    S1["Anuncio<br/>3.1"]:::verdeclaro
    S2["Anuncio<br/>3.2"]:::verdeclaro
    S3["Anuncio<br/>3.3"]:::verdeclaro
  AN3 --> S1
  S1 --> Q1["$30/día"]:::nota
  AN3 --> S2
  S2 --> Q2["$30/día"]:::nota
  AN3 --> S3
  S3 --> Q3["$30/día"]:::nota
  subgraph KN[" "]
    direction TB
    K1["CPV<br/>B2B = $0.05 - $0.25<br/>B2C = $0.02 - $0.10"]:::nota
    K2["CPF<br/>B2B = $3 - $10<br/>B2C = $1 - $5"]:::nota
    K3["25% seguidores<br/>calificados"]:::nota
    K4["10%<br/>conversaciones<br/>califcadas"]:::nota
    K1 ~~~ K2
    K2 ~~~ K3
    K3 ~~~ K4
  end
  style KN fill:none,stroke:none
  P30 ~~~ KN
```

## 3. Business Manager (Segmentación Intereses)

![E04-3](E04-3-bm-segmentacion-intereses.png)

```mermaid
flowchart TB
  classDef caja fill:#ffffff,stroke:#222,stroke-width:2px,color:#111,font-weight:bold
  classDef verde fill:#3fd35a,stroke:#222,color:#111
  classDef amarillo fill:#ffe033,stroke:#222,color:#111
  classDef rojo fill:#f0505a,stroke:#222,color:#111
  classDef nota fill:#ffe033,stroke:#222,color:#111,font-weight:bold
  classDef rosa fill:#f9c9cc,stroke:#222,color:#111,font-weight:bold
  classDef verdeclaro fill:#b6f5c4,stroke:#222,color:#111,font-weight:bold
  classDef titulo fill:#ffffff,stroke:#ffffff,color:#111,font-size:18px

  T["<b>Business Manager</b><br/>(Segmentación Intereses)"]:::titulo --> CP["Cuenta<br/>Publicitaria"]:::caja
  CP --> CT["Campaña de<br/>Tráfico"]:::caja
  CT --> SG["Segmentación<br/>Intereses"]:::caja
  SG --> P30["$30/día"]:::caja
    V1["$10/día"]:::caja
    V2["$10/día"]:::caja
    V3["$10/día"]:::caja
  P30 --> V1
  P30 -- "Ángulo" --> V2
  P30 --> V3
  V1 --> D4["$120"]:::caja
  V2 -- "Dia 4<br/>(Total)" --> D4
  V3 --> D4
  D4 --> SI["Si cumple los<br/>KPI's"]:::caja
  D4 --> NO["No cumple los<br/>KPI's"]:::caja
  NO --> AP["Apágalo"]:::caja
  SI -- "Día 8" --> IG["Identifica el<br/>anuncio<br/>ganador"]:::caja
  IG --> AP
    W1["$10/día"]:::caja
    W2["$10/día"]:::caja
    W3["$10/día"]:::caja
  IG --> W1
  IG --> W2
  IG --> W3
  W2 --> DP["Distribuir el<br/>presupuesto<br/>al anuncio ganador"]:::caja
  DP --> G30["$30/día"]:::caja
    AN1["Anuncio 1"]:::rosa
    AN2["Anuncio 2"]:::verdeclaro
    AN3["Anuncio 3"]:::rosa
  G30 --> AN2
  G30 ~~~ AN1
  G30 ~~~ AN3
    S1["Anuncio<br/>2.1"]:::verdeclaro
    S2["Anuncio<br/>2.2"]:::verdeclaro
    S3["Anuncio<br/>2.3"]:::verdeclaro
  AN2 --> S1
  S1 --> Q1["$30/día"]:::nota
  AN2 --> S2
  S2 --> Q2["$30/día"]:::nota
  AN2 --> S3
  S3 --> Q3["$30/día"]:::nota
  subgraph KN[" "]
    direction TB
    K1["CPV<br/>B2B = $0.10 - $0.35<br/>B2C = $0.05 - $0.20"]:::nota
    K2["CPF<br/>B2B = $3 - $15<br/>B2C = $1 - $8"]:::nota
    K3["25% seguidores<br/>calificados"]:::nota
    K4["10%<br/>conversaciones<br/>califcadas"]:::nota
    K1 ~~~ K2
    K2 ~~~ K3
    K3 ~~~ K4
  end
  style KN fill:none,stroke:none
  P30 ~~~ KN
```

## 4. Business Manager (Segmentación Lookalike)

![E04-4](E04-4-bm-segmentacion-lookalike.png)

```mermaid
flowchart TB
  classDef caja fill:#ffffff,stroke:#222,stroke-width:2px,color:#111,font-weight:bold
  classDef verde fill:#3fd35a,stroke:#222,color:#111
  classDef amarillo fill:#ffe033,stroke:#222,color:#111
  classDef rojo fill:#f0505a,stroke:#222,color:#111
  classDef nota fill:#ffe033,stroke:#222,color:#111,font-weight:bold
  classDef rosa fill:#f9c9cc,stroke:#222,color:#111,font-weight:bold
  classDef verdeclaro fill:#b6f5c4,stroke:#222,color:#111,font-weight:bold
  classDef titulo fill:#ffffff,stroke:#ffffff,color:#111,font-size:18px

  R["<b>Requerimientos</b><br/>2500 seguidores<br/>$1,000<br/>Audiencia de alta calidad"]:::caja --> T
  T["<b>Business Manager</b><br/>(Segmentación Lookalike)"]:::titulo --> CP["Cuenta<br/>Publicitaria"]:::caja
  CP --> CT["Campaña de<br/>Tráfico"]:::caja
  CT --> SG["Segmentación<br/>Lookalike"]:::caja
  SG --> P30["$30/día"]:::caja
    V1["$10/día"]:::caja
    V2["$10/día"]:::caja
    V3["$10/día"]:::caja
  P30 --> V1
  P30 -- "Ángulo" --> V2
  P30 --> V3
  V1 --> D4["$120"]:::caja
  V2 -- "Dia 4<br/>(Total)" --> D4
  V3 --> D4
  D4 --> SI["Si cumple los<br/>KPI's"]:::caja
  D4 --> NO["No cumple los<br/>KPI's"]:::caja
  NO --> AP["Apágalo"]:::caja
  SI -- "Día 8" --> IG["Identifica el<br/>anuncio<br/>ganador"]:::caja
  IG --> AP
    W1["$10/día"]:::caja
    W2["$10/día"]:::caja
    W3["$10/día"]:::caja
  IG --> W1
  IG --> W2
  IG --> W3
  W2 --> DP["Distribuir el<br/>presupuesto<br/>al anuncio ganador"]:::caja
  DP --> G30["$30/día"]:::caja
    AN1["Anuncio 1"]:::verdeclaro
    AN2["Anuncio 2"]:::rosa
    AN3["Anuncio 3"]:::rosa
  G30 --> AN1
  G30 ~~~ AN2
  G30 ~~~ AN3
    S1["Anuncio<br/>1.1"]:::verdeclaro
    S2["Anuncio<br/>1.2"]:::verdeclaro
    S3["Anuncio<br/>1.3"]:::verdeclaro
  AN1 --> S1
  S1 --> Q1["$30/día"]:::nota
  AN1 --> S2
  S2 --> Q2["$30/día"]:::nota
  AN1 --> S3
  S3 --> Q3["$30/día"]:::nota
  subgraph KN[" "]
    direction TB
    K1["CPV<br/>[[ilegible en video]]"]:::nota
    K2["CPF<br/>[[ilegible en video]]"]:::nota
    K3["25% seguidores<br/>calificados"]:::nota
    K4["10%<br/>conversaciones<br/>califcadas"]:::nota
    K1 ~~~ K2
    K2 ~~~ K3
    K3 ~~~ K4
  end
  style KN fill:none,stroke:none
  P30 ~~~ KN
```

## Tabla de etapas (flujos 2–4)

| # | Nodo (tal como se lee) | Qué es | Origen | Canívoros |
|---|---|---|---|---|
| 0 | Requerimientos: 2500 seguidores · $1,000 · Audiencia de alta calidad | Solo flujo Lookalike; narrador: «por lo menos 2,500 seguidores, haber invertido por lo menos $1,000 en ads» (31:55) | 🟦🗣️ | `desconocido` (seguidores y gasto histórico de Canívoros) |
| 1 | Business Manager (Segmentación …) | Encabezado | 🟦 | — |
| 2 | Cuenta Publicitaria → Campaña de Tráfico → Segmentación Abierta / Intereses / Lookalike | Campaña de tráfico a perfil (Instagram) | 🟦 · objetivo «perfil de Instagram» visto en Ads Manager (🟦 ~24:20) | `[[cuenta publicitaria Canívoros]]` |
| 3 | $30/día → (Ángulo) → $10/día ↔ $10/día ↔ $10/día | 1 ángulo creativo, 3 videos a $10/día c/u | 🟦🗣️ (11:20) | `[[ángulo Canívoros]]`, `[[3 videos]]` |
| 4 | Dia 4 (Total) · $120 | No tocar 4 días | 🟦🗣️ (11:43) | — |
| 5 | Si cumple los KPI's / No cumple los KPI's → Apágalo | Decisión día 4 con CPV y CPF | 🟦🗣️ (12:24) | KPI `desconocido` |
| 6 | Día 8 · Identifica el anuncio ganador (los demás → Apágalo) | Setter mide 25% seguidores calificados y 10% conversaciones calificadas | 🟦🗣️ (12:44–13:24) | `[[setter Canívoros]]` |
| 7 | $10/día ↔ $10/día ↔ $10/día → Distribuir el presupuesto al anuncio ganador → $30/día | Todo el presupuesto al ganador | 🟦🗣️ (14:27) | — |
| 8 | Anuncio 1 ↔ Anuncio 2 ↔ Anuncio N (ganador en verde) | Abierta: Anuncio 3; Intereses: Anuncio 2; Lookalike: Anuncio 1 | 🟦 (Lookalike ⚠️ leído en toma amplia) | — |
| 9 | Anuncio N.1 / N.2 / N.3 → $30/día c/u | 3 versiones del ganador grabadas distinto (selfie, doble cámara); repetir el proceso | 🟦🗣️ (15:05–15:49) | `[[versiones del ganador]]` |

KPI del tablero (🟦):

| Flujo | CPV | CPF | Día 8 |
|---|---|---|---|
| Abierta | B2B = $0.05 - $0.25 · B2C = $0.02 - $0.10 | B2B = $3 - $10 · B2C = $1 - $5 | 25% seguidores calificados · 10% conversaciones califcadas |
| Intereses | B2B = $0.10 - $0.35 · B2C = $0.05 - $0.20 | B2B = $3 - $15 · B2C = $1 - $8 | igual |
| Lookalike | `ilegible` | `ilegible` | igual (⚠️ toma amplia) |

## Activos

| Activo | Estado Canívoros |
|---|---|
| Cuenta publicitaria / Business Manager | `[[ ]]` |
| 1 ángulo creativo + 3 videos | `[[ ]]` |
| Setter que califica seguidores y conversaciones | `[[ ]]` |
| Audiencia semilla para Lookalike (2500 seguidores, $1,000 invertidos) | `desconocido` |
| Lista de intereses (narrador: 1 o 5–10 intereses, solo intereses, no job titles/demographics/behaviors, 26:25–26:49) | `[[ ]]` |

## Verificación contra el video (cuadros revisados)

- [x] 00:30 — toma amplia: 3 árboles a la izquierda y 3 columnas de flujo.
- [x] 09:20–10:20 — árboles $30/día, $100/día, $250/día con colores a mano; trazo rojo entre los 2 Conjuntos de $100/día.
- [x] 11:05 — encabezado «Business Manager (Segmentación Abierta)», Cuenta Publicitaria, Campaña de Tráfico, Segmentación Abierta.
- [x] 11:35–12:05 — $30/día, Ángulo, 3×$10/día, Dia 4 (Total), $120, CPV y CPF (abierta).
- [x] 12:40–13:05 — Si/No cumple los KPI's, Apágalo, Día 8, Identifica el anuncio ganador, notas 25%/10%.
- [x] 14:35–15:35 — Distribuir el presupuesto al anuncio ganador, $30/día, Anuncio 1/2 (rosa), Anuncio 3 (verde), Anuncio 3.1/3.2/3.3, $30/día (amarillo).
- [x] 24:20–25:30 — columna Intereses: CPV/CPF distintos; Anuncio 2 en verde.
- [x] 31:50–32:10 — Requerimientos (2500 seguidores, $1,000, Audiencia de alta calidad) → Business Manager (Segmentación Lookalike).
- [x] 32:45 — dos columnas lado a lado: en Lookalike el verde es el Anuncio 1.

## Brechas abiertas

- CPV/CPF del flujo Lookalike: ilegibles (solo vistos en toma amplia).
- Las flechas ↔ entre hermanos ($10/día, Anuncio 1↔2↔3) no se dibujan en mermaid sin romper la disposición; quedan como hermanos en la misma fila. El trazo rojo de $100/día se conserva.
- El orden izquierda-derecha de colores en los árboles lo reordena el motor de mermaid (⚠️ aproximado). En el tablero: $30/día verde-amarillo-rojo; $100/día verde-amarillo | verde-amarillo; $250/día verde-rojo-amarillo ×3 (⚠️ el último leído en toma amplia).
- La flecha Identifica el anuncio ganador → Apágalo sale a la derecha en el tablero; mermaid la ubica distinto.
- Nada del video define páginas, oferta ni precios: para Canívoros todo es `desconocido`.
- 🗣️ Ejemplo del narrador (no del tablero): $1,000 → 100 seguidores → 25 calificados → 10 conversaciones → 1–2 llamadas → venta de 10k, ROAS 10 (13:30–13:54). No aplica a Canívoros.

## Historial

- 2026-11-03 — v1: clon de los 4 diagramas del tablero del video (Grok Bot para Andrés).
