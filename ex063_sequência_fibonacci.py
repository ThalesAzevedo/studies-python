print('{:=^100}'.format(' EXERCÍCIO 063 '))
print('{:=^100}\n'.format(' Sequência Fibonacci '))

n = int(input('Quantos termos da Sequencia Fibonacci:'))
t1 = 0
t2 = 1
print(' 0 - 1', end='')

while n - 2 > 0:
    t = t1 + t2
    print(' - ' if n > 0 else '', end='')
    print(t, end='')
    t1 = t2
    t2 = t
    n -= 1