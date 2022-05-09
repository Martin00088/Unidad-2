class Proyecto:
    __idProy = None
    __titulo = None
    __palaCla = None
    __puntos = None

    def __init__(self, idP, tit, palaC):
        self.__idProy = idP
        self.__titulo = tit
        self.__palaCla = palaC
        self.__puntos = 0

    def getidProy(self):
        return self.__idProy

    def getTit(self):
        return self.__titulo

    def getPalaC(self):
        return self.__palaCla

    def getPuntos(self):
        return self.__puntos

    def actualizarpuntos(self, puntos):
        self.__puntos += puntos

