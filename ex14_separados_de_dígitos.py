exer = 'EXERCÍCIO 023'
tema = 'Separados de Dígitos'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

num = int(input('Digite um número:'))
n = str(num)
#print('Milhares: {} \nCentenas: {}\nDezenas: {}\nUnidades: {}'.format(n[0], n[1], n[2], n[3]))u
m = num // 1000
c = (num % 1000) // 100
d = ((num % 1000) % 100) // 10
u = (((num % 1000) % 100) % 10)
print(' Milhares: {}\n Centenas: {}\n Dezenas:  {}\n Unidades: {}'.format(m,c,d,u))