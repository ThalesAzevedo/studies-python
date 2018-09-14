exer = 'EXERCÍCIO 024'
tema = 'Verificando letras de uma Texto'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

cidade = str(input('Em qual cidade você mora?')).strip().lower()

print('santo' in cidade[:5])