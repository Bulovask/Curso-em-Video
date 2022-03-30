#Desafio 19
pessoa = {'nome': 'Ageu', 'sexo': 'M', 'idade': 19}

print(pessoa)
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

##Apagando
del pessoa['sexo']
print(pessoa.keys())

#Dicionario dentro de uma lista
e1 = {'uf': 'Pernabuco', 'sigla': 'PE'}
e2 = {'uf': 'Paraiba', 'sigla': 'PB'}
brasil = [e1, e2]

print(brasil)
