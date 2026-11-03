#!/usr/bin/env python3
"""Calculadora de embudo de ventas.

Calcula volúmenes por etapa, costo por etapa (CPL, costo por lead calificado,
CAC), economía unitaria (contribución, LTV, ROAS de equilibrio) y escenarios.

Dos modos:
  - "meta":    parte de una meta de clientes (o de ingresos) y calcula hacia atrás
               cuánto volumen hace falta en cada etapa.
  - "volumen": parte del volumen de la primera etapa (alcance, visitas, contactos)
               y calcula hacia adelante cuántos clientes resultan.

Uso:
  python calcular_embudo.py config.json [--mermaid] [--escenarios] [--salida reporte.md]
  python calcular_embudo.py --ejemplo > config.json

Solo usa la biblioteca estándar de Python 3.
"""

import argparse
import json
import math
import sys

EJEMPLO = {
    "nombre": "Embudo conversacional por WhatsApp (ejemplo)",
    "moneda": "COP",
    "modo": "meta",
    "meta_clientes": 60,
    "volumen_inicial": None,
    "etapas": [
        {"nombre": "Personas alcanzadas por anuncios"},
        {"nombre": "Clics a WhatsApp", "tasa": 0.012, "fuente": "supuesto"},
        {"nombre": "Conversaciones iniciadas", "tasa": "60%", "fuente": "supuesto"},
        {"nombre": "Leads calificados", "tasa": 0.5, "fuente": "supuesto"},
        {"nombre": "Primera compra", "tasa": 0.3, "fuente": "supuesto"},
    ],
    "costo_medios": {"etapa": "Personas alcanzadas por anuncios", "por_unidad": 15},
    "economia": {
        "precio": 95000,
        "costo_variable": 57000,
        "compras_por_cliente": 3,
        "horizonte": "12 meses",
        "otros_costos_adquisicion": 0,
    },
}

FACTORES_ESCENARIO = [("Pesimista (tasas x0,7)", 0.7), ("Base", 1.0), ("Optimista (tasas x1,3)", 1.3)]


# ---------------------------------------------------------------- formato
def num(valor, dec=0):
    """Número con formato es-CO: punto para miles y coma para decimales."""
    if valor is None:
        return "—"
    if isinstance(valor, float) and (math.isinf(valor) or math.isnan(valor)):
        return "—"
    texto = f"{valor:,.{dec}f}"
    return texto.replace(",", "§").replace(".", ",").replace("§", ".")


def dinero(valor, moneda):
    return "—" if valor is None else f"{moneda} {num(valor)}"


def pct(valor, dec=1):
    return "—" if valor is None else f"{num(valor * 100, dec)} %"


# ---------------------------------------------------------------- lectura
def leer_tasa(valor, etapa):
    if isinstance(valor, str):
        texto = valor.strip().replace(",", ".")
        if texto.endswith("%"):
            tasa = float(texto[:-1]) / 100
        else:
            tasa = float(texto)
    elif isinstance(valor, (int, float)):
        tasa = float(valor)
    else:
        raise ValueError(f"La etapa '{etapa}' no tiene una tasa válida (usa 0.35 o \"35%\").")
    if not 0 < tasa <= 1:
        raise ValueError(
            f"La tasa de '{etapa}' es {valor}: debe estar entre 0 y 1 (o entre 0% y 100%). "
            "Si querías un porcentaje, escríbelo como texto: \"35%\"."
        )
    return tasa


def normalizar(config):
    """Permite indicar volúmenes observados por etapa (útil para auditar).

    En modo "volumen", una etapa puede traer "volumen" en lugar de "tasa": la tasa se
    calcula como volumen de la etapa ÷ volumen de la etapa anterior y se marca como dato.
    """
    etapas = config.get("etapas") or []
    if config.get("modo", "meta") != "volumen" or not any("volumen" in e for e in etapas):
        return config
    config = dict(config)
    nuevas = []
    previo = config.get("volumen_inicial") or etapas[0].get("volumen")
    if previo is None:
        raise ValueError("Indica 'volumen_inicial' o el 'volumen' de la primera etapa.")
    config["volumen_inicial"] = previo
    for i, etapa in enumerate(etapas):
        etapa = dict(etapa)
        if i > 0 and "volumen" in etapa and "tasa" not in etapa:
            if not previo:
                raise ValueError(f"La etapa anterior a '{etapa['nombre']}' tiene volumen 0.")
            etapa["tasa"] = etapa["volumen"] / previo
            etapa.setdefault("fuente", "dato")
        if i == 0:
            etapa.setdefault("fuente", "dato" if "volumen" in etapa else "")
        previo = etapa.get("volumen", previo * etapa["tasa"] if i > 0 else previo)
        nuevas.append(etapa)
    config["etapas"] = nuevas
    return config


