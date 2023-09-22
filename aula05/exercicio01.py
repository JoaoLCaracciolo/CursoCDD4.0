resposta = 's'

while resposta in 'Ss':
    n1 = float(input("Digite a 1a:"))
    n2 = float(input("Digite a 2a:"))

    while n1 < 0 or n1 > 10:
        print("Digite Valores validos(0 e 10)")
        n1 = float(input("Digite a 1a:"))
    while n2 < 0 or n2 > 10:
        print("Digite Valores validos(0 e 10)")
        n2 = float(input("Digite a 2a:"))
    media = (n1 + n2) / 2
    print(media)

    resposta = input("Deseja realizar novo calculo??(S/N)")