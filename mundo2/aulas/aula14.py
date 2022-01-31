#Aula 14
#WHILE == ENQUANTO
posicao = 0
maca = 10

def cheguei():
	global posicao
	return posicao == maca

def passo():
	global posicao
	posicao += 1
	print(" Passo")

def pega():
	if cheguei():
		print(" Peguei a maçã")
	else:
		print(" Aqui não tem maçã")

#Exemmplo do guanabara

while not cheguei():
	passo()
pega()
print("Fim")
