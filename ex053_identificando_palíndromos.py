print('{:=^100}'.format(' EXERCÍCIO 053 '))
print('{:=^100}'.format(' Identificando Palíndromos '))

frase = str(input('Escreva uma frase:')).strip().upper().split()
junto = ''.join(frase)
inverso = ''

print(junto)

inverso = junto[::-1]
#for letra in range(len(junto)-1, -1, -1):
#   inverso += junto[letra]

print(inverso)

if junto == inverso:
    print('\nEssa frase é um Palíndromo.')
else:
    print('Essa frase não é um Palíndromo.')
