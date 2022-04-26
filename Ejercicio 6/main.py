from ViajeroFrecuente import *
if __name__=='__main__':
    viajero=Viajero(123, 4343434, "Martin", "Gonzalez", 900)

    viajero=600+viajero
    viajero.mostrar()

    if viajero > 900:
        print("La cantidad de millas es mayor ")
    else:print("La cantidad de millas es menor ")

    viajero=2000-viajero
    viajero.mostrar()
