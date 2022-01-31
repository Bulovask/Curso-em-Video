#Desafio 61

print(' Progressão aritmética PA')
a1 = float(input(' Primeiro Termo: ') or 0)
r = float(input(' Razão da PA: ') or 1)

n = 1

while n <= 10:
	print(str(a1 + (n-1) * r) + ('' if n == 10 else '; '), end = '')
	n+=1
