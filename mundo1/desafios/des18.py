from math import sin, cos, tan, radians
angulo = float(input(' Digite o ângulo em graus: '))
angulog = radians(angulo)
print(' O ângulo de {} tem:\n\tSeno: {:.5f};\n\tCosseno: {:.5f};\n\tTangente: {:.5f}.'.format(angulo, sin(angulog), cos(angulog), tan(angulog)))
