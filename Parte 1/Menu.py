import os
from Funciones import *
from Inputs import *
from Prints import *


def limpiar_consola() -> None:
    """Limpia la pantalla de la consola según el sistema operativo.

    Returns:
        None
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print()


def esperar_menu() -> None:
    """Pausa la ejecución hasta que el usuario presione ENTER y luego limpia la consola.

    Returns:
        None
    """
    input("\nToque ENTER para continuar...")
    limpiar_consola()


def mostrar_menu() -> None:
    """Ejecuta el menú principal del sistema, controlando el flujo completo del programa.
    Bloquea las opciones 2 a 5 si no se cargaron datos previamente.
    Al salir guarda el CSV solo si la carga fue manual (opción a).

    Returns:
        None
    """
    matriz         = []
    datos_cargados = False
    carga_manual   = False

    while True:
        imprimir_menu()
        opcion = pedir_opcion_menu()
        limpiar_consola()

        if opcion == "1":
            imprimir_menu_carga()
            sub_opcion = pedir_opcion_carga()

            if sub_opcion == "a":
                matriz         = cargar_secuencial()
                datos_cargados = True
                carga_manual   = True
                imprimir_carga_exitosa()

            elif sub_opcion == "b":
                nombre_archivo = pedir_nombre_archivo()
                resultado      = cargar_desde_csv(nombre_archivo)
                if resultado is not None:
                    matriz         = resultado
                    datos_cargados = True
                    carga_manual   = False
                    imprimir_carga_exitosa()

            else:
                imprimir_error_opcion()

        elif opcion == "2":
            if datos_cargados == True:
                mostrar_desaprobados(matriz)
            else:
                imprimir_datos_no_cargados()

        elif opcion == "3":
            if datos_cargados == True:
                mostrar_aplazos(matriz)
            else:
                imprimir_datos_no_cargados()

        elif opcion == "4":
            if datos_cargados == True:
                mostrar_porcentajes(matriz)
            else:
                imprimir_datos_no_cargados()

        elif opcion == "5":
            if datos_cargados == True:
                mostrar_mejor_trimestre(matriz)
            else:
                imprimir_datos_no_cargados()

        elif opcion == "6":
            if datos_cargados == True and carga_manual == True:
                guardar_csv(matriz)
            imprimir_despedida()
            break

        else:
            imprimir_error_opcion()

        esperar_menu()