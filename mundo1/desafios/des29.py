velocidade = float(input(' Velocidade em Km/h: '))

velMaxima = 80
multa = (velocidade - velMaxima) * 7

if velocidade > velMaxima:
	print(' Você foi multado em: {}, por exceder o limite de {}Km/h.'.format(multa, velMaxima))
else:
	print(' Tenha um bom dia!')