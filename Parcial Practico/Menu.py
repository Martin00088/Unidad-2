from ManejadorPersona import ManejadorPersona


class Menu:
    __instancia = None

    def __init__(self):
        self.__instancia = ManejadorPersona()

    def op(self):
        print("1:Dado el número de legajo de una persona, obtener el sueldo a liquidar (sueldo básico más los adicionales, menos los descuentos).\n2:Obtener un listado con el siguiente formato (ordenado alfabéticamente por nombre y apellido, para efectivizar el ordenamiento, debe sobrecargar el operador __gt__ en la clase que corresponda).\n3:Obtener el sueldo a cobrar más bajo de todo el personal, para ello deberá sobrecargar el operador __lt__ en la clase que corresponda.")
        opcion = int(input("Ingrese una opcion finalizar con 0:"))
        while opcion != 0:
            if opcion == 1:
                legajo = int(input("Ingrese un numero de legajo:"))
                sueldo = self.__instancia.itemA(legajo)
                print("El sueldo a liquidar es {}".format(sueldo))
            elif opcion == 2:
                self.__instancia.itemB1()
                self.__instancia.itemB2()
            elif opcion == 3:
                self.__instancia.itemC()
            else:
                print("La opcion ingresada no existe")
            opcion = int(input("Ingrese una opcion finalizar con 0:"))
