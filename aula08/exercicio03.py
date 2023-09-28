while True:
    print("--------------------------------MENU--------------------------------")
    numero = int(input("Digite um numero:"))
    antecessor = numero - 1
    sucessor = numero + 1
    resp = input("----Digite 1 ANTECESSOR----\n----Digite 2 SUCESSOR----\n----Digite 3 SAIR----\nInforme o desejado:")
    if resp == '1':
        print(f"O Antecessor de {numero} é: {antecessor}")
    elif resp == '2':
        print(f"O sucessor de {numero} é: {sucessor}")
    elif resp == '3':
        print("Você saiu do sistema!")
        break
    else:
        print("Digito invalido!")
