print(' Veja quanto vai ganhar com o aumento')
aumento = 15
salario = float(input(' Por favor, qual o seu salário? R$:'))
novosalario = salario * (100 + aumento) / 100
print('\n Então, com o aumento de {}% seu novo salário será:\n {:.2f} Reais'.format(aumento, novosalario))
