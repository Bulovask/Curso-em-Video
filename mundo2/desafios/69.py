# DESAFIO 69
pessoas = []


while True:
	print('', 25 * '-')
	print('', '{:^25}'.format('CADASTRE UMA PESSOA'))
	print('', 25 * '-')
	
	#Pergunte a idade
	while True:
		idade = input(' Idade: ').strip()
		if idade.isnumeric():
			idade = int(idade)
			break
	#Pergunte o Sexo
	while True:
		sexo = input(' Sexo: [M/F] ').strip()[0].upper()
		if sexo == 'M' or sexo == 'F':
			break
	#Cadastre pessoa
	pessoas.append({'sexo': sexo, 'idade': idade})
	
	#Pergunta se quer continuar ou parar
	stop = False
	
	while True:
		op = input(' Quer continuar? [S/N] ').strip()[0].upper()
		if op == 'N':
			stop = True
			break
		elif op == 'S':
			break
	
	if stop:
		break

print(' ======= FIM DO PROGRAMA =======', end = '\n\n')

#Quantidade de pessoas com mais de 18 anos
q18 = 0
hc = 0
m20 = 0
for p in pessoas:
	if p['idade'] > 18:
		q18 += 1
	if p['sexo'] == 'M':
		hc += 1
	elif p['idade'] < 20:
		m20 += 1


print(f' Total de pessoas com mais de 18 anos: {q18}')
print(f' Ao todo temos {hc} homens cadastrados')
print(f' E temos {m20} mulheres com menos de 20 anos')