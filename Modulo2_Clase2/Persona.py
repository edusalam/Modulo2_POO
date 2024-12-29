class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
        self.__cuentaBancaria = 12345
    
    def mostrarInformacion(self):
        return f'Nombre: {self.nombre} edad: {self._edad}'
    
    def __MostrarCuenta(self):
        return f'cuenta bancaria: {self.__cuentaBancaria}'
    
    def mostrarInformacionCompleta(self):
        return self.__MostrarCuenta()

#creamos una instacia o objeto creado
persona1 = Persona('luis guilleromo', 49)

print(persona1.nombre)
print(persona1._edad)

print(persona1.mostrarInformacion())

print(persona1.mostrarInformacionCompleta())

    
