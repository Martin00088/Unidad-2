class Medicamento:
    __idCama = None
    __idMedicamento = None
    __nombreComercial = None
    __monodroga = None
    __presentacion = None
    __cantidadAplicada = None
    __precioTotal = None

    def __init__(self ,idca ,idme, nomC, mono, pres, cantA, precT):
        self.__idCama = idca
        self.__idMedicamento = idme
        self.__nombreComercial = nomC
        self.__monodroga = mono
        self.__presentacion = pres
        self.__cantidadAplicada = cantA
        self.__precioTotal = precT

    def getIdCamaMe(self):
        return self.__idCama

    def getIdMedic(self):
        return self.__idMedicamento

    def getNomC(self):
        return self.__nombreComercial

    def getMono(self):
        return self.__monodroga

    def getPres(self):
        return self.__presentacion

    def getCantApl(self):
        return self.__cantidadAplicada

    def getPrecT(self):
        return self.__precioTotal
