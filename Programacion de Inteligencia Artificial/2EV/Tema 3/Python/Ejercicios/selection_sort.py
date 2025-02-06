def selection_sort(lista, n):
    for i in range(n - 2):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista

lista = [64, 25, 12, 22, 11]
n = len(lista)
print("Lista original:", lista)
lista_ordenada = selection_sort(lista, n)
print("Lista ordenada:", lista_ordenada)
