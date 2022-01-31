from math import trunc
numero = float(input(' Digite um número: '))
print(' O número {} tem a parte inteira {}.'.format(numero, trunc(numero)))

# no lugar de trunc(2.88) posso usar int(2.88)