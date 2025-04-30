class Libro:

    def __init__(self, titulo:str, autor:str, fecha_de_publicacion:str, isbn:str):
        self.titulo = titulo
        self.autor = autor
        self.fecha_de_publicacion = fecha_de_publicacion
        self.isbn = isbn
        self.estado = "D" #D: disponible, P: Prestado

