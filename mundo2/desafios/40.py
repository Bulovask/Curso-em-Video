#desafio 40
n1 = float(input(" Digite a primeira nota(0 a 10): "))
n2 = float(input(" Digite a segunda nota(0 a 10): "))

nota = (n1 + n2) / 2

print(" Sua média é", str(nota))


if nota < 5:
	print(" Você foi reprovado(a)")
elif 7 > nota >= 5:
	print(" Você ficou de recuperação")
else:
	print(" Você foi aprovado(a)")
