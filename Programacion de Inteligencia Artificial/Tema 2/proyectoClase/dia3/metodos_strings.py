texto = "Este es el texto de Federico"
resultado = texto.upper()       #Pasarlo a mayus
print(resultado)

resultado = texto[2].upper()        #La variable texto es un objeto inmutable. No modifica el valor de la variable texto
print(resultado)        #Pasar el caracter a mayus

resultado = texto.lower()       #Pasarlo a minus
print(resultado)

resultado = texto.capitalize()  #Pone la primera mayúscula en cada sentencia. No pone la F de Federico en mayus porque está en la misma sentencia
print(resultado)

resultado = texto.split()       #Devuelve un array cuyos elementos son las palabras del string
print(resultado)

resultado = texto.split("t")    #Lo mismo que el anterior, pero sin añadir la letra t
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

resultado = " ".join ([a, b, c, d])     #Toma una lista de cadenas y las une en una sola cadena, separando cada una de ellas con lo que esté entre las comillas (Espacio en blanco, puede ser otro caracter).
print(resultado)