print("empresa de transporte\n")
ban = {"Juan", "Maria", "Pedro", "Luisa"}
i = input("Ingrese el nombre del conductor: ")

if i in ban:
    print("Puede ingresar")
elif i not in ban:
    print("Usted no puede pasar")