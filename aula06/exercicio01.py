lista_compras = ['banana', 'laranja', 'maçã']
for i in lista_compras:
    print(i)
print("-----")
lista_compras.append('carro')
for i in lista_compras:
    print(i)
print("-----")
lista_compras.insert(1, 'carro')
for i in lista_compras:
    print(i)
print("-----")
del lista_compras[3]
for i in lista_compras:
    print(i)
print("-----")
item = lista_compras.pop(-1)
print(item)
print("-----")
