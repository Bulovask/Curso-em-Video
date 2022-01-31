#Desafio 77
ps = 'Macaco','maranata','parusia','Youtube','Guilherme','bonus','Baleia','Ageu', 'Pato', 'Galo', 'Mato', 'Gato', 'Alho'

for p in ps:
	vogais = ''
	for l in p.upper():
		if l in 'AEIOU':
			vogais += l + ' '
	print(f' Na palavra {p.upper()} temos {vogais}')