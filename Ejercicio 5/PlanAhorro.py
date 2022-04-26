class PlanAhorro:
    __codplan = None
    __modeloV = ""
    __versionV = ""
    __valorV = None
    __cantCuotasPlan = None         #variable de clase
    __cantCuotasLicitar = None             #variable de clase

    def __init__(self, cod, mod, vers, valor):
        self.__codplan = cod
        self.__modeloV = mod
        self.__versionV = vers
        self.__valorV = valor

    def modificarvalor(self, valor):
        self.__valorV = valor
    def getCodplan(self):
        return self.__codplan

    def getModelo(self):
        return self.__modeloV

    def getVersion(self):
        return self.__versionV

    def getValor(self):
        return self.__valorV

    @classmethod
    def getCuotaPlan(cls):
        return cls.__cantCuotasPlan

    @classmethod
    def ModificarPlan(cls, valor):
        cls.__cantCuotasPlan=valor

    @classmethod
    def ModificarLic(cls, valor):
        cls.__cantCuotasLicitar = valor

    @classmethod
    def getCuotaLic(cls):
        return cls.__cantCuotasLicitar

    def asignarCuot(self, cuot):
        self.__cantCuotasLicitar=cuot
