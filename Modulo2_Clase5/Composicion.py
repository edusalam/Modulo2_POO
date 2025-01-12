#EJERCICION DE COMPOSICION
class Motor:
    def __init__(self):
        pass
    def iniciar(self):
        pass
class MotorGasolina(Motor):
    def __init__(self):
        pass
    def iniciar(self):
        print('motor a gasolina encendido')

class MotorElectrico(Motor):
    def __init__(self):
        pass
    def iniciar(self):
        print('motor electrico encendido')

class Vehiculo:
    def __init__(self, motor):
        self.motor = motor   #ESTO SE LLAMA ENCAPSULAMIENTO
        
    def encender(self):
        print('encendiendo el vehiculo')
        self.motor.iniciar()

#CREAMOS LOS OBJETOS        
motor_gasolina = MotorGasolina()
motor_electrico = MotorElectrico()

# COMO PARTE DE LA COMPOSICION LO ESTOY ATANDO AL VEHICULO CON LOS TIPOS DE MOTOROS
auto_gasolina = Vehiculo(motor_gasolina)
auto_electrico = Vehiculo(motor_electrico)

auto_gasolina.encender()
auto_electrico.encender()