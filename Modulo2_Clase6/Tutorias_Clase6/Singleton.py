#nos asegura que una clase tenga solo una instancia
'''class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
         if not cls._instance:
              cls._instance = super(Singleton, cls).__new__(cls,*args, **kwargs)
         return cls._instance
'''
import sqlite3 # gestor o archivo de bases de datos

class DataBaseConnection:
    _instances = {}

    def __new__(cls, *args, **kwargs): #formula para crear singleton
        if cls not in cls._instances:
            cls._instances = super(DataBaseConnection,cls).__new__(cls, *args, **kwargs)
            cls._instances.connection = None
            #isinstance = super().__call__(*args, **kwargs)
            #cls._instances[cls] = isinstance
        return cls._instances
    
    def connection(self, database_name):
        if self.connection is None:
            self.connection = sqlite3.Connection(database_name)
            print('conectado a la bse de datos')
        else:
            print('ya existe una conexioin activa')
            return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print('conexion cerrada')
            self.connection = None
db1 = DataBaseConnection()
connection = db1.connect('mi_base_de_datos.db')
