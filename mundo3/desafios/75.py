#Desafio 75
t = (int(input('Digite um numero: ')),
	  int(input('Digite outro numero: ')),
	  int(input('Digite mais um numero: ')),
	  int(input(' Digite o ultimo numero: ')))

print(f' Você digitou os valores {t}')
print(f' O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
	print(f' O valor 3 apareceu na posição {t.index(3)}')
else:
	print(f' O valor 3 não apareceu em nenhuma posição')

print(' Os valores pares digitados foram: ', end='')
for i in t:
	if i % 2 == 0:
		print(i, end=' ')