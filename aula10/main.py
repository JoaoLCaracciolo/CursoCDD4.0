from biblioteca import *

while True:
    escolha = input("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Escadinha\nS-sair\nEscolha uma das opções acima:")

    if escolha in "Ss":
        sair()

    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero:"))

    if escolha == "1":
        soma(n1, n2)
    elif escolha == "2":
        subtracao(n1, n2)
    elif escolha == "3":
        multiplicacao(n1, n2)
    elif escolha == "4":
        divisao(n1, n2)
    else:
        print("Digito invalido")
