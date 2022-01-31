#Desafio 53
#Teste se é palíndromo

frase = input(' Digite uma frase:\n ')
frase = frase.replace(' ', '').lower();
inverso = frase[::-1]
p = True

for i in range(len(frase) - 1, -1, -1):
	if frase[i] != frase[len(frase) - i - 1]:
		p = False
		break
print(' o inverso de {} é {}'.format(frase.upper(), inverso.upper()))
if p:
	print(' A frase é um palíndromo')
else:
	print(' A frase não é um palíndromo')
