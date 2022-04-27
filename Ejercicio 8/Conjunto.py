class Conjunto:
    __comp=None
    __conjunto=None

    def __init__(self,comp:int=0):
        self.__comp=comp
        self.__conjunto=[]
        for i in range(comp):
            self.__conjunto.append(int(input("Ingrese un numero entero:")))
        print("{}".format(self.__conjunto))

    def __add__(self, other):
        conjunt=self.__conjunto
        for i in range(other.__comp):
            band = True
            for j in range(self.__comp):
                if other.__conjunto[i] == self.__conjunto[j]:
                    band = False
            if band == True:
                conjunt.append(other.__conjunto[i])
        return conjunt

    def __sub__(self, other):
        conjunto = []
        if self.__comp >= other.__comp:
            for i in range(self.__comp):
                band = True
                for j in range(other.__comp):
                    if self.__conjunto[i] == other.__conjunto[j]:
                        band = False
                if band == True:
                    conjunto.append(self.__conjunto[i])
        return conjunto

    def __eq__(self, other):
        if self.__comp == other.__comp:
            print("El tamaño del conjunto es igual")
        band = False
        i = 0
        j = 0
        while i < self.__comp and j < other.__comp:
            if self.__conjunto[i] != other.__conjunto[j]:
                band = False
                j += 1
            else:
                band = True
                i += 1
                j = 0
        if band == True:
            print("Los componentes del Conjunto son iguales")
            return True
        else:
            print("Los componentes del Conjunto son diferentes")
            return False
