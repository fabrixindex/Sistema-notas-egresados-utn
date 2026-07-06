import os
import Funciones
import Inputs
import Prints
import Archivos
 
 
def limpiar_consola() -> None:
    """Limpia la pantalla de la consola segun el sistema operativo.
 
    Returns:
        None
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print()
 
 
def esperar_menu() -> None:
    """Pausa la ejecucion hasta que el usuario presione ENTER y luego limpia la consola.
 
    Returns:
        None
    """
    input("\nToque ENTER para continuar...")
    limpiar_consola()
 
 
def menu_principal() -> None:
    """Controla el flujo principal del programa: muestra el menu, gestiona
    la carga de alumnos y ejecuta la opcion elegida por el usuario hasta
    que decide salir (guardando los datos en JSON antes de finalizar).
 
    Returns:
        None
    """
    alumnos        = []
    datos_cargados = False
 
    while True:
        Prints.mostrar_menu()
        opcion = Inputs.pedir_entero("Seleccione una opcion: ", 1, 6)
        limpiar_consola()
 
        if opcion == 1:
            print("\n" + "═" * 45)
            print("          CARGA DE ALUMNOS")
            print("═" * 45)
            print(" a) Cargar desde archivo JSON")
            print(" b) Carga manual")
            print("═" * 45)

            sub_opcion = input("Seleccione una opción (a/b): ").lower()

            if sub_opcion == "a":
                print("\n" + "─" * 45)
                print(" CARGA DESDE ARCHIVO")
                print("─" * 45)

                nombre_archivo = input("Ingrese el nombre del archivo (ej: alumnos.json): ")
                alumnos_cargados = Archivos.cargar_json(nombre_archivo)

                if alumnos_cargados is not None:
                    sobreescribir = True

                    if datos_cargados:
                        sobreescribir = Inputs.pedir_confirmacion(
                            "Ya hay datos cargados. ¿Desea sobreescribirlos?"
                        )

                    if sobreescribir:
                        alumnos = alumnos_cargados
                    else:
                        for alumno in alumnos_cargados:
                            alumnos.append(alumno)

                    datos_cargados = True
                    Prints.mostrar_mensaje("✓ Alumnos cargados correctamente.")

            elif sub_opcion == "b":
                print("\n" + "─" * 45)
                print(" CARGA MANUAL")
                print("─" * 45)

                nombre = Inputs.pedir_nombre_apellido("Ingrese el nombre: ")
                apellido = Inputs.pedir_nombre_apellido("Ingrese el apellido: ")
                egreso = Inputs.pedir_entero(
                    "Ingrese el año de egreso (1991-2026): ",
                    1991,
                    2026
                )
                plan = Inputs.pedir_plan()
                nota_promedio = Inputs.pedir_flotante(
                    "Ingrese la nota promedio (6-10): ",
                    6,
                    10
                )
                legajo = Funciones.generar_legajo(alumnos)

                nuevo_alumno = {
                    "legajo": legajo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "egreso": egreso,
                    "plan": plan,
                    "nota_promedio": nota_promedio
                }

                print("\n" + "═" * 45)
                print("        DATOS DEL NUEVO ALUMNO")
                print("═" * 45)

                Prints.mostrar_alumno(nuevo_alumno)

                confirmar = Inputs.pedir_confirmacion(
                    "¿Desea agregar este alumno?"
                )

                if confirmar:
                    alumnos.append(nuevo_alumno)
                    datos_cargados = True
                    Prints.mostrar_mensaje("✓ Alumno agregado correctamente.")
                else:
                    Prints.mostrar_mensaje("✗ Carga cancelada.")

            else:
                Prints.mostrar_mensaje("✗ Opción inválida.")
 
        elif opcion == 2:
            if datos_cargados == False:
                Prints.mostrar_mensaje("Primero debe cargar los alumnos (opcion 1).")
            else:
                plan        = Inputs.pedir_plan()
                encontrados = Funciones.filtrar_por_plan(alumnos, plan)
                if len(encontrados) == 0:
                    Prints.mostrar_mensaje("No hay alumnos recibidos de ese plan todavia.")
                else:
                    Prints.mostrar_lista_alumnos(encontrados)
 
        elif opcion == 3:
            if datos_cargados == False:
                Prints.mostrar_mensaje("Primero debe cargar los alumnos (opcion 1).")
            else:
                encontrados = Funciones.filtrar_anteriores_2000(alumnos)
                if len(encontrados) == 0:
                    Prints.mostrar_mensaje("No hay egresados anteriores al anio 2000.")
                else:
                    Prints.mostrar_lista_alumnos(encontrados)
                    promedio = Funciones.calcular_promedio_alumnos(encontrados)
                    Prints.mostrar_mensaje(f"Promedio general: {promedio:.2f}")
 
        elif opcion == 4:
            if datos_cargados == False:
                Prints.mostrar_mensaje("Primero debe cargar los alumnos (opcion 1).")
            else:
                texto       = Inputs.pedir_texto_busqueda("Ingrese nombre o apellido a buscar (min. 3 letras): ")
                encontrados = Funciones.buscar_por_nombre_o_apellido(alumnos, texto)
                Prints.mostrar_lista_alumnos(encontrados)
                Prints.mostrar_mensaje(f"Cantidad de alumnos encontrados: {len(encontrados)}")
 
        elif opcion == 5:
            if datos_cargados == False:
                Prints.mostrar_mensaje("Primero debe cargar los alumnos (opcion 1).")
            else:
                encontrados = Funciones.filtrar_salon_fama(alumnos)
                if len(encontrados) == 0:
                    Prints.mostrar_mensaje("No hay alumnos con promedio mayor o igual a 9.")
                else:
                    Prints.mostrar_lista_alumnos(encontrados)
 
        elif opcion == 6:
            Archivos.guardar_json(alumnos, "alumnos.json")
            Prints.mostrar_mensaje("Datos guardados. Hasta luego!")
            break
 
        esperar_menu()