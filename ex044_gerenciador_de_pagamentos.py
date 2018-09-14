print('{:=^100}'.format(' EXERÍCIO 044 '))
print('{:=^100}\n'.format(' Gerenciador de Pagamentos '))

preco = float(input('Informe o valor da compra:R$'))
pag = int(input("""Digite o número da forma de pagamento:
    [1] À vista(Dinheiro/Cheque)
    [2] À vista (Cartão)
    [3] 2X no Cartão
    [4] 3X ou mais no Cartão\n"""))

if pag == 1:
    taxa = 0.9
    forma = 'A vista (Dinheiro/Cheque)'
elif pag == 2:
    taxa = 0.95
    forma = 'À vista (Cartão)'
elif pag == 3:
    parc = 2
    taxa = 1
    forma = '2x no Cartão'
elif pag == 4:
    parc = int(input('Parcelado em quantas vezes?'))
    taxa = 1.2
    forma = '{}x no Cartão'.format(parc)
else:
    print('Opção inválida. Reinicie.')

preco = preco * taxa

print('Com pagamento {},o valor da compra será igual a R${:.2f}.'.format(forma, preco))
if pag == 4 or pag == 3:
    print('Será parcelado em {} vezes de R${:.2f}.'.format(parc, preco / parc))
