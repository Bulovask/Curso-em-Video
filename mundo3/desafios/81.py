#Desafio 81
nums = []

while True:
	v = int(input(' Digite um valor: '))
	nums.append(v)
	while True:
		c = input(' Quer continuar? [S/N] ').strip()[0].upper()
		if c in 'SN':
			break
		print('Não entendi...')
	
	if c == 'N':
		break

nums.sort(reverse=True)
print(20 * '=-')
print(f''' Você digitou {len(nums)} elementos.
 Os valores em ordem decrescente são {nums}
 O valor 5 {'' if 5 in nums else 'não '}faz parte da lista!''')
