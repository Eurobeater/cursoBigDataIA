mitexto = "Esto es una prueba"
resultado = mitexto[0]
print(resultado)
resultado = mitexto[4]
print(resultado)
resultado = mitexto[9]
print(resultado)
resultado = mitexto[-4]
print(resultado)

resultado = mitexto.index('n')
print(resultado)
resultado = mitexto.index('n', 5)
print(resultado)
resultado = mitexto.index('e')
print(resultado)

#ERROR: no se encuentra la letra x
#resultado = mitexto.index('x')
#print(resultado)

resultado = mitexto.index('prueba')
print(resultado)

resultado = mitexto.index('a', 5)   #El 5 es para indicar desde qué posición hacer la búsqueda
print(resultado)

resultado = mitexto.index('a', 5, 11)   #El 11 es para indicar dónde acaba la búsqueda
print(resultado)

resultado = mitexto.rindex('a')     #Empieza a buscar por la derecha el caracter a
print(resultado)