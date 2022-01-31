salario = float(input('Seu salário em R$:'))

if salario > 1250:
	print('''
	Seu salário de {}, com aumento de 10%,
	passa a ser {}.
	'''.format(salario, salario * 11/10))
else:
	print('''
	Seu salário de {:.2f}, com aumento de 15%,
	passa a ser {:.2f}
	'''.format(salario, salario * 115/100))