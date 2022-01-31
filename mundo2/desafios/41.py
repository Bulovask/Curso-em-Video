#desafio 41
import datetime as dt
cdt = dt.datetime.now()
date = cdt.date()
anoAtual = int(date.today().strftime("%Y"))

print(" CONFEDERAÇÃO NACIONAL DE NATAÇÃO")

nasc = int(input(" Em que ano nasceste?\n "))

idade = anoAtual - nasc
if idade > 0:
	print(" Você tem", idade, "anos")
else:
	print(" Você não nasceu ainda!!!!")
print(" Sua categoria é", end=" ")

if idade <= 9:
	print("mirim")
elif idade <= 14:
	print("infantil")
elif idade <= 19:
	print("junior")
elif idade <= 20:
	print("sênior")
elif idade > 20:
	print("master")