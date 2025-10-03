#Sistema bancário

from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, saldo_inicial = 0):
        self.__saldo = saldo_inicial
        
    def deepositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
            print (f'Depósito de valor R${valor},00 realisado com sucesso')
        else:
            print ('Erro')
    
    def get_saldo(self): #Usar o getter
        return self.__saldo
    
    @abstractmethod()
    def sacar(self, valor):
        pass
        
        
class ContaCorrente(ContaBancaria):
    def __init__(self, taxa_operacao = 1.5, saldo_inicial = 0):
        super().__init__(saldo_inicial)
        self.__taxa_operacao = taxa_operacao
    
    def sacar(self, valor):
        custo_total = valor + self.__taxa_operacao
        
        if valor > 0 and self.get_saldo() >= custo_total:
            novo_saldo = self.get_saldo - valor
            self._ContaBancaria__saldo = novo_saldo
            print(f'Saque de R${valor},00 realisado na conta corrente. Saldo atual {self.get_saldo}.')
        
        else:
            print('Saque não realisado, saldo insuficiente')


class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros = 0.1, saldo_inicial = 0):
        super().__init__(saldo_inicial)
        self.__taxa_juros = taxa_juros
        
    def sacar(self,valor):
        
        if valor > 0 and self.get_saldo() >= valor:
            novo_saldo = self.get_saldo - valor
            self._ContaBancaria__saldo = novo_saldo
            print(f'Saque de R${valor},00 realisado na conta Poupança. Saldo atual {self.get_saldo}.')
        
        else:
            print('Saque não realisado, saldo insuficiente')
    
    def aplicar_juros(self):
        juros = self.get_saldo * self.__taxa_juros
        self.deepositar(juros)
        print(f'Juros de R${juros} aplicados na poupança.')

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.__contas = []
        
    def adicionar_conta(self, conta: ContaBancaria):
        self.contas.append(conta)
        print (f'Conta do tipo {type(conta).__name__} adicionanda para o cliente {nome}')
        
        