# Prospectos Canívoros · Bogotá y Sabana · 2026-11-03

Archivo único de prospectos, según `prospectos/AGENTS.md`. Une el registro y los 5 lotes del 2026-11-03. La tabla del registro también está en `prospectos-2026-11-03.csv` (mismo nombre): se genera con `registro.py csv` y no se edita a mano. El historial queda en git.

## Resumen general

- Revisados: 38 negocios en 5 lotes (P001–P038), en Bogotá y la Sabana.
- Resultado: A 7 · B 10 · C 17 · descartados 4.
- Los mejores: Pet Gold (vende Pixie horneado congelado y tiene stock) · Puppis, Laika y Agrocampo (cadenas que venden Pixie) · Mundo Mascota (Pixie en catálogo, 4 sedes) · Animal Center (5 sedes con tienda y consulta) · Criadero Arkahnius (pastor alemán con guardería).
- Debe decidir Andrés: si P001 es cliente actual; a quién se atribuye Pet Gold, que queda cerca de Manimal; si se aborda ya a cadenas y criaderos grandes (la capacidad de producción es `desconocido`, BL-036); y aprobar los 17 borradores.
- Pendiente: la lista de 134 prospectos de BL-010 (`prospectos_bogota.xlsx`) no está en el repositorio y no se cruzó.

| Lote | Tipo y zona | IDs | A | B | C | Descartados |
|---|---|---|---|---|---|---|
| 1 | Tiendas y veterinarias · Usaquén | P001–P009 | 1 | 2 | 5 | 1 |
| 2 | Tiendas y veterinarias · Suba | P010–P015 | 2 | 1 | 3 | 0 |
| 3 | Chapinero y cadenas que venden Pixie | P016–P021 | 3 | 1 | 2 | 0 |
| 4 | Criaderos · Bogotá y Sabana | P022–P031 | 1 | 1 | 5 | 3 |
| 5 | Guarderías, colegios y hoteles · norte de Bogotá y Sabana | P032–P038 | 0 | 5 | 2 | 0 |

## Cómo se verificó

