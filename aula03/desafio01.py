h1 = int(input("Digite a hora:"))
m1 = int(input("Digite o minuto:"))
h2 = int(input("Digite a hora:"))
m2 = int(input("Digite o minuto:"))

mt = m1+m2

if h1 >= 12:
    h1 = h1-12
if h2 >= 12:
    h2 = h2-12

ht = h1 + h2

if mt >= 60:
    ht += 1
    mt = mt-60

if ht >= 12:
    ht = ht-12

print("Horario:",ht,":",mt)