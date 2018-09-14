print('{:=^100}'.format(' EXERCÍCIO 071 '))
print('{:=^100}\n'.format(' Contador de Cédulas Caixa Eletrônico '))

valor = int(input('Qual o valor que deseja sacar ?'))
cedValor = 50
while True:
    if valor > cedValor:
        cedTotal = valor // cedValor
        print(f'Total de {cedTotal} de R#{cedValor:.2f}.')
        valor = valor % cedValor
    elif cedValor == 50:
        cedValor = 20
    elif cedValor == 20:
        cedValor = 10
    elif cedValor == 10:
        cedValor = 1
    elif cedValor == 1:
        break

# SOLUCÄO 2
"""print('{:-^50}'.format(' Calculando Cédulas. '))
cedTotal = 0
cedValor = 50
while True:
    if valor >= cedValor:
        cedTotal += 1
        valor -= cedValor

    else:
        if cedTotal > 0:
            print(f'Total de {cedTotal} de R${cedValor:.2f}')
        cedTotal = 0
        if cedValor == 50:
            cedValor = 20
        elif cedValor ==20:
            cedValor = 10
        elif cedValor ==10:
            cedValor = 1
        elif cedValor == 1:
            break
"""


# SOLUÇAO 1
"""cont50 = cont20 = cont10 = cont1 = 0

while True:
    while valor // 50 >= 1:
        cont50 += 1
        valor -= 50
    while valor // 20 >= 1:
        cont20 += 1
        valor -= 20
    while valor // 10 >= 1:
        cont10 += 1
        valor -= 10
    while valor // 1 >= 1:
        cont1 += 1
        valor -= 1
    if valor == 0:
        break
print('{:-^50}'.format(' Contando Cédulas '))
print(f'Total de {cont50} cédulas de R$50.')
print(f'Total de {cont20} cédulas de R$20.')
print(f'Total de {cont10} cédulas de R$10.')
print(f'Total de {cont1} cédulas de R$1.')"""