def cargar(config):
    etapas = config.get("etapas") or []
    if len(etapas) < 2:
        raise ValueError("Se necesitan al menos dos etapas: la entrada y una conversión.")
    nombres = [e["nombre"] for e in etapas]
    tasas = [None] + [leer_tasa(e.get("tasa"), e["nombre"]) for e in etapas[1:]]
    fuentes = [etapas[0].get("fuente", "")] + [e.get("fuente", "supuesto") for e in etapas[1:]]
    return nombres, tasas, fuentes


# ---------------------------------------------------------------- cálculo
def volumenes(config, tasas):
    modo = config.get("modo", "meta")
    economia = config.get("economia") or {}
    if modo == "volumen":
        inicial = config.get("volumen_inicial")
        if not inicial:
            raise ValueError("En modo 'volumen' indica 'volumen_inicial'.")
        vols = [float(inicial)]
        for tasa in tasas[1:]:
            vols.append(vols[-1] * tasa)
        return vols
    if modo == "meta":
        meta = config.get("meta_clientes")
        if not meta and config.get("meta_ingresos"):
            precio = economia.get("precio")
            if not precio:
                raise ValueError("Para usar 'meta_ingresos' indica economia.precio.")
            meta = math.ceil(config["meta_ingresos"] / precio)
        if not meta:
            raise ValueError("En modo 'meta' indica 'meta_clientes' o 'meta_ingresos'.")
        vols = [float(meta)]
        for tasa in reversed(tasas[1:]):
            vols.insert(0, vols[0] / tasa)
        return vols
    raise ValueError("'modo' debe ser 'meta' o 'volumen'.")


def costo_medios(config, nombres, vols):
    costo = config.get("costo_medios") or {}
    if "total" in costo:
        return float(costo["total"])
    if "por_unidad" in costo:
        etapa = costo.get("etapa", nombres[0])
        if etapa not in nombres:
            raise ValueError(f"costo_medios.etapa '{etapa}' no coincide con ninguna etapa.")
        return vols[nombres.index(etapa)] * float(costo["por_unidad"])
    return None


def calcular(config, factor=1.0):
    config = normalizar(config)
    nombres, tasas, fuentes = cargar(config)
    if factor != 1.0:
        tasas = [None] + [min(1.0, t * factor) for t in tasas[1:]]
    vols = volumenes(config, tasas)
    if config.get("modo", "meta") == "meta":
        # Se necesita al menos ese volumen: redondear hacia arriba.
        vols = [math.ceil(v - 1e-9) for v in vols]
    medios = costo_medios(config, nombres, vols)
    eco = config.get("economia") or {}
    otros = float(eco.get("otros_costos_adquisicion", 0) or 0)
    costo_total = None if medios is None else medios + otros
    clientes = vols[-1]

    res = {
        "nombres": nombres,
        "tasas": tasas,
        "fuentes": fuentes,
        "vols": vols,
        "medios": medios,
        "otros": otros,
        "costo_total": costo_total,
        "clientes": clientes,
        "tasa_global": clientes / vols[0] if vols[0] else None,
    }

    precio = eco.get("precio")
    costo_var = eco.get("costo_variable")
    compras = float(eco.get("compras_por_cliente", 1) or 1)
    if precio is not None and costo_var is not None:
        contrib = float(precio) - float(costo_var)
        margen = contrib / float(precio) if precio else None
        ltv = contrib * compras
        cac = costo_total / clientes if (costo_total is not None and clientes) else None
        res.update(
            {
                "precio": float(precio),
                "contrib": contrib,
                "margen": margen,
                "compras": compras,
                "ltv": ltv,
                "cac": cac,
                "ingresos_1": clientes * float(precio),
                "resultado_1": None if costo_total is None else clientes * contrib - costo_total,
                "resultado_h": None if costo_total is None else clientes * ltv - costo_total,
                "roas_1": (clientes * float(precio) / medios) if medios else None,
                "roas_eq": (1 / margen) if margen and margen > 0 else None,
                "ltv_cac": (ltv / cac) if cac else None,
                "compras_recuperar": (cac / contrib) if (cac and contrib > 0) else None,
            }
        )
    return res


