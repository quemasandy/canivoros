#!/usr/bin/env python3
"""Crea la carpeta de un embudo nuevo dentro de embudos/ y lo registra en EMBUDOS.md.

Uso (desde la raíz del proyecto):
  python3 .claude/skills/embudos-de-venta/scripts/nuevo_embudo.py "Canívoros WhatsApp recompra" \
      --negocio Canívoros --tipo "WhatsApp + recompra" --objetivo "60 clientes nuevos/mes"

Crea embudos/E01-canivoros-whatsapp-recompra/ con embudo.md (plantilla) y calculo.json
(entradas de la calculadora), y agrega una fila a embudos/EMBUDOS.md. No sobrescribe nada:
si ya existe un embudo con el mismo nombre, avisa y no crea otro.

Solo usa la biblioteca estándar de Python 3.
"""

import argparse
import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
PLANTILLA = SKILL / "assets" / "plantilla-embudo.md"
REGISTRO_BASE = SKILL / "assets" / "EMBUDOS.md"

CALCULO_INICIAL = {
    "_ayuda": (
        "Completa las tasas de cada etapa (0.35 o \"35%\") y marca 'fuente' como 'dato' o 'supuesto'. "
        "modo 'meta' usa meta_clientes o meta_ingresos; modo 'volumen' usa volumen_inicial o el 'volumen' "
        "observado de cada etapa. Deja precio y costo_variable en null si son desconocidos: "
        "el reporte calcula volúmenes y omite el dinero. costo_medios: {\"total\": N} o "
        "{\"etapa\": \"<nombre>\", \"por_unidad\": N}."
    ),
    "nombre": "",
    "moneda": "COP",
    "modo": "meta",
    "meta_clientes": None,
    "etapas": [
        {"nombre": "Conversaciones iniciadas", "fuente": "supuesto"},
        {"nombre": "Leads calificados", "tasa": None, "fuente": "supuesto"},
        {"nombre": "Reciben oferta", "tasa": None, "fuente": "supuesto"},
        {"nombre": "Primera compra", "tasa": None, "fuente": "supuesto"},
    ],
    "costo_medios": {},
    "economia": {
        "precio": None,
        "costo_variable": None,
        "compras_por_cliente": 1,
        "horizonte": "12 meses",
        "otros_costos_adquisicion": 0,
    },
}


def slug(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    texto = re.sub(r"[^a-zA-Z0-9]+", "-", texto.lower()).strip("-")
    return texto or "embudo"


def siguiente_id(carpeta, registro):
    usados = [0]
    if registro.exists():
        usados += [int(n) for n in re.findall(r"^\|\s*E(\d+)\s*\|", registro.read_text(encoding="utf-8"), re.M)]
    usados += [int(m.group(1)) for p in carpeta.iterdir() if p.is_dir() and (m := re.match(r"E(\d+)-", p.name))]
    return f"E{max(usados) + 1:02d}"


def celda(texto):
    return (texto or "").replace("|", "/").replace("\n", " ").strip()


def registrar(registro, fila):
    lineas = registro.read_text(encoding="utf-8").splitlines()
    separador = next((i for i, l in enumerate(lineas) if re.match(r"^\|\s*-{3,}", l)), None)
    if separador is None:
        lineas += ["", fila]
    else:
        fin = separador
        while fin + 1 < len(lineas) and lineas[fin + 1].startswith("|"):
            fin += 1
        lineas.insert(fin + 1, fila)
    registro.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Crea y registra un embudo nuevo")
    parser.add_argument("nombre", help="Nombre corto: negocio y tipo, p. ej. 'Canívoros WhatsApp recompra'")
    parser.add_argument("--negocio", default="", help="Negocio o cliente")
    parser.add_argument("--tipo", default="", help="Tipo de embudo, p. ej. 'WhatsApp + recompra'")
    parser.add_argument("--objetivo", default="", help="Meta concreta y plazo")
    parser.add_argument("--carpeta", default="embudos", help="Carpeta de resultados (por defecto: embudos)")
    parser.add_argument("--fecha", default=datetime.date.today().isoformat(), help="AAAA-MM-DD")
    args = parser.parse_args(argv)

    carpeta = Path(args.carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)
    registro = carpeta / "EMBUDOS.md"
    if not registro.exists():
        registro.write_text(REGISTRO_BASE.read_text(encoding="utf-8"), encoding="utf-8")

    nombre_slug = slug(args.nombre)
    existentes = [p for p in carpeta.iterdir() if p.is_dir() and re.fullmatch(rf"E\d+-{re.escape(nombre_slug)}", p.name)]
    if existentes:
        print(f"Ya existe {existentes[0]}: actualiza ese embudo y anota el cambio en su «Historial».", file=sys.stderr)
        return 2

    ident = siguiente_id(carpeta, registro)
    destino = carpeta / f"{ident}-{nombre_slug}"
    destino.mkdir()

    texto = PLANTILLA.read_text(encoding="utf-8")
    for clave, valor in {"{{ID}}": ident, "{{NOMBRE}}": args.nombre, "{{FECHA}}": args.fecha}.items():
        texto = texto.replace(clave, valor)
    (destino / "embudo.md").write_text(texto, encoding="utf-8")

    calculo = dict(CALCULO_INICIAL, nombre=f"{ident} · {args.nombre}")
    (destino / "calculo.json").write_text(json.dumps(calculo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    fila = (
        f"| {ident} | {celda(args.nombre)} | {celda(args.negocio)} | {celda(args.tipo)} | "
        f"{celda(args.objetivo)} | borrador | [{destino.name}/]({destino.name}/) | {args.fecha} | {args.fecha} |"
    )
    registrar(registro, fila)

    print(f"Embudo {ident} creado en {destino}/")
    print(f"  - {destino / 'embudo.md'}")
    print(f"  - {destino / 'calculo.json'}")
    print(f"  - registrado en {registro}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
