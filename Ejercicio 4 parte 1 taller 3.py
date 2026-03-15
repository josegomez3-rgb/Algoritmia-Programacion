hora = int(input("Ingrese la hora: "))
a = 6
boton = 0
while hora != a:
    print("No es hora de alarma")
    break
else:
    print("Sonando alarma por 60 segundos")
    boton = input("¿Boton presionado para detener? si/no: ")
    if boton == "si":
        print("Alarma detenida")
    else:
        print("Alarma sigue sonando")
        while boton != "si":
            boton = input("¿Boton presionado para detener? si/no: ")
        print("Alarma detenida")  
        if boton == "no":
            print("Alarma sigue sonando")  