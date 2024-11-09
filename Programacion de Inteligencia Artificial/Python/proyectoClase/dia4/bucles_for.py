lista = ['a', 'b', 'c']
for letra in lista:
    print(letra)

for letra in lista:
    print('letra ' + letra)

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

#----------------------------------------------------

numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

for letra in 'python':
    print(letra)

for letra in ('p','y','t','h','o','n'):
    print(letra)

for item in [[1,2], [3,4], [5,6]]:
    print(item)

for item, item2 in [[1,2], [3,4], [5,6]]:
    print(item)     # Imprime 1, 3, 5
    print(item2)    # Imprime 2, 4, 6
    print('----')

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for clave in dic:
    print(clave)

for clave in dic.items():       # Lista el contenido del diccionario ('clave1', 'a')
    print(clave)

for clave in dic.values():       # Lista los valores del diccionario (a, b, c)
    print(clave)

for a,b in dic.items():     # Imprime clave1 a
    print(a,b)