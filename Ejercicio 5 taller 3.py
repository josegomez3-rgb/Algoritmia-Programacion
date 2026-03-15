vacio = False
lleno = False
valvula = "cerrada"

while True:

    if vacio == True:
        valvula = "abierta"
        print("La válvula se abre para llenar el tanque")
        
        while lleno == False:
            print("El tanque se está llenando")
    
        valvula = "cerrada"
        print("El tanque está lleno, la válvula se cierra") 