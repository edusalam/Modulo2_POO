#diferencia entre el metodo de instancia y metodo de una clase se trae el objeto con el parametro self
#importante en el motodo de instancia se trae el parametro o se usa la palabra selft (se trae el parametro self)
#en el metodo de clase no se trae una instancia si no que se trae toda la clase (se trae el prefijo cl de clase)
# EJEMPLO DE METODO DE INSTANCIA
class Animal:
    #definimos el metodo constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def saludar(self):
        return f'mi animalito se llama {self.name} y tiene {self.age} años'
    
#creamos el objeto animal1 (importante cuando se define el objeto se define en minuscula para diferenciarlo de la clase (animal1))
animal1 = Animal('ginebra', 3)

print(animal1.name)
print(animal1.age)
print(animal1.saludar())
    

