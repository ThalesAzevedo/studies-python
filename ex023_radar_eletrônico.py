exer = 'EXERCÍCIO 023'
tema = 'Radar Eletrônico'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

v = int(input('Qual a velocidade do carro?'))
mult = (v - 80)*7
if v >= 80:
    print(' ')
    print('Multado por Excesso de Velocidade.\nEstava a {} Km/h e o limite é de 80 km/h.'.format(v))
    print('O valor da multa é de R${:.2f}.'.format(mult))
else:
    print('Está dentro do limite de velocidade.\nDirija com Segurança!')