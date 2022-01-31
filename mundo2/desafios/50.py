#desafio 50
#leia 6 numeros inteiros e some somente os pares
s = 0
c = 0
for i in range(0, 6):
	n = int(input(' Digite um Número Inteiro: '))
	if n % 2 == 0:
		c += 1
		s += n
print(51 * '=')
print(' A soma dos {} números pares é {}'.format(c, s))
print(' Só foi considerado os números pares')
