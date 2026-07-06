import random

# LEGAJO

def legajo_existe(alumnos: list, legajo: int) -> bool:
    """Verifica si un legajo ya existe dentro de la lista de alumnos.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.
        legajo (int): Número de legajo a buscar.

    Returns:
        bool: True si el legajo ya existe, False si no existe o si
        alguno de los parámetros es inválido.
    """
    retorno = False
    if type(alumnos) == list and type(legajo) == int:
        encontrado = False
        for i in range(len(alumnos)):
            if alumnos[i]["legajo"] == legajo:
                encontrado = True
        retorno = encontrado
    return retorno


def generar_legajo(alumnos: list) -> int:
    """Genera un legajo aleatorio de 6 cifras que no se repita en la lista.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.

    Returns:
        int: Nuevo legajo único de 6 cifras, o -1 si el parámetro es inválido.
    """
    retorno = -1
    if type(alumnos) == list:
        legajo_generado = random.randint(100000, 999999)
        while legajo_existe(alumnos, legajo_generado) == True:
            legajo_generado = random.randint(100000, 999999)
        retorno = legajo_generado
    return retorno

# ALGORITMIA DE CADENAS

def es_letra(caracter: str) -> bool:
    """Verifica si un caracter es una letra (mayúscula o minúscula) o un espacio.

    Args:
        caracter (str): Caracter individual a validar.

    Returns:
        bool: True si es letra o espacio, False en caso contrario o si
        el parámetro no es un caracter válido.
    """
    retorno = False
    if type(caracter) == str and len(caracter) == 1:
        retorno = (caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z") or caracter == " "
    return retorno


def validar_nombre(cadena: str) -> bool:
    """Valida que una cadena tenga al menos 3 caracteres y contenga solo letras y espacios.

    Args:
        cadena (str): Nombre o apellido a validar.

    Returns:
        bool: True si la cadena es válida, False en caso contrario o si
        el parámetro es inválido.
    """
    retorno = False
    if type(cadena) == str and len(cadena) >= 3:
        es_valida = True
        for i in range(len(cadena)):
            if es_letra(cadena[i]) == False:
                es_valida = False
        retorno = es_valida
    return retorno


def a_minuscula(cadena: str) -> str:
    """Convierte manualmente una cadena a minúsculas sin usar .lower().

    Args:
        cadena (str): Cadena a convertir.

    Returns:
        str: Cadena convertida a minúsculas, o None si el parámetro
        no es una cadena.
    """
    retorno = None
    if type(cadena) == str:
        resultado = ""
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if caracter_ascii >= 65 and caracter_ascii <= 90:
                resultado = resultado + chr(caracter_ascii + 32)
            else:
                resultado = resultado + cadena[i]
        retorno = resultado
    return retorno


def contiene_subcadena(cadena_grande: str, subcadena: str) -> bool:
    """Busca una subcadena dentro de otra sin distinguir mayúsculas/minúsculas
    y permitiendo coincidencias parciales. No usa el operador 'in' ni .find().
    Utiliza una ventana deslizante que recorre la cadena grande caracter por caracter.

    Args:
        cadena_grande (str): Cadena donde se realiza la búsqueda.
        subcadena (str): Texto a buscar dentro de la cadena grande.

    Returns:
        bool: True si la subcadena se encuentra dentro de la cadena grande,
        False en caso contrario o si los parámetros son inválidos.
    """
    retorno = False
    if type(cadena_grande) == str and type(subcadena) == str and len(subcadena) > 0:
        cadena_min   = a_minuscula(cadena_grande)
        subcadena_min = a_minuscula(subcadena)
        largo_grande  = len(cadena_min)
        largo_sub     = len(subcadena_min)
        if largo_sub <= largo_grande:
            encontrado = False
            for posicion in range(largo_grande - largo_sub + 1):
                coincide = True
                for j in range(largo_sub):
                    if cadena_min[posicion + j] != subcadena_min[j]:
                        coincide = False
                if coincide == True:
                    encontrado = True
            retorno = encontrado
    return retorno


# FUNCIONES PROPIAS 

def calcular_suma(lista_numeros: list) -> float:
    """Calcula la suma total de una lista de números sin usar sum().

    Args:
        lista_numeros (list): Lista de valores numéricos.

    Returns:
        float: Suma total de los valores, o -1 si el parámetro es
        inválido o la lista está vacía.
    """
    retorno = -1
    if type(lista_numeros) == list and len(lista_numeros) > 0:
        total = 0
        for i in range(len(lista_numeros)):
            total = total + lista_numeros[i]
        retorno = total
    return retorno


def calcular_promedio(lista_numeros: list) -> float:
    """Calcula el promedio de una lista de números sin usar sum().

    Args:
        lista_numeros (list): Lista de valores numéricos.

    Returns:
        float: Promedio de los valores, o -1 si el parámetro es
        inválido o la lista está vacía.
    """
    retorno = -1
    if type(lista_numeros) == list and len(lista_numeros) > 0:
        retorno = calcular_suma(lista_numeros) / len(lista_numeros)
    return retorno


def calcular_promedio_alumnos(lista_alumnos: list) -> float:
    """Calcula el promedio general de notas de una lista de diccionarios de alumnos.

    Args:
        lista_alumnos (list): Lista de diccionarios con los datos de los alumnos.

    Returns:
        float: Promedio general de las notas, o -1 si el parámetro es
        inválido o la lista está vacía.
    """
    retorno = -1
    if type(lista_alumnos) == list and len(lista_alumnos) > 0:
        notas = []
        for i in range(len(lista_alumnos)):
            notas.append(lista_alumnos[i]["nota_promedio"])
        retorno = calcular_promedio(notas)
    return retorno


# ORDENAMIENTO (burbuja adaptado a lista de diccionarios)

def intercambiar_valores(lista: list, izq: int, der: int) -> None:
    """Intercambia dos elementos de una lista usando una variable auxiliar.

    Args:
        lista (list): Lista cuyos elementos se van a intercambiar.
        izq (int): Índice del primer elemento.
        der (int): Índice del segundo elemento.

    Returns:
        None
    """
    if type(lista) == list and type(izq) == int and type(der) == int:
        aux        = lista[izq]
        lista[izq] = lista[der]
        lista[der] = aux


def ordenar_por_promedio_desc(alumnos: list) -> list:
    """Ordena una copia de la lista de alumnos de mayor a menor según nota_promedio,
    usando el algoritmo de selección (igual al visto en clase adaptado a diccionarios).

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.

    Returns:
        list: Nueva lista ordenada de mayor a menor por nota_promedio, o
        None si el parámetro es inválido.
    """
    retorno = None
    if type(alumnos) == list:
        lista = alumnos.copy()
        for izq in range(len(lista) - 1):
            for der in range(izq + 1, len(lista)):
                if lista[izq]["nota_promedio"] < lista[der]["nota_promedio"]:
                    intercambiar_valores(lista, izq, der)
        retorno = lista
    return retorno


# FILTROS / BÚSQUEDAS

def filtrar_por_plan(alumnos: list, plan: int) -> list:
    """Filtra los alumnos que pertenecen a un plan de estudios determinado.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.
        plan (int): Plan de estudios a filtrar (1991, 2003 o 2024).

    Returns:
        list: Lista de alumnos que pertenecen a ese plan, o None si
        algún parámetro es inválido.
    """
    retorno = None
    if type(alumnos) == list and type(plan) == int:
        resultado = []
        for i in range(len(alumnos)):
            if alumnos[i]["plan"] == plan:
                resultado.append(alumnos[i])
        retorno = resultado
    return retorno


def filtrar_anteriores_2000(alumnos: list) -> list:
    """Filtra los alumnos egresados antes del año 2000.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.

    Returns:
        list: Lista de alumnos egresados antes del 2000, o None si el
        parámetro es inválido.
    """
    retorno = None
    if type(alumnos) == list:
        resultado = []
        for i in range(len(alumnos)):
            if alumnos[i]["egreso"] < 2000:
                resultado.append(alumnos[i])
        retorno = resultado
    return retorno


def buscar_por_nombre_o_apellido(alumnos: list, texto: str) -> list:
    """Busca alumnos cuyo nombre o apellido contenga el texto ingresado.
    La búsqueda es parcial y no distingue mayúsculas de minúsculas.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.
        texto (str): Texto a buscar dentro del nombre o apellido.

    Returns:
        list: Lista de alumnos encontrados, o None si algún parámetro
        es inválido.
    """
    retorno = None
    if type(alumnos) == list and type(texto) == str and len(texto) > 0:
        resultado = []
        for i in range(len(alumnos)):
            nombre   = alumnos[i]["nombre"]
            apellido = alumnos[i]["apellido"]
            if contiene_subcadena(nombre, texto) == True or contiene_subcadena(apellido, texto) == True:
                resultado.append(alumnos[i])
        retorno = resultado
    return retorno


def filtrar_salon_fama(alumnos: list) -> list:
    """Filtra los alumnos con nota promedio mayor o igual a 9 y los ordena
    de mayor a menor según su promedio.

    Args:
        alumnos (list): Lista de diccionarios con los datos de los alumnos.

    Returns:
        list: Lista de alumnos con promedio >= 9 ordenada de mayor a
        menor, o None si el parámetro es inválido.
    """
    retorno = None
    if type(alumnos) == list:
        resultado = []
        for i in range(len(alumnos)):
            if alumnos[i]["nota_promedio"] >= 9:
                resultado.append(alumnos[i])
        retorno = ordenar_por_promedio_desc(resultado)
    return retorno