nome = input('nome: ').strip()
#silva = nome.find('silva')


print(' '+nome, str('silva' in nome.lower()).replace('True', 'tem').replace('False', 'não tem'), 'o nome silva')