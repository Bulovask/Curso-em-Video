#Desafio 67
while True:
	print(' ' + 50 * '—')
	f = int(input(' Quer ver a tabuada de qual valor? '))
	print(' ' + 50 * '—')
	
	if f < 0:
		print(' PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
		break
	
	for f2 in range(1, 11):
		print(f' {f} × {f2} = {f * f2}')
