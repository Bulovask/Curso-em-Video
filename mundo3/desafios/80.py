#Desafio 80
num = []

for i in range(5):
	n = int(input(' Digite um valor: '))
	if i == 0:
		num.append(n)
		print(' Adicionado no final da lista...')
		continue
	l = len(num)
	for j, v in enumerate(num):
		if n < v:
			num.insert(j, n)
			print(f' Adicionado na posição {j} da lista...')
			break
	if l == len(num):
		num.append(n)
		print(' Adicionado ao final da lista...')

print(20 * '=-')
print(f' Os valores digitados em ordem foram {num}')
