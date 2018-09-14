print('{:=^100}'.format(' EXERCÍCIO 049 '))
print('{:=^100}\n'.format(' Tabuada v2.0 '))

n = int(input('Deseja saber a tabuade de:'))

print('{:=^16}'. format(' Tabuada '))
for mul in range(0, 11):
    print(' {} x {} = {}'.format(n, mul, n * mul))

print('=' * 16)