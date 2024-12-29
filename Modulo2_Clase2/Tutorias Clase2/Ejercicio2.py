#CREA UNA CLASE LLAMADA VEHICULO CON LOS ATRIBUTOS MARCA Y MODELO, LUEGO CREA UNA CLASE COCHE QUE HEREDE
#DE VEHICULO Y AGREGA UN ATRIBUTO PUERTAS.
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

moto1 = Moto('pulsar', 'A150')
coche1 = Coche('ford', 'Mustand', 4) 

print(coche1.marca)
print(coche1.modelo)
print(coche1.puertas)

print(moto1.marca)
print(moto1.modelo)

    