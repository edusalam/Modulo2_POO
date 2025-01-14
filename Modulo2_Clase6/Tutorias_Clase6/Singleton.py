#nos asegura que una clase tenga solo una instancia
'''class Singleton:
    _instance = None #LA INSTANCIA ES IGUAL A NADA

    def __new__(cls, *args, **kwargs):
         if not cls._instance:
              cls._instance = super(Singleton, cls).__new__(cls,*args, **kwargs)
         return cls._instance
'''
import sqlite3 # gestor o archivo de bases de datos

class DataBaseConnection:
    _instances = {}
    #IMPLEMENTACION METODO SINGLETON SOLO HAY UN METODO DE ACCESO, UNA CONEXION
    def __new__(cls, *args, **kwargs): #formula para crear singleton
        if not cls._instances:
            cls._instances = super(DataBaseConnection,cls).__new__(cls, *args, **kwargs)
            cls._instances.connection = None#LA INSTANCIA ES IGUAL A NADA
            #isinstance = super().__call__(*args, **kwargs)
            #cls._instances[cls] = isinstance
        return cls._instances
    # METODO CONTRUCTOR HAY VARIAS INSTANCIAS DE ACCESO, VARIAS CONEXIONES
    '''    def __init__(self):
        self.connection = None
    '''
    def connect(self, database_name):
        if self.connection is None:
            self.connection = sqlite3.Connection(database_name)
            print(f'conectado a la base de datos: {database_name} ')
        else:
            print('ya existe una conexioin activa')
        return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print('conexion cerrada')
            self.connection = None
db1 = DataBaseConnection()
connection1 = db1.connect('mi_base_de_datos.db')

db2 = DataBaseConnection()
connection2 = db2.connect('otra_base_de_datos.db')
#print(db1 == db2)

db3 = DataBaseConnection()
connection3 = db3.connect('tercera conexion a la base de datos.db')

#CERRAMOS LAS CONEXIONES DE LAS BASES DE DATOS 
db1.close_connection()
db2.close_connection()
db3.close_connection()
