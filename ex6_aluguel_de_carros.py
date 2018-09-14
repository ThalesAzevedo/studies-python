exer='EXERCÍCIO 015'
tema='Aluguel de Carros'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

dia=int(input('O carro está alugado por quantos dias? '))
km=float(input('Quantos quilometros foram rodados nos dias alugados? '))

precdia=dia*60
preckm=km*0.15

print('Será cobrado {:.2f} reais pelos dias alugados, e {:.2f} reais pelos quilometros rodados.'.format(precdia,preckm))
print('O valor total do aluguel do carro é de {:.2f} reais.'.format(precdia+preckm))