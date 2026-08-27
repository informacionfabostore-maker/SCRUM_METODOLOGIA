"""
archivos.py

Módulo encargado de guardar y cargar información
del sistema utilizando archivos JSON.
"""

import json
import os

RUTA_DATOS = "../datos"


def cargar_datos(nombre_archivo):
    """
    Carga los datos de un archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.
    """

    ruta = os.path.join(RUTA_DATOS, nombre_archivo)

    if not os.path.exists(RUTA_DATOS):
        os.makedirs(RUTA_DATOS)

    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except (json.JSONDecodeError, IOError):
        return []


def guardar_datos(nombre_archivo, datos):
    """
    Guarda los datos en un archivo JSON.
    """

    ruta = os.path.join(RUTA_DATOS, nombre_archivo)

    if not os.path.exists(RUTA_DATOS):
        os.makedirs(RUTA_DATOS)

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        return True

    except IOError:
        return False