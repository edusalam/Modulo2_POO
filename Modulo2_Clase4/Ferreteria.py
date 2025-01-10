#desarrollar dos procesos de negocios pedidos y factura
#IMPORTAMOS LA LIBRERIA
import threading
from abc import ABC, abstractmethod
#creamos el patron singleton
class SistemaFacturacion:

    #CREEAMOS LAS VARIABLES de clase
    _instancia = None
    _lock = threading.Lock() #BLOQUEA EL HILO DE LA COMUNICACION
    
    def __new__(cls, *args, **kwargs): #DEFINIMOS EL METODO NEW QUE HACE LAS VECES DEL CONSTRUCTOR

        if not cls._instancia:
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia               


       #OPCIONAL SI LE QUEREMOS METER ECEPCINES
        '''
       with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia
        '''
    def _inicializacionHistorico(self):
            self.historial = []
            print('sistema de facturacion iniicializado')
    def registrarOperacion(self, operacion):
            self.historial.append(operacion)
            print(f'la operacion fue registrada {operacion}')

#CREAMOS LA CLASE ABSTRACTA
class ProcesoNegocio(ABC):
      @abstractmethod
      def ejecutar(self):
            pass
      
class ProcesarPedido(ProcesoNegocio):
      
      def ejecutar(self):
            print('precesando pedido .....')
            return'pedido procesado'

class ProcesarFactura(ProcesoNegocio):
      def ejecutar(self):
            print('procesando factura')
            return 'factura procesada'

#CREAMOS LA FABRICA FACTORY
class FabricaProcesoNegocio:
      @staticmethod
      def crearProceso(tipoProceso):
            if tipoProceso == 'pedido':
                  return ProcesarPedido()
            elif tipoProceso == 'factura':
                  return ProcesarFactura()
            else:
                  raise ValueError('el proceso {tipoProceso} no existe')

if __name__ == '__main__':
      
      Sistema_facturacion = SistemaFacturacion()

      proceso1 = FabricaProcesoNegocio.crearProceso('pedido')
      proceso2 = FabricaProcesoNegocio.crearProceso('factura')

      resultadoPedido1 = proceso1.ejecutar()
      Sistema_facturacion.registrarOperacion(resultadoPedido1)

      resultadoPedido2 = proceso2.ejecutar()
      Sistema_facturacion.registrarOperacion(resultadoPedido2)

      print('\n***historico de proceso de negocio***\n')
      for operacion in Sistema_facturacion.historial:
            print(f'transaccion: {operacion}')
            
         


