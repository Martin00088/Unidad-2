class Email:
    __idCuenta=""
    __dominio=""
    __tipdominio=""
    __contrasena=""

    def __init__(self,i,d,t,c):
        self.__idCuenta =i
        self.__dominio =d
        self.__tipdominio =t
        self.__contrasena =c

    def retornaEmail(self):

        nombre=input("Ingrese su nombre")
        return("Estimado "+nombre+ " te enviaremos tus mensajes a la dirección:"+self.__idCuenta + "@" + self.__dominio + "." + self.__tipdominio)

    def getDominio(self):
        return (self.__dominio)

    def redContra(self,contra):
        if self.__contrasena==contra:
            self.__contrasena=input("Ingresar nueva contraseña:")
        else:print("Las contraseñas son diferentes")

    def crearCuenta(self,direccion):
        x=direccion.split("@")
        x[1]=x[1].split(".")
        self.__idCuenta=x[0]
        self.__dominio=x[1][0]
        self.__tipdominio=x[1][1]
        print(self.__idCuenta+" "+self.__dominio+" "+self.__tipdominio)

if __name__ == '__main__':
    email = Email(input("Ingrese el id de la cuenta:"),input("Ingrese el dominio de la cuenta:"),input("Ingrese el tipo de dominio:"),input("Ingrese la contraseña:"))
    print(email.retornaEmail())
    print(email.getDominio())
    email.redContra(input("Ingrese la contraseña"))
    email.crearCuenta(input("Ingrese direccion de correo"))

