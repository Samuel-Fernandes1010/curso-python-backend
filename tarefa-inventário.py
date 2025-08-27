print('-------Bem-vindo ao seu inventário.-------')

#Primeiro apresenton os comandos que podem ser usados.
print('Comandos disponíveis: [adicionar], [remover], [listar] e [sair]')
inventario = []
#Coleta de dados/tratamento.

while True:
    #O .strip serve para eliminar qualquer espaço que esteja sobrando na minha resposta assim evitando de quebrar o código caso o usuário digite um espaço sem querer.
    comando = input('Digite o seu comando: ').lower().strip()
    if comando == 'adicionar':
        nome_item = input('Digite o nome do item: ').strip()
        quantidade_string = input('Digite a quantidade do item: ').strip()
       #Aqui estou fazendo uma transformação já que o "número" que vou breceber na verdade é uma string.
       #POderia usar um "float(input('Digite a quantidade do item: ')).strip" mas se a pessoa digitasse um texto o meu código quebraria.
        if quantidade_string.isdigit():
            quantidade = float(quantidade_string)
            item = {
                'nome': nome_item,
                'quantidade': quantidade
            } 
            inventario.append(item)
            print(f'Foram adicionados {quantidade} unidanes do item {nome_item}')
        else:
            print('Valor inválido, por favor digite novamente')
    elif comando == 'remover':
        nome_item = input('Digite o nome do item que deseja remover: ').strip()
        #Vou criar uma variável para verificar se o item foi encontrado.
        encontrado = False
        #E criar um contador pra percorrer o inventário.
        i = 0
        
        while i < len(inventario):
            if inventario[i]['nome'] == nome_item:
                inventario.pop(i)
                print(f'O item {nome_item} foi removido do inventário.')
                encontrado = True
                break
            i += 1

        if not encontrado:
            print(f'O item {nome_item} não foi encontrado no inventário.')

    elif comando == 'listar':
        if len(inventario) == 0:
            print('O inventário está vazio.')
        else:
            i = 0
            while i < len(inventario):
                print(' ')
                print(f"Item: {inventario[i]['nome']}, Quantidade: {inventario[i]['quantidade']}")
                i += 1
                print(' ')
    elif comando == 'sair':
        print('Saindo do inventário. Até mais!')
        break

    else:
        print('Comando invalido digite outro comando')