"""
equipos.py

Módulo de gestión de equipos tecnológicos.

HU01: Registrar equipos tecnológicos.
SB01: Preparar estructura de datos de equipos.
"""

ESTADOS_EQUIPO = ["Disponible", "Prestado"]


def crear_equipo(codigo, tipo, marca, modelo):
    """
    Crea y devuelve la estructura de datos de un equipo.

    SB01:
    La estructura contiene:
    - codigo
    - tipo
    - marca
    - modelo
    - estado
    """

    equipo = {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": "Disponible"
    }

    return equipo
