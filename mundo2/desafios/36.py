#desafio 36
c = float(input(" Preço da casa: R$:") or 0)
s = float(input(" Seu salário: R$:") or 0)
a = int(input(" Em quantos anos deseja pagar a casa?\n ") or 1)

pr = c
po = -100

if a > 0:
	pr = c / (a * 12)
if s > 0:
	po = 100 * (pr / s)

if po > 30:
	print(" O emprestimo foi negado,\n pois a prestação mensal(R$:{:.2f})\n vale {:.2f}% do salário,\n sendo que o permitido é 30% ou menos.".format(pr, po))
elif po <= 30:
	print(" O emprestimo foi aprovado,\n pois a prestação mensal(R$:{:.2f}\n vale {:.2f}% do salário,\n que é igual ou abaixo de 30%.".format(pr, po))