#crud: permite crear registros hacer consultass, actualizar registros
from abc import ABC, abstractmethod # libreria clases abstractas
from datetime import datetime #nos permite validar fecha y hora

class Persona(ABC):
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion
    
    @abstractmethod
    def mostrar_informacion(self):
        pass

#crear clas abstrracta mascota
class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self. edad = edad
        self.historialCitas = []
    
    @abstractmethod #crear metodo que proviene de una clase abstracta
    def agregar_citas_alHistorial(self, detalles_servicio):
        pass

class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinaria):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinaria = veterinaria
    
    @abstractmethod
    def actualizar(self, **kwargs):# el kwargs: permite gestionar estructura de datos, es para aceptar objetos de tipo diccionario creada para listas

        pass
   #funcion de las subclases 
class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = [] #lista que me guarda las mascotas

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    
    def mostrar_informacion(self):
        return f'cliente{self.nombre}, contacto {self.contacto}, direccion {self.direccion}'
    
class RegistroMascota(Mascota): #crear las citas para las mascotas
    def  agregar_citas_alHistorial(self, detalles_servicio):
         self.historialCitas.append(self, detalles_servicio)
    
    def obtener_historial(self):
        return self.historialCitas
    
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, Valor in kwargs.items():#recoriiendo cada uno de los registros de la lista, elemento por elemento
            if hasattr(self.clave):
                setattr(self.clave, Valor) #actualiza

class SistemaVeterinaria:#desarrollamos nuestra logica
    def __init__(self):
        self.clientes = []
    
    def registrar_clientes(self):
        try: #para capturar errores
            nombre = input('ingrese el nombre del cliente: ').strip()#el strip borra los espacios en blanco
            contacto = input('ingrese el contacto').strip()
            direccion = input('ingrese la direccion').strip()

            if not nombre or not contacto or not direccion:
                raise ValueError('todos los campos son obligatorios')
            
            Cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(Cliente)
            print('cliente registrado con exito: ')
        
        except ValueError as e: #si sale este error arroje el mensaje ...
            print(f'error: {e}')
    def registrarMascota(self):
        try:
            nombre_cliente = input('ingrese el nombre del cliente al que asociar la mascota: ').strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)#crear funcion landam

            if not cliente:
                raise ValueError('cliente no encontrado.')
            
            nombre_mascota = input('ingrese el nombre de la mascota: ').strip()
            especie = input('ingrese la especie: ').strip()
            raza = input('ingrese la raza').strip()
            edad = int(input('ingrese la edad').strip())

            if not nombre_mascota or not especie or not raza or edad <- 0:
                raise ValueError('detalles de la mascota invalidos')  #validarr que se ingreso valores en todos los atributos y si quedaron en blanco que lo saque
            
            mascota = RegistroMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print(f'mascota registrada con exito')
         
        except ValueError as e: 
            print(f'error: {e}')

    def programar_cita(self):
        try:
            nombre_cliente = input('ingrese el nombre del cliente al que asociar la mascota').strip()
            nombre_mascota = input('ingrese el  nombre de la mascota').strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)#crear funcion landam

            if not cliente:
                raise ValueError('cliente no encontrado.')
            
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)

            if not mascota:
                raise ValueError('mascota no encontrada')
            
            fecha = input('ingrese la fecha (AAAA---MM-DD):').strip()
            hora = input('ingrese la hora(hh:mm)').strip()
            servicio = input('ingrese el servicio(consulta, vacunacion, etc):').strip()
            veterinario = input('ingrese el nombre del veterinario:').strip()

            #definir un formato y si es deacuerdo al formato
            datetime.strftime(fecha, '%Y-%n-%d')
            datetime.strptime(hora, '%H:%M')

            if not servicio or not veterinario:
                raise ValueError('detalles de la cita invalidos')
            
            cita = CitaMascota(fecha, hora, servicio, veterinariote)
            mascota.agregar_citas_alHistorial(cita)
            print('cita programada con exito')
        
        except ValueError as e: 
            print(f'error: {e}')








        





        
    

    

    