exer = 'EXERCÍCIO 038'
tema = 'Comparando Números'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('DIgite o segundo número :'))

if n1 > n2:
    print('O primeiro numero, {}, é maior que o segundo, {}.'.format(n1, n2))
elif n1 < n2:
    print('O segundo número, {}, é maior que o primeiro, {}.'.format(n2, n1))
else:
    print('O primeiro e segundo números, {} e {}, são iguais.'.format(n1, n2))