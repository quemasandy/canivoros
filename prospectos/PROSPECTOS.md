# Prospectos B2B de Canívoros · Bogotá

> **Registro único de la prospección B2B** (tiendas, veterinarias, pet shops, centros de entrenamiento y distribuidores). Instrucciones en [AGENTS.md](AGENTS.md); reglas comunes en [../AGENTS.md](../AGENTS.md).
> Sembrado el 2026-11-02 desde la lista inicial `prospectos_bogota.xlsx/csv`, hecha con ayuda de IA. **Nadie fue contactado.** Todos los datos están **por verificar**.
> Alimenta BL-010 (verificar), BL-012 (10 tiendas), BL-014 (microzonas), BL-035 (aliados actuales) y BL-026 (gatos, más adelante).

## Cómo leer este archivo

- **`por_verificar`:** dato de la lista inicial o de un directorio de distribuidores de una marca; nadie lo ha confirmado en una fuente del negocio. No se usa como gancho en un mensaje hasta verificarlo (AGENTS.md §5).
- **Marcas (según fuente):** en la lista inicial salen casi siempre de los directorios de distribuidores de las marcas: Pixie aparece en 77 filas, Peluditos BARF en 23 y Vital Doggy en 17. Es una **declaración de la marca (D)**, no una observación de la tienda.
- **Encaje:** Alto = vende alimento natural; Medio = premium sin natural observado; Bajo = masivo o dudoso; Existente = aliado actual. Reglas en AGENTS.md §2.3.
- **Estados del equipo comercial** (`contactado`, `respondio`, `muestra`, `pedido`, `reposicion`, `perdido`): los registra solo Andrés o a quien él designe. Un agente nunca los cambia.

## Resumen

- **135 negocios** en la lista inicial: 2 aliados existentes, 112 de encaje Alto, 17 Medio y 4 Bajo. (BL-010 habla de 134; la diferencia de una fila está por revisar).
- **0 verificados** con el protocolo. **0 listos para contactar. 0 contactados.**
- 108 filas sin web ni Instagram, 10 sin teléfono y 7 sin dirección.

### Por localidad

Clasificado por la primera localidad que aparece en la columna *Zona* (aproximado; las cadenas cuentan en una sola zona).

| Localidad | Alto | Medio | Bajo | Existente | Total |
|---|---|---|---|---|---|
| Suba | 30 | 1 | 0 | 0 | 31 |
| Usaquén | 20 | 6 | 0 | 0 | 26 |
| Engativá | 14 | 1 | 0 | 0 | 15 |
| Kennedy | 11 | 2 | 1 | 0 | 14 |
| Chapinero | 7 | 2 | 1 | 0 | 10 |
| Fontibón | 7 | 0 | 0 | 0 | 7 |
| Puente Aranda | 6 | 0 | 0 | 0 | 6 |
| Teusaquillo | 5 | 0 | 0 | 0 | 5 |
| Barrios Unidos | 4 | 0 | 0 | 0 | 4 |
| Bosa | 2 | 0 | 0 | 1 | 3 |
| Antonio Nariño | 2 | 0 | 0 | 0 | 2 |
| Otras (Los Mártires, Tenjo, Susa, noroccidente) | 2 | 0 | 1 | 1 | 4 |
| Varias sedes (CEBA, Laika) | 2 | 0 | 0 | 0 | 2 |
| Sin localidad (solo «Bogotá») | 0 | 5 | 1 | 0 | 6 |
| **Total** | **112** | **17** | **4** | **2** | **135** |

## Qué hacer ahora (BL-010 → BL-012)

1. **BL-035:** confirmar si Manimal y Sankatin siguen activos (lo hace el equipo, no un agente). Pista (V): en `ventas_canivoros_2026.xlsx` aparece un cliente tipo almacén «MANIMALS» en octubre de 2026; confirmar si es la misma clínica.
2. **BL-010:** verificar los lotes 1 y 2 de abajo (20 prospectos de encaje Alto) con la mini auditoría de AGENTS.md §5.
3. **BL-012:** con los verificados, proponer a Andrés 10 tiendas `listo_para_contactar` con su borrador (variantes A/B). Antes, BL-005 debe definir precio a distribuidor y pedido mínimo, y BL-044 la ficha del experimento.

## Candidatos para el próximo lote

Propuesta (H) para empezar por las microzonas candidatas. Cada lote tiene 10 prospectos de una misma zona, como pide AGENTS.md §4.

| Lote | Zona | Por qué | Prospectos |
|---|---|---|---|
| 1 | Suba, alrededor de Manimal (calles 127–153) | Microzona noroccidente; la de más prospectos | P032, P096, P091, P076, P107, P015, P090, P053, P020, P005 |
| 2 | Usaquén / Cedritos (calles 134–165) | Vecina de la microzona noroccidente; segunda en densidad | P113, P097, P100, P025, P110, P067, P068, P051, P044, P108 |
| 3 | Bosa y Kennedy, alrededor de Sankatin | Microzona sur | P070, P052, P011, P035, P034, P071, P026, P062, P040, P046 |

