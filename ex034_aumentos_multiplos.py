exer = 'EXERCÍCIO 034'
tema = 'Aumentos Multiplos'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

sal = int(input('Digite o seu salário:'))

# Definindo faixa salarial
if sal <= 1250:
    aum = 0.15
else:
    aum = 0.1

#Calculando novo salario
nsal = (sal*aum)+sal

print(' ')
print('Seu salário de R${:.2f} terá um aumento de {}%.'.format(sal, aum*100))
print('Seu novo salário será de {:.2f}'.format(nsal))