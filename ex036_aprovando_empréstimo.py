exer = 'EXERCÍCIO 036'
tema = 'Aprovando Empréstimo'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))


val = float(input('Qual o valor da casa?'))
sal = float(input('Qual o seu salário?'))
ano = int(input('Pretende pagar em quantos anos?'))

prest = val/(ano * 12)

print('O valor da prestação de uma casa de R${:.2f} para ser paga em {} anos é de R${:.2f}.'.format(val, ano, prest))

if prest >= sal*0.3:
    print('A prestação de R${:.2f} é maior que 30% do salário de R${:.2f}, que é R${:.2f}'.format(prest, sal, sal * 0.3))
    print('Seu empréstimo foi {}NEGADO{}.'.format('\033[31m', '\033[m'))
else:
    print('Seu empréstimo foi {}APROVADO{}.'.format('\033[36m', '\033[m'))