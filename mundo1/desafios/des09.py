print('\033[31;47m  Tabuada de qualquer número inteiro')
n = int(input('  Digite um número inteiro:\n  => '))
p = '\n  '
#mostrando a tabuada de n
print(51 * '—', end = '')
print('{0} ×  1 = {1} {0} ×  2 = {2} {0} ×  3 = {3} {0} ×  4 = {4} {0} ×  5 = {5} {0} ×  6 = {6} {0} ×  7 = {7} {0} ×  8 = {8} {0} ×  9 = {9} {0} × 10 = {10}'.format(p+str(n), n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10))
print(51 * '_', end = '')