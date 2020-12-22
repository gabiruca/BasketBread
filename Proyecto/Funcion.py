from transacciones import *
print("The Bread Basket     Pastelería-Edimburgo,Escocia")

ingreso_menu = input("")
if ingreso_menu == "":
    print('''    1. Productos de “The Bread Basket”
    2. Número de ventas mensuales por producto
    3. Productos más vendidos
    4. La mejor hora para vender
    5. Salir''')
print("")

ingreso_opcion = int(input("Ingrese la opción que desee: "))
while ingreso_opcion != 5:
    if ingreso_opcion == 1:
        print("Productos disponibles")
        print(listaProductos())

    elif ingreso_opcion == 2:
        nProducto = input("Nombre de Producto: ")
        nMes = int(input("Mes: "))
        print( "En el mes ",nMes, "se vendieron ",VentasProducto(nProducto, nMes)," ",nProducto)

    elif ingreso_opcion == 3:
        numeroE= int(input("Ingrese la cantidad de productos más vendidos que desea ver: "))
        masVendidos(numeroE)

    elif ingreso_opcion == 4:
        print(" Franjas Horarias: ")
        listaFranjas = ["Mañana", "Media Tarde", "Tarde", "Noche"]
        print(listaFranjas)
        print("Espere...")
        print(" \n Franja ", mejorFranjaHoraria(listaFranjas))
    print("\n")
    ingreso_opcion= int(input("Ingrese la opción que desee: "))

if ingreso_opcion == 5:
        print("Hasta luego")
        print("")