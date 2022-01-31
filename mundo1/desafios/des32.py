from datetime import date

ano = int(input('Digite um ano: Deixe em branco para escolher o ano atual. ') or date.today().year)

por4 = ano % 4 == 0
por100 = ano % 100 == 0
por400 = ano % 400 == 0

bissexto = por4 and not (por100 and not por400)

if bissexto:
	print(' O ano {} é bissexto!'.format(ano))
else:
	print(' O ano {} não é bissexto!'.format(ano))