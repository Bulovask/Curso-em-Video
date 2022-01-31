nome = input(' Seu nome completo:\n ').strip()
dividido = nome.split()
primeiro = dividido[0]
ultimo = dividido[len(dividido)-1]

print('''
	————————————————————————————————
	|Primeiro Nome:| {}
	————————————————————————————————
	|Último Nome: | {}
	————————————————————————————————
'''.format(primeiro, ultimo))