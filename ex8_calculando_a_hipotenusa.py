exer = 'EXERCÍCIO 017'
tema = 'Calculando a Hipotenusa'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

import math

co=float(input('Digite o valor do Cateto Oposto:'))
ca=float(input('Digite o valor do CAteto Adjacente:'))

#hp=math.sqrt(math.pow(co,2)+math.pow(ca,2))
#hp = (ca ** 2 + co ** 2) ** (1/2)
hp = math.hypot(ca, co)
print('O valor da Hipotenusa é {}.'.format(hp))
