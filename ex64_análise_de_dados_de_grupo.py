print('{:=^100}'.format(' EXERCÍCIO 0690 '))
print('{:=^100}\n'.format(' Análise de Dados de Grupo '))

hom = mul = maisDezoito = menosVinte = 0
print('{:-^70}'.format(' Cadastre um grupo de pessoas para análise '))
while True:
    print('{:-^70}'.format(' Cadastre uma Pessoa '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção Inválida. Informe o Sexo[M/F]' )).strip().upper()[0]
    if sexo == 'M':
        hom += 1
    if sexo == 'F':
        mul += 1
    if idade <= 20 and sexo == 'F':
        menosVinte += 1
    if idade >= 18:
        maisDezoito += 1
    opcao = str(input('Novo Cadastro?[S/N]')).strip().upper()[0]
    while opcao not in 'NS':
        opcao = str(input('Opção Imválida. Deseja realizar novo cadastro? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:-^70}'.format(' Análisando Grupo '))
print(f'Foram cadastradas {hom + mul} pessoa(s), entre eles, {hom} homens e {mul} mulheres.')
print(f'{maisDezoito} pessoas com mais de 18 anos.')
print(f'E temos {menosVinte} mulheres com menos de 20 anos.')
print('-' * 70)