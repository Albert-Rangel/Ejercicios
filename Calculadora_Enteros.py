# 3- El cliente requiere una calculadora con las operaciones básicas ( suma, resta, multiplicación y división), para dos números enteros

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
        else:
            print("Operación inválida.")

        print("Resultado:", resultado)
    except ValueError:
        print("Por favor, ingrese solo números.")

    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        break