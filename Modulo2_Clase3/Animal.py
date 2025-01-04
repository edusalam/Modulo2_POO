class Animal:

    def __init__(self):
        pass

    def hablar(self):
        pass

class Gato(Animal):

    def __init__(self):
        pass
        

    def hablar(self):
         return f'el gato hace miau miau'
        

class Perro(Animal):

    def __init__(self):
        pass
    

    def hablar(self):
        return f'el perro hace guau guau'
        
#CREAMOS UNA LISTA CON 2 OBJETOS PERRO Y GATO
animales = [Perro(), Gato()]
        
for animal in animales:
    print(animal.hablar())