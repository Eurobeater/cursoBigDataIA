lista = [1, 2, 3, 4]

for numero in lista:
    print(numero)       # Imprime desde 1 hasta 4

for numero in range(4):     # Imprime desde 0 hasta 4
    print(numero)

for numero in range(1, 5):  # Imprime desde 1 hasta 5 sin contar el 5
    print(numero)

for numero in range (10, 20, 2):    # Imprime desde 10 hasta 20 de dos en dos
    print(numero)

lista = list(range(10))
print(lista)