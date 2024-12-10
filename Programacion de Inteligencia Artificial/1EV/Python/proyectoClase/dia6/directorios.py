import os

ruta = os.getcwd()
print(ruta)

os.chdir("/home/maca/Escritorio/pruebas")
archivo = open('prueba.txt')
print(archivo.read())

# Tambien podemos crear directorios

os.mkdir("nuevo_directorio")
ruta2 = os.getcwd()
print(ruta2)

# Y cambiar de directorio

elemento = os.path.basename(ruta + "/prueba1.txt")
ruta3 = os.path.dirname(ruta + "/prueba1.txt")
print(ruta3, elemento)

elemento = os.path.split(ruta + "/prueba1.txt")
print(elemento)

# Podemos borrar un directorio
os.rmdir(ruta2 + "/nuevo_directorio")

# Para trabajar con rutas sin imoprtar el sistema operativo
from pathlib_doc import Path
print("Cambiando ruta con Path")
base_dir = os.path.join("Users", "carlos", "Desktop", "pruebas")
archivo_path = os.path.join(base_dir, "otro_archivo.txt")
print("-----------")
print(archivo_path)
archivo2 = open("f"/{archivo_path})
print(archivo2.read())