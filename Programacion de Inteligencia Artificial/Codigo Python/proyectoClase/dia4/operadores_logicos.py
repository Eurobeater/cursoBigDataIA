# Para realizar más de una comparación a la vez,
# podemos utilizar los operadores lógicos and, or y not.

mi_bool = 4 < 5 < 6
print(mi_bool)

mi_bool = 4 < 5 > 6         # 4 es menor que 5 y 6 es menor que 6
print(mi_bool)

mi_bool = 4 < 5 and 5 > 6   # Igual que el anterior
print(mi_bool)

mi_bool = 4 < 5 and 5 == 2 + 3
print(mi_bool)

mi_bool = (55 == 55) or (5 == 2 + 3)
print(mi_bool)

mi_bool = 4 < 5 and 'perro' == 'gato'
print(mi_bool)

mi_bool = 4 < 5 or 'perro' == 'gato'
print(mi_bool)

texto = 'Esta frase es breve'
mi_bool = 'frase' in texto
print(mi_bool)

mi_bool = 'frase' not in texto
print(mi_bool)

mi_bool = 'frase' in texto and 'breve' in texto
print(mi_bool)

mi_bool = 'frase' in texto and 'python' in texto
print(mi_bool)

mi_bool = not 5 == 5        # Negar que 5 == 5
print(mi_bool)

