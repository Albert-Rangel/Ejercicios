clientes = []

for i in range(3):
    cliente = {}
    cliente['CI'] = input(f"Ingrese el CI del cliente {i+1}: ")
    cliente['Nombre'] = input(f"Ingrese el nombre del cliente {i+1}: ")
    cliente['Apellido'] = input(f"Ingrese el apellido del cliente {i+1}: ")
    cliente['Sexo'] = input(f"Ingrese el sexo del cliente {i+1}: ")
    cliente['Edad'] = int(input(f"Ingrese la edad del cliente {i+1}: "))
    cliente['Móvil'] = input(f"Ingrese el número de móvil del cliente {i+1}: ")
    clientes.append(cliente)

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