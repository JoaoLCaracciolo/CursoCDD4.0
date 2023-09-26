vetor = [0,0,0,0,0,0,0,0,0,0]
vetorM = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    vetor[i] = int(input(f"Digite o {i+1}º numero:"))
multi = int(input("Digite o numero para multiplicar:"))

for x in range(10):
    vetorM[x] = vetor[x] * multi

print(vetorM)
