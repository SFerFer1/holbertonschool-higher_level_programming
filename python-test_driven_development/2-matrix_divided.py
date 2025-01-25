#!/usr/bin/python3
"""Módulo para dividir todos los elementos de una matriz
"""

def dividir_matriz(matriz, divisor):
    """Divide todos los elementos de una matriz por el divisor.

    Argumenys:
        matriz (lista de listas de enteros/decimales): La matriz que se va a dividir.
        divisor (entero/decimal): El número con el que se divide.

    Return:
        lista de listas de decimales: Un.

    Excepciones:
        TypeError: Si la matriz no es una lista de listas de enteros/decimales.
        TypeError: Si las filas de la matriz no tienen el mismo tamaño.
        TypeError: Si el divisor no es un número.
        ZeroDivisionError: Si el divisor es cero.
    """
    if not isinstance(matriz, list) or not all(isinstance(fila, list) for fila in matriz):
        raise TypeError("la matriz debe ser una lista de listas de enteros/decimales")

    if not all(isinstance(elem, (int, float)) for fila in matriz for elem in fila):
        raise TypeError("la matriz debe ser una lista de listas de enteros/decimales")

    largo_fila = len(matriz[0])
    if not all(len(fila) == largo_fila for fila in matriz):
        raise TypeError("todas las filas de la matriz deben tener el mismo tamaño")

    if not isinstance(divisor, (int, float)):
        raise TypeError("el divisor debe ser un número")
    if divisor == 0:
        raise ZeroDivisionError("división por cero")

    return [[round(elem / divisor, 2) for elem in fila] for fila in matriz]
