from math import hypot
catO = float(input(' Digite a medida do cateto oposto: '))
catA = float(input(' Digite a medida do cateto adjacente: '))
hipot = hypot(catO, catA)
print(' A medida da hipotenusa do triângulo retângulo de medidas:\n\tCateto oposto: {};\n\tCateto adjacente: {}.\n É {}.'.format(catO, catA, hipot))

'''dicas de Guanabara
•no lugar de sqrt(f) posso usar (f)**(1/2)

•posso usar o math.hypot(co, ca) para calcular a hipotenusa
'''