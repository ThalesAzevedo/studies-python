print('{:=^100}'.format(' EXERCÍCIO 052 '))
print('{:=^100}'.format(' Identificando Números Primos '))

n = int(input('Digite um número:'))
div = 0

for cal in range(1, n + 1):
    if n % cal == 0:
        div += 1
        print('\033[34m{} \033[m'.format(cal), end='')
    else:
        print('\033[31m{} \033[m'.format(cal), end='')

if div == 2:
    print('\nO número {} é Primo.'.format(n))
else:
    print('\nO numero {} náo é Primo. E pode ser dividido por {} números.'.format(n, div))