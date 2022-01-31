#Aula 17
#lista

l = [9,6,9,6,9,5,4,3,8,10]

print(' ' + str(l))

for c, v in enumerate(l):
	print(f' {c} => {v}')
print(' fim')

########
#copia##
########
a = [1,2,3]
b = a[:]