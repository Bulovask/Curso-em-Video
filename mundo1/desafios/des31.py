dist = float(input(' Distância em Km: '))

if dist <= 200:
	print('Preço da passagem é:', dist * 0.5)
else:
	print('Preço da passagem é:', dist * 0.45)
	
#maneira simplificada
print('Preço da passagem é:', dist * 0.5 if dist <= 200 else dist * 0.45)