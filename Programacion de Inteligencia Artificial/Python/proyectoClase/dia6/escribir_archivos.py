archivo = open("prueba.txt", "r")       # Leer archivo

# No podemos escribir en un archivo que se abrió en modo lectura
# archivo.write("Hola mundo\n")

archivo.close()

# Para escribir en un archivo, necesitamos abrirlo en modo escritura
archivo = open("prueba1.txt", "w")
archivo.write("Hola mundo\n")
archivo.write("Adios mundo\n")
archivo.write("Mundo cruel, me voy\n")
archivo.close()

# Si abrimos un archivo en modo escritura, se sobrescribire el contenido
archivo = open("prueba1.txt", "w")
archivo.writelines(["Hola mundo\n", "Adios mundo\n", "Mundo cruel, me voy\n"])
archivo.close()

# Para agregar contenido a un archivo, necesitamos abrirlo
archivo = open("prueba1.txt", "a")
archivo.write("Soy el cuarto en discordia\n")
archivo.close()