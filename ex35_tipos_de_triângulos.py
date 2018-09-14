exer = 'EXERCÍCIO 042'
tema = 'Tipos de Triângulos'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

a = int(input('Comprimento da reta A:'))
b = int(input('Comprimneto da reta B:'))
c = int(input('Comprimento da reta C:'))

if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        triang = 'Equilátero'
    elif a == b or a == c or b == c:
        triang = 'Isóceles'
    else:
        triang = 'Escaleno'
    print('Essas retas podem formar um triângulo {}.'.format(triang))
else:
    print('Essas retas não podem formar um triângulo')