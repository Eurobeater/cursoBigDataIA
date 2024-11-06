lista = ['a', 'b', 'c']
for letra in lista:
    print(letra)

for letra in lista:
    print('letra ' + letra)

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")