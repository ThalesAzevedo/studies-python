exer = 'EXERCÍCIO 035'
tema = 'Analisando Triangulos'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

a = float(input('Comprimento da reta A:'))
b = float(input('Comprimento da reta B:'))
c = float(input('Comprimento da reta C:'))

if a < b + c and b < a + c and c < a + b:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essa retas não podem formar um triângulo')