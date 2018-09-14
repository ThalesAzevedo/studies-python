exer="EXERCÍCIO 007"
tema='Média de 4 Notas'
print('{:=^100}'.format(exer))
print('{:=^100}'.format(tema))

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
n3=float(input('Digite a terceira note:'))
n4=float(input('Digite a quarta nota:'))

media=(n1+n2+n3+n4)/4

print('A sua média é de {:.2}'.format(media))