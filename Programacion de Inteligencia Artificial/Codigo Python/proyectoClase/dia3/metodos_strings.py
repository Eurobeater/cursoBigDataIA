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

resultado = texto.find("s")     #Devuelve la posicion donde se encuentra la letra. Si no se encuentra, devuelve -1
print(resultado)

resultado = texto.find("el")     #Igual que el anterior, devuelve donde se encuentra la primera letra que se busca
print(resultado)

resultado = texto.find("y")     #Igual que el anterior, devuelve -1 porque no se encuentra la letra
print(resultado)

resultado = texto.find("e", 2, 10)      #Buscar la siguiente subcadena indicando que comience en la posición 2 y termine en la 10
print(resultado)

resultado = texto.replace("Federico", "Heriberto")  #Devuelve el mismo string, reemplazando lo que pone en el string por lo que se quiere cambiar
print(resultado)

resultado = texto.replace("e", "i")  #Lo mismo que el anterior, reemplaza las 'e' por las 'i'
print(resultado)

resultado = texto.count("e")    #Devuelve cuantas 'e' minusculas encuentra en el string
print(resultado)

resultado = len(texto)      #Devuelve la cantidad de caracteres en el string. A diferencia de otros lenguajes se utiliza asi
print(resultado)

