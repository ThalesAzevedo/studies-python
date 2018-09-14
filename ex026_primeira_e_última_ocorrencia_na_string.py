exer = 'EXERCÍCIO 026'
tema = 'Primeira e Última Ocorrencia na String'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

frase = str(input('Escreva uma frase:')).strip().lower()

print('A letra A aparece {} vezes.'.format(frase.count('a')))
print('Aparece primeiro na posição {}.'.format(frase.find('a')+1))
print('Aparece a última vez na posição {}.'.format(frase.rfind('a')+1))