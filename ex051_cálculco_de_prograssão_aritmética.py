print('{:=^100}'.format(' EXERCÍCIO 051'))
print('{:=^100}\n'.format(' Cálculco de Prograssão Aritmética '))


t = int(input('Informe o primeiro termo:'))
r = int(input('Informe a razão:'))

for calc in range(t, t + (r * 10), r):     # Cálculo da PA
    print('{} - '.format(calc), end='')