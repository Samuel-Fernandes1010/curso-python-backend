from abc import ABC, abstractmethod

import math
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area():
        pass
    @abstractmethod
    def calcular_perimetro():
        pass
    
class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return math.pi * self.raio **2
        
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
class Quadrado(Retangulo):
    def __init__(self):
        super().__init__()
    
def gerar_relatorio(formas):
    print('Relatório Formas Geométricas')
    
    for i, forma in enumerate(formas):
        
        area = forma.calcular_area
        
        perimetro = forma.calcular_perimetro
        print (forma)
        print(f'Area: {area}, Perímetro: {perimetro}')
    area_tot = sum(forma.calcular_area for forma in formas)
    perimetro_total = sum(forma.calcular_perimetro for forma in formas)
    
    print(f'Área Total: {area_tot}, Perímetro Total: {perimetro_total}')
    
#Retangulo
r = Retangulo(10, 20)
a_retangulo = r.calcular_area()
p_retangulo = r.calcular_perimetro()

print(a_retangulo)
print(p_retangulo)

#Cículo

c = Circulo(10)
a_circulo = c.calcular_area()
p_circulo = c.calcular_perimetro()

print(a_circulo)
print(p_circulo)