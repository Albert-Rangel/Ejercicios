#5- Se requiere solicitar los siguientes datos de tres clientes y agregarlos en una tabla: CI, Nombre Apellido, Sexo, Edad, Móvil

import os

clientes = []

#contador de clientes
contador = 0

# Pedir los datos de 3 clientes
for i in range(3):
    cliente = {}

    if contador == i:
        os.system('cls')

    cliente['CI'] = input(f"Ingrese el CI del cliente {i+1}: ")

    # Validar que el CI sea un número entero
    while not cliente['CI'].isdigit():
        print("Por favor, ingrese un CI válido.")
        cliente['CI'] = input(f"Ingrese el CI del cliente {i+1}: ")


    cliente['Nombre'] = input(f"Ingrese el nombre del cliente {i+1}: ")

    # Validar que el nombre no esté vacío y que solo contenga letras
    while not cliente['Nombre'].isalpha():
        print("Por favor, ingrese un nombre válido.")
        cliente['Nombre'] = input(f"Ingrese el nombre del cliente {i+1}: ")


    cliente['Apellido'] = input(f"Ingrese el apellido del cliente {i+1}: ")

    # Validar que el apellido no esté vacío y que solo contenga letras
    while not cliente['Apellido'].isalpha():
        print("Por favor, ingrese un apellido válido.")
        cliente['Apellido'] = input(f"Ingrese el apellido del cliente {i+1}: ")

    cliente['Sexo'] = input(f"Ingrese el sexo del cliente {i+1}: M o F: ")

    # Validar que el sexo sea 'M' o 'F'
    while cliente['Sexo'].upper() not in ['M', 'F']:
        print("Por favor, ingrese un sexo válido.")
        cliente['Sexo'] = input(f"Ingrese el sexo del cliente {i+1}: ")


    cliente['Edad'] = input(f"Ingrese la edad del cliente {i+1}: ")

    #validar que la edad sea un número entero
    while not cliente['Edad'].isdigit():
        print("Por favor, ingrese una edad válida.")
        cliente['Edad'] = input(f"Ingrese la edad del cliente {i+1}: ")

    cliente['Móvil'] = input(f"Ingrese el número de móvil del cliente {i+1}: ")

    # Validar que el número de móvil sea un número entero positivo
    while not cliente['Móvil'].isdigit():
        print("Por favor, ingrese un número de móvil válido.")
        cliente['Móvil'] = input(f"Ingrese el número de móvil del cliente {i+1}: ")

    clientes.append(cliente)
    contador += 1

# Mostrar los datos en una tabla
print("\nTabla de Clientes:")
print("-" * 80)
print("{:<10} {:<15} {:<15} {:<10} {:<5} {:<15}".format("CI", "Nombre", "Apellido", "Sexo", "Edad", "Móvil"))
print("-" * 80)
for cliente in clientes:
    print("{:<10} {:<15} {:<15} {:<10} {:<5} {:<15}".format(
        cliente['CI'],
        cliente['Nombre'],
        cliente['Apellido'],
        cliente['Sexo'],
        cliente['Edad'],
        cliente['Móvil']
    ))