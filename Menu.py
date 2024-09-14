
# 2- El cliente requiere mostrar un menú con 6 platos del restaurante, para ser seleccionado por el cliente e indicar al cocinero cuál es la orden del comensal.

print("Menú del día del restaurante de la Nona:")
print("1. Tequeños")
print("2. Arepas")
print("3. Hallacas")
print("4. Sopa")
print("5. Mondongo")
print("6. Pasticho")
print("7. Albondigas")
print("8. Pollo Frito")
print("9. Pollo al horno")
print("10. Pollo Asado")

while True:
    opcion = input("Por favor ingrese el número del plato que desea ordenar en nuestro restaurante de la Nona: ")
    if opcion.isdigit():
        opcion = int(opcion)
        if 1 <= opcion <= 10:
            break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 10 que son las cantidades de platillos que disponemos actualmente.")
    else:
        print("Por favor, ingrese un número entero válido.")

print(f"Muchas Gracias! Usted eligió la opción número {opcion}.")
print("Estamos preparando su orden, por favor espere un minuto.")