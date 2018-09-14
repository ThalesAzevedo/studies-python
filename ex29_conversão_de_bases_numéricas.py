exer = 'EXERCÍCIO 037'
tema = 'conversão de bases numéricas'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

nd = int(input('Digite o número que deseja converter:'))
base = int(input("""Deseja converter para qual base? 
    Digite [1] para binário.
    Digite [2] para octal.
    Digite [3] para hexadecimal.\n"""))

if base == 1:
    nb = bin(nd)
    print('{} em decimal é igual a {} em binário.'.format(nd, nb[2:]))
elif base == 2:
    no = oct(nd)
    print('{} em decimal é igual a {} em octal'.format(nd, no[2:]))
elif base == 3:
    nh = hex(nd)
    print('{} em decimal é igual a {} em hexadecimal'.format(nd, nh[2:]))
else:
    print('Opcões inválida.')