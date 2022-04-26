from ViajeroFrecuente import *
if __name__=='__main__':
    v=Viajero(123, 4343434, "Martin", "Gonzalez", 900)

    v.mostrar()

    if 900 == v:
        print("La cantidad de millas igual ")
    else:print("La cantidad de millas es diferente ")

    v = 100+v
    v.mostrar()

    v = 1000-v
    v.mostrar()
