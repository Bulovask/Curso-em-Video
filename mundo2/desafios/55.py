#Desafio 55
#Faça um programa que leia o peso de 5 pessoas e no final mostre o maior peso e menor peso

menor = None
maior = None

for i in range(1,6):
	peso = float(input(' Peso da pessoa ' + str(i) + ': '))
	if menor == None:
		menor = peso
	if maior == None:
		maior = peso
	elif peso < menor:
		menor = peso
	elif peso > maior:
		maior = peso
print(' Maior:', maior)
print(' Menor:', menor)


#####Eu poderia ter usado o max() e o min()