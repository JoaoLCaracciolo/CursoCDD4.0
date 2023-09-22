n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))

while n2 == 0:
    n2 = int(input("Digite um numero diferente de 0:"))

divisao = n1 / n2
print("Divisão:", divisao)