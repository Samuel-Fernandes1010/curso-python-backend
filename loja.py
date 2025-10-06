#Lojinha do miojão

from abc import ABC, abstractmethod #Importando o ABC e o abstractmethod
#classe mãe (abstrata)
class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base  = preco_base
        
    @abstractmethod
    def calcular_preco_final(self):#O método que vai emplementado obrigatóriamente nas subclasses.
        pass
    
#subclasses
    
class ProdutoFisico(Produto):
        def __init__(self, nome,preco_base, custo_frete):
            super().__init__(nome, preco_base) #inicializa o nome e o preco_base da classe mãe.
            self.custo_frete = custo_frete
            
        def calcular_preco_final(self):
            return self.preco_base + self.custo_frete

class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, taxa_servico):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico
    
    def calcular_preco_final(self):
        return self.preco_base + self.taxa_servico
    
#Decidi implementar uma "interface" pra loja, apenas adaptei a tarefa do inventário aqui.
#Agora pode adicionar, remover, listar, finalizar e fazer o teste rápido.
 
# Funções auxiliares do inventário/carrinho
def mostrar_carrinho(carrinho):

    if not carrinho:
        print('O carrinho está vazio.')
        return
    print('\n--- Carrinho de compras ---')
    for produto in carrinho:
        print(f"{produto.nome} - Preço final: R$ {produto.calcular_preco_final():.2f}")
    print('-------------------------')


def finalizar_compra(carrinho):

    print('\n=== Carrinho de Compras Final ===')
    if not carrinho:
        print("O carrinho está vazio.")
        total = 0.0
    else:
        total = 0.0
        for produto in carrinho:
            preco_final = produto.calcular_preco_final()
            print(f"{produto.nome}: R$ {preco_final:.2f}")
            total += preco_final
        print(f"\nTotal da compra: R$ {total:.2f}")
    return total



#Gerenciador de Carrinho de compras

def gerenciar_carrinho():
    print('------- Bem-vindo ao Miojão -------')
    print('Comandos disponíveis:')
    print('  [adicionar]    - adicionar produto manualmente')
    print('  [remover]      - remover produto por nome')
    print('  [ver carrinho] - ver itens no carrinho')
    print('  [teste rapido] - adicionar produtos de exemplo e finalizar automaticamente')
    print('  [finalizar]    - calcular total e encerrar')

    carrinho = []

    while True:
        comando = input('\nDigite o seu comando: ').lower().strip()

        # Normalização: remove espaços, hífens e underscores para aceitar variações:
        # ex.: "ver carrinho" -> "vercarrinho", "teste-rapido" -> "testerapido"
        cmd_normalizado = ''.join(comando.split())  # remove todos os espaços
        cmd_normalizado = cmd_normalizado.replace('-', '').replace('_', '')

        # ---------- ADICIONAR ----------
        if cmd_normalizado == 'adicionar':
            nome_item = input('Digite o nome do produto: ').strip()
            preco = input('Digite o preço base do produto: ').strip()
            extra = input('Digite o frete (se físico) ou a taxa (se digital): ').strip()
            tipo = input('Esse produto é [fisico] ou [digital]? ').lower().strip()

            # validação simples de números (aceita ponto decimal)
            if not preco.replace('.', '', 1).isdigit() or not extra.replace('.', '', 1).isdigit():
                print('Erro: preço e valores adicionais precisam ser números.')
                continue

            preco = float(preco)
            extra = float(extra)

            if tipo == 'fisico':
                produto = ProdutoFisico(nome_item, preco, extra)
            elif tipo == 'digital':
                produto = ProdutoDigital(nome_item, preco, extra)
            else:
                print('Tipo inválido. Digite "fisico" ou "digital".')
                continue

            carrinho.append(produto)
            print(f'Produto "{produto.nome}" adicionado ao carrinho!')

        # ---------- REMOVER ----------
        elif cmd_normalizado == 'remover':
            nome_item = input('Digite o nome do produto que deseja remover: ').strip()
            encontrado = False
            for i, produto in enumerate(carrinho):
                if produto.nome.lower() == nome_item.lower():
                    carrinho.pop(i)
                    print(f'O produto "{nome_item}" foi removido do carrinho.')
                    encontrado = True
                    break
            if not encontrado:
                print(f'O produto "{nome_item}" não foi encontrado.')

        # ---------- VER CARRINHO / LISTAR ----------
        # Aceita "vercarrinho", "ver carrinho", "listar"
        elif cmd_normalizado in ('vercarrinho', 'ver'):
            mostrar_carrinho(carrinho)

        # ---------- TESTE RAPIDO (adiciona itens e finaliza automaticamente) ----------
        # Aceita "testerapido", "teste rapido", "teste", etc.
        elif cmd_normalizado in ('testerapido', 'teste', 'tr'):
            print('\n=== Executando Teste Rápido ===')
            # adiciona os produtos de exemplo
            carrinho = [
                ProdutoFisico("Livro Harry Potter", 50.0, 10.0),
                ProdutoFisico("Caneca Hello World", 30.0, 8.0),
                ProdutoDigital("Teclado Virtual Automático para Programadores", 40.0, 5.0),
                ProdutoDigital("Curso Online POO", 100.0, 20.0)
            ]
            print("Foram adicionados produtos de exemplo ao seu carrinho!")
            # finaliza automaticamente
            finalizar_compra(carrinho)
            print('Finalizando compra de teste. Até mais!')
            break  # encerra o loop/programa

        # ---------- FINALIZAR ----------
        elif cmd_normalizado == 'finalizar':
            finalizar_compra(carrinho)
            print('Finalizando compra. Até mais!')
            break

        else:
            print('Comando inválido, tente novamente.')
            print('Dica: você pode digitar "ver carrinho" ou "teste rapido" (sem acentos).')


# ==============================
# Execução Principal
# ==============================
if __name__ == "__main__":
    gerenciar_carrinho()