# ---------------------------------------------------------------- salida
def reporte(config, res, con_mermaid=False, con_escenarios=False):
    moneda = config.get("moneda", "")
    modo = config.get("modo", "meta")
    eco = config.get("economia") or {}
    lineas = [f"## Números del embudo: {config.get('nombre', 'sin nombre')}", ""]
    if modo == "meta":
        lineas.append(
            f"Modo **meta**: volumen mínimo por etapa para conseguir **{num(res['clientes'])}** clientes."
        )
    else:
        lineas.append(
            f"Modo **volumen**: resultado esperado a partir de **{num(res['vols'][0])}** en la primera etapa."
        )
    lineas += ["", "| Etapa | Tasa desde la etapa anterior | Volumen | Costo por unidad | Fuente de la tasa |",
               "|---|---:|---:|---:|---|"]
    for i, nombre in enumerate(res["nombres"]):
        tasa = "—" if i == 0 else pct(res["tasas"][i])
        v = res["vols"][i]
        dec = 0 if (modo == "meta" or v >= 100 or abs(v - round(v)) < 1e-6) else 1
        vol = num(res["vols"][i], dec)
        if res["costo_total"] is not None and res["vols"][i]:
            costo_u = dinero(res["costo_total"] / res["vols"][i], moneda)
        else:
            costo_u = "—"
        fuente = res["fuentes"][i] or ("—" if i == 0 else "supuesto")
        lineas.append(f"| {nombre} | {tasa} | {vol} | {costo_u} | {fuente} |")
    lineas += ["", f"Conversión global (primera → última etapa): **{pct(res['tasa_global'], 3)}**."]

    supuestos = [n for n, f in zip(res["nombres"][1:], res["fuentes"][1:]) if (f or "supuesto") != "dato"]
    if supuestos:
        lineas.append(
            f"Tasas marcadas como supuesto: {len(supuestos)} de {len(res['nombres']) - 1}. "
            "Reemplázalas con datos propios tras 2–4 semanas de medición."
        )

    if res["costo_total"] is not None:
        lineas += ["", "### Inversión de adquisición", "",
                   f"- Medios: {dinero(res['medios'], moneda)}"]
        if res["otros"]:
            lineas.append(f"- Otros costos de adquisición: {dinero(res['otros'], moneda)}")
        lineas.append(f"- Total: **{dinero(res['costo_total'], moneda)}**")

    if "contrib" in res:
        horizonte = eco.get("horizonte", "el horizonte definido")
        lineas += ["", "### Economía unitaria", "", "| Indicador | Valor | Cómo leerlo |", "|---|---:|---|"]
        filas = [
            ("Contribución por compra", dinero(res["contrib"], moneda), "Precio − costos variables de cada venta"),
            ("Margen de contribución", pct(res["margen"]), "Parte del precio que queda para pagar adquisición y fijos"),
            ("CAC (costo por cliente nuevo)", dinero(res.get("cac"), moneda), "Inversión total ÷ clientes nuevos"),
            ("CAC máximo para no perder en la 1.ª compra", dinero(res["contrib"], moneda), "Si el CAC lo supera, la primera venta da pérdida"),
            (f"LTV de contribución ({num(res['compras'], 1)} compras en {horizonte})", dinero(res["ltv"], moneda), "CAC máximo si se cumple la recompra supuesta"),
            ("Relación LTV / CAC", "—" if res.get("ltv_cac") is None else f"{num(res['ltv_cac'], 2)}", "Regla práctica común: ≥ 3 es sano; < 1 pierde dinero"),
            ("Compras para recuperar el CAC", "—" if res.get("compras_recuperar") is None else num(res["compras_recuperar"], 2), "Cuántas compras de cada cliente pagan su adquisición"),
            ("Ingresos de primera compra", dinero(res["ingresos_1"], moneda), "Clientes × precio"),
            ("ROAS de primera compra", "—" if res.get("roas_1") is None else f"{num(res['roas_1'], 2)}x", "Ingresos 1.ª compra ÷ inversión en medios"),
            ("ROAS de equilibrio (1.ª compra)", "—" if res.get("roas_eq") is None else f"{num(res['roas_eq'], 2)}x", "1 ÷ margen de contribución"),
            ("Resultado de la primera compra", dinero(res.get("resultado_1"), moneda), "Contribución − inversión de adquisición"),
        ]
        if res["compras"] > 1:
            filas.append((f"Resultado en {horizonte}", dinero(res.get("resultado_h"), moneda), "Incluye la recompra supuesta"))
        for f in filas:
            lineas.append(f"| {f[0]} | {f[1]} | {f[2]} |")
        if res["contrib"] <= 0:
            lineas += ["", "> **Alerta:** la contribución por compra es cero o negativa; ningún embudo lo compensa. Revisa precio y costos antes de invertir en tráfico."]
        elif res.get("cac") is not None and res["cac"] > res["contrib"]:
            if res["compras"] <= 1:
                lineas += ["", "> **Alerta:** el CAC supera la contribución de la primera compra y no se supuso recompra: "
                           "cada cliente nuevo genera pérdida. Mejora conversión o ticket, o diseña la recompra, antes de escalar la inversión."]
            elif res["ltv_cac"] < 1:
                lineas += ["", "> **Alerta:** con estos supuestos cada cliente cuesta más de lo que deja, incluso con recompra. "
                           "Mejora conversión, ticket o recompra antes de escalar."]
            else:
                lineas += ["", f"> **Ojo:** la primera compra no paga el CAC; la rentabilidad depende de que cada cliente "
                           f"compre al menos {num(res['compras_recuperar'], 1)} veces. Mide la recompra real antes de escalar."]

    if con_escenarios:
        lineas += ["", "### Escenarios (todas las tasas multiplicadas por un factor)", "",
                   "Las variaciones se multiplican entre etapas: con "
                   f"{len(res['nombres']) - 1} conversiones, un 30 % peor en cada paso deja el "
                   f"{pct(0.7 ** (len(res['nombres']) - 1), 0)} de los clientes.", ""]
        if modo == "meta":
            lineas += [f"| Escenario | Volumen necesario en «{res['nombres'][0]}» | Inversión total | CAC |",
                       "|---|---:|---:|---:|"]
        else:
            lineas += ["| Escenario | Clientes | Inversión total | CAC | Resultado 1.ª compra |", "|---|---:|---:|---:|---:|"]
        for etiqueta, factor in FACTORES_ESCENARIO:
            r = calcular(config, factor)
            cac = dinero(r.get("cac"), moneda) if "cac" in r else "—"
            if modo == "meta":
                lineas.append(f"| {etiqueta} | {num(r['vols'][0])} | {dinero(r['costo_total'], moneda)} | {cac} |")
            else:
                lineas.append(
                    f"| {etiqueta} | {num(r['clientes'], 1)} | {dinero(r['costo_total'], moneda)} | {cac} | "
                    f"{dinero(r.get('resultado_1'), moneda)} |"
                )

    if con_mermaid:
        lineas += ["", "### Diagrama", "", "```mermaid", "flowchart TD"]
        for i, nombre in enumerate(res["nombres"]):
            etiqueta = nombre.replace('"', "'")
            lineas.append(f'    E{i}["{etiqueta}<br/>{num(res["vols"][i])}"]')
        for i in range(1, len(res["nombres"])):
            lineas.append(f'    E{i-1} -->|"{pct(res["tasas"][i])}"| E{i}')
        lineas.append("```")

    return "\n".join(lineas) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculadora de embudo de ventas")
    parser.add_argument("config", nargs="?", help="Archivo JSON con etapas, tasas y economía")
    parser.add_argument("--mermaid", action="store_true", help="Incluir diagrama Mermaid")
    parser.add_argument("--escenarios", action="store_true", help="Incluir escenarios pesimista/base/optimista")
    parser.add_argument("--salida", help="Guardar el reporte en este archivo .md")
    parser.add_argument("--ejemplo", action="store_true", help="Imprimir una configuración de ejemplo")
    args = parser.parse_args(argv)

    if args.ejemplo:
        print(json.dumps(EJEMPLO, ensure_ascii=False, indent=2))
        return 0
    if not args.config:
        parser.error("indica el archivo de configuración o usa --ejemplo")

    with open(args.config, encoding="utf-8") as f:
        config = json.load(f)
    try:
        res = calcular(config)
        texto = reporte(config, res, args.mermaid, args.escenarios)
    except (ValueError, KeyError) as exc:
        print(f"Error en la configuración: {exc}", file=sys.stderr)
        return 1

    if args.salida:
        with open(args.salida, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Reporte guardado en {args.salida}")
    else:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
