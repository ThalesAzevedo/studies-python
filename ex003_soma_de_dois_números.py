exer='EXERCÍCIO 003'
tema='Soma de Dois Números'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

num1=int(input('Qual é o primeiro numero?'))
num2=int(input('Você quer somar com qual número?'))

res=num1+num2

print(num1,'+',num2,'é igual a {}.'.format(res))
