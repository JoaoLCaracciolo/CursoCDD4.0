n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a terceira nota:"))

media = (n1+n2+n3)/3

if media > 4:
    if media >= 7:
        print("Aprovado")
    else:
        print("Recuperação")
else:
    print("Reprovado")