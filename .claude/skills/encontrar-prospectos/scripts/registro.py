#!/usr/bin/env python3
"""Revisa e importa el registro de prospectos (prospectos/REGISTRO.md).

Subcomandos:
  revisar REGISTRO.md [--excluir ventas.xlsx ...] [--hoy AAAA-MM-DD]
      Valida la tabla: IDs, celdas vacías, niveles y estados, fuentes y fechas,
      duplicados, distribuidores publicados y posibles clientes actuales.
      Imprime un informe en Markdown con el siguiente ID libre.

  importar LISTA.csv|xlsx --registro REGISTRO.md [--excluir ...] [--hoja H] [--escribir]
      Convierte una lista externa en filas del registro (nivel C, estado
      "por verificar", fuente marcada (V)). Omite duplicados, distribuidores
      publicados y clientes actuales. Sin --escribir solo muestra las filas.

Los nombres de clientes del Excel de ventas nunca se imprimen ni se escriben:
solo se informa que hubo una coincidencia. Solo usa la biblioteca estándar;
para leer .xlsx necesita openpyxl.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import io
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DISTRIBUIDORES = SKILL_DIR / "assets" / "distribuidores_publicados.txt"
PLANTILLA_REGISTRO = SKILL_DIR / "assets" / "REGISTRO.md"

COLUMNAS = [
    "ID", "Nombre", "Tipo", "Localidad", "Web o redes", "Canal público",
    "Encaje", "Nivel", "Estado", "Fuentes", "Fecha", "Notas",
]
OPCIONALES = {"Notas"}

ESTADOS_VERIFICADOS = ("verificado", "borrador listo", "aprobado", "contactado")
ESTADOS_ABIERTOS = ("por verificar", "no verificado")
DIAS_VIGENCIA = 90

# Encabezado normalizado -> columna del registro (para importar listas externas).
ALIAS_IMPORTAR = {
    "nombre": "nombre", "negocio": "nombre", "establecimiento": "nombre",
    "empresa": "nombre", "razon_social": "nombre", "prospecto": "nombre",
    "nombre_del_negocio": "nombre", "nombre_comercial": "nombre",
    "tipo": "tipo", "segmento": "tipo", "tipo_de_negocio": "tipo", "categoria": "tipo",
    "localidad": "localidad", "zona": "localidad", "barrio": "barrio",
    "direccion": "direccion",
    "telefono": "telefono", "tel": "telefono", "celular": "telefono",
    "movil": "telefono", "telefonos": "telefono", "phone": "telefono",
    "whatsapp": "whatsapp", "wa": "whatsapp",
    "instagram": "instagram", "ig": "instagram", "facebook": "facebook",
    "web": "web", "sitio_web": "web", "pagina_web": "web", "website": "web", "url": "web",
    "correo": "correo", "email": "correo", "e_mail": "correo", "mail": "correo",
    "encaje": "encaje", "marcas": "marcas", "marcas_que_vende": "marcas",
}

PALABRAS_VACIAS = {
    "pet", "pets", "shop", "petshop", "tienda", "veterinaria", "veterinario",
    "clinica", "centro", "de", "del", "la", "el", "los", "las", "y", "and", "sas",
    "s", "a", "ltda", "mascotas", "mascota", "store", "spa", "the", "co", "company",
    "cia", "canino", "canina", "entrenamiento", "criadero",
}
# Localidades, barrios y municipios frecuentes en nombres ("Julián Cedritos"):
# no sirven para decidir si dos nombres son el mismo negocio.
LUGARES = {
    "bogota", "usaquen", "chapinero", "santa", "fe", "san", "cristobal", "usme",
    "tunjuelito", "bosa", "kennedy", "fontibon", "engativa", "suba", "barrios",
    "unidos", "teusaquillo", "martires", "antonio", "narino", "puente", "aranda",
    "candelaria", "rafael", "uribe", "ciudad", "bolivar", "sumapaz", "cedritos",
    "salitre", "modelia", "colina", "niza", "mazuren", "country", "chico", "chia",
    "cajica", "sopo", "tabio", "tenjo", "cota", "zipaquira", "tocancipa", "calera",
    "funza", "mosquera", "madrid", "soacha", "norte", "sur", "occidente", "oriente",
}
DOMINIOS_GENERICOS = {"wa.me", "api.whatsapp.com", "maps.google.com", "google.com", "goo.gl", "linktr.ee"}


# ---------------------------------------------------------------- utilidades

def sin_acentos(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))


def palabras(texto) -> list[str]:
    return re.findall(r"[a-z0-9]+", sin_acentos(str(texto or "")).lower())


def clave_encabezado(texto) -> str:
    return "_".join(palabras(texto))


CONECTORES = {"de", "del", "la", "el", "los", "las", "y", "and", "the"}


def nombre_base(texto) -> str:
    """Nombre sin palabras genéricas ni lugares; si no queda nada, sin conectores."""
    todas = palabras(texto)
    utiles = [p for p in todas if p not in PALABRAS_VACIAS and p not in LUGARES]
    return " ".join(utiles or [p for p in todas if p not in CONECTORES] or todas)


def es_desconocido(valor: str) -> bool:
    return clave_encabezado(valor) in {"", "desconocido", "desconocida", "no_verificado", "na", "n_a"}


def telefonos(texto) -> set[str]:
    """Números de 7 o más dígitos (se ignoran espacios, guiones y puntos); últimos 10."""
    t = re.sub(r"(?<=\d)[\s.\-()]+(?=\d)", "", str(texto or ""))
    return {d[-10:] for d in re.findall(r"\d{7,}", t)}


def instagram(texto) -> set[str]:
    t = str(texto or "").lower()
    cuentas = set(re.findall(r"instagram\.com/([a-z0-9_.]{2,30})", t))
    cuentas |= set(re.findall(r"(?<![\w.])@([a-z0-9_.]{2,30})", t))
    return {c.strip(".") for c in cuentas if c.strip(".")}


def dominios(texto) -> set[str]:
    encontrados = set()
    for host, ruta in re.findall(r"(?:https?://)?(?:www\.)?([a-z0-9.-]+\.[a-z]{2,})(/[^\s|)]*)?", str(texto or "").lower()):
        if host in DOMINIOS_GENERICOS or host.endswith("instagram.com"):
            continue
        if host.endswith("facebook.com"):
            ruta = (ruta or "").strip("/").split("?")[0]
            if ruta:
                encontrados.add(f"facebook.com/{ruta}")
            continue
        encontrados.add(host)
    return encontrados


def celda(valor) -> str:
    if valor is None:
        return ""
    if isinstance(valor, (dt.datetime, dt.date)):
        return valor.strftime("%Y-%m-%d")
    if isinstance(valor, float) and valor.is_integer():
        return str(int(valor))
    return str(valor).strip()


def coincide_nombre(a: str, b: str) -> bool:
    if not a or not b:
        return False
    if a == b:
        return True
    corto, largo = sorted((a, b), key=len)
    # Un nombre contenido en otro cuenta si es lo bastante específico: dos o más
    # palabras, o una sola de 7 letras o más ("finkana" sí, "canes" no).
    especifico = " " in corto or len(corto) >= 7
    if especifico and re.search(rf"\b{re.escape(corto)}\b", largo):
        return True
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.88


# ---------------------------------------------------------------- registro en Markdown

def dividir_fila(linea: str) -> list[str]:
    cuerpo = linea.strip()
    if cuerpo.startswith("|"):
        cuerpo = cuerpo[1:]
    if cuerpo.endswith("|") and not cuerpo.endswith("\\|"):
        cuerpo = cuerpo[:-1]
    partes = re.split(r"(?<!\\)\|", cuerpo)
    return [p.strip().replace("\\|", "|") for p in partes]


def es_separador(linea: str) -> bool:
    return bool(re.fullmatch(r"\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*", linea))


class Registro:
    """La primera tabla Markdown del archivo cuyo encabezado incluye ID y Nombre."""

    def __init__(self, ruta: Path):
        self.ruta = ruta
        self.lineas = ruta.read_text(encoding="utf-8").splitlines() if ruta.exists() else []
        self.encabezado: list[str] = []
        self.filas: list[dict] = []
        self.fin_tabla = None  # índice de línea después de la última fila
        for i in range(len(self.lineas) - 1):
            if self.lineas[i].lstrip().startswith("|") and es_separador(self.lineas[i + 1]):
                encabezado = dividir_fila(self.lineas[i])
                claves = {clave_encabezado(h) for h in encabezado}
                if {"id", "nombre"} <= claves:
                    self.encabezado = encabezado
                    j = i + 2
                    while j < len(self.lineas) and self.lineas[j].lstrip().startswith("|"):
                        valores = dividir_fila(self.lineas[j])
                        valores += [""] * (len(encabezado) - len(valores))
                        fila = {self._canonica(h): v for h, v in zip(encabezado, valores)}
                        fila["_linea"] = j + 1
                        self.filas.append(fila)
                        j += 1
                    self.fin_tabla = j
                    break

    @staticmethod
    def _canonica(encabezado: str) -> str:
        clave = clave_encabezado(encabezado)
        for col in COLUMNAS:
            if clave_encabezado(col) == clave:
                return col
        return encabezado.strip()

    def siguiente_id(self) -> int:
        numeros = [int(m.group(1)) for f in self.filas if (m := re.fullmatch(r"P(\d+)", f.get("ID", "").strip()))]
        return max(numeros, default=0) + 1

    def agregar(self, filas: list[dict]) -> None:
        if self.fin_tabla is None:
            raise SystemExit(f"{self.ruta} no tiene la tabla del registro (encabezado con ID y Nombre).")
        columnas = [self._canonica(h) for h in self.encabezado]
        nuevas = [fila_markdown([f.get(c, "") for c in columnas]) for f in filas]
        self.lineas[self.fin_tabla:self.fin_tabla] = nuevas
        self.ruta.write_text("\n".join(self.lineas) + "\n", encoding="utf-8")


def fila_markdown(valores: list[str]) -> str:
    limpios = [str(v).replace("|", "\\|").replace("\n", " ").strip() for v in valores]
    return "| " + " | ".join(limpios) + " |"


# ---------------------------------------------------------------- exclusiones

def leer_csv(ruta: Path) -> list[list[str]]:
    for codificacion in ("utf-8-sig", "latin-1"):
        try:
            texto = ruta.read_text(encoding=codificacion)
            break
        except UnicodeDecodeError:
            continue
    try:
        dialecto = csv.Sniffer().sniff(texto[:4096], delimiters=",;\t")
    except csv.Error:
        dialecto = csv.excel
    return list(csv.reader(io.StringIO(texto, newline=""), dialecto))


def cargar_openpyxl():
    try:
        import openpyxl  # noqa: WPS433
    except ImportError:
        sys.exit("Para leer .xlsx instala openpyxl (pip install openpyxl) o usa CSV.")
    return openpyxl


def hojas_de(ruta: Path) -> list[list[list]]:
    if ruta.suffix.lower() in {".xlsx", ".xlsm"}:
        libro = cargar_openpyxl().load_workbook(ruta, read_only=True, data_only=True)
        return [[list(f) for f in ws.iter_rows(values_only=True)] for ws in libro.worksheets]
    return [leer_csv(ruta)]


def nombres_de(ruta: Path) -> list[str]:
    """Nombres de un .txt (uno por línea) o de la columna CLIENTE/nombre de un CSV o XLSX."""
    if ruta.suffix.lower() == ".txt":
        return [l.strip() for l in ruta.read_text(encoding="utf-8").splitlines()
                if l.strip() and not l.lstrip().startswith("#")]
    nombres = []
    for filas in hojas_de(ruta):
        indice = None
        for fila in filas:
            if indice is None:
                for i, v in enumerate(fila):
                    if clave_encabezado(celda(v)) in {"cliente", "clientes", "nombre", "distribuidor"}:
                        indice = i
                        break
                continue
            if indice < len(fila) and celda(fila[indice]):
                nombres.append(celda(fila[indice]))
    return nombres


class Exclusiones:
    def __init__(self, privados: list[Path], usar_distribuidores: bool = True):
        self.publicos = []
        if usar_distribuidores and DISTRIBUIDORES.exists():
            self.publicos = [(n, nombre_base(n)) for n in nombres_de(DISTRIBUIDORES)]
        self.privados = []
        for ruta in privados:
            if not ruta.exists():
                sys.exit(f"No existe {ruta}")
            self.privados += [nombre_base(n) for n in nombres_de(ruta)]
        self.privados = list(dict.fromkeys(self.privados))

    def revisar(self, nombre: str) -> tuple[str, str] | None:
        """('distribuidor', nombre público) o ('cliente', '') o None."""
        base = nombre_base(nombre)
        for original, norm in self.publicos:
            if coincide_nombre(base, norm):
                return "distribuidor", original
        for norm in self.privados:
            if coincide_nombre(base, norm):
                return "cliente", ""
        return None


# ---------------------------------------------------------------- revisar

def claves_duplicado(fila: dict) -> set[tuple]:
    contacto = f"{fila.get('Canal público', '')} {fila.get('Web o redes', '')}"
    claves = {("teléfono", t) for t in telefonos(contacto)}
    claves |= {("Instagram", c) for c in instagram(contacto)}
    claves |= {("web", d) for d in dominios(fila.get("Web o redes", ""))}
    nombre = nombre_base(fila.get("Nombre", ""))
    if nombre:
        claves.add(("nombre y localidad", (nombre, " ".join(palabras(fila.get("Localidad", ""))))))
    return claves


def estado_de(fila: dict) -> str:
    return " ".join(palabras(fila.get("Estado", "")))


def revisar(registro: Registro, exclusiones: Exclusiones, hoy: dt.date) -> str:
    if not registro.encabezado:
        return f"No encontré la tabla del registro en {registro.ruta}. Copia la plantilla assets/REGISTRO.md."

    bloqueantes: list[str] = []
    avisos: list[str] = []
    faltan_columnas = [c for c in COLUMNAS if c not in OPCIONALES and c not in {Registro._canonica(h) for h in registro.encabezado}]
    if faltan_columnas:
        avisos.append(f"Faltan columnas en la tabla: {', '.join(faltan_columnas)}.")

    ids = Counter(f.get("ID", "").strip() for f in registro.filas)
    vistos: dict[tuple, str] = {}
    listos = []

    for f in registro.filas:
        rid = f.get("ID", "").strip() or f"(línea {f['_linea']})"
        estado = estado_de(f)
        descartado = estado.startswith("descartado")
        verificado = estado.startswith(ESTADOS_VERIFICADOS)
        nivel = f.get("Nivel", "").strip().upper()

        if not re.fullmatch(r"P\d{3,}", f.get("ID", "").strip()):
            bloqueantes.append(f"{rid}: ID con formato inválido (usar P001, P002…).")
        elif ids[f["ID"].strip()] > 1:
            bloqueantes.append(f"{rid}: ID repetido.")

        vacias = [c for c in COLUMNAS if c not in OPCIONALES | {"Nivel"} and c in f and not f[c].strip()]
        if descartado:
            vacias = [c for c in vacias if c not in {"Nivel", "Fecha"}]
        if vacias:
            avisos.append(f"{rid}: celdas vacías en {', '.join(vacias)}; escribe `desconocido`.")

        if not estado:
            avisos.append(f"{rid}: sin estado.")
        elif not (descartado or verificado or estado.startswith(ESTADOS_ABIERTOS)):
            avisos.append(f"{rid}: estado «{f.get('Estado')}» no reconocido.")

        if descartado:
            if nivel in {"A", "B", "C"}:
                avisos.append(f"{rid}: descartado con nivel {nivel}; usar `—`.")
        elif nivel not in {"A", "B", "C"}:
            avisos.append(f"{rid}: nivel «{f.get('Nivel', '')}» no es A, B ni C.")
        elif nivel in {"A", "B"} and not verificado:
            bloqueantes.append(f"{rid}: nivel {nivel} sin verificar (estado «{f.get('Estado', '')}»); la guía exige verificado para A y B.")

        fuentes = f.get("Fuentes", "")
        fecha_txt = f.get("Fecha", "").strip()
        fecha = None
        if fecha_txt and not es_desconocido(fecha_txt):
            try:
                fecha = dt.date.fromisoformat(fecha_txt[:10])
            except ValueError:
                avisos.append(f"{rid}: fecha «{fecha_txt}» ilegible (usar AAAA-MM-DD).")
        if verificado:
            if "http" not in fuentes and not dominios(fuentes):
                bloqueantes.append(f"{rid}: verificado sin URL en Fuentes.")
            if not fecha:
                bloqueantes.append(f"{rid}: verificado sin fecha de verificación.")
            elif (hoy - fecha).days > DIAS_VIGENCIA and not estado.startswith("contactado"):
                bloqueantes.append(f"{rid}: verificado hace {(hoy - fecha).days} días; volver a verificar antes de contactar.")

        texto_tipo = " ".join(palabras(f"{f.get('Tipo', '')} {f.get('Encaje', '')}"))
        if not descartado and re.search(r"\b(gato|gatos|felino|felinos|felina)\b", texto_tipo) and not re.search(r"\b(perro|perros|canino|canina)\b", texto_tipo):
            avisos.append(f"{rid}: parece negocio solo de gatos; la guía lo descarta.")

        coincidencia = None
        if "no es cliente" not in " ".join(palabras(f.get("Notas", ""))):
            coincidencia = exclusiones.revisar(f.get("Nombre", ""))
        if coincidencia and not descartado:
            if coincidencia[0] == "distribuidor":
                bloqueantes.append(f"{rid}: coincide con el distribuidor publicado «{coincidencia[1]}»; descartar o confirmar con Andrés.")
            else:
                bloqueantes.append(f"{rid}: coincide con un cliente del Excel de ventas; confirmar con Andrés y, si lo es, quitar el nombre del registro. Si no lo es, escribir `no es cliente` en Notas.")

        for clave in claves_duplicado(f):
            if clave in vistos and vistos[clave] != rid:
                bloqueantes.append(f"{rid}: posible duplicado de {vistos[clave]} (mismo {clave[0]}).")
                break
            vistos.setdefault(clave, rid)

        if nivel in {"A", "B"} and verificado and not descartado:
            listos.append(f)

    problemas_por_id = {p.split(":")[0] for p in bloqueantes}
    listos = [f for f in listos if f.get("ID", "").strip() not in problemas_por_id]

    niveles = Counter("descartado" if estado_de(f).startswith("descartado") else (f.get("Nivel", "").strip().upper() or "sin nivel") for f in registro.filas)
    estados = Counter(
        "descartado" if estado_de(f).startswith("descartado") else (estado_de(f) or "sin estado")
        for f in registro.filas
    )
    tipos = Counter((f.get("Tipo", "") or "desconocido").strip().lower() for f in registro.filas)
    localidades = Counter((f.get("Localidad", "") or "desconocido").strip() for f in registro.filas)

    lineas = [
        f"## Revisión de {registro.ruta}",
        "",
        f"- Negocios: {len(registro.filas)} · siguiente ID libre: **P{registro.siguiente_id():03d}**",
        "- Nivel: " + " · ".join(f"{k}: {niveles.get(k, 0)}" for k in ("A", "B", "C", "descartado")),
        "- Estado: " + (" · ".join(f"{k}: {v}" for k, v in estados.most_common()) or "—"),
        "- Tipo: " + (" · ".join(f"{k}: {v}" for k, v in tipos.most_common()) or "—"),
        "- Localidad: " + (" · ".join(f"{k}: {v}" for k, v in localidades.most_common()) or "—"),
        f"- A y B verificados sin problemas (listos para borrador o aprobación): {len(listos)}",
    ]
    if listos:
        lineas += ["", "| ID | Nombre | Nivel | Tipo | Localidad | Estado |", "|---|---|---|---|---|---|"]
        orden = sorted(listos, key=lambda f: (f.get("Nivel", ""), f.get("ID", "")))
        lineas += [fila_markdown([f.get(c, "") for c in ("ID", "Nombre", "Nivel", "Tipo", "Localidad", "Estado")]) for f in orden]
    lineas += ["", f"### Bloqueantes ({len(bloqueantes)})", ""]
    lineas += [f"- {p}" for p in bloqueantes] or ["- Ninguno."]
    lineas += ["", f"### Avisos ({len(avisos)})", ""]
    lineas += [f"- {p}" for p in avisos] or ["- Ninguno."]
    return "\n".join(lineas)


# ---------------------------------------------------------------- importar

def leer_lista(ruta: Path, hoja: str | None) -> list[dict]:
    if ruta.suffix.lower() in {".xlsx", ".xlsm"}:
        libro = cargar_openpyxl().load_workbook(ruta, read_only=True, data_only=True)
        ws = libro[hoja] if hoja else libro.worksheets[0]
        filas = [list(f) for f in ws.iter_rows(values_only=True)]
    else:
        filas = leer_csv(ruta)
    saltadas = 0  # títulos o filas vacías antes del encabezado
    while filas and sum(1 for v in filas[0] if celda(v)) < 2:
        filas.pop(0)
        saltadas += 1
    if not filas:
        return []
    claves = [ALIAS_IMPORTAR.get(clave_encabezado(h), clave_encabezado(h) or f"columna_{i}") for i, h in enumerate(filas[0])]
    registros = []
    for numero, fila in enumerate(filas[1:], start=saltadas + 2):
        valores = [celda(v) for v in fila]
        if not any(valores):
            continue
        dato: dict = {"_fila": numero}
        for clave, valor in zip(claves, valores):
            if valor and not dato.get(clave):
                dato[clave] = valor
        registros.append(dato)
    return registros


def importar(lista: Path, registro: Registro, exclusiones: Exclusiones, hoja: str | None, escribir: bool) -> str:
    if not registro.encabezado:
        return f"No encontré la tabla del registro en {registro.ruta}. Copia la plantilla assets/REGISTRO.md."
    datos = leer_lista(lista, hoja)
    vistos: dict[tuple, str] = {}
    for f in registro.filas:
        for clave in claves_duplicado(f):
            vistos.setdefault(clave, f.get("ID", ""))

    primero = siguiente = registro.siguiente_id()
    nuevas, duplicados, distribuidores, sin_nombre = [], [], [], []
    clientes = 0
    for d in datos:
        nombre = d.get("nombre", "")
        if not nombre:
            sin_nombre.append(d["_fila"])
            continue
        coincidencia = exclusiones.revisar(nombre)
        if coincidencia and coincidencia[0] == "cliente":
            clientes += 1
            continue
        if coincidencia:
            distribuidores.append(f"fila {d['_fila']} ({coincidencia[1]})")
            continue
        redes = [v for v in (d.get("web"), d.get("instagram"), d.get("facebook")) if v]
        canales = [v for v in (d.get("whatsapp"), d.get("telefono"), d.get("correo")) if v]
        localidad = d.get("localidad") or d.get("barrio") or "desconocido"
        encaje = "; ".join(v for v in (d.get("encaje"), f"marcas: {d['marcas']}" if d.get("marcas") else "") if v)
        fila = {
            "ID": f"P{siguiente:03d}",
            "Nombre": nombre,
            "Tipo": d.get("tipo") or "desconocido",
            "Localidad": localidad,
            "Web o redes": " · ".join(redes) or "desconocido",
            "Canal público": " · ".join(canales) or "desconocido",
            "Encaje": f"{encaje} (V)" if encaje else "desconocido",
            "Nivel": "C",
            "Estado": "por verificar",
            "Fuentes": f"importado de {lista.name}, fila {d['_fila']} (V)",
            "Fecha": "desconocido",
            "Notas": "",
        }
        repetido = next((vistos[c] for c in claves_duplicado(fila) if c in vistos), None)
        if repetido:
            duplicados.append(f"fila {d['_fila']} → {repetido}")
            continue
        for clave in claves_duplicado(fila):
            vistos.setdefault(clave, fila["ID"])
        nuevas.append(fila)
        siguiente += 1

    if escribir and nuevas:
        registro.agregar(nuevas)

    lineas = [
        f"## Importación de {lista.name}",
        "",
        f"- Filas leídas: {len(datos)} · nuevas: {len(nuevas)}"
        + (f" (P{primero:03d}–P{siguiente - 1:03d})" if nuevas else ""),
        f"- Omitidas por duplicado: {len(duplicados)}" + (f" ({'; '.join(duplicados[:15])}{'…' if len(duplicados) > 15 else ''})" if duplicados else ""),
        f"- Omitidas por distribuidor publicado: {len(distribuidores)}" + (f" ({'; '.join(distribuidores)})" if distribuidores else ""),
        f"- Omitidas por coincidir con un cliente del Excel de ventas: {clientes} (sin nombres)",
        f"- Sin nombre: {len(sin_nombre)}" + (f" (filas {', '.join(map(str, sin_nombre[:15]))})" if sin_nombre else ""),
        "- " + ("Filas agregadas a " + str(registro.ruta) if escribir else "Vista previa: agrega --escribir para guardarlas en el registro."),
    ]
    if nuevas and not escribir:
        columnas = [Registro._canonica(h) for h in registro.encabezado]
        lineas += ["", fila_markdown(columnas), fila_markdown(["---"] * len(columnas))]
        lineas += [fila_markdown([f.get(c, "") for c in columnas]) for f in nuevas]
    return "\n".join(lineas)


# ---------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="comando", required=True)

    comun = argparse.ArgumentParser(add_help=False)
    comun.add_argument("--excluir", type=Path, action="append", default=[],
                       help="Clientes actuales: .xlsx/.csv con columna CLIENTE o nombre, o .txt. Repetible.")
    comun.add_argument("--sin-distribuidores", action="store_true",
                       help="No comparar con assets/distribuidores_publicados.txt")

    p_rev = sub.add_parser("revisar", parents=[comun], help="Valida el registro")
    p_rev.add_argument("registro", type=Path)
    p_rev.add_argument("--hoy", type=dt.date.fromisoformat, default=dt.date.today())

    p_imp = sub.add_parser("importar", parents=[comun], help="Importa una lista CSV o XLSX")
    p_imp.add_argument("lista", type=Path)
    p_imp.add_argument("--registro", type=Path, required=True)
    p_imp.add_argument("--hoja", help="Hoja del XLSX (por defecto la primera)")
    p_imp.add_argument("--escribir", action="store_true", help="Agregar las filas al registro")

    args = parser.parse_args(argv)
    exclusiones = Exclusiones(args.excluir, usar_distribuidores=not args.sin_distribuidores)

    if args.comando == "revisar":
        if not args.registro.exists():
            parser.error(f"no existe {args.registro}; copia {PLANTILLA_REGISTRO}")
        print(revisar(Registro(args.registro), exclusiones, args.hoy))
    else:
        if not args.lista.exists():
            parser.error(f"no existe {args.lista}")
        if not args.registro.exists():
            if not args.escribir:
                parser.error(f"no existe {args.registro}; copia {PLANTILLA_REGISTRO} o usa --escribir para crearlo")
            args.registro.parent.mkdir(parents=True, exist_ok=True)
            args.registro.write_text(PLANTILLA_REGISTRO.read_text(encoding="utf-8"), encoding="utf-8")
        print(importar(args.lista, Registro(args.registro), exclusiones, args.hoja, args.escribir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
