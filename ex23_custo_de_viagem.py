exer = 'EXERCÍCIO 031'
tema = 'Custo de Viagem '
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

d = float(input('Qual a distância da viagem?'))

#if d <= 200:
#    p = d * 0.5
#else:
#    p = d * 0.45

p = d * 0.5 if d <= 200 else d * 0.45


print('Para a distância de {} km, o valor da passagem é de R$ {:.2f}.'.format(d, p))
