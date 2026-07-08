import datetime
import os
from Prints import *

CANTIDAD_ALUMNOS = 7
CANTIDAD_TRIMESTRES = 3

# ALGORITMIA DE CADENAS 

def quitar_salto_linea(cadena: str) -> str:
    """Elimina manualmente los caracteres de fin de línea de una cadena.
 
    Args:
        cadena (str): Línea de texto leída de un archivo.
 
    Returns:
        str: Cadena sin los caracteres '\\n' ni '\\r', o None si el
        parámetro no es una cadena.
    """
    retorno = None
    if type(cadena) == str:
        resultado = ""
        for i in range(len(cadena)):
            if cadena[i] != "\n" and cadena[i] != "\r":
                resultado = resultado + cadena[i]
        retorno = resultado
    return retorno

def separar_por_coma(cadena: str) -> list:
    """Separa manualmente una cadena en partes usando la coma como separador.
    Reemplaza al método .split(',') de la clase str.
 
    Args:
        cadena (str): Línea de texto a separar (ej: "8,9,7").
 
    Returns:
        list: Lista de subcadenas separadas por coma, o None si el
        parámetro no es una cadena.
    """
    retorno = None
    if type(cadena) == str:
        partes = []
        actual = ""
        for i in range(len(cadena)):
            if cadena[i] == ",":
                partes.append(actual)
                actual = ""
            else:
                actual = actual + cadena[i]
        partes.append(actual)
        retorno = partes
    return retorno

def es_entero_valido(cadena: str) -> bool:
    """Verifica, carácter por carácter, si la cadena representa un entero positivo.
 
    Args:
        cadena (str): Cadena a validar.
 
    Returns:
        bool: True si todos los caracteres son dígitos y la cadena no
        está vacía, False en caso contrario o si el parámetro es inválido.
    """
    retorno = False
    if type(cadena) == str and len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if caracter_ascii < 48 or caracter_ascii > 57:
                retorno = False
                break
    return retorno

def texto_a_entero(cadena: str) -> int:
    """Convierte manualmente una cadena de dígitos en un número entero.
 
    Args:
        cadena (str): Cadena formada solo por dígitos (ej: "10").
 
    Returns:
        int: Número entero representado por la cadena, o -1 si la
        cadena no es un entero válido.
    """
    retorno = -1
    if es_entero_valido(cadena) == True:
        numero = 0
        for i in range(len(cadena)):
            numero = numero * 10 + (ord(cadena[i]) - ord("0"))
        retorno = numero
    return retorno

def entero_a_texto(numero: int) -> str:
    """Convierte manualmente un número entero no negativo en su representación de texto.

    Args:
        numero (int): Número entero no negativo a convertir.

    Returns:
        str: Representación en texto del número, o None si el parámetro
        no es un entero no negativo.
    """
    retorno = None
    if type(numero) == int and numero >= 0:
        if numero == 0:
            retorno = "0"
        else:
            digitos = ""
            n = numero
            while n > 0:
                resto   = n % 10
                digitos = chr(resto + ord("0")) + digitos
                n       = n // 10
            retorno = digitos
    return retorno

