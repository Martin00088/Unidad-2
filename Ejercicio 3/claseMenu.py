class Menuop:
    __opcion = None
    __lista = None

    def __init__(self, list, op):
        self.__opcion = op
        self.__lista = list

    def menorvalor(self, var):
        if var == "Humedad":
            x = 23123123
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getHumedad() < x:
                        x = self.__lista[i][j].getHumedad()
                        dia = i+1
                        hora = j+1
            return dia, hora
        elif var == "Temperatura":
            x = 23123123
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getTemperatura() < x:
                        x = self.__lista[i][j].getTemperatura()
                        dia = i+1
                        hora = j+1
            return dia, hora
        elif var == "Presion":
            x = 23123123
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getPresion() < x:
                        x = self.__lista[i][j].getPresion()
                        dia = i+1
                        hora = j+1
            return dia, hora
        else:
            return "Error"

    def mayorvalor(self, var):
        if var == "Humedad":
            x = -323123
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getHumedad() > x:
                        x = self.__lista[i][j].getHumedad()
                        dia = i+1
                        hora = j+1
            return dia,hora
        elif var == "Temperatura":
            x = -123123
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getTemperatura() > x:
                        x = self.__lista[i][j].getTemperatura()
                        dia = i+1
                        hora = j+1
            return dia, hora
        elif var == "Presion":
            x = -23123
            dia = -1
            hora = -1
            for i in range(30):
                for j in range(24):
                    if self.__lista[i][j].getPresion() > x:
                        x = self.__lista[i][j].getPresion()
                        dia = i+1
                        hora = j+1
            return dia,hora
        else:
            return "Error"

    def mostrarNumero(self):
        variables=["Humedad", "Temperatura", "Presion"]
        for variable in variables:
            print("Para la variable {} el dia y hora de menor valor es {} y el dia y hora de mayor valor es {}".format(variable, self.menorvalor(variable), self.mayorvalor(variable)))

    def promedio(self):
        for i in range(30):
            x = 0
            for j in range(24):
                x += self.__lista[i][j].getTemperatura()
            print("El promedio del dia {} por cada hora es {}".format(i+1, x/30))

    def Listado(self):
        x=int(input("Ingrese un numero de Dia para indicar las variables:"))
        print("Hora      Temperatura      Humedad      Presion")
        for i in range(24):
            print("  {}            {}             {}           {}".format(i+1, self.__lista[x][i].getTemperatura(), self.__lista[x][i].getHumedad(), self.__lista[x][i].getPresion()))

    def menu(self):
        if self.__opcion == 1:
            self.mostrarNumero()
        elif self.__opcion == 2:
            self.promedio()
        elif self.__opcion == 3:
            self.Listado()
        else: print("Error al ingresar el codigo ")


