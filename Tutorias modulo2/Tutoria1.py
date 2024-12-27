#los metodos son las acciones     ejemplo: libro, (leerlo, pasar pagina)
# atributos son las caracteristicas ejemplo: (titulo, autor)
class libro:

      #atributos
      def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor
      def acciones(self):
            return f'el libro{self.titulo}, el señor de los cielos, {self.autor}'
      
libro1 = libro('el señor de los cielos','jr')
    
print(libro1.acciones())
    

