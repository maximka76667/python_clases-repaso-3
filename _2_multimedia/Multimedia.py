class Multimedia:
    #  título, autor, formato, y duración
    def __init__(self, titulo, autor, formato, duracion):
        self.__titulo = titulo
        self.__autor = autor
        self.__formato = formato
        self.__duracion = duracion
        
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
        
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor
        
    def get_formato(self):
        return self.__formato
    
    def set_formato(self, formato):
        self.__formato = formato
        
    def get_duracion(self):
        return self.__duracion
    
    def set_duracion(self, duracion):
        self.__duracion = duracion
        
    def __str__(self):
        return self.__titulo + ", " + self.__autor + ", " + self.__formato + ", " + str(self.__duracion)
    
    def __eq__(self, other):
        return self.__titulo == other.__titulo and self.__autor == other.__autor