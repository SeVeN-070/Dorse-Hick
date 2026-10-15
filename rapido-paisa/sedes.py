# sedes.py - Módulo para normalizar sedes de Rápido Paisa

SEDES_VALIDAS = {
    "Itagui": ["itagui", "itagüí", "itagüi", "itagui "],
    "Envigado": ["envigado", "env", "envigado "],
    "Sabaneta": ["sabaneta", "sabaneta."]
}

def obtener_sede_normalizada(texto_sede):
    """Recibe el texto de la sede y devuelve el nombre estandarizado."""
    if not texto_sede:
        return None

    limpio = texto_sede.strip().lower()
    for sede, variaciones in SEDES_VALIDAS.items():
        if limpio in variaciones or limpio == sede.lower():
            return sede
    return None