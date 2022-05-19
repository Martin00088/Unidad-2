class Persona:
    __legajo = None
    __dni = None
    __apellido = None
    __nombre = None
    __sbasico = None
    __total = None

    def __init__(self, leg, dni, ape, nom, sbas):
        self.__legajo = leg
        self.__dni = dni
        self.__apellido = ape
        self.__nombre = nom
        self.__sbasico = sbas
        self.__total = self.__sbasico

    def __gt__(self, other):
        return self.__apellido > other.__apellido

    def __lt__(self, other):
        return self.__total < other.__total

    def __str__(self):
        return "Lejago:{} DNI:{} Apellido:{} Nombre:{} SBasico:{} Total:{}".format(self.__legajo, self.__dni, self.__apellido, self.__nombre, self.__sbasico, self.__total)

    def getlegajo(self):
        return self.__legajo

    def getdni(self):
        return self.__dni

    def getapellido(self):
        return self.__apellido

    def getnombre(self):
        return self.__nombre

    def getsbasico(self):
        return self.__sbasico

    def modificartotal(self, sueldo):
        self.__total += sueldo

    def gettotal(self):
        return self.__total
