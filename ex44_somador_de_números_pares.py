print('{:=^100}'.format('EXERCÍCIO 050 '))
print('{:=^100}'.format(' Somador de Números Pares '))

total = 0

for ent in range(0, 6):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        total += n

print('')
print('A soma dos números pares é igual a {}.'.format(total))