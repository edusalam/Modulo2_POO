class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario
        self.nuevoSueldo = 1800000
        self.salarioMinimo = 1300000
        
        
    def mostrarInformacion(self):
        return f'Nombre: {self.nombre}, salario: {self._salario}'
        
    def obtenerSalario(self):
        return self._salario

    def establecerSalario(self, nuevoSalario):
        if nuevoSalario < self.nuevoSueldo:
            return f'el salario no puede ser menor al salario minimo'
        self._salario = nuevoSalario
        return f'El nuevo salario es: {self._salario}'   


empleado1 = Empleado('mario', 1300000)

print(empleado1.mostrarInformacion())
print(empleado1.obtenerSalario())
print(empleado1.establecerSalario(900000))
print(empleado1.establecerSalario(1900000))




        