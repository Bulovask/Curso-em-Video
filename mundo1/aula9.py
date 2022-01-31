#manipulando cadeias de texto
frase = 'Curso em Vídeo Python'
print(frase)
#Fatiamento
print(frase[9]) # V
print(frase[9:13]) #Víde => O 'o' não entra
print(frase[9:21]) #Vídeo Python
print(frase[9:21:2]) #VdoPto
print(frase[:5]) # Curso
print(frase[15:]) #Python
print(frase[9::3]) #VePh

#Análise
print(len(frase)) #21 caracteres
print(frase.count('o')) #3 'o' na frase
print(frase.count('o',0,13)) #1 'o' na frase[0:13]
print(frase.find('deo')) # 'deo' começou na posição 11
print(frase.find('Android')) #retorna -1 pois 'Android' não existe
print('Curso' in frase) # retorna True

#Transformação
print(frase.replace('Python','Android')) #'Curso em Vídeo Android'
print(frase.upper()) #CURSO EM VÍDEO PYTHON
print(frase.lower()) #curso em vídeo python
print(frase.capitalize()) #Curso em vídeo python
print(frase.title()) #Curso Em Vídeo Python

frase = '   Aprenda Python  '
print(frase.strip())#'Aprenda Python'
print(frase.rstrip())#'   Aprenda Python'
print(frase.lstrip())#'Aprenda Python  '

#Divisão
frase = 'Curso em Vídeo Python'
print(frase.split()) #['Curso', 'em', 'Vídeo', 'Python']

#Junção
lista = ['Curso', 'em', 'Vídeo', 'Python']
print('-'.join(lista)) #Curso-em-Vídeo-Python

###########
##PRÁTICA##
###########


print("""
         Boa tarde
  
  Olá mundo, sou eu Ageu
estudo em casa.
  Boa tarde pessoal.
     TCHAU.
""")

