#Desafio 62

print(' P.A')
A1 = float(input(' Primeiro termo: ') or 0)
r = float(input(' Razão: ') or 1)
n = 1
m = 10#int(input(' Quantos termos? ') or 10)

while m > 0:
	while n <= m:
		print('{:>10}º : {:>10}'.format(n, A1 + (n-1) * r))
		n += 1
	q = int(input(' Mais quantos termos? ') or 0)
	print('')
	if q <= 0:
		break
	m = m + q if q != 0 else 0
print(' {} Termos exibidos'.format(n - 1))
print(' FIM DO PROGRAMA')