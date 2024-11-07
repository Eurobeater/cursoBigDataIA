lista = ['a', 'b', 'c']
indice = 0
for letra in lista:
    print(f"Letra {letra}: {indice}")
    indice +=1

# Usando enumerate
lista = ['a', 'b', 'c', 'd']
for item in enumerate(lista):       # Recorre un objeto que pueda ser enumerado
    print(item)

for indice, letra in enumerate (lista):
    print(f"Letra {letra}: {indice}")

# Usando range
for indice, item in enumerate(range(10, 20, 2)):
    print(f"{indice}: {item}")

# Transformando lista en tuplas
lista = ['a', 'b', 'c']
mis_tuplas = list(enumerate(lista))
print(mis_tuplas)

print(mis_tuplas[1][1])     # Imprime b