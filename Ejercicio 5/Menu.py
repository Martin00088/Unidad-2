from Manejador import Manejador
from PlanAhorro import PlanAhorro


class Menu:
    __opcion = None

    def __init__(self, op):
        self.__opcion = op

    def menuOp(self):
        if self.__opcion == 1:
            i = Manejador()
            i.Carga()
            i.actualizarValor()
        elif self.__opcion == 2:
            i = Manejador()
            i.Carga()
            i.cuotaInferior()
        elif self.__opcion == 3:
            i = Manejador()
            i.Carga()
            i.montolicit()
        elif self.__opcion == 4:
            print("Cantidad de cuotas pagas para licitar {}".format(PlanAhorro.getCuotaLic()))
            PlanAhorro.ModificarLic(int(input("Ingrese la nueva cantidad de cuotas pagas para licitar:")))
            print("Cantidad de cuotas pagas para licitar {}".format(PlanAhorro.getCuotaLic()))
        else:
            print("Error al ingresar el codigo")
