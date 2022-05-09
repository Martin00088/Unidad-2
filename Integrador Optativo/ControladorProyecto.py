import csv
from Proyecto import Proyecto
class ManejadorProyecto:
    __lista = None

    def __init__(self):
        self.__lista = None

    """def mostrar(self):
        print("LISTA")
        for i in range(len(self.__lista)):
            print("IdProyecto:{}  ; Titulo:{} ; Palabra clave:{} ; Puntos:{}".format(self.__lista[i].getidProy(),self.__lista[i].getTit(),self.__lista[i].getPalaC(), self.__lista[i].getPuntos()))"""

    def CargaP(self):
        self.__lista = []
        archivo = open("proyectos.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                idP = str(fila[0])
                tit = str(fila[1])
                palaC = str(fila[2])
                Proy = Proyecto(idP, tit, palaC)
                self.__lista.append(Proy)
        #self.mostrar()
        return self.__lista
