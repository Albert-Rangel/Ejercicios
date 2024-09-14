# 3- El cliente requiere una calculadora con las operaciones básicas ( suma, resta, multiplicación y división), para dos números enteros
import os

while True:
    resultado=0
    os.system('cls')
    # solicitamos el primer número
    num1 = input("Ingrese el primer número: ")
    # validamos que valor ingresado sea un número entero
    while not (num1.isdigit()):
        print("Por favor, ingrese un número entero válido.")
        num1 = input("Ingrese el primer número: ")

    # convertimos el valor a int
    num1 = int(num1)

    # solicitamos el segundo número
    num2 = input("Ingrese el segundo número: ")

    # validamos que valor ingresado sea un número entero
    while  not (num2.isdigit()):
        print("Por favor, ingrese un número entero válido.")
        num2 = input("Ingrese el segundo número: ")

    # convertimos el valor a int
    num2 = int(num2)

    # solicitamos la operación
    operacion = input("Ingrese la operación (+, -, *, /): ")

    # validamos que la operación sea válida
    while operacion not in ['+', '-', '*', '/']:
        print("Operación no válida. Intente de nuevo.")
        operacion = input("Ingrese la operación (+, -, *, /): ")

    # realizamos la operación
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            resultado="No se puede dividir entre cero."
        else:
            resultado = num1 / num2


    # mostramos el resultado
    print("Resultado:", resultado)

    # preguntamos si desea continuar
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        break