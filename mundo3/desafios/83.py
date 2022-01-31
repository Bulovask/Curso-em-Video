# Desafio 83
expre = input('Digite a expressão: ').strip()

n = 0
for l in expre:
	if l == '(':
		n += 1
	elif l == ')':
		n -= 1
		if n < 0:
			break
if n == 0:
	print(' Sua expressão é válida!')
else:
	print(' Sua expressão está errada!')