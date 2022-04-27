import re

class Email:
    __idCuenta = None
    __dominio = None
    __tipoDominio = None
    __password = None

    def __init__(self, idCuenta = None, dominio = None, tipoDominio = None, password = None):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio 
        self.__password = password

    def retornaMail(self):
        mail = self.__idCuenta + "@" + self.__dominio + "." +  self.__tipoDominio
        return mail

    def getDominio(self):
        return self.__dominio

    def getPassword(self):
        return self.__password    

    def verificarRepetidos(self, identificador):
        if self.__idCuenta == identificador:
            return True
        else:
            return False        

    def cambiarPassword(self, old_password):
        if self.__password == old_password:
            new_password = input('Ingrese la nueva contrasena: ')
            print("Cambiando contrasena...")
            self.__password = new_password
            print('Contrasena cambiada con exito!')
        else:
            print('Contrasena ingresada incorrecta!')   


    def crearCuenta(self, email, password):
        self.__password = password
        aux = email.split('@')
        aux_1 = aux[1].split('.')
        #self.__idCuenta = email[:email.find('@')]
        #self.__dominio = email[email.find('@')+1:email.find('.')]
        #self.__tipoDominio = email[email.find('.')+1:]
        self.__idCuenta = aux[0]
        self.__dominio = aux_1[0]
        self.__tipoDominio = aux_1[1]

    
    





