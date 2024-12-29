class CuentaBancaria:

    def __init__(self, titular, saldo, clave):
        self.titular = titular
        self._saldo = saldo
        self.__clave = clave
        

    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f'Deposito exitoso. Saldo actual {self._saldo}'
        
#<>
    def retirar(self, cantidadRetiro):
        if cantidadRetiro > self._saldo:
            return 'fondos insuficientes'
        self._saldo -= cantidadRetiro
        return f'retiro exitoso. el saldo actual es {self._saldo}'
        
    
    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        return f'clave modificada de forma exitosa. la nueva clave es: {self.__clave}'
    
cuentaBancaria1 = CuentaBancaria('luis', 100000, 1234)

print(cuentaBancaria1.titular)
print(cuentaBancaria1._saldo)

print(cuentaBancaria1.depositar(500000))
print(cuentaBancaria1.depositar(200000))
print(cuentaBancaria1.retirar(100000))
print(cuentaBancaria1.retirar(10000))

print(cuentaBancaria1.modificarClave(4321))


