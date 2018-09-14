exer = 'EXERCÍCIO 040'
tema = 'Cálculo de Média'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

m = (n1 + n2)/2

if m >= 7:
    print('Parabens! Você está APROVADO.')
elif 7 > m >= 5:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você está REPROVADO.')

print('Sua  média foi {:.1f}.'.format(m))