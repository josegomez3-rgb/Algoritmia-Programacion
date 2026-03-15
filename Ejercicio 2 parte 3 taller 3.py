a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

suma = 0
for i in range (a, b+1):
    if i % 2 == 1:
        print(suma)
        suma += i