#desafio 43
print(" Calculo de IMC")
p = float(input(" Qual o seu peso? "))
a = float(input(" Qual a sua altura? "))

imc = p / (a * a)

if imc < 18.5:
	print(" Abaixo do peso")
elif imc < 25:
	print(" Peso ideal")
elif imc <= 30:
	print(" Sobrepeso")
elif imc <= 40:
	print(" Obesidade")
elif imc > 40:
	print(" Obesidade mórbida")
