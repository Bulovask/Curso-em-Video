'''
\033[0;33;44m
     ↑ ↑ ↑
   style|  |
      text |
          back
          
style
•0 = none, nenhum
•1 = bold, negrito
•4 = underline, subliado
•7 = negative, inverso

text
•30 = branco, preto?
•31 = vermelho
•32 = verde
•33 = amarelo
•34 = azul
•35 = lilás
•36 = ciano
•37 = cinza, branco?

back
•40 = branco
•41 = vermelho
•42 = verde
•43 = amarelo
•44 = azul
•45 = lilás
•46 = ciano
•47 = cinza


'''
print('\033[41;37;1m Teste ')
print('\033[44;33;4m Teste ')
print('\033[0;43;35;1m Teste ')
print('\033[42;37;1m Teste ')
print('\033[0;37;1m Teste ')
print('\033[7m Teste ')
print('\033[0;1;30;47m Teste ')
print('\033[m RESET ')