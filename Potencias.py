
#1- El usuario necesita poder calcular una potencia de base (entera) y exponente (entero)

import os

while True:

    os.system('cls')

    base = input("Ingresa un número entero como base: ")

    # validamos que valor ingresado sea un número entero
    while not (base.isdigit()):
        print("Ingrese un número válido.")
        base = input("Ingresa un número entero como base:")

    base = int(base)

    exponente = input("Ingresa un número entero como exponente: ")

    # validamos que valor ingresado sea un número entero
    while not (exponente.isdigit()):
        print("Ingrese un número válido.")
        exponente = input("Ingresa un número entero como exponente: ")

    exponente = int(exponente)

    resultado = base ** exponente


    print(f"El Resultado de la potencia {base} con exponente {exponente} es: {resultado}")

    # Preguntar si desea continuar
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        break