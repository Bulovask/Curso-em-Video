#Desafio 90

aluno = dict()
aluno['Nome'] = input(' Nome do aluno: ')
aluno['Média'] = float(input(' Média do aluno: '))
if aluno['Média'] < 7:
	aluno['Situação'] = 'Reprovado'
else:
	aluno['Situação'] = 'Aprovado'

for k, v in aluno.items():
	print(f' {k} é igual a {v}')
