import tempfile
from pathlib import Path

from lectores import leer_pedido


def probar_formatos():
    """Comprueba que los tres lectores funcionan correctamente."""

    with tempfile.TemporaryDirectory() as temporal:
        carpeta = Path(temporal)

        # Prueba TXT
        txt = carpeta / "prueba.txt"
        txt.write_text(
            "pedido: 1001\nsede: Itagui\nvalor: 25000\n",
            encoding="utf-8"
        )
        datos = leer_pedido(txt)
        assert datos["pedido"] == "1001"
        assert datos["sede"] == "Itagui"

        # Prueba CSV
        csv = carpeta / "prueba.csv"
        csv.write_text(
            "pedido,sede,valor\n1002,Envigado,30000\n",
            encoding="utf-8"
        )
        datos = leer_pedido(csv)
        assert datos["pedido"] == "1002"
        assert datos["valor"] == "30000"

        # Prueba JSON
        json = carpeta / "prueba.json"
        json.write_text(
            '{"pedido": "1003", "sede": "Sabaneta"}',
            encoding="utf-8"
        )
        datos = leer_pedido(json)
        assert datos["pedido"] == "1003"
        assert datos["sede"] == "Sabaneta"

        # Prueba JSON vacío
        vacio = carpeta / "vacio.json"
        vacio.write_text("", encoding="utf-8")

        datos = leer_pedido(vacio)
        assert datos == {}

        # Prueba JSON malformado
        danado = carpeta / "danado.json"
        danado.write_text("{json incorrecto}", encoding="utf-8")

        try:
            leer_pedido(danado)
            raise AssertionError("Debió detectar el JSON dañado")
        except ValueError as error:
            assert "JSON" in type(error).__name__


        # Prueba extensión no admitida
        otro = carpeta / "prueba.xml"
        otro.write_text("<pedido/>", encoding="utf-8")

        try:
            leer_pedido(otro)
            raise AssertionError("Debió rechazar el formato XML")
        except ValueError as error:
            assert "Formato no compatible" in str(error)

    print("PRUEBAS AUTOMÁTICAS: TODAS APROBADAS")


def revisar_bandeja():
    """Revisa los archivos reales sin modificarlos."""

    carpeta = Path(__file__).parent / "bandeja_entrada"

    if not carpeta.is_dir():
        print(f"No se encontró la bandeja: {carpeta}")
        return

    leidos = 0
    vacios = 0
    errores = 0
    ignorados = 0

    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue

        if archivo.suffix.lower() not in (".txt", ".csv", ".json"):
            ignorados += 1
            continue

        try:
            pedido = leer_pedido(archivo)

            if not pedido:
                vacios += 1
            else:
                leidos += 1

        except (ValueError, OSError, UnicodeError) as error:
            errores += 1
            print(f"Error en {archivo.name}: {error}")

    print("\nRESUMEN DE LA BANDEJA")
    print(f"Pedidos con datos leídos: {leidos}")
    print(f"Archivos sin datos:       {vacios}")
    print(f"Archivos con errores:     {errores}")
    print(f"Archivos ignorados:       {ignorados}")
    print("La bandeja original no se modificó.")


if __name__ == "__main__":
    probar_formatos()
    revisar_bandeja()
