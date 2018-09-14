exer="EXERCÍCIO 010"
tema='Conversão REAL para DOLAR'
print('{:=^100}'.format(exer))
print('{:=^100}'.format(tema))

dinheiro=float(input('Qual o valor em REAIS você tem hoje?'))
dolar=float(input('Qual o valor do DOLAR hoje?'))

money=dinheiro/dolar

print('Hoje você tem o equivalente a {} DOLARES'.format(money))