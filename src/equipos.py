"""
equipos.py - Gestión de equipos tecnológicos
"""

ARCHIVO_EQUIPOS = "equipos.txt"
ESTADOS_EQUIPO = ["Disponible", "Prestado"]


def crear_equipo(codigo, tipo, marca, modelo, estado="Disponible"):
    """Crea estructura de un equipo."""
    return {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado
    }


def validar_equipo(codigo, tipo, marca, modelo):
    """Valida los datos del equipo."""
    if not codigo or not tipo or not marca or not modelo:
        return False, "Todos los campos son obligatorios."
    if len(codigo.strip()) < 2:
        return False, "El código debe tener al menos 2 caracteres."
    return True, ""


def cargar_datos(archivo):
    """Carga equipos del archivo."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        return lineas
    except FileNotFoundError:
        return []


def guardar_datos(archivo, equipo_texto):
    """Guarda equipos en el archivo."""
    try:
        with open(archivo, 'a', encoding='utf-8') as f:
            f.write(equipo_texto + "\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def registrar_equipo():
    """Registra un equipo tecnológico."""
    print("\n--- REGISTRAR EQUIPO ---")

    codigo = input("Código del equipo: ").strip()
    tipo = input("Tipo de equipo: ").strip()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    # Validar
    es_valido, mensaje = validar_equipo(codigo, tipo, marca, modelo)
    if not es_valido:
        print(f"❌ {mensaje}")
        return False

    # Crear equipo
    equipo = crear_equipo(codigo, tipo, marca, modelo)
    
    # Guardar como texto
    equipo_texto = f"{codigo}|{tipo}|{marca}|{modelo}|Disponible"

    if guardar_datos(ARCHIVO_EQUIPOS, equipo_texto):
        print("✓ Equipo registrado correctamente.")
        return True
    else:
        print("✗ Error al guardar.")
        return False