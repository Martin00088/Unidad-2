from ControladorProyecto import ManejadorProyecto
from ControladorIntegrante import ManejadorIntegrantesProyecto


class Menu:
    __opcion=None

    def menuOp(self, opcion):
        self.__opcion = opcion
        if self.__opcion == 1:
            p = ManejadorProyecto()
            p.CargaP()

        elif self.__opcion == 2:
            i = ManejadorIntegrantesProyecto()
            i.CargaI()

        elif self.__opcion == 3:
            p = ManejadorProyecto()
            i = ManejadorIntegrantesProyecto()
            i.CargaI()
            lista = p.CargaP()
            i.CalcularPtsInte(lista)
            i.CalcularPtsDir(lista)
            i.CalcularPtsCodir(lista)
            i.CalcularPtsDirector(lista)
            i.CalcularPtsCodirector(lista)
            i.codianddir(lista)
            for i in range(len(lista)):
                print(lista[i].getPuntos())

        elif self.__opcion == 4:
            ManejadorProyecto.ListarOrdenProy()


