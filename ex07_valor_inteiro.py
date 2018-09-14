exer='EXERCÍCIO 016'
tema='Valor Inteiro'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

from math import trunc

n=float(input('Digite um número real:'))

print('O número {} tem a parte inteira igual a {}'.format(n,trunc(n)))

