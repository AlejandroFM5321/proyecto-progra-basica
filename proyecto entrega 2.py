seleccionMenu=int(input("Seleccione el numero de la accion que desea realizar \n 1. Ingresar nueva venta \n 2. Actualizar inventario \n 3. Salir \n"))

nombreCliente = ""
dia = 0
mes = 0
ano = 0

def mostrarProductos(productosSupermercado):
    i = 1
    for producto in productosSupermercado:
        print(str(i) + ". " + producto[0] + " - $" + str(producto[1]))
        i += 1

if seleccionMenu==1:
    while nombreCliente == "":
        nombreCliente=input("Introduza el nombre del cliente: ")
    while mes<=0 or mes>12:
        mes = int(input("Ingrese el numero de mes: "))
    if mes==2:
        while dia<=0 or dia>28:
            dia=int(input("Ingrese el numero de dia: "))
    elif mes==4 or mes==6 or mes==9 or mes==11:
        while  dia<=0 or dia>30:
            dia=int(input("Ingrese el numero de dia: "))
    else:
        while  dia<=0 or dia>31:
            dia=int(input("Ingrese el numero de dia: "))
    while ano<2022:
        ano=int(input("Ingrese el año: "))

    productosSupermercado = [
        ["Leche", 2.5], ["Pan", 1.0], ["Huevos", 3.0], ["Arroz", 2.0], ["Frijoles", 1.5],
        ["Pasta", 1.75], ["Salsa de tomate", 1.25], ["Aceite de oliva", 4.0], ["Atún enlatado", 2.75],
        ["Papel higiénico", 0.75], ["Detergente", 3.5], ["Jabón de baño", 1.0], ["Cepillo de dientes", 1.25],
        ["Pasta de dientes", 1.0], ["Cereal", 2.0], ["Galletas", 1.5], ["Refresco", 1.25], ["Agua embotellada", 0.75],
        ["Jugo de naranja", 2.0], ["Manzanas", 1.0], ["Plátanos", 0.5], ["Naranjas", 0.75], ["Papas", 1.0],
        ["Cebollas", 0.75], ["Zanahorias", 0.5]
    ]

    mostrarProductos(productosSupermercado)  # Mostrar los productos disponibles

    i = 1
    factura = []
    total = 0
    salir = False
    while len(factura) < 20 and not salir:
        productoId = int(input("Ingrese el número del producto a agregar o '0' para terminar: "))
        if productoId == 0:
            salir = True  # Salir del bucle si el usuario elige '0'
        elif productoId < 1 or productoId > len(productosSupermercado):
            print("Error: Producto no válido")
        else:
            cantidad = int(input("Ingrese la cantidad a vender: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor que cero")
            else:
                precioUnitario = productosSupermercado[productoId-1][1]
                subtotal = precioUnitario * cantidad  # Calcular el subtotal del producto
                factura += [[productosSupermercado[productoId-1][0], precioUnitario, cantidad, subtotal]]  # Agregar el producto a la factura
                total += subtotal  # Actualizar el total
                # Mostrar el producto agregado a la venta
                print("\nProducto agregado a la venta:")
                print("Nombre: " + productosSupermercado[productoId-1][0])
                print("Precio: $" + str(precioUnitario))
                print("Cantidad: " + str(cantidad))
                print("Subtotal: $" + str(subtotal))
                print("Total acumulado: $" + str(total))  # Mostrar el total acumulado

    # Mostrar el resumen de la venta
    print("\nResumen de la venta:")
    print("Cliente:", nombreCliente)
    print("Fecha:", dia,"/", mes,"/", ano)
    print("Productos:")
    for producto in factura:
        print(str(producto[2]) + "x " + producto[0] + " - $" + str(producto[1]) + " - Subtotal: $" + str(producto[3]))
    print("Total a pagar: $", total)

elif seleccionMenu==3:
    print("Hasta la proxima")
