class Ventana:
    __titulo=""
    __superiorIzqx=None
    __superiorIzqy=None
    __inferiorDerx=None
    __inferiorDery=None

    def __init__(self, tit, SiX:int=10, SiY:int=10, IzX:int=100 , InY:int=100):
        self.__titulo=tit
        self.__superiorIzqx = SiX
        self.__superiorIzqy = SiY
        self.__inferiorDerx = IzX
        self.__inferiorDery = InY

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__inferiorDery-self.__superiorIzqy

    def ancho(self):
        return self.__inferiorDerx-self.__superiorIzqx

    def mostrar(self):
        print("EL titulo es {} ,({},{})superior Izquierdo , ({},{}) Inferiro Derecho".format(self.__titulo, self.__superiorIzqx,self.__superiorIzqy,self.__inferiorDerx,self.__inferiorDery))

    def moverIzquierda(self,mov:int=0):
        if mov <= self.__inferiorDerx and mov >= self.__superiorIzqx:
            if self.__superiorIzqx >= 0:
                if self.__inferiorDerx >= 0:
                    print("Se movio a la izquierda: SupIzq({},{}) InfDer({},{})".format(self.__superiorIzqx-mov,self.__superiorIzqy, self.__inferiorDerx-mov,self.__inferiorDery))
                else: print("La ventana es menor a 0")

    def moverDerecha(self,mov:int=0):
        if self.__superiorIzqx + mov <= 500:
            if self.__inferiorDerx + mov <= 500:
                print("Se movio a la derecha : SupIzq({},{}) InfDer({},{})".format(self.__superiorIzqx+mov,self.__superiorIzqy, self.__inferiorDerx+mov, self.__inferiorDery))
            else:print("La ventana es mayor a 500")

    def bajar(self,mov:int=0):
        if self.__superiorIzqy + mov <=500 and self.__inferiorDery + mov<=500:
            print("Se movio para abajo: SupIzq({},{}) InfDer({},{})".format(self.__superiorIzqx,self.__superiorIzqy+mov,self.__inferiorDerx, self.__inferiorDery+mov))

    def subir(self,mov:int=0):
        if self.__superiorIzqy - mov >=0 and self.__inferiorDery - mov >=0:
            print("Se movio para arriba: SupIzq({},{}) InfDer({},{})".format(self.__superiorIzqx,self.__superiorIzqy-mov,self.__inferiorDerx, self.__inferiorDery-mov))
