#EJERCICIO 5: MODIFICA LA CLASE cuentaBancaria PARA USAR DECORADORES @property Y @setter EN EL ATRIBUTO _SALDO
class CuentaBancaria:
    def __init__(self, saldo, saldo2):
        self.__saldo = saldo
        #self.saldo2 = saldo2
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,cantidad):
        if cantidad > 0:
           self.__saldo = cantidad
        else:
            print('la cantidad no es valida') 
 

    def depositar(self, cantidad):
        if cantidad > 0:
           self.__saldo += cantidad
           print(f'el deposito de {cantidad} exitoso. saldo actual es de: {self.__saldo}')
        else:
            print('la cantidad no es valida') 

    def consultar_saldo(self):
        print(f'El saldo actual es de: {self.__saldo}')
     
cuentaEduard = CuentaBancaria(10,1)

cuentaEduard.consultar_saldo()
cuentaEduard.depositar(500)
cuentaEduard.saldo = 500
print(cuentaEduard.saldo)

