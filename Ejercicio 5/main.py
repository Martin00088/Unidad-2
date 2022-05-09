from Menu import *

if __name__ == '__main__':
    print("0:Exit\n1: Actualizar el valor del vehículo de cada plan\n2: Mostrar código del plan, modelo y versión del vehículo\n3: Mostrar el monto que se debe haber pagado para licitar el vehículo\n4: Modificar la cantidad cuotas que debe tener pagas para licitar.\n----------")
    op = int(input("Elija una opcion:"))
    while op != 0:
        menu = Menu(op)
        menu.menuOp()
        print("---------\n0:Exit\n1: Actualizar el valor del vehículo de cada plan\n2: Mostrar código del plan, modelo y versión del vehículo\n3: Mostrar el monto que se debe haber pagado para licitar el vehículo\n4: Modificar la cantidad cuotas que debe tener pagas para licitar.\n----------")
        op = int(input("Elija una opcion:"))
