print('{:=^100}'.format(' EXERCÍCIO 070 '))
print('{:=^100}\n'.format(' Estatística de Produtos '))

total = cont = contmil = baratoPreco = 0
print('{:-^50}'.format(' Adicione os Itens da Compra '))
while True:
    nome = str(input('Nome do Produto:'))
    preco = float(input('Preço:'))
    opcao = str(input('Adicinar outro Produto? [S/N]')).strip().upper()[0]
    cont += 1
    while opcao not in 'SN':
        print(opcao)
        opcao = str(input('Opção inválida. Quer adicionar outro produto?[S/N]')).strip().upper()[0]
    total += preco
    if preco >= 1000:
        contmil += 1
    while baratoPreco == 0:
        baratoPreco = preco
        baratoNome = nome
    if preco < baratoPreco:
        baratoPreco = preco
        baratoNome = nome
    if 'N' in opcao:
        break
print('{:=^50}'.format(' Finalizando Compra '))
print('O total da compra foi R${:.2f}, com {} itens.'.format(total, cont))
print(f'Tem {contmil} produto(s) que custa mais de R$ 1000,00.')
print('{} é o produto mais barato, custando R${:.2f}.'.format(baratoNome, baratoPreco))
