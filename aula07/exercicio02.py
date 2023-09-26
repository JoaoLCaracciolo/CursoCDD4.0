resposta = 's'
while resposta in 'Ss':
    numero = int(input("Digite um numero:"))
    while numero == 0:
        numero = int(input("Digite um numero diferente de 0:"))
    else:
        if numero < 0:
            print("NEGATIVO")
        else:
            print("POSITIVO")
        resposta = input("Deseja testar outro numero?(s/n)")