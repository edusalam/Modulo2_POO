#EJEMPLO DE INTERFACEZ con el decorador
from abc import ABC, abstractmethod

class FigurasGeometricas(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FigurasGeometricas):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.14 * self.radio()

    def ver_radio(self):
        return self.radio

mi_circulo = Circulo(50)
print(mi_circulo.radio)