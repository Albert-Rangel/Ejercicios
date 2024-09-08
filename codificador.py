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


def decimal_a_binario(numero):
  binario = ""
  while numero > 0:
    binario = str(numero % 2) + binario
    numero //= 2
  return binario if binario else "0"

# Solicitar el número al usuario
numero_decimal = int(input("Ingrese un número entero: "))

# Convertir y mostrar el resultado
resultado = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es: {resultado}")