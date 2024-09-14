# 4- Se necesita un codificador (pasar números a binario) de números enteros del 0 al 10

# Si ingresas el número 5, la función hará lo siguiente:

# binario = ""
# 5 % 2 = 1, entonces binario es "1".
# 5 // 2 = 2.
# 2 % 2 = 0, entonces binario es "01".
# 2 // 2 = 1.
# 1 % 2 = 1, entonces binario es "101".
# 1 // 2 = 0, el bucle termina.
# Se devuelve "101".

import os

while True:
    os.system('cls')
    # Solicitar el número al usuario
    numero = input("Ingrese un número: ")

    # validamos que valor ingresado sea un número positivo 
    while not (numero.isdigit() and int(numero) <= 10):
        print("Por favor, ingrese un número válido.")
        numero = input("Ingrese el primer número: ")


    # Convertir el valor a entero
    numero = int(numero)

    # guardamos el valor para mostrarlo al final
    valor = numero

    # Convertir el número decimal a binario
    binario = ""

    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2

    # Manejar el caso en que el número es 0
    if not binario:
        binario = "0"

    # Mostrar el resultado
    print(f"El número {valor} en binario es: {binario}")

    # Preguntar si desea continuar
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        break
