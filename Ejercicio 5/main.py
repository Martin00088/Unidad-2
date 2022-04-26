import csv

from PlanAhorro import *

from Menu import *

if __name__ == '__main__':
    archivo = open('planes.csv')
    reader = csv.reader(archivo,delimiter=';')
    Planes = []
    for fila in reader:
        cod = int(fila[0])
        modelo = fila[1]
        version = fila[2]
        valor = float(fila[3])
        cantcuotasplan = int(fila[4])
        cantcuotaslic = int(fila[5])
        Planes.append(PlanAhorro(cod, modelo, version, valor))
    PlanAhorro.ModificarPlan(cantcuotasplan)
    PlanAhorro.ModificarLic(cantcuotaslic)
    print("1: Actualizar el valor del vehículo de cada plan")
    print("2: Mostrar código del plan, modelo y versión del vehículo")
    print("3: Mostrar el monto que se debe haber pagado para licitar el vehículo")
    print("4: Modificar la cantidad cuotas que debe tener pagas para licitar.")
    op=int(input("Elija una opcion:"))
    menu = Menu(Planes, op)
    menu.menuOp()
