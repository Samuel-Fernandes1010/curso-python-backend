#Criando um rpg mutcho loco

from abc import ABC, abstractmethod
import time
class Personagem(ABC):
    def __init__(self, nome, vida, ataque_base):
        self.nome = nome
        self._vida = vida
        self._ataque_base = ataque_base
    
    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
    
    def esta_vivo(self):
        return self._vida > 0
    
    @abstractmethod
    def atacar(self, alvo):
        pass
    
#Criando as subclasses.
class TestePersonagem(Personagem):
    def atacar(self, alvo):
        print(f'{self.nome} atacou {alvo.nome} com {self._ataque_base} de dano.')
        alvo.receber_dano(self._ataque_base)

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque_base):
        super().__init__(nome, vida, ataque_base)
        self.__furia = 0
        
    def get_furia(self):
        return self.__furia
    
#A cada ataque que o guerreiro faz ele ganha 10 pontos de fúria, quando acumular 30 pontos de fúria automaticamente no próximo ataque é usado o ataque de fúria.
#O ataque de fúria vai dar o dobro de dano do ataque base. 
    def atacar(self, alvo):
        if self.__furia >= 30:
           self.ataque_especial(alvo)
        else:
            dano = self._ataque_base
            print(f'{self.nome} Atacou {alvo.nome} com {dano} de dano!')
            self.__furia += 10
            alvo.receber_dano(dano)
        print(f"(Fúria atual de {self.nome}: {self.__furia})")
        
    def ataque_especial(self, alvo):
        #Ataque extra que consome 30 de fúria
        if self.__furia >= 30:
            dano = self._ataque_base * 2
            print(f"{self.nome} realizou um ATAQUE ESPECIAL devastador em {alvo.nome} causando {dano} de dano!")
            alvo.receber_dano(dano)
            self.__furia -= 30
        else:
            print(f"{self.nome} tentou usar o ataque especial, mas não tem fúria suficiente!")

class Mago(Personagem):
    def __init__(self, nome, vida, ataque_base, mana):
        super().__init__(nome, vida, ataque_base)
        self.__mana = mana
        
    def get_mana(self):
        return self.__mana
#Já o mago usa mana pra fazer seus ataques que são feitiços, cada feitiço usa 10 de mana e dá 1.5x o ataque base de dano.
#Caso ele fique com menos de 10 de mana o feitiço vai valer metade de um ataque base.
#E a cada ataque fraco o mago recupera 5 de mana.
    def atacar(self, alvo):
        if self.__mana >= 10:
            dano = self._ataque_base * 1.5
            print(f'\n{self.nome} lança um feitiço em {alvo.nome} causando {dano} de dano!')
            self.__mana -= 10
        else:
            dano = self._ataque_base * 0.5
            print(f'{self.nome} está sem mana! Ataque fraco em {alvo.nome} com {dano} de dano!')
            self.__mana += 5
        alvo.receber_dano(dano)
        print(f"(Mana atual de {self.nome}: {self.__mana})")
#Senti falta de aguma solução melhor que faça o mago recuperar a mana.
        
#Teste e mais testes
if __name__ == "__main__":
    
    guerreiro1 = Guerreiro("Conan", 200, 20)
    mago1 = Mago("Merlin", 201, 20, 50)

    print('-----ARENA MEDIEVAL-----')   
    print(f"\n{guerreiro1.nome} VS {mago1.nome}")
    while guerreiro1.esta_vivo() and mago1.esta_vivo():
        print("-------------------------")
        #turno do guerreiro
        guerreiro1.atacar(mago1)
        if not mago1.esta_vivo():
            print(f'\n {mago1.nome} foi derrotado! {guerreiro1.nome} venceu a batalha')
            break
        
        #turo do mago
        mago1.atacar(guerreiro1)
        if not guerreiro1.esta_vivo():
            print(f'\n{guerreiro1.nome} foi derrotado! {mago1.nome} venceu a batalha')
            break
        
        print(f"\nVida de {guerreiro1.nome}: {guerreiro1._vida:.1f}")
        print(f"Vida de {mago1.nome}: {mago1._vida:.1f}")
        
        input('\nPrecione ENTER para o próximo turno.')#vou usar este artifício pra dar um tempo enntre os turnos e deixar um pouco interativo.
    print('\nFim da batalha! Obrigado por assistir.')