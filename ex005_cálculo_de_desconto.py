exer='EXERCÍCIO 005'
tema='Cálculo de Desconto'
print('{:=^100}'.format(exer))
print('{:=^100}'.format(tema))

prec=float(input('Qual o preço do produto?  R$ '))
desc=float(input('Quantos porcento de desconto que você quer dar?'))

valor=prec-(prec*desc/100)

print('\nO preco de {} reais com desconto de {}%, passa a custar {} reais.'.format(prec, desc, valor))