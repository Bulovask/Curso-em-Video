frase = input(' Escreva uma frase:\n ').strip()

Acount = frase.lower().count('a')
primeiroA = frase.lower().find('a') + 1
ultimoA = frase.lower().rfind('a') + 1

print('''
 _____________________________
 |  A frase tem {} letras 'a'
 |que aparece primeiro na
 |posição {} e por último na
 |posição {}.
 —————————————————————————————
'''.format(Acount,primeiroA,ultimoA).replace('''
 |que aparece primeiro na
 |posição 0 e por último na
 |posição 0.
''', '.\n'))