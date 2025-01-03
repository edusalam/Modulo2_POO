class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def descripcion(self):
        return f'libro: {self.titulo} autor: {self.autor}'
    
    def __str__(self):
        return f'libro: {self.titulo} autor: {self.autor} STR'


class LibroDigital(Libro):
    
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato
        
    def descripcion(self):
        return f'libro: {self.titulo} autor: {self.autor} formato {self.formato}'       
        

    def __str__(self):
        return f'libro: {self.titulo} autor: {self.autor} formato {self.formato} STR' 

#creacion de objetos:
libro1 = Libro('cien años de soledad', 'garcia marquez')
LibroDigital1 = LibroDigital('el conde de montecristo','alejandro dumas','pdf')

print(libro1.__str__())
print(libro1.descripcion())

print(LibroDigital1.descripcion())
print(LibroDigital1.__str__())
        
    