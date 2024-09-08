
#1- El usuario necesita poder calcular una potencia de base (entera) y exponente (entero)
while True:
    try:
        base = int(input("Por favor, ingresa un número entero como base: "))
        exponente = int(input("Por favor, ingresa un número entero como exponente: "))
        break  
    except ValueError:
        print("Por favor, ingresa solo números enteros.")
if exponente >= 0:
    resultado = base ** exponente
else:
    resultado = 1 / (base ** -exponente)

print(f"El Resultado de la potencia {base} con exponente {exponente} es: {resultado}")