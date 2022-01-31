#Desafio 82
nums = []
par = []
impar = []

while True:
	n = int(input(' Digite um número: '))
	nums.append(n)
	while True:
		c = input(' Quer continuar? [S/N] ').strip()[0].upper()
		if c in 'SN':
			break
	if c == 'N':
		break

for n in nums:
	if n % 2 == 0:
		par.append(n)
	else:
		impar.append(n)

print(20 * '-=')
print(f' A lista completa é {nums}')
print(f' A lista de pares é {par}')
print(f' A lista de impares é {impar}')