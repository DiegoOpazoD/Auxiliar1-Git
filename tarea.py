class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listo = False

    def obtenerNombre(self):
        return self.nombre

    def estaLista(self):
        return self.listo
    
    def terminar(self):
        self.listo = True
        
    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"La tarea {tarea.obtenerNombre()} está lista")
                print(f"La tarea {tarea.obtenerNombre()} no está lista")  
