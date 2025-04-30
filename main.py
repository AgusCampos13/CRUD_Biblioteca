from biblioteca import Biblioteca

print("Bienvenido a la Biblioteca!")
opt = str(input("Queres iniciar? (S/N)"))

while (opt != "X" and opt != "x"):

    biblioteca = Biblioteca()
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

        '''
        print(biblioteca.libros[0].titulo)
        print(biblioteca.libros[0].autor)
        print(biblioteca.libros[0].fecha_de_publicacion)
        print(biblioteca.libros[0].isbn)
        print(biblioteca.libros[0].estado)
        '''

    elif (opt == "2"):
        print("Listar Libros")

    elif (opt == "3"):
        print("Buscar Libro")

    elif (opt == "4"):
        print("Eliminar Libro de la Coleccion")

    elif (opt == "5"):
        print("Registrar Prestamo de Libro")

    elif (opt == "6"):
        print("Devolver Prestamo de Libro")

    elif(opt != "X" and opt != "x"):
        print("El usuario quiere seguir operando")

    else:
        print("Adios")

    #print(opt)







