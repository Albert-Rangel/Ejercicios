#Programación numérica y no numérica-tarea 1
import os

# Inicializamos las variables
# incializamos la variable opcion para que se ejecute la primera validación
opcion = None

# generamos lista con las opciones del menú
operaciones = {
    '1': 'Suma',
    '2': 'Resta',
    '3': 'Multiplicación',
    '4': 'División',
    '5': 'Exponenciación',
    '6': 'Raíz cuadrada',
}
error = None
# almacenamos el menú en una variable
menu = """
    +----------------------+
    |    Calculadora       |
    +----------------------+
    |  1. Suma             |
    |  2. Resta            |
    |  3. Multiplicación   |
    |  4. División         |
    |  5. Exponenciación   |
    |  6. Raíz cuadrada    |
    |  7. Salir            |
    +----------------------+
"""


# Iniciamos el bucle principal
while True:

    # definimo la variable resultado en None 
    resultado=None

    os.system('cls || clear')  # Limpiamos la pantalla

    # Mostramos el menú
    print(menu)

    # Validamos la opción ingresada por el usuario
    if opcion is not None and opcion not in ('1', '2', '3', '4', '5', '6', '7'):
        print(f"""
                        \u26A0
        La opción: "{opcion}" no es válida.
        Por favor, ingrese un número entre 1 y 7.
        """)

    # Solicitamos la opción al usuario
    opcion = input("Selecciona una opción: ".rjust(30))

    # si la opción es 7, salimos del bucle1
    if opcion == '7':
        print("")
        print("""
            ----¡Hasta luego!----""")
        break

    # Validamos la opción ingresada por el usuario es entre 1 y 6
    if opcion in ('1', '2', '3', '4', '5', '6'):
        while True:
            try:

                os.system('cls || clear')  # Limpiamos la pantalla

                print(menu)

                print(f"-----Bienvenido a la opción de {operaciones[opcion]}-----".center(80))
    
                print("""

                    Si desea regresar al menú principal, presione Enter sin ingresar ningún valor.

                    """)

                if opcion in ('1', '2', '3', '4'):
                    entrada = input("Ingrese el primer número: ".rjust(30))
                    if entrada.strip() == "":
                        break
                    num1 = float(entrada)
                    entrada=""
                    print("")


                    entrada = input("Ingrese el segundo número: ".rjust(30))
                    if entrada.strip() == "":
                        break
                    num2 = float(entrada)
                    entrada=""


                elif opcion == '5':

                    entrada = input("Ingrese la base: ".rjust(30))
                    if entrada.strip() == "":
                        break
                    base = float( entrada)
                    entrada=""

                    entrada = input("Ingrese el exponente: ".rjust(30))
                    if entrada.strip() == "":
                        break
                    exponente = int(entrada)
                    entrada=""

                elif opcion == '6':

                    entrada = input("Ingrese el número para calcular la raíz cuadrada: ".rjust(30))
                    if entrada.strip() == "":
                        break
                    num1 = float(entrada)
                    entrada=""


                #procesamos la operación seleccionada
                # Suma
                if opcion == '1':
                    resultado = num1 + num2
                # Resta
                elif opcion == '2':
                    resultado = num1 - num2
                # Multiplicación
                elif opcion == '3':
                    resultado = num1 * num2
                # División
                elif opcion == '4':
                    resultado = num1 / num2
                # Exponenciación
                elif opcion == '5':
                    resultado = 1  # Inicializamos el resultado en 1
                    for _ in range(abs(exponente)):
                        resultado *= base
                    if exponente < 0:
                        resultado = 1 / resultado

                # Raíz cuadrada
                elif opcion == '6':#el método de Newton
                    if num1 < 0:
                        raise ValueError()
                    tolerancia = 1e-10  # Define la tolerancia para la precisión del resultado
                    aproximacion = num1 / 2.0  # Inicializa la aproximación
                    while True:
                        mejor_aproximacion = (aproximacion + num1 / aproximacion) / 2.0
                        if abs(mejor_aproximacion - aproximacion) < tolerancia:
                            break
                        aproximacion = mejor_aproximacion
                    resultado = mejor_aproximacion

                # Mostramos el resultado
                print("")
                if resultado.is_integer():
                    print(f"El resultado es: {int(resultado)}")
                else:
                    print(f"El resultado es: {resultado}")
                break

            # Capturamos las excepciones
            except ValueError as e:
                print(f"""
                                    \u26A0
                        ¡ingrese un valor valido!
                    """)
                input("Presione Enter para continuar...")
            except ZeroDivisionError:
                print(f"""
                                \u26A0
                    ¡No se pueden realizar esta operacion entre cero!
                """)
                input("Presione Enter para continuar...")
            except Exception as e:
                print(f"""
                                \u26A0
                    ¡Valores invalidos, por favor intente nuevamente!
                """)
                input("Presione Enter para continuar...")

        # si el resultado no es None, preguntamos si desea continuar
        if resultado is not None:
            print("")
            continuar = input("¿Desea continuar? (s/n): ")
            # si la respuesta es diferente de 's' salimos del bucle
            if continuar.lower() != 's':
                break

