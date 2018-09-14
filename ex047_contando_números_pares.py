print('{:=^100}'.format(' EXERCÍCIO 047 '))
print('{:=^100}'.format(' Contando Números Pares'))

max = int(input('Números pares até:'))
for par in range(2, max+1):
    if par % 2 == 0:
        print(par)