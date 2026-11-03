# Prospectos Canívoros · Bogotá · AAAA-MM-DD

Archivo único de prospectos, según `prospectos/AGENTS.md`. La tabla del registro también está en `prospectos-AAAA-MM-DD.csv` (mismo nombre): se genera con `registro.py csv` y no se edita a mano. El historial queda en git.

## Resumen general

- Revisados: N negocios en L lotes (P001–P0xx).
- Resultado: A a · B b · C c · descartados d.
- Los mejores: <nombre> (hecho clave) · <nombre> (…) · <nombre> (…).
- Debe decidir Andrés: <aprobaciones, dudas de clientes actuales, avisos de volumen grande>.

## Cómo se verificó

<!-- Fuentes que se pudieron leer, las que quedaron bloqueadas y qué significa "verificado" en este archivo. -->

## Registro

Una fila por negocio. Los ID (`P001`, `P002`…) no se reutilizan, ni siquiera si el negocio se descarta.

- **Tipo:** tienda, tienda natural, tienda online, veterinaria, criadero, adiestramiento, guardería, hotel, peluquería, club, otro.
- **Encaje:** hecho corto con marca de evidencia: (E) visto con URL y fecha, (D) lo dice el negocio, (H) interpretación, (V) dudoso o sin fecha.
- **Nivel:** A, B o C según la guía; `—` si está descartado.
- **Estado:** `por verificar` · `verificado` · `no verificado` (página bloqueada o una sola fuente) · `borrador listo` · `aprobado` (por Andrés) · `contactado` · `descartado: <motivo>`.
- **Fecha:** día de la última verificación (AAAA-MM-DD).
- Lo que no se sabe se escribe `desconocido`; ninguna celda queda vacía, salvo Notas.
- Nada de datos personales ni nombres de clientes actuales.

| ID | Nombre | Tipo | Localidad | Web o redes | Canal público | Encaje | Nivel | Estado | Fuentes | Fecha | Notas |
|---|---|---|---|---|---|---|---|---|---|---|---|

<!-- Un bloque "## Lote N" por lote, del más viejo al más nuevo, debajo del registro. Copia el bloque para cada lote nuevo y sigue la numeración. -->

## Lote 1 · AAAA-MM-DD · <tipo> · <localidad o barrio> (P0xx–P0yy)

### Resumen

1. Revisados: N negocios de <tipo> en <localidad> (P0xx–P0yy).
2. Resultado: A a · B b · C c · descartados d (motivo principal).
3. Los 3 mejores: <nombre> (por qué) · <nombre> (por qué) · <nombre> (por qué).
4. Quedó `desconocido`: <datos que faltaron y en cuántos negocios>.
5. Debe decidir Andrés: <aprobaciones, dudas de clientes actuales, avisos de volumen grande>.

Supuestos: <tipo o zona asumidos, si no los pidieron>.

### Búsquedas hechas

| Fecha | Fuente | Búsqueda | Resultados útiles |
|---|---|---|---|

### Notas del lote

Coincidencias con clientes del Excel de ventas: <número> (sin nombres).

### Fichas A

<!-- Una ficha "#### P0xx · <Nombre> (A)" por cada A, con el formato de references/abordaje.md -->

### Borradores B

<!-- Un título "#### P0xx · <Nombre> (B)" y un borrador por cada B -->
