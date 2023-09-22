print("-------------------TIME 01---dd----------------")
t1 = input("Digite o nome do primeiro time:")
g1 = int(input("Digite o numero de gols do Time "+t1+":"))
print("-------------------TIME 02-------------------")
t2 = input("Digite o nome do segundo time:")
g2 = int(input("Digite o numero de gols do Time "+t2+":"))

if g1 != g2:
    if g1 > g2:
        print("----------Time "+t1+" Venceu----------")
        print("Time vencedor:", t1, "\nSaldo de gols:", g1)
    else:
        print("----------Time "+t2+" Venceu----------")
        print("Time vencedor:", t2, "\nSaldo de gols:", g2)
else:
    print("Empate")