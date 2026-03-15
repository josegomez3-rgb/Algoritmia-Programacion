a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = 0

for i in range(a, b+1):
    if i % 2 != 0:
        suma += i

print(suma)