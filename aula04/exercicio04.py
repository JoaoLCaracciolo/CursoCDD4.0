contadorNeg = 0
numNeg = 0
for i in range(1, 10):
    numeros = float(input("Digite um numero: "))
    if numeros < 0:
        print(numeros)
        contadorNeg += 1
        numNeg += numeros
contadorPosi = 10 - contadorNeg
print("\n---NEGATIVOS---")
print("Soma dos NEGATIVOS:", numNeg)
print("Quantidade de NEGATIVOS:", contadorNeg)
print("\n---POSITIVOS---")
print("Quantidade de POSITIVOS:", contadorPosi)
