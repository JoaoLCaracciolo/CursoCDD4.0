def caractere(numero):
    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'
    else:
        return 'Z'

def media(nota1, nota2):
    media = (nota1+nota2)/2
    return media

def aprovacao(x):
    if x >= 7:
        print(f"Sua nota foi {x}\nAprovado")
    elif x < 7 and x > 4:
        print(f"Sua nota foi {x}\nRecuperação")
    else:
        print(f"Sua nota foi {x}\nReprovado")

def adicao (*notas):
    soma = 0
    for i in notas:
        soma += i
    return soma

def texto (text):
    contador = 0
    contadorT = 0
    for letra in text:
        """if letras != " ":
            contador += 1"""
        if letra in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
            contador += 1
        contadorT += 1
    for x in range(contadorT, 0, -1):
        print(text[x-1], end="")

    return contador

def newlist(a):
    a = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]
    nova_lista = [0]
    for i in a:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista