print('{:=^100}'.format(' EXERCÍCIO 054 '))
print('{:=^100}'.format(' Grupo de Maioridade '))

from datetime import date

ano = date.today().year
ma = 0  #Número de maiores
me = 0  #Número de menores

for ent in range(0, 7):
    data = int(input('Digite o ano de nascimento:'))
    if ano - data >= 21:
        ma += 1
    else:
        me += 1

print('\nEntre as 7 pessoas, {} tem mais que 21 anos e {} tem menos.'.format(ma, me))
