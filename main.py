from Email import Email
from manejadorMail import Manejador

def test():
    print('Iniciando test...')
    mail1 = Email()
    mail2 = Email()
    mail3 = Email()
    mail1.crearCuenta('informaticafcefn@gmail.com','facultad123')
    mail2.crearCuenta('juanLiendro1957@yahoo.com', 'juan123')
    mail3.crearCuenta('CarlosPaez01@hotmail.com', 'carlos123')
    print('Direcciones creadas:\n{}\n{}\n{}'. format(mail1.retornaMail(),mail2.retornaMail(),mail3.retornaMail()))
    mail1.cambiarPassword('facultad12')
    print('Cerrando test...\n\n\n')

if __name__ == '__main__':
    test()
    lista = Manejador()
    lista.cargarLista()
    nombre = input('Ingrese su nombre y apellido: ')
    id_cuenta = input('Ingrese el id de cuenta: ')
    dominio = input('Ingrese el dominio: ')
    tipo_dominio = input('Ingrese el tipo de dominio: ')
    contra = input('Ingrese una contrasena: ')
    MailUsuario = Email(id_cuenta,dominio,tipo_dominio,contra)
    print('Estimado {} te enviaremos tus mensajes a la dirección {}.' .format(nombre,MailUsuario.retornaMail()))
    vieja_contra = input('Ingrese la contrasena actual: ')
    MailUsuario.cambiarPassword(vieja_contra)
    print(lista)
    identificador = input('Ingrese un identificador: ')
    cantidad = lista.BuscarRepetidos(identificador)
    if cantidad <= 1:
        print('No se encontraron mails repetidos con ese identificador!')
    else:
        print('Cantidad de mails con el identificador {}: {}' .format(identificador,cantidad))
   

  


     
     
     



 
   


