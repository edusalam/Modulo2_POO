#polimorfismo con herencias y metodos sobrescritos
class Animal:
    def sonido(self):
        return 'sonido generico'
    
class perro(Animal):
        def sonido(self):
            return'gua gua'

class gato(Animal):
     def sonido(self):
            return 'miau miau'
     
mi_gato = gato()
mi_perro = perro()

print(mi_gato.sonido())
        
