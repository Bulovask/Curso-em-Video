#Desafio 73

col20 = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense'

print(f' lista de times do Brasileirão: {col20}', end='\n\n')

#Cinco primeiros colocados
print(f' Os 5 primeiros são {col20[0:5]}', end='\n\n')

#Ultimos quatro
print(f' Os 4 últimos são {col20[-4:]}', end='\n\n')

#Em ordem alfabetica
print(f' Times em ordem alfabética: {sorted(col20)}', end='\n\n')

#posicao do time da chapecoense
print(f' O chapecoense está na {col20.index("Chapecoense") + 1}º posição')