exer='EXERCÍCIO 014'
tema='Conversão de Celsius para Fahrenheit'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

c=float(input('Digite a temperatura em Celsius:'))

f=c*1.8+32

print('A temperatura de {} Celsius é igual a {} Fahrenheit'.format(c,f))