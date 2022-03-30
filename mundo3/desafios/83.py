# Desafio 83
# Valide a expressão conforme os parenteses
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
	
#Resolução usando listas

pilha = []
for sim in expre:
	if sim == '(':
		pilha.append('(')
	elif sim == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break

if len(pilha) == 0:
	print(' Válida')
else:
	print(' Inválida')
		