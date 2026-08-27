"""
main.py

Punto de entrada del Sistema de Préstamo de Equipos Tecnológicos.

MVP actual:
HU01 - Registrar equipos.
HU02 - Consultar equipos.
"""

from equipos import registrar_equipo, listar_equipos


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print("\n==========================================")
    print(" SISTEMA DE PRÉSTAMO DE EQUIPOS")
    print("==========================================")
    print("1. Registrar equipo")
    print("2. Consultar equipos")
    print("0. Salir")
    print("==========================================")


def main():
    """
    Ejecuta el menú principal.
    """

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            listar_equipos()

        elif opcion == "0":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
