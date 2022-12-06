class ListaMultimedia:
    def __init__(self):
        self.__lista = []
        self.__tamano_lista = len(self.__lista)
        
    def size(self):
        return self.__tamano_lista
    
    def add(self, multimedia):
        if self.__tamano_lista == 200:
            return False
        self.__lista.append(multimedia)
        self.__tamano_lista += 1
        return True
    
    def get(self, position):
        try:  
            return self.__lista[position]
        except:
            print("No hay nada en esta posicion")
            
    def __str__(self):
        return "[" + str(self.__tamano_lista) + "] " + str(" ".join(map(str, self.__lista)))
