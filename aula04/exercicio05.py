contador = 0
numNeg = 0
for i in range(1, 10):
    numeros = float(input("Digite um numero: "))
    if numeros > 0:
        print(numeros)
        contador += 1
        numNeg += numeros

print(numNeg)
print(contador)