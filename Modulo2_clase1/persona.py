class Persona:
    #definimos el METODO constructor de la clase, permite encapsular los atributos 
    #el parametro o argumento (self) se una en los metodos de una clase para referirse a la instancia actual de la clase 
    def __init__(self, nombre, edad): #(atributos)
        self.nombre = nombre
        self.edad = edad
    #creamos un METODO saludar (metodo instancia)
    def saludar (self):
        return f'hola, soy{self.nombre} y tento {self.edad} años' #formato de salida que permite integrar dentro del mensaje atributos y cadena de texto
    
    
