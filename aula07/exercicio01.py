resposta = 'S'
while resposta in 'Ss':
    n1 = float(input("Digite o primeiro numero:"))
    n2 = float(input("Digite o segundo numero:"))

    media = (n1 + n2) / 2

    if media < 4:
        print("Reprovado")

    elif media >= 7:
        print("Aprovado")

    else:
        print("recuperação")

    print("Media:", media)

    resposta = input("Deseja verificar outro aluno?(S/N)")
