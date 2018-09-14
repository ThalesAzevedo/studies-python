exer = 'EXERCÍCIO 033'
tema = 'Maior e Menor Valor'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

# Verificando maior valor
ma = n1

if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3

# Verificando menor valor
me = n1

if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1  and n3 < n2:
    me = n3

print('')
print('O maior número é o {} e o menor é o {}'.format(ma, me))
