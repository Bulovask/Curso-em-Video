#Desafio 87
somapares = 0
soma3col = 0
maior2lin = None


###Des 86
matriz = []
for i in range(0,3):
	matriz.append([])
	for j in range(0,3):
		v = int(input(f' Digite um valor para [{i},{j}]: '))
		matriz[i].append(v)

print(40*'-')
for mi in matriz:
	print(end='  |')
	for mij in mi:
		print(f' {mij:^4} ', end='')
	print('|')
###
###des 87

for i in range(len(matriz)):
	for j in range(len(matriz[0])):
		#Soma dos pares
		Mij = matriz[i][j]
		if Mij % 2 == 0:
			somapares += Mij
		#soma da terceira coluna
		if j == 2:
			soma3col += Mij
		#Maior valor da sehunda linha
		if i == 1:
			if maior2lin == None or maior2lin < Mij:
				maior2lin = Mij
				
print(40*'-')
print(f' A soma dos valores pares é {somapares}')
print(f' A soma dos valores da terceira coluna é {soma3col}')
print(f' O maior valor da segunda linha é {maior2lin}')
