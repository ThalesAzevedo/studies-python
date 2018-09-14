print('{:=^100}'.format(' EXERCÍCIO 057 '))
print('{:=^100}\n'.format(' Validaçao de Dados '))

sexo = str(input('Informe seu sexo {M/F]:'))
while sexo not in 'MmFf':
    print('Opções Inválida.')
    sexo = str(input('Informe seu sexo {M/F]:'))
print('Sexo {} registrado.'.format(sexo.upper()))