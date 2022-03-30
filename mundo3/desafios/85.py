#Desafio 85
#   impares  pares
num = [[],    []]

for i in range(1, 8):
	n = int(input(f' Digite o {i}º valor: '))
	if n % 2 == 0:
		num[1].append(n)
	else:
		num[0].append(n)

num[0].sort()
num[1].sort()

print(f' Os valores pares digitados foram:\n  {num[1]}')
print(f' Os valores impares digitados foram:\n  {num[0]}')
