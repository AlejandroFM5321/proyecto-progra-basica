BUENAS
seleccionMenu=int(input("Seleccione el numero de la accion que desea realizar \n 1. Ingresar nueva ventana \n 2. Actualizar inventario \n 3. Salir \n"))
nombreCliente=""
dia=0
mes=0
ano=0
if seleccionMenu==1:
    while nombreCliente == "":
        nombreCliente=input("Introduza el nombre del cliente: ")
    while mes<=0 or mes>12:
        mes=int(input("Ingrese el numero de mes: "))
    if mes==2:
        while dia<=0 or dia>28:
            dia=int(input("Ingrese el numero de dia: "))
    if mes==4 or mes==6 or mes==9 or mes==11:
        while  dia<=0 or dia>30:
            dia=int(input("Ingrese el numero de dia: "))
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        while  dia<=0 or dia>31:
            dia=int(input("Ingrese el numero de dia: "))
    while ano<=2022:
        ano=int(input("Ingrese el año: "))
    print("Cliente:", nombreCliente)
    print("Fecha:", dia,"/", mes,"/", ano)
if seleccionMenu==3:
    print("Hasta la proxima")
    
    
    
    
    
        
    
