#Desafio 68
from random import randint as rd


print(20 * '=-')
print(' VAMOS JOGAR PAR OU ÍMPAR')

v = 0
while True:
	print(20 * '=-')
	n = int(input(' Diga um valor: '))
	while True:
		o = input(' Par ou Ímpar? [P/I] ').strip()[0].upper()
		if o in 'PI':
			break
	nc = rd(1,6)
	p = None
	
	b = (n + nc) % 2 == 0
	
	if b:
		p = 'DEU PAR'
	else:
		p = 'DEU ÍMPAR'
		
	
	print(40 * '-')
	print(f' Você jogou {n} e o computador {nc}.\n Total de {n+nc} {p}')
	print(40 * '-')
	
	if (b and o == 'P') or ((not b) and o == 'I'):
		print(' Você VENCEU!')
		print(' Vamos jogar novamente...')
		v += 1
	else:
		print(' Você PERDEU!')
		break

print(20 * '=-')
print(f' GAME OVER! Você venceu {v} vezes.')