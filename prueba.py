"""
    Contexto: En Excel las columnas están organizadas por medio de letras, en
    donde la primera columna es la letra “A”, la segunda la “B”, la tercera la “C”,
    sin embargo el alfabeto es finito y por esto la siguiente columna a la “Z” es la
    columna “AA” y le siguen la “AB”, “AC”,”AD”,... ”AZ”,”BA”,”BB”,”BC”,”BD”,...,
    “ZZ”,”AAA”,”AAB”,”AAC”... etc.

    Ejercicio: Realizar una aplicación en Python que reciba el número de una
    columna y diga cuál es su conversión en letras. De la misma manera que lo
    hace Excel, PERO adicionando la letra “Ñ”
"""

alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', )
tamanio = len(alfabeto) 

"""
    Defino función recursiva para calcular el valor en letras
"""
def a_letras(numero):
    """
        Si el número esta en el alfabeto se agrega a la cadena
    """
    if numero < tamanio:
        return alfabeto[numero]
    
    """
        se concatenan las letras obtenidas por la división entera y el módulo
    """
    return a_letras(numero // tamanio - 1) + a_letras(numero % tamanio)

if __name__ == "__main__":
    value = input("Ingrese el número de la columna: ")
    if not value.isdigit():
        print ("El valor a ingresar debe ser un número válido")
    else:
        print ("El valor en letras es: ", a_letras(int(value) - 1))