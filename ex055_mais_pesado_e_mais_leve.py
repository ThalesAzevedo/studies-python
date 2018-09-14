print('{:=^100}'.format(' EXERCÍCIO 055 '))
print('{:=^100}'.format(' Mais pesado e mais leve. '))

for ent in range(0, 5):
    peso = float(input('Digite o peso da pessoa {}:'.format(ent + 1)))
    if ent == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('A pessoa mais pesada tem {}kg.\nE a pessoa mais leve tem {}kg.'.format(maior, menor))