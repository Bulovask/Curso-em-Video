#Desafio 48
#Soma dos números impares que 
#são multiplos de 3 que se 
#encontram no intervalo de 1 a 500
q = 0
s = 0
for n in range(3, 500, 6):
	s += n
	q += 1
	print(' ',n)
print(' A soma dos {} solicitados é {}'.format(q, s))
