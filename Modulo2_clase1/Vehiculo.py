#ejercicio de HERENCIA
class Vehiculo:
    def __init__(self, tipo)
        self.tipo = tipo

    def descripcion(self):
        return f'este vehiculo es de tipo {self.tipo}'
class Moto(Vehiculo):

    def __init__(self, tipo, marca):
        #palabra reservada super
        super().__init__(tipo) #atributo de la clase madre
        self.marca = marca
        
#creamos nuestro primer objeto
moto1 = Moto('Motocicleta', 'ducatti')
print(moto1.descripcion())
