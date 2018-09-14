exer = 'EXERCÍCIO 041'
tema = 'Categoria de Idade'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

from datetime import date

ano = date.today().year

nasc = int(input('Qual seu ano de nascimento?'))

idade = ano - nasc

cat = 'MIRIM'

if 9 < idade <= 14:
    cat = 'INFANTIL'
elif 14 < idade <= 19:
    cat = 'JUNIOR'
elif 19 < idade <= 20:
    cat = 'SÊNIOR'
elif 20 < idade:
    cat = 'MASTER'

print('Por ter {} anos, você se encaixa na categoria {}.'.format(idade, cat))