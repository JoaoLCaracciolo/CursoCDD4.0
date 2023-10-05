def soma(n1, n2):
    resultado = n1 + n2
    print("---------------------------------")
    print(f"Resultado da soma:{resultado}")
    print("---------------------------------")
def subtracao(n1, n2):
    resultado = n1 - n2
    print("---------------------------------")
    print(f"Resultado da subtração:{resultado}")
    print("---------------------------------")
def divisao(n1, n2):
    resultado = n1 / n2
    print("---------------------------------")
    print(f"Resultado da divisão:{resultado}")
    print("---------------------------------")
def multiplicacao(n1, n2):
    resultado = n1 * n2
    print("---------------------------------")
    print(f"Resultado da multiplicação:{resultado}")
    print("---------------------------------")
def sair():
    print("flw")
    exit()
def escadinha(n):
    for i in range(1, n+1):
        print(str(i)*i)
def escadinha2(n):
    for i in range(n+1):
        for x in range(i):
            print(x+1, end=" ")
        print()
def vogal(text):
    contador = 0
    for vogais in text:
        if vogais in "AaEeIiOoUu":
            contador += 1
    print(f"Quantidade de vogais {contador}")
def espaco(text):
    contador = 0
    for branco in text:
        if branco in " ":
            contador += 1
    print(f"Quantidade de espaços em branco {contador}")

def estoque(nome_prod,quant_prod,valorU_prod):
    valor_estoque = quant_prod * valorU_prod
    return valor_estoque
    #print(f"Nome do produto:{nome_prod}\nQuantidade de produto:{quant_prod}\nValor unitario do produto:{valorU_prod}\nValor do estoque:{valor_estoque}")
