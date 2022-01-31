print('  Calcule a quantidade de tinta necessária para pintar a parede de sua casa')
width = float(input(' Qual a largura em metros? '))
height = float(input(' Qual a altura em metros? '))
area = width * height
litros = area / 2

print('  Sua parede tem {}m² e serão necessários {:.3f}l de tinta para pinta-la. \n Considerando que 1l de tinta pinta uma área de 2m²'.format(area, litros))