n = int(input(' \033[37;1mDigite um número inteiro:\n  '))
a = n-1
s = n+1
print('  \033[36mO antecessor de {} é {} e o sucessor é {}.'.format(n, a, s))
print('  {}, {}, {}'.format(a, n, s))

#resolução
n = int(input(' Digite um número: '))
print(' {}, o antecessor é {} e o sucessor é {}'.format(n, n-1, n+1))
