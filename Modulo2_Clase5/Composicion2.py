class TareasEmpleado:

    def __init__(self):
        pass

    def ejecutar(self):
        pass

class TrabajoProyecto(TareasEmpleado):
    def __init__(self):
        pass

    def ejecutar(self):
        return('trabajando en un proyecto')

class Capacitacion(TareasEmpleado):
    def __init__(self):
        pass

    def ejecutar(self):
        return 'tomando una capacitacion'

class Evaluacion(TareasEmpleado):
    def __init__(self):
        pass

    def ejecutar(self):
        return 'desarrollando una evaluacion de personal'

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)  

    def  realizar_tarea(self):
        print(f'{self.nombre}, esta desarrollando las siguientes tareass: ')
        for tarea in self.tareas:
            print(f'-{tarea.ejecutar()}')

proyecto = TrabajoProyecto()
capacitacion = Capacitacion()
evaluacion = Evaluacion() 

empleado = Empleado('eduard')
empleado.asignar_tarea(proyecto)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(capacitacion)

empleado.realizar_tarea()


    
        

