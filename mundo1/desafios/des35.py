print('Teste se 3 retas formam um triângulo')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

print('As retas de comprimentos:\n {};\n {};\n {}.'.format(r1, r2, r3))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
	print('Formam um triângulo.')
else:
	print('Não formam um triângulo.')