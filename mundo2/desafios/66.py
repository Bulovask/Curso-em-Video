#Desafio 66

q = s = 0
while True:
	v = int(input(' Digite um valor (999 faz parar): '))
	if v == 999:
		break
	q += 1
	s += v
print(f' A soma dos {q} valores foi {s}!')