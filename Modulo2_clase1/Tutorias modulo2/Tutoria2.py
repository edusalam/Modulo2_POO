class persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayor(self):
        return self.edad >= 18
    
    def menor(self):
        return self.edad <= 17
    
persona1 = persona('juan', 21) 
print(persona1.nombre)
print(persona1.mayor())

persona2 = persona('eduard', 30)
print(persona2.nombre)
print(persona2.menor())