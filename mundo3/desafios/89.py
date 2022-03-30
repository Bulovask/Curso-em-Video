#Desafio 89
alunos = []
dado = []

#Primeira Parte
print(20 * '—-' +'\n Flags:\n -t, terminar;\n -a, ajuda.\n' + 20 * '—-')
while True:
	##Perguntar os dados
	while True:
		nome = input(f' Nome do {len(alunos)+1}º Aluno: ').strip()
		if nome.replace(' ', '').isalpha():
			break
	while True:
		n1 = input(' 1ª nota: ')
		if n1.replace('.','').isdigit():
			n1 = float(n1)
			break
	while True:
		n2 = input(' 2ª nota: ')
		if n2.replace('.','').isdigit():
			n2 = float(n2)
			break
			
	##Cadastrar aluno
	dado.append(nome)
	dado.append([n1, n2])
	alunos.append(dado[:])
	dado.clear()
	
	##Continuar ou terminar?
	while True:
		f = input(20 * '—-' + '\n Digite um Flag ou aperte Enter:\n  ')
		if f == '-a':
			print(20 * '—-' +'\n Flags:\n -t, terminar;\n -a, ajuda.\n' + 20 * '—-')
		elif f == '-t':
			print(' Cadastro Terminado...')
			break
		else:
			break
	if f == '-t':
		break

#Segunda Parte
##Mostrar boletim
print(20 * '#*')
print(f' {"Nº":<4}{"NOME":>10}{"MÉDIA":>10}')
print(20 * '—-')
for n, a in enumerate(alunos):
	media = (a[1][0] + a[1][1]) / 2
	print(f' {n:<4}{a[0]:>10}{media:>10}')
print(20 * '—-')
##Mostrar notas de alunos especificos
while True:
	q = False
	while True:
		n = input(' Digite o número do aluno para ver suas notas: ').strip()
		if n[0] in 'qQtT':
			q = True
			break
		elif n.isdigit() and int(n) < len(alunos):
			n = int(n)
			break
	if q:
		break
	print(20 * '-—')
	print(f' Notas de {alunos[n][0]}\n {alunos[n][1][0]} {alunos[n][1][1]}')
	print(20 * '—-')