n = int(input("Escribe un numero: "))

suma = 0

while n > 0:
    digito = n % 10
    if digito % 2 != 0:
        suma += digito
    n = n // 10

print(suma)