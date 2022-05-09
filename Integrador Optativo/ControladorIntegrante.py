import csv
from Integrante import Integrante
import numpy as np

class ManejadorIntegrantesProyecto:
    __Array = None

    """def mostrar(self):
        print("ARRAY")
        for i in range(len(self.__Array)):
            print("Idproyecto:{} ;Apellido y Nombre :{}; DNI:{}; Rol:{}; Categoria:{}\n------------".format(self.__Array[i].getIdP(),self.__Array[i].getAyN(),self.__Array[i].getDni(),self.__Array[i].getRol(),self.__Array[i].getCatInv()))"""
    def CargaI(self):
        lista = []
        archivo = open("integrantesProyecto.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idP = fila[0]
                AyN = fila[1]
                catIn = fila[3]
                dni = fila[2]
                rol = fila[4]
                lista.append(Integrante(idP, AyN, catIn, dni, rol))
                self.__Array = np.array(lista)
        #self.mostrar()

    def CalcularPtsInte(self, proyectos):
        contInt = 0
        for i in range(len(proyectos)):
            for j in range(len(self.__Array)):
                    if proyectos[i].getidProy() == self.__Array[j].getIdP():
                        contInt += 1
            if contInt >= 3:
                proyectos[i].actualizarpuntos(10)
            else:
                proyectos[i].actualizarpuntos(-20)
            print("Los integrantes son {} del id proyecto {} y los puntos son {}".format(contInt, proyectos[i].getidProy(),proyectos[i].getPuntos()))
            contInt = 0

    def CalcularPtsDir(self, proyectos):
        for i in range(len(proyectos)):
            bandera = False
            j = 0
            while proyectos[i].getidProy() == self.__Array[j].getIdP() and j < len(self.__Array) and bandera == False:
                if self.__Array[j].getRol() == "director" and (self.__Array[j].getCatInv() == "I" or self.__Array[j].getCatInv() == "II"):
                    print("GOAS")
                    bandera = True
                else:
                    j += 1
            if bandera == True:
                proyectos[i].actualizarpuntos(10)
            else:
                proyectos[i].actualizarpuntos(-5)
                print("El proyecto {} debe tener un Director con categoria I o II".format(proyectos[i].getidProy()))


    def CalcularPtsCodir(self,proyectos):
        for i in range(len(proyectos)):
            bandera = False
            j = 0
            while proyectos[i].getidProy() == self.__Array[j].getIdP() and j < len(self.__Array) and bandera == False:
                if self.__Array[j].getRol() == "codirector" and (self.__Array[j].getCatInv() == "I" or self.__Array[j].getCatInv() == "II" or self.__Array[j].getCatInv() == "III"):
                    bandera = True
                else:
                    j += 1
            if bandera == True:
                proyectos[i].actualizarpuntos(10)
            else:
                proyectos[i].actualizarpuntos(-5)
                print("El proyecto {} debe tener un Codirector con categoria I,I o III".format(proyectos[i].getidProy()))

    def CalcularPtsDirector(self,proyectos):
        for i in range(len(proyectos)):
            bandera = False
            j = 0
            while proyectos[i].getidProy() == self.__Array[j].getIdP() and j < len(self.__Array) and bandera == False:
                if self.__Array[j].getRol() == "director":
                    bandera = True
                else:
                    j += 1
            if bandera == False:
                print("El proyecto {} debe tener un Director".format(proyectos[i].getidProy()))

    def CalcularPtsCodirector(self, proyectos):
        for i in range(len(proyectos)):
            bandera = False
            j = 0
            while proyectos[i].getidProy() == self.__Array[j].getIdP() and j < len(self.__Array) and bandera == False:
                if self.__Array[j].getRol() == "codirector":
                    bandera = True
                else:
                    j += 1
            if bandera == False:
                print("El proyecto {} debe tener un Codirector".format(proyectos[i].getidProy()))

    def codianddir(self,proyectos):
        for i in range(len(proyectos)):
            bandera = False
            j = 0
            while proyectos[i].getidProy() == self.__Array[j].getIdP() and j < len(self.__Array) and bandera == False:
                if self.__Array[j].getRol() == "codirector" and self.__Array[j].getRol() == "codirector":
                    bandera = True
                else:
                    j += 1
            if bandera == False:
                proyectos[i].actualizarpuntos(-10)
    

