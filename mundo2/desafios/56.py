#Desafio 56
#desenvolva um programa que leia o
#nome, idade e sexo de 4 pessoas.
#no final do programa mostre:
#a média de idade do grupo
#qual o nome do homem mais velho
#quantas mulheres têm menos de 20 anos

lista = []

#leia as informações
for i in range(1,5):
	print('\n Pessoa {} digite suas informações'.format(i))
	pessoa = {
		'nome': input(' Nome: ').strip(),
		'idade': int(input(' Idade: ')),
		'sexo': input(' Sexo, M ou F: ').upper()
	}
	
	lista.append(pessoa)

#média de idade do grupo
#O nome do home mais velho
media = 0
nome = 'Ninguém'
idade = None
num = 0
for o in lista:
	media += o['idade']
	
	if o['sexo'] == 'M':
		if idade == None:
			idade = o['idade']
			nome = o['nome']
		elif o['idade'] > idade:
			idade = o['idade']
			nome = o['nome']
	elif o['sexo'] == 'F':
		if o['idade'] < 20:
			num += 1
	
media /= len(lista)
print(' A média das idades do grupo é', media)
print(' O nome do homem mais velho é', nome)
print(' Tem {} mulheres com menos de 20 anos'.format(num))
