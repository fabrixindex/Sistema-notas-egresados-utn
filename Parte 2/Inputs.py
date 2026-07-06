import Funciones
 
 
def es_entero_valido(cadena: str) -> bool:
    """Verifica, caracter por caracter, si una cadena representa un numero entero.
 
    Args:
        cadena (str): Cadena a validar (puede incluir signo '-').
 
    Returns:
        bool: True si la cadena representa un entero valido, False en
        caso contrario o si el parametro es invalido.
    """
    retorno = False
    if type(cadena) == str and len(cadena) > 0:
        es_valida = True
        inicio = 0
        if cadena[0] == "-":
            inicio = 1
            if len(cadena) == 1:
                es_valida = False
        if es_valida == True:
            for i in range(inicio, len(cadena)):
                if cadena[i] < "0" or cadena[i] > "9":
                    es_valida = False
        retorno = es_valida
    return retorno
 
 
def es_flotante_valido(cadena: str) -> bool:
    """Verifica, caracter por caracter, si una cadena representa un numero decimal.
 
    Args:
        cadena (str): Cadena a validar (puede incluir un unico punto decimal).
 
    Returns:
        bool: True si la cadena representa un numero decimal valido,
        False en caso contrario o si el parametro es invalido.
    """
    retorno = False
    if type(cadena) == str and len(cadena) > 0:
        cantidad_puntos  = 0
        cantidad_digitos = 0
        es_valida        = True
        for i in range(len(cadena)):
            if cadena[i] == ".":
                cantidad_puntos = cantidad_puntos + 1
            elif cadena[i] >= "0" and cadena[i] <= "9":
                cantidad_digitos = cantidad_digitos + 1
            else:
                es_valida = False
        if cantidad_puntos > 1 or cantidad_digitos == 0:
            es_valida = False
        retorno = es_valida
    return retorno
 
 
def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
    """Pide un numero entero por teclado, validando que este dentro de un rango.
 
    Args:
        mensaje (str): Texto que se muestra para solicitar el dato.
        minimo (int): Valor minimo aceptado (inclusive).
        maximo (int): Valor maximo aceptado (inclusive).
 
    Returns:
        int: Numero entero ingresado por el usuario, ya validado dentro del rango.
    """
    retorno = -1
    valido  = False
    while valido == False:
        entrada = input(mensaje)
        if es_entero_valido(entrada) == True:
            numero = int(entrada)
            if numero >= minimo and numero <= maximo:
                retorno = numero
                valido  = True
            else:
                print(f"El valor debe estar entre {minimo} y {maximo}.")
        else:
            print("Debe ingresar un numero entero valido.")
    return retorno
 
 
def pedir_flotante(mensaje: str, minimo: float, maximo: float) -> float:
    """Pide un numero decimal por teclado, validando que este dentro de un rango.
 
    Args:
        mensaje (str): Texto que se muestra para solicitar el dato.
        minimo (float): Valor minimo aceptado (inclusive).
        maximo (float): Valor maximo aceptado (inclusive).
 
    Returns:
        float: Numero decimal ingresado por el usuario, ya validado dentro del rango.
    """
    retorno = -1.0
    valido  = False
    while valido == False:
        entrada = input(mensaje)
        if es_flotante_valido(entrada) == True:
            numero = float(entrada)
            if numero >= minimo and numero <= maximo:
                retorno = numero
                valido  = True
            else:
                print(f"El valor debe estar entre {minimo} y {maximo}.")
        else:
            print("Debe ingresar un numero valido.")
    return retorno
 
 
def pedir_nombre_apellido(mensaje: str) -> str:
    """Pide un nombre o apellido por teclado, validando que sea texto valido.
    Minimo 3 caracteres, solo letras y espacios.
 
    Args:
        mensaje (str): Texto que se muestra para solicitar el dato.
 
    Returns:
        str: Nombre o apellido ingresado por el usuario, ya validado.
    """
    retorno = None
    valido  = False
    while valido == False:
        texto = input(mensaje)
        if Funciones.validar_nombre(texto) == True:
            retorno = texto
            valido  = True
        else:
            print("Debe ingresar al menos 3 letras, sin numeros ni simbolos.")
    return retorno
 
 
def pedir_plan() -> int:
    """Pide al usuario que seleccione uno de los planes de estudio validos.
    Solo acepta 1991, 2003 o 2024.
 
    Returns:
        int: Plan de estudios elegido (1991, 2003 o 2024).
    """
    retorno = -1
    valido  = False
    while valido == False:
        print("Planes disponibles: 1991 - 2003 - 2024")
        plan = pedir_entero("Ingrese el plan: ", 1991, 2024)
        if plan == 1991 or plan == 2003 or plan == 2024:
            retorno = plan
            valido  = True
        else:
            print("El plan ingresado no es valido. Solo se aceptan: 1991, 2003, 2024.")
    return retorno
 
 
def pedir_confirmacion(mensaje: str) -> bool:
    """Pide confirmacion al usuario (s/n) para una accion determinada.
 
    Args:
        mensaje (str): Pregunta que se muestra al usuario.
 
    Returns:
        bool: True si el usuario respondio 's', False en cualquier otro
        caso o si el parametro es invalido.
    """
    retorno = False
    if type(mensaje) == str:
        respuesta     = input(mensaje + " (s/n): ")
        respuesta_min = Funciones.a_minuscula(respuesta)
        if respuesta_min == "s":
            retorno = True
    return retorno
 
 
def pedir_texto_busqueda(mensaje: str) -> str:
    """Pide un texto de busqueda por teclado, validando que tenga al menos 3 letras.
 
    Args:
        mensaje (str): Texto que se muestra para solicitar el dato.
 
    Returns:
        str: Texto de busqueda ingresado por el usuario, ya validado.
    """
    retorno = None
    valido  = False
    while valido == False:
        texto = input(mensaje)
        if len(texto) >= 3 and Funciones.validar_nombre(texto) == True:
            retorno = texto
            valido  = True
        else:
            print("Debe ingresar al menos 3 letras (sin numeros ni simbolos).")
    return retorno