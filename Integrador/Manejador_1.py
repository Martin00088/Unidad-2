import csv
from Cama import Cama
import numpy as np

class ManejadorCama:
    __Array=None

    def CargaCama(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        ArrayC = np.array([Cama()]*30)
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                habi = int(fila[1])
                estado = bool(fila[2])
                NyA = str(fila[3])
                diag = str(fila[4])
                fechaI = str(fila[5])
                fechaA = str(fila[6])
                cama = Cama(habi, estado, NyA, diag, fechaI, fechaA)
                if int(fila[0]) != None:
                    ArrayC[int(fila[0])-1] = cama
        self.__Array = ArrayC

    def ListaPacienteAlta(self):
        x = input("Ingrese el Nombre y Apellido de un paciente:")
        i = 0
        while i < 30 and x != self.__Array[i].getNyA():
            i += 1
        if i == 30:
            print("El paciente ingresado no se encuentra")
        else:
            print("Paciente: {}  Cama: {} Habitacion: {}".format(self.__Array[i].getNyA(), i+1, self.__Array[i].getHab()))
            print("Diagnostico: {}  Fecha de Internacion: {}".format(self.__Array[i].getDiag(), self.__Array[i].getFechI()))
            self.__Array[i].ModificarFechA()
            print("Fecha de Alta : {}".format(self.__Array[i].getFechA()))
        return i #retorna el Id de la cama

    def ListaPacienteInt(self):
        x = input("Ingrese un diagnostico:")
        for i in range(30):
            if self.__Array[i].getDiag() == x and self.__Array[i].getEstado() == True:
                    print("Habitacion:{}\nNombre y Apellido:{}\nFecha de Internacion:{}\nFecha de Alta:{}\n---------".format(self.__Array[i].getHab(), self.__Array[i].getNyA(), self.__Array[i].getFechI(), self.__Array[i].getFechA()))

