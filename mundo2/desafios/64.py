#Desafio 64

c = s = 0

while True:
	n = int(input(' Digite um número inteiro [999 PARAR]: ') or 999)
	
	if n != 999:
		c += 1
		s += n
	else:
		break
		
print(' Você inseriu {} números e a soma é {}'.format(c, s))
print(' FIM')
