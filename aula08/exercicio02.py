soma = 0
n = int(input("Quantos numero deseja colocar?"))
for i in range(n):
    numero = float(input(f"Digite o {i+1}º:"))
    soma += numero
media = soma / n
print("Soma:", soma)
print("Media:", media)