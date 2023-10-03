i = 0

nVet = int(input("Digite a quantidade de vetores:"))
vet1 = [0]*nVet
vet2 = [0]*nVet
vetSoma = [0]*nVet

for i in range(nVet):
    vet1[i] = int(input(f"Digite o valor do vetor 1:"))
    vet2[i] = int(input(f"Digite o valor do vetor 2:"))
    vetSoma[i] = vet1[i] + vet2[i]

print(vetSoma)