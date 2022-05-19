from Persona import Persona
import csv
import numpy as np


class ManejadorPersona:
    __cantidad = 0
    __dimension = 5
    __incremento = 5
    __array = None

    def __init__(self, dimension=1, incremento=1):
        self.__array = np.empty(dimension, dtype=Persona)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def AgregarPersona(self, persona):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__array.resize(self.__dimension)
        self.__array[self.__cantidad] = persona
        self.__cantidad += 1

    def mostrar(self):
        for i in range(len(self.__array)):
            print(self.__array[i])

    def CargaArr(self):
        archivo = open("personal.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                per = Persona(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
                self.AgregarPersona(per)
        archivo.close()

    def itemA(self, listaNov, legajo):
        sueldo = 0
        i = 0
        while self.__array[i].getlegajo() != legajo and i < self.__cantidad:
            i += 1
        if i < self.__cantidad:
            sueldo = self.__array[i].getsbasico()
            for j in range(listaNov.getcantlist()):
                if listaNov.getlegajo(j) == legajo and listaNov.getcodigo(j) == "A":
                    sueldo += listaNov.getimporte(j)
                elif listaNov.getlegajo(j) == legajo and listaNov.getcodigo(j) == "D":
                    sueldo -= listaNov.getimporte(j)
        return sueldo

    def itemB1(self, listaNov):
        for i in range(len(self.__array)):
            for j in range(len(listaNov)):
                if listaNov[j].getlegajo() == self.__array[i].getlegajo() and listaNov[j].getcodigo() == "A":
                    self.__array[i].modificartotal(listaNov[j].getimporte())
                elif listaNov[j].getlegajo() == self.__array[i].getlegajo() and listaNov[j].getcodigo() == "D":
                    self.__array[i].modificartotal(-listaNov[j].getimporte())

    def ordenar(self):
        longitud = len(self.__array)
        for i in range(longitud):
            for j in range(longitud - 1):
                k = j + 1
                if self.__array[j] > self.__array[k]:
                    self.__array[k], self.__array[j] = self.__array[j], self.__array[k]

    def itemB2(self, listaNov):

        for i in range(len(self.__array)):
            print("Apellido:{}     Nombre:{}".format(self.__array[i].getapellido(), self.__array[i].getnombre()))
            print("Dni:{}".format(self.__array[i].getdni()))
            print("Sueldo Basico:{}".format(self.__array[i].getsbasico()))
            for j in range(len(listaNov)):
                if self.__array[i].getlegajo() == listaNov[j].getlegajo():
                    print("Codigo:{}  Concepto:{}  Importe:{}".format(listaNov[j].getcodigo(), listaNov[j].getconcepto(),listaNov[j].getimporte()))
            print("Total a cobrar:{}".format(self.__array[i].gettotal()))
            print("---------")

    def itemC(self):
        menor = self.__array[0]
        for i in range(len(self.__array)-1):
            if self.__array[i+1] < menor:
                menor = self.__array[i+1]
        print("El menor sueldo a cobrar es {}".format(menor.gettotal()))


