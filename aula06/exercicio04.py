vetor_notas = ["", "", "", "", ""]
#vetor_notas = [0,0,0,0,0]

soma = 0
contador = 0

for i in range(5):
    vetor_notas[i] = float(input(f"Digite a nota do {i + 1}º aluno:"))
    #vetor_notas[i] = nota
    #vetor_notas.append(nota)

for x in range(5):
    soma += vetor_notas[x]

media = soma / 5

for y in range(5):
    if vetor_notas[y] >= media:
        contador += 1

print(f"Media da turma:{media}\nNumero de alunos na media:{contador}")
