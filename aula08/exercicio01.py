base = float(input("Digite a base:"))
while base <= 0:
    base = float(input("Digite um numero diferente de ZERO:"))

altura = float(input("Digite a altura:"))
while altura <= 0:
    altura = float(input("Digite um numero diferente de ZERO:"))

Area = (base * altura) / 2

print("Area do triangulo:", Area)
