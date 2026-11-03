# Guía para prospectar clientes de Canívoros en Bogotá

Esta guía es para cualquier agente de IA que busque clientes para Canívoros en Bogotá.
Las reglas generales del proyecto están en `../AGENTS.md`.

## Objetivo

Encontrar **negocios de Bogotá que puedan comprar y volver a comprar Canívoros**, verificarlos con datos públicos, priorizarlos y preparar borradores de mensaje para que el equipo los contacte.

## Canívoros en pocas líneas

- Alimento natural **horneado** para perros, hecho en Sopó, Cundinamarca.
- Formatos: hamburguesas y chorizos de pollo, salmón, cerdo y ternera; listo para servir.
- Se vende por WhatsApp, a criadores por kilo y en algunas tiendas y veterinarias.
- Origen de la marca: una familia que cría perros de competencia.
- Precio a tiendas, pedido mínimo y conservación en tienda: `desconocido`. **No los prometas.**

Más detalle en `../CANIVOROS-REFERENCIA-EMPRESA.md` y `../erp.md`.

## A quién buscar

| Prioridad | Tipo de cliente | Por qué |
|---|---|---|
| Alta | Tiendas de mascotas (pet shops, tiendas de alimento natural, tiendas online) | Revenden; muchas ya venden marcas naturales |
| Alta | Veterinarias con punto de venta | Revenden y recomiendan |
| Alta | Criaderos de perros | Compran mucho volumen y recomiendan a quienes compran cachorros |
| Media | Servicios caninos: adiestramiento, guarderías, hoteles, peluquerías | Alimentan perros y pueden recomendar o revender |
| Baja | Clubes de deporte canino, empresas de seguridad con perros, distribuidores mayoristas | Por explorar |

No se prospectan personas (dueños de perros) una por una.

## Paso 1 · Elige segmento y zona

Trabaja por lotes de **máximo 10 negocios** de un mismo tipo y una misma zona de Bogotá (localidad o barrio).

## Paso 2 · Busca negocios

Búsquedas sugeridas (en Google y Google Maps). Reemplaza `{localidad}`, `{barrio}` y `{raza}`:

| Tipo | Búsquedas |
|---|---|
| Tiendas | "pet shop {barrio}", "tienda de mascotas {localidad}", "comida natural para perros {localidad}", "BARF {localidad}" |
| Veterinarias | "veterinaria {barrio}", "clínica veterinaria {localidad}" |
| Criaderos | "criadero de perros Bogotá", "criadero {raza} Bogotá" |
| Servicios | "adiestramiento canino Bogotá", "guardería canina {localidad}", "hotel para perros Bogotá" |

Otras fuentes útiles:

- Páginas de "dónde comprar" de marcas naturales (Pixie, Peluditos BARF, Vital Doggy, Rawf, Kanuto): muestran tiendas que ya venden natural.
- Rappi (categoría mascotas), Instagram y Facebook de negocios.
- Clubes de raza y eventos caninos (para criaderos y adiestradores).

## Paso 3 · Verifica cada negocio

- **Existe y opera:** ficha de Maps activa, reseña o publicación reciente.
- **Datos comerciales:** dirección del negocio, localidad, web, redes y canal de contacto público (WhatsApp o correo del negocio).
- **Encaje:** ¿vende o usa alimento natural, BARF u horneado? ¿Atiende sobre todo perros? ¿Tiene congelador o nevera?
- **Tamaño:** número de sedes, número de reseñas, cantidad de perros.

Anota la URL y la fecha de cada dato.

## Paso 4 · Prioriza

| Nivel | Cuándo |
|---|---|
| **A** | Verificado, atiende perros y ya trabaja con alimento natural o maneja mucho volumen |
| **B** | Verificado y atiende perros, pero sin señales claras de alimento natural |
| **C** | Datos incompletos o poco encaje |

Descarta: negocios cerrados, duplicados, clientes actuales, personas sin negocio y negocios solo de gatos.

## Paso 5 · Prepara el abordaje

Para cada negocio **A** escribe:

- Por qué es buen cliente (2 o 3 hechos con fuente).
- Qué le puede interesar de Canívoros.
- Preguntas para la primera conversación (qué marcas vende, cuánto rota, si tiene frío, cómo compra).
- **Un borrador de mensaje** corto, personalizado y sin precios, sin condiciones y sin beneficios de salud.

Para los **B**, solo el borrador. Los **C** quedan en la lista.

## Qué se puede decir de Canívoros

- Sí: alimento horneado para perros, hecho en Sopó, con proteína animal (pollo, salmón, cerdo), listo para servir, nacido de la crianza de perros de competencia.
- No: beneficios de salud, "sin subproductos", "super premium", "registro ICA", precios ni condiciones.
- Número de contacto en borradores: `[número comercial por definir]`.

## Cómo marcar la evidencia

- **(E)** Lo viste en una fuente, con URL y fecha.
- **(D)** Lo dice el negocio de sí mismo.
- **(H)** Tu interpretación.
- **(V)** Dato dudoso o sin fecha.
- Lo que no sabes: `desconocido`.

## Dónde guardar los resultados

En esta misma carpeta, `prospectos/`:

- `REGISTRO.md`: una fila por negocio con ID `P001`, `P002`… (no se reutilizan): nombre, tipo, localidad, web o redes, canal público, encaje, nivel A/B/C, estado y fuentes.
- `lote-AAAA-MM-DD.md`: búsquedas hechas, negocios revisados, fichas de los A y B, y borradores.

## Límites

- **Nunca contactes a nadie.** Los mensajes son borradores; Andrés aprueba cada contacto.
- Solo datos comerciales públicos de negocios. Nada de datos personales (celulares personales, direcciones de vivienda, cédulas, nombres de clientes).
- Si una página pide login o bloquea, anota "No verificado". No evadas bloqueos.
- Si un cliente podría pedir volúmenes muy grandes, avísalo: la capacidad de producción es `desconocido`.
