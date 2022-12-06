from ListaMultimedia import ListaMultimedia
from Multimedia import Multimedia

lista = ListaMultimedia()

multimedia1 = Multimedia("Terminator", "James Cameron", "mov", 108)
multimedia2 = Multimedia("Terminator", "James Cameron", "mp4", 108)
multimedia3 = Multimedia("Terminator 2", "James Cameron", "mp4", 108)

lista.add(multimedia1)
lista.add(multimedia2)
lista.add(multimedia3)

print(lista)