#desafio 39
from datetime import date
print("  Alistamento Militar")

nasc = int(input(" Ano de nascimento: "))
ano = date.today().year
tempo = ano - nasc

print(" O ano atual é", ano)
print(" Você nasceu em", nasc)
if tempo > 0:
	print(" Logo sua idade é", tempo)
else:
	print(" Você não nasceu ainda!!!!")

if tempo == 18:
	print(" É hora de se alistar")
elif tempo < 18:
	print(" Ainda vai se alistar")
	print(" Em {} anos".format(18 - tempo))
	print(" Em", nasc + 18)
else:
	print(" Já passou do tempo do alistamento")
	print(" Faz {} anos que você devia ter se alistado".format(tempo - 18))
	print(" Você deveria ter se alistado em", nasc + 18)
