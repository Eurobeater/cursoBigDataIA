from pathlib import *

ruta_home = Path.home()
ruta_script = Path.cwd()

ruta_recetas = Path(Path.cwd(), 'Recetas')

#mostrar_recetas = Path.cwd().iterdir()

print(f"ruta_home: {ruta_home}")
print(f"ruta_script: {ruta_script}")
print(f"Ruta recetas: {ruta_recetas}")
print("")

print("Categorías:")

for categoria in Path(Path.cwd(), 'Recetas').iterdir():
    print(f"Categoría: {categoria.stem}")

print("")
lee_tipo_comida = input("Introduce el nombre de la categoria quieras listar: ")
lee_tipo_comida_path = Path(Path.cwd(), 'Recetas', lee_tipo_comida)
print(lee_tipo_comida_path)
print("")

print("Recetas:")
for receta in Path(Path.cwd(), 'Recetas', lee_tipo_comida).iterdir():
    print(f"Receta: {receta.stem}")

print("")
lee_receta = input("Introduce la receta que quieras leer: ")
lee_receta_path = Path(Path.cwd(), 'Recetas', lee_tipo_comida, lee_receta + ".txt")
print("")

print(lee_receta_path)
print(lee_receta_path.read_text())
print("")

print("Categorías:")

for categoria in Path(Path.cwd(), 'Recetas').iterdir():
    print(f"Categoría: {categoria.stem}")

print("")
add_tipo_comida = input("Introduce el nombre de la categoria quieras añadir: ")
add_tipo_comida_path = Path(Path.cwd(), 'Recetas', add_tipo_comida)
print(add_tipo_comida_path)
print("")

add_tipo_comida_path.mkdir()
print(add_tipo_comida_path)
print("")

for categoria in Path(Path.cwd(), 'Recetas').iterdir():
    print(f"Categoría: {categoria.stem}")