def mostrar_menu() -> None:
    """Muestra por pantalla las opciones del menú principal.

    Returns:
        None
    """
    print()
    print("\n" + "═" * 45)
    print("         MENÚ DE EGRESADOS - UTN FRA")
    print("═" * 45)
    print(" 1) Cargar alumnos")
    print(" 2) Mostrar egresados por plan")
    print(" 3) Mostrar egresados anteriores al año 2000")
    print(" 4) Buscar alumno por nombre o apellido")
    print(" 5) Salón de la fama")
    print(" 6) Salir")
    print("═" * 45)
    print()


def mostrar_alumno(alumno: dict) -> bool:
    """Muestra por pantalla los datos de un alumno.

    Args:
        alumno (dict): Diccionario con los datos del alumno
        (legajo, nombre, apellido, egreso, plan, nota_promedio).

    Returns:
        bool: True si el alumno se mostró correctamente, False si el
        parámetro no es un diccionario.
    """
    retorno = False
    if type(alumno) == dict:
        print("┌" + "─" * 38 + "┐")
        print(f"│ Legajo:         {alumno['legajo']}")
        print(f"│ Nombre:         {alumno['nombre']}")
        print(f"│ Apellido:       {alumno['apellido']}")
        print(f"│ Año de egreso:  {alumno['egreso']}")
        print(f"│ Plan:           {alumno['plan']}")
        print(f"│ Promedio:       {alumno['nota_promedio']}")
        print("└" + "─" * 38 + "┘")
        retorno = True
        
    return retorno


def mostrar_lista_alumnos(lista_alumnos: list) -> bool:
    """Muestra por pantalla todos los alumnos de una lista, o un aviso si está vacía.

    Args:
        lista_alumnos (list): Lista de diccionarios con datos de alumnos.

    Returns:
        bool: True si se mostró al menos un alumno, False si la lista
        está vacía o si el parámetro es inválido.
    """
    retorno = False
    
    if type(lista_alumnos) == list:
        print("\n" + "═" * 45)

        if len(lista_alumnos) == 0:
            print(" No se encontraron alumnos.")
        else:
            print(f" Se encontraron {len(lista_alumnos)} alumno(s)")
            print("═" * 45)

            for alumno in lista_alumnos:
                mostrar_alumno(alumno)

            retorno = True

        print("═" * 45)
            
    return retorno


def mostrar_mensaje(mensaje: str) -> bool:
    """Muestra un mensaje genérico por pantalla.

    Args:
        mensaje (str): Texto a mostrar.

    Returns:
        bool: True si el mensaje se mostró correctamente, False si el
        parámetro no es una cadena.
    """
    retorno = False
    
    if type(mensaje) == str:
        print("\n" + "═" * 45)
        print(f" {mensaje}")
        print("═" * 45 + "\n")
        retorno = True
        
    return retorno