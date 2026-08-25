print("Bienvenidos al Sistema De Inventario Por Lotes")
print()

inventario = []


while True:
    print("---------------------")
    print("Ver todo el inventario ")
    print("Ingresar un nuevo producto (2)")
    print("Descontar un lote (3)")
    print("Salir del programa (0)")
    menu = input("Seleccione El Menu: ")
    match menu:
        case "1":
                print("---------------------")
                print("Este es todo el inventario")
                if len(inventario)==0:
                       print("El inventario esta vacio")
                else:
                       for producto in inventario:
                              print("Prodcuto"[0], "Lote:", producto[1], "Cantidad", producto[3])

        case "2":
                print("---------------------")
                print("Ingreso producto")
                nombre_producto=input("Ingrese el nombre del producto: ")
                lote_producto=input("Ingrese el numero de lote: ")
                numero_producto=int(input("Ingrese la cantidad: "))
                nuevo_producto = [nombre_producto, lote_producto, numero_producto]
                inventario.append(nuevo_producto)
                print("Producto agregado con exito")

        case "3":
                print("---------------------")
                print("Eliga el producto a descontar")
                if len(inventario)==0:
                       print("El inventario esta vacio")

        case "0":
                print("---------------------")
                print("Saliendo...")
                break
        case _:
                print("---------------------")
                print("Opcion Invalida Digite nuevamente.")

