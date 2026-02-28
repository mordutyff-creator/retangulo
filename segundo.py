print ("Prepare 2 pontos x e y que pertencem a um referencial cartesiano")
ponto_1x = float(input("Coloque a abcissa (x) do primeiro ponto: "))
ponto_1y = float(input("Coloque a ordenada (y) do primeiro ponto: "))
ponto_2x = float(input("Coloque a abcissa (x) do segundo ponto: "))
ponto_2y = float(input("Coloque a ordenada (y) do segundo ponto: "))
print("O seu primeiro ponto é:", "(", ponto_1x, ",", ponto_1y, ")")
print("O seu segundo ponto é:", "(", ponto_2x, ",", ponto_2y, ")")
ponto_inseridox = float(input("Coloque a abcissa (x) que quer verificar se pertence ao retângulo: "))
ponto_inseridoy = float(input("Coloque a ordenada (y) que quer verificar se pertence ao retângulo: "))
if ponto_1x <= ponto_inseridox <= ponto_2x and ponto_1y <= ponto_inseridoy <= ponto_2y:
    print ("O seu ponto pertence ao retângulo!")
elif ponto_2x <= ponto_inseridox <= ponto_1x and ponto_2y <= ponto_inseridoy <= ponto_1y:
    print ("O seu ponto pertence ao retângulo!")
else:
    print ("O seu ponto não pertence ao retângulo!")