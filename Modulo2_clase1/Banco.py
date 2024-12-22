class banco:
    TASA_INTERES = 0.03 #Es normal utilizar las constantes en mayusculas, para diferenciarlo de una constante a una variable


    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.TASA_INTERES = nuevaTasa
    
    @staticmethod
    def conversionDolaresEuros(dolares):
        return dolares * 0.85
    
    #COMO IMPRIMIR UN OBJETO
