# Desafio 93

aproveitamento = {
	'nome': input(' Nome: '),
	'gols': [],
	'total': 0
}

nP = int(input(' Número de partidas jogadas: '))

for i in range(1, nP+1):
	numGols = int(input(f' Número de gols na {i}ª partida: '))
	aproveitamento['gols'].append(numGols)
	aproveitamento['total'] += numGols

print(30 * '=')
print(aproveitamento)
print(30 * '=')
for k, v in aproveitamento.items():
	print(f' O campo {k} tem o valor {v}.')
print(30 * '=')
print(f' O jogador {aproveitamento["nome"]} jogou {nP} partidas.')
for i, g in enumerate(aproveitamento['gols'], start=1):
	print(f'\t==> Na {i}ª partida, fez {g} gols.')
print(f' Foi um total de {aproveitamento["total"]} gols.')

