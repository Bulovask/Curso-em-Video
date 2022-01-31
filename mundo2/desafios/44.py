#desafio 44
print(" Calculo do preço")

p = float(input(" Preço do produto: "))

print(" 1 - À vista dinheiro/cheque: 10% de desconto")
print(" 2 - À vista no cartão: 5% de desconto")
print(" 3 - Em até 2x no cartão: preço normal")
print(" 4 - 3x ou mais no cartão: 20% de juros")

f = int(input(" Forma de pagamento: "))
pn = p
if f == 1:
	pn = p * 9/10
elif f == 2:
	pn = p * 95/100
elif f == 3:
	pn = p
elif f == 4:
	pn = p * 12/10
else:
	print(' Desculpe opção invalida!')
	print(' Opção 3 foi selecionada automaticamente.')
print(" Valor:", pn)