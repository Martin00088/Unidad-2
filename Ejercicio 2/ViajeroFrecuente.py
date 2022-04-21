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

    def cantidadMillasTotal(self):
        print("La cantidad de millas de {} {} total es {}".format(self.__nombre,self.__apellido,self.__millas_acum))

    def acumularMillas(self,millas):
        self.__millas_acum+millas
        print("La cantidad de millas acumuladas son {}".format(self.__millas_acum+millas))

    def canjearMillas(self,canje):
        if self.__millas_acum>=canje:
            self.__millas_acum-canje
            print("La cantidad de millas restantes son {}".format(self.__millas_acum-canje))
        else:print("Error en canje de millas,Insuficietes")


    def menu(self):
        opcion=int(input("Ingresar una opcion (1- Consultar Cantidad de Millas.2- Acumular Millas.3- Canjear Millas):"))
        if opcion==1:
            self.cantidadMillasTotal()
        elif opcion==2:
            self.acumularMillas(int(input("Ingrese la cantidad de millas para acumular:")))
        elif opcion==3:
            self.canjearMillas(int(input("Ingrese la cantidad de millas para canjear:")))
        else:print("La opcion ingresada no es correcta")
