from archivo_usuario import ArchivoUsuario

class GestorDeUsuarios:

    archivoUsuario = ArchivoUsuario()

    def __init__(self):
        pass

    def regitrarUsuario(self, usuario:str):

        if(self.validarSiExisteUsuario(usuario) == True):

            return("El ususario ya existe")

        else:
            return("Registrar Usuario")

    def iniciarSesion(self, usuario:str, clave:str):

        if(self.validarSiExisteUsuario(usuario) == True):

            if(self.validarClave(usuario, clave) == True):

                return ("Acceso Concedido")

            else:
                return ("Clave Incorrecta!")

        else:
            return ("El usuario no existe")


    def validarSiExisteUsuario(self, usuario:str) -> bool:
        pass

    def validarClave(self, usuario:str, clave:str) -> bool:
        pass
