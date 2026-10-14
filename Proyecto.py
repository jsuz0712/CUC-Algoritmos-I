# Sistema de inventario por lotes
# ahora con clases: el Inventario tiene los Lotes (composicion)

class Lote:
    stock_minimo = 5 # atributo de clase, es igual para todos

    def __init__(self, nombre, marca, codigo, cantidad):
        # privados, solo se cambian con los metodos
        self.__nombre = nombre
        self.__marca = marca
        self.__codigo = codigo
        self.__cantidad = cantidad

    #getter (obtiene el valor de un atributo privado)
    @property
    def codigo(self): #sirve para leer el codigo desde afuera sin poder cambiarlo
        return self.__codigo

    #getter (obtiene el valor de un atributo privado)
    @property
    def cantidad(self): #sirve para leer la cantidad desde afuera sin poder cambiarla
        return self.__cantidad

    def descontar(self, cantidad):
        if self.__cantidad == 0:
            print("Ese lote esta agotado, no se puede descontar")
            return False
        if cantidad <= 0: #Ningun sistema debe permitir descontar 0
            print("Debes descontar al menos 1")
            return False
        if cantidad > self.__cantidad:
            print("No hay suficiente stock.")
            return False
        self.__cantidad = self.__cantidad - cantidad
        print(f"Descuento exitoso {self.__nombre} Stock actualizado: {self.__cantidad}")
        return True

    def mostrar(self):
        aviso = ""
        if self.__cantidad == 0:
            aviso = "(agotado)"
        elif self.__cantidad < Lote.stock_minimo:
            aviso = "(stock bajo)"
        print(f"Producto: {self.__nombre}, Marca: {self.__marca}, Lote:{self.__codigo}, Cantidad: {self.__cantidad} {aviso}")

class Inventario:
    def __init__(self):
        self.__lotes = [] # lista de lotes, privada

    def agregar(self, nombre, marca, codigo, cantidad):
        # el strip quita los espacios, asi "   " cuenta como vacio
        if nombre.strip() == "" or codigo.strip() == "":
            print("El nombre y el lote no pueden estar vacios")
            return False
        # reviso que el codigo del lote no este repetido
        for lote in self.__lotes:
            if lote.codigo == codigo:
                print("Ese lote ya existe")
                return False
        nuevo = Lote(nombre, marca, codigo, cantidad)
        self.__lotes.append(nuevo)
        return True

    def mostrar(self):
        if len(self.__lotes) == 0:
            print("El inventario esta vacio")
        else:
            # numero por pantalla desde 1, pero en python arranca en 0
            for i in range(len(self.__lotes)):
                print(i+1, end=") ")
                self.__lotes[i].mostrar()

    # me dice si ese numero esta en la lista
    def existe(self, opcion):
        fila = opcion - 1  # le quito el 1 que le sume arriba
        # si no reviso el rango, el 0 me agarra la ultima fila
        return fila >= 0 and fila < len(self.__lotes)

    def descontar(self, opcion, cantidad):
        if self.existe(opcion) == True:
            return self.__lotes[opcion - 1].descontar(cantidad)
        else:
            print("Ese numero no esta en la lista.")
            return False

    # este retorna porque calcula
    def total_unidades(self):
        total = 0
        for lote in self.__lotes:
            total = total + lote.cantidad
        return total

# funcion para no repetir el while del isdigit en todos lados
def leer_numero(mensaje):
    numero = input(mensaje)
    while numero.isdigit() == False:
        print("Debes escribir un numero")
        numero = input(mensaje)
    return int(numero)


print("Bienvenidos al Sistema De Inventario Por Lotes")
print()

inventario = Inventario()
inventario.agregar("Laptop", "HP", "L-101", 15)
inventario.agregar("Laptop", "Lenovo", "L-102", 8)
inventario.agregar("Teclado", "Logitech", "L-201", 40)
inventario.agregar("Mouse", "Logitech", "L-202", 25)
inventario.agregar("Monitor", "Samsung", "L-301", 12)


while True:
    print("---------------------")
    print("Ver todo el inventario(1) ")
    print("Ingresar un nuevo producto (2)")
    print("Descontar un lote (3)")
    print("Salir del programa (0)")
    menu = input("Seleccione El Menu: ")

    match menu:
        case "1":
            print("---------------------")
            print("Este es todo el inventario")
            inventario.mostrar()
            print("Total de unidades:", inventario.total_unidades())

        case "2":
            print("---------------------")
            print("Ingreso producto")
            nombre_producto = input("Ingrese el nombre del producto: ")
            marca_producto = input("Ingrese la marca del producto: ")
            lote_producto = input("Ingrese el numero de lote: ")
            numero_producto = leer_numero("Ingrese la cantidad: ")

            if inventario.agregar(nombre_producto, marca_producto, lote_producto, numero_producto) == True:
                print("Producto agregado con exito")

        case "3":
            print("---------------------")
            print("Eliga el producto a descontar")
            inventario.mostrar()
            opcion = leer_numero("Elija el numero: ")
            # primero reviso el numero y ahi si pregunto cuanto
            if inventario.existe(opcion) == True:
                descontar = leer_numero("Cuantos quieres descontar: ")
                inventario.descontar(opcion, descontar)
            else:
                print("Ese numero no esta en la lista.")

        case "0":
            print("---------------------")
            print("Saliendo...")
            break

        case _:
            print("---------------------")
            print("Opcion Invalida Digite nuevamente.")
