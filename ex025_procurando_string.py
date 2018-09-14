exer = 'EXERCÍCIO 025'
tema = 'Procurando String'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

nome = str(input('Qual seu nome completo?')).strip().upper()

print('Seu nome tem "Silva"?', 'SILVA' in nome)