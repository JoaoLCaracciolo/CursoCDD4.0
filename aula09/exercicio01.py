numero = ["","","","",""]
i = 0
for i in range(5):
    numero[i] = int(input(f"Digite o {i+1}º numero:"))

for i in range(i, -1, -1):
    print(numero[i], end=" ")
