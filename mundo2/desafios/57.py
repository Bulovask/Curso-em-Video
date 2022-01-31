#desafio 57
#Valide se o sexo digitado é válido
# M e F são válidos
sexo = None

while not (sexo == 'M' or sexo == 'F'):
	if not sexo == None:
		print(' Opção inválida, digite novamente!')
	sexo = input(' Digite seu sexo[M/F]: ').strip().upper()[0]

s = 'Masculino' if sexo == 'M' else 'Feminino'
print(' Seu sexo é:', s)

###Resolução

sexo = input(' Informe seu sexo [M/F]: ').lstrip()[0].upper()

while not (sexo == 'M' or sexo == 'F'):
	sexo = input(' Dado invalido, informe seu sexo [M/F]: ').lstrip()[0].upper()

print(' Sexo cadastrado:', sexo)