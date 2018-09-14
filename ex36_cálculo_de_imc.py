exer = 'EXERCÍCIO 043'
tema = 'Cálculo de IMC'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))


altura = float(input('Informe sua altura (m):'))
peso = float(input('Informe seu peso (kg):'))

imc = peso/(altura ** 2)
minIdeal = 18.5 * (altura ** 2)
maxIdeal = 25 * (altura ** 2)
cat = 'ABAIXO DO PESO'

if 25 >= imc > 18.5:
    cat = 'PESO IDEAL'
elif 30 >= imc > 25:
    cat = 'SOBREPESO'
elif 40 >= imc > 30:
    cat = 'OBESIDADE'
elif imc > 40:
    cat = 'OBESIDADE MÓRBIDA'

print('')
print('Seu Índice de Massa Corporal é de {:.2f}.'.format(imc))
print('E você está na categoria de: {}.'.format(cat))
print('Seu peso ídeal é entre {:.1f}kg e {:.1f}kg.'.format(minIdeal, maxIdeal))