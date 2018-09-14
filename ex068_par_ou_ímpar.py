print('{:=^100}'.format(' EXERCÍCIO 068 '))
print('{:=^100}\n'.format(' Par ou Ímpar '))

from random import randint
from time import sleep
cont = 0
print('Vamos jogar?\nQuantas vezes consegue me ganhar no PAR ou ÍMPAR?\n')
while True:
    escJog = str(input('Escolha PAR ou ÍMPAR [P/I]')).strip().upper()[0]
    while escJog not in 'PI':
        escJog = str(input('Opçao inválida. Escolha PAR ou ÍMPAR: [P/I]')).strip().upper()[0]
    print('Você escolheu ', end='')
    if escJog == 'P':
        print('PAR.')
        print('Computador ficou com ÍMPAR.\n')
    elif escJog == 'I':
        print('ÍMPAR.')
        print('Computador ficou com PAR.\n')

    numCom = randint(1, 10)
    numJog = int(input('Escolha um número:'))
    sleep(1)
    print('\nDô Lá Sí...')
    sleep(1)
    print('JÁÁÁ!!!\n')
    sleep(1)
    calc = numJog + numCom
    print(f'\nVocê escolheu {numJog} e o Computador escolheu {numCom}.\nA soma é igual a {calc} que é ', end='')
    if calc % 2 == 0:
        print('PAR! Então...\n')
    else:
        print('ÍMPAR! Então...\n')
    sleep(0.5)
    if calc % 2 == 0  and escJog == 'P' or calc % 2 == 1 and escJog == 'I':
        print('Você GANHOU!\n')
        cont += 1
    else:
        print('Você PERDEU!\n')
        break
if cont > 0:
    print(f'Você conseguiu me ganhar {cont} vezes seguidas. Parabéns.')
else:
    print('Você não conseguiu me ganhar nenhuma vez.')
