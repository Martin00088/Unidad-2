class Novedad:
    __legajo =None
    __importe=None
    __concepto=None
    __codigo=None
    __totales=None

    def __init__(self,leg,imp,con,cod):
        self.__legajo = leg
        self.__importe = imp
        self.__concepto = con
        self.__codigo = cod


    def getlegajo(self):
        return self.__legajo

    def getimporte(self):
        return self.__importe

    def getconcepto(self):
        return self.__concepto

    def getcodigo(self):
        return self.__codigo
