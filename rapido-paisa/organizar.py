
from pathlib import Path
from shutil import copy2


def organizar_pedidos(obtener_sede):
    entrada = Path("bandeja_entrada")
    salida = Path("pedidos_ordenados")

    if not entrada.is_dir():
        print("Error: no existe la carpeta bandeja_entrada.")
        return

    salida.mkdir(parents=True, exist_ok=True)

    organizados = 0
    sin_clasificar = 0

    for archivo in entrada.iterdir():
        if not archivo.is_file():
            continue

        sede = obtener_sede(archivo)

        if not sede:
            print(f"No se pudo identificar la sede: {archivo.name}")
            sin_clasificar += 1
            continue

        carpeta_sede = salida / sede
        carpeta_sede.mkdir(parents=True, exist_ok=True)

        destino = carpeta_sede / archivo.name
        copy2(archivo, destino)

        organizados += 1
        print(f"Copiado: {archivo.name} -> {sede}")

    print(f"Pedidos organizados: {organizados}")
    print(f"Pedidos sin clasificar: {sin_clasificar}")
