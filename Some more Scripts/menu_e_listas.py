list_nomes = []
while True:
    menu = int(input("""
============= Escolhe uma Ação =============
        [1] Adicionar 
        [2] Remover
        [3] Exibir
        [4] Sair"""))
    if menu == 1:
        print(f'------ADICIONANDO NOME------')
        addNome = str(input('Digite umm nome:'))
        list_nomes += [addNome]
    if menu == 2:
        print('------REMOVENDO NOME------')
        print(list_nomes)
        subNome = str(input('Escolhe o número do item para remover da lista.'))
        list_nomes -= [subNome]
    if menu == 3:
        print('------EXIBINDO LISTA------')
        print(list_nomes)
    if menu == 4:
        print('------SAINDO DO PROGRAMA------')
        break