exer = 'EXERCÍCIO 039'
tema = 'Ano de Alistamento'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

from datetime import date

ano = date.today().year
print('O ano atual é {}'.format(ano))

sexo = int(input("""Informe seu sexo:
    [1] Masculino
    [2] Feminino \n"""))
if sexo == 1:
    nasc = int(input('Qual seu ano de nascimento?'))

    idade = ano - nasc
    prazo = idade - 18

    if prazo > 0:
        print('Você deveria ter se apresentado ao Serviço  Militar há {} ano(s).'.format(prazo))
        print('Deveria ter se apresentado em {}.'.format(nasc + 18))
    elif prazo < 0:
        print('Você deverá se apresentar ao Serviço Militar daqui a {} ano(s).'.format(str(prazo)[1:]))
        print('Deverá se apresentar em {}.'.format(nasc + 18))
    else:
        print('Você deverá se apresentar ao Serviço Militar esse ano.\nBoa Sorte.')
if sexo == 2:
    print('Por voce ser do sexo feminino, não precisa se apresentar ao Serviço Militar.')