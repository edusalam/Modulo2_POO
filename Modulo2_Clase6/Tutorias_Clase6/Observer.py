class NuevoCanal:
    def __init__(self):
        self._suscriptor =[]
        self._later_mews = None
    
    def suscribirse(self, suscribirse):
        self._suscriptor.append(suscribirse)

    def dessuscribirse(self, dessuscribirse):
        self._suscriptor.append(dessuscribirse)
    
    def notificacion(self):
        for sus in self._suscriptor:
            sus.update(self._later_mews)

    def publicacion(self, news):
        self._later_mews = news
        print(f'notificacion pblica: {news}')
        self.notificacion()
class Suscriptor:
    def __init__(self, name):
        self.name = name
    def update(self, news):
        print(f'{self.name} ha recibido la notificacion')

canalDevseniorcode = NuevoCanal()

#SE CREAN LAS SUSCRIPCIONES
Suscriptor1 = Suscriptor('eduard')
Suscriptor2 = Suscriptor('fernando')
Suscriptor3 = Suscriptor('dani')

#SE SUSCRIBEN AL CANAL
canalDevseniorcode.suscribirse(Suscriptor1)
canalDevseniorcode.suscribirse(Suscriptor2)
canalDevseniorcode.suscribirse(Suscriptor3)

canalDevseniorcode.publicacion('tenemos tutoria el dia de hoy')
                            
    