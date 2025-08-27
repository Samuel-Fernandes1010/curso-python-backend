print('-------Bem-vindo ao carrinho de compras-------')

carrinho = []

print('Comandos disponíveis: [adicionar], [listar] e [finalizar')

comando = input('Oque você deseja fazer? ').lower()

if comando == 'finalizar':
    print('Finalizando a sua compra')
    breakpoint()
elif comando == 'adicionar':
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input(f'Digite o preço do {nome_produto}: '))
    
    produto = {
        'nome': nome_produto,
        'preco': preco_produto
    }

    carrinho.append(produto)
    print(f'{nome_produto} adicionado ao carrinho com sucesso!')
    print(carrinho)

elif comando == 'listar':
    if len(carrinho) == 0:
        print('Seu carrinho está vazio')
    else:
        print('Total de itens: ', len(carrinho))
        print(carrinho)

else:
    print('Comando inválido, por favor digite um comando válido')