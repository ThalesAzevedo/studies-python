exer="EXERCÍCIO 008"
tema='Conversão de Metros para Centímetro e Milímetro'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

m=float(input('Digite o valor em METROS para a conversão:'))

cm=m*100
mm=m*1000

print('Na conversão, {} METROS é igual á {} CENTÍMETROS e {} MILÍMETROS'.format(m, cm, mm))