#Desafio 76

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15, 'Papel Sulfite', 20)

larg = 30
ind = 10

print(ind * ' ' + larg * '—')
print(ind * ' ' + '{1:^{0}}'.format(larg, 'LISTAGEM DE PREÇOS'))
print(ind * ' ' + larg * '—')
for i in range(len(listagem) // 2):
	print(ind * ' ' + '{1:.<{0}}R${2:>8}'.format(larg - 10, listagem[i*2], listagem[i*2+1]))
print(ind * ' ' + larg * '—')