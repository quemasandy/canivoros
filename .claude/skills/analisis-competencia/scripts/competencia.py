#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Herramientas de la skill «analisis-competencia».

Subcomandos
  iniciar  Crea la carpeta de un análisis con las plantillas.
  precios  Precio por kg, por kg de materia seca y costo diario, con avisos.
  matriz   Matriz de perfil competitivo con cobertura de evidencia y sensibilidad.
  resenas  Temas y sentimientos de reseñas por marca: patrones vs. menciones aisladas.

Solo usa la biblioteca estándar de Python 3. Acepta CSV separados por coma,
punto y coma o tabulador (Excel en español suele exportar con punto y coma),
en UTF-8 o Windows-1252, y números en formato colombiano (45.900 · 1,5) o
internacional (45,900 · 1.5).

Ejemplos
  python3 competencia.py iniciar competencia/2026-11-03-precios-bogota
  python3 competencia.py precios observaciones.csv --propia "Canívoros" --hoy 2026-11-03
  python3 competencia.py matriz matriz.csv --propia "Canívoros"
  python3 competencia.py resenas resenas.csv --min-patron 3
"""

import argparse
import csv
import datetime as dt
import io
import re
import statistics
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"

TIPOS_EVIDENCIA = ("observado", "declarado", "terceros", "estimado", "hipotesis")
CERTEZAS = ("alta", "media", "baja")
VACIOS = {"", "na", "n_a", "nd", "n_d", "desconocido", "sin_dato", "no_aplica", "null", "none"}

ALIAS_PRECIOS = {
    "marca": "competidor",
    "peso": "peso_g",
    "peso_gramos": "peso_g",
    "precio": "precio_regular",
    "promocion": "precio_promocion",
    "precio_promo": "precio_promocion",
    "nivel_de_certeza": "certeza",
    "url": "fuente",
    "humedad": "humedad_pct",
    "racion": "racion_g_dia",
}
ALIAS_MATRIZ = {
    "marca": "competidor",
    "ponderacion": "peso",
    "puntaje": "puntuacion",
    "calificacion": "puntuacion",
}
ALIAS_RESENAS = {
    "marca": "competidor",
    "tema": "temas",
    "rating": "calificacion",
    "estrellas": "calificacion",
}

UNIDADES_PESO = {
    "g": 1.0, "gr": 1.0, "grs": 1.0, "gramo": 1.0, "gramos": 1.0,
    "kg": 1000.0, "kgs": 1000.0, "kilo": 1000.0, "kilos": 1000.0,
    "kilogramo": 1000.0, "kilogramos": 1000.0,
    "oz": 28.3495, "onza": 28.3495, "onzas": 28.3495,
    "lb": "libra", "lbs": "libra", "libra": "libra", "libras": "libra",
}


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #

def norm_key(texto):
    """Minúsculas, sin tildes y con guiones bajos: «Precio Regular» -> precio_regular."""
    t = unicodedata.normalize("NFKD", texto or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", t.lower()).strip("_")


def es_vacio(valor):
    v = (valor or "").strip()
    return v in ("", "-", "—", "?") or norm_key(v) in VACIOS


def leer_tabla(ruta, alias):
    """Lee un CSV y devuelve (columnas normalizadas, [(línea, fila)], delimitador)."""
    p = Path(ruta)
    if not p.exists():
        sys.exit(f"No existe el archivo: {ruta}")
    datos = p.read_bytes()
    try:
        texto = datos.decode("utf-8-sig")
    except UnicodeDecodeError:
        texto = datos.decode("cp1252")
    lineas = texto.splitlines()
    if not lineas:
        sys.exit(f"El archivo está vacío: {ruta}")
    cabecera = lineas[0]
    delim = max([",", ";", "\t"], key=cabecera.count)
    lector = csv.reader(io.StringIO(texto), delimiter=delim)
    encabezado = next(lector, None) or []
    claves = [norm_key(h) for h in encabezado]
    presentes = set(claves)
    claves = [alias[k] if k in alias and alias[k] not in presentes else k for k in claves]
    filas = []
    for registro in lector:
        linea = lector.line_num
        celdas = [c.strip() for c in registro]
        no_vacias = [c for c in celdas if c]
        if not no_vacias or no_vacias[0].startswith("#"):
            continue
        fila = {k: (celdas[i] if i < len(celdas) else "") for i, k in enumerate(claves) if k}
        if len(celdas) > len(claves) and any(celdas[len(claves):]):
            fila["__desfase__"] = (
                f"la fila tiene {len(celdas)} columnas y el encabezado {len(claves)}: probablemente un decimal "
                f"con coma sin comillas (p. ej. 1,5 kg). Escríbelo entre comillas, con punto o en gramos"
            )
        filas.append((linea, fila))
    return claves, filas, delim


def exigir_columnas(claves, requeridas, plantilla):
    faltan = [c for c in requeridas if c not in claves]
    if faltan:
        sys.exit(
            "Faltan columnas: " + ", ".join(faltan)
            + f". Usa la plantilla assets/{plantilla} como referencia."
        )


def parse_numero(valor):
    """Convierte '45.900', 'COP 45,900.50', '1,5', '20 %' en float. Vacío o 'desconocido' -> None."""
    if valor is None or es_vacio(str(valor)):
        return None
    t = re.sub(r"[^\d.,\-]", "", str(valor))
    if not re.search(r"\d", t):
        return None
    negativo = t.startswith("-")
    t = t.replace("-", "")
    if "." in t and "," in t:
        if t.rfind(",") > t.rfind("."):
            t = t.replace(".", "").replace(",", ".")
        else:
            t = t.replace(",", "")
    elif "," in t or "." in t:
        sep = "," if "," in t else "."
        partes = t.split(sep)
        miles = len(partes) > 2 or (len(partes[-1]) == 3 and partes[0] not in ("", "0"))
        t = t.replace(sep, "") if miles else t.replace(sep, ".")
    try:
        v = float(t)
    except ValueError:
        return None
    return -v if negativo else v


def parse_peso_g(valor, libra_g):
    """Devuelve (gramos | None, aviso | None). Número sin unidad = gramos. Acepta '3 x 500 g'."""
    crudo = (valor or "").strip()
    if es_vacio(crudo):
        return None, None
    txt = crudo.lower().replace("×", "x")
    multiplo = 1
    m_pack = re.match(r"^\s*(\d+)\s*x\s*(.+)$", txt)
    if m_pack:
        multiplo = int(m_pack.group(1))
        txt = m_pack.group(2)
    m = re.match(r"^\s*([\d.,]+)\s*([a-zñáéíóú]*)\.?\s*$", txt)
    if not m:
        return None, f"peso no reconocido «{crudo}»"
    cantidad = parse_numero(m.group(1))
    unidad = norm_key(m.group(2)) or "g"
    if cantidad is None:
        return None, f"peso no reconocido «{crudo}»"
    factor = UNIDADES_PESO.get(unidad)
    if factor is None:
        return None, f"unidad de peso desconocida «{m.group(2)}»"
    if factor == "libra":
        if libra_g is None:
            return None, (
                "peso en libras sin equivalencia: registra los gramos de la etiqueta "
                "o usa --libra-g 500 (uso comercial en Colombia) o 453.6 (libra internacional)"
            )
        factor = libra_g
    return cantidad * factor * multiplo, None


def parse_fecha(valor):
    crudo = (valor or "").strip()
    if not crudo:
        return None
    crudo = crudo.split()[0].split("T")[0]
    for formato in ("%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(crudo, formato).date()
        except ValueError:
            continue
    return None


def fmt_num(x, decimales=0):
    """Formato es-CO: miles con punto y decimales con coma."""
    if x is None:
        return "desconocido"
    s = f"{x:,.{decimales}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def fmt_dinero(x):
    if x is None:
        return "desconocido"
    return fmt_num(x, 0 if abs(x) >= 100 else 2)


def fmt_peso(gramos):
    if gramos is None:
        return "desconocido"
    if gramos >= 1000:
        kg = round(gramos / 1000, 2)
        texto = fmt_num(kg, 0 if kg == int(kg) else (1 if kg * 10 == int(kg * 10) else 2))
        return f"{texto} kg"
    return f"{fmt_num(gramos, 0 if gramos == int(gramos) else 1)} g"


def fmt_pct(x, decimales=0):
    return "desconocido" if x is None else f"{fmt_num(x * 100, decimales)} %"


def md(texto):
    return (texto or "").replace("|", "\\|").replace("\n", " ").strip()


def fuente_corta(fuente):
    f = (fuente or "").strip()
    if not f:
        return "—"
    if re.match(r"^https?://", f, re.I):
        host = urlparse(f).netloc.lower()
        return host[4:] if host.startswith("www.") else host
    return f if len(f) <= 32 else f[:31] + "…"


def tabla_md(encabezados, filas):
    salida = ["| " + " | ".join(encabezados) + " |",
              "|" + "|".join("---" for _ in encabezados) + "|"]
    for fila in filas:
        salida.append("| " + " | ".join(str(c) for c in fila) + " |")
    return "\n".join(salida)


def escribir_salida(texto, ruta):
    print(texto)
    if ruta:
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        Path(ruta).write_text(texto + "\n", encoding="utf-8")
        print(f"\n(Guardado en {ruta})", file=sys.stderr)


def fecha_referencia(valor):
    if not valor:
        return dt.date.today()
    f = parse_fecha(valor)
    if f is None:
        sys.exit("--hoy debe ser una fecha válida (AAAA-MM-DD)")
    return f


# --------------------------------------------------------------------------- #
# iniciar
# --------------------------------------------------------------------------- #

def cmd_iniciar(a):
    destino = Path(a.carpeta)
    destino.mkdir(parents=True, exist_ok=True)
    hoy = fecha_referencia(a.hoy)
    tema = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", destino.name).replace("-", " ").strip() or "competencia"
    plan = [
        ("observaciones.csv", "observaciones.csv"),
        ("matriz.csv", "matriz.csv"),
        ("resenas.csv", "resenas.csv"),
        ("plantilla-informe.md", "informe.md"),
    ]
    for origen, nombre in plan:
        objetivo = destino / nombre
        if objetivo.exists():
            print(f"Se conserva (ya existe): {objetivo}")
            continue
        contenido = (ASSETS / origen).read_text(encoding="utf-8")
        contenido = contenido.replace("{{FECHA}}", hoy.isoformat()).replace("{{TEMA}}", tema)
        objetivo.write_text(contenido, encoding="utf-8")
        print(f"Creado: {objetivo}")


# --------------------------------------------------------------------------- #
# precios
# --------------------------------------------------------------------------- #

def cmd_precios(a):
    claves, filas, delim = leer_tabla(a.csv, ALIAS_PRECIOS)
    exigir_columnas(claves, ["competidor", "producto", "peso_g", "precio_regular", "fecha", "fuente"],
                    "observaciones.csv")
    hoy = fecha_referencia(a.hoy)
    propia = norm_key(a.propia) if a.propia else None
    avisos, items, vistos = [], [], {}

    for linea, r in filas:
        etiqueta = f"{r.get('competidor') or '¿?'} · {r.get('producto') or '¿?'}"
        av = []

        bloqueos = []  # motivos por los que la fila no entra en comparaciones
        peso, aviso_peso = parse_peso_g(r.get("peso_g"), a.libra_g)
        if aviso_peso:
            av.append(aviso_peso)
        elif peso is None:
            av.append("sin peso: precio por kg desconocido")
        elif peso < 20:
            bloqueos.append(f"peso inusualmente bajo ({fmt_peso(peso)}): ¿estaba en kg? escribe la unidad, p. ej. «2 kg»")
        elif peso > 50000:
            bloqueos.append(f"peso inusualmente alto ({fmt_peso(peso)}): revisa separadores de miles y decimales")

        precio = parse_numero(r.get("precio_regular"))
        if precio is None:
            av.append("sin precio regular")
        promo = parse_numero(r.get("precio_promocion"))
        if promo is not None and precio is not None and promo >= precio:
            av.append("el precio de promoción no es menor que el regular")

        fecha = parse_fecha(r.get("fecha"))
        if not (r.get("fecha") or "").strip():
            bloqueos.append("sin fecha")
        elif fecha is None:
            bloqueos.append(f"fecha no reconocida «{r.get('fecha')}» (usa AAAA-MM-DD)")
        else:
            edad = (hoy - fecha).days
            if edad < 0:
                av.append("fecha posterior a la fecha de referencia")
            elif edad > a.max_dias:
                av.append(f"dato de hace {edad} días (máx. {a.max_dias}): verificar vigencia")

        if es_vacio(r.get("fuente")):
            bloqueos.append("sin fuente")
        av = bloqueos + av

        tipo = norm_key(r.get("tipo_evidencia", ""))
        if "tipo_evidencia" in claves:
            if not tipo:
                av.append("sin tipo_evidencia")
            elif tipo not in TIPOS_EVIDENCIA:
                av.append(f"tipo_evidencia «{r.get('tipo_evidencia')}» no válido (usa: {', '.join(TIPOS_EVIDENCIA)})")
        certeza = norm_key(r.get("certeza", ""))
        if certeza and certeza not in CERTEZAS:
            av.append(f"certeza «{r.get('certeza')}» no válida (usa: {', '.join(CERTEZAS)})")

        humedad = parse_numero(r.get("humedad_pct"))
        if humedad is not None and not (0 <= humedad < 100):
            av.append("humedad fuera de rango 0–100: se ignora")
            humedad = None

        racion = parse_numero(r.get("racion_g_dia"))
        fuente_racion = (r.get("fuente_racion") or "").strip()
        perfil = (r.get("perfil_racion") or "").strip()
        racion_valida = racion is not None and racion > 0 and bool(fuente_racion) and bool(perfil)
        if racion is not None and not fuente_racion:
            av.append("ración sin fuente: no se calcula costo diario")
        elif racion is not None and not perfil:
            av.append("ración sin perfil de mascota: no se calcula costo diario")

        if r.get("__desfase__"):
            # Columnas corridas: los demás valores no son confiables; solo se informa la causa.
            av = bloqueos = [r["__desfase__"]]
            peso = precio = promo = humedad = None
            racion_valida = False

        pkg = precio / peso * 1000 if (precio is not None and peso) else None
        pkg_promo = promo / peso * 1000 if (promo is not None and peso) else None
        pkg_ms = pkg / (1 - humedad / 100) if (pkg is not None and humedad is not None) else None
        costo_dia = pkg * racion / 1000 if (pkg is not None and racion_valida) else None

        clave_dup = (norm_key(r.get("competidor")), norm_key(r.get("producto")), peso,
                     norm_key(r.get("canal")), norm_key(r.get("vendedor")), fecha)
        if clave_dup in vistos:
            av.append(f"posible duplicado de la línea {vistos[clave_dup]}")
        else:
            vistos[clave_dup] = linea

        items.append({
            "linea": linea, "fila": r, "peso": peso, "precio": precio, "promo": promo,
            "pkg": pkg, "pkg_promo": pkg_promo, "pkg_ms": pkg_ms, "costo_dia": costo_dia,
            "racion": racion if racion_valida else None, "perfil": perfil, "fuente_racion": fuente_racion,
            "fecha": fecha, "moneda": (r.get("moneda") or "").strip().upper(),
            "propia": bool(propia) and norm_key(r.get("competidor")) == propia,
            "avisos": av, "comparable": not bloqueos and pkg is not None,
        })
        for m in av:
            avisos.append((linea, etiqueta, m + (" (fila fuera de las comparaciones)" if m in bloqueos else "")))

    monedas = sorted({i["moneda"] for i in items if i["moneda"]})
    generales = []
    if len(monedas) > 1:
        generales.append(f"Hay varias monedas ({', '.join(monedas)}): el script no convierte; compara solo dentro de cada moneda.")
    if any(not i["moneda"] for i in items):
        generales.append("Hay filas sin moneda: se asume que todas usan la misma.")
    if propia and not any(i["propia"] for i in items):
        generales.append(f"No hay filas de la marca propia «{a.propia}»: no se puede ubicar frente a la competencia.")

    salida = [f"# Comparación de precios",
              ""]
    fechas = [i["fecha"] for i in items if i["fecha"]]
    competidores = {norm_key(i["fila"].get("competidor")) for i in items}
    salida.append(
        f"Fecha de referencia: {hoy.isoformat()} · Filas: {len(items)} · Marcas: {len(competidores)} · "
        f"Datos entre {min(fechas).isoformat() if fechas else '—'} y {max(fechas).isoformat() if fechas else '—'} · "
        f"Moneda: {', '.join(monedas) if monedas else 'no indicada'}"
    )
    salida.append("")

    hay_promo = any(i["pkg_promo"] is not None for i in items)
    hay_ms = any(i["pkg_ms"] is not None for i in items)
    comparables = [i for i in items if i["comparable"]]
    excluidas = [i for i in items if not i["comparable"]]
    orden = sorted(comparables, key=lambda i: (i["moneda"], i["pkg"]))

    encabezados = ["#", "Marca", "Producto", "Categoría", "Peso", "Precio regular", "Precio/kg"]
    if hay_promo:
        encabezados.append("Precio/kg promo")
    if hay_ms:
        encabezados.append("Precio/kg materia seca*")
    encabezados += ["Canal · vendedor", "Fecha", "Fuente", "Evidencia · certeza", "Avisos"]
    filas_md = []
    for n, i in enumerate(orden, 1):
        r = i["fila"]
        marca = md(r.get("competidor"))
        if i["propia"]:
            marca = f"**{marca}**"
        canal = " · ".join(x for x in (md(r.get("canal")), md(r.get("vendedor"))) if x) or "—"
        evid = " · ".join(x for x in (md(r.get("tipo_evidencia")), md(r.get("certeza"))) if x) or "—"
        fila = [n, marca, md(r.get("producto")), md(r.get("categoria")) or "—", fmt_peso(i["peso"]),
                fmt_dinero(i["precio"]), fmt_dinero(i["pkg"])]
        if hay_promo:
            fila.append(fmt_dinero(i["pkg_promo"]) if i["pkg_promo"] is not None else "—")
        if hay_ms:
            fila.append(fmt_dinero(i["pkg_ms"]) if i["pkg_ms"] is not None else "—")
        fila += [canal, i["fecha"].isoformat() if i["fecha"] else "—", md(fuente_corta(r.get("fuente"))), evid,
                 f"línea {i['linea']}: {len(i['avisos'])}" if i["avisos"] else "—"]
        filas_md.append(fila)
    salida.append("## Precio por kg (de menor a mayor)")
    salida.append("")
    salida.append(tabla_md(encabezados, filas_md) if filas_md else "Ninguna fila tiene datos suficientes para comparar.")
    if hay_ms:
        salida.append("")
        salida.append("\\* Materia seca calculada con la humedad declarada (normalmente un máximo de etiqueta): "
                      "es una estimación para comparar productos de distinta humedad, no un costo de alimentación.")
    if excluidas:
        salida.append("")
        salida.append("### Filas fuera de la comparación")
        salida.append("")
        salida.append("Les falta peso, precio, fecha o fuente, o tienen un dato sospechoso. "
                      "Complétalas o corrígelas y vuelve a correr el script; no se rellenan con supuestos.")
        salida.append("")
        salida.append(tabla_md(
            ["Línea", "Marca", "Producto", "Peso", "Precio regular", "Motivo"],
            [[i["linea"], md(i["fila"].get("competidor")), md(i["fila"].get("producto")), fmt_peso(i["peso"]),
              fmt_dinero(i["precio"]), md("; ".join(i["avisos"]) or "sin precio por kg")] for i in excluidas]))
    salida.append("")

    # Resumen por categoría (sin la marca propia)
    grupos = {}
    for i in comparables:
        if i["propia"]:
            continue
        clave = (i["moneda"], (i["fila"].get("categoria") or "sin categoría").strip())
        grupos.setdefault(clave, []).append(i["pkg"])
    if grupos:
        salida.append("## Resumen por categoría" + (" (sin la marca propia)" if propia else ""))
        salida.append("")
        filas_cat = []
        for (moneda, cat), valores in sorted(grupos.items(), key=lambda kv: statistics.median(kv[1])):
            filas_cat.append([md(cat) + (f" ({moneda})" if len(monedas) > 1 else ""), len(valores),
                              fmt_dinero(min(valores)), fmt_dinero(statistics.median(valores)), fmt_dinero(max(valores))])
        salida.append(tabla_md(["Categoría", "n", "Mínimo/kg", "Mediana/kg", "Máximo/kg"], filas_cat))
        salida.append("")
        salida.append("Con pocas filas por categoría, la mediana describe la muestra levantada, no el mercado.")
        salida.append("")

    # Posición de la marca propia
    propias = [i for i in comparables if i["propia"]]
    if propias:
        salida.append(f"## Posición de {md(propias[0]['fila'].get('competidor'))}")
        salida.append("")
        for p in propias:
            mismos = [i for i in comparables if i["moneda"] == p["moneda"]]
            orden_pkg = sorted(mismos, key=lambda i: i["pkg"])
            puesto = orden_pkg.index(p) + 1
            texto = (f"- **{md(p['fila'].get('producto'))}** ({fmt_peso(p['peso'])}): {fmt_dinero(p['pkg'])}/kg, "
                     f"puesto {puesto} de {len(orden_pkg)} (1 = más barato por kg)")
            cat = (p["fila"].get("categoria") or "sin categoría").strip()
            pares = grupos.get((p["moneda"], cat), [])
            if pares:
                mediana = statistics.median(pares)
                dif = p["pkg"] / mediana - 1
                lado = "por encima" if dif >= 0 else "por debajo"
                texto += f"; {fmt_pct(abs(dif))} {lado} de la mediana de «{md(cat)}» ({fmt_dinero(mediana)}/kg, n={len(pares)})"
            salida.append(texto + ".")
        salida.append("")

    # Costo diario
    salida.append("## Costo diario (solo con ración documentada)")
    salida.append("")
    con_racion = [i for i in comparables if i["costo_dia"] is not None]
    if not con_racion:
        salida.append("No hay raciones documentadas con fuente y perfil de mascota: no se calcula costo diario. "
                      "El precio por kg no equivale al costo de alimentar, porque cada producto tiene su propia ración.")
        salida.append("")
    else:
        perfiles = {}
        for i in con_racion:
            perfiles.setdefault(i["perfil"], []).append(i)
        for perfil, lista in perfiles.items():
            salida.append(f"### Perfil: {md(perfil)}")
            salida.append("")
            lista.sort(key=lambda i: i["costo_dia"])
            salida.append(tabla_md(
                ["Marca", "Producto", "Ración g/día", "Fuente de la ración", "Costo diario", "Costo 30 días"],
                [[("**%s**" % md(i["fila"].get("competidor"))) if i["propia"] else md(i["fila"].get("competidor")),
                  md(i["fila"].get("producto")), fmt_num(i["racion"], 0), md(fuente_corta(i["fuente_racion"])),
                  fmt_dinero(i["costo_dia"]), fmt_dinero(i["costo_dia"] * 30)] for i in lista]))
            salida.append("")
        if len(perfiles) > 1:
            salida.append("Compara costos diarios solo dentro de un mismo perfil de mascota.")
            salida.append("")

    # Avisos
    salida.append("## Avisos")
    salida.append("")
    if not avisos and not generales:
        salida.append("Sin avisos.")
    for g in generales:
        salida.append(f"- {g}")
    for linea, etiqueta, m in avisos:
        salida.append(f"- Línea {linea} ({md(etiqueta)}): {m}")

    escribir_salida("\n".join(salida), a.guardar)

    if a.salida:
        dec = "," if delim == ";" else "."

        def num_csv(x):
            if x is None:
                return ""
            s = f"{x:.0f}" if abs(x) >= 100 else f"{x:.2f}"
            return s.replace(".", dec)

        columnas = [k for k in claves if k]
        extra = ["peso_g_normalizado", "precio_kg_regular", "precio_kg_promocion",
                 "precio_kg_materia_seca", "costo_diario", "avisos"]
        with open(a.salida, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter=delim)
            w.writerow(columnas + extra)
            for i in items:
                w.writerow([i["fila"].get(k, "") for k in columnas] + [
                    num_csv(i["peso"]), num_csv(i["pkg"]), num_csv(i["pkg_promo"]),
                    num_csv(i["pkg_ms"]), num_csv(i["costo_dia"]), " | ".join(i["avisos"])])
        print(f"(CSV normalizado en {a.salida})", file=sys.stderr)


# --------------------------------------------------------------------------- #
# matriz
# --------------------------------------------------------------------------- #

def cmd_matriz(a):
    claves, filas, _ = leer_tabla(a.csv, ALIAS_MATRIZ)
    exigir_columnas(claves, ["factor", "peso", "competidor", "puntuacion"], "matriz.csv")
    escala = a.escala
    propia = norm_key(a.propia) if a.propia else None
    factores, competidores, pesos, celdas, avisos = [], [], {}, {}, []

    for linea, r in filas:
        f, c = (r.get("factor") or "").strip(), (r.get("competidor") or "").strip()
        if r.get("__desfase__"):
            avisos.append(f"Línea {linea}: {r['__desfase__']}; se ignora.")
            continue
        if not f or not c:
            avisos.append(f"Línea {linea}: fila sin factor o sin competidor; se ignora.")
            continue
        if f not in factores:
            factores.append(f)
        if c not in competidores:
            competidores.append(c)
        p = parse_numero(r.get("peso"))
        if p is not None:
            if f in pesos and abs(pesos[f] - p) > 1e-9:
                avisos.append(f"Línea {linea}: peso distinto para «{f}»; se usa el primero ({fmt_num(pesos[f], 2)}).")
            pesos.setdefault(f, p)
        if (f, c) in celdas:
            avisos.append(f"Línea {linea}: puntuación repetida de «{c}» en «{f}»; se usa la primera.")
            continue
        s = parse_numero(r.get("puntuacion"))
        evidencia = (r.get("evidencia") or "").strip()
        if s is None:
            celdas[(f, c)] = None
            continue
        if s != int(s) or not 1 <= s <= escala:
            avisos.append(f"Línea {linea}: puntuación «{r.get('puntuacion')}» fuera de la escala 1–{escala}; se ignora.")
            celdas[(f, c)] = None
            continue
        if not evidencia:
            avisos.append(f"Línea {linea}: «{c}» en «{f}» tiene puntuación sin evidencia.")
        celdas[(f, c)] = int(s)

    sin_peso = [f for f in factores if f not in pesos]
    for f in sin_peso:
        avisos.append(f"El factor «{f}» no tiene peso: queda fuera del total.")
    factores_validos = [f for f in factores if f in pesos]
    if not factores_validos:
        sys.exit("Ningún factor tiene peso: no se puede calcular la matriz.")
    total = sum(pesos[f] for f in factores_validos)
    if total > 1.5:
        avisos.append(f"Los pesos suman {fmt_num(total, 1)}: se interpretan como porcentajes.")
        for f in factores_validos:
            pesos[f] /= 100
        total = sum(pesos[f] for f in factores_validos)
    if abs(total - 1) > 0.01:
        avisos.append(f"Los pesos suman {fmt_num(total, 2)} y no 1,00: se normalizan para que sumen 1.")
        for f in factores_validos:
            pesos[f] /= total

    def totales(w):
        res = {}
        for c in competidores:
            suma = cobertura = 0.0
            for f in factores_validos:
                s = celdas.get((f, c))
                if s is not None:
                    suma += w[f] * s
                    cobertura += w[f]
            res[c] = (suma, cobertura)
        return res

    res = totales(pesos)
    completos = [c for c in competidores if res[c][1] >= 0.999]
    ranking = sorted(completos, key=lambda c: -res[c][0])

    salida = ["# Matriz de perfil competitivo", ""]
    if escala == 4:
        salida.append("Escala 1–4: 1 = debilidad mayor, 2 = debilidad menor, 3 = fortaleza menor, 4 = fortaleza mayor. "
                      "Celda: puntuación · ponderado.")
    else:
        salida.append(f"Escala 1–{escala} (mayor es mejor). Celda: puntuación · ponderado.")
    salida.append("")

    def nombre(c):
        return f"**{md(c)}**" if propia and norm_key(c) == propia else md(c)

    filas_md = []
    for f in factores_validos:
        fila = [md(f), fmt_num(pesos[f], 2)]
        for c in competidores:
            s = celdas.get((f, c))
            fila.append("sin dato" if s is None else f"{s} · {fmt_num(pesos[f] * s, 2)}")
        filas_md.append(fila)
    filas_md.append(["**Total ponderado**", "1,00"] +
                    [f"**{fmt_num(res[c][0], 2)}**" if c in completos else f"{fmt_num(res[c][0], 2)} (incompleto)"
                     for c in competidores])
    filas_md.append(["Cobertura del peso", ""] + [fmt_pct(res[c][1]) for c in competidores])
    salida.append(tabla_md(["Factor", "Peso"] + [nombre(c) for c in competidores], filas_md))
    salida.append("")

    salida.append("## Ranking")
    salida.append("")
    if ranking:
        for n, c in enumerate(ranking, 1):
            salida.append(f"{n}. {nombre(c)}: {fmt_num(res[c][0], 2)}")
    incompletos = [c for c in competidores if c not in completos]
    if incompletos:
        salida.append("")
        salida.append("Fuera del ranking por falta de datos (no se rellenan con supuestos): "
                      + ", ".join(f"{md(c)} ({fmt_pct(res[c][1])} del peso)" for c in incompletos) + ".")
    salida.append("")

    umbral = 0.05 * (escala - 1)
    if len(ranking) >= 2:
        margen = res[ranking[0]][0] - res[ranking[1]][0]
        salida.append("## Robustez")
        salida.append("")
        if margen < umbral:
            salida.append(f"- Empate práctico: {md(ranking[0])} supera a {md(ranking[1])} por {fmt_num(margen, 2)} "
                          f"(menos de {fmt_num(umbral, 2)}). Con puntuaciones subjetivas, esa diferencia no es concluyente.")
        else:
            salida.append(f"- {md(ranking[0])} supera a {md(ranking[1])} por {fmt_num(margen, 2)}.")
        iguales = {f: 1 / len(factores_validos) for f in factores_validos}
        res_eq = totales(iguales)
        ranking_eq = sorted(completos, key=lambda c: -res_eq[c][0])
        if ranking_eq[0] != ranking[0]:
            salida.append(f"- Con pesos iguales el primer lugar cambia a {md(ranking_eq[0])}: la conclusión depende de "
                          "los pesos. Justifica los pesos con evidencia de compradores antes de usarla.")
        elif ranking_eq != ranking:
            salida.append("- Con pesos iguales el primer lugar se mantiene, pero cambia el orden del resto: "
                          + " > ".join(md(c) for c in ranking_eq) + ".")
        else:
            salida.append("- Con pesos iguales el orden no cambia.")
        salida.append("")

    if propia:
        nombres_propios = [c for c in competidores if norm_key(c) == propia]
        if not nombres_propios:
            avisos.append(f"No hay filas de la marca propia «{a.propia}».")
        else:
            yo = nombres_propios[0]
            brechas, ventajas = [], []
            for f in factores_validos:
                mia = celdas.get((f, yo))
                otros = [(celdas.get((f, c)), c) for c in competidores if c != yo and celdas.get((f, c)) is not None]
                if mia is None or not otros:
                    continue
                mejor, quien = max(otros)
                if mejor - mia >= 1:
                    brechas.append((pesos[f] * (mejor - mia), f, mia, mejor, quien))
                elif mia > mejor:
                    ventajas.append((f, mia, mejor))
            salida.append(f"## Brechas y ventajas de {md(yo)}")
            salida.append("")
            if brechas:
                brechas.sort(reverse=True)
                salida.append(tabla_md(
                    ["Factor", "Peso", f"{md(yo)}", "Mejor competidor", "Brecha ponderada"],
                    [[md(f), fmt_num(pesos[f], 2), mia, f"{mejor} ({md(quien)})", fmt_num(b, 2)]
                     for b, f, mia, mejor, quien in brechas]))
                salida.append("")
                salida.append("Las brechas con mayor peso son candidatas a mejora o a prueba comercial, "
                              "si la evidencia de la puntuación es sólida.")
            else:
                salida.append("Sin brechas de 1 punto o más frente al mejor competidor en cada factor.")
            if ventajas:
                salida.append("")
                salida.append("Ventajas (puntuación mayor que la de cualquier competidor): "
                              + "; ".join(f"{md(f)} ({mia} vs {mejor})" for f, mia, mejor in ventajas) + ".")
            salida.append("")

    salida.append("## Avisos")
    salida.append("")
    if avisos:
        salida.extend(f"- {m}" for m in avisos)
    else:
        salida.append("Sin avisos.")
    escribir_salida("\n".join(salida), a.guardar)


# --------------------------------------------------------------------------- #
# resenas
# --------------------------------------------------------------------------- #

SENTIMIENTOS = {
    "positivo": "pos", "positiva": "pos", "pos": "pos", "+": "pos",
    "negativo": "neg", "negativa": "neg", "neg": "neg", "-": "neg",
    "neutro": "neu", "neutra": "neu", "neu": "neu", "0": "neu",
    "mixto": "mix", "mixta": "mix", "mix": "mix", "+-": "mix",
}


def parse_sentimiento(valor):
    crudo = (valor or "").strip().lower()
    if crudo in SENTIMIENTOS:
        return SENTIMIENTOS[crudo]
    return SENTIMIENTOS.get(norm_key(crudo))


def cmd_resenas(a):
    claves, filas, _ = leer_tabla(a.csv, ALIAS_RESENAS)
    exigir_columnas(claves, ["competidor", "temas", "sentimiento"], "resenas.csv")
    hoy = fecha_referencia(a.hoy)
    propia = norm_key(a.propia) if a.propia else None
    avisos, marcas = [], {}

    for linea, r in filas:
        c = (r.get("competidor") or "").strip()
        if r.get("__desfase__"):
            avisos.append(f"Línea {linea}: {r['__desfase__']}; se ignora.")
            continue
        if not c:
            avisos.append(f"Línea {linea}: reseña sin competidor; se ignora.")
            continue
        m = marcas.setdefault(c, {"n": 0, "fuentes": set(), "fechas": [], "notas": [], "temas": {}, "antiguas": 0})
        m["n"] += 1
        if r.get("fuente"):
            m["fuentes"].add(r["fuente"].strip())
        f = parse_fecha(r.get("fecha"))
        if f:
            m["fechas"].append(f)
            if (hoy - f).days > a.max_dias:
                m["antiguas"] += 1
        elif (r.get("fecha") or "").strip():
            avisos.append(f"Línea {linea}: fecha no reconocida «{r.get('fecha')}».")
        nota = parse_numero(r.get("calificacion"))
        if nota is not None:
            m["notas"].append(nota)
        sent_fila = parse_sentimiento(r.get("sentimiento"))
        temas = [t.strip() for t in re.split(r"[|;,]", r.get("temas") or "") if t.strip()]
        if not temas:
            avisos.append(f"Línea {linea}: reseña sin temas codificados.")
        vistos = set()
        for t in temas:
            nombre_tema, sent = t, sent_fila
            if ":" in t:
                nombre_tema, s = t.rsplit(":", 1)
                sent = parse_sentimiento(s) or sent_fila
            clave = norm_key(nombre_tema)
            if not clave:
                continue
            if sent is None:
                avisos.append(f"Línea {linea}: sentimiento no reconocido para «{nombre_tema.strip()}» "
                              "(usa positivo, negativo, neutro o mixto).")
                sent = "neu"
            tema = m["temas"].setdefault(clave, {"nombre": nombre_tema.strip(), "pos": 0, "neg": 0, "neu": 0, "mix": 0,
                                                  "resenas": 0})
            tema[sent] += 1
            if clave not in vistos:
                tema["resenas"] += 1
                vistos.add(clave)

    if not marcas:
        sys.exit("No hay reseñas para analizar.")

    k = a.min_patron

    def lectura(t):
        if t["neg"] >= k and t["pos"] >= k:
            return "patrón dividido"
        if t["neg"] >= k:
            return "patrón negativo"
        if t["pos"] >= k:
            return "patrón positivo"
        if t["resenas"] >= k:
            return "patrón mixto"
        return "aislado: hipótesis"

    def nombre(c):
        return f"**{md(c)}**" if propia and norm_key(c) == propia else md(c)

    salida = ["# Reseñas por tema", "",
              f"Umbral de patrón: {k} o más menciones. Las reseñas son experiencias declaradas por clientes; "
              "describen percepciones, no prueban efectos del producto.", "", "## Muestra", ""]
    filas_m = []
    for c, m in marcas.items():
        filas_m.append([nombre(c), m["n"], md(", ".join(sorted(fuente_corta(x) for x in m["fuentes"]))) or "—",
                        min(m["fechas"]).isoformat() if m["fechas"] else "—",
                        max(m["fechas"]).isoformat() if m["fechas"] else "—",
                        fmt_num(statistics.mean(m["notas"]), 1) if m["notas"] else "—"])
        if m["n"] < a.min_muestra:
            avisos.append(f"{c}: solo {m['n']} reseñas (menos de {a.min_muestra}); úsalas para formular hipótesis, no para concluir.")
        if m["antiguas"]:
            plural = "reseñas tienen" if m["antiguas"] > 1 else "reseña tiene"
            avisos.append(f"{c}: {m['antiguas']} {plural} más de {a.max_dias} días; puede no reflejar la oferta actual.")
    salida.append(tabla_md(["Marca", "Reseñas", "Fuentes", "Desde", "Hasta", "Calificación media"], filas_m))
    salida.append("")
    salida.append("## Temas por marca")
    salida.append("")
    negativos = {}
    for c, m in marcas.items():
        salida.append(f"### {nombre(c)} (n = {m['n']})")
        salida.append("")
        temas = sorted(m["temas"].values(), key=lambda t: (-t["resenas"], t["nombre"]))
        salida.append(tabla_md(
            ["Tema", "Positivas", "Negativas", "Neutras/mixtas", "% de reseñas", "Lectura"],
            [[md(t["nombre"]), t["pos"], t["neg"], t["neu"] + t["mix"], fmt_pct(t["resenas"] / m["n"]), lectura(t)]
             for t in temas]))
        salida.append("")
        for clave, t in m["temas"].items():
            if t["neg"] >= k:
                negativos.setdefault(clave, {"nombre": t["nombre"], "marcas": [], "menciones": 0})
                negativos[clave]["marcas"].append(c)
                negativos[clave]["menciones"] += t["neg"]

    salida.append("## Problemas repetidos en varias marcas")
    salida.append("")
    comunes = [v for v in negativos.values() if len(v["marcas"]) >= 2]
    if comunes:
        comunes.sort(key=lambda v: (-len(v["marcas"]), -v["menciones"]))
        salida.append(tabla_md(["Tema", "Marcas con patrón negativo", "Menciones negativas"],
                               [[md(v["nombre"]), ", ".join(md(x) for x in v["marcas"]), v["menciones"]] for v in comunes]))
        salida.append("")
        salida.append("Un problema que se repite en varias marcas puede ser una necesidad mal resuelta de la categoría: "
                      "es oportunidad solo si podemos resolverla y demostrarlo. Conviértelo en una prueba comercial.")
    else:
        salida.append("Ningún tema negativo alcanza el umbral de patrón en dos o más marcas.")
    salida.append("")
    salida.append("## Avisos")
    salida.append("")
    if avisos:
        salida.extend(f"- {m}" for m in avisos)
    else:
        salida.append("Sin avisos.")
    escribir_salida("\n".join(salida), a.guardar)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv=None):
    p = argparse.ArgumentParser(
        description="Herramientas de la skill analisis-competencia.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    sub = p.add_subparsers(dest="comando", required=True)

    s = sub.add_parser("iniciar", help="crea la carpeta de un análisis con las plantillas")
    s.add_argument("carpeta", help="p. ej. competencia/2026-11-03-precios-bogota")
    s.add_argument("--hoy", help="fecha del informe (AAAA-MM-DD); por defecto, hoy")
    s.set_defaults(func=cmd_iniciar)

    s = sub.add_parser("precios", help="precio por kg, materia seca y costo diario con avisos")
    s.add_argument("csv", help="observaciones.csv")
    s.add_argument("--propia", help="nombre de la marca propia para ubicarla frente a las demás")
    s.add_argument("--hoy", help="fecha de referencia (AAAA-MM-DD); por defecto, hoy")
    s.add_argument("--max-dias", type=int, default=60, help="antigüedad máxima de un precio antes de avisar (60)")
    s.add_argument("--libra-g", type=float, default=None,
                   help="gramos por libra; sin este valor las filas en libras quedan sin precio por kg")
    s.add_argument("--salida", help="ruta de un CSV con las columnas calculadas")
    s.add_argument("--guardar", help="ruta donde guardar el informe en Markdown")
    s.set_defaults(func=cmd_precios)

    s = sub.add_parser("matriz", help="matriz de perfil competitivo")
    s.add_argument("csv", help="matriz.csv (formato largo: factor, peso, competidor, puntuacion, evidencia)")
    s.add_argument("--escala", type=int, default=4, help="puntuación máxima (4 por defecto; 5 si usas 1–5)")
    s.add_argument("--propia", help="nombre de la marca propia para calcular brechas")
    s.add_argument("--guardar", help="ruta donde guardar el informe en Markdown")
    s.set_defaults(func=cmd_matriz)

    s = sub.add_parser("resenas", help="temas y sentimientos de reseñas por marca")
    s.add_argument("csv", help="resenas.csv")
    s.add_argument("--min-patron", type=int, default=3, help="menciones para considerar un patrón (3)")
    s.add_argument("--min-muestra", type=int, default=10, help="reseñas por marca por debajo de las cuales avisa (10)")
    s.add_argument("--max-dias", type=int, default=365, help="antigüedad a partir de la cual avisa (365)")
    s.add_argument("--hoy", help="fecha de referencia (AAAA-MM-DD); por defecto, hoy")
    s.add_argument("--propia", help="nombre de la marca propia para resaltarla")
    s.add_argument("--guardar", help="ruta donde guardar el informe en Markdown")
    s.set_defaults(func=cmd_resenas)

    a = p.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
