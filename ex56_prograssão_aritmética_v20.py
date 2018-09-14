print('{:=^100}'.format(' EXERCÍCIO 061 '))
print('{:=^100}\n'.format(' Prograssão Aritmética v2.0 '))

t = int(input('Informe o primeiro termo:'))
r = int(input('Informe a razão:'))
n = int(input('Informe o número de termos:'))

while n > 0:
    print('{}'.format(t), end='')
    print(' - ' if n > 1 else '', end='')
    t += r
    n -= 1

