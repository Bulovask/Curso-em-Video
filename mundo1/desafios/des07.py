print(' \033[37mCalcule sua média a partir de duas notas')
nota1 = float(input(' Primeira nota: '))
nota2 = float(input(' Segunda nota: '))
media = (nota1 + nota2) / 2
print('\033[30;47;1m Sua média é {:.1f}'.format(media))
