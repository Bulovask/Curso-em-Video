#desafio 37
print(" Base de conversão")
n = int(input(" Digite um número inteiro na decimal:\n "))
nc = 0
print("\n 1 para binário\n 2 para octal\n 3 para hexadecimal")

op = input(" Digite o número de uma opção:\n ")
base = None

if op == "1":
	base = "binário"
	nc = bin(n)[2:]
elif op == "2":
	base = "octal"
	nc = oct(n)[2:]
elif op == "3":
	base = "hexadecimal"
	nc = hex(n)[2:]

if base != None:
	print(" O número {} convertido em {} é {}".format(n, base, nc))
else:
	print(" Desculpe, mas houve um erro, escolha uma opção válida")