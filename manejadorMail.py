import csv
from Email import Email

class Manejador:
    __listaMails = []

    def __init__(self):
        self.__listaMails = []

    def __str__(self):
        s = ''
        for mail in self.__listaMails:
            s+=str(mail.retornaMail()) + '\n'
        return s        

    def agregarMail(self, unMail):
        if type(unMail) == Email:
            self.__listaMails.append(unMail)    

    def cargarLista(self):
        archivo = open('correos.csv')
        reader = csv.reader(archivo,delimiter = ',')
        band = True
        print('Creando Instancias...')
        for fila in reader:
            if band: #saltea la lectura del encabezado
                band = False
            else:
                Mail = Email(fila[0],fila[1],fila[2],fila[3])
                self.agregarMail(Mail)
        archivo.close()

    def BuscarRepetidos(self, identificador):
        cant = 0
        for i in range(len(self.__listaMails)):
            if self.__listaMails[i].verificarRepetidos(identificador):
                print('Se detectó un mail con ese identificador')
                cant += 1
        return cant        

            







