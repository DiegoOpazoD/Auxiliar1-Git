class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email #hola
    

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
