#EL POLIMORFISMO nos permite reutilizar metodos (viene de muchas cosas, responder de varias maneras algo)
#PRIMERA MANERA DE POLIMORFISMO
class Gato:
    def sonido(self):
        return'miau'
    
class Carro:
    def sonido(self):
        return 'pili pili'
    
def hacer_sonido(objeto):
    print(objeto.sonido())

#instanciamos (definimos)
mi_gato = Gato()
mi_carro = Carro()

print(f'mi gato luna hace el siguiente sonido: ')
hacer_sonido(mi_gato)

print(f'mi carro negro pita de la siguiente forma')
hacer_sonido(mi_carro)


    
