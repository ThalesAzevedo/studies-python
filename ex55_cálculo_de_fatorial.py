print('{:=^100}'.format(' EXERCÍCIO 060 '))
print('{:=^100}\n'.format(' Cálculo de Fatorial '))

n = int(input('Calcule o FATORIAL de :'))
fat = 1

print('Calculando {}!...'.format(n))
while n != 1:
    fat *= n
    print(' {} x'.format(n), end='')
    n = n-1
#for f in range(n, 1, -1):
#    fat *= f
#    print(' {} x'.format(f), end='')
print(' 1 = {}'.format(fat))

