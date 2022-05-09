from PlanAhorro import PlanAhorro
import csv


class Manejador:
    __lista = None

    def Carga(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        planes = []
        for fila in reader:
            cod = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = float(fila[3])
            cantcuotasplan = int(fila[4])
            cantcuotaslic = int(fila[5])
            planes.append(PlanAhorro(cod, modelo, version, valor))
        self.__lista = planes
        PlanAhorro.ModificarPlan(cantcuotasplan)
        PlanAhorro.ModificarLic(cantcuotaslic)

    def actualizarValor(self):
        for i in range(len(self.__lista)):
            print("El codigo del plan es {} Modelo :{} Version: {} ".format(self.__lista[i].getCodplan(), self.__lista[i].getModelo(), self.__lista[i].getVersion()))
            self.__lista[i].modificarvalor(int(input("Ingrese el nuevo valor:")))

    def cuotaInferior(self):
        x = float(input("Ingrese un valor :"))
        for i in range(len(self.__lista)):
            if x < self.__lista[i].getValor():
                print("Codigo del plan: {} , Modelo: {} , Version: {}".format(self.__lista[i].getCodplan(), self.__lista[i].getModelo(), self.__lista[i].getVersion()))

    def montolicit(self):
        for i in range(len(self.__lista)):
            impcuota = (self.__lista[i].getValor() / PlanAhorro.getCuotaPlan()) + self.__lista[i].getValor()*0.10
            print("El Codigo del plan {} el Monto para licitar pagado es {}".format(self.__lista[i].getCodplan(), PlanAhorro.getCuotaLic()*impcuota))
