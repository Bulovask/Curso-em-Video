#Desafio 91

from random import randint
from time import sleep

j = {}

for i in range(1, 5):
	d = randint(1, 6)
	j['jogador' + str(i)] = d
	print(f' O jogador{i} tirou {d}')
	sleep(0.2)

js = {}
m = [None, -6]

while True:
	for k, v in j.items():
		if v > m[1] and k not in js:
			m[0] = k
			m[1] = v
			
	js[m[0]] = m[1]
	m = [None, -6]
	if len(js) == 4:
		break

for n, i in enumerate(js.items(), start=1):
	k, v = i
	print(f' O {n}º lugar é {k} com {v}')
	sleep(0.3)
	
#Resolução
##Posso usar o sorted para ordenar um dicionario
from operator import itemgetter
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)

print(' Ranking')
for i, v in enumerate(ranking, start=1):
	print(f' {i}º lugar: {v[0]} tirou {v[1]}')
	sleep(0.2)