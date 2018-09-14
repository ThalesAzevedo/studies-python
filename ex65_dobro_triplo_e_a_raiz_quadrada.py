exer="EXERCÍCIO 006"
tema='Dobro, Triplo e a Raiz Quadrada'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

n=float(input('Digite um número qualquer:\n'))

dn=n*2
tn=n*3
rn=n**(1/2)

print('O dobro de {} é {}'.format(n, dn))
print('O triplo de {} é {}'.format(n, tn))
print('A raiz quadrada de {} é {:.5}'.format(n, rn))