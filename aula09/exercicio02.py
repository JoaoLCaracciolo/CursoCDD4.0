nomes = [0,0,0,0,0]
senha = [0,0,0,0,0]
i = 0
x = 0
tentativa = 0
nomeT = False
senhaT = False

for i in range(2):
    nomes[i] = input(f"Digite o {i+1}º nome:")
    senha[i] = input("Digite sua senha:")
while tentativa < 3:
    print("-----LOGIN-----")
    nomeV = input("Digite seu nome:")
    for i in range(2):
    if nomeT == False:
        while tentativa < 3:
            if nomeV == senha[i]:
                tentativa = 4
                nomeT = True
                continue
            else:
                print("Nome invalido")
                senhaV = input("Digite seu nome:")
                tentativa += 1
    if nomeT == True:
        while tentativa < 3:
            senhaV = input("Informe sua senha:")
            if senhaV == senha[i]:
                print("----Login sucesso----")
                print(f"posição:{x}\nnome:{nomes[x]}\nsenha:{senha[x]}")
                tentativa = 4
                senhaT = True
            else:
                print("Senha invalida")
                tentativa += 1