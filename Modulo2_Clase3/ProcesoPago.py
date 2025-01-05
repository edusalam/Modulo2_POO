#implementar interfaces en python (NO SE PUEDEN DEFIRNIR ATRIBUTOS)
from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    @abstractmethod
    def procesoPago(self, cantidad: float) -> None: #NO RETORNA NADA
        pass

    @abstractmethod
    def reembolsoPago(self, trasaccionId: str) -> None:
        pass

class Paypal(ProcesoPago):

    def procesoPago(self, cantidad: float) -> None:
        print(f'procesando pago de $ {cantidad} por Paypal')
    
    def reembolsoPago(self, trasaccionId: str)-> None:
        print(f'Reembolsando Id transaccion numero{trasaccionId} por paypal')
    
class Stripe(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print(f'procesando pago de $ {cantidad} por Stripe')

    def reembolsoPago(self, trasaccionId):
        print(f'Reembolsando Id transaccion numero{trasaccionId} por stripe')

if __name__ == '__main__':
   procesopypal = Paypal()
   procesostripe = Stripe()

   procesopypal.procesoPago(500.0)
   procesopypal.reembolsoPago('FDC1233')

   procesostripe.reembolsoPago(1000.0)
   procesostripe.procesoPago('FDC1233')

    