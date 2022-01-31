#desafio 78
valores = []

for i in range(0,5):
	valores.append(int(input(f' Digite um valor para a Posição {i}: ')))

maior = max(valores)
menor = min(valores)

print(20 * '=-')
print(f' O maior valor digitado foi {maior} nas posições ', end = '')
for i, v in enumerate(valores):
	if v == maior:
		print(f'{i}...', end='')

print(f'\n O menor valor digitado foi {menor} nas posições ', end = '')
for i, v in enumerate(valores):
	if v == menor:
		print(f'{i}...', end='')
