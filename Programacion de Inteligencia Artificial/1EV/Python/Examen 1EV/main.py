from os import system

libros = []

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


def registrar_libro():
    titulo = input("Introduce el titulo del libro para añadir: ")
    autor = input("Introduce el autor del libro para añadir: ")
    libros_prestados = input("Cuantos libros ha prestado: ")

    libro_nuevo = Libro(titulo, autor, genero, dispo)
    libros.append(libro_nuevo)

def mostrar_libros_disponibles():
    for libro in libros:
        print(libro.titulo)
        print(libro.autor)
        print(libro.genero)
        print(libro.dispo)

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario para añadir: ")
    autor = input("Introduce el appellido del usuario para añadir: ")
    genero = input("Introduce el nombre del usuario para añadir: ")
    dispo = input("Introduce el nombre del usuario para añadir: ")

def menu():
    print("Menú de opciones:")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar libros disponibles")
    print("7. Salir\n")
    opcion = input("Introduce el número de la opción que deseas realizar: ")
    return opcion

opcion = menu()

while opcion != "7":
    if opcion == "1":
        registrar_libro()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        buscar_libro()
    elif opcion == "4":
        prestar_libro()
    elif opcion == "5":
        devolver_libro()
    elif opcion == "6":
        mostrar_libros_disponibles()
    letra = input("Presiona Enter tecla para continuar...")
    system("cls")
    opcion = menu()

print("¡Hasta luego!")