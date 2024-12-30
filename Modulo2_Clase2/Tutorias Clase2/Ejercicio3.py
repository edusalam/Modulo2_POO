#AGREGUE UN METODO PROTEGIDO _CALCULAR_INTERES EN LA CLASE CUENTA BANCARIA
#QUE CALCULE UN 5% DE INTERESES SOBRE EL SALDO ACTUAL.
class CuentaBancaria:
    def __init__(self, saldo, saldo2):
        self.__saldo = saldo
        #self.saldo2 = saldo2

    def _calcular_interes(self):
        interes = self.__saldo * 0.05
        print(f'el interes es de {interes}')
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,cantidad):
        if cantidad > 0:
           self.__saldo = cantidad
        else:
            print('CANTIDAD NO VALIDA') 
 

    def depositar(self, cantidad):
        if cantidad > 0:
           self.__saldo += cantidad
           print(f'el deposito de {cantidad} exitoso. saldo actual es de: {self.__saldo}')
        else:
            print('la cantidad no es valida') 

    def consultar_saldo(self):
        print(f'El saldo actual es de: {self.__saldo}')
     
cuentaEduard = CuentaBancaria(5,6)

cuentaEduard.consultar_saldo()
cuentaEduard.depositar(100)
cuentaEduard.saldo = -100
print(cuentaEduard.saldo)
cuentaEduard._calcular_interes()