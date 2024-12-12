class Biblioteca:
    usuarios = []
    libros = []
    #libros_disponibles = []
    libros_prestados = []

    def registrar_usuario():
        nombre = input("Introduce el nombre del usuario para añadir: ")
        apellido = input("Introduce el appellido del usuario para añadir: ")
        # libros_prestados = []
        # usuario = Usuario(nombre, apellido, libros_prestados)
        usuario = Usuario(nombre, apellido)
        Biblioteca.usuarios.append(usuario)

        print("Usuarios: \n")
        for usuario in Biblioteca.usuarios:
            # print(f"Nombre: {usuario.nombre}, Apellidos: {usuario.apellido}, Libros prestados: {usuario.libros_prestados}")
            print(f"Nombre: {usuario.nombre}, Apellidos: {usuario.apellido}")

        print("")

    def registrar_libro():
        titulo = input("Introduce el titulo del libro para añadir: ")
        autor = input("Introduce el autor del libro para añadir: ")
        genero = input("Introduce el género del libro para añadir: ")
        #dispo = input("¿Está disponible? (True/False): ").lower()
        # dispo = input("¿Está disponible? (True/False): ").lower() == "true"

        #libro_nuevo = Libro(titulo, autor, genero, dispo)
        libro_nuevo = Libro(titulo, autor, genero)
        Biblioteca.libros.append(libro_nuevo)

    def mostrar_libros_disponibles():
        """
        print("Libros disponibles:")
        for libro in Biblioteca.libros_disponibles:
            print(f"Titulo: {libro.titulo}, autor: {libro.autor}, género: {libro.genero}, disponibilidad: {libro.dispo}")

        print("")
        """
        print("Libros en total:")
        for libro in Biblioteca.libros:
            # print(f"Titulo: {libro.titulo}, autor: {libro.autor}, género: {libro.genero}, disponibilidad: {libro.dispo}")
            print(f"Titulo: {libro.titulo}, autor: {libro.autor}, género: {libro.genero}")

        print("")

    def buscar_libro():
        patron = input("Introduce el nombre del libro: ")
        for libro in Biblioteca.libros:
            if patron.lower() == libro.titulo.lower():
                #return print(f"Se ha encontrado un libro: {libro.titulo}, de {libro.autor}. Disponibilidad: {libro.dispo}")
                return print(f"Se ha encontrado un libro: {libro.titulo}, de {libro.autor}")

        print("No se ha encontrado el libro")

    def prestar_libro():
        print("Libros disponibles")
        for libro in Biblioteca.libros:
            print(f"Titulo: {libro.titulo}, autor: {libro.autor}, género: {libro.genero}")

        print("")
        nombre_libro_prestar = input("Introduce el libro a prestar: ")

        if nombre_libro_prestar.lower() == libro.titulo.lower():
            Biblioteca.libros_prestados.append(libro.titulo)
        else:
            print("No se ha encontrado el libro")


class Libro(Biblioteca):
    #def __init__(self, titulo, autor, genero, dispo):
        #self.titulo = titulo
        #self.autor = autor
        #self.genero = genero
        # self.dispo = dispo

    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class Usuario(Biblioteca):
    """
    def __init__(self, nombre, apellido, libros_prestados):
        self.nombre = nombre
        self.apellido = apellido
        self.libros_prestados = libros_prestados
    """

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


usuario = Usuario("Juan", "Pérez")
Biblioteca.usuarios.append(usuario)

libro1 = Libro("Python Básico", "Autor A", "Programación")
libro2 = Libro("Python Avanzado", "Autor B", "Programación")
Biblioteca.libros.append(libro1)
Biblioteca.libros.append(libro2)


def prestar_libro():
    pass

def devolver_libro():
    pass

