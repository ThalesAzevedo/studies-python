print('{:=^100}'.format(' EXERCÍCIO 046 '))
print('{:=^100}'.format(' Contagem Regrassiva! '))

import emoji
from time import sleep

for fogos in range(10, 0, -1):
    print(fogos)
    sleep(1)
print(emoji.emojize(':fireworks:', use_aliases=True))