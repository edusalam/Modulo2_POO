#EJERCICIO 1: CREA UNA CLASE cuentaBancaria CON UN ATRIBUTO PRIVADO __SALDO, AGREGA METODOS PARA 
# DEPOSITAR Y RETIRAR DINERO ASEGURANDOTE DE QUE NO SE PERMITA UN SALDO NEGATIVO
class CuentaBancaria:
    def __init__(self, saldo, saldo2):
        self.__saldo = saldo
        #self.saldo2 = saldo2
        
    def depositar(self, cantidad):
        if cantidad > 0:
           self.__saldo += cantidad
           print(f'el deposito de {cantidad} exitoso. saldo actual es de: {self.__saldo}')
        else:
            print('la cantidad no es valida') 

    """def retirar(self, cantidad):    NO SE HA CREADO ESTE METODO
        if cantidad > 0:
           self.__saldo += cantidad
           print(f'el deposito de {cantidad} exitoso. saldo actual es de: {self.__saldo}')
        else:
            print('la cantidad no es valida') 
    """
    """def test(self, cantidad):       EJEMPLO EN EL DESARROLLO DE ESTE METODO
        if cantidad > 0:
            self.saldo2 += cantidad
            print(f'deposito de {cantidad} exitoso. saldo actual es de: {self.saldo2}')
        else:
            print('la cantidad no es valida')
    """
    def consultar_saldo(self):
        print(f'El saldo actual es de: {self.__saldo}')
        #return self.__saldo
        

cuentaEduard = CuentaBancaria(10,1)

cuentaEduard.depositar(50)
CuentaBancaria.depositar(cuentaEduard, 5)
#cuentaEduard.test(2)
cuentaEduard.consultar_saldo()




        
