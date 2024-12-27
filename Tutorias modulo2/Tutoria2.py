class persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayor(self):
        return self.edad >= 18
    
persona1 = persona('juan', 16) 

print(f'{persona1.nombre} es mayor de edad:{persona1.mayor}')