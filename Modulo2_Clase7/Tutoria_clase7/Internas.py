#CUANDO UNO EJECUTA LLAMA LA SENTENCIA, (LAS CLASES INTERNAS SE UTILIZAN CUANDO NECESITAMOS LLAMAR UN PROCESO O UN MENSAJE)
#EJEMPLO SIMPLE UTLIZANDO CLASES ANIDADAS
'''class Externa:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    class Interna:
        def __init__(self, externa):
            self.externa = externa
        
        def mostrar_mensaje(self):
            print(f'mensaje desde clase externa {self.externa.mensaje}')
        
externa = Externa('hola estoy desde la clase externa')
interna = Externa.Interna(externa)

interna.mostrar_mensaje()
'''
class CuentaBanco: #clase externa
    def __init__(self,titular, saldo_inicia):
        self.titular = titular
        self.saldo = saldo_inicia    
    class Transaccion:
        def __init__(self, cuenta, monto, tipo):
            self.cuenta = cuenta
            self.monto = monto
            self.tipo = tipo

        def ejecutar(self):
            if self.tipo == 'deposito':
                self.cuenta.saldo += self.monto
            elif self.tipo == 'retiro' and self.cuenta.saldo >= self.monto:
                self.cuenta.saldo -= self.monto
            else:
                print('fondos insuficiente')
            print(f'saldo actual: {self.cuenta.saldo}')
    
cuenta = CuentaBanco('eduard ', 12000)
deposito = cuenta.Transaccion(cuenta, 500,'deposito')
deposito.ejecutar() #EJECUTAR PROCESO
            
        

        
            