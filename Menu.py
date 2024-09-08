
# 2- El cliente requiere mostrar un menú con 6 platos del restaurante, para ser seleccionado por el cliente e indicar al cocinero cuál es la orden del comensal.

def show_Menu():
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
    try:
      opcion = int(input("Por favor ingrese el número del plato que desea ordenar en nuestro restaurante de la Nona: "))
      if 1 <= opcion <= 10:
        return opcion
      else:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 10 que son las cantidades de platillos que disponemos actualmente.")
    except ValueError:
      print("Por favor, ingrese un número entero válido.")

def take_Order():
  client_Selection = show_Menu()
  print(f"Muchas Gracias!  Usted eligio la opcion numero {client_Selection}.")
  print("Estamos preparando su order, porfavor espere un minuto.")

take_Order()