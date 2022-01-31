#Desafio 59

n1 = float(input(' Digite um valor: ') or 0)
n2 = float(input(' Digite outro valor: ') or 0)

e = None

while e != 5:
	print(' Os números escolhidos são:\n  {} e {}'.format(n1, n2))
	print(''' [1] somar
 [2] multiplicar
 [3] maior
 [4] novos números
 [5] sair do programa
 ''')
	
	e = int(input(' Digite o número da opção: ') or 0)
	
	print(51 * "=")
	
	if e == 1:
		print(' {} + {} = {}'.format(n1, n2, n1 + n2))
	elif e == 2:
		print(' {} × {} = {}'.format(n1, n2, n1 * n2))
	elif e == 3:
		print(' {} >= {}'.format(max(n1, n2), min(n1, n2)))
	elif e == 4:
		n1 = float(input(' Digite um valor: ') or 0)
		n2 = float(input(' Digite outro valor: ') or 0)
	elif e == 5:
		print(' Saindo do programa...')
	else:
		print(' "{}" não é uma opção válida'.format(e))
	print(10 * '==-==' + '-')