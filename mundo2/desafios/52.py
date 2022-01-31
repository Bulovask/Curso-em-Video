#desafio 52
#Teste se é primo
n = abs(int(input(' Digite um número inteiro: ') or 0))
p = True;
pd = None

if n == 0:
	p = False
	pd = 1

for i in range(2, n):
	if n % (i) == 0 or n == 0:
		p = False
		pd = i
		break

if p and n != 1:
	print(' É primo!!')
else:
	print(' Não é primo!! o primeiro divisor é', pd)