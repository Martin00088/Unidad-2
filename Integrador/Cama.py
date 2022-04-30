from datetime import datetime
class Cama:
    __idCama = None
    __habitacion = ""
    __estado = None
    __NomyApe = ""
    __diagnostico = None
    __fechaInter = ""
    __fechaAlta = ""

    def __init__(self, hab = None, est: bool = False, NyA = None, diag = None, fI = None, fA = None):
        self.__habitacion = hab
        self.__estado = est
        self.__NomyApe = NyA
        self.__diagnostico = diag
        self.__fechaInter = fI
        self.__fechaAlta = fA

    def getHab(self):
        return self.__habitacion

    def getEstado(self):
        return self.__estado

    def getNyA(self):
        return self.__NomyApe

    def getDiag(self):
        return self.__diagnostico

    def getFechI(self):
        return self.__fechaInter

    def ModificarFechA(self):
        self.__fechaAlta = datetime.today()

    def getFechA(self):
        return self.__fechaAlta
