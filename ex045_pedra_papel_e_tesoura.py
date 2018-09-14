exer = 'EXERCÍCIO 045'
tema = 'Pedra, Papel e Tesoura'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

import emoji
from random import randint
from time import sleep

jog = int(input(emoji.emojize("""Escolha: 
    [0] Pedra   :fist:
    [1] Papel   :raised_hand:
    [2] Tesoura :v: \n""", use_aliases=True)))

com = randint(0, 2)
jogadas = ('PEDRA!:fist:', 'PAPEL!:raised_hand:', 'TESOURA!:v:')

if jog != 0 and jog != 1 and jog != 2:
    print('Opção Inválida!')
else:
    print('PEDRA...')
    sleep(0.5)
    print('PAPEL......')
    sleep(0.7)
    print('ou TESOUUUUUUUUU....')
    sleep(1)
    print('...RÁ!!!')
    sleep(1.5)
    print('')
    print(emoji.emojize('Você escolheu: {}'.format(jogadas[jog]), use_aliases=True))
    print(emoji.emojize('Computador escolheu: {}'.format(jogadas[com]), use_aliases=True))
    print('')
    sleep(1)

    if jog == 0 and com == 1 or jog == 1 and com == 2 or jog == 2 and com == 0:
        print(emoji.emojize('Dessa vez, você PERDEU!:unamused:', use_aliases=True))
    elif jog == 0 and com == 2 or jog == 1 and com == 0 or jog == 2 and com == 1:
        print(emoji.emojize('Parabéns, Você GANHOU!:smile:', use_aliases=True))
    elif jog == com:
        print('Deu EMPATE. Vamos outra!')
    sleep(3)