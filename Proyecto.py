print("Bienvenidos al Sistema De Inventario Por Lotes")
print()

# la matriz: cada fila es un lote
# columnas -> 0 nombre | 1 marca | 2 lote | 3 cantidad
inventario = [
    ["Laptop",  "HP",       "L-101", 15],
    ["Laptop",  "Lenovo",   "L-102", 8],
    ["Teclado", "Logitech", "L-201", 40],
    ["Mouse",   "Logitech", "L-202", 25],
    ["Monitor", "Samsung",  "L-301", 12],
]


while True:
    print("---------------------")
    print("Ver todo el inventario(1) ")
    print("Ingresar un nuevo producto (2)")
    print("Descontar un lote (3)")
    print("Salir del programa (0)")
    menu = input("Seleccione El Menu: ")

    match menu:
        # recorrido: paso fila por fila y la muestro
        case "1":
            print("---------------------")
            print("Este es todo el inventario")
            if len(inventario) == 0:
                print("El inventario esta vacio")
            else:
                for producto in inventario:
                    print(f"Producto: {producto[0]}, Marca: {producto[1]}, Lote:{producto[2]}, Cantidad: {producto[3]} ")

        # agrego una fila nueva al final de la matriz
        case "2":
            print("---------------------")
            print("Ingreso producto")
            nombre_producto = input("Ingrese el nombre del producto: ")
            marca_producto = input("Ingrese la marca del producto: ")
            lote_producto = input("Ingrese el numero de lote: ")

            # lo leo como texto, reviso que sea numero, y ahi si lo convierto
            numero_producto = input("Ingrese la cantidad: ")
            while numero_producto.isdigit() == False:
                print("Debes escribir un numero")
                numero_producto = input("Ingrese la cantidad: ")
            numero_producto = int(numero_producto)

            # el orden tiene que ser igual al de las columnas
            nuevo_producto = [nombre_producto, marca_producto, lote_producto, numero_producto]
            inventario.append(nuevo_producto)
            print("Producto agregado con exito")

        case "3":
            print("---------------------")
            print("Eliga el producto a descontar")

            # numero por pantalla desde 1, pero en python arranca en 0
            for i in range(len(inventario)):
                print(i+1, ")", "Producto: ",inventario[i][0], " Marca:", inventario[i][1], " Lote:", inventario[i][2], " Cantidad: ", inventario[i][3])

            opcion = input("Elija el número: ")
            while opcion.isdigit() == False:
                opcion = input("Elija el número: ")
            opcion = int(opcion)

            fila = opcion - 1  # le quito el 1 que le sume arriba

            # si no reviso el rango, el 0 me agarra la ultima fila
            if fila >= 0 and fila < len(inventario):
                descontar = input("Cuantos quieres descontar: ")
                while descontar.isdigit() == False:
                    descontar = input("Cuantos quieres descontar: ")
                descontar = int(descontar)
                if descontar == 0: #Ningun sistema debe permitir descontar 0
                    print("Debes descontar al menos 1")
                elif descontar > inventario[fila][3]:
                    print("No hay suficiente stock.")
                else:
                    # esto si cambia la matriz de verdad
                    inventario[fila][3] = inventario[fila][3] - descontar
                    print(f"Descuento exitoso {inventario[fila][0]} Stock actualizado: {inventario[fila][3]}")
            else:
                print("Ese numero no esta en la lista.")

        case "0":
            print("---------------------")
            print("Saliendo...")
            break

        case _:
            print("---------------------")
            print("Opcion Invalida Digite nuevamente.")
