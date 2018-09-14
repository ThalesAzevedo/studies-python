exer = 'EXERCÍCIO 030'
tema = 'Par ou Ímpar'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

n = int(input('Digite um número:'))

r = n % 2

print('')

if r == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))

