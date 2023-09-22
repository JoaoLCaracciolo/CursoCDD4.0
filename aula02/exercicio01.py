n1 = float(input("Informe o primeiro numero:"))
n2 = float(input("Informe o segundo numero:"))

'''if n1 == n2:
    print("\nSeus numeros são iguais\n\n", n1, n2)
else:
    if n1 > n2:
        print(n2, n1)
    else:
        print(n1, n2)'''
'''elseif n1 == n2:
    print("\nSeus numeros são iguais\n\n",n1,n2)'''
#Melhor maneira de aplicar nessa situação
if n1 != n2:
    if n1 > n2:
        print(n2, n1)
    else:
        print(n1, n2)
else:
    print("Numeros iguais")