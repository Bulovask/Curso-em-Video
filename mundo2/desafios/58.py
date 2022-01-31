#Desafio 58

from random import randint as ri

n = ri(0,10)
e = None
t = 0

print('Olá eu sou um PROGRAMA, euquero brincar mais você(na verdade fui programado para isso) você tem que acerta o número que eu pensei tá certo? vamos brincar!!!')

while n != e:
	if e != None:
		print(' Errou!!!')
	e = int(input(' Digite um número inteiro de 0 a 10: '))
	t += 1
	if e < n:
		print(' Maior...')
	elif e > n:
		print(' Menor...')
	
print(' Você acertou na {}ª tentativa, o número era {}'.format(t, n))