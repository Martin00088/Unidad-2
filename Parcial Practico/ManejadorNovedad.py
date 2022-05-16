from Novedad import Novedad
import csv


class ManejadorNovedad:
    __lista = []

    def __init__(self):
        self.__lista = self.CargaLis()

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
        return self.__lista

    def getcantlist(self):
        return self.__lista
