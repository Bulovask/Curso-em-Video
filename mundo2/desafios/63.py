#Desafio 63

print(' SEQUÊNCIA DE FIBONACCI')
n = int(input(' Quantos termos? (10):') or 10)

a1 = 1
a2 = 0
an = None
sequencia = ['0']

while n > 1:
	an = a1 + a2
	
	sequencia.append(str(an))
	
	a1 = a2
	a2 = an
	
	n -= 1

print('=>',', '.join(sequencia))
