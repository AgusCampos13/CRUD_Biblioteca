from usuario import Usuario

class ArchivoUsuario:

    diccionario_de_parametros = {}
    cabecera = "Usuario, Nombre, Apellido, Clave, DNI\n"
    ruta = "recursos\\usuarios.txt"

    def __init__(self):

        print("Constructor de ArchivoUsuario")

        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo_usuario:
                #print("Usuarios existe")
                pass


        except FileNotFoundError:
            # Creacion del Archivo
            #print("Usuarios no existe")
            with open(self.ruta, 'w', encoding="utf-8") as archivo_usuario:
                archivo_usuario.write(self.cabecera)

        except Exception as e:
            # print(f"Error inesperado al guardar el libro: {e}")
            pass

    
    def sobreEscribirArchivo(self):
        with open(self.ruta, 'w', encoding="UTF-8") as archivo_usuario:
            archivo_usuario.write(self.cabecera)

    def escribirUsuario(self, nuevo_usuario: Usuario) -> str:

        try:
            with open(self.ruta, 'a', encoding="UTF-8") as archivo_usuario:

                # Agregando el libro:
                archivo_usuario.writelines([nuevo_usuario.usuario, ","
                                                  , nuevo_usuario.nombre, ","
                                                  , nuevo_usuario.apellido, ","
                                                  , nuevo_usuario.clave, ","
                                                  , nuevo_usuario.dni])

                archivo_usuario.write("\n")

        except Exception as e:
            return (f"Error inesperado al guardar el libro: {e}")

    '''

    def buscarUsuario(self, usuario_a_buscar: str):  # Devuelve lista de libros

        usuario_encontrado = None

        try:
            with open(self.ruta, 'r', encoding="UTF-8") as archivo_usuario:

                usuarios_leidos = archivo_usuario.readlines()

                # Remueve la Cabecera
                for i in range(1, len(usuarios_leidos)):

                    usuario_leido = usuarios_leidos[i]
                    datos_del_usuario = usuario_leido.strip().split(",")

                    usuario_aux = Libro(
                        datos_del_usuario[0],  # Usuario
                        datos_del_usuario[1],  # Nombre
                        datos_del_usuario[2],  # Apellido
                        datos_del_usuario[3],  # Clave
                        datos_del_usuario[4])  # DNI

                    if (usuario_a_buscar.lower() in datos_del_usuario[parametro].lower()):
                        libros_coincidentes_con_busqueda.append(libro_aux)

                if (len(libros_coincidentes_con_busqueda) != 0):
                    return libros_coincidentes_con_busqueda

                else:
                    return None


        except Exception as e:
            return (f"Error inesperado al leer los libros: {e}")

 
    def agregarLibroAlArchivo(self, nuevo_libro: Libro) -> str:

        try:
            with open(self.ruta, 'a', encoding="UTF-8") as archivo_usuario:

                # Agregando el libro:
                archivo_usuario.writelines([nuevo_libro.titulo, ","
                                                  , nuevo_libro.autor, ","
                                                  , nuevo_libro.fecha_de_publicacion, ","
                                                  , nuevo_libro.isbn, ","
                                                  , nuevo_libro.estado])

                archivo_usuario.write("\n")

        except Exception as e:
            return (f"Error inesperado al guardar el libro: {e}")

    def listarLibros(self):  # Retorna un listado de Libros

        libros = []

        try:
            with open(self.ruta, 'r', encoding="UTF-8") as archivo_usuario:

                libros_leidos = archivo_usuario.readlines()

                # Remueve la Cabecera
                for i in range(1, len(libros_leidos)):
                    libro_leido = libros_leidos[i]
                    datos_del_libro = libro_leido.strip().split(",")

                    libro_aux = Libro(
                        datos_del_libro[0],
                        datos_del_libro[1],
                        datos_del_libro[2],
                        datos_del_libro[3])

                    libro_aux.estado = datos_del_libro[4]
                    libros.append(libro_aux)

                return libros

        except Exception as e:
            return (f"Error inesperado al leer los libros: {e}")

    def buscarLibroPorParametro(self, dato_a_buscar: str, parametro: int):  # Devuelve lista de libros

        libros_coincidentes_con_busqueda = []

        try:
            with open(self.ruta, 'r', encoding="UTF-8") as archivo_usuario:

                libros_leidos = archivo_usuario.readlines()

                # Remueve la Cabecera
                for i in range(1, len(libros_leidos)):

                    libro_leido = libros_leidos[i]
                    datos_del_libro = libro_leido.strip().split(",")

                    libro_aux = Libro(
                        datos_del_libro[0],  # Titulo
                        datos_del_libro[1],  # Autor
                        datos_del_libro[2],  # Fecha de Publicación
                        datos_del_libro[3])  # ISBN

                    libro_aux.estado = datos_del_libro[4]

                    if (dato_a_buscar.lower() in datos_del_libro[parametro].lower()):
                        libros_coincidentes_con_busqueda.append(libro_aux)

                if (len(libros_coincidentes_con_busqueda) != 0):
                    return libros_coincidentes_con_busqueda

                else:
                    return None


        except Exception as e:
            return (f"Error inesperado al leer los libros: {e}")

    '''