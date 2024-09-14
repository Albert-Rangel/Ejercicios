import os

def calculadora():
    while True:
        # Profesor elegimos limpiar la pantalla en un lapso de 2 segundos aproximadaente para que el usuario pueda visualizar el error en caso que exista uno
        contador = 0
        while contador < 10000000:  
            contador += 1

        os.system('cls || clear')  # Limpiamos la pantalla
        
        print("+----------------------+")
        print("||    Calculadora      ||")
        print("+----------------------+")
        print("||  1. Suma            ||")
        print("||  2. Resta           ||")
        print("||  3. Multiplicación  ||")
        print("||  4. División        ||")
        print("||  5. Exponenciación  ||")
        print("||  6. Raíz cuadrada   ||")
        print("||  7. Salir           ||")
        print("+----------------------+")


        print("")
        opcion = input("Selecciona una opción: ")

        if opcion == '7':
            print("")
            print("¡Hasta luego!")
            break

        try:
            if opcion in ('1', '2', '3', '4'):
                print("")
                num1 = float(input("Ingrese el primer número: "))
                print("")
                num2 = float(input("Ingrese el segundo número: "))
            elif opcion == '5':
                base = float(input("Ingrese la base: "))
                exponente = int(input("Ingrese el exponente (entero): "))
            elif opcion == '6':
                num1 = float(input("Ingrese el número para calcular la raíz cuadrada: "))
                num2 = None  # No se necesita un segundo número en este caso
            else:
                print("Por favor, ingrese un número entero válido.")

            if opcion == '1':
                resultado = num1 + num2
            elif opcion == '2':
                resultado = num1 - num2
            elif opcion == '3':
                resultado = num1 * num2
            elif opcion == '4':
                if num2 == 0:
                    raise ZeroDivisionError("División entre cero.")
                resultado = num1 / num2
            elif opcion == '5':
                resultado = 1  # Inicializamos el resultado en 1
                for _ in range(abs(exponente)):
                    resultado *= base
                if exponente < 0:
                    resultado = 1 / resultado
            elif opcion == '6':
                if num1 < 0:
                    raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
                resultado = num1 ** 0.5
            print("")
            print("El resultado es: ", resultado)

            # Preguntar si desea continuar
            print("")
            continuar = input("¿Desea continuar? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError as e:
            print("Error de valor:", e)
        except ZeroDivisionError:
            print("Error: División entre cero.")
        except Exception as e:
            print("Error inesperado:", e)

calculadora()