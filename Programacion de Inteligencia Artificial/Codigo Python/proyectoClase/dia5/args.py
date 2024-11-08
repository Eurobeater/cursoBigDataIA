def suma(a, b):
    return a + b

print(suma(2, 3))

# Error
# print(suma(2, 3, 4))

def suma_v2(*args):      # Recibe cualquier cantidad de argumentos
    return sum(args)

print(suma_v2(2, 3))
print(suma_v2(2, 3, 4))
print(suma_v2(2, 3, 4, 5))

# def suma_v3():
