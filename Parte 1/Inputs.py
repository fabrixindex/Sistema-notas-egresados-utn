from Funciones import *

CANTIDAD_ALUMNOS    = 7
CANTIDAD_TRIMESTRES = 3


def pedir_nota(mensaje: str) -> int:
    """Solicita una nota por teclado y valida que sea un entero entre 1 y 10.
    Repite la solicitud hasta recibir un valor válido.

    Args:
        mensaje (str): Texto que se muestra para solicitar el dato.

    Returns:
        int: Nota ingresada por el usuario, validada entre 1 y 10.
    """
    retorno     = -1
    nota_valida = False
    while nota_valida == False:
        entrada = input(mensaje)
        if es_entero_valido(entrada) == True:
            nota = texto_a_entero(entrada)
            if nota >= 1 and nota <= 10:
                retorno     = nota
                nota_valida = True
            else:
                print("La nota debe estar entre 1 y 10. Intente nuevamente.\n")
        else:
            print("Debe ingresar un número entero. Intente nuevamente.\n")
    return retorno


def cargar_secuencial() -> list:
    """Carga la matriz de notas pidiendo los datos por teclado (7 alumnos x 3 trimestres).
    Valida cada nota entre 1 y 10.

    Returns:
        list: Matriz con las notas cargadas, una fila por alumno.
    """
    retorno = []
    for fil in range(CANTIDAD_ALUMNOS):
        print(f"--- Alumno {fil + 1} ---")
        fila = []
        for col in range(CANTIDAD_TRIMESTRES):
            mensaje = "Ingrese la nota del trimestre " + entero_a_texto(col + 1) + ": "
            nota    = pedir_nota(mensaje)
            fila.append(nota)
        retorno.append(fila)
    return retorno


def pedir_nombre_archivo() -> str:
    """Solicita al usuario el nombre del archivo CSV a leer.

    Returns:
        str: Nombre del archivo ingresado por el usuario.
    """
    retorno = input("Ingrese el nombre del archivo (ej: notas.csv): ")
    return retorno


def pedir_opcion_menu() -> str:
    """Solicita al usuario que elija una opción del menú principal.

    Returns:
        str: Opción ingresada como cadena de texto.
    """
    retorno = input("Seleccione una opción: ")
    return retorno


def pedir_opcion_carga() -> str:
    """Solicita al usuario que elija entre carga secuencial (a) o desde archivo (b).

    Returns:
        str: Opción ingresada como cadena de texto.
    """
    retorno = input("Seleccione una opción (a/b): ")
    return retorno