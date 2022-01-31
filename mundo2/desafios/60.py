#Desafio 60

print(' Calculo de fatorial')
n = abs(int(input(' Digite um número inteiro positivo: ')))
c = n
v = n if n > 0 else 1

while c >= 2:
	c -= 1
	v = v * (n - (n - c))

print(' {}! = {}'.format(n, v))

#RESOLUÇÃO
'''
from math import factorial
n = int(input(' Digite um número: '))
print(' Fatorial de {} é {}'.format(n, factorial(n)))
'''

p = 1
n = int(input(' N = '))
print(' {}! = '.format(n), end = '')
while n > 0:
	print(n, '= ' if n == 1 else '× ', end = '')
	p *= n
	n -= 1
print(p)