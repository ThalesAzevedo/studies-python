print('{:=^100}'.format(' EXERCÍCIO 067 '))
print('{:=^100}\n'.format(' Tabuada v3.0 '))

while True:
    n = int(input('Deseja saber a tabuada de que número?\n[-1 para finalizar]'))
    if n < 0:
        break
    print(f'==== Tabuada de {n} ==== ')
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print('{:=^19}'.format(n))
print('Tabuada Finalizada')
