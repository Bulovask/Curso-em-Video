#desafio 49
n = int(input(' Escolha um número inteiro: ') or 0)

print('{:=^51}'.format('Tabuada do ' + str(n)))

for f in range(1,11):
	txt = '{0:>2} × {1} = {2:>{3}}'.format(f, n, f * n, len(str(10 * n)))
	print('{:^51}'.format(txt))
print(51 * '=')