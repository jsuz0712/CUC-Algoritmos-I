print("Bienvenidos al Sistema De Inventario Por Lotes")
print()


while True:
    print("---------------------")
    print("ver todo el inventario (1)")
    print("Ingresar un nuevo producto (2)")
    print("Descontar un lote (3)")
    print("Salir del programa (0)")
    menu = input("Seleccione El Menu: ")
    match menu:
        case "1":
                print("---------------------")
                print("Este es todo el inventario")
        case "2":
                print("---------------------")
                print("Ingreso producto")
        case "3":
                print("---------------------")
                print("Eliga el producto a descontar")
        case "0":
                print("---------------------")
                print("Saliendo...")
                break
        case _:
                print("---------------------")
                print("Opcion Invalida Digite nuevamente.")

