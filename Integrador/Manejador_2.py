import csv
from Medicamento import Medicamento

class ManejadorMedicamento:
    __Medicamento = None

    def CargaMed(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        Medicamentos = []
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idC = int(fila[0])
                idM = int(fila[1])
                nomC = str(fila[2])
                mono = str(fila[3])
                pres = str(fila[4])
                cant = int(fila[5])
                prec = float(fila[6])
                med = Medicamento(idC, idM, nomC, mono, pres, cant, prec)
                Medicamentos.append(med)
        self.__Medicamento = Medicamentos

    def BuscarMedicamento(self, IdCama):
        cant = 0
        print("Medicamento/Monodroga        Presentacion          Cantidad               Precio")
        for i in range(len(self.__Medicamento)):
            if self.__Medicamento[i].getIdCamaMe() == IdCama:
                cant += self.__Medicamento[i].getCantApl()
                j = i
                print("{}/{}           {}                {}                  {}".format(self.__Medicamento[i].getNomC(), self.__Medicamento[i].getMono(), self.__Medicamento[i].getPres(), self.__Medicamento[i].getCantApl(), self.__Medicamento[i].getPrecT()*self.__Medicamento[i].getCantApl()))
        print("Total Adeudado: {} ".format(cant * self.__Medicamento[j].getPrecT()))
