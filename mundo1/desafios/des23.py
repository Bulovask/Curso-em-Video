numero = str(int(input(' Digite um número: ')))
numero = '0000' + numero.strip()
t = len(numero)
unidade = numero[t-1]
dezena = numero[t-2]
centena = numero[t-3]
milhar = numero[t-4]

print('''
  {} unidades;
  {} dezenas;
  {} centenas;
  {} milhares;
'''.format(unidade, dezena, centena, milhar))

num = int(input('Digite um Número: '))
mil = num//1000%10
cen = num//100%10
dez = num//10%10
uni = num//1%10

print('''
	unidade: {}
	dezena:  {}
	centena: {}
	milhar:  {}
'''.format(uni,dez,cen,mil))