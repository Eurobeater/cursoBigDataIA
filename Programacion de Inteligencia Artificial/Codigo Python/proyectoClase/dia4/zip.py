nombres = ['Ana', 'Hugo', 'Valeria']
edades = [23, 45, 34]

combinados = zip(nombres, edades)   # Crear un objeto de tipo zip y la posición de la memoria donde está
print(combinados)
print(type(combinados))     # Imprime clase zip
print(list(combinados))     # Devuelve un array de dos dimensiones, donde el primero es el nombre y el segundo el array

nombres = ['Ana', 'Hugo', 'Valeria', 'Juan']
edades = [23, 45, 34]
print(list(zip(nombres, edades)))       # No aparece Juan

ciudades = ['Bogotá', 'Medellín', 'Cali']
#print(list(zip(nombres, edades, ciudades)))
combinados = list(zip(nombres, edades, ciudades))     # igual que el anterior, solo que se añade ciudad. Sigue sin tener en cuenta a Juan
print(combinados)

for nombre, edades, ciudad in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudad}")