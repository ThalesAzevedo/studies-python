exer = 'EXERCÍCIO 027'
tema = 'Primeiro e Ultimo Nome'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

nome = str(input('Digite o nome completo:')).strip()

div = nome.split()

print('Seu primeiro e último nomes são: {} {}'.format(div[0], div[len(div) - 1]))