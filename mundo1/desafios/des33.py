n1 = float(input('Numero 1: '))
n2 = float(input('Numero 2: '))
n3 = float(input('Numero 3: '))

if n1 >= n2 >= n3:
	maior = n1
	medio = n2
	menor = n3
elif n1 >= n3 >= n2:
	maior = n1
	medio = n3
	menor = n2
elif n2 >= n1 >= n3:
	maior = n2
	medio = n1
	menor = n3
elif n2 >= n3 >= n1:
	maior = n2
	medio = n3
	menor = n1
elif n3 >= n1 >= n2:
	maior = n3
	medio = n1
	menor = n2
elif n3 >= n2 >= n1:
	maior = n3
	medio = n2
	menor = n1

print('o maior é {} e o menor é {}'.format(maior, menor))
	