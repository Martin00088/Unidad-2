from Menu import Menu
if __name__=='__main__':
    print("0:Exit\n1:Cargar los datos de los Proyectos desde el archivo proyectos.csv.\n2:Cargar los datos de las Personas integrantes de los Proyectos, leyendo los datos del archivo integrantesProyecto.csv.\n3:Calcular los puntos por Proyecto, teniendo en cuenta las reglas de negocio.\n4:Listar los datos de los Proyectos ordenados por puntaje (de mayor a menor puntaje, rankin de Proyectos por puntaje), para ello, el analista le solicita que en la clase Proyecto sobrecargue el operador __gt__).")
    opcion=int(input("Ingrese una opcion:"))
    while opcion != 0:
        menu = Menu()
        menu.menuOp(opcion)
        opcion=int(input("Ingrese una opcion:"))
