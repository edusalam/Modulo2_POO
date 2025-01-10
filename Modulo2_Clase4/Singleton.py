#en singleton no se pone en la clase no se pone el mismo nombre, (  CREA UN OBJETO O UNA INSTANCIA)
#patron de diseño sinlgeton
class SingletonCreacionInstancia:

    _instancia = None

    #en singleton hace las veces del constructor
    def __new__(cls, *args, **kwargs):
        
        if not cls. _instancia:
            cls._instancia * super(SingletonCreacionInstancia, cls).__new__(cls)
        return cls._instancia




        