from biblioteca import Biblioteca
from gestor_de_usuarios import GestorDeUsuarios
from libro import Libro

def iniciarSesion():
    pass


def registrarse(gestorDeUsuarios:GestorDeUsuarios):

    print("---------------------------------------------")
    print("REGISTRO")
    print("---------------------------------------------")
    print("Presione (A) para Atras")
    print("---------------------------------------------")

    usuario = str(input("Nombre de Usuario: "))
    nombre = str(input("Nombre/s: "))
    apellido = str(input("Apellido/s: "))
    dni = str(input("DNI: "))





def imprimirLibro(libro:Libro) -> None:

    print(f"Titulo: {libro.titulo}")
    print(f"Autor: {libro.autor}")
    print(f"Fecha de Publicación: {libro.fecha_de_publicacion}")
    print(f"ISBN: {libro.isbn}")

    if (libro.estado == "P"):
        print(f"Estado: Prestado")
    else:
        print(f"Estado: Disponible")

def listarLibrosEnPantalla() -> None:

    libros = biblioteca.listarLibros()
    nro_de_libro = 1

    for libro in libros:
        print(f"............N° de Libro: {nro_de_libro}..............")
        imprimirLibro(libro)

        nro_de_libro += 1

def obtenerListadoIndexadoDeLibros():

    libros = biblioteca.listarLibros()
    listado_indexado_libros = {}
    nro_de_libro = 1

    for libro in libros:
        listado_indexado_libros[nro_de_libro] = libro.isbn
        nro_de_libro += 1

    return listado_indexado_libros

def menuBiblioteca(biblioteca:Biblioteca):

    opt = "S"

    while (opt != "X" and opt != "x"):


        titulo, autor, fecha_de_publicacion, isbn, estado = "Sin título", "Desconocido", "01/01/2025", "0000", "P"

        print("---------------------------------------------")
        print("BIBLIOTECA")
        print("---------------------------------------------")
        print("1 - Agregar Libro")
        print("2 - Listar Libros")
        print("3 - Buscar Libro")
        print("4 - Eliminar Libro de la Coleccion")
        print("5 - Registrar Prestamo de Libro")
        print("6 - Devolver Prestamo de Libro")
        print("---------------------------------------------")
        print("Presione (X) para Salir")
        print("---------------------------------------------")

        opt = str(input("Que operacion desea realizar?"))

        if (opt == "1"):

            print("Genial! Te pido los siguientes datos del Libro:")

            titulo = str(input("Titulo: "))
            autor = str(input("Autor: "))
            fecha_de_publicacion = str(input("Fecha de Publicacion (DD/MM/AAAA): "))
            isbn = str(input("ISBN: "))

            biblioteca.agregarLibro(titulo, autor, fecha_de_publicacion, isbn)

            print("Se ha agregado el Libro a la Coleccion")

        elif (opt == "2"):

            listarLibrosEnPantalla()
            print("Todos los libros fueron listados!")

        elif (opt == "3"):

            print("---------------------------------------------")
            print("Elija una Modalidad de Busqueda")
            print("---------------------------------------------")
            print("1 - Busqueda General")
            print("2 - Busqueda Avanzada")
            print("---------------------------------------------")

            modalidad_de_busqueda = str(input(""))

            if (modalidad_de_busqueda == "2"):  # Busqueda Avanzada

                print("---------------------------------------------")
                print("Elija por que parametro quiere buscar")
                print("---------------------------------------------")
                print("1 - ISBN")
                print("2 - Titulo")
                print("3 - Autor")
                print("4 - Rango de Fechas")
                print("---------------------------------------------")

                parametro_de_busqueda = str(input(""))

                if (parametro_de_busqueda == "1"):
                    dato_a_buscar = str(input("ISBN: "))
                    libro_encontrado = biblioteca.buscarLibroPorParametro(dato_a_buscar, "ISBN")

                elif (parametro_de_busqueda == "4"):
                    dato_a_buscar = str(input("Fecha de Publicacion (DD/MM/AAAA): "))
                    libro_encontrado = biblioteca.buscarLibroPorParametro(dato_a_buscar, "Fecha_de_Publicacion")

                elif (parametro_de_busqueda == "3"):
                    dato_a_buscar = str(input("Autor: "))
                    libro_encontrado = biblioteca.buscarLibroPorParametro(dato_a_buscar, "Autor")

                else:
                    dato_a_buscar = str(input("Titulo: "))
                    libro_encontrado = biblioteca.buscarLibroPorParametro(dato_a_buscar, "Titulo")

            else:  # Busqueda General
                dato_a_buscar = str(input("Genial! Introduce el dato a Buscar: "))
                libro_encontrado = biblioteca.buscarLibro(dato_a_buscar)

            # print(libro_encontrado)

            if (libro_encontrado is not None):

                print("Libro/s encontrado!")

                print("...........................")

                for libro in libro_encontrado:
                    imprimirLibro(libro)
                    print("...........................")

                print("Todos los libros fueron listados!")

            else:
                print("No se ha encontrado el Libro")

        elif (opt == "4"):

            listarLibrosEnPantalla()
            listado_indexado_libros = obtenerListadoIndexadoDeLibros()
            index = str(input("Que número de libro deseas eliminar? N° de Libro: "))
            biblioteca.eliminarLibro(listado_indexado_libros[int(index)])
            print("El libro fue eliminado! ")

        elif (opt == "5"):
            print("Registrar Prestamo de Libro")

        elif (opt == "6"):
            print("Devolver Prestamo de Libro")

        else:
            print("Adios")

        # print(opt)


# Main -----------------------------------------------

biblioteca = Biblioteca()
gestorDeUsuarios = GestorDeUsuarios()

print("---------------------------------------------")
print("Bienvenido a la Biblioteca!")
print("---------------------------------------------")
print("1 - Iniciar Sesión")
print("2 - Registrarse")
print("---------------------------------------------")
print("Presione (X) para Salir")
print("---------------------------------------------")

opt = str(input("Elija la operación a realizar: "))

if (opt == "1"):
    print("Iniciar Sesion")
    menuBiblioteca(biblioteca)

elif (opt == "2"):
    print("Registrarse")
    registrarse(gestorDeUsuarios)

else:
    print("Byee")












