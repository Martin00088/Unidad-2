class Integrante:
    __idProy=None
    __ApeyNom=None
    __dni=None
    __catInve=None
    __rol=None

    def __init__(self, idpro=None, AyN=None,cat=None, dni=None, rol=None):
        self.__idProy = idpro
        self.__ApeyNom = AyN
        self.__dni = dni
        self.__catInve = cat
        self.__rol = rol

    def getIdP(self):
        return self.__idProy

    def getAyN(self):
        return self.__ApeyNom

    def getCatInv(self):
        return self.__catInve

    def getDni(self):
        return self.__dni

    def getRol(self):
        return self.__rol
