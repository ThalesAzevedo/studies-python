print('{:=^100}'.format(' EXERCÍCIO 048 '))
print('{:=^100}\n'.format(' Números Impares Múltiplos de 3 '))

max = int(input('Números Ímpares múltiplos de 3 até:'))

for impar in range(0, max):
    if impar % 2 == 1 and impar % 3 == 0:
        print(impar)