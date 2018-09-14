exer = 'EXERCÍCIO 019'
tema = 'Sorteando Um Item'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

from random import choice

al01 = input('Digite o nome do aluno 1:')
al02 = input('Digite o nome do aluno 2:')
al03 = input('Digite o nome do aluno 3:')
al04 = input('Digite o nome do aluno 4:')

print('\nO aluno escolhido foi {}'.format(choice([al01, al02, al03, al04])))
