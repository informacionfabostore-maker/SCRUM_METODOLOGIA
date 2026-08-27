"""
equipos.py - Gestión de equipos tecnológicos
Cubre HU01 - Registrar equipos tecnológicos
"""

from archivos import cargar_datos, guardar_datos

ARCHIVO_EQUIPOS = "equipos.json"


def crear_equipo(codigo, tipo, marca, modelo, estado="Disponible"):
    """Crea la estructura de un equipo."""
    return {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado
    }


def validar_equipo(codigo, tipo, marca, modelo):
    """Valida los datos obligatorios del equipo."""

    if not codigo or not tipo or not marca or not modelo:
        return False, "Todos los campos son obligatorios."

    if len(codigo.strip()) < 2:
        return False, "El código debe tener al menos 2 caracteres."

    return True, ""


def registrar_equipo():
    """
    HU01 - Registrar equipo tecnológico.
    SB02 + SB03
    """

    print("\n--- REGISTRAR EQUIPO ---")

    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    codigo = input("Código del equipo: ").strip()
    tipo = input("Tipo de equipo: ").strip()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    # Validar campos
    valido, mensaje = validar_equipo(
        codigo,
        tipo,
        marca,
        modelo
    )

    if not valido:
        print(f"Error: {mensaje}")
        return

    # Validar código único
    for equipo in equipos:
        if equipo["codigo"].lower() == codigo.lower():
            print("Error: ya existe un equipo con ese código.")
            return

    # Crear equipo
    nuevo_equipo = crear_equipo(
        codigo,
        tipo,
        marca,
        modelo
    )

    # Agregar equipo a la lista
    equipos.append(nuevo_equipo)

    # Guardar información
    if guardar_datos(ARCHIVO_EQUIPOS, equipos):
        print("Equipo registrado correctamente.")
    else:
        print("Error: no se pudo guardar el equipo.")
    
def listar_equipos():
    """
    SB04 - Consulta los equipos registrados
    y muestra su disponibilidad.
    """

    print("\n--- EQUIPOS REGISTRADOS ---")

    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    if not equipos:
        print("No hay equipos registrados.")
        return

    print(
        f"{'Código':<12}"
        f"{'Tipo':<15}"
        f"{'Marca':<15}"
        f"{'Modelo':<15}"
        f"{'Estado':<15}"
    )

    print("-" * 72)

    for equipo in equipos:
        print(
            f"{equipo['codigo']:<12}"
            f"{equipo['tipo']:<15}"
            f"{equipo['marca']:<15}"
            f"{equipo['modelo']:<15}"
            f"{equipo['estado']:<15}"
        )


def consultar_por_estado():
    """
    SB05 - Consultar equipos según su estado.
    Permite visualizar los equipos disponibles o prestados.
    """

    print("\n--- CONSULTAR EQUIPOS POR ESTADO ---")

    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    if not equipos:
        print("No hay equipos registrados.")
        return

    estado = input(
        "Ingrese el estado a consultar "
        "(Disponible/Prestado): "
    ).strip().lower()

    if estado not in ["disponible", "prestado"]:
        print("Error: estado no válido.")
        return

    encontrados = []

    for equipo in equipos:
        if equipo["estado"].lower() == estado:
            encontrados.append(equipo)

    if not encontrados:
        print(f"No hay equipos con estado '{estado.capitalize()}'.")
        return

    print(
        f"\n{'Código':<12}"
        f"{'Tipo':<15}"
        f"{'Marca':<15}"
        f"{'Modelo':<15}"
        f"{'Estado':<15}"
    )

    print("-" * 72)

    for equipo in encontrados:
        print(
            f"{equipo['codigo']:<12}"
            f"{equipo['tipo']:<15}"
            f"{equipo['marca']:<15}"
            f"{equipo['modelo']:<15}"
            f"{equipo['estado']:<15}"
        )