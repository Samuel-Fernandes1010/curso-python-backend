class ContaBancaria:
    #Método construtor.
    def __init__(self,numero, titular, saldo=0, credito=1000):
        self.numero = numero
        self.titula = titular
        self.saldo = saldo
        self.credito = credito
        self.transacoes = []
        
    def depositar(self, valor):
        valor = int(input('Qual o valor do depósito?: '))
        if valor > 0:
            self.saldo += valor
            print('Saldo atualisado')
            self.transacoes.append(f'Depósito realisado de R${valor},00')
            return f'Depósito no valor de R${valor},00 realisado'
        else: return 'Erro na transação'
        
    def sacar(self, valor):
        valor = int(input('Qual o valor do saque?: '))
        if valor > 0 and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            self.transacoes.append(f'Saque realisado de R${valor},00')
            return f'Saque no valor de R${valor},00 realisado'
        else: return 'Erro na transação'
        
    def consultar_saldo(self):
        return f'O seu saldo é de R${self.saldo},00'

conta_barbara = ContaBancaria(1, 'Bárba Sousa', 500000)
conta_samuel = ContaBancaria(2, 'Samuel Fernandes', 2000, 5000)

print(conta_barbara.numero)
print(conta_samuel.numero)

print(conta_barbara.consultar_saldo())
print(conta_samuel.consultar_saldo())