#Desafio 84
pessoas = []
dados = []
print(' Digite: ":Q" ou ":q" em Nome para sair')
while True:
	nome = input(' Nome: ')
	if nome == ':Q' or nome == ':q':
		print(' Você saiu do programa.')
		break
	peso = float(input(' Peso: '))
	print(40*'—')
	dados.append(nome)
	dados.append(peso)
	pessoas.append(dados[:])
	dados.clear()


maipeso = []
menpeso = []
for p in pessoas:
	if len(maipeso) == 0:
		maipeso = p[-1::-1]
		menpeso = p[-1::-1]
	else:
		if maipeso[0] < p[1]:
			maipeso = p[-1::-1]
		elif maipeso[0] == p[1]:
			maipeso.append(p[0])
		if menpeso[0] > p[1]:
			menpeso = p[-1::-1]
		elif menpeso[0] == p[1]:
			menpeso.append(p[0])
		

print(20 * '-+')
print(f' Ao todo você cadastrou {len(pessoas)} pessoas.')
if len(pessoas) > 0:
	print(f' O maior peso foi de {maipeso[0]}Kg. Peso de {maipeso[1:]}')
	print(f' O menor peso foi de {menpeso[0]}Kg. Peso de {menpeso[1:]}')
