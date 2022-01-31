#Desafio 72

c = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dizesseis', 'dizessete', 'dezoito', 'dezenove', 'vinte'
while True:
	while True:
		n = int(input('Digite um número entre 0 a 20: '))
		if 0 <= n <= 20:
			break
		print('Tente novamente.', end=' ')
	print(40 * '—' + '\n' + f' Você digitou o número {c[n]}')
	while True:
		print('—' * 40)
		b = input(' Você quer continuar? [S/N]').strip()[0].upper()
		print('—' * 40)
		if b in 'SN':
			break
	if b == 'N':
		break