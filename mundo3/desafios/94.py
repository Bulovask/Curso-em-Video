#Desafio 94

cadastros = []

print(' digite --terminar ou --t no campo nome para terminar o cadastramento')

while True:
	pessoa = {
		'nome': input(' Nome: ')
	}
	if pessoa['nome'] in ['--t', '--terminar']:
		print(' Cadastro terminado!')
		break
	while True:
		pessoa['sexo'] = input(' Sexo: ').lstrip()[0].upper()
		if pessoa['sexo'] in 'MF':
			break
		print(' Inválido!')
	while True:
		pessoa['idade'] = input(' Idade: ')
		if pessoa['idade'].isdigit():
			pessoa['idade'] = int(pessoa['idade'])
			break
		print(' Inválido!')
	
	cadastros.append(pessoa)
	print(' Pessoa cadastrada com sucesso!')

print(20 * '=-')
num = len(cadastros)
print(f' Há {num} pessoas cadastradas')
mediaIdade = 0
mulheres = []
pessoasAcimaMedia = []
for pessoa in cadastros:
	mediaIdade += pessoa['idade'] / num
	if pessoa['sexo'] == 'F':
		mulheres.append(pessoa['nome'])
	if pessoa['idade'] > mediaIdade:
		pessoasAcimaMedia.append(pessoa)

	
print(f' A média de idade é {mediaIdade}')
print(f' mulheres {mulheres}')
print(f' Lista das pessoas com idadr acima da media: {pessoasAcimaMedia}')
