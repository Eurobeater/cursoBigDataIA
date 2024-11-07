palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Usando compresión de listas
lista = [letra for letra in palabra]        # Lo mismo que el for de la linea 5
print(lista)

lista2 = [numero for numero in range(0,10)]      # La lista va a estar compuesta por los valores de número los cuales se indican en esta misma línea
print(lista2)

lista3 = [numero for numero in range(0,21) if numero % 2 == 0]
print(lista3)

lista4 = [numero /2 for numero in range(0,11)]
print(lista4)

lista5 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista5)

pies = [10, 20, 30, 40, 50]

lista6 = [pie / 3.281 for pie in pies]
print(lista6)

cuadrados = [n**2 for n in range(0,11)]
print(cuadrados)