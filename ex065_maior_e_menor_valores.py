print('{:=^100}'.format(' EXERCÍCIO 065 '))
print('{:=^100}\n'.format(' Maior e Menor Valores '))

opcao = 'S'
soma = 0
cont = 0

while opcao in 'S':
    n = int(input('Digite um valor:'))
    if cont == 0:
        maior = menor = n
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    opcao = str(input('Outro número?[S/N]')).strip().upper()[0]
    cont += 1
media = soma/cont
print('')
print('Entre os {} números, o maior é {} e o menor é {}.'.format(cont, maior, menor))
print('A média entre esse números é {}'.format(media))
