cidade = input('Nome da cidade: ').strip()

santo = cidade[:5].lower() == 'santo'

print('a cidade "{}"'.format(cidade)+'{} começa com o nome "santo"'.format(santo).replace('True', '').replace('False', ' não'))