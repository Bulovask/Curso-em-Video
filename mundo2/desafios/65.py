#Desafio 65

q = 0
soma = 0
maior = None
menor = None

while True:
	n = input(' Digite um número inteiro ou Q para sair:\n ') or '0'	
	q += 1
	
	if n.upper() == 'Q':
		break
	else:
		n = int(n)
	
	if q == 1:
		maior = menor = media = soma = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n
		soma += n
		media = soma / q
	print('''
	O menor valor é: {};
	O maior valor é: {};
	A média é {}.
	'''.format(menor, maior, media))
	