minimo = min(58, 96, 72, 64, 35)
print(minimo)       # Imprime 35
maximo = max(58, 96, 72, 64, 35)
print(maximo)       # Imprime 96

lista = [58, 96, 72, 64, 35]
print(min(lista))
print(max(lista))

print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ['Ana', 'Hugo', 'Valeria', 'Juan']
print(min(nombres))     # Imprime Ana. Por órden alfabético

nombre = 'Federico'
print(min(nombre))      # Ordena alfabéticamente en ASCII
print(max(nombre))      # Ordena alfabéticamente en ASCII

nombre = 'federico'
print(min(nombre))      # Ordena alfabéticamente en ASCII
print(max(nombre))      # Ordena alfabéticamente en ASCII

print(min(nombre.lower()))      # Devuelve c

dic = {'c1': 45, 'c2': 11}
print(min(dic))         # Imprime c1, por la ordenación alfabética de la claves, no por la posición

