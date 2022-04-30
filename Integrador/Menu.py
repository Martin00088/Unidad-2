from Manejador_1 import ManejadorCama
from Manejador_2 import ManejadorMedicamento

class Menu:
    __opcion = None

    def __init__(self, op):
        self.__opcion = op

    def menu(self):
        if self.__opcion == 1:
            c = ManejadorCama()
            c.CargaCama()
            pos = c.ListaPacienteAlta()
            if pos < 30:
                c = ManejadorMedicamento()
                c.CargaMed()
                c.BuscarMedicamento(pos+1)

        elif self.__opcion == 2:
            c = ManejadorCama()
            c.CargaCama()
            c.ListaPacienteInt()

        else:
            print("No exite esa opcion")