**Aparte, para que decida Andrés:**
- **Cadenas** (otro decisor y otro ciclo de venta): P003 Agrocampo, P019 CEBA, P059 Laika, P072 Movet, P083 Pet Gourmet.
- **Tiendas de gatos** (reservadas para BL-026): P022 Cat Mania, P023 Catfood Colombia, P024 Catkitten, P043 Felicette.

## Alertas de calidad

Resuélvelas al verificar el prospecto (o antes, si entra en tu lote):

| Alerta | Filas | Qué hacer |
|---|---|---|
| Mismo teléfono en dos negocios | P008 Animal Time y P015 Baratupet (315 916 1727) | Confirmar si es el mismo negocio, una cadena o un error |
| Mismo teléfono en dos negocios | P053 Huellitas Petshop y Spa y P107 Waggers (320 840 2485) | Igual que arriba |
| Mismo teléfono en dos negocios | P089 Pet Spot y P100 R&M Veterinaria (310 322 5955) | Igual que arriba |
| Teléfono con 9 dígitos (formato inválido) | P110 Wow Pet (319 544 452) | Buscar el número correcto en una fuente del negocio |
| Dirección residencial | P023 Catfood Colombia | La fuente indicaba un apartamento; se retiró la dirección (AGENTS.md §10) |
| Fuente secundaria | 9 filas con fuente `exa.ai` | Es un índice de búsqueda: confirmar en Maps o en la web del negocio |

## Red actual publicada (BL-035)

Distribuidores que publica el sitio de Canívoros (`../CANIVOROS-REFERENCIA-EMPRESA.md`). Sirven para deduplicar y para BL-035. Los de fuera de Bogotá no son prospectos de esta carpeta.

| Aliado | Ciudad / zona | Dirección comercial | Teléfono publicado | En el registro | Estado |
|---|---|---|---|---|---|
| Clínica Veterinaria Manimal | Bogotá, noroccidente | Calle 134d #45a-08 | 601 274 4806 | P001 | por_verificar |
| Sankatin PetShop | Bogotá, Bosa (José Antonio Galán) | Carrera 78f #58m-11 Sur | 304 272 1381 | P002 | por_verificar |
| Malcriados PetShop | Chía | Carrera 15a #12-08 | 302 570 2926 | — | por_verificar |
| Clínica Veterinaria Terranova | Sopó | Calle 1 #3-57 | 302 304 4015 | — | por_verificar |
| Pets & Company | Zipaquirá | Carrera 22 #7d-91 | 319 498 3473 | — | por_verificar |
| Club Canes Centro de Entrenamiento Canino | Villavicencio, Meta | Carrera 33a #15-105 | 313 885 6095 | — | por_verificar |

## Métricas BL-012 (las registra el equipo comercial)

| Métrica | Valor |
|---|---|
| Prospectos verificados | 0 |
| Listos para contactar | 0 |
| Contactados | 0 |
| Respondieron | desconocido |
| Muestra entregada | desconocido |
| Pedido inicial | desconocido |
| Reposición | desconocido |
| Ingreso COP de pedidos B2B (precio confirmado sí/no) | desconocido |
| Motivos de no compra | desconocido |

## Fichas verificadas

_Aún no hay fichas. Usa el formato de AGENTS.md §9._

## Registro

