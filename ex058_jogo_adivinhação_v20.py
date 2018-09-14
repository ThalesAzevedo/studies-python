print('{:=^100}'.format(' EXERCÍCIO 058 '))
print('{:=^100}\n'.format(' Jogo Adivinhação v2.0 '))

from random import randint

com = randint(1, 10)
print('Pensei em um número de 1 a 10.')
jog = int(input('Quer tentar adivinhar o número que eu pensei? '))
tent = 1

while jog != com:
    if jog > com:
        jog = int(input('Errou, tenta um número menor. '))
    if jog < com:
        jog = int(input('Errou, tenta um número maior. '))
    tent += 1

print('Acertou!!! Você acertou após {} tentativas.'.format(tent))