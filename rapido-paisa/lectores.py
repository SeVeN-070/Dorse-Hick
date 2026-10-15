
import json
import csv
from pathlib import Path


def leer_txt(ruta):
    """Lee un pedido en formato TXT y devuelve sus datos."""
    pedido = {}

    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        for linea in archivo:
            if ":" in linea:
                clave, valor = linea.split(":", 1)
                pedido[clave.strip()] = valor.strip()

    return pedido


def leer_csv(ruta):
    """Lee un pedido en formato CSV y devuelve sus datos."""
    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)

        if not filas:
            return {}

        return filas[0]


def leer_json(ruta):
    """Lee un pedido JSON y maneja archivos vacíos."""
    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        contenido = archivo.read()

    # Un archivo vacío o con solo espacios no contiene datos.
    if not contenido.strip():
        return {}

    # Si el JSON tiene errores de sintaxis, se informa al programa
    # que lo llama mediante la excepción JSONDecodeError.
    return json.loads(contenido)


def leer_pedido(ruta):
    """Identifica el formato y llama al lector correspondiente."""
    ruta = Path(ruta)

    if not ruta.is_file():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ruta}"
        )

    extension = ruta.suffix.lower()

    if extension == ".txt":
        return leer_txt(ruta)

    elif extension == ".csv":
        return leer_csv(ruta)

    elif extension == ".json":
        return leer_json(ruta)

    else:
        raise ValueError(f"Formato no compatible: {extension}")
