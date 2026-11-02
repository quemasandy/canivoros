# Investigación de mercado · Canívoros en Bogotá

> **Documento vivo** de la fase 1 del playbook (mapa del mercado) y de la investigación agregada del consumidor. Instrucciones en [AGENTS.md](AGENTS.md) §4; reglas comunes en [../AGENTS.md](../AGENTS.md).
> Cada dato lleva etiqueta (E)/(D)/(H)/(V), fuente y fecha. Lo que no se sabe es `desconocido`.
> Sembrado el 2026-11-02 solo con lo que ya está en el repositorio. **Todavía no hay investigación web nueva.**

## 1. Preguntas que debe responder la investigación

| # | Pregunta | Dónde se responde | Estado |
|---|---|---|---|
| 1 | ¿Quién acepta un alimento horneado para perros? | BL-006, BL-007, §6 | Abierta |
| 2 | ¿Cuánto paga hoy un comprador por alimentar a su perro? | BL-006, `../competencia/` | Abierta |
| 3 | ¿Qué le impide cambiar de alimento? | BL-006, §6 | Abierta |
| 4 | ¿Dónde prefiere comprar (tienda, veterinaria, domicilio, app)? | BL-006, §4 | Abierta |
| 5 | ¿Qué presentación necesita y cada cuánto vuelve a comprar? | BL-006, BL-023, BL-004 | Abierta |
| 6 | ¿Qué marcas rotan en las tiendas y por qué? | BL-007, BL-012 | Abierta |
| 7 | ¿Qué condiciones piden las tiendas (pedido mínimo, margen, plazo, devoluciones)? | BL-007, BL-012 | Abierta |
| 8 | ¿Qué segmento compra más kilos con recompra y deja contribución positiva? | BL-004, BL-043, BL-025 | Abierta |

Las preguntas 1 a 5 vienen del plan (`../CANIVOROS-PLAN-CRECIMIENTO-BOGOTA.md`); las 6 a 8, del plan y del backlog.

## 2. Lo que ya sabemos

