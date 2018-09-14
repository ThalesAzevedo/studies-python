exer = 'EXERCÍCIO 020'
tema = 'Sorteando Ordem de uma Lista'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

import random

al1 = input('Digite o nome do aluno 1:')
al2 = input('Digite o nome do aluno 2:')
al3 = input('Digite o nome do aluno 3:')
al4 = input('Digite o nome do aluno 4:')

#lista = [al1, al2, al3, al4]
random.shuffle(lista)

#print('A ordem da apresentação será:\n{}'.format(random.sample(lista, k=4)))
print('A ordem da apresentaçao será:\n{}'.format(lista))