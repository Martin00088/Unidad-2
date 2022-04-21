import csv
from ViajeroFrecuente import *

if __name__ == '__main__':
    archivo = open('viajero.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        num=int(fila[0])
        dni=int(fila[1])
        nom=str(fila[2])
        ape=str(fila[3])
        mill=int(fila[4])
        viajero=Viajero(num,dni,nom,ape,mill)
        viajero.menu()
        listaViajero=[]
        listaViajero.append(viajero)
        print(listaViajero)
    archivo.close()

