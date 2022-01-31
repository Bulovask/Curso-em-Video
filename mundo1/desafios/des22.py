nome = str(input('Digite seu nome completo:\n ')).strip()
nomeUPPER = nome.upper() #Maiusculo
nomeLOWER = nome.lower() #Minusculo
letras = len(nome.replace(' ', ''))
letrasPrimeiroNome = len(nome.split()[0])

print('''
 seu nome é:
 	{}
 Maiúsculo:
 	{}
 Minúsculo:
 	{}
 Numero de letras sem contar espaços:
 	{}
 Número de letras do primeiro nome:
 	{}
'''.format(nome, nomeUPPER, nomeLOWER, letras, letrasPrimeiroNome))