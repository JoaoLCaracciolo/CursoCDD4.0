n1 = int(input("Digite o n1:"))
n2 = int(input("Digite o n2:"))
n3 = int(input("Digite o n3:"))

if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
elif n2 > n3:
    if n2 > n1:
        print(n2)
else:
    print(n3)
