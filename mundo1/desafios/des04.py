algo = input('\033[37;1m Digite algo:\033[0;32m\n ')

print(' O tipo primitivo é {}'.format(type(algo)))
print(' {} é um número? {}.'.format(algo, algo.isnumeric()))
print(' É alfabetico? {}.'.format(algo.isalpha()))
print(' É alfa-numérico? {}'.format(algo.isalnum()))
print(' Seus caractéres são ASCII? {}'.format(algo.isascii()))
print(' É decimal? {}'.format(algo.isdecimal()))
print(' É formado por dígitos? {}'.format(algo.isdigit()))
print(' É um indentificador válido? {}'.format(algo.isidentifier()))
print(' Está em minúsculo? {}'.format(algo.islower()))
print(' Está em maiúsculo? {}'.format(algo.isupper()))