condição = True

if condição:
	print('Ganhou')
else:
	print('Perdeu')
	
#condição simplificada

tempo = int(input('Idade do carro: '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')

#pratica
nome = str(input('Qual seu nome'))

if nome == 'Gustavo':
	print('Que nome lindo você têm!')
else:
	print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))









