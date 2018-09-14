print('{:=^100}'.format(' EXERCÍCIO 056 '))
print('{:=^100}'.format(' Analisando Grupo de Pessoas. '))

idadeTotal = 0
idadeVelho = 0
nomeVelho = ''
mulheres = 0

for ent in range(0, 4):
    print('------ Pessoa {} ------'.format(ent + 1))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    idadeTotal += idade
    if sexo in 'Mm' and idadeVelho < idade:
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

mediaIdade = idadeTotal/4

print('')
print('A média de idade do grupo é de {:.0f} anos.'.format(mediaIdade))
print('O homem mais velho é o {}.'.format(nomeVelho))
print('Tem {} mulheres com menos de 20 anos.'.format(mulheres))