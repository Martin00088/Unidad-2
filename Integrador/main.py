from Menu import Menu
if __name__ == '__main__':
    print("1:Listar datos del paciente de alta\n2:Listar datos de pacientes internados")
    m = Menu(int(input("Ingrese una opcion:")))
    m.menu()
