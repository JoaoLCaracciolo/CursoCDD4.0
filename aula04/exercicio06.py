contador = 0
for i in range(1, 10):
    numeros = float(input("Digite um numero: "))
    if 10 <= numeros <= 20:
        contador += 1

fora = 10 - contador

print("Numeros no intervalo de 10 e 20:", contador)
print("Numeros fora do intervalor de 10 e 20: ", fora)