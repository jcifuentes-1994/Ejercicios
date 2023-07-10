import Funciones as fn

print("Bienvenidos a Vuelos-Duoc")

asientos = fn.asientos
asientos_ocupados = fn.asientos_ocupados
pasajeros = {}

menu = 0
valorNormal = 78900
valorVip = 240000
confirmar = 0

while menu != 5:
    print("Seleccione una de las siguientes opciones: ")
    print("1. Ver asientos disponibles \n2.Comprar asiento \n3.Anular vuelo \n4.Modificar datos de pasajero \n5.Salir")
    menu = int(input())

    if menu == 1:
        print("Asientos disponibles")
        print(asientos_ocupados[0][0:3],"       ",asientos_ocupados[0][3:6])
        print(asientos_ocupados[1][0:3],"       ",asientos_ocupados[1][3:6])
        print(asientos_ocupados[2][0:3],"    ",asientos_ocupados[2][3:6])
        print(asientos_ocupados[3][0:3],"    ",asientos_ocupados[3][3:6])
        print(asientos_ocupados[4][0:3],"    ",asientos_ocupados[4][3:6])
        print("____________      ____________")
        print("____________      ____________")
        print(asientos_ocupados[5][0:3],"    ",asientos_ocupados[5][3:6])
        print(asientos_ocupados[6][0:3],"    ",asientos_ocupados[6][3:6])

    elif menu == 2:
        print ("Comprar asiento")
        print("Recuerde que los asientos del 31 al 42 tienen valor VIP")
        nombre = input("Ingrese su nombre y apellido: ").upper()
        rut = input("Ingrese su Rut sin puntos ni guión: ").upper()
        telefono = input("Ingrese su número telefónico: ")
        banco = int(input("Seleccione su banco: \n1.BancoDuoc 2.Otros Bancos \n"))
        

        while True:
            eleccionAsiento = int(input("Indique el número de su asiento: "))
            if eleccionAsiento > 0 and eleccionAsiento < 43:
                f,c = fn.buscar_asiento(eleccionAsiento,asientos)
                break
            else:
                print("El asiento no existe")
        
        if banco == 1:
            if eleccionAsiento > 0 and eleccionAsiento < 31:
                valor = valorNormal * 0.85
                print("El valor a pagar es: $",valor)
            elif eleccionAsiento > 30 and eleccionAsiento < 43:
                valor = valorVip * 0.85
                print("El valor a pagar es: $",valor)
        elif banco == 2:
            if eleccionAsiento > 0 and eleccionAsiento < 31:
                valor = valorNormal
                print("El valor a pagar es: $",valor)
            elif eleccionAsiento > 30 and eleccionAsiento < 43:
                valor = valorVip
                print("El valor a pagar es: $",valor)

        while True:
            print("Desea confirmar la compra?:")
            confirmar = int(input("1.Si  2.No \n"))
            if confirmar == 1:
                print("Muchas gracias por su compra")
                asientos_ocupados[f][c] = "X"
                pasajeros[eleccionAsiento] = nombre,rut,telefono

                break
            elif confirmar == 2:
                print("Compra cancelada")
                break
            else:
                print("La elección no existe")

    elif menu == 3:
        print("Anular vuelo")
        eleccionAsiento = int(input("Ingrese su asiento: "))
        print("Se anulará el asiento N°",eleccionAsiento)
        print("Pasajero: ",pasajeros[eleccionAsiento][0])
        print("Rut: ",pasajeros[eleccionAsiento][1])
        print("Teléfono: ",pasajeros[eleccionAsiento][2])
        f,c = fn.buscar_asiento(eleccionAsiento,asientos)
        conf_Anul = int(input("Desea confirmar la anulación: \n1.Si  2.No \n"))
        if conf_Anul == 1:
            asientos_ocupados[f][c] = eleccionAsiento
            del pasajeros[eleccionAsiento]
            print("Anulación Realizada")
        if conf_Anul == 2:
            print("Anulación cancelada")

    elif menu == 4:
        print("Modificar datos de pasajero")
        eleccionAsiento = int(input("Ingrese su asiento: "))
        rut = input("Ingrese su Rut sin puntos ni guión: ").upper()
        
        if pasajeros[eleccionAsiento][1] == rut:
            opcion = int(input("Seleccione la opción que desea modificar: \n1.Nombre pasajero  2.Teléfono pasajero \n"))
            if opcion == 1:
                print("Modificar nombre de pasajero")
                nombre = input("Ingrese el nuevo nombre: ").upper()
                rut = pasajeros[eleccionAsiento][1]
                telefono = pasajeros[eleccionAsiento][2]
                del pasajeros[eleccionAsiento]
                pasajeros[eleccionAsiento] = nombre,rut,telefono
                print("Nombre modificado con éxito")
                print("Pasajero: ",pasajeros[eleccionAsiento][0])
                print("Rut: ",pasajeros[eleccionAsiento][1])
                print("Teléfono: ",pasajeros[eleccionAsiento][2])
                
            elif opcion == 2:
                print("Modificar teléfono de pasajero")
                telefono = int(input("Ingrese el nuevo teléfono: "))
                nombre = pasajeros[eleccionAsiento][0]
                rut = pasajeros[eleccionAsiento][1]
                del pasajeros[eleccionAsiento]
                pasajeros[eleccionAsiento] = nombre,rut,telefono
                print("Nombre modificado con éxito")
                print("Pasajero: ",pasajeros[eleccionAsiento][0])
                print("Rut: ",pasajeros[eleccionAsiento][1])
                print("Teléfono: ",pasajeros[eleccionAsiento][2])
                
        else:
            print("El pasajero no existe")

    elif menu == 5:
        print("Hasta luego")



        




