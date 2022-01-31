#DESAFIO 46
from time import sleep

for s in range(10, -1, -1):
	print(' {:0>2} Segundos restantes'.format(s))
	if s > 0:
		sleep(1)
print(' Boom!!!!')