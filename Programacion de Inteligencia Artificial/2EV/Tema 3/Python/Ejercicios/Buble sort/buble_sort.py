def bubble_sort(lista, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

lista = [5, 3, 8, 1, 2]
n = len(lista)
bubble_sort(lista, n)
print("Lista ordenada:", lista)
