from pathlib import *
from platform import system
# import pathlib

def get_recipes_path():
    return Path(Path.home().cwd(), "recetas")

def welcome():
    print("Bienvenido al libro de recetas\n")
    print("La ruta de acceso a la carpeta de recetas es: ")
    recipes_path = get_recipes_path()
    print(recipes_path)
    cantidad = Path(recipes_path).glob("**/*.txt")
    print(f"En la carpeta de recetas hay {len(list(cantidad))} recetas\n")

def menu():
    print("Menú de opciones:")
    print("1. Mostrar receta")
    print("2. Añadir receta")
    print("3. Crear categoría")
    print("4. Elimimar receta")
    print("5. Eliminar categoría")
    print("6. Salir\n")
    opcion = input("Introduce el número de la opción que deseas realizar: ")
    return opcion


# Programa principal
welcome()
opcion = menu()

while opcion != 6:
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    system("clear")
    opcion = menu()
print("¡Hasta luego!")


























"""
opcion_usuario = 0

def saludar():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@ Bienvenido, usuario @@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")

def terminar_programa():
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@ Hasta la próxima @@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def listar_opciones():
    opcion1 = "Opcion 1"
    opcion2 = "Opcion 2"
    opcion3 = "Opcion 3"
    opcion4 = "Opcion 4"
    opcion5 = "Opcion 5"
    opcion6 = "Opcion 6"

    print("******** Elige una opción **********")
    print(f"- {opcion1}")
    print(f"- {opcion2}")
    print(f"- {opcion3}")
    print(f"- {opcion4}")
    print(f"- {opcion5}")
    print(f"- {opcion6}")

saludar()

while opcion_usuario != 6:
    listar_opciones()
    opcion_usuario = int(input("Elige una opción: "))
    if opcion_usuario == 6:
        terminar_programa()
"""


