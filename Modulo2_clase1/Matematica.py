#metodos estaticos
class Matematica:
    #decoorador estatic
    @staticmethod
    def suma(a, b):
        return a + b
    @staticmethod
    def resta(a, b):
        return a - b
print(Matematica.suma(5, 50111))
print(Matematica.resta(1000, 1))