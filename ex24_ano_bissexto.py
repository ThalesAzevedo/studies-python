exer = 'EXERCÍCIO 032'
tema = 'Ano Bissexto'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

from datetime import date
import colorsys

ano = int(input('Digite um ano para saber se ele é bissexto.\nPara analisar o ano atual digite 0:'))

if ano ==0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano de {} é bissexto'.format(ano))
else:
    print('O Ano {} não é bissexto.'.format(ano))
