from libro import Libro
import os

class ArchivoLibro:

    diccionario_de_parametros = {}
    cabecera = "Titulo,Autor,Fecha de Publicacion,ISBN,Estado\n"
    ruta = "recursos\\libros.txt"

    def __init__(self, diccionario_de_parametros):

        self.diccionario_de_parametros = diccionario_de_parametros.copy()

        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo_biblioteca:
                #print("Libros existe")
                #archivo_biblioteca.write("Titulo,Autor,Fecha de Publicacion,ISBN,Estado\n")
                pass


        except FileNotFoundError:
            #Creacion del Archivo
            #print("Libros no existe")
            with open(self.ruta, 'w', encoding="utf-8") as archivo_biblioteca:
                archivo_biblioteca.write(self.cabecera)

        except Exception as e:
            #print(f"Error inesperado al guardar el libro: {e}")
            pass


    def sobreEscribirArchivo(self):
        with open(self.ruta, 'w', encoding="UTF-8") as archivo_biblioteca:
            archivo_biblioteca.write(self.cabecera)

    def agregarLibroAlArchivo(self, nuevo_libro: Libro) -> str:

        try:
            with open(self.ruta, 'a', encoding="UTF-8") as archivo_biblioteca:

                # Agregando el libro:
                archivo_biblioteca.writelines([nuevo_libro.titulo, ","
                                                  , nuevo_libro.autor, ","
                                                  , nuevo_libro.fecha_de_publicacion, ","
                                                  , nuevo_libro.isbn, ","
                                                  , nuevo_libro.estado])

                archivo_biblioteca.write("\n")

        except Exception as e:
            return(f"Error inesperado al guardar el libro: {e}")

    def listarLibros(self): # Retorna un listado de Libros

        libros = []

        try:
            with open(self.ruta, 'r', encoding="UTF-8") as archivo_biblioteca:

                libros_leidos = archivo_biblioteca.readlines()


                #Remueve la Cabecera
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
            return(f"Error inesperado al leer los libros: {e}")

    def buscarLibroPorParametro(self, dato_a_buscar:str, parametro:int): #Devuelve lista de libros

        '''
        parametro = 0 --> Titulo
        parametro = 1 --> Autor
        parametro = 3 --> ISBN

        '''

        libros_coincidentes_con_busqueda = []

        try:
            with open(self.ruta, 'r', encoding="UTF-8") as archivo_biblioteca:

                libros_leidos = archivo_biblioteca.readlines()

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

                if (len(libros_coincidentes_con_busqueda)!= 0):
                    return libros_coincidentes_con_busqueda

                else:
                    return None


        except Exception as e:
            return (f"Error inesperado al leer los libros: {e}")

