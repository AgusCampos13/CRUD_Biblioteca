class Libro:

    def __init__(self, titulo:str, autor:str, fecha_de_publicacion:str, isbn:str):
        self.titulo = titulo
        self.autor = autor
        self.fecha_de_publicacion = fecha_de_publicacion
        self.isbn = isbn
        self.estado = "D" #D: disponible, P: Prestado


    #Valida si dos libros son de la misma clase y si tienen el mismo ISBN, dato que usamos como ID
    def __eq__(self, other):
        return self.titulo == other.titulo and self.isbn == other.isbn