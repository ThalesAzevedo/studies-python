#Cria uma lista de números de 0 a 10
print('Lista de Dados:')
numbers = [i for i in range(1, 5)]
print(numbers)

import csv

help(csv)

# Função de soma dos itens de listas
def sum_itens(numlist):
    print('Soma todos os itens.')
    sum = 0
    for x in numlist:
        sum += x
    return sum

# Funçao soma 2 em cada item da lista
def sum_numbers(numlist):
    print('Soma 2 a cada item.')
    for x in range(len(numlist)):
        numlist[x] += 2
    return numlist

# Multiplicação dos itens da listas por 2
def mult_numbers(numlist):
    print('Duplicada o valor de cada item.')
    for x in range(len(numlist)):
        numlist[x] *= 2
    return numlist

# Multiplica os itens na lista
def mult_itens(numlist):
    print('Multiplica os itens da lista.')
    mult = 1
    for x in numlist:
        mult *= x
    return mult

# Chamando as funções.
print('\nResultado de Funções:')


#print(sum_numbers(numbers))
#print(sum_itens(numbers))
#print(mult_numbers(numbers))
#print(mult_itens(numbers))