print('{:=^100}'.format(' EXERCÍCIO 062 '))
print('{:=^100}\n'.format(' Prograssão Aritmética v3.0 '))

t = int(input('Informe o primeiro termo:'))
r = int(input('Informe a razão:'))
n = int(input('Informe o número de termos:'))
cont = 0
print('')
while n != 0:
    while n + 1 > 1:
        print('{}'.format(t), end='')
        print(' - ' if n > 1 else '', end='')
        t += r
        n -= 1
        cont += 1
    n = int(input('\nQuer mostrar quantos termos a mais?'))
print('Foram gerados {} termos da PA.'.format(cont))