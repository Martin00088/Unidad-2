from PlanAhorro import *
class Menu:
    __opcion=None
    __lista=None

    def __init__(self,lista,op):
        self.__opcion=op
        self.__lista=lista

    def actualizarValor(self):
        for i in range(len(self.__lista)):
            print("El codigo del plan es {} Modelo :{} Version: {} ".format(self.__lista[i].getCodplan(), self.__lista[i].getModelo(), self.__lista[i].getVersion()))
            self.__lista[i].modificarvalor(int(input("Ingrese el nuevo valor:")))

    def cuotaInferior(self):
        x=float(input("Ingrese un valor :"))
        for i in range(len(self.__lista)):
            if x < self.__lista[i].getValor():
                print("Codigo del plan: {} , Modelo: {} , Version: {}".format(self.__lista[i].getCodplan(), self.__lista[i].getModelo(), self.__lista[i].getVersion()))

    def montolicit(self):
        for i in range(len(self.__lista)):
            impcuota = (self.__lista[i].getValor()/ PlanAhorro.getCuotaPlan()) + self.__lista[i].getValor()*0.10
            print ("El Codigo del plan {} el Monto para licitar pagado es {}".format(self.__lista[i].getCodplan(), PlanAhorro.getCuotaLic()*impcuota))


    def menuOp(self):
        if self.__opcion == 1:
            self.actualizarValor()
        elif self.__opcion == 2:
            self.cuotaInferior()
        elif self.__opcion == 3:
            self.montolicit()
        elif self.__opcion == 4:
            print("Cantidad de cuotas pagas para licitar {}".format(PlanAhorro.getCuotaLic()))
            PlanAhorro.ModificarLic(int(input("Ingrese la nueva cantidad de cuotas pagas para licitar:")))
            print("Cantidad de cuotas pagas para licitar {}".format(PlanAhorro.getCuotaLic()))
        else:print("Error al ingresar el codigo")
