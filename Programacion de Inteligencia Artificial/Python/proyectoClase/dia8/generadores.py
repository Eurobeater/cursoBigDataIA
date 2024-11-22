# Las funciones generadoras son funciones que contienen
# la palabra resersvada yield.
# Sirven para generar una secuencia de valores en lugar de devolver
# un único valor.
# Devuelven un objeto generador que es iterable.

# Veamos un ejemplo que diferencia entre una función normal y una generadora
def mi_funcion():
    return 4

def mi_generador():
    yield 4

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))

# Otro ejemplo trabajando con listas
def mi_funcion2():
    lista = []
    for x in range(1, 5):
        lista.append(x*10)
    return lista

def mi_generador2():
    for x in range(1, 5):
        yield x*10

print(mi_funcion2())
print(mi_generador2())

g = mi_generador2()
print(next(g))
print(next(g))
print(next(g))

# Otro ejemplo
def mi_generador3():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador3()
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) Error