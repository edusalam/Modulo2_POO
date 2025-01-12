#IMPORTAMOS LA LIBRERIA, RECORDAR QUE LA CLASE ABSTRACTA ES UNA PLANTILLA
from abc import ABC, abstractmethod
#pero si la variable esta fuera del constructor es una variable de clase
class Sujeto:
    def __init__(self):
        self._observadores = []  #si esta dentro del constructor es una variable de instancia
    
    def agregarObservador(self, observador):
        self._observadores.append(observador)
    
    def quitarObservador(self, observador):
        self._observadores.remove(observador)

    def notificarObservador(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

class observador(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def actualizar(self, mensaje):
        raise NotImplementedError('subclases deben estar implementadas')#manejo de gestion de errores o ecepciones
    
class ObservadorConcreto(observador):

    def __init__(self, nombre):
        self.nombre = nombre#encapsulamos el nombre
    
    def actualizar(self, mensaje):
        print(f'{self.nombre} recibio: {mensaje}')

#creamos un objeto
sujeto = Sujeto()

obs1 = ObservadorConcreto('observador1')
obs2 = ObservadorConcreto('observador2')

sujeto.agregarObservador(obs1)
sujeto.agregarObservador(obs2)

sujeto.notificarObservador('mensaje de advertencia lptx')


        


        
    
    

    

