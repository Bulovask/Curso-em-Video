#Desafio 71

print('', '=' * 35)
print(' {:^35}'.format('BANCO CEV'))
print('', '=' * 35)

while True:
	saque = input(' Que valor você quer sacar? R$').strip()
	if saque.isnumeric():
		saque = int(saque)
		break
	print(' VALOR INVÁLIDO!')

n50 = saque // 50
n20 = saque % 50 // 20
n10 = saque % 50 % 20 // 10
n1 = saque % 50 % 20 % 10 // 1

ns = [
	['50', n50],
	['20', n20],
	['10', n10],
	['1', n1]
]
for n in ns:
	if n[1] != 0:
		print(f' Total de {n[1]} cédulas de R${n[0]}')

print('', '=' * 35)
print(' Volte sempre ao BANCO CEV!\n Tenha um bom dia!')