- El 2026-11-03, la red de la sesión de trabajo bloqueó la lectura directa de sitios web, Google Maps e Instagram. Todo se revisó con resultados de búsqueda (WebSearch).
- Por eso no se vieron reseñas recientes en Maps ni fotos de estantería o congeladores.
- **Verificado** aquí significa: dos fuentes independientes coinciden en nombre y zona, y una es el sitio propio activo o una fuente fechada en 2025–2026.
- Una sola fuente, o fuentes viejas → `no verificado` y nivel C.
- **Antes de enviar cualquier borrador, una persona debe abrir la ficha de Maps** y confirmar que el negocio sigue abierto.

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
| P001 | [retirado: posible cliente actual] | veterinaria | Usaquén | retirado | retirado | retirado | — | descartado: posible cliente actual (coincide con el Excel de ventas); confirmar con Andrés | retirado | 2026-11-03 | Sin datos para no exponer a un cliente. Andrés confirma si es cliente; si no lo es, se vuelve a registrar con un ID nuevo |
| P002 | Animal Center | tienda | Usaquén (sede Cedritos, Cl. 140 # 13-27) | animalcenter.pet · facebook.com/AnimalCenterCol | WhatsApp 317 866 1212 (V, directorios) | Pet shop, farmacia y consulta veterinaria (E); 5 sedes en la web y 6 según guía 2026 (E); marcas naturales desconocido | A | borrador listo | https://www.animalcenter.pet/nuestras-sedes/ · https://colombia.com.co/tiendas-de-mascotas-en-bogota/ · https://co.latinoplaces.com/bogota/animal-center-cedritos-1109025 | 2026-11-03 | A por volumen (H), no por natural. Sedes: Santa Bárbara, Pepe Sierra, Bella Suiza (Usaquén) y Rosales (Chapinero). Una reseña dice que no contestan WhatsApp (V) |
| P003 | Dog Kat | tienda | Usaquén (Cedritos) | dogkat.com.co | WhatsApp 316 693 4890 (E, sitio) | "Hipermercado para mascotas" con domicilios (D); alimento natural desconocido | B | borrador listo | https://dogkat.com.co/ · https://www.civico.com/lugar/mascotas-dog-kat-bogota/ · https://co.latinoplaces.com/bogota/dog-kat-677788 · https://petlist.co/anuncio/dog-kat-tienda-de-mascotas-cedritos/ | 2026-11-03 | Direcciones no coinciden entre fuentes: Cra 19 # 144-09 y Cl. 150 # 18-37 (V) |
| P004 | Clínica Veterinaria Dover | veterinaria | Usaquén (Santa Bárbara, Cl. 126A # 7-98) | dover.com.co | PBX (601) 516 9500 (E) | Urgencias 24 h y Pet Center con venta de productos (V); alimento natural desconocido | B | borrador listo | https://dover.com.co/nuestras-sedes/ · https://es-co.petlist.co/anuncio/clinica-veterinaria-dover-santa-barbara/ · https://bivett.com/sedes/bogota | 2026-11-03 | Sede Chicó (Cl. 97A # 9-82) podría trasladarse a Cl. 116 # 16-08 como Dover-Bivett (V) |
| P005 | Natural Taste | tienda natural | Usaquén (Cedritos, Feria Artesanal de la 140) | desconocido | desconocido | Pastelería canina y felina con comida BARF (V); "solo alimentación natural", abrió en 2015 (V) | C | no verificado | https://todocedritos.com/venta_comida_alimentos_perros_gatos_mascotas_cedritos_bogota_pasteleria_canina_felina_natural_taste.htm · https://www.cursopasteleriacaninayfelina.com/ | 2026-11-03 | Encaje alto si opera: pasaría a A. Falta fuente propia y señal reciente. Puede fabricar su propio BARF: preguntar si revende |
| P006 | Cedritos Pet Shop | tienda | Usaquén (Cedritos, Cra 19A # 150-10) | facebook.com/cedritospetshop1 | 318 337 6730 (V, Facebook) | Venta de alimento y accesorios, domicilio en Cedritos (D); natural desconocido | C | no verificado | https://www.facebook.com/cedritospetshop1/ | 2026-11-03 | Una sola fuente, con una reseña |
| P007 | La Esquina de los Peludos | tienda | Usaquén (Cedritos, Calle 148 # 15-02) | desconocido | WhatsApp 350 540 4364 (V, directorio) | Alimentos y accesorios, domicilio gratis (V); natural desconocido | C | no verificado | https://todocedritos.com/la_esquina_de_los_peludos_pet_shop_almacen_tienda_venta_alimentos_productos_accesorios_mascotas_perros_gatos_barrio_cedritos_norte_bogota.htm | 2026-11-03 | Una sola fuente (directorio de barrio) |
| P008 | Petcol | tienda | Usaquén (Cedritos, Calle 140 # 13-18) | desconocido | desconocido | Pet shop según directorio (V) | C | no verificado | https://www.planetacolombia.com/petcol-F120FC90119D043 | 2026-11-03 | Una sola fuente; el directorio mezcla dos direcciones |
| P009 | Veterinaria Grecia | veterinaria | Usaquén (Santa Bárbara Central, Calle 119 # 11-59) | desconocido | desconocido | Clínica con venta de alimento según directorios (V) | C | no verificado | https://enbogota.com.co/sitios-veterinarias-y-todo-para-mascotas/veterinaria-grecia · https://www.planetacolombia.com/veterinaria-grecia-F1709C70712D0 | 2026-11-03 | Datos de directorios con varios años |
| P010 | Pet Gold | veterinaria | Suba (Cl. 160 # 56-15, Cantagallo) | petgold.com.co · Rappi | 601 916 0700 (V, directorio) | Vende Pixie dieta horneada congelada, con stock en su tienda online (E); veterinaria y tienda en Rappi (E) | A | borrador listo | https://petgold.com.co/productos/pixie-dieta-horneada-carne-de-res-500gr/ · https://www.rappi.com.co/tiendas/900172241-petgold-veterinaria-mt-nc · https://www.planetacolombia.com/pet-gold-F1209C70013D745 · https://co.latinoplaces.com/bogota/pet-gold-1536769 | 2026-11-03 | Otro local en Calle 150 # 45-41 y CEDI en Cra 56A # 159-82 (E, Rappi). Teléfonos distintos entre fuentes. El local de la Calle 150 queda cerca de Manimal (distribuidor): acordar atribución con Andrés |
| P011 | Mundo Mascota Pet Shop | tienda | Suba (sede Las Villas, Calle 128B # 59A-22) | mundomascotapetshop.com · facebook.com/MundoMascotapetshopoficial | desconocido (el sitio publica un teléfono por sede) | Pixie de pescado al horno en su catálogo, sin stock al indexar (E); 4 sedes (E) | A | borrador listo | https://mundomascotapetshop.com/ · https://www.facebook.com/MundoMascotapetshopoficial/ · https://magavet.co/donde-comprar/ | 2026-11-03 | Otras sedes: Tabora y Las Ferias (Av. Calle 72, Engativá), San Miguel (Calle 65 # 50-09). Copiar el teléfono de la sede Las Villas desde el sitio |
| P012 | Puppy Export | tienda | Suba (sede Niza, Calle 128 Bis) | puppyexport.com · facebook.com/PuppyExport | (601) 555 9838 (E, sitio) | Pet shop con baño y domicilios en Bogotá (D); alimento natural desconocido | B | borrador listo | https://puppyexport.com/sedes · https://biolink.info/sedespuppyexport · https://yandex.com/maps/org/puppy_export_tienda_para_mascotas_sede_niza/116294379987/ | 2026-11-03 | La web oficial lista Norte, Centro Mayor, Hayuelos y Quinta Paredes, no Niza (V) |
| P013 | Valenutrirse | tienda | Suba (Calle 161 # 55-21, Local 2) | valenutrirse.com | desconocido | Tienda de alimento con nutricionista y venta mayorista a veterinarias (D) | C | no verificado | https://www.valenutrirse.com/ | 2026-11-03 | Única fuente: su sitio. El celular publicado (310 555 0161) parece ficticio (H). Si existe, sería un canal mayorista interesante |
| P014 | T & T Mascotas | tienda | Suba (Cra 102C # 139-37) | desconocido | desconocido | Comida para todas las razas y snacks (V) | C | no verificado | https://www.cylex.com.co/bogota/suba/tienda+de+productos+para+mascotas.html | 2026-11-03 | El directorio lo marca como cerrado (V); confirmar antes de descartar |
| P015 | Distribuciones J & S | otro | Suba (Cra 90 # 145-27, cerca de Subazar) | desconocido | desconocido | Distribuidor de concentrados con domicilios (V); alimento convencional | C | no verificado | https://www.aiyellow.com/concentradosanimalessuba_nortebogota/ | 2026-11-03 | Poco encaje: vende concentrado |
| P016 | Pet Garden Veterinaria | veterinaria | Chapinero (Galería 93, Cl. 93B # 15-34, Local 107) | petgarden.com.co · facebook.com/Petgardenbogota | 350 837 2309 (E, guía 2026) | Veterinaria, grooming, farmacia y tienda (E); alimento natural desconocido | B | borrador listo | https://petgarden.com.co/ · https://colombia.com.co/tiendas-de-mascotas-en-bogota/ · https://www.informacolombia.com/directorio-empresas/informacion-empresa/cj-pet-garden-veterinaria-sas | 2026-11-03 | El directorio de empresas da otro teléfono: 304 590 0847 |
| P017 | Doglamour Pets | peluquería | Chapinero (Virrey, Cra 15 # 88-26) | doglamour.co · @doglamour.pets | WhatsApp Virrey 324 283 0911 (D) | Boutique y spa; dice vender alimento premium y snacks naturales (D) | C | no verificado | https://doglamour.co/sedes/ · https://doglamour.co/boutique-de-mascotas/ | 2026-11-03 | Una sola fuente (su sitio). Sedes: Virrey y Rosales (Chapinero), Calle 109 (Usaquén). Posible B al verificar |
| P018 | El Paraíso de las Mascotas | tienda | Chapinero (Cra 15 # 93-47) | elparaisodelasmascotas.shop | 320 261 4917 (D) | Tienda con marcas premium convencionales (D); veterinaria y guardería (D) | C | no verificado | https://elparaisodelasmascotas.shop/ | 2026-11-03 | Una sola fuente (su sitio) |
| P019 | Puppis | tienda | Chapinero (sede Chicó, Cra 15 # 94-52) | puppis.com.co · Rappi | desconocido | Vende Pixie dieta horneada congelada (E); 34 tiendas en Colombia (D) | A | borrador listo | https://www.puppis.com.co/nuestras-sucursales · https://www.puppis.com.co/alimento-congelado-para-perro-pixie-dieta-horneada-pollo/p · https://booking.page/en/company/page/puppiscolombia · https://www.rappi.com.co/bogota/tiendas/marca-puppis | 2026-11-03 | Cadena: la compra se decide en oficina central (H). Otras sedes: Galerías (Calle 53 # 16-53), Chapinero (Cra 8 # 63-63), Chicó Navarra (Calle 109 # 17-26) |
| P020 | Laika | tienda online | Usaquén (tienda Pepe Sierra, Calle 116 # 18B-43) | laika.com.co | 300 910 8496 (V, guía 2026) | Vende Pixie dieta horneada (E); más de 4.000 productos con dietas naturales (D); 23 tiendas en Colombia (E, prensa 2026) | A | borrador listo | https://laika.com.co/product_details/bog/pixie-dieta-horneada-carne-de-res/dog · https://www.portafolio.co/negocios/empresas/extender-las-tiendas-fisicas-en-el-pais-los-planes-de-laika-600086 · https://abceconomia.co/2026/10/01/tiendas-fisicas-de-laika-expansion-chile-2026/ | 2026-11-03 | Gran cadena: proceso formal de proveedor (H). Otras tiendas: Cedritos (Cra 19 # 139-91), La Felicidad, Calle 94 |
| P021 | Agrocampo | tienda | Barrios Unidos (Av. Caracas # 73-39) | agrocampo.com.co | (601) 326 5999 (V, directorio) | Vende Pixie (E); hipermercado agro y mascotas con domicilio en Bogotá (E) | A | borrador listo | https://www.agrocampo.com.co/perros/comida/pixie · https://www.agrocampo.com.co/ · https://firmania.com.co/bogota/agrocampo-30168 · https://colombia.com.co/tiendas-de-mascotas-en-bogota/ | 2026-11-03 | Gran superficie: proceso formal de proveedor (H) |
| P022 | Criadero Arkahnius | criadero | Suba rural (Guaymaral) | criaderopastoralemanbogota.com · tuperroconpedigree.com · hotelguarderiacaninabogota.com | 310 480 1374 (V, los teléfonos cambian entre sus páginas) | Pastor alemán con registro APPA (D); también opera guardería "Arkahnius Dog Club" (D) | A | borrador listo | https://www.criaderopastoralemanbogota.com/ · https://tuperroconpedigree.com/venta-pastor-aleman-arkahnius/ · https://www.hotelguarderiacaninabogota.com/ · https://www.nexdu.com/co/bogota-dc-dc/empresa/criadero-arkahnius-323699 | 2026-11-03 | A por volumen (H): raza grande + guardería. Número de perros desconocido. Avisar capacidad |
| P023 | Pet Lovers Criadero | criadero | Cajicá (Cundinamarca) | petloverscriadero.com | +57 301 460 0976 · hola@petloverscriadero.com (D) | Criadero familiar de golden, husky, malamute, border collie y otras razas, más de 12 años (D); sitio con año 2026 (E) | B | borrador listo | https://petloverscriadero.com/ · https://about.me/pet.lovers · https://www.zoominfo.com/c/pet-lovers-criadero/1335137530 | 2026-11-03 | No confundir con "Pet Lovers Centro Canino" (Cra 6 # 2-60, Cajicá), que podría ser otro negocio |
| P024 | Criadero Santelmo | criadero | Chía (vereda Fagua) | desconocido | 310 216 6416 (V, directorio) | Akita, pastor alemán, border collie y otras razas; cachorros con registro ACCC (D) | C | no verificado | https://accc.com.co/cachorros/algunos-criaderos · https://guru4pets.com/gurus/santelmo-criadero-canino.html · https://revistageneticacanina.com/razas/criaderos-razas/criadero-santelmo/ · https://colombia.worldplaces.me/view-place/74623102-santelmo-criadero-canino.html | 2026-11-03 | Existe en varias fuentes, pero la reseña más reciente es de 2018. Posible A si sigue activo |
| P025 | Criadero Montecristo | criadero | Briceño (Cundinamarca) | cachorrosgoldenbogota.com | 300 586 1709 (D) | Golden, pomerania, yorkie y westie; padres "campeones nacionales" (D) | C | no verificado | https://cachorrosgoldenbogota.com/ · https://cachorrosgoldenbogota.com/contacto.php | 2026-11-03 | Solo fuentes propias. Queda cerca de Sopó (H): logística fácil |
| P026 | Rottbullcan | criadero | El Rosal (Cundinamarca) | rottbullcan.com | +57 312 529 1524 (D) | Rottweiler; dice ser "el criadero de rottweiler más grande de Colombia" (D) | C | no verificado | https://rottbullcan.com/contacto/ · https://rottbullcan.com/nosotros/ | 2026-11-03 | Su sitio tiene contenido de plantilla y ubicaciones distintas (V). Si es real, volumen grande: avisar capacidad |
| P027 | GoldenBros | criadero | desconocido | goldenbros.com.co | 316 431 8138 (V, listado ACCC) | Golden retriever importado de EE. UU. (D) | C | no verificado | https://goldenbros.com.co/ · https://accc.com.co/cachorros/algunos-criaderos | 2026-11-03 | Ubicación desconocida |
| P028 | Criadero Golden San Martín | criadero | desconocido | facebook.com/p/Criadero-Golden-San-Martín-100035012366767 | desconocido | Golden retriever (V) | C | no verificado | https://www.facebook.com/p/Criadero-Golden-San-Mart%C3%ADn-100035012366767/ · https://accc.com.co/cachorros/algunos-criaderos | 2026-11-03 | Ubicación desconocida |
| P029 | Dinastía Cachorros | otro | Bogotá y Medellín | dinastiacachorros.com.co | desconocido | Vende cachorros de muchas razas en varias ciudades (D) | — | descartado: intermediario de venta de cachorros, no criadero propio | https://dinastiacachorros.com.co/criadero-perros-bogota/ | 2026-11-03 | |
| P030 | Cachorros Elite | otro | desconocido | cachorroselite.com | desconocido | Páginas de "criadero" por raza y ciudad sin ubicación (V) | — | descartado: intermediario de venta de cachorros | https://cachorroselite.com/producto/criadero-gran-danes-bogota/ | 2026-11-03 | |
| P031 | Mascotas Medellín | otro | Rionegro (Antioquia) | mascotasmedellin.com | desconocido | Vende cachorros en varias ciudades; contacto en Rionegro (E) | — | descartado: intermediario fuera de Bogotá | https://mascotasmedellin.com/colombia/bogota/gran-danes/ | 2026-11-03 | |
| P032 | CanBridge | guardería | Usaquén (norte de Bogotá) y Chía (vía Guaymaral) | canbridgeguarderiacanina.com | desconocido (WhatsApp en su sitio) | Guardería, colegio y hotel con ruta puerta a puerta de Calle 200 a Calle 63 (D); opera desde 1995 como El Frailejón (V) | B | borrador listo | https://canbridgeguarderiacanina.com/ · https://www.semana.com/perros/actividades/articulo/colegios-para-perros-en-colombia/5391/ | 2026-11-03 | Copiar el WhatsApp desde su sitio |
| P033 | Country Club Canino | hotel | Usaquén (a 5 min de Cra 7 con Calle 127) | countryclubcanino.com · facebook.com/CountryClubCan | WhatsApp 316 490 0757 (V, negocio.site) | Hotel y guardería en más de 20 hectáreas de bosque (D) | B | borrador listo | https://countryclubcanino.com/ · https://www.facebook.com/CountryClubCan/ · https://countryclubcanino.negocio.site/ | 2026-11-03 | |
| P034 | El Parque Club Canino | guardería | La Calera (vereda El Triunfo) | elparqueclubcanino.com · facebook.com/ElParqueClubCanino | WhatsApp 316 301 9608 · info@elparqueclubcanino.com (D) | Colegio, guardería, hotel y semi internado; más de 11 años (D) | B | borrador listo | https://elparqueclubcanino.com/ · https://www.facebook.com/ElParqueClubCanino/ · https://www.petbacker.es/colombia/daycare/bogota/bogot%C3%A1/guarder%C3%ADa-canina-campestre-bogota-el-parque-club-canino-day-nursery | 2026-11-03 | |
| P035 | Cultura Canina | guardería | Bogotá rural (km 4.5 vía Patios–La Calera) | culturacanina.com · @culturacanina | 311 872 6182 · familia@culturacanina.com (D) | Colegio, guardería y hotel con transporte puerta a puerta y veterinario 24/7 (D) | B | borrador listo | https://culturacanina.com/ · https://www.instagram.com/culturacanina/ · https://www.facebook.com/CulturaCanina1/ | 2026-11-03 | |
| P036 | The CamPets | guardería | Suba (Villa del Prado, Calle 172 # 135-54) | thecampets.com | 310 268 4430 (V) | Guardería, hotel y colegio (D) | B | borrador listo | https://thecampets.com/ · https://www.waze.com/live-map/directions/co/cundinamarca/bogota/the-campets-guarderia-canina?to=place.ChIJOb0xIiWEP44RgZDJL7DDaXs · https://yandex.com/maps/org/the_campets/228419052858/ | 2026-11-03 | Horario corto (8:00–15:00) según Waze (V) |
| P037 | La Huella Campestre | guardería | Tenjo (Cundinamarca) | lahuellacampestre.com | +57 321 474 5545 (V) | Colegio, guardería, hotel y veterinaria (D) | C | no verificado | https://lahuellacampestre.com/ · https://www.depelos.co/guarderia-colegio-perros/guarderia-campestre-tenjo-bogota/5 | 2026-11-03 | El sitio tiene unos 5 años sin cambios (V) |
| P038 | Country Pets Col | guardería | Chía (Cra 7 km 17) | countrypetscol.com · facebook.com/countrypetscol | +57 310 231 8727 (V, Facebook) | Guardería, colegio, hotel y spa (D) | C | no verificado | https://countrypetscol.com/ · https://www.facebook.com/countrypetscol/ | 2026-11-03 | El sitio tiene unos 4 años sin cambios (V) |


## Lote 1 · 2026-11-03 · tiendas y veterinarias · Usaquén (P001–P009)

### Resumen

1. Revisados: 9 negocios de tiendas y veterinarias en Usaquén (P001–P009).
2. Resultado: A 1 · B 2 · C 5 · descartados 1 (posible cliente actual).
3. Los 3 mejores: Animal Center (5 sedes con pet shop y consulta) · Dog Kat ("hipermercado para mascotas" en Cedritos) · Clínica Veterinaria Dover (24 h con Pet Center).
4. Quedó `desconocido`: marcas naturales que venden (9 de 9), si tienen congelador (9 de 9), canal confirmado en 4 negocios.
5. Debe decidir Andrés: confirmar si P001 es cliente actual; aprobar los 3 borradores.

Supuestos: zona Usaquén por BL-010. Tipo tiendas y veterinarias juntas porque en Usaquén casi todas combinan las dos cosas.

### Búsquedas hechas

| Fecha | Fuente | Búsqueda | Resultados útiles |
|---|---|---|---|
| 2026-11-03 | WebFetch | pixie.com.co, peluditosbarf.com.co, dogsy.com.co, bocadopetfood.com, 4dogs.co, campeonpetfood.com, masvital.pet | Ninguno: dominios bloqueados por la red de la sesión |
| 2026-11-03 | WebSearch | Pixie alimento natural perros puntos de venta Bogotá tiendas | Pixie dice tener más de 700 puntos de venta; sin lista pública |
| 2026-11-03 | WebSearch | Peluditos BARF puntos de venta Bogotá | Sin lista de tiendas |
| 2026-11-03 | WebSearch | Vital Doggy dónde comprar Bogotá tiendas | Sin resultados de la marca |
| 2026-11-03 | WebSearch | tienda comida natural BARF perros Usaquén Bogotá | Solo fabricantes BARF (competidores) |
| 2026-11-03 | WebSearch | pet shop Cedritos Usaquén Bogotá tienda de mascotas dirección WhatsApp | Cedritos Pet Shop, Dog Kat, Animal Center, La Esquina de los Peludos, Petcol |
| 2026-11-03 | WebSearch | veterinaria con tienda Usaquén Bogotá … Santa Bárbara Country | Veterinaria Grecia, Animal Center, Dover |
| 2026-11-03 | WebSearch | alimento natural perros tienda Bogotá Suba Calle 147 Cedritos domicilios BARF congelado | Natural Taste |
| 2026-11-03 | WebSearch | Magavet dónde comprar Bogotá tiendas veterinarias lista | Página "dónde comprar" de Magavet (unos 2 años) |
| 2026-11-03 | WebSearch | Búsquedas de verificación por nombre (7) | Segunda fuente para Animal Center, Dog Kat y Dover |

### Notas del lote

Coincidencias con clientes del Excel de ventas: 1 (sin nombres).

### Fichas A

#### P002 · Animal Center (A)

**Por qué es buen cliente**
1. Tiene 5 sedes en Bogotá con pet shop, farmacia y consulta veterinaria: Cedritos, Santa Bárbara, Pepe Sierra, Bella Suiza y Rosales (E) — https://www.animalcenter.pet/nuestras-sedes/, 2026-11-03
2. Una guía de tiendas de mascotas de Bogotá de 2026 lo presenta como cadena con 6 sedes y más de 20 años (E) — https://colombia.com.co/tiendas-de-mascotas-en-bogota/, 2026-11-03
3. Un solo acuerdo cubre varias sedes del norte; la consulta veterinaria puede recomendar el producto (H).

**Qué le puede interesar de Canívoros:** un alimento horneado, hecho cerca (Sopó) y listo para servir, que el veterinario puede recomendar y la tienda vender en sus 5 sedes.

**Preguntas para la primera conversación**
- ¿Qué marcas de alimento venden más hoy? ¿Manejan alguna natural u horneada?
- ¿Tienen congelador o nevera para producto refrigerado en todas las sedes?
- ¿Quién decide las compras: cada sede o una oficina central?
- ¿Cada cuánto reponen y cómo le compran a su proveedor (pedido mínimo, plazo de pago)?

**Borrador**
> Buenos días, equipo de Animal Center. Le escribe [nombre de quien escribe], de Canívoros. Somos una marca de Sopó que hace alimento horneado para perros con pollo, salmón o cerdo, listo para servir; nació en una familia que cría perros de competencia. Vi que tienen pet shop y consulta veterinaria en sus sedes de Cedritos, Santa Bárbara, Pepe Sierra, Bella Suiza y Rosales. ¿Con quién podría hablar sobre nuevos productos para sus tiendas? [número comercial por definir]

### Borradores B

#### P003 · Dog Kat (B)

> Hola, equipo de Dog Kat. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que en Cedritos tienen un hipermercado para mascotas con domicilios, por eso pensé que podría encajar con sus clientes. ¿Les puedo contar cómo trabajamos con tiendas? Mi WhatsApp es [número comercial por definir].

#### P004 · Clínica Veterinaria Dover (B)

> Buenos días. Le escribe [nombre de quien escribe], de Canívoros. Somos una marca de Sopó que hace alimento horneado para perros con proteína animal, listo para servir; nació en una familia que cría perros de competencia. Vi que en Dover Santa Bárbara tienen Pet Center además de la atención 24 horas. ¿Tendría unos minutos esta semana para conocer el producto? [número comercial por definir]

## Lote 2 · 2026-11-03 · tiendas y veterinarias · Suba (P010–P015)

### Resumen

1. Revisados: 6 negocios de tiendas y veterinarias en Suba (P010–P015).
2. Resultado: A 2 · B 1 · C 3 · descartados 0.
3. Los 3 mejores: Pet Gold (vende Pixie horneado congelado y tiene stock) · Mundo Mascota Pet Shop (Pixie en catálogo, 4 sedes) · Puppy Export (cadena con sede en Niza).
4. Quedó `desconocido`: si tienen congelador (6 de 6), canal confirmado (4 de 6), marcas que más rotan (6 de 6).
5. Debe decidir Andrés: Pet Gold (Calle 150 # 45-41) queda a unas 15 cuadras de Clínica Veterinaria Manimal, distribuidor actual: acordar atribución antes de contactar. Aprobar 3 borradores.

Supuestos: zona Suba por BL-010. Mismo método de verificación (ver «Cómo se verificó») (solo resultados de búsqueda; Maps e Instagram bloqueados).

### Búsquedas hechas

| Fecha | Fuente | Búsqueda | Resultados útiles |
|---|---|---|---|
| 2026-11-03 | WebSearch | pet shop Suba Bogotá alimento natural perros domicilio instagram | Distribuciones J & S, T & T Mascotas, Masvital (competidor) |
| 2026-11-03 | WebSearch | pet shop Colina Campestre Niza Mazurén Suba … | Puppy Export Niza; otra cadena que coincide con un cliente del Excel (sin nombre) |
| 2026-11-03 | WebSearch | mundomascotapetshop.com Pixie alimento natural horneado | Mundo Mascota con Pixie; lista de cadenas que venden Pixie |
| 2026-11-03 | WebSearch | "Pixie" dieta horneada congelado tienda mascotas Bogotá … | Pet Gold con Pixie y stock |
| 2026-11-03 | WebSearch | Pet Gold tienda mascotas Colombia petgold.com.co sede Bogotá | Direcciones de Pet Gold en Suba |
| 2026-11-03 | WebSearch | Valenutrirse … (2 búsquedas) | Solo su sitio |
| 2026-11-03 | WebSearch | Puppy Export tienda para mascotas Bogotá sedes Niza | Sedes y canal |

### Notas del lote

Coincidencias con clientes del Excel de ventas: 0.

### Fichas A

#### P010 · Pet Gold (A)

**Por qué es buen cliente**
1. Su tienda online vende Pixie dieta horneada congelada de carne de res (500 g) y mostraba 131 unidades disponibles (E) — https://petgold.com.co/productos/pixie-dieta-horneada-carne-de-res-500gr/, 2026-11-03
2. Opera como veterinaria y tienda en Rappi, con un local en Calle 150 # 45-41 y un centro de distribución en Cra 56A # 159-82 (E) — https://www.rappi.com.co/tiendas/900172241-petgold-veterinaria-mt-nc, 2026-11-03
3. Si vende horneado congelado, ya tiene congelador y clientes que compran este tipo de alimento (H).

**Qué le puede interesar de Canívoros:** una segunda marca de horneado, hecha en Sopó, para clientes que ya compran este formato.

**Preguntas para la primera conversación**
- ¿Cuánto Pixie venden al mes y en qué presentación?
- ¿Sus clientes piden otras proteínas (salmón, cerdo)?
- ¿Cuánto espacio de congelador tienen y en cuántos locales?
- ¿Cómo le compran al proveedor (pedido mínimo, plazo de pago)?

**Borrador**
> Hola, equipo de Pet Gold. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que en su tienda manejan dieta horneada congelada, por eso pensé que podría encajar con sus clientes. ¿Les puedo contar cómo trabajamos con tiendas? Mi WhatsApp es [número comercial por definir].

#### P011 · Mundo Mascota Pet Shop (A)

**Por qué es buen cliente**
1. Su catálogo incluye Pixie de pescado al horno; al indexarse aparecía sin stock (E) — https://www.mundomascotapetshop.com/product/detail/eyJpdiI6ImtudEpYUEkyVlVqbjJJWVZiTW1EOXc9PSIsInZhbHVlIjoiVjNCejJZWnVtNzRoTjhuWUVNY0czdz09IiwibWFjIjoiNmM0YTgwNTAxMTIyZGVmNjJjOThjNDczZGY0NDk4ZTAxNWRkNmE2Zjg4NTVhMGE0MjRkYjQwZmZkMDFmNjQ0MiJ9, 2026-11-03
2. Tiene 4 sedes: Las Villas (Calle 128B # 59A-22), Tabora, Las Ferias y San Miguel (E) — https://mundomascotapetshop.com/, 2026-11-03
3. Un producto horneado sin stock puede indicar problemas de abastecimiento con su proveedor actual (H).

**Qué le puede interesar de Canívoros:** un horneado de un proveedor cercano para no quedarse sin producto en sus 4 sedes.

**Preguntas para la primera conversación**
- ¿Cada cuánto se les agota el alimento horneado y por qué?
- ¿Tienen congelador en las 4 sedes?
- ¿Qué marcas de alimento natural piden más sus clientes?
- ¿Las compras se deciden por sede o en un solo lugar?

**Borrador**
> Hola, equipo de Mundo Mascota. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que en su catálogo tienen alimento horneado y cuatro sedes en Bogotá, por eso pensé que podría encajar con sus clientes. ¿Les puedo contar cómo trabajamos con tiendas? Mi WhatsApp es [número comercial por definir].

### Borradores B

#### P012 · Puppy Export (B)

> Hola, equipo de Puppy Export. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que tienen varias sedes en Bogotá, incluida Niza, y domicilios en toda la ciudad, por eso pensé que podría encajar con sus clientes. ¿Les puedo contar cómo trabajamos con tiendas? Mi WhatsApp es [número comercial por definir].

## Lote 3 · 2026-11-03 · tiendas y veterinarias · Chapinero y cadenas que venden Pixie (P016–P021)

### Resumen

1. Revisados: 6 negocios: 4 de Chapinero y 2 cadenas de varias localidades (P016–P021).
2. Resultado: A 3 · B 1 · C 2 · descartados 0.
3. Los 3 mejores: Puppis (vende Pixie congelado; 34 tiendas) · Laika (vende Pixie; 23 tiendas y en expansión) · Agrocampo (vende Pixie; hipermercado en Av. Caracas).
4. Quedó `desconocido`: canal comercial de compras de las 3 cadenas, si Pet Garden vende natural, y datos de Doglamour y El Paraíso de las Mascotas, que solo tienen su propio sitio.
5. Debe decidir Andrés: si vale la pena entrar a cadenas grandes ahora. Piden proceso formal de proveedor y volumen, y la capacidad de producción es `desconocido` (BL-036). Aprobar 4 borradores.

Supuestos: las cadenas se agrupan en este lote aunque tengan sedes en varias localidades, porque se negocian con una sola oficina (H). Mismo método de verificación (ver «Cómo se verificó»).

### Búsquedas hechas

| Fecha | Fuente | Búsqueda | Resultados útiles |
|---|---|---|---|
| 2026-11-03 | WebSearch | tienda de mascotas Chapinero Bogotá comida natural BARF perros | Solo fabricantes BARF (competidores) |
| 2026-11-03 | WebSearch | tienda de mascotas Chapinero Chicó Galerías … alimento premium natural | Doglamour, Pet Garden, El Paraíso de las Mascotas |
| 2026-11-03 | WebSearch | tienda holística natural para mascotas Bogotá … | Doglamour, Valenutrirse, competidores |
| 2026-11-03 | WebSearch | pixie.net.co puntos de venta Bogotá … | Pixie no publica puntos de venta; tiendas que lo venden |
| 2026-11-03 | WebSearch | Puppis Colombia tiendas Bogotá sedes … 2026 | Sedes de Puppis |
| 2026-11-03 | WebSearch | Laika mascotas tiendas físicas Bogotá … 2026 | Tiendas y prensa 2026 |
| 2026-11-03 | WebSearch | Agrocampo tiendas Bogotá sedes dirección | Sede Av. Caracas |
| 2026-11-03 | WebSearch | Doglamour, Pet Garden, El Paraíso de las Mascotas (3 búsquedas) | Verificación |

### Notas del lote

Coincidencias con clientes del Excel de ventas: 0.

### Dato para competencia (BL-015)

Pixie es el competidor más directo: también es **horneado y congelado**. Se vende en Puppis, Laika, Agrocampo, Pet Gold, Mundo Mascota, Homecenter y Rappi. Pixie no publica su lista de puntos de venta (E) — https://pixie.net.co/, 2026-11-03.

Precios vistos el 2026-11-03 en resultados de búsqueda; pueden haber cambiado:

| Producto | Tienda | Precio (COP) | Fuente |
|---|---|---|---|
| Pixie dieta horneada carne de res 500 g | Laika | 12.900 (12.255 con descuento) | https://laika.com.co/product_details/bog/pixie-dieta-horneada-carne-de-res/dog |
| Pixie dieta horneada carne de res 500 g | Pet Gold | 13.000 | https://petgold.com.co/productos/pixie-dieta-horneada-carne-de-res-500gr/ |
| Pixie dieta horneada pollo 2 kg (congelado) | Puppis | 42.500 | https://www.puppis.com.co/alimento-congelado-para-perro-pixie-dieta-horneada-pollo/p |
| Pixie dieta horneada perro adulto pavo | Agrocampo | 17.551 (peso desconocido) | https://www.agrocampo.com.co/perros/comida/pixie |

Puppis indica guardar Pixie en congelador a −18 °C y descongelar en nevera (E). Las tiendas que venden Pixie ya tienen congelador.

Otras marcas naturales encontradas en las búsquedas. Son competidores, no prospectos, y no se registran: Dogsy, Bocado, 4Dogs, Peluditos BARF, Barf Pet Colombia, Masvital, Campeón Pet Food, Hello Dog, Petmeal, Rovinfood, Duby Natural y Fortiz Pets (BARF o cocido), y Natural Toys y Petinco (snacks). Conviene pasarlas a `competencia/`.

### Fichas A

#### P019 · Puppis (A)

**Por qué es buen cliente**
1. Vende Pixie dieta horneada congelada de pollo en 2 kg, con instrucciones de congelador (E) — https://www.puppis.com.co/alimento-congelado-para-perro-pixie-dieta-horneada-pollo/p, 2026-11-03
2. Tiene sedes en Chicó (Cra 15 # 94-52), Galerías (Calle 53 # 16-53) y Chapinero; dice tener 34 tiendas en Colombia (D) — https://www.puppis.com.co/nuestras-sucursales, 2026-11-03
3. Si entra en la cadena, llega a muchas tiendas con un solo acuerdo (H).

**Qué le puede interesar de Canívoros:** una segunda marca de horneado congelado, hecha en Sopó, con proteínas que Pixie no siempre tiene (salmón, cerdo).

**Preguntas para la primera conversación**
- ¿Quién maneja la compra de alimento natural y congelado?
- ¿Qué requisitos piden a un proveedor nuevo (registro, codificación, volumen)?
- ¿Cuánto rota el horneado congelado en Bogotá?
- ¿Hacen pruebas en pocas tiendas antes de llevar un producto a toda la cadena?

**Borrador**
> Buenos días, equipo de compras de Puppis. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que en sus tiendas ya venden dieta horneada congelada, por eso pensé que podría encajar con sus clientes. ¿Con quién podría hablar sobre proveedores nuevos de esta categoría? [número comercial por definir]

#### P020 · Laika (A)

**Por qué es buen cliente**
1. Vende Pixie dieta horneada en su tienda online de Bogotá (E) — https://laika.com.co/product_details/bog/pixie-dieta-horneada-carne-de-res/dog, 2026-11-03
2. Tiene 23 tiendas en Colombia y está abriendo más en 2026 (E) — https://abceconomia.co/2026/10/01/tiendas-fisicas-de-laika-expansion-chile-2026/, 2026-11-03
3. Dice ofrecer más de 4.000 productos, entre ellos dietas naturales (D).

**Qué le puede interesar de Canívoros:** un horneado local para su categoría de dietas naturales, con entrega desde Sopó.

**Preguntas para la primera conversación**
- ¿Cómo es el proceso para proveedores nuevos?
- ¿Venden alimento congelado en todas sus tiendas o solo online?
- ¿Qué volumen esperan de un proveedor en el primer pedido?
- ¿Aceptan marcas pequeñas en prueba?

**Borrador**
> Buenos días, equipo de Laika. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que en Laika ya ofrecen dieta horneada dentro de sus dietas naturales. ¿Cuál es el proceso para presentarles un proveedor nuevo? [número comercial por definir]

#### P021 · Agrocampo (A)

**Por qué es buen cliente**
1. Vende Pixie en su categoría de comida para perros (E) — https://www.agrocampo.com.co/perros/comida/pixie, 2026-11-03
2. Tiene un hipermercado agro y de mascotas en Av. Caracas # 73-39 con domicilio en Bogotá (E) — https://www.agrocampo.com.co/, 2026-11-03
3. Su cliente compra por volumen y precio (H).

**Qué le puede interesar de Canívoros:** un horneado hecho en Cundinamarca, que encaja con su perfil agro y local.

**Preguntas para la primera conversación**
- ¿Quién compra la categoría de alimento para perros?
- ¿Qué requisitos tienen para proveedores nuevos?
- ¿Cuánto rota el alimento horneado frente al concentrado?
- ¿Tienen congelador en la tienda de la Caracas?

**Borrador**
> Buenos días, equipo de Agrocampo. Les escribe [nombre de quien escribe], de Canívoros: hacemos alimento horneado para perros en Sopó, con pollo, salmón o cerdo, listo para servir. Vi que en Agrocampo ya venden alimento horneado para perros. ¿Con quién podría hablar sobre proveedores nuevos de esta categoría? [número comercial por definir]

### Borradores B

#### P016 · Pet Garden Veterinaria (B)

> Buenos días. Le escribe [nombre de quien escribe], de Canívoros. Somos una marca de Sopó que hace alimento horneado para perros con proteína animal, listo para servir; nació en una familia que cría perros de competencia. Vi que en Pet Garden, en Galería 93, tienen veterinaria, grooming y tienda en un mismo lugar. ¿Tendría unos minutos esta semana para conocer el producto? [número comercial por definir]

## Lote 4 · 2026-11-03 · criaderos · Bogotá y Sabana (P022–P031)

### Resumen

1. Revisados: 10 criaderos o vendedores de cachorros de Bogotá y la Sabana (P022–P031).
2. Resultado: A 1 · B 1 · C 5 · descartados 3 (intermediarios de venta de cachorros).
3. Los 3 mejores: Criadero Arkahnius (pastor alemán con criadero y guardería en Guaymaral) · Pet Lovers Criadero (razas medianas y grandes en Cajicá; sitio activo en 2026) · Criadero Santelmo (akita y pastor alemán en Chía; existe en varias fuentes, pero falta una señal reciente).
4. Quedó `desconocido`: número de perros de cada criadero (10 de 10), ubicación de 2 criaderos, señal reciente en 5.
5. Debe decidir Andrés: Arkahnius y Rottbullcan podrían pedir volúmenes grandes, y la capacidad de producción es `desconocido` (BL-036). Revisar si alguno ya compra como "criador" en el Excel de ventas (el script no encontró coincidencias de nombre). Aprobar 2 borradores.

Supuestos: razas grandes primero, como pide la skill, porque los criadores que más compran en julio–octubre llevan de 40 a 520 kg (BL-043). Se incluyen municipios de la Sabana porque muchos criaderos de Bogotá están ahí. Mismo método de verificación (ver «Cómo se verificó»).

### Búsquedas hechas

| Fecha | Fuente | Búsqueda | Resultados útiles |
|---|---|---|---|
| 2026-11-03 | WebSearch | criadero pastor alemán Bogotá Cundinamarca cachorros exposición | Arkahnius, Montenegro, avisos clasificados viejos |
| 2026-11-03 | WebSearch | criadero dóberman rottweiler Bogotá Cundinamarca criadero registrado ACCC | Rottbullcan; intermediarios |
| 2026-11-03 | WebSearch | criadero gran danés mastín dogo akita Bogotá Cundinamarca | Santelmo; intermediarios |
| 2026-11-03 | WebSearch | criadero golden retriever labrador Bogotá Cundinamarca exposición campeón | Montecristo, GoldenBros, Pet Lovers, Golden San Martín |
| 2026-11-03 | WebSearch | ACCC "algunos criaderos" … | Lista de criaderos anunciados en la ACCC (sin verificación de la ACCC) |
| 2026-11-03 | WebSearch | Verificación por nombre (6 búsquedas) | Arkahnius, Rottbullcan, Montecristo, Pet Lovers, GoldenBros, Santelmo |

### Notas del lote

Coincidencias con clientes del Excel de ventas: 0.

- Los sitios de "venta de cachorros" con páginas por raza y ciudad (Dinastía Cachorros, Cachorros Elite, Mascotas Medellín y similares) no muestran un criadero propio. Se descartan.
- La ACCC aclara que su lista de criaderos la publican los dueños y que no la verifica.
- Un proyecto de ley de 2025 en el Senado (PL 002 de 2025) busca prohibir la cría y venta de animales de compañía. Si avanza, afectaría a este segmento.

### Fichas A

#### P022 · Criadero Arkahnius (A)

**Por qué es buen cliente**
1. Se presenta como criadero de pastor alemán en Guaymaral, con registro APPA (D) — https://www.criaderopastoralemanbogota.com/, 2026-11-03
2. Opera también una guardería y hotel canino, "Arkahnius Dog Club", en Guaymaral (D) — https://www.hotelguarderiacaninabogota.com/, 2026-11-03
3. Un criadero de raza grande con guardería alimenta muchos perros todos los días (H). Aparece en un directorio de empresas (E) — https://www.nexdu.com/co/bogota-dc-dc/empresa/criadero-arkahnius-323699, 2026-11-03

**Qué le puede interesar de Canívoros:** una marca que viene del mismo mundo, los perros de competencia, con compra por kilo para criadores y un producto para recomendar a quien compra un cachorro.

**Preguntas para la primera conversación**
- ¿Cuántos perros alimentan hoy entre el criadero y la guardería?
- ¿Qué alimento usan y cuántos kilos compran al mes?
- ¿Recomiendan un alimento a las familias que compran cachorros?
- ¿Tienen congelador o nevera para producto refrigerado?

**Borrador**
> Hola, Criadero Arkahnius. Soy [nombre de quien escribe], de Canívoros. Venimos del mundo de los perros de competencia y hacemos en Sopó alimento horneado con pollo, salmón o cerdo, listo para servir. Vi que crían pastor alemán y que también tienen guardería en Guaymaral. ¿Cuántos perros manejan hoy? Si le interesa, le cuento cómo le vendemos a criaderos. [número comercial por definir]

### Borradores B

#### P023 · Pet Lovers Criadero (B)

> Hola, Pet Lovers Criadero. Soy [nombre de quien escribe], de Canívoros. Venimos del mundo de los perros de competencia y hacemos en Sopó alimento horneado con pollo, salmón o cerdo, listo para servir. Vi que en Cajicá crían golden, husky, malamute y border collie. ¿Cuántos perros manejan hoy? Si le interesa, le cuento cómo le vendemos a criaderos. [número comercial por definir]

## Lote 5 · 2026-11-03 · guarderías, colegios y hoteles caninos · norte de Bogotá y Sabana (P032–P038)

### Resumen

1. Revisados: 7 servicios caninos del norte de Bogotá y la Sabana (P032–P038).
2. Resultado: A 0 · B 5 · C 2 · descartados 0.
3. Los 3 mejores: CanBridge (guardería con ruta puerta a puerta de la Calle 200 a la 63; opera desde 1995, según Semana) · Country Club Canino (hotel y guardería en 20 hectáreas en Usaquén) · Cultura Canina (colegio, hotel y veterinario 24/7 en la vía a La Calera).
4. Quedó `desconocido`: cuántos perros atienden (7 de 7), qué alimento dan (7 de 7), si venden alimento a sus clientes (7 de 7).
5. Debe decidir Andrés: si las guarderías se abordan como clientes (alimentan perros) o como recomendadores (código o QR, como en el Experimento 3 del plan). Aprobar 5 borradores.

Supuestos: prioridad media según la guía. Se juntan guarderías, colegios y hoteles porque casi todos ofrecen los tres servicios. Mismo método de verificación (ver «Cómo se verificó»).

### Búsquedas hechas

| Fecha | Fuente | Búsqueda | Resultados útiles |
|---|---|---|---|
| 2026-11-03 | WebSearch | centro de adiestramiento canino Bogotá escuela canina obediencia guardería campestre | El Parque, CanBridge, La Huella Campestre, Cultura Canina, Insignia, Adiscan |
| 2026-11-03 | WebSearch | guardería canina hotel para perros Bogotá Usaquén Suba Chía campestre | Country Club Canino, Canes Club Campestre, Country Pets, The CamPets, Dogs Urban |
| 2026-11-03 | WebSearch | Verificación por nombre (7 búsquedas) | CanBridge, Country Club Canino, El Parque, The CamPets, La Huella, Cultura Canina, Country Pets |

### Notas del lote

Coincidencias con clientes del Excel de ventas: 0.

Para un siguiente lote quedaron sin revisar: Centro de adiestramiento Insignia (Suba), Adiscan (Engativá), Dogest y Dog Happy (Usaquén), Canes Club Campestre, Dogs Urban y Alaska Dog's (Cajicá).

### Borradores B

#### P032 · CanBridge (B)

> Hola, equipo de CanBridge. Soy [nombre de quien escribe], de Canívoros: alimento horneado para perros, hecho en Sopó y listo para servir. Vi que tienen guardería y hotel en el norte de Bogotá y en Chía, con ruta puerta a puerta. ¿Les interesaría conocerlo para los perros que atienden o para recomendarlo a sus clientes? [número comercial por definir]

#### P033 · Country Club Canino (B)

> Hola, equipo de Country Club Canino. Soy [nombre de quien escribe], de Canívoros: alimento horneado para perros, hecho en Sopó y listo para servir. Vi que tienen hotel y guardería en una zona de bosque en Usaquén. ¿Les interesaría conocerlo para los perros que atienden o para recomendarlo a sus clientes? [número comercial por definir]

#### P034 · El Parque Club Canino (B)

> Hola, equipo de El Parque Club Canino. Soy [nombre de quien escribe], de Canívoros: alimento horneado para perros, hecho en Sopó y listo para servir. Vi que tienen colegio, guardería y semi internado en su sede campestre de La Calera. ¿Les interesaría conocerlo para los perros que atienden o para recomendarlo a sus clientes? [número comercial por definir]

#### P035 · Cultura Canina (B)

> Hola, equipo de Cultura Canina. Soy [nombre de quien escribe], de Canívoros: alimento horneado para perros, hecho en Sopó y listo para servir. Vi que tienen colegio, guardería y hotel en la vía a La Calera, con transporte puerta a puerta. ¿Les interesaría conocerlo para los perros que atienden o para recomendarlo a sus clientes? [número comercial por definir]

#### P036 · The CamPets (B)

> Hola, equipo de The CamPets. Soy [nombre de quien escribe], de Canívoros: alimento horneado para perros, hecho en Sopó y listo para servir. Vi que tienen guardería, hotel y colegio en Suba. ¿Les interesaría conocerlo para los perros que atienden o para recomendarlo a sus clientes? [número comercial por definir]
