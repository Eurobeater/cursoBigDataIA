class Biblioteca:
    pass

class Libro(Biblioteca):
    def __init__(self, titulo, autor, genero, dispo):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.dispo = dispo

class Usuario(Biblioteca):
    def __init__(self, nombre, apellido, libros_prestados):
        self.nombre = nombre
        self.apellido = apellido
        self.libros_prestados = libros_prestados

usuario1 = Usuario("Manuel", "Fernández", 0)
usuario2 = Usuario("Miguel", "Zapata", 2)

libro1 = Libro("Metro 2033", "Dmitri Glujovski", "Terror", False)
libro2 = Libro("Metro 2035", "Dmitri Glujovski", "Terror", True)



def registrar_libro(libros):
    titulo = input("Introduce el titulo del libro para añadir: ")
    autor = input("Introduce el autor del libro para añadir: ")
    genero = input("Introduce el género del libro para añadir: ")
    dispo = input("¿Está disponible? (True/False): ").lower()
    #dispo = input("¿Está disponible? (True/False): ").lower() == "true"

    libro_nuevo = Libro(titulo, autor, genero, dispo)
    libros.append(libro_nuevo)

def mostrar_libros_disponibles(libros):
    for libro in libros:
        print(f"Titulo: {libro.titulo}, autor: {libro.autor}, género: {libro.genero}, disponibilidad: {libro.dispo}")
        print("")

def buscar_libro():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario para añadir: ")
    autor = input("Introduce el appellido del usuario para añadir: ")
    libros_prestados = []