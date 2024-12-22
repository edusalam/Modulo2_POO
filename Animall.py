# EJEMPLO DE METODO DE CLASE
class Animall:
    #variable que va a comular la cantidad de objetos que se creen
    cantidadAnimales = 0
    #definimos nuestro metodo inicial
    def __init__(self, name):
        self.name = name
        #definimos una variable
        Animall.cantidadAnimales += 1
# utilizamos los decoradores, pueden cambiar o mutar un coportamiento es decir un metodo
#extension darknight
    @classmethod 
    def totalAnimales(cls):
     return f'Tengo {cls.cantidadAnimales}animalitos'
#objetos creados
animalitos1 = Animall('ron')
animalitos2 = Animall('rayo')
animalitos3 = Animall('dani')

print(animalitos3.name)
print(Animall.cantidadAnimales)
print(Animall.totalAnimales())
