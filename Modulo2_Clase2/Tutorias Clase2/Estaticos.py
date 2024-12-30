#METODOS ESTATICOS, METODO QUE NO NECESITA ACCEDER A NADA, NINGUN ATRIBUTO,METODOS ETC, 
#USANDO SUS PROPIOS PARAMETROS  VA FUNCIONAR, (SI IMPORTA EL ORDEN, ALTERA EL RESULTADO.)
class miclase:
    #decorativa
    @staticmethod

    def mi_metodo_estatico(numero1,numero2):
        return numero1 + numero2
    
obj = miclase()
print(obj.mi_metodo_estatico(1, 2)) 
