#IMPORTAR LIBRERIA DE CLASES ABASTRACTAS CON EL DECORADOR DEL METODO ABSTRACTO 
from abc import ABC, abstractmethod

class Formas(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod    
    def area(self):
        pass

class Circulo(Formas):
    def __init__(self, radio):
        self.radio = radio
        

    def area(self):
        return f'el area de un circulo es {3.14 * self.radio ** 2}'
    
    def perimetro(self):
        return f'El perimetro de un circulo es: {2 * 3.14 * self.radio}'
    
class Rectangulo(Formas):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return f'el area de un rectangulo es {self.base * self.altura}'
    
    def perimetro(self):
        return f'el perimetro de un rectangulo es: {2 * (self.base + self.altura)}'

class Cuadrado(Formas):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
          return f'el area de un cuadrado es {self.lado ** 2}'
    
    
#creamos una lissta (objetos)
forma = [Circulo(5), Rectangulo(10, 10), Cuadrado(4), Rectangulo(10,20), Circulo(22)]

print('area de las Forma:')
for formas in forma:
    print(formas.area())

circulo1 = Circulo(5)
print(circulo1.perimetro())


rectangulo1 = Rectangulo(10,20)
print(rectangulo1.perimetro())
  




