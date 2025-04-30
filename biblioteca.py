from libro import Libro
from archivo import ArchivoLibro

class Biblioteca:

    libros = []
    ArchivoLibro = ArchivoLibro()

    def __init__(self):
        pass

    def agregarLibro(self, titulo:str, autor:str, fecha_de_publicacion:str, isbn:str) -> None: #otros tipos de dato posibles int, float, bool, list[<tipo_de_dato>] dict[<tipo_de_dato>,<tipo_de_dato>]

        nuevo_libro = Libro(titulo, autor, fecha_de_publicacion, isbn)
        self.libros.append(nuevo_libro)

        #print(f" len(self.libros-1): {len(self.libros)-1} self.libros[len(self.libros-1)] {self.libros[len(self.libros)-1]}")
        self.ArchivoLibro.agregarLibroAlArchivo(self.libros[len(self.libros)-1])


