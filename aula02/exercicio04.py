litros = float(input("Informe quantos litros:"))
tipo = input("Informe o tipo de combustivel ETANOL(E) ou GASOLINA(G):")

if tipo == 'g' or tipo == 'G':
    preco = litros * 5.80
    print("Valor total:", preco)
elif tipo == 'e' or tipo == 'E':
    preco = litros * 4.90
    print("Valor total:", preco)
else:
    print("Valor invalido")