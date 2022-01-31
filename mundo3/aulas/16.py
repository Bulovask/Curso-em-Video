#Aula 16
#Tuplas
####
lanches = ('Pastel', 'Coxinha', 'Sanduiche')
print(lanches)

####
num = 1, 2, 3, 4
print(num)
print(num[0:1])
#######
itens = ('abs', 'carro', 'pato', 'bota')
for pos, item in enumerate(itens):
	print(f'{pos} => {item}')

#### ordena a tupla ou lista
print(sorted(itens))

###Somar tuplas
a = 1,2,3
b = 4,5,6

print(a+b)
print(b+a)

### .count e .index
a1 = 1,2,3,4,5,6,7,8,9,3
print('count', a1.count(3))
print('index', a1.index(3))
print('index', a1.index(3, 3))

####Apagar
del(a1)