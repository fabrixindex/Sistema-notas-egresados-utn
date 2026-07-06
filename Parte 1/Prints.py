def imprimir_menu() -> None:
    """Muestra el menú principal de opciones.

    Returns:
        None
    """
    print("\n===== MENÚ DE NOTAS =====\n")
    print("1 - Cargar notas")
    print("2 - Mostrar alumnos desaprobados")
    print("3 - Mostrar alumnos con aplazos")
    print("4 - Mostrar porcentaje de aprobados y desaprobados")
    print("5 - Mostrar trimestre con mejor promedio")
    print("6 - Salir")
    print()


def imprimir_menu_carga() -> None:
    """Muestra el submenú de tipo de carga de datos.

    Returns:
        None
    """
    print("===== CARGA DE DATOS =====\n")
    print("a - Carga secuencial")
    print("b - Carga desde archivo CSV")
    print()


def imprimir_error_opcion() -> None:
    """Muestra un mensaje de error ante una opción inválida.

    Returns:
        None
    """
    print()
    print("Opción inválida.\n")


def imprimir_datos_no_cargados() -> None:
    """Indica al usuario que primero debe cargar los datos antes de usar esa opción.

    Returns:
        None
    """
    print()
    print("Primero debe cargar las notas (opción 1).\n")


def imprimir_carga_exitosa() -> None:
    """Indica que la carga de datos fue exitosa.

    Returns:
        None
    """
    print()
    print("Datos cargados correctamente.\n")


def imprimir_error_archivo() -> None:
    """Indica que el archivo no existe o no pudo cargarse.

    Returns:
        None
    """
    print()
    print("No se pudo cargar el archivo. Verifique que exista.\n")


def imprimir_despedida() -> None:
    """Muestra el mensaje de salida del programa.

    Returns:
        None
    """
    print("\nSaliendo...")
    print("\n¡Gracias por usar el sistema!\n")