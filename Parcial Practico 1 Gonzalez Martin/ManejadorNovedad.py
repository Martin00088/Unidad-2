from Novedad import Novedad
import csv


class ManejadorNovedad:
    __lista = []

    def __init__(self):
        self.__lista = []

    def CargaLis(self):
        archivo = open("novedades.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                nov = Novedad(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]))
                self.__lista.append(nov)

    def getlista(self):
        return self.__lista

    def getcantlist(self):
        return len(self.__lista)

    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])

    def getlegajo(self, pos):
        return self.__lista[pos].getlegajo()

    def getcodigo(self, pos):
        return self.__lista[pos].getcodigo()

    def getimporte(self, pos):
        return self.__lista[pos].getimporte()

