#Desafio 95

jogadores = []

while True:
	print(20 * '-—')
	jogador = {
		'nome': input(' Nome do jogador: '),
		'gols': [],
		'total': 0
	}
	nP = int(input(' Número de partidas jogadas: '))
	for i in range(1, nP+1):
		numGols = int(input(f' Número de gols na {i}ª partida: '))
		jogador['gols'].append(numGols)
		jogador['total'] += numGols
	jogadores.append(jogador)
	if input(' Continuar? ') in 'nN':
		break
print(20 * '-=')
print(f'{"cod":4} {"nome":10} {"gols":10} {"total":5}')
for cod, jogador in enumerate(jogadores):
	nome = jogador['nome']
	gols = str(jogador['gols']).replace('[', '').replace(']', '')
	total = jogador['total']
	print(f'{cod:^4} {nome:.<10} {gols:.>10} {total:.>5}')
while True:
	print(20 * '-—')
	cod = int(input('Mostrar dados de qual jogador? '))
	if 0 <= cod < len(jogadores):
		print(f'--LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"].upper()}')
		for i, gols in enumerate(jogadores[cod]['gols'], start=1):
			print(f' No {i}º jogo fez {gols} gols.')
	else:
		break
