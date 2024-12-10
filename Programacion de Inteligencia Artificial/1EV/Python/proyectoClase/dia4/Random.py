# Para importar una función de una librería de Python

from random import randint

from dia4.bucles_for import numero

aleatorio = randint(1, 50)
print(aleatorio)

# Para importar una librería completa de Python

from random import *

aleatorio = uniform(1, 5)   # Obtiene un número aleatorio en el rango cerrado en 'a' abierto en 'b'. Incluye 'a' pero no incluye 'b'
print(aleatorio)

aleatorio = round(uniform(1, 5), 2)     # Redondea a 2
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'rosa', 'morado', 'blanco']
color = choice(colores)
print(color)

numeros = list(range(5, 50, 5))     # Devuelve desde el primero hasta el último (sin incluir este) de 5 en 5. Si no se incluye el tercer parámetro va de uno en uno
print(numeros)

shuffle(numeros)        # Los mezcla, baraja
print(numeros)