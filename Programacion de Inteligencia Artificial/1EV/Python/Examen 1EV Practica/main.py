from os import system
from gestor_biblioteca import registrar_libro, registrar_usuario, buscar_libro, prestar_libro, devolver_libro, mostrar_libros_disponibles

libros = []

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
        registrar_libro(libros)
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        buscar_libro()
    elif opcion == "4":
        prestar_libro()
    elif opcion == "5":
        devolver_libro()
    elif opcion == "6":
        mostrar_libros_disponibles(libros)

    letra = input("Presiona Enter tecla para continuar...")
    system("cls")
    opcion = menu()

print("¡Hasta luego!")