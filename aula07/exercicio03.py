resp = 's'
while resp in 'Ss':
    idade = int(input("Digite sua idade:"))
    mes = int(input("Digite o mes:"))
    mesAtual = int(input("Digite o mês atual:"))

    ano = 2023 - idade

    if mesAtual <= mes:
        ano -= 1

    print(ano)
    resp = input("Deseja analisar outra idade?(s/n)")