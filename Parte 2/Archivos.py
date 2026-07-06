import json
import os


def cargar_json(nombre_archivo: str) -> list:
    """Carga una lista de diccionarios de alumnos desde un archivo JSON.

    Args:
        nombre_archivo (str): Nombre o ruta del archivo JSON a leer.

    Returns:
        list: Lista de diccionarios cargada desde el archivo, o None si
        el parámetro es inválido o el archivo no existe.
    """
    retorno = None
    if type(nombre_archivo) == str and len(nombre_archivo) > 0:
        if os.path.exists(nombre_archivo) == True:
            archivo = open(nombre_archivo, "r", encoding="utf-8")
            datos   = json.load(archivo)
            archivo.close()
            del archivo
            retorno = datos
        else:
            print("ERROR: El archivo no existe.")
    return retorno


def guardar_json(alumnos: list, nombre_archivo: str) -> bool:
    """Guarda la lista de diccionarios de alumnos en un archivo JSON.
    Si el archivo ya existe lo sobreescribe.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.
        nombre_archivo (str): Nombre o ruta del archivo JSON a generar.

    Returns:
        bool: True si el archivo se guardó correctamente, False si algún
        parámetro es inválido.
    """
    retorno = False
    if type(alumnos) == list and type(nombre_archivo) == str and len(nombre_archivo) > 0:
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)
        archivo.close()
        del archivo
        retorno = True
    return retorno