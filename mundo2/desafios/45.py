#desafio 45
from random import randint
print(" Jokenpô")

print(" 1 - pedra\n 2 - papel\n 3 - tesoura")

e = {"1": "pedra", "2": "papel", "3": "tesoura"}

j = input(" Escolha uma opção: ")
c = str(randint(1,3))

if 1 <= int(j) <= 3:
	print(" Você: {}, Computador: {}".format(e[j], e[c]))
if (c == "1" and j == "2") or (c == "2" and j == "3") or (c == "3" and j == "1"):
	print(" Você ganhou!")
elif (c == j):
	print(" Empatou!!!")
elif not (int(j) <= 3 and int(j) >= 1):
	print(" Houve um erro!!!")
else:
	print(" Computador ganhou")