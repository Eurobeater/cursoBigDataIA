def selection_sort(lista, n):
    for i in range(n - 2):  # Iteramos desde 0 hasta n-2
        min_index = i  # Suponemos que el mínimo está en la posición i
        for j in range(i + 1, n):  # Buscamos el mínimo en el resto de la lista
            if lista[j] < lista[min_index]:
                min_index = j  # Actualizamos la posición del mínimo encontrado
        
        # Intercambiar el menor encontrado con el primer elemento no ordenado
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista  # Retornamos la lista ordenada

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
n = len(lista)
print("Lista original:", lista)
lista_ordenada = selection_sort(lista, n)
print("Lista ordenada:", lista_ordenada)
