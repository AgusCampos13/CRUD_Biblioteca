from libro import Libro
from archivo_libro import ArchivoLibro

class Biblioteca:

    #Mapeo de Parametros
    diccionario_de_parametros = {

        "Titulo": 0,
        "Autor": 1,
        "Fecha_de_Publicacion": 2,
        "ISBN": 3,
        "Estado": 4
    }

    libros = []
    ArchivoLibro = ArchivoLibro(diccionario_de_parametros)

    def __init__(self):
        pass

    def obtenerListadoUnicoDeLibros(self, libros_existentes, nueva_lista_de_libros):

        libros_unicos = libros_existentes
        for i in nueva_lista_de_libros:  # 4, 9, 8 , 0

            elemento_repetido = False
            for j in libros_unicos:  # 4 = 1, 4 = 2, 4 = 3, 4 = 4, 4 = 5

                #print(f" {i.isbn}  {j.isbn}")

                if i.__eq__(j):
                    elemento_repetido = True

            #print(f" elemento_repetido: {elemento_repetido}")
            if (elemento_repetido == False):
                libros_unicos.append(i)

        return libros_unicos

    def agregarLibro(self, titulo:str, autor:str, fecha_de_publicacion:str, isbn:str) -> str: #otros tipos de dato posibles int, float, bool, list[<tipo_de_dato>] dict[<tipo_de_dato>,<tipo_de_dato>]

        nuevo_libro = Libro(titulo, autor, fecha_de_publicacion, isbn)
        self.libros.append(nuevo_libro)

        #print(f" len(self.libros-1): {len(self.libros)-1} self.libros[len(self.libros-1)] {self.libros[len(self.libros)-1]}")
        return(self.ArchivoLibro.agregarLibroAlArchivo(self.libros[len(self.libros)-1]))

    def listarLibros(self): #Devuelve un array de Libros

        libros = self.ArchivoLibro.listarLibros()
        return(libros)

    def buscarLibro(self, dato_a_buscar:str): #Devuelve un array de Libros

        libros_coincidentes_con_busqueda = []

        # Busqueda por ISBN
        libros_aux = self.ArchivoLibro.buscarLibroPorParametro(dato_a_buscar, self.diccionario_de_parametros["ISBN"])
        if (libros_aux is not None):
            libros_coincidentes_con_busqueda = libros_coincidentes_con_busqueda + libros_aux

        #Busqueda por Titulo
        libros_aux = self.ArchivoLibro.buscarLibroPorParametro(dato_a_buscar, self.diccionario_de_parametros["Titulo"])
        if (libros_aux is not None):

            libros_coincidentes_con_busqueda = self.obtenerListadoUnicoDeLibros(libros_coincidentes_con_busqueda, libros_aux)

        #Buqueda por Autor
        libros_aux = self.ArchivoLibro.buscarLibroPorParametro(dato_a_buscar, self.diccionario_de_parametros["Autor"])
        if (libros_aux is not None):
            libros_coincidentes_con_busqueda = self.obtenerListadoUnicoDeLibros(libros_coincidentes_con_busqueda,
                                                                                libros_aux)

        return (libros_coincidentes_con_busqueda)

    def buscarLibroPorParametro(self, dato_a_buscar:str, parametro:int):

        parametro = self.diccionario_de_parametros[parametro]

        libros_coincidentes_con_busqueda = self.ArchivoLibro.buscarLibroPorParametro(dato_a_buscar, parametro)
        return (libros_coincidentes_con_busqueda)

    def eliminarLibro(self, isbn_a_eliminar):

        libros = self.ArchivoLibro.listarLibros()
        self.ArchivoLibro.sobreEscribirArchivo()
        for libro in libros:
            if(libro.isbn != isbn_a_eliminar):
                self.ArchivoLibro.agregarLibroAlArchivo(libro)