| Dato | Etiqueta | Fuente | Qué implica |
|---|---|---|---|
| En 2021, el 40,2 % de los hogares de Bogotá tenía mascota; de ellos, el 65,8 % tenía perro y el 43,7 % gato (los grupos se superponen) | (E) dato oficial histórico | [DANE, Encuesta Multipropósito 2021](https://www.dane.gov.co/files/investigaciones/multi/Comunicado_EM_2021.pdf), citado en el plan | Referencia de tenencia, **no** de demanda de alimento natural ni de ventas de Canívoros |
| La Cámara de Comercio de Bogotá lanzó en 2024 un Clúster de Protección y Bienestar Animal | (D) | [CCB](https://www.ccb.org.co/es/de-interes/comunicados/camara-de-comercio-de-bogota-lanza-iniciativa-cluster-de-proteccion-y-bienestar-animal-para-bogota-y-la-region), citado en el plan | Posible fuente de aliados y datos del sector (BL-046) |
| Pixie declara unos 90 puntos de venta en Bogotá, Peluditos BARF unos 50 y Vital Doggy unos 35 | (D) de cada marca | `../competencia/COMPETENCIA.md` | La categoría natural ya tiene red en tiendas: hay tiendas con clientes que conocen el natural |
| La lista inicial tiene 135 negocios: 102 tiendas (S1), 26 veterinarias (S2) y 7 distribuidores (S6). Suba (31) y Usaquén (26) concentran la mayor parte | (D)/(V) | `PROSPECTOS.md` | Densidad en el norte; **no hay ninguna cuenta de S3, S4 ni S5** |
| Las ventas de jul–oct 2026 se registran por separado para cliente final, almacén y criador; hay pedidos de criadores de 40 a 520 kg | (E) del archivo interno | `../ventas_canivoros_2026.xlsx`, BL-043 | Los criaderos (S3) pueden ser el segmento de mayor volumen |
| Hoy se vende sobre todo por relaciones personales y por la credibilidad de Omar en el mundo canino | (D) | `../erp.md` | Puente cálido probable en S3 y S4 |
| La responsable percibe que pocos clientes pagan la línea premium y que algunos compradores recortan el presupuesto de alimento | (D) | `../erp.md` | Probar presentaciones (BL-023) y segmentos antes de invertir en publicidad |
| BARF parece más barato por kg ($10.000–$22.500) que el horneado o cocido ($24.400–$27.960) | (V) precios sin fecha | `../competencia/COMPETENCIA.md` | Re-verificar antes de usarlo en precio o mensaje |

## 3. Tamaño del mercado (por completar)

El tamaño orienta dónde buscar; **no** es una proyección de ventas.

| Indicador | Valor | Fuente y fecha | Estado |
|---|---|---|---|
| Hogares de Bogotá | `desconocido` | DANE (año más reciente publicado) | Por buscar |
| Hogares con perro | `desconocido` | Cálculo: hogares × 40,2 % × 65,8 % (aproximado, datos 2021) | Depende del dato anterior |
| Puntos de venta de mascotas por localidad | `desconocido` | Conteo en Maps con búsqueda exacta y fecha | Por buscar |
| Veterinarias por localidad | `desconocido` | Conteo en Maps o registros públicos | Por buscar |
| Criaderos con presencia comercial en Bogotá | `desconocido` | Clubes de raza, Maps, redes | Por buscar |
| Servicios caninos (entrenamiento, guarderías, hoteles) | `desconocido` | Maps, redes | Por buscar |

## 4. Cuentas identificadas por segmento y localidad

Del registro actual (`PROSPECTOS.md`), por la primera localidad que aparece en la columna *Zona*. S3, S4 y S5 están en cero porque la lista inicial solo buscó tiendas y veterinarias.

| Localidad | S1 Tiendas | S2 Veterinarias | S6 Distribuidores | Total |
|---|---|---|---|---|
| Suba | 24 | 7 | 0 | 31 |
| Usaquén | 21 | 4 | 1 | 26 |
| Engativá | 11 | 3 | 1 | 15 |
| Kennedy | 7 | 4 | 3 | 14 |
| Chapinero | 8 | 1 | 1 | 10 |
| Fontibón | 7 | 0 | 0 | 7 |
| Puente Aranda | 4 | 2 | 0 | 6 |
| Teusaquillo | 4 | 1 | 0 | 5 |
| Barrios Unidos | 2 | 2 | 0 | 4 |
| Bosa | 3 | 0 | 0 | 3 |
| Antonio Nariño | 2 | 0 | 0 | 2 |
| Otras (Los Mártires, Tenjo, Susa, noroccidente) | 2 | 1 | 1 | 4 |
| Varias sedes (CEBA, Laika) | 1 | 1 | 0 | 2 |
| Sin localidad (solo «Bogotá») | 6 | 0 | 0 | 6 |
| **Total** | **102** | **26** | **7** | **135** |

| Segmento | Cuentas identificadas | Próximo paso |
|---|---|---|
| S3 Criaderos | 0 | Primer lote de búsqueda (AGENTS.md §5.2) |
| S4 Servicios caninos | 0 | Primer lote de búsqueda en Suba y Usaquén |
| S5 Perros de trabajo y deporte | 0 | Búsqueda exploratoria, solo para aprender |

Localidades sin ninguna cuenta todavía: Santa Fe, San Cristóbal, Usme, Tunjuelito, La Candelaria, Rafael Uribe Uribe, Ciudad Bolívar y Sumapaz. Que no haya cuentas en la lista no significa que no haya negocios: la lista inicial no las cubrió.

## 5. Microzonas candidatas (BL-014)

Puntaje de cada criterio de 1 a 5, **solo con evidencia**. Resultado = suma de (peso × puntaje) ÷ 5, en escala de 0 a 100 (fórmula del plan).

| Microzona | Demanda observada (30 %) | Contribución después de entrega (25 %) | Calidad de aliados (20 %) | Facilidad logística (15 %) | Oportunidad frente a competidores (10 %) | Puntaje |
|---|---|---|---|---|---|---|
| Noroccidente: Suba, alrededor de Manimal | sin evidencia | sin evidencia | sin evidencia | sin evidencia | sin evidencia | — |
| Norte: Usaquén y Cedritos | sin evidencia | sin evidencia | sin evidencia | sin evidencia | sin evidencia | — |
| Sur: Bosa y Kennedy, alrededor de Sankatin | sin evidencia | sin evidencia | sin evidencia | sin evidencia | sin evidencia | — |

No uses el estrato como sustituto de la disposición a pagar. El tamaño de la zona se ajusta a la capacidad comercial y logística del piloto.

## 6. Voz del consumidor (agregada)

Patrones de reseñas y de conversaciones públicas. Sin autores ni datos de personas.

| Tema | Menciones revisadas | Fuentes y fechas | Patrón observado | Hipótesis que sugiere |
|---|---|---|---|---|
| Aceptación del perro | 0 | — | — | — |
| Precio | 0 | — | — | — |
| Entrega y disponibilidad | 0 | — | — | — |
| Empaque y conservación | 0 | — | — | — |
| Atención | 0 | — | — | — |

## 7. Hallazgos → hipótesis → prueba

| # | Hipótesis (H) | Base | Prueba comercial | Métrica | Tarea |
|---|---|---|---|---|---|
| 1 | Las tiendas que ya venden natural compran y reponen más rápido que las demás | Directorios de marcas (D) | En BL-012, comparar tiendas con y sin natural verificado | Respuesta, pedido y reposición por grupo | BL-012 |
| 2 | Los criaderos compran mucho volumen y además recomiendan el alimento a quienes compran cachorros | Pedidos de criadores de 40–520 kg (E interno) | Identificar 15–20 criaderos con presencia comercial y conversar con 3 | Kilos recurrentes; cachorros referidos con código | BL-043 |
| 3 | El norte concentra la oferta natural, pero también la competencia | Densidad de la lista (D/V) | Comparar un lote del norte con uno del sur con la misma oferta | Respuesta y pedido por zona | BL-014 |
| 4 | Los servicios caninos sirven como canal de recomendación | Club Canes como aliado (D); segmento «perros activos» del plan | Piloto con 3 servicios con código propio | Pedidos referidos por servicio | BL-021 |
| 5 | Mostrar el origen en perros de competencia abre más puertas en S3 y S4 que en S1 | Credibilidad de Omar (D) | Comparar respuesta al toque 1 por segmento | Tasa de respuesta | BL-020 |

Antes de lanzar cualquiera, llena la ficha de BL-044: hipótesis, métrica principal, número de casos, gasto máximo y regla de seguir, ajustar o parar.

## 8. Historial

### Siembra 2026-11-02
- Creado con datos del plan, `erp.md`, el Excel de ventas (solo agregados), `PROSPECTOS.md` y `../competencia/COMPETENCIA.md`.
- Sin búsquedas web. Todos los tamaños de mercado quedan `desconocido`.
