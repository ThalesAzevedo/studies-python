exer = 'EXERCÍCIO 022'
tema = 'Analisador de Texto'
print('{:=^100}'.format(exer))
print('{:=^100}'.format(tema))

nome = str(input('Digite seu nome completo:')).strip()

print('Analisando...')

print('Maiusculo:', nome.upper())
print('Minúsculo:', nome.lower())

print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(lista[0], len(lista[0])))