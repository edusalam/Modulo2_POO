#EJERCICIO TARIFARIO ARRIENDO DE VEHICULOS
from abc import  ABC, abstractmethod
class EstrategiaTarifa(ABC):
    def calcularTarifa(self, distancia, tiempo):
        raise NotImplementedError('se debe implementar este metodo')
    

class TarifaFija(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return 300

class TarifaHora(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return tiempo * 25

class TarifaKilometro(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return distancia * 2
    
class CalculadoraTarifa:
    def __init__(self, estrategia):
        self.estrategia = estrategia
        
    def cambiarEstrategia(self, estrategia):
        self.estrategia = estrategia
    
    def calcular(self, distancia, tiempo):
        return self.estrategia.calcularTarifa(distancia, tiempo)

#creeamos los objetos
arriendo1 = TarifaFija()
calculadora = CalculadoraTarifa(arriendo1)
print('la tarifa fija: ', calculadora.calcular(10,5))

calculadora.cambiarEstrategia(TarifaHora())
print('tarifa por hora: ', calculadora.calcular(100, 2))

calculadora.cambiarEstrategia(TarifaKilometro())
print('tarifa por kilometrro: ', calculadora.calcular(100, 3))