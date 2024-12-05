from pathlib import *


def get_recipes_path():
    return Path.home().cwd()

def menu():
    print("Menú de opciones:")
    print("1. Mostrar receta")
    print("2. Añadir receta")
    print("3. Crear categoria")
    print("4. Elimimar receta")
    print("5. Eliminar categoria")
    print("6. Salir\n")
    opcion = input("Introduce el número de la opción que deseas realizar: ")
    return opcion

def welcome():
    print("Bienvenido al libro de recetas\n")
    print("La ruta de acceso a la carpeta de recetas es: ")
    recipes_path = get_recipes_path()
    print(recipes_path)
    cantidad = Path(recipes_path).glob("**/*.txt")
    print(f"En la carpeta de recetas hay {len(list(cantidad))} recetas\n")

menu()
print(get_recipes_path())