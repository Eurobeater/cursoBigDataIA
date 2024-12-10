from pathlib import *
from platform import system
from select import select
from os import system
# import pathlib

def get_recipes_path():
    return Path(Path.home().cwd(), "recetas")

def get_category_path(categoria):
    return Path(get_recipes_path(), categoria)

def get_recipe_path(categoria, recipe):
    return Path(get_category_path(categoria), recipe + ".txt")

def welcome():
    print("Bienvenido al libro de recetas\n")
    print("La ruta de acceso a la carpeta de recetas es: ")
    recipes_path = get_recipes_path()
    print(recipes_path)
    cantidad = Path(recipes_path).glob("**/*.txt")
    print(f"En la carpeta de recetas hay {len(list(cantidad))} recetas\n")

def select_category():
    print("Las categorias de recetas disponibles son: ")
    recipes_path = get_recipes_path()
    for categoria in Path(recipes_path).iterdir():
        print(categoria.name)
    print("\n")
    categoria = input("Introduce el nombre de la categoria que deseas seleccionar: ")
    return categoria, get_category_path(categoria)

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

def show_recipe():
    categoria, category_path = select_category()
    print(f"Las recetas de la categoría {categoria} son: ")
    for receta in Path(category_path).iterdir():
        print(receta.stem)
    print("\n")
    receta = input("Introduce el nombre de la receta que deseas ver: ")
    receta_path = get_recipe_path(categoria, receta)
    print("\n")
    print(receta_path.read_text())
    print("\n")

def add_recipe():
    categoria,category_path = select_category()
    receta = input("Introduce el nombre de la receta que deseas añadir: ")
    receta_path = get_recipe_path(categoria, receta)
    receta_path.touch()
    contenido = input("Introduce el contenido de la receta: ")
    receta_path.write_text(contenido)
    print("Receta añadida correctamente\n")

def create_category():
    categoria = input("Introduce el nombre de la categoría que deseas crear: ")
    category_path = get_category_path(categoria)
    category_path.mkdir()
    print("Categoria creada correctamente\n")

def delete_recipe():
    categoria, category_path = select_category()
    receta = input("Introduce el nombre de la receta qeu deseas eliminar: ")
    receta_path = get_recipe_path(categoria, receta)
    receta_path.unlink()
    print("Receta eliminada correctamente\n")

def delete_category():
    categoria = input("Introduce el nombre de la categoría que deseas eliminar: ")
    category_path = get_category_path(categoria)
    category_path.unlink()
    print("Categoria creada correctamente\n")

# Programa principal
welcome()
opcion = menu()

while opcion != "6":
    if opcion == "1":
        show_recipe()
    elif opcion == "2":
        add_recipe()
    elif opcion == "3":
        create_category()
    elif opcion == "4":
        delete_recipe()
    elif opcion == "5":
        delete_category()
    letra = input("Presiona Enter tecla para continuar...")
    system("cls")
    opcion = menu()

print("¡Hasta luego!")
