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
        self.historial_citas = []
    
    @abstractmethod #crear metodo que proviene de una clase abstracta
    def agregar_al_Historial(self, detalles_servicio):
        pass

class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinaria = veterinario
    
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
        return f'cliente: {self.nombre}, contacto: {self.contacto}, direccion: {self.direccion}'
    
class RegistroMascota(Mascota): #crear las citas para las mascotas
    def  agregar_citas_al_Historial(self, detalles_servicio):
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
    
    def registrar_Cliente(self):
        try: #para capturar errores
            nombre = input('Ingrese el nombre del cliente: ').strip()#el strip borra los espacios en blanco
            contacto = input('Ingrese el contacto: ').strip()
            direccion = input('Ingrese la direccion: ').strip()

            if not nombre or not contacto or not direccion:
                raise ValueError('Todos los campos son obligatorios')
            cliente = Cliente(nombre,contacto,direccion)
            self.clientes.append(cliente)
            print('Cliente registrado con exito: ')
        
        except ValueError as e: #si sale este error arroje el mensaje ...
            print(f'error: {e}')

    def registrar_Mascota(self):
        try:
            nombre_cliente = input('Ingrese el nombre del cliente al que asociar la mascota: ').strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)#crear funcion landam

            if not cliente:
                raise ValueError('Cliente no encontrado.')
            
            nombre_mascota = input('Ingrese el nombre de la mascota: ').strip()
            especie = input('Ingrese la especie: ').strip()
            raza = input('Ingrese la raza: ').strip()
            edad = int(input('Ingrese la edad: ').strip())

            if not nombre_mascota or not especie or not raza or edad <- 0:
                raise ValueError('Detalles de la mascota invalidos.')  #validarr que se ingreso valores en todos los atributos y si quedaron en blanco que lo saque
            
            mascota = RegistroMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print('Mascota registrada con exito.')
         
        except ValueError as e: 
            print(f'error: {e}')

    def programar_cita(self):
        try:
            nombre_cliente = input('Ingrese el nombre del cliente al que asociar la mascota: ').strip()
            nombre_mascota = input('Ingrese el  nombre de la mascota: ').strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)#crear funcion landam

            if not cliente:
                raise ValueError('Cliente no encontrado.')
            
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)

            if not mascota:
                raise ValueError('Mascota no encontrada')
            
            fecha = input('Ingrese la fecha (AAAA---MM-DD): ').strip()
            hora = input('Ingrese la hora(hh:mm): ').strip()
            servicio = input('Ingrese el servicio(consulta, vacunacion, etc): ').strip()
            veterinario = input('Ingrese el nombre del veterinario: ').strip()

            #definir un formato y si es deacuerdo al formato
            datetime.strftime(fecha, '%Y-%m-%d')
            datetime.strptime(hora, '%H:%M')

            if not servicio or not veterinario:
                raise ValueError('Detalles de la cita invalidos.')
            
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_citas_alHistorial(cita)
            print('Cita programada con exito.')
        
        except ValueError as e: 
            print(f'error: {e}')

    def actualizar_cita(self):
        try:
            nombre_cliente = input('Ingrese el nombre del cliente al que asociar la mascota: ').strip()
            nombre_mascota = input('Ingrese el  nombre de la mascota: ').strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)#crear funcion landam

            if not cliente:
                raise ValueError('Cliente no encontrado.')
            
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)

            if not mascota:
                raise ValueError('Mascota no encontrada')
            
            if not mascota.historial_citas:
                raise ValueError('No hay citas registrada para esta mascota.')

            print('Citas disponibles para actualiizar: ')
            for i, cita in enumerate(mascota.historial_citas):
                print(f'{i + 1}, fecha: {cita.fecha}, hora: {cita.hora}, servicio: {cita.servicio}, veterinaria: {cita.Veterinaria}')

            indice = int(input('Seleccione el numero de la cita a actualizar: ').strip()) -1
            if indice < 0 or indice <= len(mascota.historial_citas):
                raise ValueError('Seleccion invalida.')
            
            cita = mascota.historial_citas[indice]

            print('Deje en blanco los campos que no desea actualizar.')
            nueva_fecha = input('Nueva fecha (AAA-MM-DD: )').strip()
            nueva_hora = input('Nueva hora (hh-mm): ').strip()
            nuevo_servicio = input('Nuevo servicio: ').strip()
            nuevo_veterinario = input('Nuevo veterinario: ').strip()  

            if nueva_fecha:
                datetime.strptime(nueva_fecha, '%Y-%m-%d')
                cita.actualizar(fecha = nueva_fecha)
            if nueva_hora:
                datetime.strptime(nueva_hora, '%H:%M')
                cita.actualizar(hora = nueva_hora)
            if nuevo_servicio:
                cita.actualizar(servicio = nuevo_servicio)
            if nuevo_veterinario:
                cita.actualizar(veterinario = nuevo_veterinario)
            
            print('Cita actualizada con exito.')              
 
        except ValueError as e: 
            print(f'error: {e}') 

    def consultar_historial(self):
        try:
            nombre_cliente = input('Ingrese el nombre del cliente al que asociar la mascota: ').strip()
            nombre_mascota = input('Ingrese el  nombre de la mascota: ').strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)#crear funcion landam
            if not cliente:
                raise ValueError('Cliente no encontrado.')
            
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError('Mascota no encontrada.')

            historial = mascota.obtener_historial()
            if not historial:
                print('No hay historial disponible para estsa mascota. ')
            else:
                for entrada in historial:
                     print(f'fecha: {entrada.fecha}, hora: {entrada.hora}, servicio: {entrada.servicio}, veterinaria: {entrada.Veterinaria}')

        except ValueError as e: 
            print(f'error: {e}')
            
    def iniciar(self):
        while True:  #$ es forzar un while para que entre y se ejecute lo que esta dentro
            print('=======Menu Principal======')
            print('1. Registrar cliente')
            print('2. Registrar mascota')
            print('3. Programar cita')
            print('4. Actualizar cita')
            print('5. Consultar historial')
            print('6. Salir\n')

            opcion = input('Ingrese opcion: ').strip()#VARIABLE

            if opcion == '1':
                self.registrar_Cliente()
            elif opcion == '2':
                self.registrar_Mascota()
            elif opcion == '3':
                self.programar_cita()
            elif opcion == '4':
                self.actualizar_cita()
            elif opcion == '5':
                self.consultar_historial()
            elif opcion == '6':
                print('Saliendo del sistema.')
                break
            else:
                print('Opcion Invalida.')
                

if __name__ == '__main__':
    sistema = SistemaVeterinaria()
    sistema.iniciar()

        
            











        





        
    

    

    