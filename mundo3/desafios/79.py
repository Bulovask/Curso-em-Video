#desafio 79
num = []

while True:
	v = int(input(' Digite um valor: '))
	if v not in num:
		num.append(v)
		print(' Valor adicionado com sucesso...')
	else:
		print(' Valor duplicado! Não vou adicionar...')
	
	while True:
		c = input(' Quer continuar? [S/N] ').strip()[0].upper()
		if c in 'SN':
			break
		print(' Não entendi...')
	if c == 'N':
		break

print(20 * '=-')
num.sort()
print(f' Você digitou os valores {num}')
	
	
	
