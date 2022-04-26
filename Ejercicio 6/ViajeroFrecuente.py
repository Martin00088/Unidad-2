class Viajero:
    __num_viajero=""
    __dni=""
    __nombre=""
    __apellido=""
    __millas_acum=""

    def __init__(self,num,dni,nom,ap,mill):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ap
        self.__millas_acum=mill
    
    def __gt__(self,other):
        if self.__millas_acum > other:
            return True
        else :return False

    def __add__(self, other):
        self.__millas_acum+other
        print("Millas acumuladas con exito")
        return Viajero(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum+other)

    def __radd__(self, other):
        self.__millas_acum+other
        print("Millas acumuladas con exito")
        return Viajero(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum+other)

    def __sub__(self, other):
        if other <= self.__millas_acum:
            print("Millas canjeadas con exito")
            self.__millas_acum-other
            return Viajero(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-other)
        else: print("No se puede realizar la seguiente operacion Millas insuficientes")

    def __rsub__(self, other):
        if self.__millas_acum <= other:
            print("Millas canjeadas con exito")
            other-self.__millas_acum
            return Viajero(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,other-self.__millas_acum)
        else: print("No se puede realizar la seguiente operacion Millas insuficientes")

    def mostrar(self):
        print("------------------")
        print("El numero de viajero es {}".format(self.__num_viajero))
        print("El DNI de viajero es {}".format(self.__dni))
        print("El nombre del viajero es {}".format(self.__nombre))
        print("El apellido del viajero es {}".format(self.__apellido))
        print("Las millas acumuladas del viajero son {}".format(self.__millas_acum))
        print("------------------")
