from libro import Libro
import os

class ArchivoLibro:

    def __init__(self):

        print("Llego al constructor de ArchivoLibro!")

        try:
            with open("recursos/libros.txt", "a", encoding="utf-8") as archivo_biblioteca:
                print("Libros existe")
                archivo_biblioteca.write("Titulo,Autor,Fecha de Publicacion,ISBN,Estado\n")

        except FileNotFoundError:
            #Creacion del Archivo
            print("Libros no existe")
            with open("recursos\\libros.txt", 'w', encoding="utf-8") as archivo_biblioteca:
                archivo_biblioteca.write("Titulo,Autor,Fecha de Publicacion,ISBN,Estado\n")

        except Exception as e:
            print(f"Error inesperado al guardar el libro: {e}")

    @staticmethod #Porque no necesitamos self, en el parametro. No modificamos la instancia
    def agregarLibroAlArchivo(nuevo_libro: Libro) -> None:

        try:
            with open("recursos\\libros.txt", 'a', encoding="UTF-8") as archivo_biblioteca:

                # Agregando el libro:
                archivo_biblioteca.writelines([nuevo_libro.titulo, ","
                                                  , nuevo_libro.autor, ","
                                                  , nuevo_libro.fecha_de_publicacion, ","
                                                  , nuevo_libro.isbn, ","
                                                  , nuevo_libro.estado])

                archivo_biblioteca.write("\n")

        except Exception as e:
            print(f"Error inesperado al guardar el libro: {e}")






