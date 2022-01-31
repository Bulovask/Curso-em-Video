#Desafio 74

from random import randint

mi = 0
ma = 10

t = (randint(mi,ma),
     randint(mi,ma),
     randint(mi,ma),
     randint(mi,ma),
     randint(mi,ma))

s = ''
for i in t:
	s += str(i) + ' '
print(f' Os valores sorteados foram: {s}')
print(f' O maior valor sorteado foi {max(t)}')
print(f' O menor valor sorteado foi {min(t)}')