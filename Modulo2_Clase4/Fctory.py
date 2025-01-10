#PATRON DE DISEÑO FACTORY SE DEFINE COMO UNA INTERFAZ
#para las clases abstractas siempre se importa la libreria from abc import ABC
from abc import ABC, abstractmethod
#CREAMOS LA CLASE ABSTRACTA
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass
#SUBCLASES DE LA CLASE ABSTRACTA
class ClaseA(Clases):
    def operacion(self):
        return 'esta es la clase A'

class ClaseB(Clases):
    def operacion(self):
        return 'es la clase B'

#CREAMOS LA CLASE FACTORY, llamada factoria o fabrica
class FabricaClases:
    #CREAMOS UN METODO ESTATICO
    @staticmethod
    def creacionObjetos(tipoObjeto):
        if tipoObjeto == 'A':
            return ClaseA()
        elif tipoObjeto == 'B':
             return ClaseB()
        else:
            raise ValueError(f'la clase {tipoObjeto} no existe')
    

#creamos un objeto
objeto1 = FabricaClases.creacionObjetos('A')
objeto2 = FabricaClases.creacionObjetos('c')

print(objeto1.operacion())

