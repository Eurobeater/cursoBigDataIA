miLista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(type(miLista))

otraLista = ['hola', 55, 6.1]       #En Java, explota
print(otraLista)

resultado = len(miLista)
print(resultado)

resultado = miLista[0]      #Devuelve lo que contiene el elemento 0 de la lista (Array)
print(resultado)

resultado = miLista[0:3]    #Devuelve ['a', 'b', 'c']
print(resultado)

resultado = miLista[3:]     #Devuelve ['d', 'e', 'f', 'g']
print(resultado)

miLista2 = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
print(miLista + miLista2)
print(miLista + miLista)    #Sale duplicada la lista miLista

miLista3 = miLista + miLista2
print(miLista3)

miLista3.pop(0)         #Extrae el valor del elemento 0 (a). Mutable, modifica la lista miLista3 a diferencia de los strings
print(miLista3)

miLista3.pop(1)         #Igual que el anterior. Se ha quitado anteriormente el elemento 0 y ahora se quita el elemento 1 (c) de la lista
print(miLista3)

miLista3.reverse()      #Poner la lista del revés
print(miLista3)