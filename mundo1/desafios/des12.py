des = 5
print(' Calcule seu desconto de {}%'.format(des))
preco = float(input(' Por favor informe o preço do produto: R$:'))
novopreco = preco * (100-des)/100
print('\n Com {}% o valor fica {:.2f}'.format(des, novopreco))

