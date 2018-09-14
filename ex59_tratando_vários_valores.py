print('{:=^100}'.format(' EXERCÍCIO 064 '))
print('{:=^100}\n'.format(' Tratando Vários Valores '))

n = 0
soma = -999
cont = -1
while n != 999:
    n = int(input('Digite um valor para soma[999 para finalizar]:'))
    soma += n
    cont += 1
print('Você somou {} números, e deu o total de {}.'.format(cont, soma))