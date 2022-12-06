class Alumno:
    # nombre, dirección, teléfono y DNI
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        
    def getDni(self):
        return self.__dni

    def ver_datos(self):
        print(self.__dni, self.__nombre , self.__direccion , self.__telefono)

    def __eq__(self, otherDni):
        return self.__dni == otherDni