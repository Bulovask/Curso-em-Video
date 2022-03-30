#Desafio 86
matriz = []
for i in range(0,3):
	matriz.append([])
	for j in range(0,3):
		v = int(input(f' Digite um valor para [{i},{j}]: '))
		matriz[i].append(v)

for mi in matriz:
	print(end='  |')
	for mij in mi:
		print(f' {mij:^4} ', end='')
	print('|')