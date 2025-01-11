#los patrones de diseño buscan resolver un problema, busca la menor manera de estructurar para mejorar su codigo
import json
class SistemaGuardado:
    __instance = None
    @staticmethod
    def get_instance():
        if SistemaGuardado.__instance is None:
            SistemaGuardado.__instance = SistemaGuardado()
        return SistemaGuardado.get_instance
    
    def __init__(self):
        self.archivo_guardado = 'guardado.bat'


    def guardar_juego(self, dato_a_guardar):
        with open(self.archivo_guardado, 'w') as f:
            json.dump(dato_a_guardar,f, indent=2)

    def cargar_juego(self):
        with open(self.archivo_guardado, 'r') as f:
             return json.load(f)
        
class Jugador():
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    '''
    def guardar_progreso(self):
        guardado = SistemaGuardado.get_instance()
        dato_a_guardar = self.serializar()
        jugador = Jugador.deserializar(dato_a_guardar)
    '''
    def serializar(self):
        return {'nombre': self.nombre, 'nivel': self.nivel}
    @classmethod
    def deserializar(self, data):
        return self(data['nombre'], data['nivel'])

def CargarPartida():
        guardo = SistemaGuardado.get_instance()
        datos_cargados = guardo.cargar_juego()
        jugador = Jugador.deserializar(datos_cargados)
'''    
jugador1 = Jugador('eduard',50)
guardado = SistemaGuardado.get_instance()
guardado.guardar_juego(jugador1.serializar())
'''
guardando = SistemaGuardado.get_instance()
datos_cargados = guardando.cargar_juego()
Jugador_cargado = Jugador.deserializar(datos_cargados)
print(Jugador_cargado.nombre)