| ID | Nombre | Tipo | Zona | Dirección | Web / Instagram | Teléfono público | Marcas (según fuente) | Encaje | Estado | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| P001 | Clínica Veterinaria Manimal | Veterinaria con tienda | Noroccidente | Calle 134d #45a-08 | desconocido | 601 274 4806 | Canívoros (aliado actual) | Existente | por_verificar | CANIVOROS-REFERENCIA-EMPRESA.md |
| P002 | Sankatin PetShop | Pet shop | Bosa | Carrera 78f #58m-11 Sur (José Antonio Galán) | desconocido | 304 272 1381 | Canívoros (aliado actual) | Existente | por_verificar | CANIVOROS-REFERENCIA-EMPRESA.md |
| P003 | Agrocampo | Cadena agro/veterinaria y mascotas | Chapinero (Cl. 73) | Cl. 73 #20-62 | https://www.agrocampo.com.co/ · @agrocampoco | 601 326 5999 | Pixie, Peluditos BARF + concentrados | Alto | por_verificar | https://pixie.net.co/contacto ; https://peluditosbarf.com.co/distribuidores/ ; https://www.agrocampo.com.co/ |
| P004 | Aldan Pets | Pet shop | Antonio Nariño | Cl. 2 Bis #16-18 | desconocido | 300 207 5607 / 300 590 4895 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P005 | Animal Love | Pet shop | Suba | Cl. 146F #76-06 | desconocido | 320 263 4133 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P006 | Animal Pride | Pet shop | Teusaquillo/Galerías | Cra. 17 #50-69 | desconocido | 312 407 1561 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P007 | Animal TOP | Pet shop/veterinaria | Engativá | Cl. 86 #95d-26 L2 | desconocido | 320 452 0844 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P008 | Animal Time | Pet shop | Engativá (aprox.) | Cra. 70 #64i-23 | desconocido | 315 916 1727 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P009 | Animaladas Balú | Pet shop | Kennedy/Puente Aranda (aprox.) | Cra. 70b #3a-5 | desconocido | 300 482 8689 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P010 | Animales con Estilo | Pet shop | Fontibón | Cl. 16F #100-21 | desconocido | 300 450 9183 / 311 875 1500 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P011 | Animalia Spa y Tienda de Mascotas | Pet shop + spa | Kennedy | Cra. 77v #48a-38 Sur | desconocido | 317 619 7529 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P012 | Animals (Cl. 73) | Pet shop | Chapinero | Cl. 73 #20-65 | desconocido | 316 467 9013 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P013 | Animals Express | Pet shop | Suba (Cl. 170) | Cra. 55 #170a-35 L2 | desconocido | 302 220 2270 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P014 | Animarket Salitre | Pet shop | Fontibón/Salitre | Cra. 68d #23-32 L5 | desconocido | 301 771 5351 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P015 | Baratupet | Pet shop | Suba | Cra. 59 #130-57 | desconocido | 315 916 1727 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P016 | Barf Colombia (punto de venta) | Tienda BARF | Engativá (aprox.) | Cl. 63 #70D-42 | desconocido | 601 430 5510 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P017 | Barry Collie | Pet shop | Engativá (Pepe Sierra/Cl. 116) | Av. Pepe Sierra #71b-9 | desconocido | 315 229 8763 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P018 | Big Pet Co | Pet shop | Engativá (aprox.) | Cra. 72j #46-22 | desconocido | 310 781 7075 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P019 | CEBA Mascotas (cadena) | Cadena pet shop + veterinaria | Múltiples sedes (Cedritos, Usaquén, Santa Bárbara, Colina, Suba, Niza, 170, 72, Galerías, Modelia, Fontibón, Kennedy, Santa Isabel, Diver Plaza) | Ej. Cedritos: Cra 19 #147-60 L15 | https://ceba.com.co/ | Cedritos 317 879 5710; Usaquén 318 417 3024; Colina 318 413 5215 (ver fuente para resto) | Pixie (horneado) en sedes Bogotá | Alto | por_verificar | https://pixie.net.co/contacto ; https://ceba.com.co/pages/ubicanos-1 ; https://ceba.com.co/pages/tyc |
| P020 | Capivet | Veterinaria con tienda | Suba | Cl. 153 #59-15 | desconocido | 310 563 9245 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P021 | Castell Pet Centro Veterinario | Veterinaria con tienda | Teusaquillo | Cra. 21 #53d-52 | desconocido | 601 347 0717 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P022 | Cat Mania | Pet shop (gatos) | Usaquén | Cra. 12 #118-45 | desconocido | 320 899 2536 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P023 | Catfood Colombia - Pet Shop | Tienda online/pet shop (gatos) | Usaquén | desconocido (dirección residencial retirada) | https://www.catfood.com.co/ | +57 317 725 9412 | Alimento de gato de difícil consecución/premium (reseñas) | Alto | por_verificar | https://exa.ai/library/places?q=da454bbc1e1741a3 ; Resultados WebSearch (índice Exa Places / Google Maps) 2026-10-25 |
| P024 | Catkitten | Pet shop (gatos) | Usaquén (Cedritos) | Cl. 140 #16A-59 | desconocido | 305 750 9363 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto ; https://www.voofla.com/CO/Bogot%C3%A1/1073718719437329/Catkitten. |
| P025 | Charming Pets & Co | Pet shop + grooming | Usaquén | CC Show Place, Cl. 147 #7-52 sótano local 10 | https://www.charmingpetsco.com/ · @charmingpetsco | 301 488 7004 / 317 290 5086 | Pixie, Peluditos BARF | Alto | por_verificar | https://pixie.net.co/contacto ; https://peluditosbarf.com.co/distribuidores/ ; https://www.charmingpetsco.com/contacto |
| P026 | Chonino | Pet shop/veterinaria | Kennedy (Tintal) | Cra. 90C #6A-67 | desconocido | 312 300 1588 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P027 | Clínica Veterinaria El Club de las Mascotas | Veterinaria con tienda | Puente Aranda (aprox.) | Av. Cl. 3 #26a-32 | desconocido | 316 430 2892 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P028 | Clínica Veterinaria Mr. Doggy | Veterinaria con tienda | Engativá | Cl. 71 Bis #86a-59 | desconocido | 305 817 0683 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P029 | Clínica Veterinaria Zoomascotas Veraguas | Veterinaria con tienda | Puente Aranda | Cra. 34 #3-27 | desconocido | 313 351 1131 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P030 | Clínica Veterinaria de Bogotá | Pet shop/veterinaria | Suba | Av. Cl. 116 #71-30 | desconocido | 601 253 2851 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P031 | Comando Mascotas | Pet shop | Fontibón | Av. La Esperanza #68C-25 | desconocido | 300 238 9309 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P032 | Connie Pet Shop | Pet shop/veterinaria | Suba | Cra. 52A #134A-35 | desconocido | 322 367 7205 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P033 | Consulpet | Veterinaria/pet shop | Kennedy/Fontibón (Av. Boyacá) | Av. Boyacá #12b-18 L2-99 | desconocido | 302 682 7474 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P034 | Coraje Doggy Shop | Pet shop | Kennedy | Cra. 73 #39-29 Sur | desconocido | 312 424 3621 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P035 | DK Dunkans | Pet shop | Kennedy | Cl. 51a Sur #80-23 | desconocido | 310 777 6927 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P036 | Doggy y Lobby | Pet shop | Chapinero (Chicó) | Cl. 95 #11a-46 | desconocido | 313 631 2149 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P037 | Doggy's Service Group | Pet shop/veterinaria | Suba | Cl. 174 #52A-14 | desconocido | 324 206 9961 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P038 | Dogin Pet Shop | Pet shop | Usaquén | Cl. 165 #13c-33 | desconocido | 319 739 2993 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P039 | Dogkat | Pet shop | Suba (Mirandela) | Cra. 54d #187-10 | desconocido | 316 693 4890 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P040 | Drako Pet Shop | Pet shop | Kennedy | Cra. 78 #8B-28 | desconocido | 320 273 5353 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P041 | EKÜ - Alimento Natural para Mascotas | Tienda de alimento natural | Suba (aprox.) | desconocido | desconocido | desconocido | desconocido | Alto | por_verificar | https://exa.ai/library/places?q=da454bbc1e1741a3 |
| P042 | Felican Mascotas Saludables | Pet shop natural | Engativá (aprox.) | Cra. 69 #63A-20 | desconocido | 311 555 0966 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P043 | Felicette | Pet shop (gatos) | Teusaquillo | Av. Cl. 24 #40-88 | desconocido | 321 233 0556 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P044 | Friendly Eco Pet | Pet shop eco | Usaquén | Av. Cra. 19 #154-26 | desconocido | 321 434 0977 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P045 | Full Mascotas | Pet shop | Antonio Nariño | Dg. 4A #18C-07 | desconocido | 310 219 3394 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P046 | Gaia Clínica Veterinaria | Pet shop/veterinaria | Kennedy | Cl. 8A Bis #79-79 | desconocido | 319 658 6331 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P047 | Garfields Acuariam | Pet shop | Usaquén | Cl. 189 #8-73 | desconocido | 310 882 6453 / 314 462 1639 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P048 | Gogo Pets | Pet shop | Fontibón/Salitre | CC Ciprés Plaza, Ak. 50 #22-41 L117 | desconocido | 316 057 3386 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P049 | Guardianes | Pet shop | Puente Aranda | Cra. 47 #22-35 | desconocido | 313 877 2209 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P050 | Gupet | Pet shop | Engativá | Cra. 69h #64-27 | desconocido | 317 373 4521 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P051 | Hairy Pets | Pet shop | Usaquén (Barrancas) | Cl. 156 #8-82 | desconocido | 313 680 4620 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P052 | Hu Mascotas | Pet shop | Bosa/Kennedy | Tv. 78d #71c Sur-16 | desconocido | 314 560 3380 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P053 | Huellitas Petshop y Spa | Pet shop + spa | Suba | Cl. 149 #54a-64 | desconocido | 320 840 2485 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P054 | Il Mio Pet | Tienda online/pet pharma | Bogotá / Tenjo | Tv. 19a #97-59 (Tenjo, según Vital Doggy) | https://ilmiopet.com/ | 310 554 0502 | Alimentos especializados; Vital Doggy BARF | Alto | por_verificar | https://ilmiopet.com/ ; https://vitaldoggy.co/distribuidores/ |
| P055 | Kastel Pets | Pet shop | Chapinero | Cl. 90 #13a-43 | desconocido | 320 963 7379 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P056 | Kibou Pets | Pet shop | Suba | Cl. 160 #63-16 | desconocido | 320 419 6379 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P057 | Kumpet | Pet shop | Chapinero (Chicó) | Cra. 15 #94-38 | desconocido | 311 507 9459 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P058 | La Tienda de Zoe | Pet shop | Usaquén | Cra. 8 #108A-70 | desconocido | 312 328 9302 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P059 | Laika Mascotas | Cadena + app de domicilios | Varias (Pepe Sierra, Cedritos, La Felicidad, Engativá) | Cl. 116 #18B-43; Cra. 19 #139-91; Cra. 78 #17-55 CC Meridiano 13 | https://laika.com.co/ | 300 910 8496 / 314 460 4885 | Pixie, Peluditos BARF + premium | Alto | por_verificar | https://pixie.net.co/contacto ; https://peluditosbarf.com.co/distribuidores/ ; https://laika.com.co/frequent_questions_laika_member/bog ; https://www.linkedin.com/posts/mar%C3%ADa-alejandra-mujica-trespalacios-427b48191_laika-proveedores2027-convocatoriaproveedores-activity-7505358511162286080-qk5Y |
| P060 | Likipets | Pet shop | Teusaquillo | Cl. 52 #25-56 | desconocido | 310 454 0627 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P061 | Loporti | Pet shop | Suba/Barrios Unidos | Cl. 97 #60c-8 | desconocido | 304 215 7180 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P062 | Lupaki Pet Shop | Pet shop | Kennedy | Cra. 82A #8C-09 | desconocido | 320 940 5835 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P063 | Malcria / Malcriado2 | Pet shop | Engativá | Cl. 86 #103c-49 / Dg. 81 #76A-15 | desconocido | 315 834 4102 / 315 834 4101 | Pixie, Vital Doggy BARF | Alto | por_verificar | https://pixie.net.co/contacto ; https://vitaldoggy.co/distribuidores/ |
| P064 | Mapache Azul | Pet shop/veterinaria | Barrios Unidos/Teusaquillo | Cl. 57 #57-28 L8A | desconocido | 321 210 5651 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P065 | Mascohogar Clínica Veterinaria | Pet shop/veterinaria | Suba | Dg. 147 #141A-42 | desconocido | 320 860 2075 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P066 | Mascotizados | Pet shop | Suba | Cl. 128F #104B-09 | desconocido | 302 397 5506 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P067 | Max Puppys | Pet shop | Usaquén | Cl. 151 #13A-33 LC 14 | desconocido | 313 775 5420 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P068 | Medical Vet | Pet shop/veterinaria | Usaquén | Cra. 7A #151-80 | desconocido | 322 855 4867 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P069 | Merquepets (Villa del Prado / Barrancas) | Pet shop (2 sedes) | Suba / Usaquén | Cl. 174a #54b-55; Cl. 163a #9-07 | desconocido | 323 244 7968 / 311 226 3509 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P070 | Mis Gordogs | Pet shop | Bosa | Cl. 65I Sur #80G-08 | desconocido | 305 897 7718 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P071 | Morris Natural Food for Dogs and Cats | Tienda de alimento natural | Kennedy | Cra. 72m #38F-06 Sur | desconocido | desconocido | desconocido | Alto | por_verificar | https://exa.ai/library/places?q=da454bbc1e1741a3 |
| P072 | Movet (red veterinaria) | Red de clínicas veterinarias con tienda | Chapinero, Castilla, Cedritos, Colina (24/7) | Cra. 7 #59-54; Cra. 72 #7c-77; Cra. 58 #136-08 | https://www.movet.co/ | 601 580 0111 / 601 648 2542 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto ; https://movet.co/clinicas/clinica-veterinaria-colina |
| P073 | Mundo Mascotas (Tabora) | Pet shop | Engativá | Cl. 72 #77a-20 | desconocido | 310 220 4677 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P074 | Mundo Mascotas Col | Pet shop | Fontibón/Salitre | Cra. 69 #25-67 | @Mundomascotas_col | 313 411 1192 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P075 | Nala Tienda y Peluquería | Pet shop + peluquería | Suba | Cl. 187 #49-64 L1-01 | desconocido | 321 442 8588 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P076 | Natural Foodie | Tienda de alimento natural/BARF | Suba (Prado Norte) | Cl. 129 #50A-40 piso 3 | https://naturalfoodie.com.co/ · @natural_foodie_ | 313 390 5998 | BARF, snacks deshidratados (alimentación natural) | Alto | por_verificar | https://naturalfoodie.com.co/ ; https://www.rappi.com.co/tiendas/900376509-naturalfoodiesas-mt-enc |
| P077 | Natural Pet's Lover | Pet shop natural | Engativá (Minuto de Dios) | Tv. 76 #81G-04 | desconocido | 350 576 5013 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P078 | Oh My Doggie | Pet shop | Suba (Puente Largo) | Cl. 106 #54-93 L3 | desconocido | 320 853 5040 | Pixie, Acana, Orijen (Rappi) | Alto | por_verificar | https://pixie.net.co/contacto ; https://www.rappi.com.co/tiendas/900431881-ohmydoggie-mt-enc |
| P079 | Okpet | Pet shop | Puente Aranda | Ac. 3 #39-16 | desconocido | 317 509 9222 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P080 | Pacca y Juana | Pet shop | Usaquén (Cl. 180) | Cra. 7 #180-75 LC10 | desconocido | 316 877 2658 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P081 | Pawpatropolis / La Placita de Mi Gran Amigo | Pet shop | Barrios Unidos (aprox.) | Cl. 66 #57b-4 / Cl. 66 #57-52 | desconocido | 319 582 9077 | Pixie, Peluditos BARF | Alto | por_verificar | https://pixie.net.co/contacto ; https://peluditosbarf.com.co/distribuidores/ |
| P082 | Pet Depot | Pet shop | Suba (Av. Boyacá 152) | Av. Boyacá #152-127 LC110 | desconocido | 300 209 1343 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P083 | Pet Gourmet (cadena) | Cadena pet shop premium | Suba, 106, Salitre, Virrey, Colina | Av. 15 #105A-12 (106); CC Plaza Imperial L2-09; CC Salitre Plaza L1-69; Av. 15 #88-83; Av. Las Villas #132-17 | https://petgourmet.com.co/ · @petgourmet | 601 761 6431 / 313 864 4612 / 305 769 9596 | Pixie + premium | Alto | por_verificar | https://pixie.net.co/contacto ; https://petgourmet.com.co/tiendas-pet-gourmet/ |
| P084 | Pet Partners Petshop | Pet shop | Teusaquillo/Salitre | Ac. 24 #58-23 L18 | desconocido | 321 467 8951 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto ; Resultados WebSearch (índice Exa Places / Google Maps) 2026-10-25 |
| P085 | Pet Shop Amigos Peludos | Pet shop | Barrios Unidos | Cl. 60 #57-34 | desconocido | 320 239 3384 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P086 | Pet Shop Bigotes | Pet shop | Engativá | Dg. 78c #108-09 | desconocido | 313 555 9044 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P087 | Pet Shop Luki | Pet shop | Los Mártires/Santa Isabel | Cl. 3 #20A-75 | desconocido | 310 642 0915 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P088 | Pet Shop San Pablo / San Angel | Pet shop | Puente Aranda/Teusaquillo | Cra. 44a #22B-30 | desconocido | 314 646 9219 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P089 | Pet Spot | Pet shop | Usaquén/Chicó | Cl. 103 #14a-10 | desconocido | 310 322 5955 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P090 | Petgold | Pet shop | Suba (Cl. 150) | Cl. 150 #45-35 | desconocido | 316 617 3994 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P091 | Pethill Spa | Pet shop + spa | Suba (Colina) | Cra. 58 #137a L-2 | desconocido | 312 730 6418 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P092 | Pets and Roll | Pet shop/veterinaria | Engativá | Cl. 78 #110C-03 | desconocido | 311 220 3513 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P093 | Petville | Pet shop | Suba/Barrios Unidos | Cl. 98 #62-11 | desconocido | 324 436 6862 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P094 | Plaza Pets | Pet shop | Suba | Cl. 167a #55a-60 L4 | desconocido | 321 429 2593 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P095 | Polovet | Veterinaria con tienda | Barrios Unidos (Polo) | Cra. 24 #85-34 | desconocido | 320 310 3815 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P096 | Potencia Animal | Pet shop | Suba | Cl. 137 #50-64 | desconocido | 310 777 6189 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P097 | Puppis | Pet shop | Usaquén (Cedritos) | Cl. 140 #9-70 L2 | desconocido | 322 461 5562 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P098 | Pupspot | Pet shop | Puente Aranda/Salitre | Cra. 60 #24-09 L-101 | desconocido | 302 839 8208 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P099 | Que Dice Mi Perro | Pet shop | Usaquén | Cra. 7a #130b-23 | desconocido | 318 788 7268 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P100 | R&M Veterinaria | Veterinaria con tienda | Usaquén (Belmira) | Av. Cra. 7 #140-71 | desconocido | 301 473 9866 / 310 322 5955 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P101 | Razas Pet Shop | Pet shop | Usaquén | Cl. 161 #15-6 | desconocido | 312 408 7887 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P102 | Sintiendo Huellas | Pet shop | Chapinero | Cra. 13a #78-17 Int 3 | desconocido | 313 423 9387 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P103 | Supermarpet / Supermar Pet | Pet shop | Suba (Cl. 116) | Cl. 116 #47A-17 | desconocido | 314 367 3438 / 305 417 9557 | Pixie (horneado), Peluditos BARF | Alto | por_verificar | https://pixie.net.co/contacto ; https://peluditosbarf.com.co/distribuidores/ |
| P104 | The Pet House Spa | Pet shop + spa | Suba | Cl. 98b #70-91 L22 | https://thepethouseco.com/ | 319 509 0954 | Pixie, Kanuto (horneado) | Alto | por_verificar | https://pixie.net.co/contacto ; https://thepethouseco.com/collections/alimentos-perros |
| P105 | Veterinarias Golden | Pet shop | Fontibón | Cl. 19 #103-19 | desconocido | 322 462 5556 | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P106 | Vetnutrition Clínica Veterinaria | Veterinaria (nutrición) | Kennedy | Cl. 8 Sur #69c-03 | desconocido | 310 513 8575 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P107 | Waggers | Pet shop | Suba | Cl. 127b Bis #50A-32 | desconocido | 320 840 2485 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P108 | Wanco | Pet shop | Usaquén | Cra. 17 #146 | desconocido | 315 047 3721 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P109 | Woof (Suba) | Pet shop/veterinaria | Suba | Cra. 139 #132-11 | desconocido | 301 229 7885 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P110 | Wow Pet | Pet shop | Usaquén | Cra. 14 #147-05 L06 | desconocido | 319 544 452 (incompleto en fuente) | Vital Doggy BARF | Alto | por_verificar | https://vitaldoggy.co/distribuidores/ |
| P111 | Yoko Store | Pet shop/veterinaria | Suba | Cra. 109 #152A-39 | desconocido | 311 875 0153 | Peluditos BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ |
| P112 | Zeus Pet Shop | Pet shop | Fontibón (aprox.) | Cra. 82 #22D-04 / #22d-38 | desconocido | 300 278 6000 / 311 282 7177 | Pixie, Peluditos BARF | Alto | por_verificar | https://pixie.net.co/contacto ; https://peluditosbarf.com.co/distribuidores/ |
| P113 | Zooluciones | Pet shop | Usaquén | Cra. 19A #134-35 | desconocido | 313 209 7766 | Pixie | Alto | por_verificar | https://pixie.net.co/contacto |
| P114 | Zoopets | Pet shop con alimento natural/BARF | Engativá | Ak 86 #82a-03 / Dg 83a #87a-15 / Cl. 82A Bis #86-49 | desconocido | 321 442 7850 | Peluditos BARF; alimento natural/BARF | Alto | por_verificar | https://peluditosbarf.com.co/distribuidores/ ; https://www.rappi.com.co/tiendas/900442442-zoopets-mt-enc |
| P115 | AgeveT | Distribuidor veterinario mayorista | Engativá (Parque Ind. El Dorado) | Tv. 93 #53-48 Bodega 53 | https://www.agevet.co/ | 300 313 3217 | desconocido | Medio | por_verificar | https://www.agevet.co/ |
| P116 | Animal Center (cadena) | Cadena veterinaria + pet shop | Usaquén, Chapinero, Teusaquillo | Pepe Sierra Av Cra 19 #114a-26; Rosales Cl. 68 #4A-14; Santa Bárbara Cra 19a #125-54; Galerías Cra 24 #45c-21; Cedritos Cl. 140 #13-27; Bella Suiza Ak 9 #127-82 | https://www.animalcenter.pet/ | PBX 601 756 9923; WhatsApp 350 540 6474 / 314 475 9783 / 317 866 1212 | desconocido | Medio | por_verificar | https://www.animalcenter.pet/nuestras-sedes/ |
| P117 | Animal Home (Vibe Andina SAS) | Distribuidor mayorista | Kennedy (Corabastos) | Cra. 80 #2-51 Corabastos Bodega 16 L3-4 | https://animalhome.co/ | WhatsApp 311 876 7205 | +2.000 productos marcas comerciales | Medio | por_verificar | https://animalhome.co/ |
| P118 | Barket Flagship & Café | Pet store + café | Chapinero | Cra. 14 #90-16 | https://barketstore.com/ | 315 637 5441 | desconocido | Medio | por_verificar | https://exa.ai/library/places?q=f62bc2c237340c85 |
| P119 | Cerati Pet Shop | Pet shop con domicilio | Suba | Cra. 128b #142D-95 | https://www.ceratipet.com/ | desconocido | desconocido | Medio | por_verificar | https://www.ceratipet.com/ |
| P120 | Colombiana de Mascotas | Pet shop | Usaquén | Cl. 151 #13a-17 | desconocido | desconocido | desconocido | Medio | por_verificar | https://exa.ai/library/places?q=f62bc2c237340c85 |
| P121 | De Pelos | Tienda online + servicios | Bogotá | desconocido | https://www.depelos.co/ | desconocido | Taste of the Wild, Acana, Orijen | Medio | por_verificar | https://www.depelos.co/comida-para-perros |
| P122 | Didopet Calle 121 | Veterinaria + pet shop | Usaquén | Ak 9 #121-76 | https://didopet.com/ | 601 917 2122 | desconocido | Medio | por_verificar | https://exa.ai/library/places?q=f62bc2c237340c85 |
| P123 | Kanu Pet (Bogotá) | Cadena pet shop | Chapinero (La Cabrera), Usaquén (Santa Bárbara) | Cra. 11 #84A-12; Cl. 122 #18B-08 | https://kanu.pet/ | 316 188 9545 / 315 467 7027 | desconocido | Medio | por_verificar | https://kanu.pet/pages/tiendas-kanu-perimetro |
| P124 | MascotaMarket | Tienda online | Bogotá | desconocido | https://mascotamarket.com/ | desconocido | Taste of the Wild, Acana, Orijen | Medio | por_verificar | https://mascotamarket.com/ |
| P125 | Petit Bakery | Panadería/snacks naturales para mascotas | Bogotá | desconocido | desconocido | desconocido | Deshidratados, galletas, tortas, snacks propios | Medio | por_verificar | https://exa.ai/library/places?q=da454bbc1e1741a3 |
| P126 | Servicampo (Corabastos) | Distribuidor/almacén agro | Kennedy (Corabastos) | Corabastos Bodega E Local 2 | desconocido | 310 594 3376 | Pixie | Medio | por_verificar | https://pixie.net.co/contacto |
| P127 | Shaly.co | Tienda online boutique | Bogotá (Normandía) | Cl. 49a #70d-26 | https://shaly.co/ | WhatsApp 319 343 4211 / 301 380 3870 | Nupec, Hill's, Pro Plan, Taste of the Wild, Diamond, Royal Canin | Medio | por_verificar | https://shaly.co/ |
| P128 | Silveragro Autopista Norte | Almacén agro/mascotas | Usaquén | Autopista Norte #145-34 | desconocido | 601 861 1061 | Pixie | Medio | por_verificar | https://pixie.net.co/contacto |
| P129 | Tekoa Pet Store | Pet shop | Usaquén (Autopista Norte) | Autopista Norte 145A-44 | https://www.tekoa.com.co/ · @tekoapetstore | 320 348 1325 / 314 470 1624 | desconocido | Medio | por_verificar | https://www.tekoa.com.co/ |
| P130 | TrayGo | Tienda online | Bogotá | desconocido | https://www.traygo.com.co/ | desconocido | Taste of the Wild | Medio | por_verificar | https://www.traygo.com.co/ |
| P131 | Woof Exclusive | Pet shop premium | Usaquén | Ak 9 #107A-35 | desconocido | 315 516 2308 | desconocido | Medio | por_verificar | https://exa.ai/library/place/4x703bmn6y5 |
| P132 | 4GR S.A.S. | Distribuidor mayorista | Susa, Cundinamarca (despacha Cundinamarca) | Km 1 vía Susa–Chiquinquirá | https://www.4grmascotas.com/ | 320 263 5300 | Italcol, Raza, Nutrion, Don Bigotes, Hacienda | Bajo | por_verificar | https://www.4grmascotas.com/ |
| P133 | Megapets Mayorista | Distribuidor mayorista | Kennedy (Corabastos) | Corabastos Bodega 1 Local 8 | https://megapetsmayorista.com.co/ | desconocido | desconocido | Bajo | por_verificar | https://megapetsmayorista.com.co/ |
| P134 | Petline | Tienda online | Bogotá | desconocido | https://petline.com.co/ | desconocido | Pro Plan, Dog Chow, Felix, Fancy Feast; snacks naturales | Bajo | por_verificar | https://petline.com.co/ |
| P135 | Trompas Pet Shop | Pet shop online | Chapinero | Cra. 14 #98-73 Of 403 | https://trompaspetshop.com/ | 304 375 2720 | desconocido | Bajo | por_verificar | https://exa.ai/library/places?q=f62bc2c237340c85 |

## Historial de lotes

### Revisión 2026-11-02 · calidad del registro (sin verificación web)
- Se agregaron el resumen por localidad, los candidatos para los lotes 1 a 3, las alertas de calidad y la red actual publicada.
- P001 y P002: dirección y teléfono tomados de `../CANIVOROS-REFERENCIA-EMPRESA.md` (lo publica la marca; siguen `por_verificar`).
- P023: se retiró la dirección porque correspondía a un apartamento.
- La columna «Marcas observadas» pasa a llamarse «Marcas (según fuente)»: en la lista inicial son declaraciones de los directorios de las marcas.
- Ninguna fila cambió de encaje ni de estado. Nadie fue contactado.

### Siembra 2026-11-02 · lista inicial
- Origen: `prospectos_bogota.csv` (135 filas), generado con ayuda de IA a partir de directorios públicos de distribuidores (Pixie, Peluditos BARF, Vital Doggy y otros) y búsquedas.
- Sin verificación individual. Campos faltantes marcados `desconocido`.
- Limitaciones: el encaje se infiere de directorios de marcas; puede estar desactualizado.
