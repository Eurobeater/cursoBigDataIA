mi_conjunto = set([1, 2, 3, 4, 5])
print(type(mi_conjunto))
print(mi_conjunto)

mi_conjunto = set({1, 2, 3, 4, 5})
print(type(mi_conjunto))
print(mi_conjunto)

mi_conjunto = {1, 2, 3, 4, 5}
print(type(mi_conjunto))
print(mi_conjunto)

mi_conjunto = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5}    #No pueden haber elementos repetidos en un conjunto. Devuelve 1, 2, 3, 4, 5
print(mi_conjunto)

#ERROR, no se puede acceder a un elemento por su índice porque los conjuntos no tienen índice
#print(mi_conjunto[0])

#ERROR, no se puede añadir listas, diccionarios ni conjuntos
#mi_conjunto = {1, [2, 3]}
#mi_conjunto = {1, {'2 : 3', '3: 4'}}
#mi_conjunto = {1, {2, 3}}

#Un conjunto puede contener tuplas
mi_conjunto = {1, (2, 3)}
print(mi_conjunto)

mi_conjunto = {1, 2, 3, 4, 5}
print(len(mi_conjunto))
print(2 in mi_conjunto)
print(6 in mi_conjunto)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)       #El 3 no se repite
print(s3)

s1.add(4)
print(s1)

s1.add(2)           #Como se esta añadiendo un valor repetido, la funcion add() no hace nada
print(s1)

s1.remove(2)        #Elimina el elemento 2 del conjunto
print(s1)

#ERROR, no se puede eliminar un elemento que no existe
#s1.remove(6)

s1.discard(6)       #Elimina el elemento 6 del conjunto y si no existe no da error a diferencia del remove
print(s1)

s1.pop()            #Elimina el primer elemento del conjunto. La funcion pop() tambien funciona en elementos
print(s1)

s1 = {1, 2, 3}      #Elimina el conjunto. Devuelve None
print(s1.clear())