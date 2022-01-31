from random import randint

s = randint(0,5)
n = int(input(' Digite um número entre 0 e 5: '))
print(' Acertou!' if s == n else ' Perdeu! o número é {}.'.format(s))
