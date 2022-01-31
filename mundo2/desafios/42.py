#desafio 42

print(" Testando triângulos")

l1 = float(input(" Lado 1: "))
l2 = float(input(" Lado 2: "))
l3 = float(input(" Lado 3: "))

if l1 + l2 >  l3 and l1 + l3 > l2 and l2 + l3 > l1:
	print(" É possível forma um triângulo com essas medidas")
	if l1 != l2 != l3 != l1:
		print(" Triângulo escaleno")
	elif l1 == l2 == l3:
		print(" Triângulo equilatero")
	else:
		print(" Triângulo isósceles")
else:
	print(" Não é possível formar um triângulo com essas medidas")