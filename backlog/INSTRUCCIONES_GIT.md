# Cómo subir este backlog a la rama `backlog`

Requiere permiso de escritura en `quemasandy/canivoros`.

```bash
git clone https://github.com/quemasandy/canivoros.git   # o entra a tu copia local
cd canivoros
git fetch origin
git checkout -b backlog origin/develop     # si la rama ya existe en origin, NO la sobrescribas
cp -r /ruta/descomprimida/backlog ./backlog
git add backlog
git commit -m "Agrega backlog semanal (BL-001...BL-034)"
git push -u origin backlog                 # sin --force
```

Ver: https://github.com/quemasandy/canivoros/tree/backlog
