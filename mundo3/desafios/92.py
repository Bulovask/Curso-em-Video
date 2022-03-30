#Desafio 92
from datetime import datetime

dados = {
'nome': input(' Nome: '),
'idade': datetime.now().year - int(input(' Ano de nascimento: ')),
'ctps': input(' Carteira de trabalho (0 se não tiver): ')
}

if dados['ctps'] != '0':
	dados['contratação'] = int(input(' Ano de contratação: '))
	dados['salário'] = float(input(' Salário: '))
	dados['aposentadoria'] = 35 - (datetime.now().year - dados['contratação']) + dados['idade']

for k, v in dados.items():
	print(f' {k} é igual a {v}', end='\n' + 30 * '—' + '\n')