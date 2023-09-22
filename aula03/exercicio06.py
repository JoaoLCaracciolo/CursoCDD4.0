cont = 0
soma = 0

nAluno = int(input("Digite o numero de alunos:"))

while cont < nAluno:
    numero = float(input("Digite a Nota: "))
    soma += numero
    cont += 1

print("Media: ", soma/nAluno)