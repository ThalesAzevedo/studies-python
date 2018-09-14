exer = 'EXERCÍCIO 028'
tema = 'Jogo de Adivinhação'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

import random
from time import sleep

n = int(random.randint(1, 5))

tent = int(input('Pensei em um número de 1 a 5.\nTenta adivinhar!\n'))

print('Será...?')
sleep(2)

if n == tent:
    print('Parabéns! Você acertou!')
else:
    print('Você errou. Eu pensei no {} e não no {}.\nMais sorte na próxima.'.format(n, tent))

sleep(5)
