class Administrator:
    def __init__(self):
        self.__alumnos = []
        
    def anhadir_alumno(self, alumno):
        if self.buscar_alumno(alumno.getDni()) >= 0:
            print("Alumno ya existe")
            return;
        self.__alumnos.append(alumno)
        
    def buscar_alumno(self, dni):
        try:
            return self.__alumnos.index(dni)
        except:
            return -1
    
    def mostrar_alumno(self, dni):
        index = self.buscar_alumno(dni)
        if index < 0:
            print("Alumno no encontrado")
            return
        self.__alumnos[index].ver_datos()
        
        
    def ver_alumnos(self):
        for alumno in self.__alumnos:
            alumno.ver_datos()
