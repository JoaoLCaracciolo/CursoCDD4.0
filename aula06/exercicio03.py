quantAlunos = int(input("Quantos alunos:"))

vetor_alunos = []

for i in range(quantAlunos):
    nome = input(f"Digite o nome do {i+1}º aluno:")
    vetor_alunos.append(nome)

for y in range(quantAlunos):
    print(f"aluno na posição {y}:", vetor_alunos[y])

nAluno = input("Qual nome deseja buscar?")

for x in range(quantAlunos):
    if nAluno == vetor_alunos[x]:
        print(vetor_alunos[x])
    else:
        print("Aluno não encontrado")