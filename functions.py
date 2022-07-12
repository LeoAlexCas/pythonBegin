#se definen con def

from unicodedata import numeric


def saludar():
    print("Hola mundo")

def saludarConParam(string):
    print(f"Hola {string}")

saludarConParam("Leo")

#tipica funcion de calculadora
def calculadora(operation, number1, number2):
    if operation == "suma":
        print(number1 + number2)
    elif operation == "resta":
        print(number1 - number2)
    elif operation == "multiplicar":
        print(number1 * number2)
    elif operation == "dividir":
        print(number1 / number2)
    elif operation == "modulo":
        print(number1 % number2)


calculadora("resta", 1, 4)

#existen funciones lambda, pero son distintas
suma = lambda n1, n2: print(n1 + n2)

suma(1, 3)