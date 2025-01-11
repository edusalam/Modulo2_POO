#EJEMPLO DE HERENCIA TRADICIONAL

class Vehiculo:
    def __init__(self, marca, modelo):
     self.marca = marca
     self.modelo = modelo
         
    def descripcion(self):
        return f'el vehiculo es de marca {self.marca}, modelo {self.modelo}'
    
class Auto(Vehiculo):
   def __init__(self, marca, modelo, puertas):
      super().__init__(marca, modelo)
      self.puertas = puertas
    
    #CON POLIMORFISMO MODIFICAMOS EL METODO O FUNCION DESCRIPCION
   def descripcion(self):
       return f'el vehiculo es de marca{self.marca}, modelo {self.modelo} y tiene {self.puertas} puertas'
   
#CREAMOS LOS OBJETOS
mi_auto = Auto('chevrolet', 'sedan',4)
print(mi_auto.descripcion())



   


    