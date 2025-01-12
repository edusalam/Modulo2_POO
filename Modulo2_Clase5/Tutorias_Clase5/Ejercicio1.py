from abc import ABC, abstractmethod
#CREEAMOS LA CLASE ABSTRACTA
class Empleado(ABC):
    def __init__(self, nombre, id, salario_base):
        self._nombre = nombre
        self._id = id
        self._salario_base = salario_base

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def id(self):
        return self._id
    
    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self, nuevo_salario):
        if nuevo_salario>0:
            self.salario_base = nuevo_salario
        else:
            raise ValueError('el salario debe ser mayor a cero')
    @abstractmethod #le estamos diciento que este metodo es abstracto
    def calcular_bono(self):
        pass

    def __str__(self):
        return f'empleado: {self._nombre}, id: {self._id} salario base: {self._salario_base}'

#VAMOS A USAR EL POLIMORFISMO

class Desarrollador(Empleado):
    def calcular_bono(self):
        return self._salario_base * 0.10
    
        

class Diseñador(Empleado):
    def calcular_bono(self):
        return self._salario_base * 0.05
   
    
class Gerente(Empleado):
     def calcular_bono(self):
        return 500.0
    

if __name__ == '__main__':
    dev = Desarrollador('eduard', 10, 5000)
    designer = Diseñador('eduardd',11, 6000)
    manager = Gerente('eduarddd', 12, 10000)

    empleados = [dev, designer, manager]
    for empleado in empleados:
        print(empleado)
        print(f'bono: {empleado.calcular_bono()}')