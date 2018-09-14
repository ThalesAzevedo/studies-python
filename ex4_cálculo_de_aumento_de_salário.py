exer="DESAFIO 09"
tema='Cálculo de Aumento de Salário'
print('{:=^100}'.format(exer))
print('{:=^100}'.format(tema))

salario=float(input('Qual o seu salário atual?'))
aumento=float(input('Quantos porcento de aumento que você terá?'))

porc=(100+aumento)/100
valor=salario*porc

print('O salário de {} reais com {}% de aumento, passará ser {} reais.'.format(salario, aumento, valor))