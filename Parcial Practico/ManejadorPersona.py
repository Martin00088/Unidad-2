from Persona import Persona
from ManejadorNovedad import ManejadorNovedad
import csv
import numpy as np


class ManejadorPersona:
    __array=None

    def __init__(self):
        self.__array = self.CargaArr()
        self.__instancia2 = ManejadorNovedad()

    def CargaArr(self):
        archivo = open("personal.csv")
        reader = csv.reader(archivo,delimiter=";")
        lista = []
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                per = Persona(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
                lista.append(per)
        self.__array = np.array(lista)
        return self.__array

    def itemA(self, legajo):
        listaNov = self.__instancia2.getcantlist()
        sueldo = 0
        i = 0
        while self.__array[i].getlegajo() != legajo and i < len(self.__array):
            i += 1
        if i < len(self.__array):
            sueldo = self.__array[i].getsbasico()
            for j in range(len(listaNov)):
                if listaNov[j].getlegajo() == legajo and listaNov[j].getcodigo() == "A":
                    sueldo = sueldo + listaNov[j].getimporte()
                elif listaNov[j].getlegajo() == legajo and listaNov[j].getcodigo() == "D":
                    sueldo = sueldo - listaNov[j].getimporte()
        return sueldo

    def itemB1(self):
        listaNov = self.__instancia2.getcantlist()
        for i in range(len(self.__array)):
            for j in range(len(listaNov)):
                if listaNov[j].getlegajo() == self.__array[i].getlegajo() and listaNov[j].getcodigo() == "A":
                    self.__array[i].modificartotal(listaNov[j].getimporte())
                elif listaNov[j].getlegajo() == self.__array[i].getlegajo() and listaNov[j].getcodigo() == "D":
                    self.__array[i].modificartotal(-listaNov[j].getimporte())
                else:
                    self.__array[i].modificartotal(0)

    def itemB2(self):
        listaNov = self.__instancia2.getcantlist()
        self.__array.sort()

        for i in range(len(self.__array)):
            print("Apellido:{}     Nombre:{}".format(self.__array[i].getapellido(), self.__array[i].getnombre()))
            print("Dni:{}".format(self.__array[i].getdni()))
            print("Sueldo Basico:{}".format(self.__array[i].getsbasico()))
            for j in range(len(listaNov)):
                if self.__array[i].getlegajo() == listaNov[j].getlegajo():
                    print("Codigo:{}  Concepto:{}  Importe:{}".format(listaNov[i].getcodigo(), listaNov[i].getconcepto(),listaNov[i].getimporte()))

            print("Total a cobrar:{}".format(self.__array[i].gettotal()))
            print("---------")

    def itemC(self):
        menor = self.__array[0]
        for i in range(len(self.__array)-1):
            if self.__array[i+1] < menor:
                menor = self.__array[i+1]
        print("El menor sueldo a cobrar es {}".format(menor.gettotal()))


