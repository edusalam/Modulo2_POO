#nos permite al mismo tiempo herredar al mismo tiempo todos los datos, todos los atributos y metodos
class Mamifero:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def alimentar(self):
        print(f'{self.nombre} se esta alimentando')


class Volador:
    def volar(self):
        return f'{self.nombre} esta volando'
class Murcielago(Mamifero,Volador):
    def __init__(self, nombre):
        super().__init__(nombre)
    
bat =  Murcielago('bety')

print(bat.volar())
print(bat.alimentar())
