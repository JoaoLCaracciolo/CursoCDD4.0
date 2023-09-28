votosBrancos = int(input("Digite o numero de votos em brancos:"))
nulos = int(input("Digite o numero de votos nulos:"))
validos = int(input("Digite o numero de votos validos:"))

quantTotal = votosBrancos + nulos + validos

pVotosBranco = (votosBrancos / quantTotal) * 100
pNulos = (nulos / quantTotal) * 100
pvalidos = (validos / quantTotal) * 100

print(f"Percentual:\nVotos Brancos:{pVotosBranco}%\nVotos Nulos:{pNulos}%\nVotos Validos:{validos}%")