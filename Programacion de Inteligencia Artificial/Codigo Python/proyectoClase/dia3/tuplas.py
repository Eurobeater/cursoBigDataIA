miTupla = (1, 2, 3, 4, 5)       #Las tuplas a diferencia de las listas son inmutables, ocupan menos espacio en memoria y son más rápidas
print(type(miTupla))

miTupla = 1, 2, 3, 4, 5
print(type(miTupla))    #Devuelve tipo tupla

t = (5, 5.6, 'ff')      #Devuelve tipo tupla
print(type(t))

print(miTupla[0])
print(miTupla[-2])      #Devuelve dicho elemento de la tupla comenzando desde el final

#No se puede asignar un valor a una tupla (Es inmutable)
#miTupla[0] = 5

#Mismo error de antes, ni con el metodo append()
#miTupla.append(6)

miTupla = (1, 2, (10, 20), 4)      #Tupla anidada
print(miTupla[2])
print(miTupla[2][1])               #Acceder al valor de la tupla anidada

miTupla = list(miTupla)         #Pasarlo la tupla a lista
print(type(miTupla))

miTupla = tuple(miTupla)        #Pasar la lista a tupla
print(type(miTupla))

t = (1, 2, 3)
x, y, z = t             #Se asigna el valor a cada una de las variables utilizando la tupla guardada en la variable t
print(x, y, z)
print(x)

print(len(t))
t = (1, 2, 3, 1)        #Se añado un valor mas a la tupla
print(len(t))
print(t.count(1))       #Cuenta cuantos '1' hay en la tupla
print(t.index(2))       #Indica en qué lugar de la tupla se encuentra el valor '2'