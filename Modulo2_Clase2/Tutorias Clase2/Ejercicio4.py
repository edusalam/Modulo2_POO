#AGREGUE UN METODO MOSTRAR_INFO A COCHE PARA MOSTRAR LOS DETALLES DEL VEHICULO
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_informacion(self):
        print(f'marca: {self.marca}, Modelo: {self.modelo}, Puertas: {self.puertas}')

    
class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
  
    
    

#moto1 = Moto('pulsar', 'A150', 4)
coche1 = Coche('ford', 'Mustand', 4) 
coche1.mostrar_informacion()

print(coche1.marca)
print(coche1.modelo)
print(coche1.puertas)

#print(moto1.marca)
#print(moto1.modelo)
print()
