from random import sample
a1 = input(' Aluno 1: ')
a2 = input(' Aluno 2: ')
a3 = input(' Aluno 3: ')
a4 = input(' Aluno 4: ')

li = sample([a1, a2, a3, a4], k=4)

print(' A ordem foi:\n\t1º {};\n\t2º {};\n\t3º {};\n\t4º {}.'.format(li[0], li[1], li[2], li[3]))