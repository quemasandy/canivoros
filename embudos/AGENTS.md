# Guía para diseñar embudos de venta de Canívoros

Esta guía es para cualquier agente de IA que diseñe, calcule o audite embudos de venta en este repositorio.
Las reglas generales del proyecto están en `../AGENTS.md`.

## Objetivo

Diseñar embudos que lleven a un cliente de Bogotá desde conocer Canívoros hasta comprar y **volver a comprar**, con textos listos, seguimiento definido y números medibles.

## Qué se guarda aquí

```
embudos/
├── AGENTS.md            # esta guía
├── CLAUDE.md
├── EMBUDOS.md           # registro: una fila por embudo
└── E01-<nombre>/        # una carpeta por embudo
    ├── embudo.md        # el documento del embudo (borrador)
    ├── calculo.json     # entradas de la calculadora
    ├── numeros.md       # salida de la calculadora
    └── auditoria-AAAA-MM-DD.md   # revisiones con datos reales
```

- Cada embudo tiene un ID (`E01`, `E02`…) que no se reutiliza, aunque se descarte.
- Nombre de carpeta: `E01-<negocio>-<tipo>`, en minúsculas y con guiones. Ejemplo: `E01-canivoros-whatsapp-recompra`.
- Si el embudo ya existe, se actualiza su carpeta. No se crean copias. Los cambios se anotan en la sección «Historial» de `embudo.md`.
- Una auditoría de un embudo registrado va en su carpeta como `auditoria-AAAA-MM-DD.md`.

## Reglas

- Todo es **borrador** hasta que Andrés lo apruebe. No se publican anuncios ni se envían mensajes.
- Cada número lleva su marca: **dato** (medido), **supuesto** (estimación a validar) o **meta**.
- Lo que no se sabe se escribe `desconocido`. Precio, costo y margen de Canívoros son `desconocido` hasta que se confirmen (BL-005, BL-025). Si el usuario da una cifra, se usa como **supuesto del usuario** y se dice.
- Sin precio ni costo confirmados, los volúmenes (cuántas conversaciones o leads hacen falta) sí se calculan; la parte de dinero queda como escenario.
- No inventes testimonios ni beneficios de salud. Usa solo lo publicado por la marca y preséntalo como experiencia individual.
- Mensajes a clientes solo con permiso (Ley 1581 de 2012). Guarda el permiso en el CRM.
- No guardes datos personales de clientes en esta carpeta.

## Tareas del backlog relacionadas

BL-019 (captura de leads por WhatsApp), BL-020 (comparar mensajes), BL-021 (origen de las ventas), BL-022 (recordatorio de reposición), BL-041 (raciones), BL-044 (hipótesis antes de experimentar), BL-058 (permiso de datos).
