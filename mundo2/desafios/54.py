#Desafio 54
#Ler o ano de nascimento de 7 pessoas
#e dizer quantas pessoas são maior de idade
#e quantas são menor de idade
#21 anos é considerado maior de idade

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for i in range(1,8):
	ano = int(input(' Ano de nascimento da pessoa ' + str(i) + ': '))
	idade = atual - ano
	if idade >= 21:
		maior += 1
	else:
		menor += 1
		
print(' {} pessoas são maior de idade e {} são menor de idade'.format(maior, menor))