exer="EXERCÍCIO 011"
tema='Cálculo de Tinta para Pintar uma Parede'
print('{:=^100}'.format(exer))
print('{:=^100}'.format(tema))

altu=float(input('Qual a altura da sua parede?'))
larg=float(input('Qual a largura da sua parede?'))

# Cada litro de tinta pinta 2 M² de parede

#area=altu*larg
#tint=area/2

tint=(altu*larg)/2

print('\nSerá necessário {} litros de tinta para pintar toda a parede.'.format(tint))