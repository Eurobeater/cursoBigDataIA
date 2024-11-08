def chequear_3_cifras(numero):
    return numero in range(100, 1000)

print(chequear_3_cifras(99))
print(chequear_3_cifras(100))
print(chequear_3_cifras(999))
print(chequear_3_cifras(1000))

suma = 586 + 402
print(chequear_3_cifras(suma))
print(chequear_3_cifras(586 + 402))

def chequear_3_cifras_v2(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass

print(chequear_3_cifras_v2([58, 99, 5860]))
print(type(chequear_3_cifras_v2([58, 99, 5860])))
print(chequear_3_cifras_v2([58, 99, 586]))
print(chequear_3_cifras_v2([586, 99, 586]))

def chequear_3_cifras_v3(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False

print(type(chequear_3_cifras_v3([58, 99, 5860])))
print(chequear_3_cifras_v3([58, 99, 5860]))

# Ahora queremos que devuelva una lista con todos los números de 3 c
def chequear_3_cifras_v4(lista):
    tres_cifras = []
    for n in lista:
        if n in range(100, 1000):
            tres_cifras.append(n)
    return tres_cifras

print(chequear_3_cifras_v4([58, 99, 5860]))
print(chequear_3_cifras_v4([581, 99, 5860]))

def anadir_3_cifras(lista, numero):
        if numero in range(100, 1000):
            lista.append(numero)
        return lista

def chequear_3_cifras_v5(lista):
    tres_cifras = []
    for n in lista:
        anadir_3_cifras(tres_cifras, n)
    return tres_cifras

print(chequear_3_cifras_v5([58, 99, 5860]))
print(chequear_3_cifras_v5([581, 99, 586]))