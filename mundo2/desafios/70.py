#Desafio 70

carrinho = []

print('', 35 * '—')
print(' {:^35}'.format('LOJA SUPER BARATÃO'))
print('', 35 * '—')

while True:
	nome = input(' Nome do Produto: ')
	
	#pergunte e valide o preço
	while True:
		preco = input(' Preço: [ex.: 12,99] R$').replace(' ', '').replace('.', '').split(',')
		if 1 <= len(preco) <= 2 and preco != ['']:
			if preco[0].isnumeric() and (len(preco) == 1 or preco[1].isnumeric()):
				preco = float('.'.join(preco))
				break
	
	#Coloque no carrinho
	carrinho.append({'nome': nome, 'preco': preco})
	
	#Pergunte se quer continuar
	stop = False
	while True:
		op = input(' Quer continuar? [S/N] ').strip()[0].upper()
		if op == 'S':
			break
		elif op == 'N':
			stop = True
			break
	if stop:
		break

print(' {:—^35}'.format(' FIM DO PROGRAMA '))

t = 0
qm = 0
#     nome, preco
mb = [None, None]
for p in carrinho:
	t += p['preco']
	if p['preco'] > 1000:
		qm += 1
	if (mb[1] == None) or (p['preco'] < mb[1]):
		mb[0] = p['nome']
		mb[1] = p['preco']

ts = '{:.2f}'.format(t).replace('.', ',')
mbs = '{:.2f}'.format(mb[1]).replace('.', ',')

print(f' O total da compra foi R${ts}')
print(f' Temos {qm} produtos custando mais de R$1000')
print(f' O produto mais barato foi {mb[0]} que custa R${mbs}')