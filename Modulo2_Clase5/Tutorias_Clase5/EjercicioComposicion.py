# lo primero es definir una clase
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def encender(self):
        print(f'el motoor de tipo {self.tipo} se ha encendido')
class Rueda:
    def __init__(self, tamano):
        self.tamano = tamano

    def girar(self):
        print(f'la rueda de tamaño {self.tamano} esta girando')

class Coche:
    def __init__(self, motor, ruedas):
        self.motor = motor
        self.ruedas = ruedasS

    def iniciar_viaje(self):
        self.motor.encender()
        for rueda in self.ruedas:
            rueda.girar()
        print('el coche ha comenzado a moverse')
motor_deportivo = Motor('v10')
ruedas_pequeñas = [Rueda(14),Rueda(14),Rueda(14),Rueda(14),]

coche_deportivo = Coche(motor_deportivo, ruedas_pequeñas)
coche_deportivo.iniciar_viaje()
