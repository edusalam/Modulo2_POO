class CalcularImpuesto:
    def ejecutar(self, monto):
        return monto * 0.19

class AplicarDescuento:
    def ejecutar(self, monto, descuento):
        return monto - (monto * descuento / 100)

class GenerarRecibo:
    def ejecutar(self, monto):
        return f'recibo generado por${monto:.2f}'

class Facturacion:
    def __init__(self):
        self.pasos = []

    def agregarPasos(self, paso):
        self.pasos.append(paso)
    
    def procesarFactura(self, monto, descuento=0):
        print('procesar factura')
        for paso in self.pasos:
            if isinstance(paso, CalcularImpuesto):  #Valida el objeto paso y que provenga de la clase que se llama calcular impuesto
                impuesto = paso.ejecutar(monto)
                print(f'impuesto calculado: ${impuesto:.2f}')
                monto += impuesto
            elif isinstance(paso,AplicarDescuento):
                monto = paso.ejecutar(monto, descuento)
                print(f'descuento aplicado: ${monto:.2f}')
            elif isinstance(paso, GenerarRecibo):
                print(paso.ejecutar(monto))
    
facturacion = Facturacion()
impuesto = CalcularImpuesto()
descuento = AplicarDescuento()
recibo = GenerarRecibo()
facturacion.agregarPasos(impuesto)
facturacion.agregarPasos(descuento)
facturacion.agregarPasos(recibo)

facturacion.procesarFactura(500, descuento=10)



