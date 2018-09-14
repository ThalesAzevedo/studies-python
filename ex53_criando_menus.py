print('{:=^100}'.format(' EXERCÍCIO 059 '))
print('{:=^100}\n'.format(' Criando Menus '))

from time import sleep
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))


opcao = 0

while opcao != 5:
    opcao = int(input("""
--------Menu--------
    [1] Somar
    [2] Multiplicar
    [3] Maior Valor
    [4] Trocar números
    [5] Sair 
    Opção:"""))
    if opcao == 1:
        print('A soma entre os valores {} e {} é {}.'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O primeiro número {} é maior.'.format(n1))
        elif n2 > n1:
            print('O segundo número {} é maior.'.format(n1))
        elif n1 ==n2:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif opcao == 5:
        print('Finalizando Programa.')
    else:
        print('Opção inválida.')
    sleep(2)