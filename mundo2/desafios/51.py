#desafio 51
#leia o primeiro termo e a razão
#de uma PA e mostre os 10 primeiros
#termos da PA
#An = A1 + (n - 1) * d

a1 = float(input(' Primeiro termo da PA: '))
r = float(input(' Razão da PA: '))

sequencia = []

for n in range(1, 11):
	sequencia.append(str(round(float(a1 + (n - 1) * r), 2)))

print(' =>', ', '.join(sequencia))