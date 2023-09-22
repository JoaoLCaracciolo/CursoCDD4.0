contador = 0
for i in range(1, 10):
    numeros = float(input("Digite um numero: "))
    if numeros < 0:
        print(numeros)
        contador += 1

print(contador)