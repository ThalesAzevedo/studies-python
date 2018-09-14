exer = 'EXERCÍCIO 018'
tema = 'Cálculo de Seno Cosseno e Tamgente'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

import math

ang = float(input('Digite o ângulo:'))
rad = math.radians(ang)

print('O ângulo de {} graus tem:'.format(ang))
print('SENO: {:.4f}'.format(math.sin(rad)))
print('COSSENO: {:.4f}'.format(math.cos(rad)))
print('TANGENTE: {:.4f}'.format(math.tan(rad)))