print('{:=^100}'.format(' EXERCÍCIO 066 '))
print('{:=^100}'.format(' Vários Números com Flag '))

cont = soma = 0
while True:
    n = int(input('Digite um valor:\n(999 para parar)'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma entre os {cont} números é igual a {soma}.')