def formatear_dos_digitos(numero: int) -> str:
    """Formatea un número de día o mes con dos dígitos (agrega cero a la izquierda si es necesario).
    Es autocontenida: no depende de entero_a_texto para evitar errores en cadena.

    Args:
        numero (int): Número entero positivo entre 1 y 99 (día, mes).

    Returns:
        str: Número formateado con dos dígitos (ej: "05", "12"), o None si el
        parámetro es inválido.
    """
    retorno = None
    if type(numero) == int and numero >= 0:
        if numero < 10:
            retorno = "0" + chr(numero + ord("0"))
        else:
            retorno = chr(numero // 10 + ord("0")) + chr(numero % 10 + ord("0"))
    return retorno

# AUXILIARES DE MATRIZ
 
def obtener_cantidad_columnas(matriz: list) -> int:
    """Obtiene la cantidad de columnas tomando la longitud de la primera fila.
 
    Args:
        matriz (list): Matriz (lista de listas).
 
    Returns:
        int: Cantidad de columnas, o 0 si la matriz es inválida o está vacía.
    """
    retorno = 0
    if type(matriz) == list and len(matriz) > 0:
        retorno = len(matriz[0])
    return retorno

# CARGA DE DATOS

def cargar_desde_csv(nombre_archivo: str) -> list:
    """Carga la matriz leyendo un archivo CSV línea por línea, sin usar el módulo csv.
    Salta automáticamente la primera línea si es el encabezado.
    Separa los valores por coma usando algoritmia de cadenas.
 
    Args:
        nombre_archivo (str): Nombre o ruta del archivo CSV a leer.
 
    Returns:
        list: Matriz de notas leída del archivo, o None si el archivo no
        existe o el parámetro no es válido.
    """
    retorno = None
    if type(nombre_archivo) == str and len(nombre_archivo) > 0:
        if os.path.exists(nombre_archivo) == True:
            matriz  = []
            archivo = open(nombre_archivo, "r", encoding="utf-8")
            lineas  = archivo.readlines()
            archivo.close()
            del archivo
            for numero_linea in range(len(lineas)):
                if numero_linea == 0:          
                    continue
                linea_limpia = quitar_salto_linea(lineas[numero_linea])
                if len(linea_limpia) > 0:
                    partes = separar_por_coma(linea_limpia)
                    fila   = []
                    for i in range(len(partes)):
                        fila.append(texto_a_entero(partes[i]))
                    matriz.append(fila)
            retorno = matriz
        else:
            imprimir_error_archivo()
    return retorno

# FUNCIONES DE OPCIONES DEL MENÚ

def mostrar_desaprobados(matriz: list) -> bool:
    """Muestra los alumnos que tienen al menos una nota menor a 7.
    Si no existen, informa al usuario.
 
    Args:
        matriz (list): Matriz de notas (filas = alumnos, columnas = trimestres).
 
    Returns:
        bool: True si se encontró al menos un desaprobado, False si no
        hay ninguno o si el parámetro es inválido.
    """
    retorno = False
    if type(matriz) == list and len(matriz) > 0:
        encontrados = False
        print("===== ALUMNOS DESAPROBADOS =====\n")
        for fil in range(len(matriz)):
            tiene_nota_baja = False
            for col in range(obtener_cantidad_columnas(matriz)):
                if matriz[fil][col] < 7:
                    tiene_nota_baja = True
            if tiene_nota_baja == True:
                print(f"Alumno N° {fil + 1}")
                print(f"  1° Trimestre: {matriz[fil][0]}")
                print(f"  2° Trimestre: {matriz[fil][1]}")
                print(f"  3° Trimestre: {matriz[fil][2]}")
                print("--------------------------------")
                encontrados = True
        if encontrados == False:
            print("No hay alumnos desaprobados.")
        retorno = encontrados
    return retorno

def mostrar_aplazos(matriz: list) -> bool:
    """Muestra los alumnos que tienen al menos una nota menor a 4 (aplazo).
    Si no existen, informa al usuario.
 
    Args:
        matriz (list): Matriz de notas (filas = alumnos, columnas = trimestres).
 
    Returns:
        bool: True si se encontró al menos un alumno con aplazo, False si
        no hay ninguno o si el parámetro es inválido.
    """
    retorno = False
    if type(matriz) == list and len(matriz) > 0:
        encontrados = False
        print("===== ALUMNOS CON APLAZOS =====\n")
        for fil in range(len(matriz)):
            tiene_aplazo = False
            for col in range(obtener_cantidad_columnas(matriz)):
                if matriz[fil][col] < 4:
                    tiene_aplazo = True
            if tiene_aplazo == True:
                print(f"Alumno N° {fil + 1}")
                print(f"  1° Trimestre: {matriz[fil][0]}")
                print(f"  2° Trimestre: {matriz[fil][1]}")
                print(f"  3° Trimestre: {matriz[fil][2]}")
                print("--------------------------------")
                encontrados = True
        if encontrados == False:
            print("No hay alumnos con aplazos.")
        retorno = encontrados
    return retorno

def mostrar_porcentajes(matriz: list) -> tuple:
    """Calcula y muestra el porcentaje de alumnos aprobados y desaprobados.
    Un alumno se considera desaprobado si tiene al menos una nota menor a 7.
 
    Args:
        matriz (list): Matriz de notas (filas = alumnos, columnas = trimestres).
 
    Returns:
        tuple: (porcentaje_aprobados, porcentaje_desaprobados), o None si el
        parámetro es inválido.
    """
    retorno = None
    if type(matriz) == list and len(matriz) > 0:
        cantidad_aprobados    = 0
        cantidad_desaprobados = 0
        print("===== PORCENTAJE APROBADOS / DESAPROBADOS =====\n")
        for fil in range(len(matriz)):
            tiene_nota_baja = False
            for col in range(obtener_cantidad_columnas(matriz)):
                if matriz[fil][col] < 7:
                    tiene_nota_baja = True
            if tiene_nota_baja == True:
                cantidad_desaprobados += 1
            else:
                cantidad_aprobados += 1
        total                   = len(matriz)
        porcentaje_aprobados    = round((cantidad_aprobados    * 100) / total, 2)
        porcentaje_desaprobados = round((cantidad_desaprobados * 100) / total, 2)
        print(f"Aprobados:    {porcentaje_aprobados} %")
        print(f"Desaprobados: {porcentaje_desaprobados} %\n")
        retorno = (porcentaje_aprobados, porcentaje_desaprobados)
    return retorno

def mostrar_mejor_trimestre(matriz: list) -> list:
    """Calcula el promedio de cada trimestre y muestra cuál tuvo el mejor resultado.
    Contempla la posibilidad de empate entre trimestres.
 
    Args:
        matriz (list): Matriz de notas (filas = alumnos, columnas = trimestres).
 
    Returns:
        list: Lista con el promedio de cada trimestre, o None si el
        parámetro es inválido.
    """
    retorno = None
    if type(matriz) == list and len(matriz) > 0:
        promedios = []
        for col in range(CANTIDAD_TRIMESTRES):
            suma = 0
            for fil in range(len(matriz)):
                suma += matriz[fil][col]
            promedio = round(suma / len(matriz), 2)
            promedios.append(promedio)
 
        mejor_promedio = promedios[0]
        for i in range(1, len(promedios)):
            if promedios[i] > mejor_promedio:
                mejor_promedio = promedios[i]
 
        print("===== PROMEDIOS POR TRIMESTRE =====\n")
        for i in range(len(promedios)):
            print(f"  Trimestre {i + 1}: {promedios[i]}")
        print(f"\nMejor promedio: {mejor_promedio}\n")
        print("Trimestre/s con el mejor promedio:")
        for i in range(len(promedios)):
            if promedios[i] == mejor_promedio:
                print(f"  Trimestre N° {i + 1}")
        retorno = promedios
    return retorno

def obtener_fecha_actual() -> str:
    """Obtiene la fecha actual del sistema y la devuelve con formato dd-mm-aaaa.
    Usa el módulo datetime para acceder a la fecha del sistema operativo.
 
    Returns:
        str: Fecha actual formateada (ej: "24-06-2026").
    """
    hoy     = datetime.date.today()
    dia     = formatear_dos_digitos(hoy.day)
    mes     = formatear_dos_digitos(hoy.month)
    anio    = entero_a_texto(hoy.year)
    retorno = dia + "-" + mes + "-" + anio
    return retorno

def guardar_csv(matriz: list) -> bool:
    """Guarda la matriz de notas en un archivo CSV dentro de la carpeta
    'archivos_guardados'. El nombre del archivo es la fecha actual (dd-mm-aaaa.csv).
 
    Args:
        matriz (list): Matriz de notas a guardar.
 
    Returns:
        bool: True si el archivo se guardo correctamente, False si el
        parametro es invalido o la matriz esta vacia.
    """
    retorno = False
    if type(matriz) == list and len(matriz) > 0:
        carpeta = "archivos_guardados"
        if os.path.exists(carpeta) == False:
            os.makedirs(carpeta)
        nombre_archivo = carpeta + "/" + obtener_fecha_actual() + ".csv"
        archivo        = open(nombre_archivo, "w", encoding="utf-8")
        archivo.write("trimestre1,trimestre2,trimestre3\n")
        for fil in range(len(matriz)):
            linea = ""
            for col in range(obtener_cantidad_columnas(matriz)):
                linea += entero_a_texto(matriz[fil][col])
                if col < obtener_cantidad_columnas(matriz) - 1:
                    linea += ","
            archivo.write(linea + "\n")
        archivo.close()
        del archivo
        print(f"Datos guardados en '{nombre_archivo}'")
        retorno = True
    return retorno