nombre = "Carina"

#Da error, porque las cadenas de texto son inmutables. Es decir, que no se pueden modificar directamente
#nombre[0] = "K"
#print(nombre)

apellido = "Pérez"
print(nombre + " " + apellido)
nombre1 = "Cari"
nombre2 = "na"
print(nombre1 + nombre2)

#Repetir una cadena de texto. Imprime 10 veces esa cadena. En POO se llama polimorfismo.
print(nombre2 * 10)

#Cadena de texto multilínea
poema = """En un lugar de la Mancha
de cuyo nombre no quiero acordarme
no ha mucho que vivía
un hidalgo de los de lanza en astillero"""
print(poema)

print("Mancha" in poema)    #Buscar la palabra en la cadena
print("Murcia" in poema)    #Igual que el anterior. Devuelve False

print(len(poema))