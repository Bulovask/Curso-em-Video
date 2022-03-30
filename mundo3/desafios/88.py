#Desafio 88
from random import randint
from time import sleep

print(f'{"":-<51}')
print(f'{"JOGA NA MEGA SENA":^51}')
print(f'{"":-<51}')

jogos = []
q = int(input(' Quantos jogos você quer que eu sorteie? '))

for j in range(q):
	jogo = []
	while True:
		n = randint(1, 60)
		n = f'{n:0>2}'
		if n not in jogo:
			jogo.append(n)
		if len(jogo) >= 6:
			break
	jogos.append(jogo)

for i, j in enumerate(jogos):
	j.sort()
	cd = len(str(len(jogos)))
	print(f' jogo {i+1:0>{cd}} => {", ".join(j)}')
	sleep(0.1)